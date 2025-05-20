#!/usr/bin/env python3
"""
Script to fix GitHub compatibility issues in Markdown files.
This script removes custom HTML/CSS elements and replaces them with GitHub-compatible Markdown.
"""

import os
import re
import glob

def fix_file(file_path):
    """Fix GitHub compatibility issues in a Markdown file."""
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix border-left div sections (intro sections)
    content = re.sub(
        r'<div style="border-left: 4px solid #[0-9A-F]+; background-color: #[0-9A-F]+; padding: [0-9]+px; margin-bottom: [0-9]+px;">\s*\n*\s*\n*## (.*?)\s*\n*\s*\n*> (.*?)\s*\n*\s*\n*</div>',
        r'## \1\n\n> **Note:** \2',
        content,
        flags=re.DOTALL
    )
    
    # Fix border div sections (user input and LLM instructions)
    content = re.sub(
        r'<div style="border: 1px solid #[0-9A-F]+; border-radius: [0-9]+px; padding: [0-9]+px; margin: [0-9]+px 0; background-color: #[0-9A-F]+;">\s*\n*\s*\n*## (.*?)\s*\n*',
        r'## \1\n',
        content,
        flags=re.DOTALL
    )
    
    # Fix colored span elements
    content = re.sub(
        r'<span style="color: #[0-9A-F]+;">(.*?)</span>',
        r'**\1**',
        content,
        flags=re.DOTALL
    )
    
    # Fix closing div tags followed by another div tag
    content = re.sub(
        r'</div>\s*\n*\s*\n*<div style=".*?">',
        r'\n---\n',
        content,
        flags=re.DOTALL
    )
    
    # Fix remaining div closing tags
    content = re.sub(
        r'</div>',
        r'',
        content
    )
    
    # Fix styling for note sections
    content = re.sub(
        r'> ([^*])',
        r'> **Note:** \1',
        content
    )
    
    # Add horizontal rule after sections
    content = re.sub(
        r'(YOUR INPUT: .*?)\s*\n\s*\n(?!---)',
        r'\1\n\n---\n\n',
        content,
        flags=re.DOTALL
    )
    
    # Write the fixed content back to the file
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    """Main function to fix all markdown files."""
    module_dir = "/Users/mattysquarzoni/Library/Mobile Documents/com~apple~CloudDocs/Projects-AI/Vibe_businessplanning/VibeBusinessPlanning"
    
    # Process all Markdown files in the directory
    markdown_files = glob.glob(os.path.join(module_dir, "Module *.md"))
    
    for file_path in markdown_files:
        # Skip the README
        if "README" not in file_path:
            fix_file(file_path)
    
    print("All files have been updated with GitHub-compatible styling.")

if __name__ == "__main__":
    main()
