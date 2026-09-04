# Handoff — investment function repository, set-up session

**Date:** 2026-09-03
**Written by:** Claude, at the end of the set-up session
**For:** Stu and Danni, and any later session on any account
**Source:** Written from this session's work. Not a meeting record.
**Fed decisions:** D-0006 (adoption of this repository)

This document exists so the work can continue without the conversation that
produced it. Read it top to bottom once; after that, CLAUDE.md is the
operating manual.

---

## 1. What this repository is

The decision record and knowledge base for the personal investment function
of Stu Hilditch and Danni Cullen. It covers how money leaves Moncel and how
it is invested once it arrives. It is documents only: no application code.

Repository: `github.com/stuhilditch/investing`, private, branch `main`.

**Read order at the start of any session** (also in CLAUDE.md):

1. `policy/extraction-policy.md` — how money leaves Moncel today
2. `policy/investment-policy-statement.md` — how money is invested today
3. `context/tax-constraints.md` — the fifteen rules that bind every choice
4. `decisions/README.md` — the index and the record format

**The three rules that hold it together:**

- A choice is made only in a numbered record under `decisions/`. Policy and
  context never introduce a choice of their own.
- An accepted record is frozen. The only later edit is stamping
  `superseded-by` when a new record replaces it.
- Every policy clause cites the record that set it, as `[D-NNNN]`. When a
  record is accepted, the policy is updated in the same commit.

Records with `materiality: policy` (anything that changes a policy, moves
money out of Moncel, or opens an account or entity) need both Stu and Danni
named as `deciders` before status may become `accepted`.

---

## 2. What is in it now

| Folder | Contents |
|---|---|
| `decisions/` | Records 0001 to 0006, all `accepted`, plus the index and format convention |
| `policy/` | `extraction-policy.md` (10 clauses), `investment-policy-statement.md` (4 clauses, mostly "not yet decided") |
| `context/` | `entities.md`, `money-flow.md`, `tax-constraints.md` (C1 to C15), `advisors.md`, `digests/` (both Buzzacott reports) |
| `sources/` | Both Buzzacott reports of 2026-05-07, Danni's proposal of 2026-08-27, and the provenance table |
| `notes/` | The June owners meeting, the July Q2 review, the May Buzzacott meeting, the proposal analysis, and this document |
| `.claude/skills/` | Ten skills (see section 5) |
| `docs/superpowers/` | The design spec and implementation plan for the repository itself |

**The six accepted records.** All are back-filled from existing evidence and
say so in their Context sections. They record decisions already taken before
this session, not new ones.

| No. | Decision | Date |
|---|---|---|
| 0001 | Australian corporate trustee appointed to both trusts before UK residency | 2026-05-08 |
| 0002 | Moncel Limited UK incorporated, 50/50 personally, outside the trusts, to bill UK work | 2026-05-19 |
| 0003 | Regular dividend of AUD 50,000 per month from June 2026 | 2026-06-08 |
| 0004 | Retain surplus in AIFS to an AUD 1.3M cash floor; extra distributions paused until reached | 2026-06-08 |
| 0005 | Any investment vehicle sits outside the UK and outside the trusts; Buzzacott consulted first | 2026-05-19 |
| 0006 | Adopt this repository as the decision record | 2026-09-03 |

---

## 3. What is NOT decided

**Nothing has been decided about Danni's proposal.** There is no decision
record for it. Stu had not read the proposal as of the end of this session.
The analysis in `notes/2026-09-03-analysis-of-danni-investment-proposal.md`
is input to a decision, not a decision.

The Investment Policy Statement is deliberately mostly empty. Objectives,
risk tolerance, allocation, instruments, jurisdiction, provider, currency,
contribution schedule, rebalancing and reporting are all listed as "not yet
decided" because no record has set them.

---

## 4. Danni's proposal and the analysis of it

**What she proposes** (`sources/2026-08-27-danni-investment-proposal-sp500-under-fig.pdf`,
eight pages, written by her Assistant from her Gemini research threads):

