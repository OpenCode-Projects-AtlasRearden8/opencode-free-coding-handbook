"""Tests for the "Free AI Coding with OpenCode" manual and site builder.

Run with:
    python3 -m unittest discover -s tests -v

Checks:
- book structure (chapters exist, word count >= 10,000)
- markdown conversion correctness (headings, tables, code, checkboxes, links)
- full build into a temporary site/ (pages valid, nav present, no external assets)
- privacy sweep (no secret-shaped strings anywhere in docs or generated site)
- LICENSE contains the required exact copyright line
"""

import pathlib
import re
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

DOCS = ROOT / "docs"
SITE = ROOT / "site"


class TestBookContent(unittest.TestCase):
    def setUp(self):
        self.slugs = build.chapter_slugs()
        self.texts = {s: build.read_text(DOCS / f"{s}.md") for s in self.slugs}

    def test_required_chapters_exist(self):
        required = [
            "index",
            "01-what-is-opencode",
            "02-installing-opencode",
            "03-picking-free-models",
            "04-permissions-and-safety",
            "05-writing-good-task-prompts",
            "06-git-basics",
            "07-reviewing-ai-changes",
            "08-limits-of-free-tiers",
            "09-troubleshooting",
            "10-appendix-checklists",
        ]
        for slug in required:
            self.assertIn(slug, self.slugs, f"missing chapter: {slug}.md")

    def test_every_chapter_has_title_and_body(self):
        for slug, text in self.texts.items():
            self.assertIn("# ", text, f"{slug}: no H1 title")
            self.assertGreater(len(text.split()), 300, f"{slug}: suspiciously short")

    def test_word_count_at_least_ten_thousand(self):
        total = sum(len(t.split()) for t in self.texts.values())
        self.assertGreaterEqual(total, 10000, f"book is only {total} words")

    def test_manual_has_tables_and_checklists(self):
        all_text = "\n".join(self.texts.values())
        self.assertGreaterEqual(all_text.count("\n| "), 20, "expected many tables")
        self.assertGreaterEqual(len(re.findall(r"^- \[ \]", all_text, re.M)), 15, "expected checklists")

    def test_internal_md_links_resolve(self):
        for slug, text in self.texts.items():
            for m in re.finditer(r"\]\(([^#http][^)]*\.md)\)", text):
                target = m.group(1)
                self.assertTrue((DOCS / target).exists(), f"{slug}: broken link {target}")


class TestMarkdownConversion(unittest.TestCase):
    def test_headings_get_ids(self):
        html = build.md_to_html("# Hello There\n\ntext")
        self.assertIn("<h1 id=\"hello-there\">", html)

    def test_table_renders(self):
        html = build.md_to_html("| a | b |\n|---|---|\n| 1 | 2 |\n")
        self.assertIn("<table>", html)
        self.assertIn("<th>", html)

    def test_fenced_code_renders(self):
        html = build.md_to_html("```bash\ngit status\n```\n")
        self.assertIn("<pre>", html)
        self.assertIn("git status", html)

    def test_open_task_item_becomes_styled_todo(self):
        html = build.md_to_html("- [ ] Water the plants\n")
        self.assertIn('class="todo"', html)
        self.assertIn("☐", html)

    def test_done_task_item_becomes_styled_done(self):
        html = build.md_to_html("- [x] Water the plants\n")
        self.assertIn('class="done"', html)
        self.assertIn("☑", html)

    def test_task_marker_inside_code_fence_is_untouched(self):
        html = build.md_to_html("```\n- [ ] literal in code\n```\n")
        self.assertNotIn('class="todo"', html)
        self.assertIn("[ ] literal in code", html)

    def test_md_link_rewritten_to_html(self):
        html = build.md_to_html("[Git](06-git-basics.md)")
        self.assertIn('href="06-git-basics.html"', html)
        self.assertNotIn("06-git-basics.md", html)


class TestBuildOutput(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="site-test-")
        real_site = build.SITE
        build.SITE = pathlib.Path(cls.tmp)
        try:
            build.build()
        finally:
            build.SITE = real_site
        cls.out = pathlib.Path(cls.tmp)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_expected_files_generated(self):
        slugs = build.chapter_slugs()
        for slug in slugs:
            self.assertTrue((self.out / f"{slug}.html").exists(), f"missing site/{slug}.html")
        for name in ("index.html", "full-book.html", "style.css"):
            self.assertTrue((self.out / name).exists(), f"missing site/{name}")

    def test_pages_are_valid_figments(self):
        for page in self.out.glob("*.html"):
            text = page.read_text(encoding="utf-8")
            self.assertIn("<!DOCTYPE html>", text, f"{page.name}: no doctype")
            self.assertIn("</html>", text, f"{page.name}: unclosed html")
            self.assertIn('lang="en"', text)
            self.assertIn("charset=\"utf-8\"", text)

    def test_pages_use_local_stylesheet_only(self):
        for page in self.out.glob("*.html"):
            text = page.read_text(encoding="utf-8")
            self.assertIn('href="style.css"', text)
        style = (self.out / "style.css").read_text(encoding="utf-8")
        self.assertNotIn("http://", style)
        self.assertNotIn("https://", style)

    def test_chapter_pages_have_prev_next_nav_and_credit(self):
        text = (self.out / "09-troubleshooting.html").read_text(encoding="utf-8")
        self.assertIn('class="nav"', text)
        self.assertIn('<a href="10-appendix-checklists.html"', text)
        self.assertIn('href="08-limits-of-free-tiers.html"', text)
        self.assertIn("Asdale Dynamics, LLC", text)

    def test_full_book_contains_all_chapters(self):
        text = (self.out / "full-book.html").read_text(encoding="utf-8")
        for slug in build.chapter_slugs():
            md_text = build.read_text(DOCS / f"{slug}.md")
            title, _ = build.chapter_title(md_text, slug)
            fragment = title.split("—")[0].strip()[:20].replace("&", "&amp;")
            self.assertIn(fragment, text, f"full-book is missing '{title}'")

    def test_landing_lists_every_chapter(self):
        text = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn("Contents", text)
        for slug in build.chapter_slugs():
            self.assertIn(f'href="{slug}.html"', text, f"index missing link to {slug}")


class TestPrivacyAndLicense(unittest.TestCase):
    SECRET_PATTERNS = [
        re.compile(r"sk-[A-Za-z0-9]{10,}"),          # OpenAI-style key
        re.compile(r"AKIA[0-9A-Z]{16}"),             # AWS access key
        re.compile(r"ghp_[A-Za-z0-9]{20,}"),         # GitHub PAT
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY"),# PEM key material
        re.compile(r"nvapi-[A-Za-z0-9]{10,}"),       # NVIDIA-style key
    ]
    no_real_secrets = True

    def test_no_secret_shaped_strings(self):
        targets = []
        targets.extend((ROOT / "docs").glob("*.md"))
        if SITE.is_dir():
            targets.extend(SITE.glob("*.html"))
            targets.extend(SITE.glob("*.css"))
        for path in targets:
            text = path.read_text(encoding="utf-8")
            for pattern in self.SECRET_PATTERNS:
                self.assertIsNone(
                    pattern.search(text),
                    f"{path.name}: looks like a secret: {pattern.pattern}",
                )

    def test_license_line_exact(self):
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        # The MIT template uses (c) for the copyright symbol; the requirement
        # is the exact line below.
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", text)

    def test_readme_credits_asdale(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", text)


if __name__ == "__main__":
    unittest.main()
