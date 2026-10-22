# STATUS.md — Free AI Coding with OpenCode

Last updated: 2026-10-22

## What was built

A complete beginner manual, **"Free AI Coding with OpenCode"**, in two forms:

1. **`docs/`** — the source of truth: 11 Markdown chapters (welcome page + 10 numbered
   chapters), ~13,700 words total. Plain English throughout, with tables, checklists,
   copy-paste commands, and no unexplained jargon.
2. **`site/`** — a built static HTML site (committed, works offline): one page per chapter
   with prev/next navigation, a landing contents page, a single-file print-friendly
   `full-book.html` edition, and `style.css`. Zero external assets: no web fonts, no
   scripts, no trackers, no network requests needed to view it.

### Chapter inventory

| File | Title | Approx. words |
|---|---|---|
| docs/index.md | Welcome — Read Me First | ~1,050 |
| docs/01-what-is-opencode.md | Chapter 1 — What Is OpenCode? | ~1,100 |
| docs/02-installing-opencode.md | Chapter 2 — Installing OpenCode | ~1,450 |
| docs/03-picking-free-models.md | Chapter 3 — Picking Free Models | ~1,500 |
| docs/04-permissions-and-safety.md | Chapter 4 — Permissions and Safety | ~1,400 |
| docs/05-writing-good-task-prompts.md | Chapter 5 — Writing Good Task Prompts | ~1,400 |
| docs/06-git-basics.md | Chapter 6 — Git Basics (Your Safety Net) | ~1,550 |
| docs/07-reviewing-ai-changes.md | Chapter 7 — Reviewing AI Changes | ~1,250 |
| docs/08-limits-of-free-tiers.md | Chapter 8 — Limits of Free Tiers | ~1,200 |
| docs/09-troubleshooting.md | Chapter 9 — Troubleshooting | ~1,300 |
| docs/10-appendix-checklists.md | Chapter 10 — Appendix: Checklists & Glossary | ~850 |

Supporting files:

- `README.md` — project overview, build/test instructions, credit to Asdale Dynamics, LLC.
- `LICENSE` — MIT with the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`.
- `build.py` — site generator (docs/*.md → site/*.html + index + full-book).
- `tests/test_build.py` — 21-test suite (stdlib `unittest`).
- `requirements.txt` — build dependency (`markdown`).
- `.gitignore` — Python/editor noise.

## How to run it

**Read the book:** open `site/index.html` in any browser (or start at `docs/index.md`).

**Rebuild the site** after editing chapters:

```bash
pip install -r requirements.txt
python3 build.py
```

**Run the tests:**

```bash
python3 -m unittest discover -s tests -v
```

## Verification results (all green, run 2026-10-22)

- ✅ `python3 build.py` builds cleanly: 11 chapter pages + index + full-book + style.css.
- ✅ Test suite: **21/21 tests pass** (book structure, 10,000+ word minimum — actual 13,756,
  markdown conversion incl. tables/fenced code/checkbox styling/link rewriting,
  generated-site checks incl. navigation and no-external-assets, privacy/secret sweep,
  exact LICENSE line, README credit).
- ✅ All generated HTML pages parse (Python `html.parser`, zero failures).
- ✅ Smoke test: served `site/` over a local HTTP server; `index.html`, `full-book.html`,
  a chapter page, and `style.css` all returned HTTP 200 with expected sizes.
- ✅ Word count verified with `wc -w`: 13,756 words across `docs/`.
- ✅ Manual checks: chapter order correct (Welcome first), task-list checkboxes render
  styled on chapter pages, no escaped-pipe artifacts in install-command tables.
- ✅ No secrets/API keys/personal data: secret-pattern sweep passes on docs and site.

## Design decisions of note

- **Local-first and static**: the builder only reads/writes local files; documents use
  no emoji, no external assets, and no trackers.
- **Facts accuracy**: install commands, `/connect`/`/models`/`/init`/`/undo` mechanics,
  Plan/Build mode (Tab), permission keys and defaults (e.g. `.env` reads denied by
  default), `AGENTS.md`, and the Ollama/LM Studio config shapes follow OpenCode's
  official documentation as of Oct 2026, with explicit reminders that provider
  prices/limits change and should be re-checked on provider pages.
- **Checkbox rendering** is handled by a code-fence-aware preprocessor plus HTML
  styling, so GitHub-style `- [ ]` checklists render as real checkboxes on the site
  and stay literal inside code blocks.

## Known gaps / honest notes

- **Free-tier numbers are dated by design.** The book teaches limits' shapes and points
  to provider pages for current numbers; specific quotas in Chapter 3/8 are illustrative.
- **Site styling is intentionally minimal** (clean typography, dark-mode-aware); there
  is no search box or JavaScript — deliberate for offline/reliability goals. Search can
  be added later if wanted.
- **No screenshots.** Terminal screenshots would date badly; the book describes UI
  elements in words. Illustrations could be added later.
- **Windows paths** in the book assume WSL; native-win subtleties beyond the documented
  installers are not covered beyond pointers to Chapter 9.
- **Single test engine** (`unittest`): no external test framework needed; fine for this
  project's scope.
- The build currently requires the `markdown` pip package (see requirements.txt);
  a zero-dependency fallback converter was deliberately not shipped to keep one
  well-tested code path.

## Git

Repository initialized locally with a plain commit (no co-author trailers,
no remote configured, nothing pushed or published — per instructions).
