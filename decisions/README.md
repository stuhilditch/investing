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
|---|---|---|---|---|

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
