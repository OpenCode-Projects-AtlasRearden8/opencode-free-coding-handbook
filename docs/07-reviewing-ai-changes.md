# Chapter 7 — Reviewing AI Changes

If prompts are how you direct the AI, review is how you keep your project *yours*. Skipping review is how people end up with folders they no longer understand. This chapter gives you a light, repeatable review routine — light enough that you'll actually do it every time.

## The mindset

Treat every AI change like a **pull request from a new coworker**: competent, fast, occasionally wrong about details, always acting in good faith. You don't read it looking for evil; you read it looking for **misunderstandings**. Then — and this is the part people forget — you are the one signing the work. "The AI wrote it" is not a defence anywhere in life.

## Step 1: See what changed (`git diff`)

The review always starts in the same place:

```bash
git diff          # unsaved changes, line by line
git diff --stat   # just the file list and sizes first
```

Reading order that works:

1. `--stat` first — how many files? Does the *scope* match the task? (You asked for a dark-mode toggle and it touched 14 files? Ask why before reading anything.)
2. Then read the diff of each changed file top to bottom. Lines starting with `+` were added, `-` removed.
3. Anything confusing *stays* confusing until you've asked. "Explain @src/app.js changes from this diff" in OpenCode is legitimate review, not cheating — make the AI teach you its own change.

**Scope-of-work check.** The most common AI mistake is not bad code; it is *more code than you asked for*: extra helpers, reformatting of untouched files, "improvements" beside the point. If you see it, say so: "revert everything except the `dark-mode` toggle changes." Scope discipline is review.

## Step 2: Run the thing

Code review that never runs the code is just reading fiction. The checklist:

- [ ] The program/app runs and does the new thing
- [ ] The old things still work (the new toggle didn't break list view)
- [ ] The *done-definition* from your prompt is met — you wrote one, it's checkable
- [ ] Error paths: give it bad input, slow network, empty file — does it grumble politely instead of crashing?
- [ ] If tests exist: they pass (and if none exist and the change is logic, ask the AI to add some — "no new dependencies")

## Step 3: Read it like an editor

You are not hunting for perfect style; you are triaging risk. Look for these **frequent, findable problems**:

| Red flag | Looks like | Triage |
|---|---|---|
| **Scope creep** | Files touched that the task didn't involve | Ask to revert to task scope |
| **Hard-coded secrets** | Something that looks like a key/token in the diff | Remove & rotate — non-negotiable |
| **Lying logs** | `// this function is unused` on a function now used everywhere | Ask the AI to recheck comments; stale comments are a classic |
| **Missing error handling** | Code assuming files exist, networks answer, users don't do weird things | Ask: "handle the empty case / offline case / invalid input" |
| **Over-engineering** | A config system, three abstractions and a factory for one feature | "Simplify to the smallest version that meets the done-definition" |
| **Magic behaviour** | Works but you can't explain why | Refuse it. Ask the AI to explain plainly until you can |
| **Copy-paste clones** | The same function appears in two files | "Deduplicate — keep one, referenced from both" |
| **Suspicious URLs** | Looks-plausible links/pages created wholesale | Never trust AI-made links without checking |

You will not catch everything at first. You will get dramatically better in a month, mostly through the review *prompts* in the next section.

## Step 4: The review prompts (your unfair advantage)

OpenCode can help you review — and free models are typically *better at critical reading than at perfect generation*. Use it:

- "Explain the changes from this last task as if I'm new: what, why, and what could go wrong."
- "What is the riskiest part of the change you just made? What would you test first?"
- "Review your own diff like a stern senior dev. List anything you'd be embarrassed about." (Great on good models, comedy on small ones — but both are useful.)
- "Write three quick test cases for `slugify()` — normal, empty, weird input." Then make it implement and run them.

Also remember `/undo` and `/redo`: OpenCode keeps a history of change-sets, so iterating ("that's 90% right, but the toggle should sit top-left") is cheap. Undo does not replace Git — it replaces *re-prompting from scratch*.

## Step 5: The accept ritual

When satisfied, make the acceptance formal — this doubles as the end of the loop:

```bash
git add -A
git commit -m "add dark-mode toggle with saved preference"
```

If instead you are *not* satisfied and the AI's second attempt gets worse rather than better:

```bash
git restore .     # back to your pre-task snapshot
```

…and then change the *prompt*, not the code. Two failed generations is a prompt problem; a fresh-scope task or a Plan-mode pass will usually do better than a third wild attempt.

## A note on formatters and standards

If your project uses a formatter (e.g. Prettier, Black), run it after AI changes and review *that* diff separately. Judging style is a waste of your review attention — the machine can settle style; you settle meaning. OpenCode can also be configured to run formatters automatically (its `formatter` settings), which is worth doing once your routine is stable.

## Review on a budget (free-tier friendly)

Reviewing is one of the *cheapest* things a free model does well, since it is usually short-input, short-output: diffs, explanations, test suggestions. A frugal pattern that works surprisingly well:

1. Big, careful **Plan** with your best/strongest allowed model (rare requests anyway).
2. **Build** with whatever model your tier handles comfortably.
3. **Review** — cheap, free-friendly — with the same or even a different capable model.
4. **Commit** locally. No tokens required for steps 3's Git part at all.

## The review checklist (shrink onto a card)

- [ ] `git diff --stat` — scope matches the task
- [ ] Full diff read (or read with AI narration where unclear)
- [ ] Ran the thing; done-definition met; old features intact
- [ ] No secrets or weird URLs entered the diff
- [ ] Self-review prompt: "riskiest part? would you be embarrassed anywhere?"
- [ ] Formatter run, if one exists
- [ ] Accepted → commit. Not accepted after two tries → `git restore .`, new prompt

Review might feel slow as you read this. In practice it is minutes, and it is the exact habit that keeps the AI a tool rather than a hazard. Now, let's look honestly at what free tiers give you — and what they don't.

---
