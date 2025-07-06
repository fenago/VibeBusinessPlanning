# Universal API Implementation Guide Generator (Full-Stack)

## Template Prompt for Converting Any API Documentation into Comprehensive Windsurf Implementation with Frontend/Backend Separation

---

**COPY THIS ENTIRE PROMPT AND CUSTOMIZE THE INPUT VARIABLES BELOW:**

---

You are an expert full-stack developer and system architect. I need you to analyze the provided API documentation and create a comprehensive, production-ready implementation guide as a series of detailed Windsurf prompts with clear frontend/backend separation using Netlify Functions.

## INPUT VARIABLES (Customize these for your specific API):

**API_NAME**: [e.g., "Stripe", "VAPI", "OpenAI", "Twilio"]
**API_DOCS_URL**: [e.g., "https://docs.stripe.com/api", "https://docs.vapi.ai/api-reference"]
**BUSINESS_NAME**: [e.g., "PaymentFlow.com", "AgenticVoice.net", "AIAssistant.pro"]
**PRIMARY_ENTITY**: [e.g., "customer", "user", "account", "project"]
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

## ARCHITECTURE OVERVIEW:

### Frontend (React + Netlify)
**Location**: `/src/` directory
**Deployment**: Netlify static hosting
**Responsibilities**:
- User interface and interactions
- State management and UI logic
- Form validation and user feedback
- Real-time updates and notifications
- Responsive design and accessibility
- Client-side routing and navigation

### Backend (Netlify Functions)
**Location**: `/netlify/functions/` directory
**Deployment**: Netlify serverless functions
**Responsibilities**:
- API key management and security
- Third-party API calls and data processing
- Authentication and authorization
- Data transformation and business logic
- Error handling and logging
- Rate limiting and caching

---

## FRONTEND/BACKEND SEPARATION GUIDELINES:

### 🎨 **FRONTEND COMPONENTS** (React)

**What Goes in Frontend:**
```
/src/
├── components/           # Reusable UI components
├── pages/               # Route-based page components
├── context/             # React Context for state management
├── hooks/               # Custom React hooks
├── utils/               # Client-side utilities
├── styles/              # CSS and styling
└── services/            # Frontend API client (calls backend functions)
```

**Frontend Responsibilities:**
- ✅ UI rendering and user interactions
- ✅ Form validation and input handling
- ✅ Client-side state management
- ✅ Real-time UI updates and notifications
- ✅ Responsive design and accessibility
- ✅ Client-side routing and navigation
- ✅ Local storage and session management
- ✅ User feedback and loading states

**Frontend Security:**
- ❌ NO API keys or secrets
- ❌ NO direct third-party API calls
- ❌ NO sensitive business logic
- ✅ Environment variables for public config only
- ✅ Input validation (with backend verification)
- ✅ XSS protection and sanitization

### ⚙️ **BACKEND FUNCTIONS** (Netlify Functions)

**What Goes in Backend:**
```
/netlify/functions/
├── api/                 # API endpoint handlers
│   ├── [entity]/        # Entity-specific operations
│   ├── auth/            # Authentication functions
│   ├── webhooks/        # Webhook handlers
│   └── utils/           # Shared backend utilities
├── scheduled/           # Cron job functions
└── middleware/          # Shared middleware
```

**Backend Responsibilities:**
- ✅ API key storage and management
- ✅ Third-party API calls and integration
- ✅ Authentication and authorization
- ✅ Data processing and transformation
- ✅ Business logic and validation
- ✅ Error handling and logging
- ✅ Rate limiting and caching
- ✅ Webhook processing
- ✅ Scheduled tasks and automation

**Backend Security:**
- ✅ Secure API key storage in environment variables
- ✅ Input validation and sanitization
- ✅ CORS configuration
- ✅ Rate limiting and abuse prevention
- ✅ Error logging without exposing secrets
- ✅ Authentication token validation

---

## IMPLEMENTATION REQUIREMENTS:

Create a comprehensive implementation guide with the following specifications:

### 1. API Research and Documentation
- Research ALL available API endpoints from the provided documentation
- Document request/response structures, authentication, and rate limits
- Identify all service categories and their relationships
- Map out the complete API surface area
- Include links to API testing interfaces (if available)
- **Categorize endpoints by frontend/backend responsibility**

### 2. Entity-Centric Design Philosophy
- Design around the PRIMARY_ENTITY perspective (single [entity] view)
- Create a comprehensive [entity] detail view as the most important interface
- Implement [entity]-specific filtering across ALL API services
- Ensure complete [entity] data isolation and tracking
- Provide 360° [entity] overview with all API services represented

### 3. Full-Stack Implementation Structure
Create **25+ detailed Windsurf prompts** with this progression:

**Foundation (Prompts 1-4):**
- Project setup with Netlify deployment structure
- Backend API client and Netlify Functions setup
- Frontend authentication and API client
- [Entity]-specific dashboard with real-time metrics

**Backend Infrastructure (Prompts 5-9):**
- Core API integration functions
- Authentication and security middleware
- Data processing and transformation functions
- Error handling and logging systems
- Webhook and integration handlers

**Frontend Core (Prompts 10-14):**
- Main UI components and pages
- [Entity] management interfaces
- Real-time monitoring dashboards
- Form handling and validation
- Navigation and routing

