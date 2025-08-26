<goal>
I'd like for you to help me brainstorm the overall structure of my application. You should act like a Senior Software Engineer that has extensive experience developing, and building architecture for large scale web applications. You should ask me follow up questions as we proceed if you think it's necessary to gather a fuller picture.

To accomplish this, you take the Context below, considering:
What I’m trying to build (WHAT)
Who I’m building it for (WHO)
The pains it solves (WHY)
How it’s different from the current status quo (HOW)
Any other details I give you
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
An image detailing a full system diagram of the MVP. Please create a clean SVG architecture diagram with color-coded layers, rounded containers, and clear component relationships, similar to the one attached image

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
I’d like to build a [mobile app, web app, etc] that is a [one liner elevator pitch]. 

You should take inspiration from apps like [inspiration], but it will be significantly different for the following reasons:

[add core points of differentiation that you think make this app unique]

Here is the full extent of how the app should function as an MVP:

[bulleted list of the high-level user flow through your app as you see it]

<other-critical-notes>
WHAT - per my intro above, I’m building a [one liner]
WHO - this app is for [audience]
WHY - this app solves the problem that [pain]
HOW - this app is different from others in that [differentiator]
</other-critical-notes>
<current-tech-choices>
The frontend will be built in React Native using Expo
The backend will be built in Node.js using NestJS
The database will be Postgres, hosted through Supabase
The server will be hosted on AWS App Runner
I’d like to develop locally with a Docker container
I will use Posthog for analytics in my application
I will use Stripe for payments in my application
</current-tech-choices>

</context>
