# Welcome — Read Me First

## Who this book is for

This book is for anyone who wants to use an AI coding assistant without spending money, without already being a professional programmer, and without feeling talked down to.

Maybe you have an idea for a website, a tool for your small business, a script that saves you an hour a week, or just plain curiosity about how "AI coding" actually works. Maybe you have tried a chatbot in a browser and thought: *this is great at explaining, but I want it to actually build things.* This book will show you how to do that, for free, using a tool called **OpenCode**.

You do not need a computer science degree. You do not need to buy anything. Everything in this book can be done with a regular computer, a normal internet connection, and free accounts (or no accounts at all, if you go the local route). Wherever something can go wrong, we will tell you how to notice it and how to fix it.

One promise before we start: we will never assume you already know the thing we are explaining. Every term gets explained the first time it shows up. Every command is written out in full so you can copy it exactly. And if a step feels risky, we will say so — and show you how to make it safe first.

## What you will learn

By the end of this book, you will be able to:

1. **Install OpenCode** — a free, open-source AI coding agent that runs right in your terminal — on Windows, macOS, or Linux.
2. **Pick a free model** and connect it, choosing between cloud providers with free tiers, subscriptions you might already have, and models that run entirely on your own computer.
3. **Set up guardrails** so the AI can help you without overstepping — this is the *permissions and safety* part, and it matters more than most beginners realize.
4. **Write prompts that actually produce good work**, instead of vague requests that produce vague results.
5. **Use Git** — the industry-standard version control system — as your safety net, so no AI mistake can ever destroy your work.
6. **Review AI changes like an editor**, not a spectator, so you stay in charge of your own project.
7. **Understand the limits of free tiers** — what you get, what you don't, and how to work around it.
8. **Fix problems yourself** using a systematic troubleshooting chapter, because things *will* occasionally break, and that is normal.

## How to read this book

You have two ways to read this:

- **As a book, chapter by chapter.** Each chapter builds on the previous ones. If you are brand new to all of this, reading in order is worth it. The appendices at the end are checklists you will come back to again and again.
- **As a reference.** Later, when you just need the troubleshooting table or the pre-commit checklist, jump straight to those chapters. They are written to stand on their own.

## Conventions used in this book

| What you see | What it means |
|---|---|
| `opencode` | A command you type into your terminal. Typing rules: type the text after the `$` prompt you see in examples — never type the `$` itself. |
| `/connect`, `/models`, `/init` | Commands typed *inside* OpenCode (they start with a slash). |
| **Bold** | Something you click, press, or should pay extra attention to. |
| *Italic* | A term being introduced, or gentle emphasis. |
| A checklist with empty boxes | Something to actually do — print it, copy it, or tick it off mentally. |

Two terms come up constantly, so let's get them out of the way now:

- **Terminal** (also called the command line, command prompt, or console): the text window where you type commands directly to your computer instead of clicking buttons. If you have never used one, don't worry — Chapter 2 walks you through your first commands, and you will need far fewer of them than you fear.
- **Model**: the actual "brain" the AI uses — for example, a large language model such as Qwen Coder or GLM. OpenCode is the tool; the model is the engine inside it. Chapter 3 is all about choosing one.

## Map of the book

| Chapter | Title | What it covers |
|---|---|---|
| 1 | What Is OpenCode? | The mental model: what an AI coding agent is, and how it differs from a chatbot |
| 2 | Installing OpenCode | Every supported way to install it, step by step, then your first launch |
| 3 | Picking Free Models | Cloud free tiers, subscriptions you may already own, and fully local models |
| 4 | Permissions and Safety | Guardrails so the AI never oversteps; keeping your secrets and files safe |
| 5 | Writing Good Task Prompts | The prompt formula that turns vague wishes into finished work |
| 6 | Git Basics | Version control: your undo button for real life |
| 7 | Reviewing AI Changes | How to check AI-generated code before it becomes your problem |
| 8 | Limits of Free Tiers | What free actually buys you, and smart ways to work within it |
| 9 | Troubleshooting | A symptom → cause → fix table for everything that commonly breaks |
| 10 | Appendix: Checklists | The one-page routines you will reuse on every project |

## The one rule of this book

If you remember nothing else, remember this:

> **Never let the AI be the only person who understands your project.**

Free models are good — genuinely good — and OpenCode makes them pleasant to use. But you are the boss here. The AI proposes; you review, you decide, you commit. That single habit is what separates "the AI helped me build something I'm proud of" from "I have no idea what this folder even does anymore." Everything else in this book supports that habit.

## About the fine print

Prices, rate limits, model names, and menu options change constantly in the AI world. This book describes how things work as of late 2026, and the *techniques* here are durable — but the specific numbers (how many requests per day, how big a context window is) will drift. Whenever this book gives a specific limit, treat it as "a typical example, check the provider's current page for today's number." We will remind you of this in the chapters where it matters.

Ready? Turn the page.

---
