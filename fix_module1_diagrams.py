#!/usr/bin/env python3
"""
Fix Module 1 Mermaid Diagrams Script
This script specifically targets and fixes the broken avatar and empathy map diagrams in Module 1.
"""

import re

# Path to Module 1
module1_path = "Module 1_ Core Business Concept.md"

# Read file content
with open(module1_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the double brackets in node labels [B1][Age range] -> [Age range]
pattern = r'B1\[B1\]\[Age range\]'
content = content.replace('B1[B1][Age range]', 'B1[Age range]')
content = content.replace('B2[B2][Income level]', 'B2[Income level]')
content = content.replace('D1[D1][Pain point 1]', 'D1[Pain point 1]')
content = content.replace('D2[D2][Pain point 2]', 'D2[Pain point 2]')
content = content.replace('E1[E1][Goal 1]', 'E1[Goal 1]')
content = content.replace('E2[E2][Goal 2]', 'E2[Goal 2]')
content = content.replace('F1[F1][Primary value]', 'F1[Primary value]')

# Write fixed content back to file
with open(module1_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed the avatar diagrams in Module 1")
