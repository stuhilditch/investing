# Investment Decision Repository Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold and seed a documents-only repository that records Stu and Danni's extraction and investment decisions as immutable decision records with living policy documents on top.

**Architecture:** Append-only `decisions/` log (numbered, frozen once accepted) plus two living `policy/` documents whose every clause cites a decision. `context/` holds facts (entities, money flow, tax constraints, advisers, advice digests), `sources/` holds original adviser PDFs, `notes/` holds dated informal notes. No code.

**Tech Stack:** Markdown with YAML front matter, git. Verification is done with `ls`, `grep` and `test` in bash. No scripts are added to the repo.

**Spec:** `docs/superpowers/specs/2026-09-03-investment-decision-repo-design.md`

## Global Constraints

- ISO dates (`YYYY-MM-DD`) everywhere.
- Every amount states its currency (AUD, GBP, CAD); never bare.
- Never write account numbers, account identifiers, credentials, API keys or tokens anywhere.
- Decision files: `decisions/NNNN-short-title.md`, four-digit number, one sequence across both domains.
- Front matter fields and allowed values exactly as in spec Section 6: `domain` ∈ {extraction, investment, both}; `materiality` ∈ {operational, policy}; `status` ∈ {proposed, accepted, rejected, superseded}.
- Every policy clause ends with a citation of the form `[D-NNNN]` to an existing record.
- Back-filled records reconstructed from meeting notes say so in their Context section.
- Claude is not a licensed adviser; documents flag tax questions for Buzzacott or William Buck rather than asserting treatment.
- No templates folder; formats are conventions in READMEs.
- One commit per task. Commit messages end with `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
- Working directory: `/Users/stuarthilditch/Developer/investing`. Do not touch `~/Moncel/` except to copy the two PDFs named in Task 2.

---

## File map

| Path | Responsibility | Task |
|---|---|---|
| `README.md` | What the repo is, reading order, layout | 1, 9 |
| `decisions/README.md` | Record format convention + index table | 1, 7 |
| `sources/README.md` | Provenance table for original documents | 2 |
| `sources/2026-05-07-buzzacott-uk-tax-report.pdf` | Original adviser doc | 2 |
| `sources/2026-05-07-buzzacott-corporate-residency-review.pdf` | Original adviser doc | 2 |
| `context/entities.md` | Every entity, residency, control, role | 3 |
| `context/money-flow.md` | Pipeline from AIFS profit to UK account | 3 |
| `context/tax-constraints.md` | Binding tax rules with sources; open items tracked elsewhere | 4 |
| `context/advisors.md` | Firms, people, scope | 4 |
| `context/digests/2026-05-07-buzzacott-uk-tax-report.md` | Digest of trust/FIG report | 5 |
| `context/digests/2026-05-07-buzzacott-corporate-residency-review.md` | Digest of AIFS/Moncel residency report | 5 |
| `notes/2026-06-08-owners-meeting-dividends-and-cash-floor.md` | Granola summary | 6 |
| `notes/2026-07-23-q2-financial-review.md` | Granola summary | 6 |
| `decisions/0001-…` to `decisions/0006-…` | Back-filled accepted records | 7 |
| `policy/extraction-policy.md` | Living extraction position | 8 |
| `policy/investment-policy-statement.md` | Living investment position | 8 |
| `CLAUDE.md` | Session instructions + verification checklist | 9 |

---

### Task 1: Repository skeleton and READMEs

**Files:**
- Modify: `README.md` (currently one line)
- Create: `decisions/README.md`, `policy/.gitkeep`, `context/digests/.gitkeep`, `sources/.gitkeep`, `notes/.gitkeep`

**Interfaces:**
- Produces: the record format convention in `decisions/README.md` that Task 7 follows verbatim, and the index table header that Task 7 fills.

- [ ] **Step 1: Write `README.md`**

```markdown
# Investment Function

This repository is the decision record and knowledge base for the personal
investment function operated by Stu Hilditch and Danni Cullen on top of
Moncel. Moncel's objective is to produce profit that transfers to this
function. This repository records how that money leaves Moncel and how it is
invested once it arrives.

It is a knowledge base, not a codebase. Decisions are recorded once and never
edited; the current position is read from the policy documents.

## Start here

1. `policy/extraction-policy.md` — how money leaves Moncel today
2. `policy/investment-policy-statement.md` — how money is invested today
3. `context/tax-constraints.md` — the rules that bind every choice
4. `decisions/README.md` — the index of every decision and the record format

## Layout

| Folder | What lives there | Can it change? |
|---|---|---|
| `decisions/` | Numbered decision records | Frozen once accepted; superseded by new records |
| `policy/` | Living statements of the current position, every clause citing a decision | Updated when a decision is accepted |
| `context/` | Facts: entities, money flow, tax constraints, advisers, advice digests | Updated as facts change |
| `sources/` | Original adviser documents | Never edited |
| `notes/` | Dated informal notes and meeting transcripts | Free-form |
| `docs/superpowers/` | Design specs and implementation plans for this repository | As needed |

## Rules

- A choice is made only in a decision record. Policy and context never make
  choices of their own.
- Policy decisions (anything that changes a policy, moves money out of Moncel,
  or opens an account or entity) require both Stu and Danni as deciders.
- Figures as decided are recorded. Account numbers, identifiers and
  credentials are never recorded.
- Claude assists with drafting and analysis and is not a licensed adviser.
  Tax treatment is checked with Buzzacott (UK) or William Buck (AU).
```

- [ ] **Step 2: Write `decisions/README.md`**

```markdown
# Decisions

One file per decision, `NNNN-short-title.md`, numbered in one sequence across
both domains. A record is created as `proposed`, then becomes `accepted` or
`rejected`. From that point its body is frozen. A change of mind is a new
record that names the old one in `supersedes`; the old record receives
`superseded-by` and status `superseded`. That stamp is the only edit ever made
to a frozen record. When a record is accepted, the matching policy document is
updated in the same commit.

## Index

| No. | Title | Domain | Materiality | Status | Decided |
|---|---|---|---|---|---|

## Record format

Front matter:

```yaml
---
number: 0000
title:
domain:            # extraction | investment | both
materiality:       # operational | policy
status:            # proposed | accepted | rejected | superseded
proposed:          # YYYY-MM-DD
decided:           # YYYY-MM-DD when accepted or rejected
deciders: []       # [Stu] for operational; [Stu, Danni] required for policy
supersedes:        # number, if any
superseded-by:     # number, stamped later if superseded
sources: []        # repo-relative paths under sources/, notes/, context/digests/
---
```

Body sections, in this order:

1. **Context** — what prompted the decision and which constraints bind it.
   Cite `context/tax-constraints.md` and relevant digests. If the record is
   reconstructed from meeting notes rather than a signed document, say so here.
2. **Options considered** — each option with its case for and against.
3. **Decision** — what was chosen, in one paragraph.
4. **Consequences** — what changes in policy, what it costs, what risks are
   accepted, what must be checked with advisers.
5. **Review** — when to revisit, if ever.

Materiality:

- **operational** — within an already-accepted policy. Stu alone may accept.
- **policy** — changes a policy, moves money out of Moncel, or opens a new
  account or entity. Both Stu and Danni must be named in `deciders` before
  status may become `accepted`.
```

- [ ] **Step 3: Create empty folders**

```bash
mkdir -p policy context/digests sources notes
touch policy/.gitkeep context/digests/.gitkeep sources/.gitkeep notes/.gitkeep
```

- [ ] **Step 4: Verify**

```bash
test -f README.md && test -f decisions/README.md && ls -d policy context/digests sources notes
grep -c "Record format" decisions/README.md
```
Expected: the five paths print, and the grep prints `1`.

- [ ] **Step 5: Commit**

```bash
git add README.md decisions policy context sources notes
git commit -m "Scaffold repository layout and decision record convention

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: Copy adviser sources and write provenance table

**Files:**
- Create: `sources/2026-05-07-buzzacott-uk-tax-report.pdf`
- Create: `sources/2026-05-07-buzzacott-corporate-residency-review.pdf`
- Create: `sources/README.md`
- Delete: `sources/.gitkeep`

**Interfaces:**
- Produces: the two source paths above, cited by Tasks 5 and 7.

- [ ] **Step 1: Copy the PDFs**

```bash
cp "/Users/stuarthilditch/Moncel/Inbox/Buzzacott/UK Tax Report - 7 May 2026.pdf" sources/2026-05-07-buzzacott-uk-tax-report.pdf
cp "/Users/stuarthilditch/Moncel/Inbox/Buzzacott/0507 Australian Institute of Food Safety residency advice - draft for client.pdf" sources/2026-05-07-buzzacott-corporate-residency-review.pdf
rm sources/.gitkeep
```

- [ ] **Step 2: Write `sources/README.md`**

