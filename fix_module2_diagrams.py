#!/usr/bin/env python3
"""
Fix Module 2 Mermaid Diagrams Script
This script specifically targets and fixes the broken diagrams in Module 2.
"""

import re

# Path to Module 2
module_path = "Module 2_ Solution & Products (Part 1 of 2).md"

# Read file content
with open(module_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix missing node labels for destinations
content = content.replace('A[Milestone 1] --> [Milestone 2]', 'A[Milestone 1] --> B[Milestone 2]')
content = content.replace('A[Entry Level] --> [Mid Level]', 'A[Entry Level] --> B[Mid Level]')

# Fix double brackets in node labels
content = content.replace('B --> B[B][Milestone 3]', 'B --> C[Milestone 3]')
content = content.replace('C --> B[B][Milestone 4]', 'C --> D[Milestone 4]')
content = content.replace('D --> B[B][Final Outcome]', 'D --> E[Final Outcome]')
content = content.replace('B --> B[B][Premium Level]', 'B --> C[Premium Level]')

# Fix arrow spacing 
content = content.replace('B  -.->  E', 'B -.-> E')

# Write fixed content back to file
with open(module_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed the Mermaid diagrams in Module 2")
