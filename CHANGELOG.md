# Changelog

## 1.1.0 — 2026-10-17

- Evidence labels: every finding is tagged Strong, Solid, Mixed, Thin or
  Untested, and every verdict states its label.
- Mode C: rank a list of test ideas, with a note on which pairs shouldn't run
  at the same time.
- Mode A answers end with a "How to read it" line: primary metric, guardrail,
  and the platform or geo split to check.
- A lookup table routes common questions (exit discount, hard paywall, loader
  screens) to the right library section and to the cross-flow cases.
- Explicit handling for questions the library doesn't cover: say so, answer
  without numbers, never borrow a range from another element.
- Two worked examples (grading one idea, a stuck user) to anchor the format.
- Answers follow the user's language.
- Evidence library moved to `references/evidence-library.md`, with a short
  glossary (ARPU, CR, trial-to-paid, Tier-1, guardrail).
- Fixed figures that broke the skill's own rules: the CTA and limit-triggered
  paywall results were quoted as sharp single-test numbers and are now bands;
  the second-chance discount figure now matches between its two sections.
- Removed the reference to a "potential" signal the library never carried.
- Packaged as a Claude Code plugin marketplace; a GitHub release builds the zip
  for claude.ai after a frontmatter and honesty-rule check.

## 1.0.0

- First version: two modes (grade an idea, help a stuck user), evidence library
  by paywall element, onboarding, and cross-flow tests.
