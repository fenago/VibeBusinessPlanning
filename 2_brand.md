
### The Expert-Driven Brand & Design System Prompt

**Instructions for Use:**

1.  Copy the entire prompt below.
2.  Take the complete markdown output from the "Research Summary" prompt and paste it into the `[PASTE THE ENTIRE 'RESEARCH SUMMARY' MARKDOWN HERE]` section.
3.  Provide the completed prompt to the AI.

---

### **PROMPT START**

**ROLE & GOAL:**

Act as a "Brand & Design Syndicate," a specialized team hired to translate a strategic research summary into a comprehensive and actionable brand identity and design system. Your team consists of:

1.  **The Brand Strategist:** An expert in brand positioning, voice, and narrative.
2.  **The Lead UI/UX Designer:** An expert in visual systems, color theory, typography, and component-based design.
3.  **The Lead Front-End Developer:** An expert in implementation, accessibility, responsive design, and design tokens.

Your goal is to use the provided **Research Summary** as the single source of truth to create a formal **Brand Identity & Design System**. The final output must be a single markdown file, meticulously structured to match the provided format, tone, and technical depth.

**PRIMARY INPUT:**

*   **Research Summary:**
    ```markdown
    [PASTE THE ENTIRE 'RESEARCH SUMMARY' MARKDOWN HERE]
    ```

**TASK: GENERATE THE BRAND IDENTITY & DESIGN SYSTEM**

Produce the document by collaborating as the Brand & Design Syndicate. Each expert will lead their relevant sections, ensuring every decision is rooted in the information from the Research Summary. Structure the output in markdown format precisely as follows:

---

`# [Business Name] Brand Identity & Design System`
(Extract the business name from the Research Summary)

`## Brand Identity`
(Contribution led by the **Brand Strategist**)

`### Brand Essence`
(Distill the `Project Overview` and `Value Proposition` from the Research Summary into 5-7 core brand attributes. Examples: Professionalism, Innovation, Efficiency, Reliability, Security.)

`### Brand Voice`
(- **Tone**: Define the tone based on the target audience (e.g., Professional, confident, reassuring).
- **Language**: Describe the language style (e.g., Clear, jargon-free explanations).
- **Communication Style**: Describe the overall approach (e.g., Solution-oriented, emphasizing benefits).)

`### Brand Narrative`
(Write a short, compelling paragraph that tells the story of the brand. It should summarize what the business does, for whom, and why it matters, drawing heavily from the `Project Overview` and `Avatar Research Insights`.)

`## Design System`
(Contribution led by the **Lead UI/UX Designer** and **Lead Front-End Developer**)

`### Color Palette`

`#### Primary Colors`
(- **Gradient Base**: State that the gradient from the Research Summary is the brand's identity. **You must copy the exact CSS `linear-gradient` from the `Research Summary` input.**
- **Primary Colors (Extracted from gradient)**: List the 6-8 key colors from the gradient by their hex code. For each color, give it a name (e.g., Orange, Teal) and a one-word attribute (e.g., Energy, Trust).)

`#### Secondary Colors`
(Define a standard set of neutral colors for UI. Propose specific hex codes for: Dark Blue (primary text), Medium Gray (secondary text), Light Gray (backgrounds), White, and Black.)

`#### Functional Colors`
(Define a standard set of functional colors. Propose specific hex codes for: Success, Warning, Error, and Info.)

`### Typography`

`#### Font Family`
(- **Primary Font**: Choose a clean, modern, highly-readable sans-serif font like **Inter**. Justify the choice.
- **Secondary Font**: Choose an elegant, sophisticated serif font like **DM Serif Display** for major headlines. Justify the choice.)

`#### Font Sizes`
(Create a full typographic scale. **This must be detailed and precise, matching the sample's format.** Include H1-H6, Body (Regular, Small, XSmall), and Special Text (Display, Caption). For each, provide the `rem`, `px`, and `line-height` values.)

`#### Font Weights`
(List the standard font weights to be used: Light (300), Regular (400), Medium (500), Semibold (600), Bold (700).)

`### UI Components`

`#### 21st.dev Components`
(Based on the `UI Framework & Components` section of the Research Summary, list the categories of components from a modern library like **21st.dev** that will be used. Examples: Navigation, Layout, Forms, Feedback, Data Display, Disclosure.)

`#### MagicUI Components`
(Based on the Research Summary, list at least 5 specific animated components from a library like **MagicUI** that would enhance the user experience. Examples: Animated Cards, Hover Effects, Scroll Animations, Testimonial Carousels, Animated Icons.)

`#### Custom Components`
(Based on the core function of the business described in the Research Summary, propose 3-4 essential custom components that would need to be built. Examples: Voice Agent Visualization, ROI Calculator, Call Demo Interface, Dashboard Widgets.)

`### Micro-Interactions`
(Define 5-6 subtle animations for common UI events. Examples: Button Hover, Form Focus, Loading States, Success Actions, Navigation, Scrolling.)

`### Responsive Design`
(Contribution led by the **Lead Front-End Developer**)
(- **Mobile-First Approach**: State this as the core principle.
- **Breakpoints**: List the standard Tailwind CSS breakpoints (sm, md, lg, xl, 2xl) with their pixel values.
- **Mobile Adaptations**: List key changes for mobile, such as simplified navigation (hamburger menu), stacked layouts, and larger touch targets.)

`### Accessibility`
(List key accessibility commitments. Must include: Color Contrast (WCAG AA), Keyboard Navigation, Screen Reader Support (ARIA), Visible Focus Indicators, and Respect for Reduced Motion.)

`### Dark/Light Mode`
(State that both modes will be supported, mentioning DaisyUI themes as the implementation mechanism, along with automatic system preference detection and a user-selectable toggle.)

`## Implementation Guidelines`
(Contribution led by the **Lead Front-End Developer**)

`### CSS Framework`
(List the frameworks mentioned in the Research Summary: Tailwind CSS, DaisyUI, and a placeholder for custom utilities.)

`### Animation Library`
(Propose a primary animation library like **Framer Motion** for complex animations and state that **Tailwind Animations** will be used for simple ones.)

`### Icon System`
(Propose a standard, comprehensive icon set like **Heroicons** and mention the use of custom SVGs.)

`### Asset Management`
(Specify the preferred file formats for different assets: SVG for icons, WebP for images, MP4/WebM for video.)

`### Code Structure`
(Outline best practices: Component-Based Architecture, Utility-First CSS, Responsive Variants.)

`## Design Tokens`
(As the **Lead Front-End Developer**, create a JSON object that codifies the design system's core values. Populate the JSON structure below using the values defined in the `Color Palette`, `Typography`, and common spacing/radius conventions. **The structure must be exactly as follows.**)
```json
{
  "colors": {
    "primary": {
      // Populate with the extracted primary colors
    },
    "neutral": {
      // Populate with the neutral colors
    },
    "functional": {
      // Populate with the functional colors
    }
  },
  "typography": {
    "fontFamily": {
      "primary": "Inter, sans-serif",
      "secondary": "DM Serif Display, serif"
    }
  },
  "spacing": {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem",
    "2xl": "3rem",
    "3xl": "4rem"
  },
  "borderRadius": {
    "sm": "0.125rem",
    "md": "0.25rem",
    "lg": "0.5rem",
    "xl": "1rem",
    "full": "9999px"
  }
}
```

---

**FINAL CHECK:**

Ensure the entire output is a single, clean markdown file. Do not include any conversational text outside of the generated document. The structure, headings, code blocks, and JSON object must precisely mirror the instructions.

### **PROMPT END**