```markdown
# Sources

Original adviser documents. Never edited. Each has a digest in
`context/digests/` under the same date and slug.

## Provenance

| File | Date | Author | What it is | Status |
|---|---|---|---|---|
| `2026-05-07-buzzacott-uk-tax-report.pdf` | 2026-05-07 | Buzzacott LLP (Nyah Duffy) | UK tax treatment of the Ellell Trust and GHS Hilditch Trust, and of Stu and Danni as UK residents under the FIG regime | Final |
| `2026-05-07-buzzacott-corporate-residency-review.pdf` | 2026-05-07 | Buzzacott LLP (James Currie) | UK corporate tax residency and permanent establishment review for AIFS and Moncel Australia (RTO) Pty Ltd | Marked DRAFT on every page |

## Known documents not yet copied

Copy only when Stu confirms. Originals are in `~/Moncel/Inbox/LEGAL/` unless
noted.

| Document | Date | Where it is |
|---|---|---|
| Supplemental Deed — GHS Hilditch Trust (fully executed) | 2026-05-08 | `~/Moncel/Inbox/LEGAL/EXECUTED/` |
| Supplemental Deed — Ellell Trust (fully executed) | 2026-05-08 | `~/Moncel/Inbox/LEGAL/EXECUTED/` |
| Single Director's Declarations, both trustee resolutions (fully executed) | 2026-05-08 | `~/Moncel/Inbox/LEGAL/EXECUTED/` |
| Australia Director Agreement — GHS Hilditch Mgmt (fully executed) | 2026-05-08 | `~/Moncel/Inbox/LEGAL/EXECUTED/` |
| Deed of Indemnity (fully executed) | 2026-05-08 | `~/Moncel/Inbox/LEGAL/EXECUTED/` |
| Acquisition of Company — GHS Ellell Management Pty Ltd (parts 1 and 2, signed) | 2026-05 | `~/Moncel/Inbox/LEGAL/EXECUTED/` |
| Australia Director Agreement — AIFS (Andrew Phillips, completed via DocuSign) | 2026-06-05 | Gmail, DocuSign completion email |
| ASIC Form 484s — AIFS director changes (completed) | 2026-06-03 | Gmail, Adobe Sign completion email |
| 2026 Trust Distribution Resolutions, both trusts (signed by Andrew Phillips) | 2026-06-11 | Gmail, William Buck thread |
| Dividend statement and minutes template (William Buck / Russell Kennedy) | 2026-06-10 | Gmail, William Buck thread |
| Danni's investment proposal | forthcoming | To be provided |
```

- [ ] **Step 3: Verify**

```bash
ls -la sources/
test -f sources/2026-05-07-buzzacott-uk-tax-report.pdf && test -f sources/2026-05-07-buzzacott-corporate-residency-review.pdf && echo OK
```
Expected: two PDFs of roughly 258 KB and 323 KB, `README.md`, no `.gitkeep`, and `OK`.

- [ ] **Step 4: Commit**

```bash
git add sources
git commit -m "Add Buzzacott source documents and provenance table

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 3: Context — entities and money flow

**Files:**
- Create: `context/entities.md`
- Create: `context/money-flow.md`

**Interfaces:**
- Produces: entity names used consistently by Tasks 4 to 8: "GHS Hilditch Trust", "Ellell Trust", "GHS Ellell Management Pty Ltd", "AIFS", "Moncel RTO", "CIFS", "Userve", "AIFS Foundation", "Moncel Limited UK".

- [ ] **Step 1: Write `context/entities.md`**

```markdown
# Entities

Facts about each entity in the structure as understood on 2026-09-03. Update
as facts change. Items marked **confirm** are reconstructed from notes and
correspondence and should be checked against the registers.

## Ownership diagram

```
GHS Hilditch Trust (50%) ──┐          ┌── Ellell Trust (50%)
  trustee: GHS Ellell      │          │     trustee: GHS Ellell
  Management Pty Ltd       │          │     Management Pty Ltd
                           ▼          ▼
            Australian Institute of Food Safety Pty Ltd (AIFS, Australia)
                    │                              │
                    ▼                              ▼
   Canadian Institute of Food Safety Ltd     Userve Inc (US)
              (CIFS, Canada)

GHS Hilditch Trust (50%) + Ellell Trust (50%) ── Moncel Australia (RTO) Pty Ltd
Stu (50%) + Danni (50%), personally ─────────── Moncel Limited (UK)
Separate: Australian Institute of Food Safety Foundation (charity)
```

## Trusts

### GHS Hilditch Trust
- Queensland discretionary trust created 2010-11-10. Named settlor Daniel John
  Hillier with a notional AUD 10; Stu subsequently settled his 50% of AIFS and
  50% of Moncel RTO into it. Treated as settled by Stu for UK purposes.
- Trustee: GHS Ellell Management Pty Ltd (Australian company, sole director
  Andrew Phillips, NSW resident) since the supplemental deed of 2026-05-08.
  Stu was sole trustee before that.
- Principal (power to remove and appoint the trustee): Stu. Alternative
  Principal: Danni.
- Primary beneficiaries Stu and Danni; wide secondary and tertiary classes.
- UK treatment: non-UK resident, substantive (not bare), settlor-interested,
  excluded property for IHT while Stu is not a long-term UK resident.

### Ellell Trust
- Identical terms and dates to the GHS Hilditch Trust. Danni settled her 50%
  of AIFS and 50% of Moncel RTO. Treated as settled by Danni.
- Trustee: GHS Ellell Management Pty Ltd since 2026-05-08. Danni was sole
  trustee before that.
- Principal: Danni. Alternative Principal: Stu.
- UK treatment as for the GHS Hilditch Trust, taxed on Danni.

### GHS Ellell Management Pty Ltd (corporate trustee)
- Australian proprietary company acquired in 2026-05 to act as trustee of both
  trusts. **Confirm** ACN and that a single company acts for both trusts; the
  2026-05-06 plan named two companies (GHS Hilditch Management Pty Ltd and
  Ellell Management Pty Ltd), later correspondence names one.
- Sole director: Andrew Phillips, engaged as a nominee director through Sarah
  Guy Pty Ltd. Shareholders: Stu and Danni, 100%.
- Engagement terms (from the 2026-05-06 review): nominee only, up to two
  director meetings per year, express written owner approval before acting
  beyond Corporations Act requirements, 30 days' termination either way.
- Held its first trustee meeting on 2026-06-11 and signed the 2026 trust
  distribution resolutions the same day.

## Operating companies

### Australian Institute of Food Safety Pty Ltd (AIFS)
- Australian trading company, the group's primary commercial entity and the
  source of profit. Owned 50/50 by the two trusts via the corporate trustee.
- Directors since 2026-06: Andrew Phillips (Chair, sole attending director)
  and Rodney Hilditch (Stu's father, Australian resident, co-signs, does not
  attend). Stu and Danni resigned; ASIC Form 484s completed 2026-06-03. Drew
  Robertson (VP Finance & Operations, Toronto) is company secretary, not a
  director. Quarterly board meetings held outside the UK.
- Net profit AUD 233,819 for FY ending 2025-06-30; AUD 500,728 for the nine
  months to 2026-03-31 (Buzzacott corporate residency review, 1.4).
- Pays franked dividends to the trusts.
- Subsidiaries: CIFS (Canada), Userve Inc (US).

### Moncel Australia (RTO) Pty Ltd (Moncel RTO)
- Australian registered training organisation. Non-commercial: no income, no
  expenditure, issues certifications only. Owned 50/50 by the two trusts.
- Directors: Stu, Danni, Rodney Hilditch (per 2022 ASIC review; **confirm**).
- Must remain dormant. Buzzacott (2026-05-19) confirmed Stu and Danni may stay
  as directors only while it is inactive; any activity would need decisions
  taken physically outside the UK. Open question whether its compliance
  services to AIFS undermine dormancy (Buzzacott written analysis requested
  2026-05-19; outcome **confirm**).

### Canadian Institute of Food Safety Limited (CIFS)
- Canadian subsidiary of AIFS. Pays dividends to AIFS.
- Directors: Stu and Danni (**confirm**). On 2026-08-06 Stu and Drew agreed to
  replace them with Rodney Hilditch, to be filed effective 2026-08-24 (the AGM
  date) or backdated to the start of the UK tax year. Drew owns this.
- Candidate contracting counterparty for Moncel Limited UK's services
  agreement (preferred over AIFS at the 2026-05-19 Buzzacott meeting).

### Userve Inc
- US subsidiary of AIFS, operating in the USA. Pays dividends to AIFS.
- Not addressed in either Buzzacott report. Potential indirect US tax
  exposure (Subpart F, GILTI) flagged in the 2026-05 restructuring notes but
  not yet advised on.

### Australian Institute of Food Safety Foundation
- Australian registered charity, ~AUD 17,000 revenue FY2023, donates to
  OzHarvest. Not dormant.
- Directors: Stu, Danni, Daniel Hillier (ACNC 2023 return; **confirm**).
- Buzzacott advised the same principles as for AIFS apply; tailored advice on
  board makeup outstanding.

### Moncel Limited (UK)
- UK private company incorporated 2026-05-28 via Buzzacott, who provide the
  registered office. Year-end 30 June. Xero for accounts.
- Owned 50/50 by Stu and Danni personally, outside the trust group, so that the
  trusts hold no UK property. Class A / Class B shares for dividend
  flexibility. Dividends preferred over salary.
