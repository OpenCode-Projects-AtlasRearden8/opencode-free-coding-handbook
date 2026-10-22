# Chapter 9 — Troubleshooting

Everything breaks sometimes — terminals, keys, models, permissions — and the fix is almost always in the top ten possibilities. This chapter is a giant symptom → cause → fix table plus a few "get unstuck manually" walkthroughs. Keep it open when something misbehaves; skim it on a good day so it's familiar on a bad one.

## The universal debugging drills

Before the tables: three habits that solve half of all problems before you look anything up.

1. **Reproduce it exactly.** Same command, same folder, same order. Flaky problems are diagnosis-eaters; a stable reproduction is half the diagnosis.
2. **Change one thing at a time.** New terminal? Or new model? Not both. One variable, then test.
3. **Read the actual error.** Out loud, like it matters. Most are surprisingly plain: `command not found`, `401`, `permission denied`. Match them below.

## Part A: OpenCode itself

| Symptom | Likely cause | Fix |
|---|---|---|
| `opencode: command not found` | Shell PATH doesn't include install dir, or stale shell | Open a **fresh** terminal; if persists, find the install dir (`npm config get prefix` for npm) and add its `bin` to PATH (Ch. 2) |
| TUI renders scrambled / colours wrong | Weak terminal emulator | Switch to Ghostty, WezTerm, Kitty, Alacritty (or WSL on Windows) |
| Screen garbles after resizing | Terminal resize event missed | Press **Ctrl+L**, or restart the TUI |
| Version numbers unchanged after update | Old install copy shadowing a new one | `which opencode` (or `where` on Windows) — confirm which one runs; re-run installer; open fresh terminal |
| Freezes / keys dead | Rare TUI/terminal hiccup | **Ctrl+C** twice to exit cleanly; relaunch. Losing nothing but session view |
| Everything is slow or erroring at once | Provider load/outage today | Try a second model/provider (`/models`); check the provider's status page |

## Part B: Authentication and keys

| Symptom | Likely cause | Fix |
|---|---|---|
| `401 Unauthorized` / `invalid API key` | Key wrong, revoked, or pasted with a typo | Re-run `/connect` for that provider; paste fresh key; restart OpenCode |
| `/models` shows nothing usable | No provider configured yet | Complete `/connect` first (Recipe in Ch. 3) |
| "Model requires a higher plan" (Copilot) | That model is tier-gated | Pick another model; free plans don't carry top models |
| Key leaked (committed/pasted anywhere) | Rotation needed | Revoke at the provider's website → re-`/connect` → clean the file/commit (Ch. 4) |
| Auth resets every launch | Permissions problem on `~/.local/share/opencode/auth.json` | Check file exists & is readable by you; re-connect once |

Do remember where keys live — `~/.local/share/opencode/auth.json` on Linux/macOS/WSL — and that "delete the file" is *not* the fix for a leak. Revoke-rotate-reconnect is the fix.

## Part C: Models and providers

| Symptom | Likely cause | Fix |
|---|---|---|
| `429` / rate-limit errors | Free quota for the hour/day | Wait (quota windows reset); switch model/provider; plan offline (Ch. 8) |
| Tool calls fail or the AI "forgets" instructions mid-task | Local model with small context | Raise Ollama's `num_ctx` (16k–32k to start); confirm the model supports tool calls; prefer coder models |
| Weird refusal-y/beepy answers from a big cloud | Wrong provider endpoint or free-tier route swapped to a small model | `/models`, pick explicitly; retry; nothing at all is ever your fault here |
| Extremely slow responses | Server load, or a very big model on weak local hardware | Off-peak retry; or check `ollama ps` — is it CPU-thrashing? |
| Nonsense answers on a local model | Corrupted/partial download, wrong model | `ollama pull <model>` again; check RAM fit for the model size |

## Part D: Files, edits, and permission prompts

| Symptom | Likely cause | Fix |
|---|---|---|
| AI won't read a file | `.env` read is denied by default (by design) | Env vars or manual value; true need = explicit override *with a reason* (Ch. 4) |
| "Permission denied" prompts flood in | `"*": "ask"` posture | That's fine; approve via **always** for safe categories (git status, grep) once you trust them |
| AI edits files outside the project | `external_directory` allows it | Set explicit path rules; default is `ask` — keep it |
| AI repeats the same failing action | `doom_loop` should ask by default | Approve investigation or reject; often the underlying task is impossible as stated — re-prompt |
| AI can't run a specific command | Your `permission.shell` rules deny it | Add a precise allow rule (e.g. `"pytest *": "allow"`), deny for `rm *` stays |

## Part E: Project-level oddities

| Symptom | Likely cause | Fix |
|---|---|---|
| Every answer misses the project's structure | Stale or missing `AGENTS.md` | Re-run `/init` after big structural changes; commit `AGENTS.md` (Ch. 2, 6) |
| AI says the file doesn't exist (it does) | Wrong path or context window lost it | Use `@` to hard-reference it; restart session for a fresh context |
| Changes lost after closing OpenCode | `/undo`'d but never committed, or plain not-saved | Commit early, commit often (Ch. 6) — OpenCode history is not Git history |
| Everything looks fine but tests fail silently | Test command differing from project convention (`/init` writes the right one) | Use the commands in `AGENTS.md` or ask the AI which test command your project expects |

## Part F: Git "rescue" recipes

Common beginner Git scares, resolved:

| Symptom | What is true | Fix |
|---|---|---|
| "I made a mess and want yesterday's version" | Last good commit exists | `git restore .` (unsaved changes) or `git checkout <hash>` to look back (then branch or copy) |
| "I staged a secret!" | Staging is safe; commit is the door | `git restore --staged <file>` to unstage; **if already committed**, remove the secret, rotate it at the provider, then commit the removal |
| "I committed something wrong" | Commits are printable history | Fix the file, commit again; for *fresh local* mistakes, `git commit --amend` is OK. Never rewrite pushed history |
| "My branch is a disaster" | Branchies are free | `git checkout main` (or your main branch), start fresh; delete the ruin with `git branch -D <name>` |

## When to ask for help

You are entitled to ask for help, and knowing where helps twice:

- **OpenCode's own docs** — opencode.ai/docs — always current, and this book deliberately sticks to their shape.
- **The TUI's `/help`** — the fastest answer for keys and commands.
- **OpenCode's Discord/GitHub** — real humans, and bug reports are welcome there. Search first; your exact error text is often already answered.
- **Error messages, verbatim**, always travel with you to any of these.

## The triage card (when panic arrives)

1. Fresh terminal. Fresh session.
2. `opencode --version`; confirm which binary.
3. One-variable change; retest.
4. Read the error verbatim; match it to the tables above.
5. `/models` swap to a fallback path.
6. `git status`/`git diff` to confirm nothing precious is lost.
7. Still stuck: docs → Discord → walk away for ten minutes (seriously, this fixes human-scale bugs).

Ninety percent of beginner "it's broken" moments die by step 4.

---
