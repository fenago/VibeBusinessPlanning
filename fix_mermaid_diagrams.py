#!/usr/bin/env python3
"""
Script to fix Mermaid diagram syntax in Markdown files to ensure GitHub compatibility.
"""

import os
import re
import glob

def fix_mermaid_diagrams(file_path):
    """Fix Mermaid diagrams in a Markdown file for GitHub compatibility."""
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all Mermaid code blocks
    mermaid_blocks = re.findall(r'```mermaid\s*(.*?)```', content, re.DOTALL)
    
    # Process each Mermaid block
    for block in mermaid_blocks:
        # Remove the "**Note:**" text that was erroneously added to Mermaid diagrams
        fixed_block = re.sub(r'\*\*Note:\*\*\s*', '', block)
        
        # Fix quadrantChart syntax to ensure it works on GitHub
        fixed_block = re.sub(r'(x-axis.*?-->)\s*.*?(.*?)$', r'\1 \2', fixed_block, flags=re.MULTILINE)
        fixed_block = re.sub(r'(y-axis.*?-->)\s*.*?(.*?)$', r'\1 \2', fixed_block, flags=re.MULTILINE)
        
        # Replace the original block with the fixed one
        content = content.replace(block, fixed_block)
    
    # Write the fixed content back to the file
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    """Main function to fix Mermaid diagrams in all markdown files."""
    module_dir = "/Users/mattysquarzoni/Library/Mobile Documents/com~apple~CloudDocs/Projects-AI/Vibe_businessplanning/VibeBusinessPlanning"
    
    # Process all Markdown files in the directory
    markdown_files = glob.glob(os.path.join(module_dir, "Module *.md"))
    
    for file_path in markdown_files:
        # Skip the README
        if "README" not in file_path:
            fix_mermaid_diagrams(file_path)
    
    print("All Mermaid diagrams have been fixed for GitHub compatibility.")

if __name__ == "__main__":
    main()