- Purpose: to carry out Stu and Danni's UK work for the group and charge an
  arm's-length management fee, ring-fencing any UK permanent establishment.
  Charging roughly AUD 17,000 per month as at 2026-07 (Q2 financial review).
  Also funds Australia travel (~AUD 50,000 per year).
- Services agreement counterparty (CIFS or AIFS): **confirm** what was
  executed.

## People

- **Stu Hilditch** — CEO of Moncel; UK resident from 2026-05-11 (tax year
  2026/27); Principal of the GHS Hilditch Trust; 50% of GHS Ellell Management
  Pty Ltd and of Moncel Limited UK.
- **Danni Cullen** — President of Moncel; UK resident from 2026-05-11;
  Principal of the Ellell Trust; 50% of GHS Ellell Management Pty Ltd and of
  Moncel Limited UK.
- **Andrew Phillips** — Australian-resident nominee director: sole director of
  GHS Ellell Management Pty Ltd; Chair of AIFS. Fee AUD 12,000 per year for the
  AIFS role (amended 2026-05-27).
- **Rodney Hilditch** — Stu's father, Australian resident; director of AIFS
  and Moncel RTO; intended CIFS director.
- **Drew Robertson** — Moncel VP Finance & Operations, Toronto; AIFS company
  secretary; runs board logistics and payments.
```

- [ ] **Step 2: Write `context/money-flow.md`**

```markdown
# Money flow

The pipeline from AIFS profit to an investable balance in the UK, as operated
on 2026-09-03. At each step: who decides, which entity acts, where tax
attaches. Figures are those decided in the cited records, not live balances.

## Main pipeline

| Step | What happens | Who decides | Who acts | Tax attaches |
|---|---|---|---|---|
| 1 | AIFS earns operating profit across AU, CA and US brands; CIFS and Userve pay dividends up to AIFS | AIFS board (Andrew, Rod) with management | AIFS, CIFS, Userve | Australian company tax on AIFS; Canadian and US tax on subsidiaries |
| 2 | AIFS provisions 25% for tax and 12% for the employee bonus pool; 66% of the remainder is available for dividends; AIFS holds cash to a floor before paying anything beyond the regular dividend | Owners set the formula and floor [D-0003, D-0004]; AIFS board resolves each dividend | AIFS | None additional |
| 3 | AIFS pays franked dividends 50/50 to the two trusts via the corporate trustee | AIFS board | AIFS → GHS Ellell Management Pty Ltd as trustee | Australian franking credits attach; not creditable in the UK |
| 4 | The corporate trustee resolves to distribute trust income to Stu (GHS) and Danni (Ellell) | Trustee (Andrew) on owner request; annual distribution resolution by 30 June | GHS Ellell Management Pty Ltd | Both trusts are settlor-interested, so income is treated as Stu's and Danni's as it arises whether or not distributed. Outside UK tax if a FIG claim is made for that year; otherwise UK dividend rates up to 39.35% with no credit for franking |
| 5 | Distributions are paid to Stu and Danni's Australian Wise accounts, then transferred to UK accounts | Owners | Trustee instructs payment; Drew executes via Airwallex to Wise | Transfers over reporting thresholds are flagged by banks; William Buck supplied dividend statement and minutes templates (2026-06-10) so each payment is documented |
| 6 | Cash sits in UK personal accounts pending investment decisions | Owners | Stu, Danni | UK-situs cash is inside the UK IHT net; interest is UK-source income |

## Side flow: Moncel Limited UK

| Step | What happens | Who decides | Tax attaches |
|---|---|---|---|
| A | Moncel Limited UK invoices the group (CIFS or AIFS) an arm's-length management fee for Stu and Danni's UK work, roughly AUD 17,000 per month as at 2026-07 [D-0002] | Owners as directors of Moncel Limited UK | UK corporation tax on Moncel Limited UK's profit; the fee is a deductible cost in the paying entity |
| B | Moncel Limited UK pays dividends to Stu and Danni via Class A / Class B shares in preference to salary | Owners | UK dividend tax on Stu and Danni; this is UK-source income and is not covered by FIG |

## One-off flows recorded to date

- 2026-06: proceeds of the Canadian car sale to be split 50/50 into the
  Australian Wise accounts after tax implications were calculated; an invoice
  from Moncel Limited UK was raised for the international transfer (owners
  meeting 2026-06-08).
- Q2 2026: additional dividends of AUD 147,900 were paid, the main driver of
  the income reduction versus Q1 (Q2 financial review 2026-07-23).

## Where the investment function begins

The investment domain starts at step 6. Everything before it is the
extraction domain. Any investment vehicle sits outside the UK and outside the
trusts [D-0005]; the choice of vehicle, jurisdiction and currency is not yet
made (see `policy/investment-policy-statement.md`).
```

- [ ] **Step 3: Verify**

```bash
grep -c "confirm" context/entities.md
grep -o "D-000[0-9]" context/money-flow.md | sort -u
```
Expected: the first grep prints a number ≥ 5; the second prints `D-0002`, `D-0003`, `D-0004`, `D-0005` (Task 7 creates these records).

- [ ] **Step 4: Commit**

```bash
git add context/entities.md context/money-flow.md
git commit -m "Add entity map and money-flow context

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 4: Context — tax constraints and advisers

**Files:**
- Create: `context/tax-constraints.md`
- Create: `context/advisors.md`

**Interfaces:**
- Produces: constraint identifiers `C1` to `C12` cited by decision records in Task 7 and by the investment policy in Task 8.

- [ ] **Step 1: Write `context/tax-constraints.md`**

```markdown
# Tax constraints

Rules that bind extraction and investment choices, each stated as a
constraint with its source. These are facts about the rules as advised, not
decisions. Anything marked *advice needed* is a question for Buzzacott (UK) or
William Buck (AU), not something to be settled here.

Sources: `context/digests/2026-05-07-buzzacott-uk-tax-report.md` (trusts and
FIG) and `context/digests/2026-05-07-buzzacott-corporate-residency-review.md`
(company residency and permanent establishment).

## Residency facts the constraints rest on

- Stu and Danni became UK resident on 2026-05-11, in UK tax year 2026/27.
  Neither had been UK resident in any of the previous 10 tax years.
- Both intend to leave before completing four UK tax years. All Buzzacott
  advice assumes this; if it changes, fresh advice is required.

## Constraints

**C1 — FIG window.** Both Stu and Danni may claim the 4-year Foreign Income
and Gains regime for tax years 2026/27 to 2029/30 inclusive. Under a valid
claim, foreign income and gains realised in that year, including trust income
and gains attributed to them and distributions from the trusts, are outside UK
tax. The claim is made per person, per year, on the Self Assessment return
(first return for 2026/27 due 2028-01-31; FIG claim hard deadline
2029-01-31). Skipping a year does not extend the window.

**C2 — Cost of a FIG claim.** In any year a FIG claim is made, that person
loses the UK personal allowance and the CGT annual exempt amount, and cannot
claim foreign income or capital losses for that year. Whether to claim each
year is a decision, not automatic. *Advice needed* each year before filing.

**C3 — Settlor-interested trusts.** Both trusts are settlor-interested. Trust
income and gains are taxed on the settlor (GHS on Stu, Ellell on Danni) as
they arise while UK resident, whether or not distributed, unless covered by a
FIG claim. Australian franking credits are not creditable in the UK; without
FIG the net dividend is taxed at UK dividend rates (top rate 39.35%).

**C4 — Motive defence and the 2012 boundary.** Buzzacott expect the motive
defence to the Transfer of Assets Abroad rules to apply, so income and gains
inside AIFS are not attributed to the trusts or settlors until distributed or
realised. The defence for gains applies only from 2012-04-06; gains in the
underlying companies before that date sit in the trusts' stockpiled gains
pool. Distributions made under a FIG claim do not wash out the stockpiled
gains or offshore income gains pools; they carry forward to match later
capital distributions to UK residents. A one-page file note from William Buck
on the 2010 trust purpose supports the defence (requested 2026-05, status
unknown).

**C5 — Offshore income gains.** Gains on non-reporting offshore funds
(most ETFs, mutual funds and money market funds not set up for UK investors)
are offshore income gains taxed as income, not capital gains, and are matched
to capital distributions ahead of ordinary gains. Any fund held personally or
via a vehicle while UK resident should either have HMRC reporting-fund status
or be covered by a FIG claim for the year of realisation. *Advice needed* on
fund selection before the first purchase.

**C6 — Inheritance tax and situs.** While neither is a long-term UK resident,
only UK-situs assets are within UK IHT. Cash in UK bank accounts, UK
property, and UK-listed holdings held directly are UK-situs. Foreign-situs
assets are outside. Both trusts are excluded property trusts on the same
basis and must not hold UK property or derive value from UK residential
property.

**C7 — Long-term residence threshold.** UK residence in 10 of the previous 20
tax years makes a person a long-term resident: worldwide assets enter UK IHT,
and trusts they settled enter the relevant property regime (10-year and exit
charges up to 6%). Planning assumes departure well before this.

**C8 — Trust residence.** The trusts stay non-UK resident only while the sole
trustee is non-UK resident. Stu and Danni retain Principal powers to remove
and appoint the trustee; whether exercising that power from the UK is itself a
central management and control act is an open question raised 2026-05-06.
*Advice needed* before any exercise of Principal powers from the UK.

**C9 — No additions to the trusts.** Buzzacott's advice assumes no assets are
added to either trust while Stu and Danni are UK resident. Adding assets
would require fresh advice. Any investment vehicle sits outside the trusts
[D-0005].

**C10 — Company residence and permanent establishment.** AIFS remains
Australian resident only while strategic decisions are made by its
Australian-resident board outside the UK and Stu and Danni do not exercise
shadow control. Moncel RTO must remain dormant while Stu and Danni are its
directors. Stu and Danni's UK work creates a UK permanent establishment risk
for AIFS, which Moncel Limited UK exists to ring-fence [D-0002]. Contracts
for the group are not concluded from UK soil except through Moncel Limited UK.

**C11 — Trust Registration Service.** The trusts must register with HMRC
within 90 days if they become liable to UK tax on UK income or assets, acquire
UK land or property, or gain a UK-resident trustee and enter a UK business
relationship. Any UK-touching activity at trust level triggers a check.

**C12 — Investment vehicle location.** Buzzacott's in-principle position
(2026-05-19): set up any investment vehicle outside the UK; do not place it
inside the trusts without specific advice; consult Buzzacott before
incorporating anything [D-0005].

## Open items tracked elsewhere

Not this repository's job, but they touch the tax position:

- ATO notice "You have an overdue tax debt" for Stu, forwarded by William
  Buck on 2026-08-17. Owner: Stu with William Buck.
- CIFS director change from Stu and Danni to Rodney Hilditch, to be filed
  effective 2026-08-24 or backdated. Owner: Drew.
- Buzzacott written analyses requested 2026-05-19 and not seen here: Moncel
  RTO's indirect relationship with AIFS; contracting counterparty for Moncel
  Limited UK.
- Userve Inc US tax position with UK-resident beneficiaries: not yet advised.
- D&O insurance for the corporate trustee and operating entities: open since
  2026-05.
```

