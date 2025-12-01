Take the output above, and apply this logic to it. Your output should follow the output format from “EXAMPLE OUTPUT STRUCTURE”
Input Processing
When given app feature documentation, extract and reorganize ONLY design-relevant information:
Required Design Foundation
App Vibe: 2-3 descriptive adjectives (e.g., "minimalist and focused", "vibrant and encouraging")
Primary Background: Light or dark
Primary Color: Hex code
Primary Corner Radius: Specify (e.g., "fully rounded", "2px", "sharp corners")
Typography: Font style/personality (e.g., "playful sans-serif", "elegant serif for headings")
Screen-by-Screen Organization
Structure each screen as a "feature show" - a specific state or view of the feature. Include:
Screen [Number] - [Screen Name/State]
Purpose: One sentence describing user goal
Core Components: Specific UI elements (use keywords like "navigation bar," "call-to-action button," "card layout")
Key Interactions: Primary user actions on this screen
Image/Visual Guidance: Describe desired imagery style or content
Specific Details: Colors, spacing, or styling unique to this screen
Output Format: Stitch-Ready Prompts
Generate prompts following Stitch best practices:
1. Initial High-Level Prompt
"[App type] for [target users] to [core functionalities]. [Vibe adjectives]. 
Primary color: [hex]. [Background type] background. [Corner radius style]. [Font description]."

Example: "An app for marathon runners to find training partners, get coaching advice, and discover races. Vibrant and encouraging. Primary color: #FF6B35. Light background. Fully rounded corners. Modern sans-serif font."
2. Screen-Specific Refinement Prompts
For each screen, create one focused prompt per screen that includes:
Screen identifier
1-2 specific changes maximum
Clear, actionable instructions
Reference to specific UI elements
Format:
"[Screen name]: [Specific component/element] should [specific change]. [Optional: Additional styling detail]."

Examples:
"Partner Discovery screen: Add a filter bar below the header with options for distance, pace, and availability. Use primary brand color for selected filters."
"Training Plan detail page: Display coach photo as a circular avatar in the top left. Background should be a subtle gradient from white to light gray."
"Race Results screen: Show finish time in large, bold numbers at the top. Medal icon should be gold-colored, positioned to the left of the time."
3. Image-Specific Prompts
When features require specific imagery:
"On [screen name], [specific image location/element]: [describe desired style/content of image]. [Optional: How it relates to theme]."

Examples:
"On Training Dashboard, hero background image: Use macro photography of running shoes on a track, warm morning light, slightly blurred."
"Partner profile cards: Profile photos should have a subtle blue border matching primary color, with activity type icon overlay in bottom right."
Stitch Best Practices Applied
✅ DO:
Start with one comprehensive high-level prompt including vibe, colors, and structure
Iterate screen-by-screen with specific, incremental changes
Use precise UI/UX terminology (header, CTA button, card layout, navigation bar)
Describe image style/content clearly
Reference exact elements ("primary button on sign-up form" not "the button")
Make one major change per prompt for complex screens
❌ DON'T:
Include backend logic, API details, or technical implementation
Use ambiguous terms like "make it better" or "improve design"
Try to change multiple screens in one prompt
Leave image descriptions vague ("nice photo" → specify style/subject)
Example Output Structure
=== FOUNDATION ===
"Community-driven fitness app for marathon runners. Vibrant and encouraging. 
Primary color: #FF6B35. Light background with subtle texture. 
Fully rounded corners on all buttons and cards. Clean sans-serif font."

=== SCREEN 1: Partner Discovery ===
"Partner Discovery feed: Display runner cards in a 2-column grid. Each card shows 
profile photo (circular), name, pace range, and preferred distance. Primary CTA 
button says 'Connect' in brand orange."

=== SCREEN 2: Individual Partner Profile ===
"Partner profile detail: Hero section at top with banner image showing their favorite 
running route (map-style imagery). Profile photo overlaps banner as large circular 
avatar. Stats displayed as three columns below: total runs, avg pace, preferred time."

=== SCREEN 3: Training Dashboard ===
"Training Dashboard home: Large progress ring showing weekly mileage in center. 
Background should be a soft gradient from white to light peach. Upcoming workouts 
listed as cards below with workout type icon, distance, and scheduled time."


Usage: Feed your technical feature stories into this framework, and output clean, Stitch-optimized design prompts that follow Google's best practices for incremental, specific, screen-by-screen design iteration
