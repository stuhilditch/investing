# Analysis of Danni's investment proposal (S&P 500 under FIG)

**Date:** 2026-09-03
**Prepared by:** Claude, applying `.claude/skills/uk-fig-investing` to
`sources/2026-08-27-danni-investment-proposal-sp500-under-fig.pdf`
**Status:** Analysis only. No decision has been made and no decision record
exists for this proposal. Stu has not yet read the proposal.
**Fed decisions:** none yet; input to a future `proposed` record

---

# Evaluation

## Headline answer

**Not yet a clean yes.** The structure Danni proposes — Irish-domiciled
accumulating S&P 500 UCITS ETF, held in a joint Interactive Brokers account
opened outside the UK, funded straight from your Australian account, with an
active FIG election filed every year — is the right shape and nothing in it
fails a hard constraint. But three things it labels "advice needed" really
are unresolved, one fact in the proposal conflicts with this repo's record,
and Buzzacott sign-off (required by your own policy before any investment
structure is committed to) hasn't happened. Get those closed and this becomes
a yes. Don't wire money before then.

## Fund and account structure to use

- **Fund:** CSPX — iShares Core S&P 500 UCITS ETF (Acc), ISIN
  `IE00B5BMR087`, Irish-domiciled, accumulating. Confirmed on HMRC's current
  reporting-fund list (checked below) — this clears the biggest way a "cheap
  tracker" quietly turns into an income-tax bill.
- **Account:** joint Interactive Brokers account, opened under a non-UK IBKR
  entity (Ireland or the US entity, not IBKR UK), funded in AUD directly from
  your Australian account — not routed through UK cash.
- **Tax treatment each year:** both of you actively claim FIG relief
  (SA106/SA109) on the return for that year; this is a decision each year,
  not a default.

This matches D-0005 (vehicle outside the UK and outside the trusts) and the
C6 alternative of not letting distributions sit in UK-situs cash. It is not
yet a decision — see Decision routing below.

## What must happen before the first transfer

1. **Resolve the FIG start-date conflict.** The proposal states 18 May 2026;
   this repo's record (Buzzacott) states 11 May 2026. Get Buzzacott to
   confirm the correct date in writing before relying on either — it affects
   which tax year's activity is protected.
2. **Written Buzzacott confirmation on ERI/FIG interaction (C14).** Whether
   CSPX's Excess Reportable Income is covered by a FIG claim is, by the
   proposal's own admission, unsettled. Get this in writing before the first
   purchase of an accumulating fund — not after.
3. **Written Buzzacott confirmation on UK IHT situs of CSPX (C6).** The
   proposal covers US estate tax but not UK IHT situs of an Irish-domiciled
   fund held via a US/Irish broker entity. This repo's tax-constraints file
   has flagged this as advice needed since May and it is still open.
4. **Buzzacott sign-off on the account/vehicle itself (D-0005 / C12).**
   Policy requires Buzzacott is consulted before any investment structure is
   committed to. That consultation on the IBKR account specifically hasn't
   happened yet as far as this repo shows.
5. **Confirm the temporary non-residence exposure (C13)** with an adviser
   before assuming the Q1 2030 departure is clean — the proposal correctly
   identifies that you hit the 4-of-7 threshold, so any sale after leaving,
   followed by a return within 5 years, loses FIG shelter on those gains.
   Not a blocker to opening the account or contributing; is a blocker to any
   future sale-then-return plan.
6. **Disclose any plausible US-taxpayer route (C15)** to Buzzacott before
   fixing the fund choice. If there's a real chance of US tax status for
   either of you, this whole recommendation may need to flip to a
   US-domiciled fund instead.
7. **A `decisions/` record.** None of the above becomes real until it's
   written up as a decision record with `materiality: policy` and both of you
   named as deciders (see Decision routing). Right now nothing is decided —
   this is analysis, and the account should not be funded on the strength of
   this note alone.

None of these are reasons to abandon the plan. They are the specific,
load-bearing confirmations the proposal itself says are needed before real
money moves — and D-0005 already requires the Buzzacott step regardless.

---

