# Universal API Implementation Guide Generator - FIXED VERSION

## How to Use This Template

This template generates **self-contained, actionable prompts** for any API documentation. Each generated prompt includes complete context, clear instructions, and proper validation steps.

### Input Variables (Customize These)

```
API_NAME: [e.g., "Stripe", "OpenAI", "Twilio", "Shopify"]
API_DOCS_URL: [e.g., "https://docs.stripe.com/api", "https://platform.openai.com/docs/api-reference"]
BUSINESS_NAME: [e.g., "AgenticVoice.net", "PaymentFlow.com", "AIAssistant.io"]
PRIMARY_ENTITY: [e.g., "customer", "user", "project", "order"]
ENTITY_ID_FIELD: [e.g., "customer_id", "user_id", "project_id", "order_id"]
BUSINESS_CONTEXT: [e.g., "voice AI service provider", "e-commerce platform", "SaaS application"]
ADMIN_INTERFACE_PURPOSE: [e.g., "manage customer payments", "track user activity", "monitor project usage"]

BRAND_COLORS: [e.g., "Primary: #5073b8, Secondary: #1098ad, Accent: #f79533"]
BRAND_FONTS: [e.g., "Primary: Inter, Secondary: DM Serif Display"]
BRAND_GRADIENT: [e.g., "linear-gradient(60deg, #f79533, #f37055, #ef4e7b, #a166ab, #5073b8, #1098ad, #07b39b, #6fba82)"]
BRAND_VOICE: [e.g., "Professional, confident, solution-oriented"]
TARGET_AUDIENCE: [e.g., "Medical and legal practices", "E-commerce businesses", "SaaS companies"]
```

---

## UNIVERSAL PROMPT TEMPLATE

### PROMPT GENERATOR INSTRUCTIONS:

**Use this exact template structure for each generated prompt. Replace [VARIABLES] with the input values above.**

---

## Prompt [NUMBER]: [SPECIFIC_TASK_NAME] for [BUSINESS_NAME]

### CONTEXT FOR WINDSURF:
You are building a comprehensive [API_NAME] admin interface for [BUSINESS_NAME], a [BUSINESS_CONTEXT]. This interface will [ADMIN_INTERFACE_PURPOSE] using a **Big Picture → [PRIMARY_ENTITY] → Granular** navigation hierarchy.

### [BUSINESS_NAME] BRAND IDENTITY:
```
Business: [BUSINESS_CONTEXT]
Colors: [BRAND_COLORS]
Typography: [BRAND_FONTS]
Gradient: [BRAND_GRADIENT]
Voice: [BRAND_VOICE]
Target: [TARGET_AUDIENCE]
```

### ARCHITECTURE REQUIREMENTS:
- **Frontend**: React 18 with Tailwind CSS and DaisyUI
- **Backend**: Netlify Functions (no [API_NAME] keys in frontend)
- **Navigation**: Big Picture → [PRIMARY_ENTITY] → Granular drill-down
- **Security**: All [API_NAME] API calls through backend functions only

### [API_NAME] API ENDPOINTS FOR THIS TASK:
[List specific API endpoints with URLs and descriptions]

### TASK:
[Specific, detailed task description with clear deliverables]

### IMPLEMENTATION INSTRUCTIONS:

#### 1. [Step 1 Title]
[Detailed implementation instructions with code examples]

#### 2. [Step 2 Title]
[Detailed implementation instructions with code examples]

[Continue with all necessary steps...]

### VALIDATION STEPS:

**BEFORE MARKING THIS PROMPT COMPLETE, VERIFY:**

1. **[Validation Category 1]**:
   - [ ] [Specific validation item]
   - [ ] [Specific validation item]
   - [ ] [Specific validation item]

2. **[Validation Category 2]**:
   - [ ] [Specific validation item]
   - [ ] [Specific validation item]
   - [ ] [Specific validation item]

[Continue with all validation categories...]

**UI VALIDATION LOCATIONS:**
- [Specific URL]: [What should be visible/working]
- [Specific URL]: [What should be visible/working]

**API VALIDATION:**
- [Specific API test]: [Expected result]
- [Specific API test]: [Expected result]

**DO NOT PROCEED TO PROMPT [NEXT_NUMBER] UNTIL ALL VALIDATION ITEMS ARE CHECKED AND WORKING.**

---

## EXAMPLE USAGE

