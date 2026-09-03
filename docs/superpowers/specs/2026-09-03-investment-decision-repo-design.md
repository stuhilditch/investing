# Investment Function Decision Repository — Design

**Date:** 2026-09-03
**Status:** Approved in conversation, pending written review
**Owners:** Stu Hilditch and Danni Cullen

## 1. Purpose

This repository is the decision record and knowledge base for the personal
investment function that Stu and Danni operate on top of Moncel. Moncel's
single objective is to produce profit that transfers to this function. The
repository records how that money leaves Moncel and how it is invested once it
arrives, in the style of Architectural Decision Records.

It is a knowledge base first. It holds no code, no tooling and no reporting in
this version.

## 2. Scope

**In scope: extraction through investment.** Two domains with a clear seam.

- **Extraction.** Owner-level decisions about how much leaves Moncel, when,
  and through which channel: dividend level and formula, cash floors that gate
  extra distributions, trust distribution timing, transfer channel and
  currency, and the role of Moncel Limited UK. The corporate trustee and the
  AIFS board execute these decisions; the owners make them.
- **Investment.** Decisions from the point cash is in Stu and Danni's hands:
  objectives, risk, allocation, instruments, jurisdiction, accounts, currency,
  rebalancing.

**Out of scope for this version.** Moncel's internal governance (board
protocol, cash management, cost control). Personal tax compliance and the FIG
election mechanics beyond recording them as constraints. Property, pensions and
estate planning. Reporting and portfolio tracking. Scripts or tooling. Formal
meeting agenda and minutes formats. Copying the executed legal documents.
Each of these becomes a decision record when it is needed.

## 3. Sensitivity

Decision records carry the actual figures decided. Portfolio values may be
recorded once investing begins. Account numbers, account identifiers,
credentials, API keys and tokens are never written anywhere in the repository.
The repository lives on a private GitHub remote that Stu creates.

## 4. Participants and approval

Decisions are tiered by materiality, recorded in a `materiality` field:

- **operational** — within an already-accepted policy (e.g. rebalancing to an
  agreed allocation). Stu alone may accept.
- **policy** — changes a policy, moves money out of Moncel, or opens a new
  account or entity. Requires both Stu and Danni named as deciders before the
  record may become `accepted`.

Claude drafts records and analysis. Claude is not a licensed adviser; its
analysis is input to a decision the owners make. Anything touching tax
treatment is flagged for Buzzacott or William Buck, not asserted.

## 5. Directory layout

```
investing/
├── README.md        # what this repo is, how to read it, where to start
├── CLAUDE.md        # session instructions for Claude
├── decisions/       # numbered records, immutable once accepted
│   ├── README.md    # index table + record format convention
│   └── NNNN-short-title.md
├── policy/          # living documents stating the current position
│   ├── extraction-policy.md
│   └── investment-policy-statement.md
├── context/         # facts about the world, not choices; updated freely
│   ├── entities.md
│   ├── money-flow.md
│   ├── tax-constraints.md
│   ├── advisors.md
│   └── digests/     # plain-English digest of each advisor document
├── sources/         # original advisor documents, never edited
│   └── README.md    # provenance table
├── notes/           # dated informal notes and transcripts; no imposed structure
└── docs/superpowers/specs/   # this design and future specs
```

Three rules hold the layout together:

1. Decisions are the only place a choice is made, and are immutable once
   accepted.
2. Policy documents state the current position, and every clause cites the
   decision that set it.
3. Context documents describe facts, not choices, and are updated as facts
   change. Sources are never edited.

Naming: ISO dates (`YYYY-MM-DD`) where a document has a date; four-digit
sequence numbers for decisions, one sequence across both domains. No template
files; formats are conventions written into the relevant README.

## 6. Decision records

File: `decisions/NNNN-short-title.md`.

Header (YAML front matter):

