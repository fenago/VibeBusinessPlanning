<goal>
Attached is a PRD we made. I need you to create a very LIGHTWEIGHT series of epics and stories
</goal>

<warnings> 
I don't need verbose data models and api contracts
I just need the features deconstructed into EPICs and STORIES with just the core functional and non-functional requirements in it.
Each epic/story should be a clear separation. Meaning, there should be no duplication on efforts across epics/stories
</warnings>
<guidelines>
Feature / Initiative = user-visible capability or business outcome (e.g., “AI Chat Assistant”).
Epics = major deliverables or flows realizing that feature (chat UX, context layer, prompt logic).
Stories = increments completing an epic’s acceptance criteria.
Ensure UX is a first-class citizen, meaning epic-level, story-level, and task-level UX
The output’s root README should explain that designs may or may not be included. If it’s there, it should be read, the user should be asked to provide thoughts on the feature function when the LLM goes to build implementation plans. It should explain to LLMs that details of each feature for the stories are found in the PRD
</guidelines>

<format>
I need it all inside of a zip file, organized by feature, with epics & stories inside. There should be a folder within each epic for any reference images (think of it like design snapshots from a product designer), integrated into the Epic/Story definitions. It should look like this:

/docs
→ README.md (explains the structure of the directory to an LLM)
→ features
→ → epic-name
→ → → /story-name
→ → → → story-spec (contains relevant references to feature stories, like “F3”)
→ → → → story-images
→ → → epic-images
→ pm-notes
→ → PRD
</format>

If you have clarifying questions about details, ask me NOW