- [ ] **Step 2: Write `context/advisors.md`**

```markdown
# Advisers

Who advises on what. Contact details are business emails already in Stu's
correspondence; no account or engagement numbers are recorded here.

## Buzzacott LLP (UK) — UK personal and corporate tax

- **Nyah Duffy**, Partner — author of the UK Tax Report on the trusts and FIG
  (2026-05-07). Lead on trust and FIG matters.
- **James Currie**, Corporate team — author of the UK corporate tax residency
  review for AIFS and Moncel RTO (2026-05-07). Lead on company residency,
  permanent establishment, Moncel Limited UK.
- **Cameron Hallhit** — answered 13 pre-meeting questions and attended the
  2026-05-19 meeting.
- **Daniel Iles** — copied on FIG correspondence.
- Engagement: letters dated 2026-04-24 for both reports. Incorporation and
  registered office for Moncel Limited UK (GBP 1,400 incorporation, GBP 600
  per year registered office), ongoing accounts and UK tax returns. Also to
  handle UK Self Assessment registration and the FIG claims.
- Standing instruction from Buzzacott: consult before incorporating any
  investment vehicle [D-0005].

## William Buck (NSW, Australia) — Australian tax, trusts, ASIC

- **Karly Whitehead**, Senior Manager — lead adviser. Coordinated the
  corporate trustee setup, Andrew Phillips's engagement, ASIC Form 484s,
  annual trust distribution resolutions, dividend documentation templates.
- **Tim Lyford** — consulted on treatment of 2025/26 amounts.
- **Lucy Schuster**, **Jack Qi** — copied on correspondence.
- Also forwards ATO correspondence for Stu personally.

## Andrew Phillips — Australian-resident nominee director

- Engaged through Sarah Guy Pty Ltd. Sole director of GHS Ellell Management
  Pty Ltd (the corporate trustee); Chair and sole attending director of AIFS
  from 2026-06. AIFS fee AUD 12,000 per year (amended 2026-05-27).
- Signs trustee resolutions, including the annual distribution resolutions
  and any resolution to distribute to Stu and Danni.

## Russell Kennedy (Sydney) — Australian legal

- **Kate Littlewood** drafted the supplemental deeds, director agreements and
  deeds of indemnity (2026-05). **Danielle Styner** handled invoicing.
- On 2026-07-14 Stu instructed Drew that the firm is not to be used again
  (cost and repeated errors). A replacement Australian lawyer is needed for
  the deferred AIFS shareholders' deed and any future deed work.

## Thor.ca (Canada) — Canadian departure

- Consulted 2026-04-10 on Canadian tax residency on departure. No ongoing
  engagement recorded.
```

- [ ] **Step 3: Verify**

```bash
grep -c "^\*\*C[0-9]*" context/tax-constraints.md
grep -c "Advice needed\|advice needed" context/tax-constraints.md
grep -n "Russell Kennedy" context/advisors.md | head -1
```
Expected: `12`, a number ≥ 3, and one matching line.

- [ ] **Step 4: Commit**

```bash
git add context/tax-constraints.md context/advisors.md
git commit -m "Add tax constraints and adviser context

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 5: Advice digests

**Files:**
- Create: `context/digests/2026-05-07-buzzacott-uk-tax-report.md`
- Create: `context/digests/2026-05-07-buzzacott-corporate-residency-review.md`
- Delete: `context/digests/.gitkeep`

**Interfaces:**
- Consumes: the two PDFs in `sources/` (Task 2). Read them with the Read tool, pages 1-7 and 8-14 for the first, 1-7 and 8-13 for the second, to check the content below before writing.
- Produces: digest paths cited in `sources` front matter by Task 7.

- [ ] **Step 1: Write the trust and FIG digest**

```markdown
# Digest — Buzzacott UK Tax Report, 2026-05-07

**Source:** `sources/2026-05-07-buzzacott-uk-tax-report.pdf`
**Author:** Buzzacott LLP (Nyah Duffy), for Stu and Danni as trustees of the
GHS Hilditch Trust and Ellell Trust. Final report under engagement letters of
2026-04-24.

## Summary

Both trusts are substantive (not bare) trusts and are settlor-interested:
GHS on Stu, Ellell on Danni. They remain non-UK resident provided a non-UK
resident corporate trustee is appointed before Stu and Danni arrive. Trust
income and gains are taxed on the respective settlor as they arise while UK
resident, but both settlors qualify for the 4-year FIG regime for 2026/27 to
2029/30, under which foreign income and gains, including those attributed
from the trusts and distributions received, are outside UK tax. Gains and
offshore income gains realised at trust level during FIG years go into the
stockpiled gains and OIG pools and are matched to future capital
distributions to UK residents. Both trusts are excluded property for IHT
while the settlors are not long-term UK residents.

## Assumptions the advice relies on

- The 2010-11-10 deeds are current with no amendments (the 2026-05-08
  supplemental deeds post-date the report and change the trustee only).
- Daniel John Hillier's AUD 10 settlement was notional; Stu and Danni are the
  real settlors.
- All companies held by the trusts are non-UK resident (separate advice).
- Neither Stu nor Danni was UK resident or domiciled at settlement, nor UK
  resident in the last 20 tax years.
- No assets will be added to either trust while Stu and Danni are UK
  resident.
- All pre-arrival trust income was distributed before UK residency, so no
  pre-arrival income pool exists.
- Stu and Danni will not stay beyond four UK tax years.

## Constraints it imposes

- FIG claims are per person, per year, on Self Assessment; a year not claimed
  is taxed under normal rules; claiming forfeits the personal allowance and
  CGT exempt amount and blocks foreign loss claims.
- Franking credits on AIFS dividends are not creditable in the UK; without
  FIG, net dividends are taxed at up to 39.35%.
- Distributions under FIG do not wash out the stockpiled gains or OIG pools.
  Pre-2012-04-06 gains in the underlying companies sit in the stockpiled pool.
- Non-reporting offshore funds generate offshore income gains taxed as income.
- The trusts must not hold UK-situs assets or derive value from UK
  residential property.
- TRS registration is triggered by UK tax liability, UK land, or a UK
  trustee plus UK business relationship, within 90 days.
- If either becomes a long-term UK resident (10 of 20 years), worldwide
  assets and the trusts enter UK IHT, with an exit charge when leaving.

## Open questions

- Whether exercising Principal powers from the UK is a central management and
  control act (raised 2026-05-06, not addressed in the report).
- Whether the motive defence can be evidenced now for later HMRC challenge
  (William Buck file note requested).
- The report does not address Userve Inc or CIFS beyond noting they pay
  dividends to AIFS.
```

- [ ] **Step 2: Write the corporate residency digest**

```markdown
# Digest — Buzzacott UK corporate tax residency review, 2026-05-07

**Source:** `sources/2026-05-07-buzzacott-corporate-residency-review.pdf`
**Author:** Buzzacott LLP (James Currie), for Australian Institute of Food
Safety Pty Ltd. Marked DRAFT on every page; treated as the operative advice
since no final was received.

## Summary

