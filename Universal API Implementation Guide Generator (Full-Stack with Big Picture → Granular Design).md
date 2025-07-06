# Universal API Implementation Guide Generator (Full-Stack with Big Picture → Granular Design)

## Template Prompt for Converting Any API Documentation into Comprehensive Windsurf Implementation with Multi-Level Navigation

---

**COPY THIS ENTIRE PROMPT AND CUSTOMIZE THE INPUT VARIABLES BELOW:**

---

You are an expert full-stack developer and system architect. I need you to analyze the provided API documentation and create a comprehensive, production-ready implementation guide as a series of detailed Windsurf prompts with clear frontend/backend separation using Netlify Functions and a **Big Picture → Granular drill-down navigation hierarchy**.

## INPUT VARIABLES (Customize these for your specific API):

**API_NAME**: [e.g., "Stripe", "VAPI", "OpenAI", "Twilio"]
**API_DOCS_URL**: [e.g., "https://docs.stripe.com/api", "https://docs.vapi.ai/api-reference"]
**BUSINESS_NAME**: [e.g., "PaymentFlow.com", "AgenticVoice.net", "AIAssistant.pro"]
**PRIMARY_ENTITY**: [e.g., "customer", "user", "account", "project", "organization"]
**ENTITY_ID_FIELD**: [e.g., "customer_id", "user_id", "account_id", "project_id"]
**BUSINESS_CONTEXT**: [e.g., "payment processing business", "voice AI service provider", "content creation platform"]
**ADMIN_INTERFACE_PURPOSE**: [e.g., "manage customer payments and subscriptions", "monitor voice AI interactions", "oversee content generation"]

**METADATA_STRUCTURE**: 
```json
{
  "[ENTITY_ID_FIELD]": "[example_id]",
  "user_id": "[user_mongo_id]", 
  "billing_entity": "[billing_system]",
  "user_email": "[user@example.com]",
  "user_name": "[User Name]",
  "created_by_system": "[BUSINESS_NAME]"
}
```

**ADDITIONAL_CONTEXT**: [Any specific requirements, integrations, or business rules]

---

## CORE DESIGN PHILOSOPHY: BIG PICTURE → GRANULAR NAVIGATION

### 📊 **Level 1: Big Picture Views** (System-Wide Business Intelligence)
**Purpose**: Executive dashboard for business management and high-level decision making

**Views Include**:
- **Business Overview**: Total revenue, [entities], system performance across all accounts
- **System Metrics**: Overall success rates, usage trends, resource utilization
- **[Entity] Portfolio**: All [entities] with comparative performance analysis
- **Financial Dashboard**: Revenue by service, cost analysis, billing insights
- **Resource Management**: All system resources and their utilization

**Navigation**: Click any metric or [entity] to drill down to Level 2

### 👤 **Level 2: [Entity] Views** ([Entity]-Specific Management)
**Purpose**: Complete management of individual [entities] with full service context

**Views Include**:
- **[Entity] Detail**: 360° view of one [entity]'s complete API usage
- **[Entity] Comparison**: Side-by-side [entity] performance analysis
- **[Entity] Journey**: Timeline of [entity] interactions and growth
- **[Entity] Analytics**: Detailed performance metrics and trends
- **[Entity] Management**: CRUD operations and configuration

**Navigation**: Click any service or transaction to drill down to Level 3

### 🔍 **Level 3: Granular Views** (Service-Specific Details)
**Purpose**: Detailed analysis and management of individual transactions/items

**Views Include**:
- **Individual Transactions**: Detailed transaction analysis and logs
- **Service Performance**: Specific service metrics and optimization
- **Resource Details**: Individual resource configuration and usage
- **Error Analysis**: Detailed error investigation and resolution
- **Audit Trails**: Complete activity logs and compliance tracking

**Navigation**: Breadcrumb navigation back to any level

---

## ARCHITECTURE OVERVIEW:

### 🎨 **Frontend (React + Netlify Static)**
**Location**: `/src/` directory
**Deployment**: Netlify static hosting
**Responsibilities**:
- Multi-level dashboard navigation
- Real-time data visualization
- Interactive drill-down interfaces
- Responsive design across all view levels
- State management for navigation context

### ⚙️ **Backend (Netlify Functions)**
**Location**: `/netlify/functions/` directory
**Deployment**: Netlify serverless functions
**Responsibilities**:
- API key management and security
- Data aggregation for big picture views
- [Entity]-specific data filtering
- Granular data processing and analysis
- Business logic and calculations

---

## FRONTEND/BACKEND SEPARATION GUIDELINES:

### 🎨 **FRONTEND COMPONENTS** (React)