### Input Variables for Stripe:
```
API_NAME: Stripe
API_DOCS_URL: https://docs.stripe.com/api
BUSINESS_NAME: AgenticVoice.net
PRIMARY_ENTITY: customer
ENTITY_ID_FIELD: customer_id
BUSINESS_CONTEXT: voice AI service provider for professional practices
ADMIN_INTERFACE_PURPOSE: manage customer payments, subscriptions, and billing for voice AI services
BRAND_COLORS: Orange (#f79533), Blue (#5073b8), Teal (#1098ad), Green (#07b39b)
BRAND_FONTS: Inter (primary), DM Serif Display (headlines)
BRAND_GRADIENT: linear-gradient(60deg, #f79533, #f37055, #ef4e7b, #a166ab, #5073b8, #1098ad, #07b39b, #6fba82)
BRAND_VOICE: Professional, confident, solution-oriented
TARGET_AUDIENCE: Medical and legal practices using AI voice agents
```

### Generated Prompt Example:

---

## Prompt 1: Setup Stripe Admin Foundation for AgenticVoice.net

### CONTEXT FOR WINDSURF:
You are building a comprehensive Stripe admin interface for AgenticVoice.net, a voice AI service provider for professional practices. This interface will manage customer payments, subscriptions, and billing for voice AI services using a **Big Picture → Customer → Granular** navigation hierarchy.

### AGENTICVOICE.NET BRAND IDENTITY:
```
Business: Voice AI service provider for professional practices
Colors: Orange (#f79533), Blue (#5073b8), Teal (#1098ad), Green (#07b39b)
Typography: Inter (primary), DM Serif Display (headlines)
Gradient: linear-gradient(60deg, #f79533, #f37055, #ef4e7b, #a166ab, #5073b8, #1098ad, #07b39b, #6fba82)
Voice: Professional, confident, solution-oriented
Target: Medical and legal practices using AI voice agents
```

### ARCHITECTURE REQUIREMENTS:
- **Frontend**: React 18 with Tailwind CSS and DaisyUI
- **Backend**: Netlify Functions (no Stripe keys in frontend)
- **Navigation**: Big Picture → Customer → Granular drill-down
- **Security**: All Stripe API calls through backend functions only

### STRIPE API ENDPOINTS FOR THIS TASK:
- **Balance**: `GET /v1/balance` - Account balance and available funds
- **Customers**: `GET /v1/customers` - Customer list and management
- **Charges**: `GET /v1/charges` - Payment charges and processing
- **Subscriptions**: `GET /v1/subscriptions` - Recurring billing management

### TASK:
Create the complete project foundation with secure Stripe integration, AgenticVoice.net branding, and multi-level navigation framework.

### IMPLEMENTATION INSTRUCTIONS:

#### 1. Create Project Structure
```bash
mkdir stripe-admin-agenticvoice
cd stripe-admin-agenticvoice
npm init -y
npm install react react-dom react-router-dom @stripe/stripe-js stripe tailwindcss daisyui
```

[Continue with detailed implementation...]

### VALIDATION STEPS:

**BEFORE MARKING THIS PROMPT COMPLETE, VERIFY:**

1. **Project Structure**:
   - [ ] All files created in correct locations
   - [ ] Dependencies installed successfully
   - [ ] Netlify configuration present

[Continue with validation steps...]

**DO NOT PROCEED TO PROMPT 2 UNTIL ALL VALIDATION ITEMS ARE CHECKED AND WORKING.**

---

## PROMPT GENERATION PATTERNS

### For Different API Types:

#### Payment APIs (Stripe, PayPal, Square):
- Focus on revenue, transactions, customers, subscriptions
- Big Picture: Business metrics, revenue trends, customer portfolio
- Customer Level: Payment history, subscription management, billing
- Granular: Individual transactions, payment methods, disputes

#### Communication APIs (Twilio, SendGrid, Mailgun):
- Focus on messages, campaigns, contacts, analytics
- Big Picture: Message volume, delivery rates, campaign performance
- Customer Level: Contact management, message history, preferences
- Granular: Individual messages, delivery status, engagement metrics

#### AI/ML APIs (OpenAI, Anthropic, Cohere):
- Focus on usage, models, projects, costs
- Big Picture: API usage, cost analytics, model performance
- Project Level: Project-specific usage, model configurations, costs
- Granular: Individual API calls, token usage, response analysis

#### E-commerce APIs (Shopify, WooCommerce, BigCommerce):
- Focus on orders, products, customers, inventory
- Big Picture: Sales metrics, product performance, customer analytics
- Customer Level: Order history, customer lifetime value, preferences
- Granular: Individual orders, product details, inventory tracking