Open a joint Interactive Brokers account under a non-UK IBKR entity, fund it
in AUD directly from Australia, and buy CSPX (iShares Core S&P 500 UCITS ETF,
Irish-domiciled, accumulating, ISIN IE00B5BMR087) at about GBP 10,000 per
month until a Q1 2030 departure, claiming FIG relief each year. Projects
roughly GBP 460,000 to 490,000 on GBP 410,000 contributed. Rejects
US-domiciled ETFs, ISAs, pensions, offshore bonds, single stocks and
property, with reasons for each.

**Assessment: the right shape, not yet a clean yes.** Nothing in it breaks a
constraint. Five things are open.

1. **Fact conflict.** The proposal states UK residence and FIG eligibility
   from 18 May 2026. Buzzacott's report and this repository say 2026-05-11.
2. **Excess Reportable Income (C14).** CSPX reinvests dividends, so HMRC
   taxes the holder each year on income never received. Whether a FIG claim
   covers that is unsettled by the proposal's own admission. This is the
   largest open question.
3. **Inheritance tax situs (C6).** The proposal covers US estate tax but
   never asks whether an Irish fund held through a non-UK broker is outside
   UK inheritance tax. Open in this repository since May.
4. **Buzzacott sign-off (D-0005, C12).** Policy requires consultation before
   any vehicle is committed to. It has not happened for this account.
5. **Cost of the FIG claim (C2).** Claiming costs each person the personal
   allowance and CGT exemption for that year. Both have UK-source dividends
   from Moncel Limited UK, so this is real money annually and needs computing,
   not assuming away.

**What checked out.** CSPX was verified by ISIN against HMRC's published
reporting-fund list dated 2026-08-04, so it is a reporting fund and gains are
capital rather than income (C5 PASS). Funding from Australia without passing
through UK accounts is correct and keeps the money out of the UK inheritance
tax net. The temporary non-residence rule the proposal raises is real: after
four UK tax years, selling while abroad and returning within five years pulls
those gains back into UK tax (C13).

**Two choices that are Stu and Danni's alone**, not tax questions:

- CSPX alone (concentrated, cheaper) or a global tracker such as VWRA/VWRP
  (roughly 3,600 holdings, double the fee at 0.14%). The proposal frames this
  honestly as a deliberate concentration bet.
- Whether either has any plausible route to becoming a US taxpayer. That
  alone would flip the fund choice, because non-US funds are punitively taxed
  for US persons (C15).

---

## 5. Skills installed

All in `.claude/skills/`, so they travel with the repository. Each
third-party skill was read for prompt injection, network calls and credential
access before copying. `.claude/skills/README.md` records source, commit and
licence for each.

**Third party, nine skills.** From JoelLewis/finance_skills:
`investment-policy`, `asset-allocation`, `historical-risk`, `forward-risk`,
`currencies-and-fx`, `diversification`. From gauss314/skills: `portfolio`,
`yahoo-finance`, `historyofmarket`. All MIT. The gauss314 skills are written
in Spanish. Python scripts run with `uv run`; system Python has no numpy.

**Anthropic `wealth-management` plugin**, enabled at project scope, giving
`/rebalance`, `/proposal`, `/financial-plan` and `/client-report`. Its tax
logic is US-only; ignore that part.

**Household skill `uk-fig-investing`.** Written this session because no public
skill knows UK rules. It supplies the fifteen constraints, an output contract
(facts reconciled, constraint table, external verification, adviser
questions, household specifics, decision routing), and
`scripts/check_reporting_fund.py`, which checks any ISIN against HMRC's
published reporting-fund list.

Built and tested with the official skill-creator process: three test prompts
run with and without the skill, graded against 30 assertions. Pass rate 100%
with the skill against 52% without, at a cost of about 35 seconds and 7% more
tokens per answer. Test set is at `.claude/skills/uk-fig-investing/evals/`.
The test workspace is git-ignored and local to Stu's machine.

