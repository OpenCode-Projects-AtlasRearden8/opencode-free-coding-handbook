# Chapter 8 — Limits of Free Tiers (and Working Within Them)

Free is a real option, not a broken version of paid. But free has *edges*, and beginners exhaust good free setups for lack of knowing the edges' shapes. This chapter maps the limits so you can plan around them instead of being surprised by them.

## The rules of the free game

| Limit | Where you feel it | What it actually means |
|---|---|---|
| **Rate limits / quotas** | "Too many requests" / 429 errors, slowed-down replies | A count of requests or tokens per day/month. The commonest free-tier limit. |
| **Reduced served quality** | Free tier may route you to a smaller/older model at peak | Same model name can quietly vary in power |
| **Context window constraints** | The AI "forgets" files, loses the thread on long chats | Everything (conversation + referenced files) must fit in the window |
| **Feature gating** | Some models or settings simply missing from your plan | The provider reserves high tiers; you get the generous floor |
| **Throttled speed** | Great at 9 AM, slow at 6 PM | Shared pools get crowded |
| **Training on your data** | Privacy posture on free tiers (see Chapter 4) | Free often = your texts may train them |
| **No uptime guarantee** | Occasional errors on heavy days | Free tiers fail hardest exactly when everyone else is there too |

**The most important habit in this chapter: verify today's numbers on the provider's own page.** Limits change monthly in this industry. This book teaches shapes and strategies; websites carry today's truth.

## Recognizing the symptoms early

Free-tier exhaustion announces itself politely before it ruins your day:

| Symptom | Likely limit | First response |
|---|---|---|
| 429 / "rate limit" errors | Quota exhausted | Wait for reset; switch model/provider; finish task later |
| Replies get *shorter* or trail off | Output caps or mid-session throttling | Split the task; finish in a follow-up prompt |
| "I don't have the file you mentioned" | Context window filled | Reference fewer files; start a fresh session for new tasks |
| Increasingly generic answers | Small model substituted / context bloat | Restart session; compact the ask |
| Long errors mid-day | Provider under load | Local model (if set up) or revisit at off-peak |

None of these mean you did something wrong. They are the simplest, bleakest weather report for free-tier users, and now you read it fluently.

## Strategy 1: Match model to task size

The single most effective habit: **spend scarce powerful-model requests where they pay, and not a token more.**

| Task | Spend pattern | Why |
|---|---|---|
| Writing a Plan for a multi-file feature | Strong model, careful prompt | The plan steers everything downstream |
| Executing the approved plan | Fast/cheap model | Steps are now mechanical |
| Reviewing a small diff | Any model | Short in, short out |
| Explaining unfamiliar code | Any model | Chat, not creation |
| Giant refactor across 15 files | **None, or local big-model** | Small context models will mangle it |
| Chatting through concepts | Free/cheap | Zero-risk usage |

## Strategy 2: Make AGENTS.md do the remembering

Every token of project context you state in a prompt is a token re-spent forever. Instead, put stable facts in `AGENTS.md` (see Chapter 2) — structure, conventions, commands — and re-run `/init` when the project shape changes. Cheap models do *much* better when the briefing is in the file rather than the chat, and you stop paying to re-describe your project daily.

## Strategy 3: Plan offline; build with a lean budget

A pattern that turns an exhausted daily quota into a productive day:

1. **Morning (fresh quota):** Plan mode with your best model; revise until perfect; save the plan on paper (literally — copy it into your notes or a `PLANS.md` file).
2. **Midday (quota running low):** Build mode executes the plan; approve prompts; make commits along the way (Chapter 6).
3. **Quota gone:** human review of diffs (Chapters 6–7), local Ollama run for questions, or simply stop where the next step is mechanical for tomorrow-you with a fresh quota.

Written plans are portable between models *and* days — one of the quiet superpowers of Plan-first work.

## Strategy 4: Keep a rotation

Because `/models` switching costs nothing, experienced free-tier users keep two or three paths warm (Chapter 3's menu):

- Primary cloud free tier (e.g. Copilot free plan or a fast open-weights host like Groq/Cerebras)
- Local Ollama model for privacy, off-grid work, and when all quotas blink
- OpenRouter `:free` models as a wildcard sampler

| Situation | Rotation move |
|---|---|
| Primary quota hit | Switch to secondary cloud for the rest of the task |
| Privacy-sensitive content | Local model, full stop |
| Cloud simply errors today | Local until it clears; or plan-with-paper (Strategy 3) |
| Need a big-context reasoning pass | Whichever path currently offers the biggest window |

## Strategy 5: Know what free models are actually bad at

Honest limits of small/free models, so you stop blaming yourself for them:

- **Long, coherent multi-file refactors.** They lose the plot; scope decisions wobble. Keep refactors small or make them yourself with AI as navigator.
- **Subtle security reasoning.** They can *name* common vulnerabilities yet still write one. Ask a stronger model (or a second model) to security-review anything that touches auth, files, or user input.
- **Ambiguity.** They guess rather than ask. Your four-part prompts (Chapter 5) and "ask me anything unclear" fix most of this.
- **Consistent style across a project.** Expect drift; let formatters (Chapter 7) pick up the slack; correct slowly creeping architecture in review.
- **Endless patience inside one session.** Context fills; sessions get dumber at the end. Start fresh sessions for new tasks — it is not a memory problem you can fix by trying harder.

## When free is genuinely enough

A grounding table, because most beginners over-fear this question:

| Project type | Free-tier verdict | Notes |
|---|---|---|
| Learning, practice, toy apps | Enormously enough | This is free tiers' home turf |
| A personal website/blog | Enough with patience | Mostly small tasks, reviewable diffs |
| Small business tools (checklists, converters, trackers) | Enough | Keep data local or private; review security-sensitive parts |
| Automation scripts for you | Enough | Test with fake data first |
| Serious app with real user data | Possible, not first choice | Paid models/local help; security review matters |
| Anything with other people's personal data | Caution first | Privacy rules beat savings; local models for dosage— see Chapter 4 |

## The free-tier triage checklist

Keep for days when things feel slow or sticky:

- [ ] Which limit am I actually hitting (rate limit? context? quality floor?)
- [ ] Have I restarted the session for a fresh context?
- [ ] Is today's task actually plan-shaped → save a plan, build leaner
- [ ] Has `AGENTS.md` been re-run at `/init` since the last structural change?
- [ ] Should this task size go to the local model instead?
- [ ] Checked the provider's *current* limits page within the last month?
- [ ] Am I mid-rotation? (`/models` is one command — use it)

Free tiers are the reason this book exists: real coding help at real zero dollars. Treat them like a shared community garden — plan your plots, take turns, and it will feed you well.

---