### Navigation Hierarchy Patterns:

#### 3-Level Structure:
```
Level 1 (Big Picture): Business/System Overview
├── Total metrics and KPIs
├── Trend analysis and growth
├── Top performers and insights
└── Recent activity feed

Level 2 ([PRIMARY_ENTITY]): Entity-Specific Management
├── Individual entity overview
├── Entity-specific metrics
├── Related data and history
└── Entity management actions

Level 3 (Granular): Detailed Item Analysis
├── Individual item details
├── Complete data breakdown
├── Related items and connections
└── Item-specific actions
```

### Validation Pattern Templates:

#### Backend Validation:
```
**Backend Function**:
- [ ] Function created at correct path: `/netlify/functions/api/[endpoint]`
- [ ] Function connects to [API_NAME] API successfully
- [ ] Function returns expected data structure
- [ ] Function handles errors gracefully
- [ ] Function includes [BUSINESS_NAME] metadata
```

#### Frontend Validation:
```
**Frontend Interface**:
- [ ] Page displays [BUSINESS_NAME] branding correctly
- [ ] Data loads from backend functions (not direct API calls)
- [ ] Interactive elements work (clicks, hovers, navigation)
- [ ] Loading states provide clear feedback
- [ ] Error handling displays user-friendly messages
```

#### API Validation:
```
**API Integration**:
- [ ] Direct function test: `curl http://localhost:8888/.netlify/functions/api/[endpoint]`
- [ ] Returns JSON with expected data structure
- [ ] [API_NAME] API calls are authenticated correctly
- [ ] Rate limiting and retry logic work
- [ ] Metadata injection works for [BUSINESS_NAME] tracking
```

### Brand Integration Patterns:

#### Color System:
```css
:root {
  --primary: [PRIMARY_COLOR];
  --secondary: [SECONDARY_COLOR];
  --accent: [ACCENT_COLOR];
  --gradient: [BRAND_GRADIENT];
}
```

#### Typography System:
```css
.font-primary { font-family: [PRIMARY_FONT]; }
.font-secondary { font-family: [SECONDARY_FONT]; }
```

#### Component Branding:
```jsx
// Header Component
<header className="bg-gradient-to-r from-primary via-secondary to-accent">
  <h1 className="font-secondary text-4xl font-bold">[BUSINESS_NAME]</h1>
  <p className="text-xl">[API_NAME] [ADMIN_INTERFACE_PURPOSE]</p>
</header>
```

---

## COMPLETE PROMPT SEQUENCE GENERATOR

### To Generate Full Implementation Guide:

1. **Research [API_NAME] Documentation**
   - Identify all API endpoints and categories
   - Understand data structures and relationships
   - Map API capabilities to business needs

2. **Plan Navigation Hierarchy**
   - Define Big Picture metrics and views
   - Identify [PRIMARY_ENTITY] management needs
   - Plan Granular detail requirements

3. **Generate 20+ Prompts Following Pattern**:
   - Prompts 1-5: Foundation and setup
   - Prompts 6-10: Big Picture dashboards
   - Prompts 11-15: [PRIMARY_ENTITY] management
   - Prompts 16-20: Granular detail views
   - Prompts 21-25: Advanced features and optimization

4. **Each Prompt Must Include**:
   - Complete context for Windsurf
   - [BUSINESS_NAME] brand identity
   - Specific [API_NAME] endpoints
   - Detailed implementation instructions
   - Self-contained validation steps

### Quality Checklist for Generated Prompts:

- [ ] Prompt is completely self-contained
- [ ] All necessary context included
- [ ] Clear instructions for LLM/Windsurf
- [ ] Brand identity properly integrated
- [ ] API endpoints specifically listed
- [ ] Implementation steps are detailed
- [ ] Validation steps are actionable
- [ ] Navigation hierarchy is maintained
- [ ] Security best practices included
- [ ] Error handling is addressed

---

## USAGE INSTRUCTIONS

1. **Customize Input Variables** for your specific API and business
2. **Research API Documentation** thoroughly to understand all endpoints
3. **Apply Template Pattern** to generate each prompt
4. **Ensure Self-Containment** - each prompt should work independently
5. **Test Generated Prompts** with Windsurf to verify they work
6. **Iterate and Improve** based on results

This template ensures every generated prompt is actionable, self-contained, and produces production-ready admin interfaces with proper branding and navigation hierarchy.

