#!/usr/bin/env python3
"""
Script to completely fix ALL Mermaid diagrams across all modules for GitHub compatibility.
This takes a more aggressive approach to ensure diagrams render properly.
"""

import os
import re
import glob
import sys

def fix_mermaid_completely(file_path):
    """Fix Mermaid diagrams in a Markdown file by completely simplifying them."""
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all Mermaid code blocks
    mermaid_blocks = re.findall(r'```mermaid\s*(.*?)```', content, re.DOTALL)
    
    for i, block in enumerate(mermaid_blocks):
        # Create a fixed version by removing problematic content
        
        # Remove all **Note:** occurrences
        fixed_block = re.sub(r'\*\*Note:\*\*\s*', '', block)
        
        # Fix flowchart syntax by simplifying arrows
        fixed_block = re.sub(r'-->\s*.*?\[', r'--> [', fixed_block)
        
        # Fix quadrantChart syntax
        fixed_block = re.sub(r'(x-axis.*?-->).*?(.*?)$', r'\1 \2', fixed_block, flags=re.MULTILINE)
        fixed_block = re.sub(r'(y-axis.*?-->).*?(.*?)$', r'\1 \2', fixed_block, flags=re.MULTILINE)
        
        # Remove any other potential Markdown formatting within the diagram
        fixed_block = re.sub(r'\*\*(.*?)\*\*', r'\1', fixed_block)
        
        # Simplify syntax for GitHub
        fixed_block = re.sub(r'(\w+)\s*-\.->\s*', r'\1 -.-> ', fixed_block)
        fixed_block = re.sub(r'(\w+)\s*==>\s*', r'\1 --> ', fixed_block)
        
        # Replace the original block with the fixed one
        content = content.replace(mermaid_blocks[i], fixed_block)
    
    # Write the fixed content back to the file
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    """Main function to fix Mermaid diagrams in all markdown files."""
    module_dir = "/Users/mattysquarzoni/Library/Mobile Documents/com~apple~CloudDocs/Projects-AI/Vibe_businessplanning/VibeBusinessPlanning"
    
    # Process all Markdown files in the directory
    markdown_files = glob.glob(os.path.join(module_dir, "Module *.md"))
    
    for file_path in markdown_files:
        fix_mermaid_completely(file_path)
    
    print("All Mermaid diagrams have been completely fixed for GitHub compatibility.")

if __name__ == "__main__":
    main()
