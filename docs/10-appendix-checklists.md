# Chapter 10 — Appendix: The Checklists and Glossary

This is the shortest chapter and the one you'll use most. It compresses the whole book into routines you can run without re-reading anything. Print these, or keep this chapter open as a tab.

## A. First-session setup (once per computer)

- [ ] Good terminal chosen (WSL on Windows; Ghostty/Kitty/WezTerm elsewhere)
- [ ] OpenCode installed and `opencode --version` answers
- [ ] Git installed and identity configured (`git config --global user.name/user.email`)
- [ ] A provider connected via `/connect` (cloud free tier **or** local Ollama set up)
- [ ] `/models` lists your choice; one chat completed successfully
- [ ] Basic permission posture set: `"*": "ask"` for shell, `"rm *": "deny"`, `"git push *": "deny"` while learning
- [ ] Keys live in `auth.json` / env vars — never in project files
- [ ] Practice folder exists and is far from anything precious

## B. Starting a new project

- [ ] `mkdir <project> && cd <project>`
- [ ] `git init`
- [ ] `.gitignore` created (env, secrets, caches — see Chapter 6)
- [ ] minimal `README.md` in your own words (three lines counts)
- [ ] `opencode`, then `/init` to generate `AGENTS.md`; review & personalise it
- [ ] First commit: `git add -A && git commit -m "initial project setup"`

## C. Every AI work task (the loop card)

- [ ] `git status` clean; commit anything pending first
- [ ] Prompt has all four parts: **goal, context (`@files`), constraints, definition of done**
- [ ] One task per prompt; big tasks went through **Plan mode first**
- [ ] AI asked questions (or you asked it: "anything unclear?")
- [ ] After build: `git diff --stat`, then read the diff
- [ ] Review prompts used ("riskiest part? what would you test first?")
- [ ] Program actually run; old features still fine
- [ ] No secrets, no weird URLs in the diff
- [ ] Accept → commit (specific message) — or `git restore .` and re-prompt

## D. Privacy and secrets sweep (every commit — 30 seconds)

- [ ] `git diff --staged` shows no keys, tokens, passwords, `.env` lines
- [ ] Nothing client/patient/customer-specific in any prompt today
- [ ] Sensitive work done on a local model, if applicable
- [ ] No share-links created for private sessions
- [ ] If a leak happened: revoke → rotate → reconnect → clean the file

## E. Free-tier triage (when things get sticky)

- [ ] Identified the limit: rate quota / context window / quality floor / provider load
- [ ] Fresh session for a fresh context
- [ ] `AGENTS.md` re-`/init`-ed if structure changed
- [ ] Rotation considered (`/models` to secondary cloud or local)
- [ ] Plan saved on (digital) paper for tomorrow's fresh quota
- [ ] Provider's current limits page checked within the last 30 days

## F. Before telling anyone it "works"

- [ ] Done-definition met exactly as written in the prompt
- [ ] Bad inputs tried: empty file, wrong file, no network, giant file
- [ ] Restarted from scratch once (does it *still* work?)
- [ ] Diff reviewed by at least one non-AI intelligence (you)
- [ ] Committed with a message that explains *why*
- [ ] You could explain to a friend what changed without opening the code… going for a second look only

## The pocket glossary

| Term | Meaning |
|---|---|
| Agent | A tool that acts (reads, edits, runs), not just chats |
| AGENTS.md | Per-project briefing file OpenCode reads each session |
| Branch | A parallel line of history; a free sandbox |
| Build mode | OpenCode mode where changes are allowed |
| Commit | A labelled snapshot of the project (`git commit`) |
| Context window | How much the model can consider at once (tokens) |
| Diff | Line-by-line change view (`git diff`) |
| Free tier | No-cost usage level with caps |
| Local model | An open-weights model running on your machine (Ollama etc.) |
| Model | The AI "brain" (Qwen-Coder, GLM, GPT, Claude…) |
| Permission | allow / ask / deny rule for a tool |
| Plan mode | Propose-only mode (Tab toggles it) |
| Repo | A Git-tracked project folder |
| Token | Unit of AI text; ~¾ of a word |
| Tool | An ability: read file, run command, fetch page… |
| TUI | Text user interface (OpenCode's terminal app) |

## Where to go next

The skills in this book compound in a specific order. Once the loop above feels routine:

1. **Branches and GitHub** — publish projects, and let the cloud back up your safety net.
2. **Formatters and tests** — automate the parts of review that are mechanical.
3. **Custom agents and MCP servers** — teach OpenCode new tools; the same permission thinking gates new power (opencode.ai/docs/agents, /mcp-servers).
4. **Local models, deeper** — bigger Qwen/GLM-class models if your hardware allows; the Ollama recipe from Chapter 3 scales up unchanged.
5. **Come back to Chapter 10** — the checklists age well and everything else around them will have changed by then, which is exactly what books are for and pages like this one.

You now know more about working safely and productively with AI coding tools than most people who *pay* for them. Keep the junior-developer model in mind, keep Git between you and regret, and build something you'd proudly explain to a friend.

— End of the book. —