## 1. Facts reconciled

| Claim | Proposal says | Repo says | Wins |
|---|---|---|---|
| UK residence start date | 18 May 2026 | 2026-05-11 (`context/tax-constraints.md`, Buzzacott) | Repo — flag the discrepancy to Buzzacott/lawyers before relying on either date |
| FIG window | Both eligible 2026/27–2029/30 | Same (C1) | Agree |
| Planned departure | Q1 2030 | "well before 2030-04-05" (tax-constraints); "planned departure from the UK before the FIG window closes" (IPS, not yet decided in detail) | Consistent |
| CSPX ISIN | IE00B5BMR087 | Not previously recorded here | New fact — now verified (see Section 3) |
| Fund reporting-fund status | Implied by "UK reporting fund status" | Not previously verified in this repo | Verified below: FOUND |
| No UK ISA planned | Confirmed | IPS: "Permitted and prohibited instruments" not yet decided; UK wrappers noted as generally conflicting with D-0005 | Consistent with policy, not yet formally decided |
| Funding source | "Funded directly from Australia" | Money-flow: distributions land in Australian Wise accounts first (step 5), then move to UK (step 6) | Proposal's approach avoids the UK-situs cash step — consistent with the C6 alternative already named in this repo |
| Vehicle location | IBKR account outside UK jurisdiction | D-0005: any investment vehicle sits outside the UK and outside the trusts | Consistent |
| Temporary non-residence rule | Cites HS278, describes 4-of-7 test correctly | C13, sourced from this same proposal | Consistent (repo's C13 was in fact written from this document) |

## 2. Constraint table

| Constraint | Verdict | Evidence |
|---|---|---|
| C1 — FIG window | PASS | Proposal correctly scopes the claim to 2026/27–2029/30, per person, per year, on the return |
| C2 — Cost of a FIG claim | PASS (with a live trade-off) | Proposal names the £12,570 personal allowance and £3,000 CGT exempt amount given up each claim year (3.4). Both of you have UK-source dividend income from Moncel Limited UK, so this cost is real every year, not theoretical — must be checked at each filing, not assumed to be dwarfed |
| C3 — Settlor-interested trusts | N/A | This fund purchase is funded from personal accounts post-distribution, not from trust assets directly; trust income tax treatment is governed upstream by extraction-policy, not by this fund choice |
| C4 — Motive defence / 2012 boundary | N/A | Not implicated by a personally-funded ETF purchase |
| C5 — Offshore income gains / reporting-fund status | PASS | Verified externally against the HMRC list — see Section 3 |
| C6 — IHT and situs | ADVICE NEEDED | Proposal addresses US estate tax (3.1) but not UK IHT situs of an Irish-domiciled fund held via a non-UK broker entity. Repo has flagged this open since 2026-05 and it remains open |
| C7 — Long-term residence threshold | N/A | Departure planned well inside the 10-of-20-year threshold; not engaged by this investment |
| C8 — Trust residence / Principal powers | N/A | No exercise of Principal powers involved in opening a personal brokerage account |
| C9 — No additions to the trusts | PASS | Funded from Stu and Danni's personal accounts after distribution, not added to either trust |
| C10 — Company residence / PE | N/A | Personal investment account, not a company action |
| C11 — Trust Registration Service | N/A | No UK-touching trust activity created by this account |
| C12 — Investment vehicle location | ADVICE NEEDED | Structure (non-UK IBKR entity, outside the trusts) matches D-0005 in shape, but the required Buzzacott consultation on this specific structure has not happened yet per this repo |
| C13 — Temporary non-residence | ADVICE NEEDED | Proposal correctly identifies the 4-of-7 exposure (5.2); no sale should be planned around a possible return within 5 years of the Q1 2030 departure without adviser sign-off first |
| C14 — Excess Reportable Income | ADVICE NEEDED | Proposal itself flags this as genuinely unsettled (5.1) — get it in writing before the first purchase of an accumulating fund, as C14 requires |
| C15 — US person risk | ADVICE NEEDED | Proposal flags PFIC exposure correctly (5.3) and says to disclose any plausible US-taxpayer route now, before the fund choice is fixed |

## 3. Verified externally

Ran `python3 .claude/skills/uk-fig-investing/scripts/check_reporting_fund.py IE00B5BMR087` from the repository root:

```
HMRC list: .../20260804_approved_offshore_reporting_funds.ods
List file date (from filename): 2026-08-04
Checked on: 2026-09-03  (rows scanned: 124141)
FOUND   IE00B5BMR087
        I | I0074 | iShares VII plc | I0074-0041 | iShares Core S&P 500 UCITS ETF USD (Acc) | IE00B5BMR087
```

CSPX is on HMRC's current published reporting-fund list, checked by ISIN as
the skill requires, not taken from the fund factsheet. This clears C5 for
CSPX specifically. It does not resolve C14 (ERI/FIG interaction) — reporting-
fund status and FIG coverage of ERI are two separate open questions.

## 4. Adviser questions

To Buzzacott (written, before the first transfer):

1. Was Stu and Danni's UK residence start date 2026-05-11 or 2026-08-27's
   proposal's stated 18 May 2026? Which date governs the 2026/27 FIG window?
2. Is Excess Reportable Income from a foreign reporting fund (CSPX)
   covered by a valid FIG election, or is it taxed regardless?
3. What is the UK IHT situs of an Irish-domiciled UCITS ETF (CSPX) held via
   a non-UK Interactive Brokers entity — is it inside or outside the UK IHT
   net while Stu and Danni are not long-term UK resident?
4. Does opening this Interactive Brokers account, on these terms, satisfy
   the D-0005 requirement to consult Buzzacott before committing to an
   investment structure, or is a separate specific sign-off still needed?
5. Given the planned Q1 2030 departure, what is the practical exposure under
   the temporary non-residence rules if either of us sells CSPX shares while
   non-resident and there is a realistic chance of returning within 5 years?
6. Does either of us have any plausible route to US tax status (visa,
   marriage, citizenship) that should change the fund recommendation from
   CSPX to a US-domiciled alternative?

To Interactive Brokers (broker, not tax, questions):

7. Confirm in writing which legal entity (IBKR LLC or IBKR Ireland, not IBKR
   UK) the joint account will be opened under, given declared UK tax
   residency, and that this routes correctly to Irish UCITS access.
8. Confirm the joint account will be structured as Joint Tenants with Rights
   of Survivorship, and what documentation (W-8BEN for both of you) is
   required at onboarding.

## 5. Household specifics

- Both of you have UK-source dividend income from Moncel Limited UK, so the
  FIG claim's annual cost (giving up the personal allowance and CGT
  exemption, C2) is a real number to check every filing, not a rounding
  error to assume away.
