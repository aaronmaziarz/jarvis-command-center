#!/usr/bin/env python3
import re

# Read the new section
with open('new_section.txt', 'r') as f:
    new_section = f.read()

# Read the dashboard
with open('dashboard.html', 'r') as f:
    content = f.read()

# Find and replace the AGENT SWARM section
# The section starts with "      <!--" and ends with "      </div>"
old_start = '      <!-- ═══════════════════════════════════════════════════════════════════════\n           AGENT SWARM'
# Find where the old section ends - the closing </div> of the span-8 card
old_pattern = r'      <!-- ═══════════════════════════════════════════════════════════════════════\n           AGENT SWARM\n      ═══════════════════════════════════════════════════════════════════════ -->\s*<div class="card span-8">.*?</div>\s*</div>\s*'

new_content = re.sub(old_pattern, new_section, content, flags=re.DOTALL)

# Write back
with open('dashboard.html', 'w') as f:
    f.write(new_content)

print("Replacement done!")