```yaml
---
number: 0007
title: Adopt Danni's proposed initial portfolio
domain: investment          # extraction | investment | both
materiality: policy         # operational | policy
status: proposed            # proposed | accepted | rejected | superseded
proposed: 2026-09-05
decided:                    # date accepted or rejected
deciders: [Stu, Danni]      # both required when materiality is policy
supersedes:                 # number, if any
superseded-by:
sources: []                 # repo-relative paths: sources/, notes/, context/digests/
---
```

Body sections, in order:

- **Context** — what prompted the decision and which constraints bind it,
  citing `context/tax-constraints.md` and relevant digests.
- **Options considered** — each option with its case for and against.
- **Decision** — what was chosen, one paragraph.
- **Consequences** — what changes in policy, what it costs, what risks are
  accepted, what must be checked with advisers.
- **Review** — when the decision should be revisited, if ever.

Lifecycle is a one-way ratchet:

1. Created as `proposed`. Discussion and analysis happen against it. Long
   analysis goes in `notes/` and is linked from the record.
2. Moves to `accepted` or `rejected`, with `decided` filled in. From this
   point the body is frozen.
3. A later change of mind is a new record naming the old one in `supersedes`.
   The old record receives `superseded-by` and status `superseded`. This is
   the only edit ever made to a frozen record.
4. When a record is accepted, the matching policy document is updated in the
   same commit.

Back-filled records reconstructed from meeting notes rather than signed
documents say so in their Context section.

### Danni's forthcoming investment proposal

The proposal document goes into `sources/` with a provenance entry. Claude
drafts a `proposed` record whose Options section sets out the proposal
alongside alternatives and tests each against `context/tax-constraints.md`.
Detailed working goes in `notes/`. The owners' discussion accepts, rejects, or
returns it for revision. On acceptance, the Investment Policy Statement gains
its first substantive clauses.

## 7. Policy documents

Each is a numbered list of plain-English clauses. Every clause ends with a
citation to the decision that set it, e.g. `[D-0004]`. A clause without a
citation is not permitted. Each document opens with a short "Current position"
paragraph and a "Not yet decided" list so gaps are visible.

- `policy/extraction-policy.md` — regular dividend level and formula;
  conditions for extra distributions; the AIFS cash floor; trust distribution
  timing; channel and currency for moving funds; Moncel Limited UK's role.
- `policy/investment-policy-statement.md` — objectives and time horizon; risk
  tolerance; asset allocation; permitted and prohibited instruments;
  jurisdiction and account structure; currency policy; rebalancing; reporting.
  At seeding this is mostly the "Not yet decided" list plus the one
  established principle: any vehicle sits outside the UK and outside the
  trusts pending advice. Reporting carries a placeholder clause: cadence and
  format to be decided once the first investment is made.

## 8. Context documents

- `context/entities.md` — each entity with jurisdiction, tax residency,
  directors, shareholders or trustee, and role in the flow: GHS Hilditch
  Trust, Ellell Trust, GHS Ellell Management Pty Ltd (corporate trustee),
  AIFS, Moncel Australia (RTO) Pty Ltd, CIFS, Userve Inc, AIFS Foundation,
  Moncel Limited UK.
- `context/money-flow.md` — the pipeline from AIFS profit to a UK account,
  showing at each step who decides, which entity acts, and where tax attaches.
- `context/tax-constraints.md` — rules that bind choices, each stated as a
  constraint with its source: FIG eligibility window (2026/27 to 2029/30) and
  the cost of a claim (loss of personal allowance and CGT annual exempt
  amount; no foreign loss relief); settlor-interested treatment of both
  trusts; the TOAA motive defence and its 6 April 2012 boundary; offshore
  income gains and reporting-fund status; UK-situs assets inside IHT; the
  long-term-resident threshold (10 of 20 years) and its consequences for the
  trusts; Trust Registration Service triggers; no assets added to the trusts
  while UK resident; Moncel RTO must remain dormant. Also lists open items
  tracked elsewhere: the ATO overdue tax debt notice of 2026-08-17 and the
  CIFS director change being backdated to 2026-08-24.