UK company residence turns on incorporation or central management and
control (CMC). AIFS is Australian-incorporated and, once Stu and Danni resign
and the board is wholly Australian-resident with meetings outside the UK,
should remain Australian resident, provided the board exercises genuine
independent judgement and Stu and Danni confine themselves to operational
matters while in the UK. Residual risk is medium because the ultimate owners
are UK resident. Moncel RTO, with Stu and Danni as sole directors, is at high
risk of UK residence if it ever trades, but has no consequences while dormant.
Stu and Danni's UK activity will almost certainly create a UK permanent
establishment for AIFS under the agency test. Buzzacott recommend a UK company
owned 50/50 by Stu and Danni, outside the trust group, to carry out UK
activities and charge AIFS an arm's-length management fee.

## Assumptions the advice relies on

- Stu and Danni resign as AIFS directors; Andrew Phillips is appointed
  alongside Rodney Hilditch.
- Quarterly board meetings take place in Australia with Stu and Danni
  physically outside the UK if attending remotely.
- Moncel RTO has no income, expenditure or trading.
- The group is below the transfer-pricing documentation thresholds (fewer
  than 250 employees and either under EUR 50m turnover or EUR 43m assets), so
  no formal transfer-pricing study is needed, though pricing must still be at
  arm's length.

## Constraints it imposes

- Board decisions for AIFS are made by Andrew and Rod; minutes must show
  challenge and independent reasoning; documents are held at the registered
  office in Australia and signed by Andrew or Rod.
- Stu and Danni do not rejoin the AIFS board, do not attend board meetings,
  and do not dominate key decisions, especially while physically in the UK.
- Only preparatory or auxiliary activity for AIFS happens in the UK; any
  negotiation or conclusion of contracts is done by non-UK personnel or
  routed through the UK company.
- The UK company must sit outside the trusts so the trusts hold no UK
  property (which would jeopardise FIG treatment of distributions).
- If a UK PE nonetheless exists, AIFS must register with Companies House and
  HMRC within three months, file accounts, and potentially register for VAT
  and payroll.

## Open questions

- Whether Moncel RTO's compliance services to AIFS undermine its dormancy
  (written analysis requested 2026-05-19).
- Which entity Moncel Limited UK should contract with (CIFS preferred at the
  2026-05-19 meeting; written analysis requested).
- CIFS and Userve residency with UK-resident owners is not covered.
```

- [ ] **Step 3: Remove the placeholder and verify**

```bash
rm context/digests/.gitkeep
ls context/digests/
grep -c "^## " context/digests/2026-05-07-buzzacott-uk-tax-report.md
grep -c "^## " context/digests/2026-05-07-buzzacott-corporate-residency-review.md
```
Expected: two `.md` files listed; both greps print `4`.

- [ ] **Step 4: Commit**

```bash
git add context/digests
git commit -m "Add digests of the two Buzzacott reports

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 6: Seed notes from Granola

**Files:**
- Create: `notes/2026-06-08-owners-meeting-dividends-and-cash-floor.md`
- Create: `notes/2026-07-23-q2-financial-review.md`
- Delete: `notes/.gitkeep`

**Interfaces:**
- Produces: note paths cited in `sources` front matter by decisions 0003 and 0004 (Task 7).

- [ ] **Step 1: Write the owners meeting note**

```markdown
# Owners meeting — dividends and cash floor

**Date:** 2026-06-08
**Attendees:** Stu Hilditch, Danni Cullen, Drew Robertson
**Source:** Granola summary retrieved 2026-09-03. Not a verbatim transcript.
**Fed decisions:** D-0003, D-0004

## Dividends and distributions

- Regular dividends increased from AUD 33,000 to AUD 50,000 per month from
  June 2026 (one month of impact in Q2).
- Dividend formula discussed: 66% of remaining profit after a 12% employee
  bonus provision and a 25% tax provision.
- Non-regular dividends above AUD 50,000 are excluded from SLT bonus
  calculations.
- Canadian car sale proceeds: calculate tax implications first, then
  distribute 50/50 to the Australian Wise accounts. Drew to raise an invoice
  from Moncel Limited UK for the international transfer.

## Where surplus profit should sit

- Philosophy agreed: money retained in the business remains owner money; cash
  on the balance sheet is an owner asset.
- Counter-argument noted: roughly 4% in high-yield savings versus 8 to 9%
  expected from external investments, plus diversification.
- Decision: retain in the business for now. Minimum cash target of AUD 1.3M.
  Runway basis: two months of PPC spend (~AUD 482,000) plus four months of
  general expenses (~AUD 410,000) plus a December loss cushion.
- Position at the time: ~AUD 940,000. Target date: November 2026.
- Owner bonuses and distributions beyond the regular dividend suspended until
  the target is reached; likely no extra distributions until Q1 2027.
- Drew committed to cost control; investment spend requires documented ROI.

## Related items from the same fortnight

- 2026-06-04: dividend payments blocked pending William Buck paperwork for
  the UK transfer; risk of funds stuck in transit without documentation. Drew
  to set up monthly payments from Airwallex to Wise. Stu's ANZ access limited
  to balance checking; Drew handles payment setup.
```

- [ ] **Step 2: Write the Q2 review note**

```markdown
# Q2 2026 financial review

**Date:** 2026-07-23
**Attendees:** Stu Hilditch, Danni Cullen, Drew Robertson
**Source:** Granola summary retrieved 2026-09-03. Not a verbatim transcript.
**Fed decisions:** none directly; evidence for the effect of D-0002 and D-0003

## Points relevant to extraction

- Moncel Limited UK fees of AUD 17,000 per month are now a recurring cost,
  flowing as contractor payments.
- Q2 included a one-off double-payment month (rent overlap plus Moncel UK)
  that will not repeat in Q3.
- Moncel UK payments count as a cost in SLT performance bonus calculations.
- Australia travel (~AUD 50,000 per year) is now funded by Moncel Limited UK
  and no longer hits Moncel Canada.
- Additional dividends of AUD 147,900 in Q2 were the primary driver of the
  income reduction versus Q1. The dividend increase adds AUD 17,000 per month
  to the ongoing cost base.
```

- [ ] **Step 3: Remove the placeholder and verify**

```bash
rm notes/.gitkeep
ls notes/
grep -l "D-0003" notes/*.md
```
Expected: two `.md` files listed; both files match.

- [ ] **Step 4: Commit**

```bash
git add notes
git commit -m "Seed notes from June owners meeting and Q2 financial review

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 7: Back-filled decision records and index

**Files:**
- Create: `decisions/0001-corporate-trustee-before-uk-residency.md`
- Create: `decisions/0002-moncel-limited-uk.md`
- Create: `decisions/0003-regular-dividend-aud-50k-monthly.md`
- Create: `decisions/0004-aifs-cash-floor-aud-1-3m.md`
- Create: `decisions/0005-investment-vehicle-outside-uk-and-trusts.md`
- Create: `decisions/0006-adopt-decision-repository.md`
- Modify: `decisions/README.md` (fill the index table)

**Interfaces:**
- Consumes: constraint ids C1 to C12 (Task 4); source and note paths (Tasks 2, 5, 6).
- Produces: record numbers D-0001 to D-0006 cited by Task 8.

- [ ] **Step 1: Write `decisions/0001-corporate-trustee-before-uk-residency.md`**

```markdown
---
number: 0001
title: Appoint an Australian corporate trustee to both trusts before UK residency
domain: extraction
materiality: policy
status: accepted
proposed: 2026-04-28
decided: 2026-05-08
deciders: [Stu, Danni]
supersedes:
superseded-by:
sources:
  - context/digests/2026-05-07-buzzacott-uk-tax-report.md
  - sources/2026-05-07-buzzacott-uk-tax-report.pdf
---

## Context

Back-filled on 2026-09-03 from the Buzzacott UK Tax Report, the 2026-05-06
plain-English review of the Russell Kennedy documents, and the executed deeds
dated 2026-05-08. The executed deeds are not yet copied into this repository
(see `sources/README.md`).

Until May 2026 Stu was sole trustee of the GHS Hilditch Trust and Danni sole
trustee of the Ellell Trust. A trust's UK residence follows its trustees. Once
Stu and Danni became UK resident on 2026-05-11, both trusts would have become
UK resident, ending FIG treatment of trust income and gains and bringing the
trusts into UK tax generally (constraints C1, C3, C8 in
`context/tax-constraints.md`). Buzzacott confirmed on 2026-04-28 that a
corporate trustee structure works for FIG provided its directors do not make
key decisions while UK resident.

## Options considered

1. **Do nothing; remain personal trustees.** Simplest, but collapses FIG
   protection on the trusts and exposes trust income to UK tax at up to
   39.35% with no franking credit relief.
2. **Appoint an independent professional trustee company.** Removes Stu and
   Danni from trusteeship entirely, but hands control of the AIFS shares to a
   third party with no owner shareholding in the trustee.
3. **Appoint an owner-controlled Australian corporate trustee with an
   Australian-resident nominee sole director.** Moves central management and
   control to Australia while Stu and Danni keep two levers: 100% of the
   trustee company's shares, and their Principal powers under the deeds to
   remove and replace the trustee. Costs a nominee director fee and legal
   work.