- Funding comes from trust distributions already sitting in your personal
  Australian Wise accounts; the proposal's "fund directly from Australia"
  approach correctly avoids adding assets to either trust (C9) and avoids
  routing the money through UK-situs cash first.
- Cash otherwise parked in UK accounts is UK-situs and earns UK-source
  interest (C6); the Australian accounts that already receive the
  distributions remain the concrete alternative to holding GBP idle in the
  UK before this account is opened.
- Departure is planned before 2030-04-05, and a return within five years is
  plausible enough that the temporary non-residence exposure (C13) — which
  this proposal itself surfaced — needs a real answer before any future sale
  of this holding, not just before the first purchase.

## 6. Decision routing

This document is analysis for `notes/`, not a decision. Nothing here is
"decided." To act on it: write a next-numbered record in `decisions/` with
`status: proposed`, set out this option (CSPX / joint IBKR account / annual
FIG election) alongside the alternatives the proposal itself lists (VUAA,
VWRA/VWRP, IUSA, UK ISA/GIA, SIPP, offshore bond), test each against
`context/tax-constraints.md`, and move it to `accepted` only once both Stu
and Danni are named as `deciders` (this is `materiality: policy` — it moves
money out of Moncel and opens a new account). Copy the proposal's provenance
row into `sources/README.md` if not already there, and update
`decisions/README.md`'s index in the same commit the record is accepted.