**Advanced Backend (Prompts 15-19):**
- Analytics and reporting functions
- Scheduled tasks and automation
- Advanced data processing
- Integration testing and monitoring
- Performance optimization

**Advanced Frontend (Prompts 20-25):**
- **[Entity] Detail View** (MOST IMPORTANT - comprehensive single [entity] perspective)
- Settings and [BUSINESS_NAME] branding configuration
- Advanced UI components and interactions
- API testing interface integration
- Comprehensive error handling and user feedback
- Final integration and production deployment

### 4. Netlify-Specific Implementation

**Project Structure:**
```
project-root/
├── src/                     # Frontend React app
├── netlify/functions/       # Backend serverless functions
├── public/                  # Static assets
├── netlify.toml            # Netlify configuration
├── package.json            # Dependencies
└── .env.example            # Environment variables template
```

**Netlify Configuration:**
```toml
[build]
  publish = "dist"
  command = "npm run build"
  functions = "netlify/functions"

[build.environment]
  NODE_VERSION = "18"

[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
```

**Environment Variables:**
```bash
# Backend (Netlify Functions)
[API_NAME]_API_KEY=your_api_key_here
[API_NAME]_WEBHOOK_SECRET=your_webhook_secret
DATABASE_URL=your_database_url
JWT_SECRET=your_jwt_secret

# Frontend (Public)
REACT_APP_API_BASE_URL=/.netlify/functions
REACT_APP_BUSINESS_NAME=[BUSINESS_NAME]
```

### 5. Prompt Structure Requirements
Each prompt must include:

**Context Section:**
- Clear explanation of frontend vs backend responsibilities
- How components interact across the stack
- Dependencies on previous prompts

**Implementation Details:**
- **Frontend**: Complete React components with hooks and context
- **Backend**: Complete Netlify Functions with error handling
- **Integration**: How frontend calls backend functions
- **Security**: Proper separation of concerns

**File Structure:**
```
Prompt X: [Feature Name]

Frontend Implementation:
/src/components/[Component].jsx
/src/pages/[Page].jsx
/src/context/[Context].jsx

Backend Implementation:
/netlify/functions/api/[endpoint].js
/netlify/functions/utils/[utility].js

Integration:
/src/services/[service].js
```

### 6. Security and Performance Guidelines

**Frontend Security:**
- Input validation with immediate feedback
- XSS protection and content sanitization
- Secure local storage practices
- HTTPS enforcement
- Content Security Policy headers

**Backend Security:**
- API key rotation and management
- Rate limiting per endpoint
- Input validation and sanitization
- CORS configuration
- Error logging without secret exposure
- Authentication token validation

**Performance Optimization:**
- Frontend: Code splitting, lazy loading, caching
- Backend: Function optimization, cold start reduction
- Database: Query optimization, connection pooling
- CDN: Static asset optimization
- Monitoring: Performance metrics and alerting

### 7. Testing and Validation

**Frontend Testing:**
- Component unit tests
- Integration tests for user flows
- Accessibility testing
- Cross-browser compatibility
- Mobile responsiveness

**Backend Testing:**
- Function unit tests
- API integration tests
- Security vulnerability testing
- Performance and load testing
- Error handling validation

**End-to-End Testing:**
- Complete user workflow testing
- [Entity] management scenarios
- Error recovery testing
- Performance under load
- Security penetration testing

### 8. Deployment and Monitoring

**Netlify Deployment:**
- Automated CI/CD pipeline
- Environment-specific configurations
- Function deployment and versioning
- Static asset optimization
- Domain and SSL configuration

**Monitoring and Logging:**
- Function performance monitoring
- Error tracking and alerting
- User analytics and behavior
- API usage and rate limiting
- Security event monitoring

---

## OUTPUT FORMAT:

Provide your response as a single, comprehensive markdown file with:

1. **Executive Summary** - Full-stack architecture overview
2. **API Research** - Complete endpoint documentation with frontend/backend mapping
3. **Architecture Design** - Detailed frontend/backend separation
4. **Project Setup** - Netlify configuration and structure
5. **Implementation Prompts** - 25+ detailed, sequential prompts
6. **Security Guidelines** - Frontend/backend security best practices
7. **Deployment Guide** - Netlify deployment procedures
8. **Monitoring Setup** - Performance and error monitoring

Each prompt should specify:
- **Frontend Components** - React components and UI logic
- **Backend Functions** - Netlify Functions and API integration
- **Integration Layer** - How frontend communicates with backend
- **Security Considerations** - Proper separation of sensitive operations
- **Testing Procedures** - Both frontend and backend validation

---

## EXAMPLE USAGE:

For Stripe API implementation:
- API_NAME: "Stripe"
- API_DOCS_URL: "https://docs.stripe.com/api"
- BUSINESS_NAME: "PaymentFlow.com"
- PRIMARY_ENTITY: "customer"

**Frontend**: Customer dashboard, payment forms, subscription management UI
**Backend**: Stripe API calls, webhook processing, payment validation, customer data management

**Result**: 25+ prompts for building a complete full-stack Stripe admin interface with proper security separation and Netlify deployment.

---

**BEGIN IMPLEMENTATION**: Research the provided API documentation and create the comprehensive full-stack implementation guide following this template structure with clear frontend/backend separation for Netlify deployment.

