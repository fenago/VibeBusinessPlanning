# Module 1: Core Business Concept

<!-- 
INSTRUCTIONS FOR USER:
1. This is the second file in the 5-part modular business idea development system
2. You must complete Module 0 (Research Phase) before using this template
3. Paste the complete output from Module 0 in the research_findings section below
4. Submit this template to an LLM (like Manus or Claude)
5. Save the output to use as input for Module 2
-->

<core_concept_module>

## <previous_research>
    <!-- REQUIRED: Paste the complete output from Module 0 here -->
    
    ### <research_findings priority="essential">
        PASTE MODULE 0 OUTPUT HERE: [Paste the entire output from the Research Phase module]
    </research_findings>
</previous_research>

## <user_input>
    <!-- REQUIRED: Confirm or update these fields based on research -->
    
    ### <business_name priority="essential">
        YOUR INPUT: [Confirm or update your business name]
    </business_name>
    
    ### <business_description priority="essential">
        YOUR INPUT: [Confirm or update your business description based on research insights]
    </business_description>
</user_input>

## <lLM_instructions>
    <!-- Instructions for the LLM - DO NOT MODIFY -->
    
    You are a business concept development specialist tasked with defining the core elements of a business idea. Using the research findings and user input, develop a clear and compelling business concept.
    
    ### Process:
    
    1. Carefully review the research findings from Module 0
    2. Consider the confirmed business name and description
    3. Focus on defining the fundamental identity and value proposition
    4. Ensure all elements are coherent and aligned with research insights
    5. Prioritize business value over technical implementation details
    6. Create visual diagrams using Mermaid.js where appropriate to illustrate concepts
    7. Format all output as a well-structured Markdown document
    
    ### Output Sections:
    
    1. <business_name_analysis priority="essential">
        Analyze the current business name for effectiveness.
        Suggest 3-5 alternative names if appropriate, explaining the rationale.
        Recommend the strongest name option and explain why.
        
        Format:
        - Current name: [name]
        - Name effectiveness: [brief analysis]
        - Alternative suggestions: [list with brief rationale]
        - Recommendation: [strongest option with explanation]
    </business_name_analysis>
    
    2. <elevator_pitch priority="essential">
        Create a compelling 2-3 sentence elevator pitch that clearly communicates:
        - What the business does
        - Who it serves
        - The unique value it provides
        - How it differs from alternatives
        
        The pitch should be concise, memorable, and impactful.
    </elevator_pitch>
    
    3. <industry_category priority="important">
        Identify the primary and secondary industry categories this business belongs to.
        Explain why these categorizations are appropriate.
        Note any cross-industry positioning that creates unique opportunities.
        
        Format:
        - Primary category: [category]
        - Secondary category: [category]
        - Industry positioning: [brief explanation]
    </industry_category>
    
    4. <inspiration_sources priority="important">
        Identify 3-5 existing businesses or apps that could serve as inspiration.
        For each, note specific elements worth emulating or improving upon.
        Explain how these inspirations relate to the business concept.
        
        Format:
        - [Inspiration 1]: [specific elements to emulate/improve]
        - [Inspiration 2]: [specific elements to emulate/improve]
        - [Inspiration 3]: [specific elements to emulate/improve]
    </inspiration_sources>
    
    5. <high_level_user_flow priority="important">
        Outline the main steps a user/customer takes when engaging with this business.
        Include 5-7 key touchpoints from initial awareness to ongoing relationship.
        For each step, briefly note the user's goal and the business's objective.
        
        Format:
        1. [Step 1]: [User goal] → [Business objective]
        2. [Step 2]: [User goal] → [Business objective]
        And so on...
        
        Create a Mermaid.js diagram showing the customer journey flow.
        Example:
        ```mermaid
        flowchart LR
            A[Awareness] --> B[Consideration]
            B --> C[Decision]
            C --> D[Onboarding]
            D --> E[Usage]
            E --> F[Retention]
            F --> G[Advocacy]
        ```
    </high_level_user_flow>
    
    6. <core_differentiators priority="essential">
        Identify 3-5 key differentiators that set this business apart.
        For each differentiator, explain:
        - What makes it unique
        - Why it matters to customers
        - How it creates competitive advantage
        
        Focus on meaningful differences that create real value, not superficial distinctions.
        
        Create a Mermaid.js diagram showing how these differentiators relate to customer needs.
        Example:
        ```mermaid
        flowchart LR
            A[Customer Need 1] --> D1[Differentiator 1]
            B[Customer Need 2] --> D2[Differentiator 2]
            C[Customer Need 3] --> D3[Differentiator 3]
            D1 --> V[Value Proposition]
            D2 --> V
            D3 --> V
        ```
    </core_differentiators>
    
    7. <avatar_analysis priority="essential">
        Create a detailed avatar (customer persona) based on the Avatar Framework:
        
        a) <passion_elements priority="important">
            - Who would the business help for free?
            - What comes naturally to the business in serving customers?
        </passion_elements>
        
        b) <problem_definition priority="essential">
            - What explicit need does the business address?
            - How is the market for this solution growing?
            - How does the business solve the problem better/cheaper/faster?
        </problem_definition>
        
        c) <profit_potential priority="important">
            - How can customers afford this solution?
            - What's the size of the target niche?
            - How can ROI be quantified?
            - What's the potential for recurring revenue?
        </profit_potential>
        
        d) <presence_strategy priority="important">
            - How can the business be seen as the "go-to" provider?
            - How competitive is the niche?
            - What messaging is currently used in the market?
        </presence_strategy>
        
        e) <pathway_to_engagement priority="important">
            - How easily can the target audience be reached online?
            - Which social channels dominate for this audience?
            - What interests, experts, publications, and groups are relevant?
        </pathway_to_engagement>
        
        f) <demographics priority="important">
            - Age, income, education, occupation, location
        </demographics>
        
        g) <psychographics priority="important">
            - Values, beliefs, interests, attitudes, lifestyle
        </psychographics>
        
        h) <pains_and_frustrations priority="essential">
            - What problems and challenges does the avatar face?
        </pains_and_frustrations>
        
        i) <goals_and_desires priority="essential">
            - What does the avatar want to achieve or experience?
        </goals_and_desires>
        
        j) <fears_and_implications priority="important">
            - What is the avatar afraid of and what are the consequences?
        </fears_and_implications>
        
        k) <dreams_and_aspirations priority="important">
            - What ideal future state does the avatar aspire to?
        </dreams_and_aspirations>
        
        l) <currency priority="important">
            - What matters most to the avatar? (time, money, status, etc.)
        </currency>
        
        Create a Mermaid.js diagram visualizing the avatar's key characteristics.
        Example:
        ```mermaid
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
        ```
    </avatar_analysis>
    
    8. <million_dollar_message priority="essential">
        Create a compelling Million Dollar Message following this formula:
        "I help [TARGET AUDIENCE] achieve/do [GOAL/SOLUTION], so they can [DESIRED RESULT] without [PAIN POINT] in [TIMEFRAME]."
        
        The message should be:
        - Crisp and not overly wordy
        - Focused on customer outcomes, not features
        - Specific and compelling
        - Resonant with the target audience
        
        Provide the final message and a brief explanation of why it's effective.
        Ensure the message speaks directly to and resonates with the end customer.
    </million_dollar_message>
    
    9. <empathy_map_canvas priority="important">
        Create an empathy map for the primary customer segment:
        - What do they see? (environment, market offerings)
        - What do they hear? (influences, information sources)
        - What do they think and feel? (aspirations, concerns)
        - What do they say and do? (public behavior vs. private thoughts)
        - What are their pains? (frustrations, obstacles)
        - What are their gains? (desires, measures of success)
        
        Use this to deepen understanding of customer perspective.
        
        Create a Mermaid.js diagram showing the empathy map.
        Example:
        ```mermaid
        mindmap
            root((Customer Empathy Map))
                Sees
                    Market offerings
                    Competitor messages
                    Peer activities
                Hears
                    Recommendations
                    Expert opinions
                    Social media
                Thinks & Feels
                    Aspirations
                    Concerns
                    Motivations
                Says & Does
                    Public statements
                    Behaviors
                    Actions
                Pains
                    Frustrations
                    Obstacles
                    Fears
                Gains
                    Desires
                    Needs
                    Success measures
        ```
    </empathy_map_canvas>
    
    10. <core_concept_summary priority="essential">
        Synthesize all the above elements into a cohesive 2-3 paragraph summary.
        This should serve as a comprehensive yet concise overview of the business concept.
        Highlight how the various elements work together to create a compelling business opportunity.
        Note any particularly strong aspects of the concept and any areas that might need further development.
    </core_concept_summary>
    
    Format your output as a well-structured Markdown document with clear headings and subheadings. Use bullet points, tables, and emphasis where appropriate to enhance readability. Include Mermaid.js diagrams where they add value to visualize concepts.
    
    Important: Ensure all elements are coherent with each other and with the research findings. Focus on business value rather than technical implementation. Be creative but realistic in your development of the business concept.
</lLM_instructions>

## <next_steps>
    <!-- Instructions for proceeding to the next module -->
    
    After receiving the core business concept output from the LLM:
    
    1. Review the concept elements for alignment with your vision
    2. Save the complete output (including all sections)
    3. Proceed to "Module 2: Solution & Products" and paste this output where indicated
    4. The core concept will inform the development of your solution and product offerings
</next_steps>

</core_concept_module>
