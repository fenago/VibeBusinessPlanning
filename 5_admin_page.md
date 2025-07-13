### The Expert-Driven Admin Page Specifications Prompt

**Instructions for Use:**

1.  Copy the entire prompt below.
2.  Paste the complete markdown output from the "Research Summary" into the first placeholder.
3.  Paste the complete markdown output from the "Brand Identity & Design System" into the second placeholder.
4.  Provide the completed prompt to the AI.

---

### **PROMPT START**

**ROLE & GOAL:**

Act as a "Technical Product Syndicate," an integrated team of three senior experts tasked with creating the complete technical and functional specifications for a platform's Admin Page. Your team consists of:

1.  **The Product Manager:** Owns the features, user personas, requirements, and user flows.
2.  **The Lead Backend Architect:** Owns the database schema, API endpoints, security model, and system architecture.
3.  **The Lead UI/UX Designer:** Owns the page layout, component selection, and adherence to the established design system.

Your goal is to synthesize the provided `Research Summary` and `Brand Identity & Design System` documents into a comprehensive specification for the Admin Page. The final output must be a single markdown file, meticulously structured to match the provided sample's format, tone, and extreme level of detail.

**PRIMARY INPUTS:**

*   **Research Summary:**
    ```markdown
    [PASTE THE ENTIRE 'RESEARCH SUMMARY' MARKDOWN HERE]
    ```

*   **Brand Identity & Design System:**
    ```markdown
    [PASTE THE ENTIRE 'BRAND IDENTITY & DESIGN SYSTEM' MARKDOWN HERE]
    ```

**TASK: GENERATE THE ADMIN PAGE SPECIFICATIONS**

Produce the specifications document by collaborating as the Technical Product Syndicate. Each expert will contribute to their relevant sections, ensuring every decision is rooted in the provided input documents. Structure the output in markdown format precisely as follows:

---

`# [Business Name] Admin Page Specifications`
(Extract the business name from the input documents)

`## Overview`
(As a **Product Manager**, write a concise paragraph explaining the purpose of the Admin Page as the central control hub for the platform.)

`## User Personas`
(As a **Product Manager**, define two primary personas for this page:
    - **Primary User: Platform Administrator:** Detail their role, goals (managing users, subscriptions, system settings), and pain points.
    - **Secondary User: Support Administrator:** Detail their role, goals (assisting customers, resetting passwords), and pain points.)

`## Features and Functionality`
(As a **Product Manager**, detail the required features, adapting the business specifics from the Research Summary. Follow this exact structure.)
`### 1. User Management` (Directory, Detail View, Creation/Editing, Suspension/Deletion)
`### 2. Subscription and Pricing Management` (Adapt this section's title based on the business model. Detail Plan Configuration, Usage Monitoring, Billing Integration, and Promotional Tools.)
`### 3. Security and Compliance` (Role Management, Audit Logging, Compliance Settings, Security Settings)
`### 4. System Configuration` (Integration Management, Email/Notification Settings, Localization Settings, Branding Settings)

`## User Interface Design`
(As a **UI/UX Designer**, describe the UI, ensuring it aligns with the provided Brand & Design System.)
`### Layout` (Specify a responsive design with a left sidebar, header, main content area, and footer.)
`### Key UI Components` (List essential components for the Header, Navigation, and Content areas, referencing components like Data Tables, Cards, and Modals.)
`### Visual Design` (Explicitly state that the visual design *must* follow the provided Brand Identity & Design System, referencing its color palette, typography, and micro-interactions.)

`## Database Schema`
(As a **Lead Backend Architect**, define a normalized database schema to support all specified features. **You must provide the schema for the following tables in the exact format shown in the sample**, including columns, data types (e.g., UUID, VARCHAR, TIMESTAMP, JSONB), and keys (PK, FK).
- `Users Table`
- `Roles Table`
- `Permissions Table`
- `Role Permissions Table`
- `Subscription Plans Table`
- `Customer Subscriptions Table`
- `Usage Records Table`
- `Audit Logs Table`
)

`## Security Roles and Permissions`
(As a **Lead Backend Architect**, define a Role-Based Access Control (RBAC) model.)
`### Role Hierarchy` (Define at least 4-5 distinct roles, from a `Super Administrator` down to more limited roles like `Support` or `Billing`.)
`### Permission Categories` (Define granular permissions grouped by category (e.g., User Management, Subscription Management). Use the format `action:resource`, like `create:users` or `view:billing`.)

`## API Endpoints`
(As a **Lead Backend Architect**, define the necessary RESTful API endpoints. Group them by functionality and use standard HTTP verbs (`GET`, `POST`, `PUT`, `DELETE`).
- `User Management Endpoints`
- `Role Management Endpoints`
- `Subscription Management Endpoints`
- `System Configuration Endpoints`
- `Audit and Security Endpoints`
)

`## User Flows`
(As a **Product Manager**, describe the step-by-step process for at least three critical administrative tasks.)
`### User Management Flow`
`### Subscription Management Flow`
`### Role and Permission Management Flow`

`## Error Handling`
(As a team, list key error handling strategies, such as form validation, confirmation dialogs for destructive actions, and activity logging.)

`## Accessibility Considerations`
(As a **UI/UX Designer**, list key accessibility commitments, referencing WCAG 2.1 AA, keyboard navigation, and screen reader support.)

`## Implementation Notes`
(As a **Lead Backend Architect**, provide key technical guidance for development, such as implementing RBAC, using server-side rendering, and using WebSockets for real-time updates.)

`## Mermaid Diagrams`
(As a team, create four Mermaid diagrams to visually represent the system's structure. **You must generate the diagrams in the specified types and populate them with the data you defined in the sections above.**)

`### Admin Page Structure`
(Use a `graph TD` to show the high-level sections of the admin page.)

`### User Role Hierarchy`
(Use a `graph TD` to show the relationship between the defined security roles.)

`### Database Relationship Diagram`
(Use an `erDiagram` to model the relationships between the tables you defined in the Database Schema section.)

`### User Management Flow`
(Use a `sequenceDiagram` to illustrate the interaction between the Admin, UI, API, and Database for a common user management task like updating a user.)

---

**FINAL CHECK:**

Ensure the entire output is a single, clean markdown file. Do not include any conversational text. The structure, headings, code blocks, and Mermaid diagrams must precisely mirror the instructions and the provided sample document's depth and format.
