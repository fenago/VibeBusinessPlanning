#!/usr/bin/env python3
"""
Final GitHub Mermaid Diagram Fix Script
Replicates the working format from Module 2 across all Mermaid diagrams.
"""

import os
import re
import glob

# Directory containing markdown files
base_dir = os.path.dirname(os.path.abspath(__file__))

# Find all markdown files
md_files = glob.glob(os.path.join(base_dir, "*.md"))

def fix_diagram_in_module1(content):
    """Fix the value proposition diagram in Module 1."""
    # Value proposition diagram
    value_prop_pattern = re.compile(r'Example diagram:.*?```mermaid.*?```', re.DOTALL)
    
    def replace_value_prop(match):
        return """Example diagram:

```mermaid
graph LR
    A[Customer Need] --> B[Your Solution]
    B --> C[Key Benefit 1]
    B --> D[Key Benefit 2]
    B --> E[Key Benefit 3]
```"""
    
    return value_prop_pattern.sub(replace_value_prop, content)

def fix_mindmap_in_module1(content):
    """Fix the mindmap in Module 1."""
    # Mindmap diagram
    mindmap_pattern = re.compile(r'```mermaid\s*\nmindmap.*?```', re.DOTALL)
    
    def replace_mindmap(match):
        return """```mermaid
flowchart TD
    A[Avatar Name] --> B[Demographics]
    B --> B1[Age range]
    B --> B2[Income level]
    B --> B3[Education]
    B --> B4[Location]
    A --> C[Psychographics]
    C --> C1[Values]
    C --> C2[Beliefs]
    C --> C3[Interests]
    A --> D[Pains]
    D --> D1[Pain point 1]
    D --> D2[Pain point 2]
    A --> E[Goals]
    E --> E1[Goal 1]
    E --> E2[Goal 2]
    A --> F[Currency]
    F --> F1[Primary value]
```"""
    
    return mindmap_pattern.sub(replace_mindmap, content)

def fix_empathy_map_in_module1(content):
    """Fix the empathy map in Module 1."""
    empathy_pattern = re.compile(r'```mermaid\s*\nmindmap\s*\nroot\(\(Customer Empathy Map\)\).*?```', re.DOTALL)
    
    def replace_empathy(match):
        return """```mermaid
flowchart TD
    A[Customer Empathy Map] --> B[Sees]
    A --> C[Hears]
    A --> D[Thinks & Feels]
    A --> E[Says & Does]
    A --> F[Pains]
    A --> G[Gains]
    B --> B1[Market offerings]
    B --> B2[Competitors]
    B --> B3[Social media]
    C --> C1[Influencers]
    C --> C2[Media]
    C --> C3[Friends/Family]
    D --> D1[Aspirations]
    D --> D2[Concerns]
    D --> D3[Motivations]
    E --> E1[Public statements]
    E --> E2[Behaviors]
    E --> E3[Actions]
    F --> F1[Frustrations]
    F --> F2[Obstacles]
    F --> F3[Fears]
    G --> G1[Desires]
    G --> G2[Needs]
    G --> G3[Success measures]
```"""
    
    return empathy_pattern.sub(replace_empathy, content)

def fix_quadrant_chart(content):
    """Fix quadrant charts."""
    quadrant_pattern = re.compile(r'```mermaid\s*\nquadrantChart.*?```', re.DOTALL)
    
    def replace_quadrant(match):
        match_text = match.group(0)
        
        # Preserve the title and axes
        title_match = re.search(r'title\s+(.*)', match_text)
        x_axis_match = re.search(r'x-axis\s+(.*)', match_text)
        y_axis_match = re.search(r'y-axis\s+(.*)', match_text)
        
        title = title_match.group(1) if title_match else "Competitive Positioning"
        x_axis = x_axis_match.group(1) if x_axis_match else "Low Market Share --> High Market Share"
        y_axis = y_axis_match.group(1) if y_axis_match else "Low Product Quality --> High Product Quality"
        
        return f"""```mermaid
quadrantChart
    title {title}
    x-axis {x_axis}
    y-axis {y_axis}
    quadrant-1 "Opportunity Area"
    quadrant-2 "Market Leaders"
    quadrant-3 "Declining Segment"
    quadrant-4 "Emerging Players"
    "Competitor A": [0.7, 0.8]
    "Competitor B": [0.5, 0.6]
    "Our Business": [0.4, 0.7]
    "Competitor C": [0.3, 0.4]
    "Competitor D": [0.6, 0.3]
```"""
    
    return quadrant_pattern.sub(replace_quadrant, content)

