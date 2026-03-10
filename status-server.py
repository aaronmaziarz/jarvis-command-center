#!/usr/bin/env python3
"""
Simple HTTP server that serves Jarvis agent status JSON.
Polls OpenClaw gateway and subagent data to provide real-time status.
"""

import json

def get_openrouter_usage():
    """Get real usage from OpenRouter API"""
    import requests
    import os
    
    # Try to get API key from config
    config_path = os.path.expanduser('~/.openclaw/agents/main/agent/models.json')
    api_key = None
    
    try:
        import json
        with open(config_path, 'r') as f:
            config = json.load(f)
            api_key = config.get('default', {}).get('key')
    except:
        pass
    
    if not api_key:
        return None
    
    try:
        resp = requests.get(
            f"https://openrouter.ai/api/v1/usage?date=2026-03",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=5
        )
        if resp.status_code == 200:
            data = resp.json()
            return {
                "total_spend": data.get("total_spend", 0),
                "currency": data.get("currency", "USD"),
                "requests": data.get("total_requests", 0)
            }
    except:
        pass
    
    return None

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



def get_kpis():
    """Get KPI metrics"""
    import os
    from datetime import datetime
    
    # Count tasks completed today
    today = datetime.now().strftime('%Y-%m-%d')
    memory_dir = os.path.expanduser('~/.openclaw/workspace/memory')
    tasks_today = 0
    
    try:
        daily_file = os.path.join(memory_dir, f'{today}.md')
        if os.path.exists(daily_file):
            with open(daily_file, 'r') as f:
                tasks_today = f.read().count('✓')
    except:
        pass
    
    # Count total tasks from agent states
    import json

def get_openrouter_usage():
    """Get real usage from OpenRouter API"""
    import requests
    import os
    
    # Try to get API key from config
    config_path = os.path.expanduser('~/.openclaw/agents/main/agent/models.json')
    api_key = None
    
    try:
        import json
        with open(config_path, 'r') as f:
            config = json.load(f)
            api_key = config.get('default', {}).get('key')
    except:
        pass
    
    if not api_key:
        return None
    
    try:
        resp = requests.get(
            f"https://openrouter.ai/api/v1/usage?date=2026-03",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=5
        )
        if resp.status_code == 200:
            data = resp.json()
            return {
                "total_spend": data.get("total_spend", 0),
                "currency": data.get("currency", "USD"),
                "requests": data.get("total_requests", 0)
            }
    except:
        pass
    
    return None

    agent_states_file = os.path.join(memory_dir, 'agent-states.json')
    total_tasks = 0
    active_agents = 0
    
    try:
        if os.path.exists(agent_states_file):
            with open(agent_states_file, 'r') as f:
                states = json.load(f)
                for agent, data in states.items():
                    total_tasks += data.get('tasks_completed', 0)
                    if data.get('status') in ['active', 'working']:
                        active_agents += 1
    except:
        pass
    
    return {
        "tasksTotal": total_tasks,
        "tasksToday": tasks_today,
        "agentsActive": active_agents,
        "tasksPending": 2  # Could track from task list
    }


def get_budget():
    """Get budget with actual spending"""
    import os
    import json

def get_openrouter_usage():
    """Get real usage from OpenRouter API"""
    import requests
    import os
    
    # Try to get API key from config
    config_path = os.path.expanduser('~/.openclaw/agents/main/agent/models.json')
    api_key = None
    
    try:
        import json
        with open(config_path, 'r') as f:
            config = json.load(f)
            api_key = config.get('default', {}).get('key')
    except:
        pass
    
    if not api_key:
        return None
    
    try:
        resp = requests.get(
            f"https://openrouter.ai/api/v1/usage?date=2026-03",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=5
        )
        if resp.status_code == 200:
            data = resp.json()
            return {
                "total_spend": data.get("total_spend", 0),
                "currency": data.get("currency", "USD"),
                "requests": data.get("total_requests", 0)
            }
    except:
        pass
    
    return None

    
    budget_file = os.path.expanduser('~/.openclaw/budget.json')
    monthly_limit = 20.00  # $20/month
    
    spent = 0.00
    
    # Try to read from agent run logs
    try:
        runs_dir = os.path.expanduser('~/.openclaw/subagents/runs')
        if os.path.exists(runs_dir):
            for f in os.listdir(runs_dir):
                if f.endswith('.json'):
                    with open(os.path.join(runs_dir, f), 'r') as rf:
                        data = json.load(rf)
                        # Estimate cost from tokens
                        tokens = data.get('total_tokens', 0)
                        # Rough estimate: $1 per million tokens average
                        spent += (tokens / 1_000_000) * 1.0
    except:
        pass
    
    # Also check sessions for usage
    sessions_dir = os.path.expanduser('~/.openclaw/agents/main/sessions')
    if os.path.exists(sessions_dir):
        for f in os.listdir(sessions_dir):
            if f.endswith('.jsonl'):
                try:
                    with open(os.path.join(sessions_dir, f), 'r') as rf:
                        # Rough estimation from file size
                        size = os.path.getsize(os.path.join(sessions_dir, f))
                        spent += (size / 1_000_000) * 0.5  # Rough estimate
                except:
                    pass
    
    remaining = max(0, monthly_limit - spent)
    
    return {
        "remaining": round(remaining, 2),
        "openrouter": get_openrouter_usage(),
        "monthly_limit": monthly_limit,
        "spent": round(spent, 2),
        "percent_used": round((spent / monthly_limit) * 100, 1) if monthly_limit > 0 else 0
    }


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
