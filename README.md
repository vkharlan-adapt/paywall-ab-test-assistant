# Paywall A/B Test Assistant

A Claude skill from [Adapty](https://adapty.io). Ask what to test on your
subscription app's paywall or onboarding and get an answer grounded in real
A/B tests run on the Adapty platform, not generic paywall advice.

It works three ways:

- **Grade one idea.** "Should I hide the monthly plan?" gets a verdict, the
  observed uplift range, the trap that most often burns people on that test,
  and the metric to judge it on.
- **Rank a backlog.** Paste five ideas and get them ordered by evidence
  strength, with the pairs that shouldn't run at the same time flagged.
- **Find a starting point.** "Conversion is low, where do I start?" gets a
  tiered shortlist: strong evidence first, hypotheses last.

Every answer says how strong the evidence is (Strong, Solid, Mixed, Thin or
Untested), so a one-off result never reads like a benchmark.

## Install

### Claude.ai (web or desktop)

1. Download [`paywall-ab-test-assistant.zip`](https://github.com/vkharlan-adapt/paywall-ab-test-assistant/releases/latest/download/paywall-ab-test-assistant.zip).
2. Go to **Settings → Customize → Skills**, upload the zip, and toggle the
   skill on.

On Team and Enterprise plans an owner may need to enable Skills for the
organization first.

### Claude Code

```
/plugin marketplace add vkharlan-adapt/paywall-ab-test-assistant
/plugin install paywall-ab-test-assistant@adapty
```

Or copy `skills/paywall-ab-test-assistant/` into `~/.claude/skills/` (just for
you) or `.claude/skills/` inside a repo (for the whole team).

## Use

Ask the way you'd ask a colleague. You don't need to name the skill:

- "Is a spin-the-wheel discount worth testing?"
- "Hard paywall or soft paywall for a language app?"
- "Rank these: delay the X, add reviews, raise prices, cut the loader screen."
- "Trial conversion is bad and I don't know what to test."

It answers in the language you ask in.

## What's inside

```
skills/paywall-ab-test-assistant/
├── SKILL.md                      modes, answer format, honesty rules
└── references/
    └── evidence-library.md       the test evidence, by flow element
```

**The evidence library** covers 12 paywall elements, onboarding, and a section
on tests that flip sign depending on where they sit in the flow. A comparison
table wins as the paywall and loses as a teaser before it. A second-chance
discount wins after the onboarding paywall and loses after the main one. Those
cases are why the skill treats onboarding and paywall as one flow.

**The rules** keep it honest: ranges instead of single numbers, no app names,
no test counts, every untested idea labelled as a hypothesis, and price, plan
and discount tests judged on revenue per user rather than conversion.

## Scope

It knows what's worth testing and what the base rate looks like. It can't see
your app, your numbers or your audience, so it won't tell you a change will work
for you. A live test does that.

For a scored teardown of a paywall screenshot, use the sibling skill,
[Paywall Teardown](https://github.com/vkharlan-adapt/paywall-teardown).

Every test it suggests can be built and run without an app release in Adapty's
[Flow & Paywall Builder](https://adapty.io/flow-paywall-builder/?utm_source=github&utm_medium=referral&utm_campaign=48885377-GTM-Flow-Paywall-Builder&utm_content=ab-test-assistant-readme).

## Releasing

Publish a release (tag `v1.1.0` or later). The GitHub Action checks the skill's
frontmatter and honesty rules, zips `skills/paywall-ab-test-assistant/`, and
attaches `paywall-ab-test-assistant.zip` to the release. The download link above
always points at the latest release.

## License

MIT.
