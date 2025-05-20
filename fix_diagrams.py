#!/usr/bin/env python3
"""
Script to fix Mermaid diagrams by removing all **Note:** text that breaks the syntax.
"""

import os
import re
import glob

def fix_mermaid_diagrams(file_path):
    """Fix Mermaid diagrams in a Markdown file."""
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all Mermaid code blocks
    pattern = r'```mermaid\s*(.*?)```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for match in matches:
        # Create a fixed version by removing all **Note:** occurrences
        fixed_match = re.sub(r'\*\*Note:\*\*\s*', '', match)
        
        # Replace the original match with the fixed version
        content = content.replace(match, fixed_match)
    
    # Write the fixed content back to the file
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    """Main function to fix Mermaid diagrams in all markdown files."""
    module_dir = "/Users/mattysquarzoni/Library/Mobile Documents/com~apple~CloudDocs/Projects-AI/Vibe_businessplanning/VibeBusinessPlanning"
    
    # Process all Markdown files in the directory
    markdown_files = glob.glob(os.path.join(module_dir, "Module *.md"))
    
    for file_path in markdown_files:
        fix_mermaid_diagrams(file_path)
    
    print("All Mermaid diagrams have been fixed.")

if __name__ == "__main__":
    main()