- `context/advisors.md` — Buzzacott (UK tax, corporate residency), William
  Buck (AU tax, trust compliance, ASIC), Russell Kennedy (AU legal; noted as
  not to be used further per Stu 2026-07-14), Andrew Phillips (corporate
  trustee sole director, AIFS director): people, scope, engagement.
- `context/digests/` — one digest per advisor document, structured as
  Summary, Assumptions the advice relies on, Constraints it imposes, Open
  questions. Seeded with the two Buzzacott reports of 2026-05-07.

## 9. Seed content

Back-filled decision records, all `accepted`:

| No. | Title | Domain | Materiality | Date |
|---|---|---|---|---|
| 0001 | Appoint an Australian corporate trustee to both trusts before UK residency | extraction | policy | 2026-05-08 |
| 0002 | Incorporate Moncel Limited UK, owned 50/50 outside the trusts, to bill UK work | extraction | policy | 2026-05-19 |
| 0003 | Regular dividend of AUD 50,000 per month from June 2026 | extraction | policy | 2026-06-08 |
| 0004 | Retain surplus in AIFS to an AUD 1.3M cash floor; pause extra distributions until reached | extraction | policy | 2026-06-08 |
| 0005 | Any investment vehicle sits outside the UK and outside the trusts; consult Buzzacott before incorporating | investment | policy | 2026-05-19 |
| 0006 | Adopt this repository as the decision record for the investment function | both | policy | 2026-09-03 |

Sources copied in: the two Buzzacott reports of 2026-05-07 from
`~/Moncel/Inbox/Buzzacott/`. `sources/README.md` also lists known documents
not copied pending confirmation: executed supplemental deeds, director
agreements, deeds of indemnity, and Danni's forthcoming proposal.

Notes seeded: `notes/2026-06-08-owners-meeting-dividends-and-cash-floor.md`
and `notes/2026-07-23-q2-financial-review.md`, holding the Granola summaries
retrieved on 2026-09-03.

Not seeded: nothing from the `~/Moncel/Assistant/` workspace is copied.

## 10. CLAUDE.md

Short. Tells a session:

1. What the repository is and whose it is.
2. Reading order at session start: both policy documents, then
   `context/tax-constraints.md`, then `decisions/README.md`.
3. Rules: decisions only through a record; accepted records frozen except the
   superseded-by stamp; every policy clause cites a decision; policy-materiality
   decisions need both deciders before acceptance; no account identifiers or
   credentials anywhere.
4. What Claude is not: not a licensed adviser; analysis is input; tax
   treatment is flagged for advisers, not asserted.
5. How to handle common tasks: draft a proposed record from a proposal or a
   meeting; update policy on acceptance; write a digest for new advice; pull a
   Granola transcript into `notes/`.
6. The verification checklist (Section 12).

## 11. Conventions

- ISO dates everywhere.
- Every amount states its currency (AUD, GBP, CAD); never bare.
- Figures in decision records are the figures as decided, not live balances.
- One commit per decision state change so git history is the audit trail.
- Private GitHub remote created by Stu; the repository is initialised with no
  remote and the command to add one is given at hand-over.

## 12. Verification

No code, no test suite. Before reporting done, and at the end of any session
that changes records or policy, check:

1. Every policy clause cites an existing decision record.
2. Every record's `sources` paths resolve to files in the repository.
3. `decisions/README.md` index matches the files on disk.
4. `sources/README.md` provenance table matches the files on disk.
5. No file contains an account number, identifier or credential.

## 13. Approaches considered

- **Decision log plus living policy (chosen).** Immutable log for audit,
  living policy for the current position, one policy document per domain.
- **Pure decision log.** Simplest, but the current position exists only as
  the sum of non-superseded records and must be replayed each time.
- **Domain-partitioned trees.** Explicit seam in the layout, but cross-domain
  decisions have no natural home and templates and indexes double.
