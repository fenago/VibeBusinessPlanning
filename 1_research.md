### The Expert-Driven Research Summary Prompt

**Instructions for Use:**

1.  Copy the entire prompt below.
2.  Replace the bracketed placeholders `[Business Name]`, `[Brief Business Description]`, and `[Core Technology/Platform]` with your specific information.
3.  Paste the `[Problem-Aware Avatar Description]` and `[Avatar's Diary Entry]` you have prepared into the designated sections.
4.  Provide the completed prompt to the AI.

---

### **PROMPT START**

**ROLE & GOAL:**

Act as a "Strategic Product Syndicate," a team of four elite consultants hired to produce a foundational research summary for a new business concept. Your team consists of:

1.  **The Business Strategist:** Expert in market positioning, monetization, and value propositions.
2.  **The Lead Systems Architect:** Expert in modern tech stacks, integrations, and platform capabilities.
3.  **The UX/UI Visionary:** Expert in user experience, modern design frameworks, and brand identity.
4.  **The Product Manager:** Expert in user requirements, project scoping, and actionable next steps.

Your goal is to synthesize the provided information into a comprehensive research summary. The final output must be a single markdown file, meticulously structured to match the format, tone, and detail level of the AgenticVoice.net example.

**PRIMARY INPUTS:**

*   **Business Name:** `[Business Name]`
*   **Brief Business Description:** `[Brief Business Description]`
*   **Core Technology/Platform:** `[Core Technology/Platform]` (This is the central technology the business is built ON TOP OF, similar to how AgenticVoice.net uses Vapi.ai).

**USER RESEARCH INPUTS:**

*   **Problem-Aware Avatar Description:**
    ```
    [PASTE YOUR PROBLEM-AWARE AVATAR DESCRIPTION HERE]
    ```

*   **Avatar's Diary Entry:**
    ```
    [PASTE YOUR AVATAR'S DIARY ENTRY HERE]
    ```

**TASK: GENERATE THE RESEARCH SUMMARY**

Produce the research summary by collaborating as the Strategic Product Syndicate. Each expert should contribute to their relevant sections. Structure the output in markdown format precisely as follows:

---

`# [Business Name] Research Summary`

`## Project Overview`
(As a team, write a concise, high-level summary. What is the business? Who is the primary target audience? What core function does it perform?)

`## Key Research Findings`
(This is the core of the summary. Each expert will contribute.)

`### 1. Business Model`
(Contribution from the **Business Strategist**. Define a plausible and compelling business model.
    - **Approach:** Propose a primary approach (e.g., Service-First, SaaS, B2B, B2C).
    - **Target Industries:** Identify the most lucrative initial industries to target, based on the avatar.
    - **Value Proposition:** Clearly state the key benefits for the customer. Use strong action verbs. What costs does it reduce, what time does it save, what revenue does it generate, what pain does it eliminate?)

`### 2. Technical Foundation`
(Contribution from the **Lead Systems Architect**. Outline a robust and modern technical foundation.
    - **Core Technology:** Explicitly name the `[Core Technology/Platform]` as the foundational layer.
    - **Integration Capabilities:** Propose at least 3-5 logical third-party integrations that would enhance the product's value (e.g., CRMs, calendar APIs, data enrichment tools, automation platforms like n8n.io or Zapier).
    - **Authentication:** Recommend standard, secure authentication methods (e.g., Google OAuth, Magic Links, traditional email/password).)

`### 3. UI Framework & Components`
(Contribution from the **UX/UI Visionary**. Propose a modern and aesthetically pleasing UI strategy.
    - **Current Implementation (Proposed):** Suggest a base framework (e.g., Next.js, SvelteKit), styling solution (e.g., Tailwind CSS), and a base component library (e.g., DaisyUI, Flowbite).
    - **Planned Enhancements:** Suggest at least two cutting-edge UI libraries to elevate the user experience, referencing specific examples like **shadcn/ui** for components and **MagicUI** for animations and micro-interactions.)

`### 4. Existing Brand Elements (Proposed)`
(Contribution from the **UX/UI Visionary**. Propose foundational brand elements to guide design.
    - **Logo:** Briefly describe a concept for a logo and state where it would be stored (e.g., "in the public directory as logo.svg").
    - **Color Scheme:** Propose a gradient-based color scheme. **You must provide a sample CSS linear-gradient** with at least 5-6 hex color codes, similar to the sample.
    - **Animations:** Define 3-5 conceptual custom animation names that would fit the brand's feel (e.g., `fadeIn`, `slideUp`, `pulse`, `shimmer`). Mention they would be defined in a config file like `tailwind.config.js`.)

`### 5. User Requirements`
(Contribution from the **Product Manager**. List critical non-functional requirements and project constraints.
    - **Mobile Support:** State the requirement (e.g., "Full mobile-responsive functionality required").
    - **Multilingual Support:** State the requirement for the user interface.
    - **Timeline:** Propose a realistic but aggressive timeline (e.g., "one week for MVP," "four weeks for V1").
    - **User Control:** Define the level of control end-users will have, drawing inspiration from the sample (e.g., "Limited customer control over core workflows; visualizations and dashboards will be provided for monitoring.").

`## [Core Technology/Platform] Capabilities`
(Contribution from the **Lead Systems Architect**. Based on your knowledge of the specified `[Core Technology/Platform]`, provide a summary of its key features and how our business will leverage it. If you are unsure, perform a quick "lookup" to provide an accurate summary.)

`### Core Features`
(List 3-4 key features of the platform itself.)

`### Technical Integration Points`
(Describe how a developer would integrate with this platform.
    - **API & SDK Integration:** Mention the existence of its APIs/SDKs.
    - **Example Snippet:** **Provide a small, illustrative code snippet** for a key function in a relevant language (e.g., JavaScript, Python), similar to the Vapi.js example.
    - **Authentication:** Briefly describe how developers authenticate with the platform's API (e.g., Bearer Token, API Key).
    - **Webhooks:** Mention the availability of webhooks for real-time events.)

`## Avatar Research Insights`
(Contribution from the **Product Manager** and **Business Strategist**. Synthesize the provided **Problem-Aware Avatar Description** and **Avatar's Diary Entry**.)
(Your analysis MUST:
    - Directly reference the pain points, frustrations, and emotional state described in the inputs.
    - Explain *how* `[Business Name]` serves as the "antidote" to these specific problems.
    - Justify the product's existence by connecting it directly to the avatar's narrative.
    - Propose how this deep understanding informs the marketing approach, referencing high-converting strategies.)

`## Next Steps`
(As a team, conclude with a numbered list of 3-4 clear, actionable next steps for the project. These should be immediate and tangible.)

---

**FINAL CHECK:**

Ensure the entire output is a single, clean markdown file. Do not include any conversational text outside of the generated summary. The structure, headings, and use of lists/code blocks must mirror the provided sample.

### **PROMPT END**
