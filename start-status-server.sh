#!/bin/bash
# Start Jarvis Status Server
# Usage: ./start-status-server.sh

cd "$(dirname "$0")"

echo "Starting Jarvis Status Server..."
python3 status-server.py &
echo "Server started on port 18790"
echo ""
echo "To view dashboard with live updates, use:"
echo "  dashboard.html?statusUrl=http://localhost:18790"
echo ""
echo "For remote access (from another machine):"
echo "  1. Find your local IP: hostname -I | awk '{print \$1}'"
echo "  2. Use: dashboard.html?statusUrl=http://YOUR_IP:18790"
