#!/usr/bin/env python3
"""
Targeted GitHub Mermaid Diagram Fix Script
This script specifically fixes the problematic diagrams visible in the screenshots.
"""

import os
import re
import glob

# Directory containing markdown files
base_dir = os.path.dirname(os.path.abspath(__file__))

# Find all markdown files
md_files = glob.glob(os.path.join(base_dir, "*.md"))

def fix_module1_mindmap(file_path):
    """Fix the mindmap diagram in Module 1."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the problematic mindmap diagram with a fixed version
    mindmap_pattern = re.compile(r'```mermaid\s*\n\s*mindmap(.*?)```', re.DOTALL)
    
    def fix_mindmap(match):
        mindmap_content = match.group(1).strip()
        fixed_content = """```mermaid
mindmap
    root((Avatar Name))
        Demographics
            Age range
            Income level
            Education
            Location
        Psychographics
            Values
            Beliefs
            Interests
        Pains
            Pain point 1
            Pain point 2
        Goals
            Goal 1
            Goal 2
        Currency
            Primary value
```"""
        return fixed_content
    
    content = mindmap_pattern.sub(fix_mindmap, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def fix_value_proposition(file_path):
    """Fix the value proposition diagram that appears in Module 1."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the problematic value proposition diagram
    value_prop_pattern = re.compile(r'Example diagram:.*?\n```mermaid.*?\n.*?-->\s*.*?\n.*?```', re.DOTALL)
    
    def fix_value_prop(match):
        match_content = match.group(0)
        
        # Create a completely new, properly formatted diagram
        fixed_content = """Example diagram:

```mermaid
graph LR
    A[Customer Need] --> B[Your Solution]
    B --> C[Key Benefit 1]
    B --> D[Key Benefit 2]
    B --> E[Key Benefit 3]
```"""
        return fixed_content
    
    # Only replace if pattern is found
    if value_prop_pattern.search(content):
        content = value_prop_pattern.sub(fix_value_prop, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def fix_all_diagrams(file_path):
    """Fix all Mermaid diagrams with clean syntax."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match mermaid blocks that need fixing
    mermaid_pattern = re.compile(r'```mermaid\s*\n(.*?)\n```', re.DOTALL)
    
    def clean_diagram(match):
        diagram_content = match.group(1).strip()
        
        # Remove any problematic syntax or characters
        diagram_content = re.sub(r'Note:.*?\n', '', diagram_content)
        
        # Fix common issues
        
        # Fix arrows
        diagram_content = re.sub(r'-->', '-->', diagram_content)
        
        # Fix subgraphs with quotes
        diagram_content = re.sub(r'subgraph\s+"([^"]+)"', r'subgraph \1', diagram_content)
        
        # Fix missing newlines for proper structure
        lines = diagram_content.split('\n')
        clean_lines = []
        
        for line in lines:
            # Make sure all lines are properly indented and formatted
            clean_line = line.strip()
            if clean_line:
                clean_lines.append(clean_line)
        
        # Rejoin with clean formatting
        clean_content = '\n'.join(clean_lines)
        
        return f"```mermaid\n{clean_content}\n```"
    
    # Apply the fix
    new_content = mermaid_pattern.sub(clean_diagram, content)
    
    # Only write if changes were made
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    """Main function to process all markdown files."""
    print("Starting targeted Mermaid diagram fixes...")
    
    for md_file in md_files:
        file_name = os.path.basename(md_file)
        print(f"Processing {file_name}...")
        
        # Apply specific fixes based on file
        if "Module 1_" in file_name:
            if fix_module1_mindmap(md_file):
                print(f"  Fixed mindmap in {file_name}")
            if fix_value_proposition(md_file):
                print(f"  Fixed value proposition diagram in {file_name}")
        
        # Apply general fixes to all files
        if fix_all_diagrams(md_file):
            print(f"  Applied general diagram fixes to {file_name}")
    
    print("\nComplete! Fixed targeted diagrams across all modules.")

if __name__ == "__main__":
    main()
