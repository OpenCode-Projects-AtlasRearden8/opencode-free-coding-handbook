# Chapter 4 — Permissions and Safety

Here is the sentence that makes this chapter matter: **an agent that can edit files and run commands is powerful, and power without guardrails is how beginners get hurt.** OpenCode ships with sensible guardrails. This chapter shows you how they work, how to tune them, and how to develop habits that make AI coding safe even on a free model.

## The permission dial: allow, ask, deny

OpenCode uses a `permission` config to decide, for every action it wants to take, one of three answers:

| Setting | Meaning | Feels like |
|---|---|---|
| `"allow"` | Runs without asking you | Trust-but-log |
| `"ask"` | Prompts you; you decide each time | Traffic light on yellow |
| `"deny"` | Blocks the action entirely | Hard fence |

Every tool can get its own setting. The main keys, straight from OpenCode's design:

| Permission key | Controls |
|---|---|
| `read` | Reading files (rule matches the file path). **`.env` files are denied by default** — see below. |
| `edit` | All file changes (edit, write, patch) |
| `shell` | Terminal commands (matches the command text, e.g. `git status --porcelain`) |
| `glob` / `grep` | File searches |
| `webfetch` / `websearch` | Fetching URLs / searching the web |
| `task` | Spawned subagents |
| `skill` | Loaded skills |
| `external_directory` | Touching files **outside** the folder you started OpenCode in (asks by default) |
| `doom_loop` | Detects the AI repeating the identical failing tool call three times (asks by default) |

## Where the rules live, and how they match

Put rules in your OpenCode config — globally at `~/.config/opencode/opencode.json`, or per-project in `opencode.json` at the project root. The simplest global stance:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "*": "ask",
    "edit": "allow"
  }
}
```

This says: let the AI edit files freely (you will review via Git anyway — Chapter 6), but **ask before every terminal command, web fetch, and everything else**. That is a wonderful beginner posture. It is a little more clicky, but each prompt is a free safety lesson about what the AI is currently doing.

Rules match with patterns, and **the last matching rule wins**. A common and sensible pattern: allow safe read-only commands, ask about the world, deny the genuinely dangerous:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "shell": {
      "*": "ask",
      "git *": "allow",
      "npm *": "allow",
      "grep *": "allow",
      "rm *": "deny"
    }
  }
}
```

Notes on pattern matching, because everyone trips here once:

- `*` matches anything; `?` matches exactly one character.
- `"grep *"` allows `grep thing file.txt`. Bare `"grep"` would *not* cover `grep` with arguments — patterns must include the wildcard to cover arguments.
- **Last rule wins**, so specificity goes *after* the catch-all. In the example above, `rm *` comes after `"*"` on purpose.
- Also useful: `"git push *": "deny"` in any config where you never want the AI to publish anything. This book's default stance is exactly that: the AI reads, writes, and commits locally; *pushing to the internet stays your job*.

You can also restrict where OpenCode may even look. Paths outside the start folder are gated by `external_directory` (asks by default). Keep it that way unless you have a reason.

## What "ask" looks like, and the three answers

When OpenCode prompts you, you pick from:

- **once** — approve this single request;
- **always** — approve this *category* of requests for the rest of the session (e.g. all `git status*` commands);
- **reject** — no.

Beginner guidance: read the prompt. It shows exactly what will run. If a shell command surprises you — press reject, then ask the AI why it wanted to run that. Surprises are information. If nothing surprises you any more, that is your cue that `always` is safe for that category.

## Auto mode: speed with a fence

`opencode --auto` auto-approves everything that would normally ask — **except rules explicitly set to `deny`**, which still bite. It is great for long, well-understood tasks on a safe project. It is *not* for your first week. If you use it, keep at least these denies in place:

- [ ] `rm *` (or at minimum any pattern touching files you care about)
- [ ] `git push *` (publishing stays manual)
- [ ] `webfetch` / `websearch` if you want the AI browsing only when you say so
- [ ] `.env` reads (the default denies them; keep it that way)

## Secrets: the non-negotiables

Some rules in this book are habits; these are laws:

1. **Never put API keys in files inside your project.** Keys belong in OpenCode's auth store (`~/.local/share/opencode/auth.json`) or environment variables — nowhere else, not even "temporarily."
2. **Never let `.env` contents into a conversation.** OpenCode denies reading `.env` by default *on purpose* — leave it that way. If the AI truly needs a value from `.env`, set it as an environment variable yourself or tell the AI *which* value in words, without pasting the secret.
3. **Never commit secrets to Git.** Chapter 6's `.gitignore` protects you; the reviewing chapter (7) has a pre-commit secret check.
4. **Rotate, don't panic.** If a key leaks (committed, pasted, shared), go to the provider's website and revoke/rotate it. That takes two minutes and neutralizes the leak.
5. **Mind AI-supplied links.** Free models occasionally hallucinate plausible-looking URLs. Never log in "via a link the AI gave you" — navigate to the provider's site yourself.

## Privacy: where does your code actually go?

With a cloud model, your prompts — meaning your code and file contents — travel to that provider's servers. Facts to internalize:

- **Local models (Ollama, LM Studio, llama.cpp) keep everything on your machine.** Strongest option for sensitive material.
- **Free cloud tiers often train on your data.** If the provider's free tier says it may use data to improve models, that text usually means exactly what it appears to mean.
- **Sessions may be shareable.** Some OpenCode versions can publish a share-link of a session. If such a feature is present, treat it like publishing pages on the internet — a fine way to show off a demo project, a terrible way to "ask friends about" anything private.
- As a nurse-turned-author, our founder's rule is worth borrowing: **treat patient, client, or customer details as radioactive in any AI context unless the tooling is explicitly designed and contracted for it.** This book is about tools and learning; it is never a place to paste real case data.

## Your first-signin safety checklist

Do these five minutes of tuning once, then relax:

- [ ] Set `"*": "ask"` for `shell` (commands get prompts)
- [ ] Add `"rm *": "deny"` to `shell` rules
- [ ] Decide on `"git push *"`: `deny` while you learn, `ask` later
- [ ] Leave `read` rules at default so `.env` stays denied
- [ ] Leave `external_directory` at `ask`
- [ ] Check your model choice's privacy posture (Chapter 3)
- [ ] Confirm keys live in `auth.json` or env vars, not project files
- [ ] Turn off auto-approvals (`--auto` unused) until Git is in your routine

## A gentle word about what safety is *for*

Safety rails are not distrust of you. They exist because this is a *new way of working*: software now proposes changes to your disk, your terminal, and your network, and the human reviewing it is learning to review. Every prompt you approve in your first weeks is a tiny education in what agents do. By the time auto mode truly suits you, you will *know* why — because you will have read a hundred of those prompts. That earned confidence is the whole game.

---
