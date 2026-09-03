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

## Installed skills

`.claude/skills/` holds four vetted third-party skills (investment-policy,
asset-allocation, historical-risk, portfolio) and the Anthropic
`wealth-management` plugin is enabled at project scope; see
`.claude/skills/README.md` for provenance. Scripts run with `uv run`. Skill
output is analysis for `notes/`; it never writes to `decisions/` or `policy/`,
and none of these skills knows UK tax rules, so every result is tested against
`context/tax-constraints.md` before it informs a decision.

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
   `grep -rniE '(iban|sort code|bsb|routing|swift|account (no\.?|number))[: ]*[0-9]' --include='*.md' README.md CLAUDE.md decisions policy context notes sources`
   Expected: no output.
