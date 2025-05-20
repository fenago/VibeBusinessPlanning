#!/usr/bin/env python3
"""
Direct Manual Fix for Problematic Mermaid Diagrams
This script directly replaces known problematic diagrams with working versions.
"""

import os
import re

# Path to Module 1
module1_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                            "Module 1_ Core Business Concept.md")

# Read Module 1 content
with open(module1_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Customer Journey Flow diagram
customer_journey_pattern = re.compile(
    r'Create a Mermaid\.js diagram showing the customer journey flow\.\s*Example:\s*```mermaid.*?```',
    re.DOTALL
)

customer_journey_replacement = """Create a Mermaid.js diagram showing the customer journey flow.
Example:

```mermaid
flowchart LR
    A[Awareness] --> B[Consideration]
    B --> C[Decision]
    C --> D[Onboarding]
    D --> E[Usage]
    E --> F[Retention]
    F --> G[Advocacy]
```"""

content = customer_journey_pattern.sub(customer_journey_replacement, content)

# 2. Fix Differentiators diagram
differentiators_pattern = re.compile(
    r'Create a Mermaid\.js diagram showing how these differentiators relate to customer needs\.\s*Example:\s*```mermaid.*?```',
    re.DOTALL
)

differentiators_replacement = """Create a Mermaid.js diagram showing how these differentiators relate to customer needs.
Example:

```mermaid
flowchart LR
    A[Customer Need 1] --> B[Differentiator 1]
    C[Customer Need 2] --> D[Differentiator 2]
    E[Customer Need 3] --> F[Differentiator 3]
    B --> G[Value Proposition]
    D --> G
    F --> G
```"""

content = differentiators_pattern.sub(differentiators_replacement, content)

# 3. Fix Value Proposition diagram
value_prop_pattern = re.compile(
    r'Example diagram:\s*```mermaid.*?```',
    re.DOTALL
)

value_prop_replacement = """Example diagram:

```mermaid
flowchart LR
    A[Customer Need] --> B[Your Solution]
    B --> C[Key Benefit 1]
    B --> D[Key Benefit 2]
    B --> E[Key Benefit 3]
```"""

content = value_prop_pattern.sub(value_prop_replacement, content)

# 4. Fix Avatar Analysis mindmap
avatar_mindmap_pattern = re.compile(
    r'```mermaid\s*mindmap\s*root\(\(Avatar Name\)\).*?```',
    re.DOTALL
)

avatar_mindmap_replacement = """```mermaid
flowchart TD
    A[Avatar Name] --> B[Demographics]
    A --> C[Psychographics]
    A --> D[Pains]
    A --> E[Goals]
    A --> F[Currency]
    B --> B1[Age range]
    B --> B2[Income level]
    B --> B3[Education]
    B --> B4[Location]
    C --> C1[Values]
    C --> C2[Beliefs]
    C --> C3[Interests]
    D --> D1[Pain point 1]
    D --> D2[Pain point 2]
    E --> E1[Goal 1]
    E --> E2[Goal 2]
    F --> F1[Primary value]
```"""

content = avatar_mindmap_pattern.sub(avatar_mindmap_replacement, content)

# 5. Fix Customer Empathy Map
empathy_map_pattern = re.compile(
    r'```mermaid\s*mindmap\s*root\(\(Customer Empathy Map\)\).*?```',
    re.DOTALL
)

empathy_map_replacement = """```mermaid
flowchart TD
    A[Customer Empathy Map] --> B[Sees]
    A --> C[Hears]
    A --> D[Thinks & Feels]
    A --> E[Says & Does]
    A --> F[Pains]
    A --> G[Gains]
    B --> B1[Market offerings]
    C --> C1[Information sources]
    D --> D1[Aspirations]
    E --> E1[Behaviors]
    F --> F1[Frustrations]
    G --> G1[Desires]
```"""

content = empathy_map_pattern.sub(empathy_map_replacement, content)

# Write the fixed content back to the file
with open(module1_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied manual fixes to Module 1 diagrams.")
