#!/usr/bin/env python3
"""
Comprehensive GitHub Mermaid Diagram Fix Script
This script properly formats all Mermaid diagrams in markdown files to ensure
they render correctly on GitHub.
"""

import os
import re
import glob

# Directory containing markdown files
base_dir = os.path.dirname(os.path.abspath(__file__))

# Find all markdown files
md_files = glob.glob(os.path.join(base_dir, "*.md"))

# Patterns to match mermaid blocks
mermaid_pattern1 = re.compile(r'```mermaid\s*\n(.*?)\n```', re.DOTALL)
mermaid_pattern2 = re.compile(r'```\s*\n\s*```mermaid\s*\n(.*?)\n\s*```', re.DOTALL)
mermaid_pattern3 = re.compile(r'```\s*\nmermaid\s*\n(.*?)\n\s*```', re.DOTALL)
mermaid_example_pattern = re.compile(r'Example:\s*\n\s*```mermaid', re.DOTALL)

def fix_file(file_path):
    """Fix mermaid diagrams in a single file."""
    print(f"Processing {os.path.basename(file_path)}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if there are any mermaid diagrams in the file
    if "mermaid" not in content:
        print(f"  No mermaid diagrams found in {os.path.basename(file_path)}")
        return False

    # Save original content for comparison
    original_content = content
    
    # Fix Example: ```mermaid blocks (common in the files)
    content = mermaid_example_pattern.sub('Example:\n\n```mermaid', content)
    
    # Fix triple-nested mermaid blocks
    def clean_mermaid_block(match):
        mermaid_content = match.group(1).strip()
        # Remove any Note: lines that cause parsing errors
        mermaid_content = re.sub(r'^\s*Note:.*$', '', mermaid_content, flags=re.MULTILINE)
        # Fix any common mermaid syntax errors
        mermaid_content = fix_mermaid_syntax(mermaid_content)
        return f"```mermaid\n{mermaid_content}\n```"
    
    # Apply the fixes to all mermaid patterns
    content = mermaid_pattern1.sub(clean_mermaid_block, content)
    content = mermaid_pattern2.sub(clean_mermaid_block, content)
    content = mermaid_pattern3.sub(clean_mermaid_block, content)
    
    # Fix any remaining improperly formatted blocks
    content = fix_remaining_blocks(content)
    
    # Check if content was modified
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed mermaid diagrams in {os.path.basename(file_path)}")
        return True
    else:
        print(f"  No changes made to {os.path.basename(file_path)}")
        return False

def fix_mermaid_syntax(mermaid_content):
    """Fix common syntax issues in mermaid diagram content."""
    # Fix flowchart connections with --> 
    mermaid_content = re.sub(r'(\w+)\s*-->\s*(\w+)', r'\1 --> \2', mermaid_content)
    
    # Fix incorrect arrow syntax
    mermaid_content = re.sub(r'-->', r'-->', mermaid_content)
    
    # Fix spacing in subgraphs with quotes
    mermaid_content = re.sub(r'subgraph\s+"([^"]+)"', r'subgraph \1', mermaid_content)
    
    # Fix node definitions with incorrect brackets
    mermaid_content = re.sub(r'\[([^\]]+)\]', r'[\1]', mermaid_content)
    
    # Remove any 'Note:' lines that could interfere with rendering
    mermaid_content = re.sub(r'^\s*Note:.*$', '', mermaid_content, flags=re.MULTILINE)
    
    return mermaid_content.strip()

def fix_remaining_blocks(content):
    """Fix any remaining mermaid blocks with complex patterns."""
    # Find indented mermaid blocks that aren't properly formatted
    pattern = re.compile(r'(```)\s*(\n\s*mermaid\s*\n)', re.MULTILINE)
    content = pattern.sub(r'```mermaid\n', content)
    
    # Clean up extra newlines around mermaid blocks
    content = re.sub(r'```mermaid\s*\n\s*\n', r'```mermaid\n', content)
    content = re.sub(r'\n\s*\n\s*```', r'\n```', content)
    
    # Ensure proper spacing after diagrams
    content = re.sub(r'```\s*\n\s*(\w)', r'```\n\n\1', content)
    
    return content

def main():
    """Main function to process all markdown files."""
    print("Starting GitHub Mermaid diagram fixes...")
    fixed_count = 0
    
    for md_file in md_files:
        if fix_file(md_file):
            fixed_count += 1
    
    print(f"\nComplete! Fixed mermaid diagrams in {fixed_count} files.")

if __name__ == "__main__":
    main()