## Decision

Appoint an Australian proprietary company, GHS Ellell Management Pty Ltd,
wholly owned by Stu and Danni and with Andrew Phillips as sole director, as
trustee of both trusts by supplemental deeds executed 2026-05-08, before the
2026-05-11 UK arrival. Stu remains Principal of the GHS Hilditch Trust and
Danni of the Ellell Trust; each becomes Alternative Principal of the other's
trust.

## Consequences

- Both trusts remain non-UK resident. Trust income and gains stay within FIG
  scope for 2026/27 to 2029/30.
- Every trust action, including the resolution to distribute income to Stu
  and Danni, now requires Andrew Phillips to resolve as director of the
  trustee. Owners request; the trustee decides and minutes.
- Nominee director fees (AIFS role AUD 12,000 per year; trustee role per the
  separate engagement letter) and the initial legal cost are accepted.
- Accepted risks: Andrew has full statutory powers constrained only by his
  engagement letter; an AIFS shareholders' deed was deferred and remains
  outstanding; exercising Principal powers from the UK is an unresolved CMC
  question (C8).
- No assets may be added to either trust while UK resident (C9).

## Review

Revisit if Stu or Danni intend to stay in the UK beyond four tax years, if the
nominee director arrangement ends, or if Buzzacott's view on Principal powers
changes.
```

- [ ] **Step 2: Write `decisions/0002-moncel-limited-uk.md`**

```markdown
---
number: 0002
title: Incorporate Moncel Limited UK, owned 50/50 outside the trusts, to bill UK work
domain: extraction
materiality: policy
status: accepted
proposed: 2026-05-07
decided: 2026-05-19
deciders: [Stu, Danni]
supersedes:
superseded-by:
sources:
  - context/digests/2026-05-07-buzzacott-corporate-residency-review.md
  - sources/2026-05-07-buzzacott-corporate-residency-review.pdf
  - notes/2026-07-23-q2-financial-review.md
---

## Context

Back-filled on 2026-09-03 from the Buzzacott corporate residency review and
the 2026-05-19 Buzzacott meeting as recorded in the UK Restructuring Phase 2
task notes. The company was registered on 2026-05-28.

Stu and Danni continue to work for the group from the UK. Buzzacott advised
that this work would almost certainly create a UK permanent establishment for
AIFS under the agency test, exposing AIFS profits to UK corporation tax,
Companies House filing, and potentially VAT and payroll (C10). They
recommended ring-fencing UK activity in a UK company outside the trust group
so the trusts hold no UK property (C6, C9).

## Options considered

1. **Accept a UK permanent establishment of AIFS.** No new entity, but UK
   corporation tax on attributable profit, UK filing of AIFS's worldwide
   accounts, and an untidy interaction with FIG.
2. **Employ Stu and Danni directly from AIFS or CIFS under UK payroll.**
   Avoids a new company but still concludes contracts from the UK, so the PE
   risk remains, and UK employment income is fully taxable.
3. **Incorporate a UK service company owned personally 50/50, outside the
   trusts, charging an arm's-length management fee.** Contains the PE inside
   an entity built for it, keeps the trusts free of UK property, and allows
   profit extraction by dividend with flexibility via share classes.

## Decision

Incorporate Moncel Limited (UK) through Buzzacott, owned 50/50 by Stu and
Danni personally with Class A and Class B shares, year-end 30 June, Xero for
accounts, Buzzacott as registered office. Moncel Limited UK provides Stu and
Danni's services to the group under a formal arm's-length services agreement
and is paid a management fee; owners are remunerated by dividend rather than
salary.

## Consequences

- A second extraction channel exists alongside trust distributions: Moncel
  Limited UK profit paid out as UK dividends. This is UK-source income, fully
  UK taxable, and not covered by FIG.
- The management fee (about AUD 17,000 per month as at 2026-07) is a cost to
  the paying entity and reduces AIFS profit available for dividends.
- Australia travel is funded through Moncel Limited UK.
- Group contracts are not concluded from UK soil except through this company.
- Costs: GBP 1,400 incorporation, GBP 600 per year registered office, annual
  accounts and tax compliance.
- Open: which entity is the services-agreement counterparty (CIFS preferred);
  minimum defensible director remuneration; VAT registration when turnover
  requires it.

## Review

Revisit when the services agreement counterparty is settled in writing, and
before departure from the UK to plan extraction of retained profit.
```

- [ ] **Step 3: Write `decisions/0003-regular-dividend-aud-50k-monthly.md`**

```markdown
---
number: 0003
title: Regular dividend of AUD 50,000 per month from June 2026
domain: extraction
materiality: policy
status: accepted
proposed: 2026-06-08
decided: 2026-06-08
deciders: [Stu, Danni]
supersedes:
superseded-by:
sources:
  - notes/2026-06-08-owners-meeting-dividends-and-cash-floor.md
  - notes/2026-07-23-q2-financial-review.md
---

## Context

Back-filled on 2026-09-03 from the Granola summary of the owners meeting with
Drew Robertson on 2026-06-08. No signed minute is held here; the AIFS board
resolves each dividend on the owners' request.

With the move complete and Moncel Limited UK not yet billing, Stu and Danni
needed a predictable monthly income in the UK. The prior regular dividend was
AUD 33,000 per month. Distributions from the trusts are within FIG scope for
2026/27 to 2029/30 if claimed (C1), so the timing of extraction is
tax-efficient now and less so after 2030.

## Options considered

1. **Hold at AUD 33,000 per month.** Preserves more cash in AIFS but leaves
   the owners short during the settling-in period.
2. **Raise to AUD 50,000 per month with a formula behind it.** Meets
   household needs, is affordable against FY2026 profit, and ties the number
   to a rule (66% of profit after a 12% employee bonus provision and a 25% tax
   provision) so it can be revisited objectively.
3. **Variable monthly dividend equal to the formula output.** Most
   responsive but gives the household an unpredictable income and complicates
   the transfer documentation each month.

## Decision

Set the regular dividend at AUD 50,000 per month from June 2026, paid by AIFS
to the trusts and distributed to Stu and Danni 50/50 into their Australian
Wise accounts, then transferred to the UK. The guiding formula is 66% of
remaining profit after a 12% employee bonus provision and a 25% tax
provision. Non-regular dividends above AUD 50,000 are excluded from SLT bonus
calculations.

## Consequences

- Adds AUD 17,000 per month to AIFS's cost base relative to the prior level.
- Each payment requires a dividend statement and trustee minute using the
  William Buck template of 2026-06-10, so that UK bank transfer flags can be
  answered with documentation.
- FIG claims for 2026/27 onward should be considered each year so these
  distributions stay outside UK tax (C1, C2); this is a Buzzacott question
  before each return.
- Interacts with D-0004: nothing beyond the regular dividend is paid until the
  cash floor is reached.

## Review

At each quarterly financial review, and when AIFS's cash position reaches the
D-0004 floor.
```

- [ ] **Step 4: Write `decisions/0004-aifs-cash-floor-aud-1-3m.md`**

```markdown
---
number: 0004
title: Retain surplus in AIFS to an AUD 1.3M cash floor; pause extra distributions until reached
domain: extraction
materiality: policy
status: accepted
proposed: 2026-06-08
decided: 2026-06-08
deciders: [Stu, Danni]
supersedes:
superseded-by:
sources:
  - notes/2026-06-08-owners-meeting-dividends-and-cash-floor.md
---

## Context

Back-filled on 2026-09-03 from the Granola summary of the owners meeting on
2026-06-08.

AIFS held about AUD 940,000 in cash. The owners had to choose between
extracting surplus now, while FIG makes distributions tax-free in the UK
(C1), or holding it in the business as runway. High-yield savings in the
business earn roughly 4%; external investments were expected to earn 8 to 9%
with diversification benefits.

## Options considered

1. **Extract surplus now and invest personally.** Captures FIG-era
   tax-free extraction and higher expected returns, but leaves AIFS thin on
   runway heading into a seasonally weak December and an active period of
   investment in the platform.
2. **Retain everything in the business indefinitely.** Maximum safety, but
   forgoes the FIG window and concentrates the household's entire net worth
   in one operating business, the pattern of the last 13 years.
3. **Set an explicit cash floor, retain until it is reached, then resume
   extraction.** Makes the trade-off explicit and time-bound.

## Decision

Retain surplus in AIFS until cash reaches AUD 1.3M, built as two months of
PPC spend (~AUD 482,000) plus four months of general expenses (~AUD 410,000)
plus a December loss cushion. Target date November 2026. Owner bonuses and
distributions beyond the D-0003 regular dividend are suspended until the
floor is reached. Money retained in the business is regarded as owner money.

## Consequences

- No extra extraction is expected before Q1 2027. The investment function
  therefore has only the regular dividend and Moncel Limited UK dividends to
  deploy in 2026.
- Drew is accountable for cost control and for documenting ROI on any
  investment spend in the business.
- Accepted cost: roughly 4 to 5 percentage points of forgone return on the
  retained balance for the period, and FIG-year capacity not used.
- Once the floor is reached, the size and timing of the resumed distributions
  is a new decision.

