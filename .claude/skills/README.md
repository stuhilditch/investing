# Installed skills

Third-party skills copied into this repository so they travel with it and are
visible in git. Each was read for prompt-injection and network or credential
access before being copied (2026-09-03): none found. Scripts depend only on
numpy, scipy and pandas. Skills produce analysis that lands in `notes/`; they never
write to `decisions/` or `policy/`.

| Skill | Source | Commit copied | Licence | Notes |
|---|---|---|---|---|
| `investment-policy` | github.com/JoelLewis/finance_skills, plugins/wealth-management/skills | 5c498ea | MIT | IPS construction framework. US examples (ERISA); method is neutral. |
| `asset-allocation` | github.com/JoelLewis/finance_skills | 5c498ea | MIT | SAA/TAA, mean-variance, Black-Litterman, risk parity; script with `--verify`. |
| `historical-risk` | github.com/JoelLewis/finance_skills | 5c498ea | MIT | Volatility, drawdown, VaR, downside deviation, tracking error; script. |
| `portfolio` | github.com/gauss314/skills, skills/portfolio | 5156f81 | MIT | Markowitz, Black-Litterman, HRP/HERC/NCO optimiser with tests. Written in Spanish. |

None of these knows UK tax rules. Every output is tested against
`context/tax-constraints.md` before it informs a decision.
