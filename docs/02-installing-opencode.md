# Chapter 2 — Installing OpenCode

Installation sounds scary if you have never done "developer stuff" before. Good news: it is usually **one command**, and this chapter shows every option with full copy-paste instructions. Ten minutes from now you will have the tool running.

## Step 0: Get a decent terminal first

OpenCode lives in the **terminal**, so you want a terminal that renders it well. If you are on Windows, the single most important advice in this chapter is: **use WSL** (Windows Subsystem for Linux). Windows' classic console (`cmd.exe`) struggles with modern text interfaces. WSL gives you a real Linux environment inside Windows, and OpenCode's own documentation recommends it.

| Platform | Recommended terminal | Notes |
|---|---|---|
| Windows | **WSL** (with Windows Terminal as the window) | Full compatibility; skips most rendering problems. See Microsoft's "Install WSL" guide, then continue this chapter *inside* WSL. |
| Windows (no WSL) | Windows Terminal | Workable via Chocolatey/Scoop/npm, but expect occasional display quirks. |
| macOS | iTerm2, Ghostty, Kitty, WezTerm, or plain **Terminal.app** | All fine; Ghostty and Kitty are OpenCode's favourite picks. |
| Linux | Ghostty, Kitty, Alacritty, WezTerm | Nearly any modern emulator works. Very old ones (or plain `xterm`) can be flaky. |

Installing WSL (once, in PowerShell as Administrator):

```bash
wsl --install
```

Then restart your machine and open the new "Ubuntu" app. Everything below happens in that window, or in Terminal.app/Ghostty on Mac and Linux.

## Step 1: Install OpenCode

Pick **one** method from the table — the first one that matches you. All methods produce the same `opencode` command.

| Your situation | Command | Where to run it |
|---|---|---|
| Linux, macOS, or WSL (easiest) | `curl` one-liner — see just below the table | Terminal |
| You already use **Node.js** | `npm install -g opencode-ai` | Terminal |
| macOS/Linux with **Homebrew** | `brew install anomalyco/tap/opencode` | Terminal |
| Arch Linux | `sudo pacman -S opencode` (stable) or `paru -S opencode-bin` (newest) | Terminal |
| Windows without WSL | `choco install opencode` **or** `scoop install opencode` **or** `npm install -g opencode-ai` | PowerShell |
| You prefer containers | `docker run -it --rm ghcr.io/anomalyco/opencode` | Anywhere Docker runs |

Note the `|` in the curl line below is a real pipe character. Copy it exactly as printed:

```bash
curl -fsSL https://opencode.ai/install | bash
```

### Verifying the install

Whatever method you chose, check it worked:

```bash
opencode --version
```

You should see a version number print and the shell come back. If instead you see `command not found`, your shell does not yet know where `opencode` lives. Two usual causes:

1. **You just installed it** and the shell has a stale list of commands. Close the terminal window completely, open a fresh one, and try again. This fixes it surprisingly often.
2. **The install directory is not on your PATH** (the list of folders your shell searches). The npm method is the classic case — try `npx opencode` as a stopgap, or find the folder npm used (`npm config get prefix`) and read Troubleshooting (Chapter 9) for the PATH fix.

### Keeping it updated

AI tooling moves quickly; update every few weeks:

```bash
opencode upgrade        # if your version supports it
```

or simply re-run the install command for your method — installers happily overwrite an older copy. Check what you have with `opencode --version`.

### Uninstalling (for completeness)

| Method | Uninstall command |
|---|---|
| npm | `npm uninstall -g opencode-ai` |
| Homebrew | `brew uninstall opencode` |
| Arch | `sudo pacman -R opencode` |
| Chocolatey | `choco uninstall opencode` |
| curl script | Delete the `opencode` binary from the folder the installer reported (often `~/.opencode/bin` or similar), then remove that folder from PATH |

## Step 2: First launch

Now for your first ten wins. Work through this checklist in order — do not skip the practice folder; it keeps the mess far from anything important.