**Apply `uk-fig-investing` to any investment question.** The nine third-party
skills all assume a US taxpayer and will otherwise apply US concepts (IRA,
401k, Roth, wash sale) to this household.

---

## 6. Open items

**For Stu and Danni:**

1. Read the proposal and the analysis note.
2. Choose between CSPX and a global tracker.
3. Answer the US-taxpayer question for Buzzacott.

**For Buzzacott**, six questions, all in section 4 of the analysis note:
the residence date, ERI under FIG, IHT situs of the fund, sign-off on the
IBKR structure, temporary non-residence exposure, and the US-person route.

**For Interactive Brokers**, two questions: which legal entity the joint
account opens under, and joint tenancy plus W-8BEN documentation.

**Then, and only then:** draft the next-numbered decision record as
`proposed`, following the "A proposal arrives" task in CLAUDE.md.

**Elsewhere, touching the tax position but not this repository's job:**

- ATO overdue tax debt notice for Stu, forwarded by William Buck 2026-08-17.
- CIFS director change from Stu and Danni to Rod, agreed 2026-08-06 for
  filing effective 2026-08-24. Not filed as of this session. Drew owns it.
- Buzzacott written analyses requested 2026-05-19 and not yet seen: Moncel
  RTO's dormancy given its services to AIFS, and the contracting counterparty
  for Moncel Limited UK.
- D&O insurance for the corporate trustee and operating entities, open since
  May.

---

## 7. Housekeeping and gotchas

- **Git remote.** Still points at the old repository name. Run:
  `git remote set-url origin https://github.com/stuhilditch/investing.git`
  A permission classifier blocked this during the session. Pushes work
  through GitHub's redirect in the meantime.
- **Provenance paths.** `~/Moncel/Inbox/` was moved to
  `~/Moncel/Assistant/archive/misc/Inbox/` and the assistant deliverables to
  `~/Moncel/Assistant/archive/v1/` by something outside this session. Rows in
  `sources/README.md` point at those archive paths and go stale if the folder
  moves again.
- **Remaining `confirm` markers in `context/entities.md`:** Moncel RTO
  directors, whether Daniel Hillier is still a Foundation director, the
  Moncel RTO dormancy analysis, and the Moncel Limited UK services-agreement
  counterparty. Confirmed on 2026-09-03: one corporate trustee company acts
  for both trusts, and Stu and Danni remain directors of CIFS and the
  Foundation.
- **CLI model id.** Claude Code 2.1.250 rejects `claude-fable-5-1` in
  `claude -p`. Use `claude-opus-5` for skill-creator scripts.
- **Connectors.** Several MCP servers in this environment need authorising
  before their tools work, including GitHub, Slack, Atlassian, Notion and
  Linear. Authorise through claude.ai connector settings or `claude mcp` in
  an interactive session.
- **Verification.** The five-check list is in CLAUDE.md. Run it before
  reporting any change complete. All five passed at the end of this session.

---

## 8. Decisions Claude made on Stu's behalf during the build

Recorded so they can be reviewed and reversed.

- Built on a branch in the main checkout rather than a git worktree, then
  merged. Documents only, no build to isolate.
- Batched the nine build tasks into three implementer dispatches rather than
  nine, giving larger review diffs.
- Copied the Buzzacott PDFs from the archive path after the source folder
  moved mid-session, and wrote archive paths into the provenance table.
- Did not edit frozen records to close a provenance gap the final review
  found. Added `notes/2026-05-19-buzzacott-meeting.md` and provenance rows
  instead, so record 0005's own `sources` list still names only the two
  digests.
- Left two minor review findings unfixed: extraction policy clause 10 is
  slightly stronger than the record it cites, and the July note says "Moncel
  Canada", which is not an entity name.
- Fixed a faulty verification command in CLAUDE.md but left the design spec
  as a historical record, so the spec still contains the original.
