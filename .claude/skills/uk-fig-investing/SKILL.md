---
name: uk-fig-investing
description: Evaluates any investment, fund, ETF, broker, account, cash holding or vehicle against the UK tax position of Stu and Danni, who are UK resident under the 4-year FIG regime with Australian trusts and a UK service company. Produces a facts-reconciled, constraint-by-constraint evaluation with adviser questions and a reporting-fund check. Use it whenever money is about to be placed anywhere, whenever a proposal, friend or adviser note claims something is tax-efficient or "obvious", whenever cash is sitting in UK accounts, and whenever a finance skill is about to apply US tax logic (IRA, 401k, Roth, wash sale) to this household, even if the user just asks a quick question.
---

# UK FIG Investing

## Overview

Stu and Danni are UK resident for 2026/27 to 2029/30 under the Foreign
Income and Gains regime, with business interests in Australian trusts and a
UK service company. Every generic finance skill in this repository assumes a
US taxpayer. This skill supplies the UK-specific checks, and the rule that
tax treatment is confirmed by Buzzacott, never asserted here.

**REQUIRED BACKGROUND:** `context/tax-constraints.md` (C1 to C15) and
`context/entities.md`. Read both before applying this skill.

## When to use

- A fund, ETF, broker, account type or vehicle is being proposed or compared.
- A document says "tax-free", "FIG-efficient", "outside UK tax" or similar.
- `asset-allocation`, `rebalancing`, `portfolio-rebalance`, `tax-loss-harvesting`
  or `financial-plan` output mentions IRA, 401k, Roth, wash sale, RMD or
  Social Security. Strip those and apply this skill instead.

## Output contract

An evaluation produced with this skill contains these six parts, in this
order, under these headings. A request for a short or decisive answer shortens
each part; it does not remove one, because the parts most often dropped under
time pressure (facts reconciliation, adviser routing) are where the money is
lost.

**1. Facts reconciled.** A table with columns `Claim | Proposal says | Repo
says | Wins`, one row per date, entity, status or figure the proposal states.
The first row is always the UK residence start date: the repo value is
2026-05-11 (Buzzacott, `context/tax-constraints.md`), and the repo wins unless
Buzzacott has revised it. A proposal quoting any other date is a discrepancy
to record, not a fact to repeat.

**2. Constraint table.** Columns `Constraint | Verdict | Evidence`, one row
for each of C1 to C15 in order. Verdict is PASS, FAIL, ADVICE NEEDED or N/A
with a reason. All fifteen rows appear because the constraints that get skipped as
"obviously irrelevant" (trust residence, TRS, company residence) are the
ones a UK-based holding quietly trips.

**3. Verified externally.** Reporting-fund status of every pooled fund is
checked against HMRC's published list, not a factsheet or aggregator,
because the list is the only source HMRC will accept and factsheets lag.
Run `python3 .claude/skills/uk-fig-investing/scripts/check_reporting_fund.py <ISIN> [<ISIN> ...]`
from the repository root; it downloads the current list from gov.uk and
prints FOUND or MISSING per ISIN with the list date. Quote that output. If
the script fails, say so and mark C5 ADVICE NEEDED rather than substituting
another source.

**4. Adviser questions.** Each ADVICE NEEDED row rewritten as a numbered
question for Buzzacott, answerable yes or no, with the decision that depends
on the answer. Broker and account-titling questions go to the broker.

**5. Household specifics.** One line each on how these bear on the case: both
spouses have UK-source dividend income from Moncel Limited UK, so a FIG
claim's cost (C2) is real each year; funding comes from trust distributions
and never adds assets to the trusts (C9); cash parked in UK accounts is
UK-situs and earns UK-source interest (C6), and the concrete alternative is
the Australian accounts that already receive the distributions; departure is planned before 2030-04-05 and a return within
five years is possible (C13).

**6. Decision routing.** The evaluation is analysis for `notes/`. The choice
is made in a `decisions/` record with `materiality: policy` and both deciders,
and nothing is "decided" in the evaluation itself.

## Quick reference

| Topic | Rule of thumb | Constraint |
|---|---|---|
| Fund domicile | Irish or Luxembourg UCITS with HMRC reporting-fund status; never US-domiciled while UK resident | C5, C14 |
| Accumulating share class | Reinvested income is Excess Reportable Income, taxable yearly; FIG coverage of ERI is unconfirmed | C14 |
| Situs for IHT | Register location, not listing venue; UK cash and UK property are UK-situs | C6 |
| Leaving the UK | Four of the last seven years resident triggers the temporary non-residence rule on gains realised abroad if back within five years | C13 |
| US persons | Non-US funds become PFICs if either spouse becomes a US taxpayer; flag any plausible route | C15 |
| Vehicles | Outside the UK, outside the trusts, Buzzacott consulted first | C9, C12 |
| UK wrappers (ISA, SIPP, GIA at a UK platform) | Everything inside is UK-situs and UK-source, so FIG adds nothing and IHT applies; the ISA wrapper is not recognised by most other countries once resident there, and a SIPP locks funds until at least 57. Conflicts with D-0005 unless a record says otherwise | C6, C12 |
| Cash awaiting investment | GBP in UK banks is UK-situs and its interest is UK-source; the named alternative is to leave distributions in the Australian accounts that receive them, or another non-UK account, until deployed | C6 |
| FIG claim | Per person, per year, on the return; costs the personal allowance and CGT exemption that year | C1, C2 |

## Red flags

- The answer repeats a date, ISIN or status from the proposal without a row
  in the facts table.
- Fewer than fifteen constraint rows.
- The words "tax-free" without "if a valid FIG claim is made for that year".
- IRA, 401k, Roth, wash sale or RMD anywhere in the output.

## Common mistakes

- Treating a proposal's tax statements as established because they cite
  GOV.UK. Cite them as the proposal's claim and route to Buzzacott.
- Saying "tax-free" when the accurate statement is "outside UK tax if a valid
  FIG claim is made for that year".
- Ignoring the FIG claim trade-off because "the saving dwarfs the allowance".
  Compute it: UK dividend income from Moncel Limited UK times the allowance
  lost, against the foreign income and gains sheltered.
- Letting a US-built skill's rebalancing or harvesting logic into the output.
