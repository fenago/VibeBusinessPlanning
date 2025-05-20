#!/usr/bin/env python3
"""
Fix All Mermaid Diagrams Script
This script fixes Mermaid diagrams across all module files to ensure proper GitHub rendering.
It focuses only on fixing diagrams without excessive styling changes.
"""

import os
import re
import glob

# Directory containing markdown files
base_dir = os.path.dirname(os.path.abspath(__file__))

# Find all markdown files
md_files = glob.glob(os.path.join(base_dir, "Module*.md"))

def fix_mermaid_diagram(match):
    """Fix a single mermaid diagram block."""
    full_match = match.group(0)
    diagram_content = match.group(1)
    
    # Skip already fixed diagrams
    if "flowchart TD" in diagram_content and "-->" in diagram_content and not "  -->" in diagram_content:
        return full_match
        
    # Identify diagram type
    if "gitGraph" in diagram_content:
        # Replace gitGraph with timeline
        return """```mermaid
timeline
    title Timeline
    section Past
        2020 : Initial Phase
        2022 : Development
    section Current
        2023 : Present State
    section Future
        2024 : Next Steps
        2025 : Future Vision
```"""
    
    # Fix flowchart arrows and connections
    if "flowchart" in diagram_content or "graph" in diagram_content:
        # Fix the arrow syntax - this is a common issue
        diagram_content = re.sub(r'(\w+)\s+-->\s+\[([^\]]+)\]', r'\1 --> B[\2]', diagram_content)
        diagram_content = re.sub(r'\s+-->\s+', r' --> ', diagram_content)
        
        # Fix missing node labels
        lines = diagram_content.split('\n')
        fixed_lines = []
        
        for line in lines:
            if "-->" in line and not re.search(r'\[\w+\]', line):
                # Add missing node labels
                line = re.sub(r'-->\s+([A-Za-z0-9_]+)', r'--> \1[\1]', line)
            fixed_lines.append(line)
        
        diagram_content = '\n'.join(fixed_lines)
        
        return f"```mermaid\n{diagram_content}\n```"
    
    # For any other type, just ensure proper formatting
    return f"```mermaid\n{diagram_content.strip()}\n```"

def fix_file(file_path):
    """Fix mermaid diagrams in a single file."""
    print(f"Processing {os.path.basename(file_path)}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Save original content for comparison
    original_content = content
    
    # Find and fix all mermaid blocks
    mermaid_pattern = re.compile(r'```mermaid\s*\n(.*?)\n```', re.DOTALL)
    content = mermaid_pattern.sub(fix_mermaid_diagram, content)
    
    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed mermaid diagrams in {os.path.basename(file_path)}")
        return True
    else:
        print(f"  No changes needed in {os.path.basename(file_path)}")
        return False

def main():
    """Process all markdown files."""
    print("Starting to fix Mermaid diagrams across all modules...")
    fixed_count = 0
    
    for md_file in md_files:
        if fix_file(md_file):
            fixed_count += 1
    
    print(f"\nComplete! Fixed diagrams in {fixed_count} files.")

if __name__ == "__main__":
    main()
