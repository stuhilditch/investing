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
