# Chapter 6 — Git Basics (Your Safety Net)

Git is the one tool in this book that has nothing directly to do with AI — and is the reason AI coding is *safe* for beginners. Git records snapshots of your project, called **commits**, so that any mistake — yours or the AI's — can be reversed with one command. Everything else in this book quietly assumes you know this chapter.

## The idea in one paragraph

Imagine you save a copy of a document before every edit, forever, into a numbered archive that takes no space and never gets mislabelled. That is Git. A **repository** ("repo") is a project folder that Git archives. A **commit** is one archived snapshot with a label you wrote. A **diff** is the difference between two snapshots. That vocabulary plus six commands is 95% of what beginners need.

## Setup once, per computer

Tell Git who you are (this goes into the archive labels of commits you make):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

The email does not need to be real for local work, but using your real one matters later if you publish to GitHub, since GitHub links commits to accounts by email. Nothing in this book requires an online service; Git is fully local.

## The six commands that matter

| Command | What it does | When you type it |
|---|---|---|
| `git init` | Turn this folder into a repo | Once, at the start of a project |
| `git status` | Show what changed and what's staged | Constantly; your dashboard |
| `git add -A` | Stage all current changes for the next snapshot | When you like what you see |
| `git commit -m "…"` | Save a labelled snapshot | Every time you reach a good state |
| `git log --oneline` | List past snapshots short | When you want an overview |
| `git diff` | Show unstaged changes line by line | Before staging — your review screen |

And for emergencies (learn these the day something breaks):

| Command | What it does |
|---|---|
| `git restore <file>` | Discard unsaved changes to a file — back to last commit |
| `git restore --staged <file>` | Unstage a file you add-ed by mistake |
| `git checkout <hash>` | Travel back in time to look at any old snapshot, read-only |
| `git branch <name>` / `git checkout -b <name>` | Create a parallel history (see below) |
| `git merge <name>` | Blend a branch's work back into the main line |

Nothing here touches the internet. This book keeps you **local-first**: GitHub is a good future step, but you do not need accounts or remotes to be protected.

## `.gitignore`: files Git should never touch

Some files should never enter history: caches, build output, and above all **secrets**. Put a `.gitignore` file in your project root on day one:

```gitignore
# Never commit these
.env
.env.*
*.pem
*secret*
auth.json

# Usually noise
node_modules/
__pycache__/
.DS_Store
```

Check that it works:

- [ ] `git status` shows no `.env` (or similar) as untracked after you add `.gitignore`
- [ ] `node_modules/` (if you use it) is invisible to `git status`
- [ ] The `.gitignore` itself **is** tracked (it's a project file, and a great one)

Note the difference in defaults you already carry from Chapter 4: OpenCode refuses to read `.env` by the same logic — secrets stay out of conversations *and* out of history.

## The recommended AI-working rhythm

This is the chapter's gift to your future self: a rhythm that makes AI work trivially reversible.

1. **Start clean.** Before asking the AI for anything, `git status` should say "nothing to commit." If not, commit or discard the old work first — never mix old and new in one review.
2. **Commit before you prompt.** A commit right before each AI task is a restore point keyed by task (write it in the message: "before dark mode feature").
3. **Let the AI work.** Approve, watch, keep Git untouched.
4. **Review the diff** (`git diff`, Chapter 7 teaches the routine).
5. **Commit the result — or roll back.** Good? `git add -A && git commit -m "add dark mode toggle"`. Bad? `git restore .` and nothing of value was lost — your last commit still stands.

Optionally level up with branches: `git checkout -b dark-mode` before a bigger feature, explore there, `git merge dark-mode` when satisfied. A branch is a free sandbox that protects the main line; it pairs beautifully with AI experiments.

## Writing commit messages that help (including with the AI)

A commit message is a label for your future self. Patterns that cost seconds and pay for weeks:

- **Present tense, imperative-ish, specific**: `add slugify helper with tests`, `fix crash on empty photo name`, **not** `fixes` / `stuff` / `asdf`.
- **Why beats what**: `cap crops at 1200px (eBay requires min 800)` is gold six months later; `resize images` is decorations.
- **One idea per commit**: if the message needs the word "and" three times, make two commits.
- **Never commit secrets or junk files**: check `git diff --staged` before any commit if you are unsure what you staged.

## What to commit — including `AGENTS.md`

Short answer: everything that defines the project. Specifically relevant to this book:

| File | Commit it? | Why |
|---|---|---|
| Source code (`src/`, etc.) | Yes | Obviously |
| `AGENTS.md` | **Yes** | Your AI briefing travels with the project; per OpenCode's own advice |
| README, config, test data (fake) | Yes | Part of the project |
| `.gitignore` | Yes | Protects the future |
| `.env`, keys, `auth.json` | **Never** | Secrets |
| `node_modules/`, build output | No | Reproducible from source; huge |
| Large media you could regenerate | Usually not | Keeps repo snappy |

## Your rhythm as a checklist

Print this. It is the operational spine of the whole book:

- [ ] Repo initialized (`git init`), user configured
- [ ] `.gitignore` in place, secrets excluded
- [ ] Working tree clean before each AI task
- [ ] Commit before prompting (snapshot A)
- [ ] `git diff` reviewed after the AI's work
- [ ] Commit after acceptance (snapshot B) **or** `git restore .` to roll back
- [ ] Messages: specific, one idea each, no secrets

With this rhythm, the scariest sentence in AI coding — *"I don't know what it changed"* — becomes a question with a nine-character answer: `git diff`. On to reviewing, proper.

---
