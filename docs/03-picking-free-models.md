# Chapter 3 — Picking Free Models

OpenCode is the tool; the **model** is the engine. This chapter gets you an engine without spending money, and explains the honest trade-offs you are making.

## What "free" really means

"Free" in this world comes in four flavours. You will meet all of them, so learn to tell them apart:

| Flavour | What it is | Catch |
|---|---|---|
| **Free tier (cloud)** | A hosted model you can call from OpenCode with a signup, limited by requests per day/month or tokens | Limits, slower queues, sometimes weaker models served |
| **Subscription you already own** | A ChatGPT Plus, GitHub Copilot, or GitLab plan you *already pay for* elsewhere — OpenCode can use it for coding with zero setup | Not "free," but no *new* money; subject to that plan's caps |
| **Free credits / promotional** | Start-up providers giving new accounts a helping stack of tokens | Runs out; better as a taste than a plan |
| **Local models** | Open-weights models running on *your* computer via Ollama, LM Studio, or llama.cpp | No limits ever, but your hardware and patience are the budget |

The overriding truth, stated kindly: **the free world is real and good.** Free and open-weights coding models — the Qwen-Coder family, GLM series, DeepSeek-Coder variants, Llama, and friends — are routinely capable enough to build small projects, clean data, write scripts, and maintain a website. You are not choosing between "free" and "useful." You are choosing speed, patience, and privacy trade-offs, which the table below makes concrete.

| Trade-off axis | Cloud free tier | Local model |
|---|---|---|
| Cost | 0 (with caps) | 0 (with your electricity) |
| Speed | Usually fast, sometimes throttled | Depends on your machine |
| Privacy | Your code travels to the provider's servers | Code never leaves your machine |
| Quality ceiling | Usually higher | Smaller models, smaller context |
| Setup | Account + API key | Install a program + download model files |
| Limits | Daily/monthly caps | None — run it till your fan gives up |

## The menu of free paths

Here is the landscape as of late 2026. **Prices and limits change constantly** — treat every number here as an example, and the provider's own page as the truth. OpenCode supports all of these via `/connect`.

| Path | What you get | Rough shape of the limits | Good for |
|---|---|---|---|
| **GitHub Copilot (free plan)** | Coding models through your GitHub account; device-code login, no API key to manage | Monthly request/message caps on the free plan; the best models often need paid tiers | Beginners who already have GitHub; the smoothest login |
| **ChatGPT Plus/Pro** (if you own it) | OpenCode connects with your existing subscription via browser sign-in | Your subscription's usage caps | People who already pay for one; no new account |
| **Google AI Studio (Gemini)** | A generous free tier on Gemini models via an API key from AI Studio | Daily request caps; data may be used to improve service on the free tier | Big context windows and strong general ability |
| **Groq** | Very fast serving of open models (e.g. Llama, Qwen families) | Free tier with rate limits | Lightning-fast iteration on free-weights models |
| **Cerebras** | Open models such as Qwen-Coder at very high speed | Free tier with rate limits | Same as Groq — pick whichever is smoothest that week |
| **NVIDIA (build.nvidia.com)** | Free access to Nemotron and many open models | Per-model rate limits | Sampling many open models free |
| **OpenRouter (`:free` models)** | A menu-service routing to many labs; models suffixed `:free` cost nothing | Daily caps on free models; quality varies | Trying lots of models without committing |
| **Hugging Face Inference** | Free monthly inference credits across many providers | Credits refresh monthly | Occasional use of trendy new models |
| **Ollama (local)** | Open-weights models entirely on your machine | Only your RAM/GPU/disk | Privacy, offline work, unlimited practice |
| **LM Studio (local)** | Point-and-click app for downloading and serving local models | Same as Ollama | Beginners who prefer windows over commands |

## The two setup recipes you'll actually need

### Recipe A: GitHub Copilot (the smoothest cloud start)

1. Make sure you have a GitHub account (free to create).
2. In OpenCode, run `/connect`, search for and choose **GitHub Copilot**.
3. OpenCode shows a short code and the address `github.com/login/device`. Open that page in a browser, enter the code, and approve.
4. Back in OpenCode, run `/models` and pick a model.