**Project Structure**:
```
/src/
├── components/
│   ├── common/              # Shared components across all levels
│   ├── bigpicture/          # Big picture view components
│   │   ├── BusinessOverview.jsx
│   │   ├── SystemMetrics.jsx
│   │   ├── [Entity]Portfolio.jsx
│   │   └── FinancialDashboard.jsx
│   ├── [entity]/            # [Entity]-specific components
│   │   ├── [Entity]Detail.jsx
│   │   ├── [Entity]Comparison.jsx
│   │   ├── [Entity]Analytics.jsx
│   │   └── [Entity]Management.jsx
│   └── granular/            # Detailed view components
│       ├── TransactionDetails.jsx
│       ├── ServiceAnalysis.jsx
│       ├── ResourceDetails.jsx
│       └── AuditTrails.jsx
├── pages/
│   ├── BigPicture/          # Level 1 pages
│   ├── [Entity]/            # Level 2 pages
│   └── Granular/            # Level 3 pages
├── context/
│   ├── NavigationContext.jsx  # Multi-level navigation state
│   ├── [Entity]Context.jsx    # [Entity] management state
│   └── ViewContext.jsx        # Current view level state
├── hooks/
│   ├── useNavigation.js     # Navigation between levels
│   ├── useDrillDown.js      # Drill-down functionality
│   └── useBreadcrumbs.js    # Breadcrumb management
└── services/
    ├── bigPictureService.js # Big picture API calls
    ├── [entity]Service.js   # [Entity]-specific API calls
    └── granularService.js   # Detailed data API calls
```

### ⚙️ **BACKEND FUNCTIONS** (Netlify Functions)

**Project Structure**:
```
/netlify/functions/
├── api/
│   ├── bigpicture/          # System-wide data aggregation
│   │   ├── overview.js      # Business overview metrics
│   │   ├── metrics.js       # System performance metrics
│   │   ├── [entities].js    # All [entities] portfolio
│   │   └── financial.js     # Financial dashboard data
│   ├── [entities]/          # [Entity]-specific operations
│   │   ├── list.js          # List all [entities]
│   │   ├── detail.js        # Individual [entity] details
│   │   ├── analytics.js     # [Entity] analytics
│   │   └── management.js    # [Entity] CRUD operations
│   ├── granular/            # Detailed data processing
│   │   ├── transactions.js  # Individual transaction details
│   │   ├── services.js      # Service-specific analysis
│   │   ├── resources.js     # Resource details
│   │   └── audit.js         # Audit trail processing
│   └── auth/                # Authentication functions
├── utils/
│   ├── [api]Client.js       # Third-party API client
│   ├── dataAggregator.js    # Data aggregation utilities
│   ├── [entity]Filter.js    # [Entity] filtering logic
│   └── analytics.js         # Analytics calculations
└── middleware/
    ├── auth.js              # Authentication middleware
    ├── rateLimit.js         # Rate limiting
    └── cors.js              # CORS configuration
```

---

## IMPLEMENTATION REQUIREMENTS:

### 1. Multi-Level Navigation Architecture

**Navigation Flow**:
```
Big Picture Overview
├── Business Metrics → [Entity] Portfolio → Individual [Entity] Detail
├── System Performance → Service Analysis → Individual Service Detail
├── Financial Dashboard → [Entity] Revenue → Transaction Details
└── Resource Management → Resource Categories → Individual Resources
```

**State Management**:
- **Navigation Context**: Current level, breadcrumbs, drill-down history
- **[Entity] Context**: Selected [entity], comparison sets, filters
- **View Context**: Active view, data refresh state, user preferences

### 2. Data Aggregation Strategy

**Big Picture Level**:
- Aggregate all API data across [entities]
- Calculate system-wide KPIs and metrics
- Identify trends and patterns
- Generate executive summaries

**[Entity] Level**:
- Filter all data by specific [entity]
- Calculate [entity]-specific metrics
- Compare [entity] performance
- Track [entity] journey and growth

**Granular Level**:
- Detailed individual item analysis
- Service-specific performance metrics
- Error analysis and debugging
- Audit trails and compliance data

### 3. Implementation Structure
Create **30+ detailed Windsurf prompts** with this progression:

**Foundation (Prompts 1-5):**
- Project setup with multi-level architecture
- Backend API client and data aggregation
- Frontend navigation framework
- Authentication and security
- Basic big picture dashboard

**Big Picture Views (Prompts 6-12):**
- Business overview dashboard
- System metrics and performance
- [Entity] portfolio management
- Financial analytics dashboard
- Resource utilization overview
- Comparative analytics
- Executive reporting

**[Entity] Views (Prompts 13-20):**
- [Entity] detail comprehensive view
- [Entity] analytics and insights
- [Entity] comparison tools
- [Entity] management interface
- [Entity] journey tracking
- [Entity] performance optimization
- [Entity] relationship mapping
- [Entity] lifecycle management

**Granular Views (Prompts 21-28):**
- Individual transaction analysis
- Service-specific deep dives
- Resource detail management
- Error investigation tools
- Audit trail interfaces
- Performance debugging
- Compliance reporting
- Data export and integration

