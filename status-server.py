#!/usr/bin/env python3
"""
Simple HTTP server that serves Jarvis agent status JSON.
Polls OpenClaw gateway and subagent data to provide real-time status.
"""

import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import subprocess

# Configuration
PORT = 18790  # Separate from gateway (18789)
OPENCLAW_DIR = os.path.expanduser("~/.openclaw")
SUBAGENTS_FILE = os.path.join(OPENCLAW_DIR, "subagents", "runs.json")
GATEWAY_TOKEN = "97781c1ffe55cb0248394b17708c3913ed3ff367bc212bf0"

# Budget tracking (simple file-based)
BUDGET_FILE = os.path.join(OPENCLAW_DIR, "budget.json")


def get_budget():
    """Read current budget from file."""
    if os.path.exists(BUDGET_FILE):
        try:
            with open(BUDGET_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"remaining": 20.00, "monthly_limit": 20.00, "spent": 0.00}


def get_gateway_status():
    """Get status from OpenClaw gateway."""
    try:
        result = subprocess.run(
            ["openclaw", "gateway", "call", "status", "--json", "--token", GATEWAY_TOKEN],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception as e:
        print(f"Gateway status error: {e}", file=sys.stderr)
    return {}


def get_subagent_runs():
    """Get subagent runs from file."""
    if os.path.exists(SUBAGENTS_FILE):
        try:
            with open(SUBAGENTS_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"runs": {}}


def build_status_response():
    """Build the complete status JSON response."""
    budget = get_budget()
    gateway = get_gateway_status()
    subagents = get_subagent_runs()
    
    # Determine active subagents
    active_runs = []
    for run_id, run_data in subagents.get("runs", {}).items():
        active_runs.append({
            "runId": run_id,
            "label": run_data.get("label", "Unknown"),
            "task": run_data.get("task", "")[:100],
            "createdAt": run_data.get("createdAt"),
            "startedAt": run_data.get("startedAt"),
            "model": run_data.get("model", ""),
            "requesterOrigin": run_data.get("requesterOrigin", {})
        })
    
    # Count sessions by type
    sessions = gateway.get("sessions", {})
    recent_sessions = sessions.get("recent", [])
    
    # Build active agent statuses
    agents = {
        "researcher": {"status": "idle", "task": "", "completed": 0, "failed": 0},
        "coder": {"status": "idle", "task": "", "completed": 0, "failed": 0},
        "writer": {"status": "offline", "task": "Coming in Phase 2", "completed": 0, "failed": 0},
        "analyst": {"status": "offline", "task": "Coming in Phase 2", "completed": 0, "failed": 0}
    }
    
    # Check active runs to update agent statuses
    for run in active_runs:
        label = run.get("label", "")
        task = run.get("task", "")
        
        if "researcher" in label.lower() or "research" in label.lower():
            agents["researcher"] = {"status": "working", "task": task, "completed": 1, "failed": 0}
        elif "coder" in label.lower() or "code" in label.lower():
            agents["coder"] = {"status": "working", "task": task, "completed": 0, "failed": 0}
        elif "writer" in label.lower():
            agents["writer"] = {"status": "active", "task": task, "completed": 0, "failed": 0}
        elif "analyst" in label.lower() or "analy" in label.lower():
            agents["analyst"] = {"status": "active", "task": task, "completed": 0, "failed": 0}
    
    # Find the "main" session (your chat with Jarvis)
    main_session = None
    subagent_sessions = []
    for s in recent_sessions:
        if s.get("key", "").endswith(":direct:5853257853"):
            main_session = s
        elif "subagent" in s.get("key", ""):
            subagent_sessions.append(s)
    
    # Calculate active count
    active_count = len([a for a in agents.values() if a["status"] in ("active", "working")])
    
    response = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "jarvis": {
            "status": "online",
            "context": "Ready for commands" if main_session else "Initializing..."
        },
        "budget": {
            "remaining": budget.get("remaining", 20.00),
            "monthly_limit": budget.get("monthly_limit", 20.00),
            "spent": budget.get("spent", 0.00)
        },
        "model": "M2.5",
        "sessions": {
            "active": len(recent_sessions),
            "direct_chat": main_session is not None,
            "context_usage": main_session.get("percentUsed", 0) if main_session else 0
        },
        "agents": agents,
        "active_runs": active_runs,
        "active_agent_count": active_count
    }
    
    return response


class StatusHandler(BaseHTTPRequestHandler):
    """HTTP handler for status endpoint."""
    
    def log_message(self, format, *args):
        """Suppress default logging."""
        pass
    
    def do_GET(self):
        if self.path in ("/status.json", "/api/status"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            
            status = build_status_response()
            self.wfile.write(json.dumps(status, indent=2).encode())
            
        elif self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


def main():
    """Start the status server."""
    server = HTTPServer(("0.0.0.0", PORT), StatusHandler)
    print(f"🚀 Jarvis Status Server running on http://0.0.0.0:{PORT}/status.json")
    print(f"   Gateway token configured: {GATEWAY_TOKEN[:8]}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