Notes worth knowing:

- Some models require paid Copilot plans (Pro+); the free plan's models still work fine for learning.
- If you later see "model requires a higher plan" errors, pick a different model from `/models` — nobody is charging you here, the menu is just saying *that one's not in your tier*.

### Recipe B: Ollama (the local, unlimited start)

Ollama runs models on your own computer. Nothing leaves your machine — which matters for medical-adjacent work, small business records, or anything private.

1. Install Ollama from `ollama.com` (Windows and macOS installers; Linux a one-line script).
2. Pull a coding model from your terminal, e.g.:

   ```bash
   ollama pull qwen3-coder:7b
   ```

   (Model names and size tags change — browse the library at ollama.com/library and pick a *coder* model that fits your hardware. As a rule of thumb: about 8 GB of RAM will run a 7–8B model; 16 GB or a modest GPU comfortably runs the bigger useful ones.)
3. Tell OpenCode about the provider by adding this to `~/.config/opencode/opencode.json` (create the file if needed):

   ```json
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "ollama": {
         "npm": "@ai-sdk/openai-compatible",
         "name": "Ollama (local)",
         "options": {
           "baseURL": "http://localhost:11434/v1"
         },
         "models": {
           "qwen3-coder:7b": {
             "name": "Qwen3-Coder 7B (local)"
           }
         }
       }
     }
   }
   ```

4. Restart OpenCode, run `/models`, and you will see your local model listed.

Two local-model tips that save hours:

- **Increase the context size**: if tool calls misbehave or the model "forgets," raise Ollama's `num_ctx` (start around 16k–32k). Small default contexts are the number-one cause of flaky local behaviour.
- **Check the model is running**: `ollama ps` shows what is loaded; `ollama run qwen3-coder:7b` lets you chat with it directly to confirm it works outside OpenCode.

## The real selection criteria (beyond "is it free")

Tick these five boxes whenever you evaluate a free model:

- [ ] **Does it support tool calls?** OpenCode is an *agent* — it needs models that can call tools (read/edit files, run commands). Non-tool-calling models can chat but will fail at agentic jobs. Coder-focused models (Qwen-Coder, DeepSeek-Coder, big GLM variants, frontier models) are the safe picks.
- [ ] **Is the context window big enough?** Your whole project's key files and the conversation must fit. If the model has ~8k tokens of context, ambitious tasks will break in confusing ways. Prefer comfortable contexts (128k is common this decade).
- [ ] **What are the actual rate limits today?** Check the provider's own pricing/limits page — not this book — before planning a work day around it.
- [ ] **What is the privacy story?** Cloud free tiers often *may use your data for training*. If the content is sensitive (client data, health information, business records), use a paid key or a local model. Say it plainly: *do not paste anything you would not put on a postcard through a public free tier.*
- [ ] **Is there a "plan" model and a "build" model?** A common free-tier strategy: use a strong model for planning (rare, precious requests) and a faster one for execution (plentiful requests). Chapter 8 builds on this.

## A simple starting recommendation

If you want one default answer rather than a research project:

- **Comfortable and social**: GitHub Copilot's free plan (Recipe A) — fewest moving parts if you already have GitHub.
- **Private and unlimited**: a Qwen3-Coder-class local model via Ollama (Recipe B) — the "free forever" path, gated by your hardware.
- **Experimentation budget**: OpenRouter's `:free` suffix models or Groq/Cerebras/NVIDIA free tiers — great for taste-testing models before committing to one.

And remember: switching models is **one command** (`/models`), so this decision is cheap to revisit. You are not marrying a model; you are hiring per task.

## Checklist of this chapter

- [ ] You can name the four flavours of "free"
- [ ] Connected at least one cloud model via `/connect`, or
- [ ] Set up Ollama with a local coding model in `opencode.json`
- [ ] `/models` shows your choice and you have chatted with it once
- [ ] You checked the provider's current limits page (today's numbers, not a book's)
- [ ] You know the privacy posture of whichever model you picked

---
