<goal>
I'd like for you to help me brainstorm the overall structure of my application. You should act like a Senior Software Engineer that has extensive experience developing, and building architecture for large scale web applications. You should ask me follow up questions as we proceed if you think it's necessary to gather a fuller picture.
To accomplish this, you take the Context below, considering:
What I’m trying to build (WHAT)
Who I’m building it for (WHO)
The pains it solves (WHY)
How it’s different from the current status quo (HOW)
Any other details I give you
<sub-goal>
As part of your process, make sure to research public documentation for each tech choice we’re making to ensure it makes sense in the broader context of our application.
</sub-goal>
</goal>
<format>
Return your format in Markdown, without pre-text or post-text descriptions.
## Launch Features (MVP)
### Feature Name
**Strong** 2-3 sentence summary of what the feature is or does
* List
* Of
* Core
* Requirements or Functions
#### Tech Involved
* Main Technologies Involved w/ Feature
#### Main Requirements
* Any
* Requirements
* Of Feature
## Future Features (Post-MVP)
### Feature Name
* List
* Of
* Core
* Requirements or Functions
#### Tech Involved
* Main Technologies Involved w/ Feature
#### Main Requirements
* Any
* Requirements
* Of Feature
## System Diagram
An image detailing a full system diagram of the MVP. Please create a clean architecture diagram with layers, rounded containers, and clear component relationships, similar to the one attached image
## Questions & Clarifications
* list
* of
* clarifying
* questions
## List of Architecture Consideration Questions
* list
* of
* Architecture
* questions
</format>
<warnings-or-guidance>
We’re focusing on functional accomplishments of features in this stage, not designing UX in detail
If a feature or tech choice seems ambiguous, ask me for clarification such that you would get what you need to continue
You should consider how tech choices may evolve or change if the application scales and give me recommendations with tradeoff consideration
We should have a clear architecture for the app, including main infrastructure considerations, services/microservices required, critical 3rd party APIs choices, etc
</warnings-or-guidance>
<context>
I’d like to build a mobile app that is a modern day news app that gives users control to curate personal news stories and turn them into bite-sized 5-10 minute briefings
You should take inspiration from apps like Spotify & Feedly but it will be significantly different for the following reasons:
- This is an "AI-first" approach to news curation
- The app combines users news feeds together to create short-form news stories as podcast clips
- The app can scrub bias out of news stories and only report facts
- The user can "chat" with stories to dive deeper into details and learn more as they see fit
- The user can view history about a news story which pulls timelines of how we came to be where we are
Here is the full extent of how the app should function as an MVP:
1. User opens app for first time, onboards by selecting topics they're interested in
2. Once in app, user has a feed of news stories, listed as "scrubbed" headlines (scrubbed meaning all bias language removed from headline)
3. User can click in to one of them, which pops open a new video that lets them read bulleted facts about the story
4. User can chat with an AI to ask anything more about it
5. A separate tab at bottom has a different feed, but this time its curated list of "for you" podcast style clips combining stories across all the stuff they care about into a "5 o-clock news" style of segment
6. A separate tab at bottom has a "deep research" style chat interface where someone can insert a story from their feeds and then ask the system to give them a deeper analysis into the event
7. Profile section where different things can get configured
<other-critical-notes>
WHAT - per my intro above, I’m building an AI-first news app 
WHO - this app is for open-minded critical thinkers that are distrustful of modern news cycles
WHY - this app solves the problem that most news outlets are politically biased and dishonest in their reporting, often passing off opinions as facts, or intentionally framing events to rile up their base
HOW - this app is different from others in that it enables deep exploration of actual facts behind scenarios, allowing users to draw their own opinions
</other-critical-notes>
<current-tech-choices>
The frontend will be built in React Native using Expo
The backend will be built in Node.js using Express
The database will be Postgres, hosted through Supabase
The server will be hosted on AWS App Runner
I’d like to develop locally with a Docker container
I will use Posthog for analytics in my application
I will use Stripe for payments in my application
</current-tech-choices>
</context>


