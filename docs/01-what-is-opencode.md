# Chapter 1 — What Is OpenCode?

## From chatbot to coworkers

You have probably used an AI chatbot in a browser. You type a question, it answers, you copy what you like. That is a *conversation*.

**OpenCode is different.** It is an **AI coding agent**: instead of just talking *about* your code, it can actually *work on it* — reading your files, writing changes, running commands in your terminal, and reporting back. The difference is the difference between asking a friend "how do I change a tire?" and handing your keys to a mechanic who does it while you watch.

Here is what an agent can do that a plain chatbot cannot:

| Ability | Browser chatbot | OpenCode (an agent) |
|---|---|---|
| Explain code | Yes | Yes |
| Read the files in your project | Only if you paste them | Yes — it can open and read files itself |
| Edit files directly | No | Yes, with your permission |
| Run commands (tests, builds, Git) | No | Yes, with your permission |
| Work across many files at once | Painfully, via copy-paste | Yes — that is its whole job |
| Remember your project's style | No | Yes — via an `AGENTS.md` file it writes for your project |

That last row deserves a quick explanation. When you first run OpenCode in a project, you type `/init`. OpenCode looks around your project, figures out what it is (a blog? a data-cleaning script? a shop?), and writes an `AGENTS.md` file — think of it as a *welcome note to the AI*, describing the project layout, the conventions, and the commands that build and test it. From then on, every session starts with OpenCode already knowing the house rules.

## What OpenCode actually is

A few facts, so you know what you are getting into:

- **Open source.** The code is public; anyone can inspect it. You are trusting software you can read.
- **Runs in your terminal.** The main interface is a friendly text-based app (called a **TUI** — a *text user interface*). There is also a desktop app and an IDE extension, but this book focuses on the terminal, because it is the most reliable path and teaches you the most.
- **Model-agnostic.** OpenCode does not lock you to one company. It supports **75+ providers** — big labs, small labs, and your own computer. That is exactly why a book about *free* AI coding is possible: you can point OpenCode at whatever is free today.
- **Permission-aware.** By default it asks before editing files and before running commands. Chapter 4 turns this dial up or down.

## The mental model: a junior developer on your team

Beginners often swing between two extremes: treating the AI like a magic oracle, or treating it like a hostile autocomplete. Neither is useful.

The model that works is this: **you have hired a junior developer who is extremely fast, extremely tireless, extremely confident — and who does not know your project yet.**

What follows from that little story:

1. **You have to give real instructions.** "Make it better" is not spec. "Add a search box to the top of the notes page that filters by title, and show 'no results' when nothing matches" is.
2. **You have to review the work.** Fast and confident means fast and confident *mistakes*. Not malicious ones — just ordinary misunderstandings. Your review is the quality control. Chapter 7 gives you the routine.
3. **You should protect the project.** A careful senior developer never lets someone push straight to the live product with no review and no undo. Chapter 6 teaches you Git, which is exactly that protection.
4. **You can lean on it for the boring parts.** Explaining unfamiliar code, writing repetitive boilerplate, renaming things everywhere, drafting tests — this is where agents shine, and where they free *you* to think.

If you internalize the junior-developer model, everything else in this book will feel obvious rather than fussy.

## The five-step working loop

Almost everything you do with OpenCode follows the same small loop. Learn it once; use it forever:

1. **Ask.** Describe what you want, with context. (Chapter 5.)
2. **Plan.** For anything bigger than a small tweak, press **Tab** to switch OpenCode into **Plan mode**. In Plan mode the AI is *forbidden* from changing files — it can only propose an approach. You read the plan, correct it, and iterate until it matches what you actually wanted.
3. **Build.** Press **Tab** again to return to Build mode and say "go ahead." The AI edits files, runs commands, and narrates what it did.
4. **Review.** Look at what changed (`git diff`, Chapter 7), ask follow-up questions, and test the result.
5. **Undo or proceed.** Happy? Commit your work with Git. Unhappy? Type `/undo` to back out the changes and try again with a better prompt. OpenCode keeps a history, so you can also `/redo` if you change your mind — and `/undo` more than once to walk back further.

> **Why Plan mode matters.** Beginners pay for AI mistakes in churn: "no, not like that — undo — try again." Plans cost seconds; wrong builds cost minutes and leave a mess. The pros you watch in AI-coding videos are mostly just people who insist on good plans.

## A tiny tour of the terminology

You will meet these words constantly. Here is the whole cheat sheet in one table — bookmark this page.

| Term | Plain meaning |
|---|---|
| **Model** | The AI "brain" — e.g., Qwen 3 Coder, GLM, GPT, Claude. Different models differ hugely at coding tasks. |
| **Provider** | The company or service that serves a model — OpenAI, Anthropic, Groq, Google, your own machine. Usually you need an account or a programme installed. |
| **API key** | A long password-like string that proves to a provider that you are you. Keep it secret; never paste it into code you share. |
| **Token** | The unit of AI text — about ¾ of a word. Providers bill and limit by tokens. Your prompt uses input tokens; the answer uses output tokens. |
| **Context window** | How much text (your files + conversation) the model can consider at once, measured in tokens. Too-small context = the AI "forgets" things you said. |
| **Free tier** | A no-cost usage level offered by a provider, usually with daily/monthly limits. |
| **TUI** | Text user interface — OpenCode's terminal app. |
| **Tool** | An ability the agent can use: read a file, edit a file, run a shell command, search the web. Each tool can have its own permission rule. |
| **Permission** | Your rulebook: `allow`, `ask`, or `deny` for each tool. Chapter 4. |
| **Agent mode** | Build mode vs Plan mode — whether the AI may change things or only propose. |
| **AGENTS.md** | The project guidebook file that OpenCode reads at startup; `/init` creates it. |
| **Repository (repo)** | A folder tracked by Git, so changes are recorded and reversible. Chapter 6. |
| **Diff** | The line-by-line "what changed" view. How you review AI work. |

## What OpenCode is *not*

To keep expectations calibrated:

- **It is not a one-click app builder.** It will not guess your business away from you. It needs your decisions, clearly stated. (Chapter 5 fixes that.)
- **It is not infallible.** Models sometimes misread intent, invent a function that does not exist, or quietly break a part of your project you did not mention. This is normal, expected, and fully recoverable with the loop above — especially if you have Git.
- **It is not free of *judgment*.** Even with a free model, *you* are responsible for what it produces and what you ship. Reviewing is not optional bureaucracy; it is the job.

## Your first look ahead

In Chapter 2, you will install OpenCode in about ten minutes using one command, open it in a practice folder, and take it for a spin. Then Chapter 3 gets you a capable model *without paying anyone anything*.

If you ever feel lost in the jargon, come back to the table above. Every beginner is confused by this vocabulary for roughly a week; after that it is simply how you talk.

---
