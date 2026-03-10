#!/usr/bin/env python3
import re

with open('dashboard.html', 'r') as f:
    content = f.read()

# Pattern to find the old AGENT SWARM section
old_pattern = r'<!--\s+══════════════════════════════════════════════════════════════════════\s+AGENT SWARM\s+══════════════════════════════════════════════════════════════════════\s+-->\s+<div class="card span-8">.*?</div>\s*</div>\s*(?=<!--|$)'

new_section = '''<!-- ═══════════════════════════════════════════════════════════════════════
           AGENT COMMAND CENTER
      ═══════════════════════════════════════════════════════════════════════ -->
      <div class="card span-8">
        <div class="card-header">
          <span class="card-title">Command Center</span>
          <span class="card-icon">🎛️</span>
        </div>
        
        <!-- RESEARCH ZONE -->
        <div class="zone-header">
          <div class="zone-indicator research"></div>
          <span class="zone-title">Research Zone</span>
          <div class="zone-line"></div>
        </div>
        <div class="workstation-row">
          <div class="workstation ready" data-agent="researcher" onclick="openAgentModal('researcher')">
            <div class="ws-monitor">
              <div class="ws-header">
                <div class="ws-agent-info">
                  <div class="ws-avatar">🤡</div>
                  <div class="ws-name-role">
                    <div class="ws-name">Researcher</div>
                    <div class="ws-role">Web search & analysis</div>
                  </div>
                </div>
                <div class="ws-status-light">
                  <div class="ws-led"></div>
                  <span>Ready</span>
                </div>
              </div>
            </div>
            <div class="ws-desk">
              <div class="ws-task">— DeepSeek R1 —</div>
              <div class="ws-stats">
                <div class="ws-stat">✓ 2 completed</div>
                <div class="ws-stat">⏱️ 2h 15m</div>
              </div>
              <div class="ws-desk-items">
                <div class="desk-item">🔍</div>
                <div class="desk-item">📄</div>
                <div class="desk-item">📊</div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- DEVELOPMENT ZONE -->
        <div class="zone-header">
          <div class="zone-indicator development"></div>
          <span class="zone-title">Development Zone</span>
          <div class="zone-line"></div>
        </div>
        <div class="workstation-row">
          <div class="workstation ready" data-agent="coder" onclick="openAgentModal('coder')">
            <div class="ws-monitor">
              <div class="ws-header">
                <div class="ws-agent-info">
                  <div class="ws-avatar">💻</div>
                  <div class="ws-name-role">
                    <div class="ws-name">Coder</div>
                    <div class="ws-role">Python, SQL & automation</div>
                  </div>
                </div>
                <div class="ws-status-light">
                  <div class="ws-led"></div>
                  <span>Ready</span>
                </div>
              </div>
            </div>
            <div class="ws-desk">
              <div class="ws-task">— Qwen2.5 Coder —</div>
              <div class="ws-stats">
                <div class="ws-stat">✓ 1 completed</div>
                <div class="ws-stat">⏱️ 1h 45m</div>
              </div>
              <div class="ws-desk-items">
                <div class="desk-item">🐍</div>
                <div class="desk-item">🗄️</div>
                <div class="desk-item">⚙️</div>
              </div>
            </div>
          </div>
          
          <div class="workstation" data-agent="frontend" onclick="openAgentModal('frontend')">
            <div class="ws-monitor">
              <div class="ws-header">
                <div class="ws-agent-info">
                  <div class="ws-avatar">🎨</div>
                  <div class="ws-name-role">
                    <div class="ws-name">Frontend</div>
                    <div class="ws-role">UI/UX & dashboard</div>
                  </div>
                </div>
                <div class="ws-status-light">
                  <div class="ws-led"></div>
                  <span>Ready</span>
                </div>
              </div>
            </div>
            <div class="ws-desk">
              <div class="ws-task">— Claude Sonnet 4.6 —</div>
              <div class="ws-stats">
                <div class="ws-stat">✓ 1 completed</div>
                <div class="ws-stat">⏱️ 45m</div>
              </div>
              <div class="ws-desk-items">
                <div class="desk-item">🎛️</div>
                <div class="desk-item">📐</div>
                <div class="desk-item">✨</div>
              </div>
            </div>
          </div>
          
          <div class="workstation" data-agent="security" onclick="openAgentModal('security')">
            <div class="ws-monitor">
              <div class="ws-header">
                <div class="ws-agent-info">
                  <div class="ws-avatar">🛡️</div>
                  <div class="ws-na}