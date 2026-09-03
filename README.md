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