## Review

At the November 2026 financial review, or earlier if cash reaches the floor.
```

- [ ] **Step 5: Write `decisions/0005-investment-vehicle-outside-uk-and-trusts.md`**

```markdown
---
number: 0005
title: Any investment vehicle sits outside the UK and outside the trusts; consult Buzzacott before incorporating
domain: investment
materiality: policy
status: accepted
proposed: 2026-05-19
decided: 2026-05-19
deciders: [Stu, Danni]
supersedes:
superseded-by:
sources:
  - context/digests/2026-05-07-buzzacott-uk-tax-report.md
  - context/digests/2026-05-07-buzzacott-corporate-residency-review.md
---

## Context

Back-filled on 2026-09-03 from the Buzzacott meeting of 2026-05-19 as recorded
in the UK Restructuring Phase 2 task notes (section L, "Future investment
vehicle"). Recorded as an in-principle constraint agreed with Buzzacott, not a
choice of vehicle.

The owners intend to build an investment portfolio from Moncel profits. Both
trusts are settlor-interested and must not acquire UK property or receive
additions while Stu and Danni are UK resident (C6, C9). A UK-resident vehicle
would produce UK-source income outside FIG and UK-situs assets inside IHT
(C6). A vehicle controlled from the UK could itself become UK resident (C10).

## Options considered

1. **Invest inside the trusts.** Uses an existing structure, but adds assets
   to settlor-interested trusts contrary to the advice assumptions and risks
   the FIG and IHT position of the whole trust.
2. **Invest through a UK company or UK accounts.** Convenient, but everything
   is UK-source and UK-situs: no FIG relief, inside IHT.
3. **Hold a non-UK vehicle or accounts outside the trusts, with Buzzacott
   consulted on form and location before anything is created.** Preserves FIG
   treatment of foreign income and gains and keeps assets foreign-situs,
   provided management and control is handled correctly.

## Decision

Any investment vehicle or account used by the investment function is set up
outside the UK and outside the two trusts, and Buzzacott is consulted before
any entity is incorporated or any structure is committed to. The specific
vehicle, jurisdiction, provider and currency are not decided by this record.

## Consequences

- Danni's forthcoming investment proposal and every subsequent investment
  decision must be tested against this constraint and C5 (reporting-fund
  status of any pooled fund).
- Cash accumulating in UK bank accounts before a vehicle exists is UK-situs
  and inside IHT (C6); the amount held there should be limited to what the
  household needs.
- A Buzzacott engagement for structuring advice is a cost of the first
  investment decision.

## Review

When the first concrete vehicle is proposed, and if either owner's intention
to leave the UK within four tax years changes.
```

- [ ] **Step 6: Write `decisions/0006-adopt-decision-repository.md`**

```markdown
---
number: 0006
title: Adopt this repository as the decision record for the investment function
domain: both
materiality: policy
status: accepted
proposed: 2026-09-03
decided: 2026-09-03
deciders: [Stu, Danni]
supersedes:
superseded-by:
sources:
  - docs/superpowers/specs/2026-09-03-investment-decision-repo-design.md
---

## Context

Stu and Danni have reinvested Moncel profits for 13 years without an external
portfolio. The move to the UK under FIG creates a four-year window in which
extraction and investment decisions carry unusual weight, and the decisions
already taken in 2026 lived only in meeting notes and adviser emails.

## Options considered

1. **Keep using Moncel's systems and meeting notes.** No new work, but owner
   decisions are mixed with company governance and the current position must
   be reconstructed each time.
2. **A single running document.** Easy to start, but decisions and current
   state blur, and there is no audit trail of what changed when.
3. **An append-only decision log with living policy documents on top.**
   Immutable records for audit; policy documents for the current position;
   context and sources for the facts and advice relied on.

## Decision

Adopt this repository, structured per the design spec of 2026-09-03, as the
system of record for extraction and investment decisions. Decisions are made
only through numbered records; policy documents cite them; policy-materiality
decisions require both owners; figures are recorded but identifiers and
credentials never are; the repository lives on a private GitHub remote.

## Consequences

- Records 0001 to 0005 are back-filled from existing evidence and marked as
  such in their Context sections.
- Danni's investment proposal will be the first record created as `proposed`
  rather than back-filled.
- Reporting, portfolio tracking, tooling and formal meeting formats are out of
  scope until a decision brings each in.
- Maintaining the policy documents on every acceptance is a standing duty.

## Review

After the first ten live decisions, or after one year, whichever comes first.
```

- [ ] **Step 7: Fill the index in `decisions/README.md`**

Replace the empty table under `## Index` with:

```markdown
| No. | Title | Domain | Materiality | Status | Decided |
|---|---|---|---|---|---|
| [0001](0001-corporate-trustee-before-uk-residency.md) | Appoint an Australian corporate trustee to both trusts before UK residency | extraction | policy | accepted | 2026-05-08 |
| [0002](0002-moncel-limited-uk.md) | Incorporate Moncel Limited UK, owned 50/50 outside the trusts, to bill UK work | extraction | policy | accepted | 2026-05-19 |
| [0003](0003-regular-dividend-aud-50k-monthly.md) | Regular dividend of AUD 50,000 per month from June 2026 | extraction | policy | accepted | 2026-06-08 |
| [0004](0004-aifs-cash-floor-aud-1-3m.md) | Retain surplus in AIFS to an AUD 1.3M cash floor; pause extra distributions until reached | extraction | policy | accepted | 2026-06-08 |
| [0005](0005-investment-vehicle-outside-uk-and-trusts.md) | Any investment vehicle sits outside the UK and outside the trusts; consult Buzzacott before incorporating | investment | policy | accepted | 2026-05-19 |
| [0006](0006-adopt-decision-repository.md) | Adopt this repository as the decision record for the investment function | both | policy | accepted | 2026-09-03 |
```

- [ ] **Step 8: Verify**

```bash
ls decisions/ | grep -c '^000[1-6]-'
for f in decisions/000*.md; do grep -q '^status: accepted' "$f" && grep -q '^deciders: \[Stu, Danni\]' "$f" || echo "BAD $f"; done
for f in decisions/000*.md; do awk '/^sources:/{s=1;next} s&&/^  - /{print $2} s&&!/^  - /{s=0}' "$f" | while read p; do test -e "$p" || echo "MISSING $p in $f"; done; done
grep -c '^| \[000' decisions/README.md
```
Expected: `6`; no `BAD` lines; no `MISSING` lines; `6`.

- [ ] **Step 9: Commit**

```bash
git add decisions
git commit -m "Back-fill decision records 0001-0006 and index

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 8: Policy documents

**Files:**
- Create: `policy/extraction-policy.md`
- Create: `policy/investment-policy-statement.md`
- Delete: `policy/.gitkeep`

**Interfaces:**
- Consumes: D-0001 to D-0006 (Task 7), constraints C1 to C12 (Task 4).

- [ ] **Step 1: Write `policy/extraction-policy.md`**

```markdown
# Extraction Policy

How money leaves Moncel and reaches Stu and Danni. Every clause cites the
decision that set it. Change a clause only by accepting a new decision record.

**Last updated:** 2026-09-03

## Current position

Both trusts sit under an Australian corporate trustee and stay outside UK
residence. AIFS pays a regular dividend of AUD 50,000 per month, distributed
50/50 to Stu and Danni through the trusts. Nothing beyond that is paid until
AIFS cash reaches AUD 1.3M, expected November 2026. Moncel Limited UK bills
the group for UK work and is a second, UK-taxed, channel.

## Clauses

1. Both trusts are held by GHS Ellell Management Pty Ltd as sole trustee,
   with Andrew Phillips as its sole director. Stu and Danni do not act as
   trustees and do not direct trustee decisions from the UK. [D-0001]
2. No assets are added to either trust while Stu and Danni are UK resident.
   [D-0001]
3. Every distribution from the trusts is resolved and minuted by the
   corporate trustee on the owners' request, using the William Buck dividend
   statement and minutes template. [D-0003]
4. The regular AIFS dividend is AUD 50,000 per month from June 2026, guided by
   66% of remaining profit after a 12% employee bonus provision and a 25% tax
   provision. [D-0003]
5. Regular distributions are paid 50/50 to Stu and Danni's Australian Wise
   accounts and then transferred to the UK. [D-0003]
6. Non-regular dividends above AUD 50,000 are excluded from SLT bonus
   calculations. [D-0003]
7. AIFS retains surplus until cash reaches AUD 1.3M. Owner bonuses and
   distributions beyond the regular dividend are suspended until then. Money
   retained in the business is regarded as owner money. [D-0004]
8. Stu and Danni's UK work for the group is provided through Moncel Limited
   UK under an arm's-length services agreement and paid as a management fee.
   Group contracts are not concluded from UK soil except through Moncel
   Limited UK. [D-0002]
9. Moncel Limited UK remunerates its owners by dividend in preference to
   salary, using Class A and Class B shares. [D-0002]
10. Whether to claim the FIG regime is considered each tax year with Buzzacott
    before the return is filed, so that trust distributions in FIG years stay
    outside UK tax. [D-0003]

## Not yet decided

- Size and timing of resumed distributions once the AUD 1.3M floor is reached.
- Whether pre-2030 extraction should be accelerated to use the FIG window.
- The services agreement counterparty for Moncel Limited UK (CIFS or AIFS).
- Minimum defensible remuneration for Stu and Danni from Moncel Limited UK.
- Treatment of one-off receipts (asset sales, bonuses) versus regular
  dividends.
- Currency in which distributions are held before investment.
```

- [ ] **Step 2: Write `policy/investment-policy-statement.md`**

```markdown
# Investment Policy Statement

How money is invested once it is in Stu and Danni's hands. Every clause cites
the decision that set it. Change a clause only by accepting a new decision
record.

**Last updated:** 2026-09-03

## Current position

Nothing has been invested. The one established principle is that any vehicle
or account sits outside the UK and outside the trusts, with Buzzacott
consulted before anything is created. Danni's investment proposal is the next
expected decision and will fill most of the list below.

## Clauses

1. Any investment vehicle or account is established outside the UK and
   outside the GHS Hilditch Trust and Ellell Trust. [D-0005]
2. Buzzacott is consulted before any entity is incorporated or any structure
   is committed to for investment purposes. [D-0005]
3. Every investment decision is tested against `context/tax-constraints.md`,
   in particular reporting-fund status of pooled funds (C5), UK situs and
   IHT (C6), and company residence (C10). [D-0005]
4. Reporting cadence and format are decided once the first investment is
   made; none exists yet. [D-0006]

## Not yet decided

- Objectives and time horizon (including the planned departure from the UK
  before the FIG window closes).
- Risk tolerance and drawdown limits.
- Target asset allocation.
- Permitted and prohibited instruments; reporting-fund policy.
- Jurisdiction, provider and account structure.
- Base currency and currency hedging.
- Contribution schedule from extraction.
- Rebalancing rules.
- Reporting cadence and format.
- Whether to engage an investment manager or adviser.
```

- [ ] **Step 3: Remove the placeholder and verify**

```bash
rm policy/.gitkeep
for f in policy/*.md; do echo "$f: clauses=$(awk '/^## Clauses/{c=1;next} /^## /{c=0} c&&/^[0-9]+\./' "$f" | wc -l | tr -d ' ') citations=$(awk '/^## Clauses/{c=1;next} /^## /{c=0} c' "$f" | grep -c '\[D-[0-9]\{4\}\]')"; done
for d in $(grep -oh 'D-[0-9]\{4\}' policy/*.md | sort -u); do n=${d#D-}; ls decisions/$n-*.md >/dev/null 2>&1 || echo "NO RECORD $d"; done
```
Expected: `extraction-policy.md: clauses=10 citations=10`, `investment-policy-statement.md: clauses=4 citations=4`, and no `NO RECORD` lines.

- [ ] **Step 4: Commit**

```bash
git add policy
git commit -m "Add extraction policy and investment policy statement

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 9: CLAUDE.md, final README check, and full verification

**Files:**
- Create: `CLAUDE.md`
- Verify: whole repository

- [ ] **Step 1: Write `CLAUDE.md`**

```markdown
# CLAUDE.md

This is the decision record for the personal investment function of Stu
Hilditch and Danni Cullen. It covers how money leaves Moncel and how it is
invested. It is documents only: no code, no scripts, no tooling.

## Read first, every session

1. `policy/extraction-policy.md`
2. `policy/investment-policy-statement.md`
3. `context/tax-constraints.md`
4. `decisions/README.md`

## Rules

- A choice is made only in a decision record under `decisions/`. Policy and
  context files never introduce a choice of their own.
- An accepted or rejected record is frozen. The only later edit is stamping
  `superseded-by` and setting status `superseded` when a new record replaces
  it.
- Every clause in a policy document ends with `[D-NNNN]` citing an existing
  record. When a record is accepted, update the policy in the same commit.
- Records with `materiality: policy` need `deciders: [Stu, Danni]` before
  status may become `accepted`. Operational records may be accepted by Stu.
- Never write account numbers, account identifiers, credentials, API keys or
  tokens anywhere. Figures as decided are fine.
- ISO dates. Every amount states its currency.
- One commit per decision state change.

## What Claude is and is not

Claude drafts records, digests and analysis and checks proposals against the
constraints. Claude is not a licensed financial or tax adviser. Its analysis
is input to a decision Stu and Danni make. Anything that turns on tax
treatment is written as a question for Buzzacott (UK) or William Buck (AU),
not asserted as settled.

## Common tasks

**A proposal arrives (for example Danni's investment proposal).** Copy the
document to `sources/` with a provenance row. Create the next-numbered record
with `status: proposed`. In Options, set out the proposal alongside
alternatives and test each against `context/tax-constraints.md`. Long
analysis goes in `notes/YYYY-MM-DD-title.md`, linked from `sources`. Update
the index in `decisions/README.md`.

**A decision is made.** Set `status`, `decided`, and `deciders`. Update the
relevant policy document: add, amend or remove clauses, each citing the
record, and refresh "Current position" and "Not yet decided". Update the
index. One commit.

**New adviser advice arrives.** Copy to `sources/` with a provenance row.
Write `context/digests/YYYY-MM-DD-slug.md` with sections Summary, Assumptions
the advice relies on, Constraints it imposes, Open questions. Update
`context/tax-constraints.md` if a constraint changes.

**A meeting happened.** Pull the Granola summary into
`notes/YYYY-MM-DD-title.md` with date, attendees, source line, and which
decisions it fed. No other structure is required.

**Facts change.** Update `context/entities.md`, `context/money-flow.md` or
`context/advisors.md` directly. Facts are not decisions.

## Verification checklist

Run before reporting any change complete:

1. Every policy clause cites an existing record:
   `for d in $(grep -oh 'D-[0-9]\{4\}' policy/*.md | sort -u); do ls decisions/${d#D-}-*.md >/dev/null 2>&1 || echo "NO RECORD $d"; done`
2. Every record's `sources` paths resolve:
   `for f in decisions/[0-9]*.md; do awk '/^sources:/{s=1;next} s&&/^  - /{print $2} s&&!/^  - /{s=0}' "$f" | while read p; do test -e "$p" || echo "MISSING $p in $f"; done; done`
3. The decisions index matches the files on disk:
   `diff <(ls decisions/ | grep -o '^[0-9]\{4\}' | sort) <(grep -o '^| \[[0-9]\{4\}' decisions/README.md | grep -o '[0-9]\{4\}' | sort)`
4. The sources provenance table matches the files on disk:
   `diff <(ls sources/ | grep -v README.md | sort) <(grep -o '^| `[^`]*`' sources/README.md | tr -d '|` ' | sort)`
5. No identifiers or credentials:
   `grep -rniE 'iban|sort code|bsb|account (no|number)|routing|swift|password|api[_ -]?key|token' --include='*.md' . | grep -v CLAUDE.md`
   Expected: no output.
```

- [ ] **Step 2: Run the full verification checklist**

```bash
cd /Users/stuarthilditch/Developer/investing
for d in $(grep -oh 'D-[0-9]\{4\}' policy/*.md | sort -u); do ls decisions/${d#D-}-*.md >/dev/null 2>&1 || echo "NO RECORD $d"; done
for f in decisions/[0-9]*.md; do awk '/^sources:/{s=1;next} s&&/^  - /{print $2} s&&!/^  - /{s=0}' "$f" | while read p; do test -e "$p" || echo "MISSING $p in $f"; done; done
diff <(ls decisions/ | grep -o '^[0-9]\{4\}' | sort) <(grep -o '^| \[[0-9]\{4\}' decisions/README.md | grep -o '[0-9]\{4\}' | sort) && echo INDEX_OK
diff <(ls sources/ | grep -v README.md | sort) <(grep -o '^| `[^`]*`' sources/README.md | tr -d '|` ' | sort) && echo SOURCES_OK
grep -rniE 'iban|sort code|bsb|account (no|number)|routing|swift|password|api[_ -]?key|token' --include='*.md' . | grep -v CLAUDE.md; echo "IDENT_CHECK_DONE"
find . -name .gitkeep -not -path './.git/*'
```
Expected: no `NO RECORD` or `MISSING` lines; `INDEX_OK`; `SOURCES_OK`; nothing between the grep and `IDENT_CHECK_DONE`; no `.gitkeep` files remain.

Note on check 5: the word "account" appears legitimately (e.g. "Wise accounts"). The pattern only matches "account no" or "account number". If a legitimate phrase matches, read the line and confirm it is not an identifier; do not weaken the pattern.

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "Add CLAUDE.md session instructions and verification checklist

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

- [ ] **Step 4: Report hand-over items to Stu**

State in the final message:

- The repository has no remote. To push to a private GitHub repository Stu
  creates:
  ```bash
  git remote add origin git@github.com:<owner>/investing.git && git push -u origin main
  ```
- Items marked **confirm** in `context/entities.md` need checking against
  ASIC and Companies House.
- Documents listed under "Known documents not yet copied" in
  `sources/README.md` await Stu's go-ahead.
- Danni's investment proposal is the next expected decision record.
