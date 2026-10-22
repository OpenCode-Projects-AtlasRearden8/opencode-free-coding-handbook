# Chapter 5 — Writing Good Task Prompts

Bad prompts are the single biggest cause of "the AI is useless" experiences — and the fix costs nothing. This chapter gives you a formula, worked examples, and the little OpenCode mechanics (`@`, images, Plan mode) that turn decent prompts into great ones.

## The four-part prompt formula

Every good task prompt contains four ingredients. You do not need perfect style; you need all four present:

1. **Goal** — what you want to be true when the work is done.
2. **Context** — where the work happens (files, folders, examples of similar things).
3. **Constraints** — boundaries: what *not* to touch, style rules, keep it simple.
4. **Definition of done** — how you will check the result (a page opens, a test passes, a file is created).

A friendly way to remind yourself: *goal, where, guardrails, and how I'll know.*

## Bad and good, side by side

The jump from bad to good is smaller than you think — it is just the four parts, said out loud:

| Vague prompt | Good prompt |
|---|---|
| "Fix my website." | "Goal: the `/contact` page's form should send submissions to a local text file and show a success message. Context: it lives in `site/contact.html` and `js/contact.js`. Constraints: don't change other pages; keep styling as-is. Done: submitting the form produces a line in `submissions.txt` and a visible success note." |
| "Make the data cleaner." | "Goal: remove duplicate rows in `data/patients.csv` where `ID` matches, keeping the earliest `VisitDate`. Context: it's a CSV with a header row; dates are `YYYY-MM-DD`. Constraints: don't reorder rows otherwise; warn me how many duplicates you removed. Done: the output file has a count of removed rows and opens without errors." |
| "Add tests." | "Goal: add tests for the `slugify()` function in `src/text.js`. Context: test pattern for this project is `tests/*.test.js`; see `tests/none-yet`. Constraints: use the project's existing test style; no new dependencies. Done: `npm test` passes and covers empty strings, uppercase, and repeated dashes." |
| "Can it have a dark mode?" | "Goal: add a dark/light toggle to the reader page. Context: colours live in `style.css`; the toggle button can sit in the top-left of `reader.html`. Constraints: store the choice in `localStorage`; don't add frameworks. Done: toggling survives a page refresh." |

Notice what the good column is *not*: jargon-heavy, clever, or long. It is just explicit about the four parts. Beginners routinely under-specify the **definition of done**, which is the part the AI also uses to *check itself* before handing you work.

## Work across the table from your junior developer

Chapter 1's mental model pays off here. You would not say "make onboarding better" to a new hire and walk away. You would hand them a ticket. Write prompts like tickets:

- **One task per prompt.** Sequential, small asks beat a single giant wish. Small tasks also fit small context windows (relevant for free models, see Chapter 8) and produce reviewable diffs (Chapter 7).
- **Point at concrete things.** Use `@` while typing to reference real files (`@src/app.js`); OpenCode pulls the file into the AI's attention. Reference by-with example: "handle it like the other routes do in @packages/functions/src/notes.ts".
- **Invite questions.** "Before you start, ask me anything unclear" is a magic sentence. It converts silent wrong guesses into a short conversation you can afford.
- **Give constraints you care about but wouldn't think to say**: "plain JavaScript, no frameworks"; "don't reformat files I didn't mention"; "comments only where code isn't obvious"; "never edit files under `archive/`".
- **Let it propose, then choose.** For anything design-flavoured, ask for three options with trade-offs before building any. Choosing between sketches is easier than undoing a building.

## The Plan → Build drill

This rides on Chapter 1's loop but deserves its own drill, because it is *the* quality lever:

1. Press **Tab** into **Plan mode**.
2. Write the four-part prompt.
3. Read the plan as if grading someone's work. Fix: missing steps, wrong files touched, scope creep, anything it "assumed" that you did not say.
4. Iterate the plan with short replies ("step 2 should use the existing helper in `@utils/date.js`, not a new one").
5. When the plan matches your intent, **Tab** back to Build mode and say: "Approved — go ahead with exactly this plan."

Cost of all that: two minutes. Cost of not doing it: a bad half-hour of undoing. On free tiers this is also simply the cheapest way to spend tokens.

## A worked example (start to finish)

Task: you want to build a **soft-delete flow for notes** — the same example shape OpenCode's own documentation demonstrates, and a very common real-world need.

**In Plan mode:**

> Goal: when a user deletes a note, we flag it as deleted in the database instead of deleting it. Then add a "Recently deleted" screen where a note can be undeleted or permanently removed.
> Context: notes live in `src/notes/`; the database layer is `src/db.js`; see how the existing list view in `src/notes/list.js` is structured and match it.
> Constraints: no new dependencies; keep the UI style consistent; don't touch anything outside `src/notes/` and `src/db.js`.
> Done: deleting a note hides it from the main list, it appears under Recently deleted, undelete puts it back, permanent delete is possible but asks for confirmation.

Iterate the plan if needed. Then, in Build mode: "Approved — implement this plan."

After it builds: review (Chapter 7), run the app, and commit. A real feature, built by an AI, understood by you.

## Small-mechanic chapter: things OpenCode gives you for free in prompts

| Mechanic | Use |
|---|---|
| `@file` references | Pull specific files into context ("see how `@notes.ts` handles auth") |
| Drag-and-drop images | Screenshots of the design you want matched; error popups for debugging |
| Plan mode (Tab) | Force a review-first workflow |
| `/undo`, `/redo` | Cheap iteration: change the prompt, not the mess |
| `/init` + edits to `AGENTS.md` | Put *standing* preferences in `AGENTS.md` ("in `@AGENTS.md`: always answer in plain English") so you stop repeating them |
| Follow-up "why did you…?" | The best review engine is the chat itself — make the AI explain its own changes |

## Prompt anti-patterns to retire

Retire these habits now, with love:

| Anti-pattern | Why it fails | Replacement |
|---|---|---|
| "Make it good/professional/modern" | Untestable; guarantees generic output | Concrete description of the visible result |
| Ten tasks in one prompt | First three get done, rest forgotten, context fills | One ticket per prompt, sequenced |
| "You're an expert, just do it" | Confidence theatre; moves nothing | Provide the context and done-definition |
| No mention of files | AI wanders the project guessing | `@` references to real files |
| "Rewrite everything from scratch" | Throws away unreviewed value | Ask for a targeted change or an new module |
| Silence when unhappy | Rolls with the bad version | Say exactly what's wrong; re-prompt or `/undo` |

## Checklist: before you press Enter

Glance down this list when you finish typing any prompt:

- [ ] The **goal** is a result, not a mood
- [ ] **Context**: real files are referenced (with `@` where possible)
- [ ] **Constraints** that matter are stated (scope, style, no-new-deps)
- [ ] **Definition of done** is checkable by *you*, not just the AI
- [ ] It is **one task** (or an explicitly-sequenced plan)
- [ ] In Plan mode, if the change is bigger than a tweak
- [ ] Long-term preferences live in `AGENTS.md`, not in every prompt

That's the craft. Next chapter: the safety net beneath all of this.

---