**Advanced Features (Prompts 29-35):**
- Advanced analytics and ML insights
- Automated alerting and monitoring
- Custom dashboard creation
- API testing and validation
- Settings and configuration
- User management and permissions
- Final integration and deployment

### 4. Navigation UX Patterns

**Drill-Down Interactions**:
- **Click Metrics**: Navigate from big picture to relevant detail
- **Entity Selection**: Choose [entity] to view their complete profile
- **Service Deep-Dive**: Click services to analyze individual performance
- **Breadcrumb Navigation**: Easy return to any previous level
- **Context Preservation**: Maintain filters and selections across levels

**Visual Hierarchy**:
- **Big Picture**: Executive dashboards with high-level KPIs
- **[Entity] Level**: Detailed cards and comprehensive views
- **Granular Level**: Tables, logs, and detailed analysis interfaces

### 5. Example Navigation Flows

**For Stripe Implementation**:
```
Big Picture: Payment Overview
├── Total Revenue → Customer Portfolio → Customer Payment History
├── Transaction Volume → Payment Methods → Individual Transactions
├── Success Rates → Failed Payments → Error Analysis
└── Subscription Revenue → Customer Subscriptions → Billing Details
```

**For OpenAI Implementation**:
```
Big Picture: AI Usage Overview
├── Total API Calls → Project Portfolio → Project Usage Details
├── Model Performance → Model Analytics → Individual Requests
├── Cost Analysis → Project Costs → Token Usage Details
└── Error Rates → Failed Requests → Error Investigation
```

**For Twilio Implementation**:
```
Big Picture: Communication Overview
├── Message Volume → Customer Communications → Message History
├── Call Analytics → Phone Numbers → Individual Calls
├── Delivery Rates → Failed Messages → Delivery Analysis
└── Cost Tracking → Usage by Service → Billing Details
```

### 6. Data Visualization Strategy

**Big Picture Level**:
- Executive KPI cards with trend indicators
- High-level charts and graphs
- System health indicators
- Comparative visualizations

**[Entity] Level**:
- [Entity] performance dashboards
- Timeline visualizations
- Comparative charts
- Detailed metrics displays

**Granular Level**:
- Detailed data tables
- Log viewers and analyzers
- Performance graphs
- Error investigation tools

---

## PROMPT STRUCTURE REQUIREMENTS:

Each prompt must include:

**Context Section:**
- Clear explanation of the view level (Big Picture/[Entity]/Granular)
- Navigation relationships to other levels
- Business value and use cases

**Implementation Details:**
- **Frontend**: React components for the specific view level
- **Backend**: Netlify Functions for data processing
- **Navigation**: Drill-down and breadcrumb functionality
- **Data Flow**: How data flows between levels

**Navigation Integration:**
```
Prompt X: [Feature Name] - [Level] View

Frontend Implementation:
/src/pages/[Level]/[Feature].jsx
/src/components/[level]/[Feature]Components.jsx

Backend Implementation:
/netlify/functions/api/[level]/[endpoint].js

Navigation:
- Drill-down targets: [specific navigation paths]
- Breadcrumb integration: [breadcrumb structure]
- Context preservation: [state management]
```

---

## OUTPUT FORMAT:

Provide your response as a single, comprehensive markdown file with:

1. **Executive Summary** - Multi-level architecture overview
2. **API Research** - Complete endpoint mapping to navigation levels
3. **Navigation Architecture** - Detailed drill-down flow design
4. **Data Aggregation Strategy** - How data flows between levels
5. **Implementation Prompts** - 30+ detailed, sequential prompts
6. **UX Guidelines** - Navigation patterns and user experience
7. **Performance Optimization** - Multi-level data loading strategies
8. **Testing Strategy** - Validation across all navigation levels

Each prompt should specify:
- **View Level**: Big Picture, [Entity], or Granular
- **Navigation Context**: How it connects to other levels
- **Data Requirements**: What data is needed and how it's processed
- **User Experience**: How users interact and navigate
- **Drill-Down Targets**: Where users can navigate from this view

---

## EXAMPLE USAGE:

For Stripe API implementation:
- API_NAME: "Stripe"
- PRIMARY_ENTITY: "customer"
- BUSINESS_NAME: "PaymentFlow.com"

**Big Picture Views**:
- Payment processing overview across all customers
- Revenue analytics and financial dashboards
- System performance and transaction success rates

**Customer Views**:
- Individual customer payment history and analytics
- Customer subscription management and billing
- Customer payment method and preference management

**Granular Views**:
- Individual transaction details and dispute resolution
- Payment method analysis and optimization
- Detailed error investigation and compliance reporting

**Result**: 30+ prompts for building a complete multi-level Stripe admin interface with intuitive drill-down navigation from business overview to transaction details.

---

**BEGIN IMPLEMENTATION**: Research the provided API documentation and create the comprehensive multi-level implementation guide following this template structure with Big Picture → [Entity] → Granular navigation hierarchy.