**Your first-session checklist:**

- [ ] Have the version confirmed (`opencode --version` works)
- [ ] Create a playground, e.g. `mkdir ~/opencode-playground && cd ~/opencode-playground`
- [ ] Start the program: `opencode`
- [ ] See the chat interface
- [ ] Exit safely and re-launch it once, so the start/stop cycle is familiar

Type `opencode` and press **Enter**:

```bash
cd ~/opencode-playground
opencode
```

You will drop into the TUI: a chat area, a prompt at the bottom, and a help line. The basics:

- **Type a message and press Enter** to send it.
- **`Ctrl+C` twice, or type `/exit`** to leave.
- **`/help`** lists every special command.

Commands that start with `/` go to OpenCode itself, not to the AI `—` think of them as the program's menu. You will use these five constantly:

| Command | What it does |
|---|---|
| `/help` | List all commands and key binds |
| `/connect` | Attach a provider/model (Chapter 3 does this together with you) |
| `/models` | Pick or switch the model you are using |
| `/init` | Have OpenCode analyse the current folder and write `AGENTS.md` |
| `/undo`, `/redo` | Back out or re-apply the last set of changes |

A few keys worth knowing early:

- **Tab** toggles **Plan ↔ Build** mode (bottom-right shows which you are in).
- **@** while typing lets you fuzzy-search and reference files in this project — the single most useful beginner key.
- **Drag an image** into the window to attach a screenshot for the AI to look at.

If the display looks scrambled (misaligned lines, colours everywhere), your terminal is the culprit, not you — return to the table at the top and try Ghostty, WezTerm, or Kitty. Chapter 9 has more fixes.

## Step 3: Meet `AGENTS.md` (your project's welcome note)

While still in the playground, run:

```
/init
```

OpenCode will look around, and in an empty folder it has little to say — that is fine and quick. In a real project it writes an `AGENTS.md` file in the project root describing structure, style, and how to run things. Two habits to build now:

1. **Re-run `/init` after big structural changes** so the welcome note stays accurate.
2. **Commit `AGENTS.md` to Git** (Chapter 6). It is part of your project, and committing it means the AI (and collaborators) always have the same briefing.

Later, you can *hand-edit* `AGENTS.md` to add house rules, e.g. "always answer in plain English" or "never edit files in `./archive`". OpenCode reads it as instructions every session.

## Step 4: Point OpenCode at a model

Right now OpenCode is a car with no engine: it has no model to think with. The `/connect` command walks you through attaching one — another provider, a subscription you already own, or a model running on your own machine. That is the entire subject of Chapter 3, which is where we go next.

## Where your credentials live (so you stop worrying)

When you paste an API key during `/connect`, OpenCode stores it on your machine — in `~/.local/share/opencode/auth.json` on Linux/macOS/WSL — not inside your project folder. Three consequences:

- You **can** commit your project to git without leaking keys (but check anyway — Chapter 6 shows how).
- Anyone with access to your user account can read that file, like any password cache.
- If you suspect it leaked, revoke the key at the provider's website, not by deleting the file — then re-connect.

## Common first-run feelings (and why they are fine)

- *"The terminal feels alien."* It is a muscle, not a talent. You will use about six commands for 90% of your work, and this book prints every one.
- *"I'm afraid I'll break something."* With Git (Chapter 6) you gain a time machine. Until then, stay in your playground folder.
- *"The AI's answers feel vague."* Almost always the prompt, not the tool — and Chapter 5 is entirely about prompts.

## Checkbox recap of this chapter

- [ ] Chose and opened a good terminal (WSL on Windows)
- [ ] Installed OpenCode with one command
- [ ] `opencode --version` prints a version
- [ ] Launched and exited the TUI
- [ ] Ran `/init` in a practice folder
- [ ] Know where `~/.local/share/opencode/auth.json` lives

When every box is ticked, you are ready to give your agent a brain — for free.

---