def fix_gantt_charts(content):
    """Fix Gantt charts."""
    gantt_pattern = re.compile(r'```mermaid\s*\ngantt.*?```', re.DOTALL)
    
    def replace_gantt(match):
        return """```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Research
    Market Analysis      :a1, 2023-01-01, 30d
    Competitor Analysis  :a2, after a1, 20d
    section Development
    Product Design       :b1, after a2, 45d
    Development          :b2, after b1, 60d
    Testing              :b3, after b2, 30d
    section Launch
    Marketing            :c1, after b1, 45d
    Launch               :c2, after b3, 10d
    section Post-Launch
    Evaluation           :d1, after c2, 20d
    Iteration            :d2, after d1, 30d
```"""
    
    return gantt_pattern.sub(replace_gantt, content)

def fix_pie_charts(content):
    """Fix pie charts."""
    pie_pattern = re.compile(r'```mermaid\s*\npie.*?```', re.DOTALL)
    
    def replace_pie(match):
        return """```mermaid
pie
    title Revenue Breakdown
    "Product A" : 40
    "Product B" : 30
    "Product C" : 20
    "Other" : 10
```"""
    
    return pie_pattern.sub(replace_pie, content)

def fix_general_mermaid_diagrams(content):
    """Fix all other Mermaid diagrams."""
    # Find all mermaid diagrams that haven't been fixed by the specific functions
    mermaid_pattern = re.compile(r'```mermaid\s*\n(.*?)\n```', re.DOTALL)
    
    def clean_diagram(match):
        diagram_content = match.group(1).strip()
        diagram_type = ""
        
        # Extract the diagram type (first word in diagram content)
        first_line = diagram_content.split('\n')[0].strip()
        
        # Skip diagrams we've already processed with specific functions
        if first_line in ["quadrantChart", "gantt", "pie"] or first_line.startswith("mindmap"):
            return match.group(0)
        
        if first_line.startswith("flowchart") or first_line.startswith("graph"):
            diagram_type = first_line
            diagram_content = '\n'.join(diagram_content.split('\n')[1:])
        else:
            # Default to flowchart TD if no type specified
            diagram_type = "flowchart TD"
        
        # Clean up the diagram content
        lines = diagram_content.split('\n')
        clean_lines = []
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Fix arrows
            line = re.sub(r'-->', ' --> ', line)
            line = re.sub(r'-\.->|\.\.\.>', ' -.-> ', line)
            
            # Fix subgraphs - remove quotes
            line = re.sub(r'subgraph\s+"([^"]+)"', r'subgraph \1', line)
            
            # Add proper indentation
            if line.startswith('subgraph') or line == 'end':
                clean_lines.append(line)
            else:
                clean_lines.append('    ' + line)
        
        # Join the lines with clean formatting
        clean_content = '\n'.join([diagram_type] + clean_lines)
        
        return f"```mermaid\n{clean_content}\n```"
    
    return mermaid_pattern.sub(clean_diagram, content)

def fix_file(file_path):
    """Fix mermaid diagrams in a single file."""
    file_name = os.path.basename(file_path)
    print(f"Processing {file_name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip files without mermaid diagrams
    if '```mermaid' not in content:
        print(f"  No mermaid diagrams found in {file_name}")
        return False
    
    # Original content for comparison
    original_content = content
    
    # Apply specific fixes based on the file name
    if "Module 1_" in file_name:
        content = fix_diagram_in_module1(content)
        content = fix_mindmap_in_module1(content)
        content = fix_empathy_map_in_module1(content)
    
    # Apply general fixes for all diagram types
    content = fix_quadrant_chart(content)
    content = fix_gantt_charts(content)
    content = fix_pie_charts(content)
    content = fix_general_mermaid_diagrams(content)
    
    # Only write changes if the content was modified
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed mermaid diagrams in {file_name}")
        return True
    else:
        print(f"  No changes made to {file_name}")
        return False

def main():
    """Main function to process all markdown files."""
    print("Starting final GitHub Mermaid diagram fixes...")
    fixed_count = 0
    
    for md_file in md_files:
        if fix_file(md_file):
            fixed_count += 1
    
    print(f"\nComplete! Fixed mermaid diagrams in {fixed_count} files.")

if __name__ == "__main__":
    main()
