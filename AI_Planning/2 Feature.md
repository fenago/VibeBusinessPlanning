<goal>
You’re an industry-veteran software engineer responsible for crafting high-touch features for the largest FANG-style SaaS companies in the world. You excel at creating detailed technical specifications for features, and understanding how different features connect and nest within each other.

You must review the <context> below and use it to output a thorough, no-stone-unturned feature specification document

DO NOT WRITE CODE IN THIS OUTPUT UNLESS IT’S PSEUDOCODE FOR A TECHNICAL SITUATION

</goal>
<format>
Structure your output as follows:

## File System
Folder and file structure both front-end and back-end repositories


## Feature Specifications
### Feature N
Feature goal
Any API relationships
Detailed feature requirements
Detailed implementation guide

### Feature N+1
Feature goal
Any API relationships
Detailed feature requirements
Detailed implementation guide

</format>
<warnings-and-guidelines>
<warning-1>Do not leave out steps. This absolutely must be a step-by-step output that, when passed to a human, accurately describes in exact detail what needs built</warning-1>
<warning-2>This is not a code writing step. Only pseudocode if needed to guide the user. This is a stage of detailed feature specifications</warning-2>
<guideline-1>
For each FEATURE, make sure you also consider each of these items:

1. System Architecture Overview

High-level architecture diagram/description
Technology stack selection with justification
Deployment architecture
Integration points with external systems

2. Database Schema Design

Entity-relationship diagrams
Table definitions with all fields, types, and constraints
Indexing strategy
Foreign key relationships
Database migration/versioning approach

3. Comprehensive API Design

RESTful/GraphQL endpoints with full specifications
Request/response formats with examples
Authentication and authorization mechanisms
Error handling strategies and status codes
Rate limiting and caching strategies

4. Frontend Architecture

Component hierarchy with parent-child relationships
Reusable component library specifications
State management strategy
Routing and navigation flow
Responsive design specifications

5. Detailed CRUD Operations

For each entity:

Create operation: validation rules, required fields
Read operation: filtering, pagination, sorting
Update operation: partial updates vs. full replacement
Delete operation: soft delete vs. hard delete, cascading



6. User Experience Flow

User journey maps
Wireframes for key screens
State transitions and loading states
Error handling from user perspective

7. Security Considerations

Authentication flow details
Authorization matrix (roles and permissions)
Data validation and sanitization rules
Protection against common vulnerabilities (CSRF, XSS, etc.)

8. Testing Strategy

Unit test requirements
Integration test scenarios
End-to-end test flows
Performance testing thresholds

9. Data Management

Data lifecycle policies
Caching strategies
Pagination and infinite scrolling implementation
Real-time data requirements

10. Error Handling & Logging

Structured logging format
Error classification and prioritization
Monitoring and alerting thresholds
Recovery mechanisms
</guideline-1>
</warnings-and-guidelines>
<context>
Take your most recent output to me above as the main context for everything I’m asking you to do here. It’s imperative that your response is highly-detailed. I would prefer if you took serious time to think about your response, latency does not matter to me right now, only accuracy and quality.

Provide specific implementation guidelines at every step, with detailed, grounded examples.

If different features must interact with each other, you need to specify that in BOTH feature specifications.

For each feature, think through the full scope of CRUD operations associated with that feature.
</context>
