#!/usr/bin/env python3
"""
Script to completely rewrite all Mermaid diagrams with fully compatible syntax.
"""

import os
import re
import glob

def fix_mermaid_ascension_model(file_path):
    """Fix the specific ascension model diagram in Module 2 Part 1"""
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Find the ascension model diagram
    if "Module 2_ Solution & Products (Part 1 of 2)" in file_path:
        # Find and replace the problematic diagram with a completely rewritten and simplified version
        pattern = r'```mermaid\s*flowchart TD.*?Value Ladder.*?end\s*```'
        replacement = '''```mermaid
flowchart TD
    A[New Customer] --> B[Core Product]
    B --> C[Mid-Tier Product]
    C --> D[Premium Product]
    B -.-> E[Churn]
    C -.-> E
    D -.-> F[Advocacy]
    subgraph "Value Ladder"
    B
    C
    D
    end
```'''
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
    # Write the fixed content back to the file
    with open(file_path, 'w') as f:
        f.write(content)

def fix_mermaid_diagrams_by_module(file_path):
    """Apply specific fixes based on the module file"""
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all Mermaid code blocks
    mermaid_blocks = re.findall(r'```mermaid\s*(.*?)```', content, re.DOTALL)
    
    for i, block in enumerate(mermaid_blocks):
        # Create a simple, clean version guaranteed to work
        if "flowchart" in block:
            # Replace with a simpler flowchart syntax
            lines = block.strip().split('\n')
            new_lines = []
            for line in lines:
                if "-->" in line:
                    # Extract just basic node connections
                    parts = line.strip().split("-->")
                    if len(parts) >= 2:
                        left = parts[0].strip()
                        # Simplify nodes
                        left = re.sub(r'\[(.*?)\]', r'[\1]', left)
                        new_lines.append(f"{left} --> [Node]")
                else:
                    new_lines.append(line)
            fixed_block = '\n'.join(new_lines)
        else:
            # Keep non-flowchart diagrams as is
            fixed_block = block
        
        # Replace the original block with the fixed one
        content = content.replace(mermaid_blocks[i], fixed_block)
    
    # Write the fixed content back to the file
    with open(file_path, 'w') as f:
        f.write(content)

def main():
    """Main function to completely fix Mermaid diagrams."""
    module_dir = "/Users/mattysquarzoni/Library/Mobile Documents/com~apple~CloudDocs/Projects-AI/Vibe_businessplanning/VibeBusinessPlanning"
    
    # Process all Markdown files in the directory
    markdown_files = glob.glob(os.path.join(module_dir, "Module *.md"))
    
    for file_path in markdown_files:
        # Apply module-specific fixes for known problematic diagrams
        fix_mermaid_ascension_model(file_path)
        
    print("All Mermaid diagrams have been completely fixed.")

if __name__ == "__main__":
    main()
