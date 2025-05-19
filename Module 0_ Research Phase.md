# 📊 Module 0: Research Phase 📊

![Phase: Research](https://img.shields.io/badge/Phase-Research-5BCEFA?style=for-the-badge)
![Status: Ready For Input](https://img.shields.io/badge/Status-Ready_For_Input-22C55E?style=for-the-badge)
![Estimated Time: 45 Minutes](https://img.shields.io/badge/Estimated_Time-45_Minutes-F5A9B8?style=flat-square)

## 🌌 Business Intelligence Gathering

> [!NOTE]
> This is the first module in the Vibe Business Planning System. Here, you'll provide basic information about your business idea to generate comprehensive market research that will inform later modules.

### 🔍 Module Purpose

- 📊 **Foundation Building**: Establish the knowledge base for your entire business plan
- 📈 **Market Validation**: Confirm your business idea has real-world potential
- 👥 **Audience Identification**: Discover exactly who will benefit from your solution
- 📋 **Competitive Analysis**: Understand the landscape you'll be entering

<!-- 
INSTRUCTIONS FOR USER:
1. This is the first file in a 5-part modular business idea development system
2. Fill in ONLY the business name and description below
3. Provide any URLs or resources you want the LLM to research
4. Submit this template to an LLM (like Manus or Claude)
5. Save the output to use as input for Module 1
-->

<research_module>

## <user_input>
    <!-- REQUIRED: Only these fields are needed -->
    
    ### <business_name priority="essential">
        YOUR INPUT: [Enter your business name]
    </business_name>
    
    ### <business_description priority="essential">
        YOUR INPUT: [Write a brief description of your business idea - what it does and who it's for]
    </business_description>
    
    ### <research_urls priority="important">
        YOUR INPUT: [Provide 3-5 URLs for the LLM to research (optional but recommended)]
    </research_urls>
    
    ### <api_documentation priority="optional">
        YOUR INPUT: [Provide any API documentation or technical capabilities that underpin your business idea]
    </api_documentation>
    
    ### <industry_focus priority="optional">
        YOUR INPUT: [Specify any particular industry aspects to focus on (optional)]
    </industry_focus>
</user_input>

## <lLM_instructions>
    <!-- Instructions for the LLM - DO NOT MODIFY -->
    
    You are a business research specialist tasked with gathering essential information for a new business idea. Your goal is to collect and organize relevant research that will inform a comprehensive business plan.
    
    ### Research Process:
    
    1. First, analyze the business name and description provided by the user
    2. If URLs are provided, extract key information from those sources
    3. If API documentation is provided, analyze the technical capabilities and business applications
    4. Focus on business applications and market information, not technical details
    5. Organize your findings in a structured format
    6. Keep your research focused and relevant to business planning
    7. Create visual diagrams using Mermaid.js where appropriate to illustrate concepts
    8. Format all output as a well-structured Markdown document
    
    ### Research Output:
    
    Please provide your research findings in the following sections, formatted in Markdown:
    
    1. <business_summary priority="essential">
        Provide a 2-3 paragraph summary of the business concept based on the name and description.
        Focus on clarifying the core value proposition and target market.
    </business_summary>
    
    2. <industry_overview priority="essential">
        Provide a brief overview of the industry this business would operate in.
        Include market size, growth trends, and key players if available.
        Identify 2-3 similar businesses or competitors.
        
        Create a Mermaid.js diagram showing the industry structure and where this business fits.
        Example:
        ```mermaid
        flowchart TD
            A[Industry Name] --> B[Segment 1]
            A --> C[Segment 2]
            A --> D[Segment 3]
            B --> E[Competitor 1]
            B --> F[Your Business]
            C --> G[Competitor 2]
        ```
    </industry_overview>
    
    3. <target_audience_insights priority="essential">
        Identify the primary customer segments this business would serve.
        Describe their key characteristics, needs, and pain points.
        Explain why this audience would value the proposed solution.
    </target_audience_insights>
    
    4. <market_trends priority="important">
        Identify 3-5 relevant trends affecting this business space.
        Explain how these trends create opportunities or challenges.
        Note any regulatory or technological factors to consider.
        
        If appropriate, create a Mermaid.js timeline diagram showing the evolution of key trends.
        Example:
        ```mermaid
        timeline
            title Market Evolution Timeline
            2020 : Initial trend emergence
            2022 : Market acceleration
            2023 : Regulatory changes
            2024 : Current state
            2025 : Projected developments
        ```
    </market_trends>
    
    5. <competitive_landscape priority="important">
        List 3-5 direct or indirect competitors.
        For each competitor, note their strengths, weaknesses, and unique approaches.
        Identify potential gaps or opportunities in the market.
        
        Create a Mermaid.js quadrant chart showing competitive positioning if appropriate.
        Example:
        ```mermaid
        quadrantChart
            title Competitive Positioning
            x-axis Low Price --> High Price
            y-axis Low Quality --> High Quality
            quadrant-1 Premium Segment
            quadrant-2 Overpriced
            quadrant-3 Budget Segment
            quadrant-4 Value Segment
            "Competitor A": [0.3, 0.6]
            "Competitor B": [0.7, 0.7]
            "Your Business": [0.5, 0.8]
        ```
    </competitive_landscape>
    
    6. <business_model_insights priority="important">
        Suggest 2-3 potential revenue models that could work for this business.
        Identify key resources or partnerships that might be needed.
        Note any industry-specific business model considerations.
    </business_model_insights>
    
    7. <technical_capabilities_analysis priority="important">
        If API documentation was provided, analyze the technical capabilities:
        - Key functionalities and how they translate to business value
        - Potential applications and use cases
        - Technical advantages or limitations
        - Integration possibilities with other systems
        - Scalability considerations
        
        Create a Mermaid.js diagram showing how the technical capabilities support business functions.
        Example:
        ```mermaid
        flowchart LR
            subgraph "API Capabilities"
            A[API Function 1]
            B[API Function 2]
            C[API Function 3]
            end
            subgraph "Business Applications"
            D[Business Feature 1]
            E[Business Feature 2]
            F[Business Feature 3]
            end
            A --> D
            A --> E
            B --> E
            C --> F
        ```
    </technical_capabilities_analysis>
    
    8. <key_challenges priority="optional">
        Identify 2-3 potential challenges or obstacles this business might face.
        Suggest possible approaches to addressing these challenges.
    </key_challenges>
    
    9. <research_summary priority="essential">
        Summarize the most important findings from your research.
        Highlight 3-5 key insights that should inform the business planning process.
        Note any areas where additional research might be beneficial.
    </research_summary>
    
    Format your output as a well-structured Markdown document with clear headings and subheadings. Use bullet points, tables, and emphasis where appropriate to enhance readability. Include Mermaid.js diagrams where they add value to visualize concepts.
    
    Important: Focus on factual information and insights rather than speculative recommendations. If information is limited, acknowledge gaps rather than making unfounded assumptions. Cite sources where appropriate.
</lLM_instructions>

## <next_steps>
    <!-- Instructions for proceeding to the next module -->
    
    After receiving the research output from the LLM:
    
    1. Review the research findings for accuracy and relevance
    2. Save the complete output (including all sections)
    3. Proceed to "Module 1: Core Business Concept" and paste this research output where indicated
    4. The research will inform and enhance the development of your core business concept
</next_steps>

</research_module>
