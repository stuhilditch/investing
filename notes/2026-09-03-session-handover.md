# Session hand-over — repository set-up day

**Date:** 2026-09-03
**Attendees:** Stu Hilditch with Claude
**Source:** Written by Claude at the end of the set-up session so a session on
another account can continue without this conversation's history.
**Fed decisions:** D-0006 (adoption of this repository)

## What exists

- Decision log 0001 to 0006, all `accepted` and back-filled from evidence;
  two living policy documents; context files including fifteen tax
  constraints C1 to C15; digests of both Buzzacott reports of 2026-05-07;
  sources and provenance table; this `notes/` folder.
- `.claude/skills/`: nine vetted third-party skills (JoelLewis finance_skills
  and gauss314 skills), the Anthropic `wealth-management` plugin at project
  scope, and the household skill `uk-fig-investing`, built and tested with the
  official skill-creator process (3 test prompts; 100% assertion pass rate
  with the skill against 52% without). Its script
  `scripts/check_reporting_fund.py` checks any ISIN against HMRC's published
  reporting-fund list.
- Danni's proposal of 2026-08-27 in `sources/`, and Claude's analysis of it in
  `notes/2026-09-03-analysis-of-danni-investment-proposal.md`.

## Not decided

No decision record exists for Danni's proposal. Stu has not yet read the
proposal. The analysis note is input only.

## Open items, in priority order

1. Stu and Danni read the proposal and the analysis note.
2. Settle with Buzzacott: UK residence start 2026-05-11 (Buzzacott) versus
   18 May 2026 (proposal); whether Excess Reportable Income from CSPX is
   covered by a FIG claim (C14); UK IHT situs of an Irish ETF held via a
   non-UK broker (C6); sign-off on the IBKR structure per D-0005; temporary
   non-residence exposure (C13); any plausible US-taxpayer route (C15).
3. Stu and Danni choose between CSPX alone and a global tracker (VWRA/VWRP).
4. Then draft the next-numbered decision record as `proposed`, following
   CLAUDE.md "A proposal arrives".
5. Housekeeping: local git remote still points at the old repository name
   (`investment`); run
   `git remote set-url origin https://github.com/stuhilditch/investing.git`.
   Provenance rows in `sources/README.md` point at
   `~/Moncel/Assistant/archive/` paths that go stale if that folder moves.
   Remaining **confirm** markers in `context/entities.md`: Moncel RTO
   directors, whether Daniel Hillier is still a Foundation director, Moncel
   RTO dormancy analysis, Moncel Limited UK services-agreement counterparty.
   The CIFS director change to Rod (agreed 2026-08-06) has not been filed.

## Process notes for the next session

- Read order and rules are in CLAUDE.md. Apply `uk-fig-investing` to any
  investment question; it produces the six-part evaluation the analysis note
  follows.
- Skill test workspace `.claude/skills/uk-fig-investing-workspace/` is
  git-ignored and local to Stu's machine; it can be regenerated from
  `.claude/skills/uk-fig-investing/evals/evals.json`.
- The installed Claude Code CLI (2.1.250) rejects the `claude-fable-5-1`
  model id in `claude -p`; use `claude-opus-5` for skill-creator scripts.
