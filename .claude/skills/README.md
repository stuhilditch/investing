# Installed skills

Third-party skills copied into this repository so they travel with it and are
visible in git. Each was read for prompt-injection and network or credential
access before being copied (2026-09-03): none found. Analysis scripts depend only on
numpy, scipy and pandas; the two data skills fetch from Yahoo Finance and
historyofmarket.com and nowhere else. Skills produce analysis that lands in `notes/`; they never
write to `decisions/` or `policy/`.

| Skill | Source | Commit copied | Licence | Notes |
|---|---|---|---|---|
| `investment-policy` | github.com/JoelLewis/finance_skills, plugins/wealth-management/skills | 5c498ea | MIT | IPS construction framework. US examples (ERISA); method is neutral. |
| `asset-allocation` | github.com/JoelLewis/finance_skills | 5c498ea | MIT | SAA/TAA, mean-variance, Black-Litterman, risk parity; script with `--verify`. |
| `historical-risk` | github.com/JoelLewis/finance_skills | 5c498ea | MIT | Volatility, drawdown, VaR, downside deviation, tracking error; script. |
| `portfolio` | github.com/gauss314/skills, skills/portfolio | 5156f81 | MIT | Markowitz, Black-Litterman, HRP/HERC/NCO optimiser with tests. Written in Spanish. |
| `forward-risk` | github.com/JoelLewis/finance_skills | 5c498ea | MIT | VaR, expected shortfall, Monte Carlo, stress tests; script with `--verify`. |
| `currencies-and-fx` | github.com/JoelLewis/finance_skills | 5c498ea | MIT | FX exposure, hedging, parity relationships; script. |
| `diversification` | github.com/JoelLewis/finance_skills | 5c498ea | MIT | Correlation, minimum variance, diversification ratio; script. |
| `yahoo-finance` | github.com/gauss314/skills, skills/yahoo-finance | 5156f81 | MIT | Unofficial Yahoo Finance API for price history and fundamentals. Makes network calls to Yahoo only; needs `curl_cffi`. Spanish. |
| `historyofmarket` | github.com/gauss314/skills, skills/historyofmarket | 5156f81 | MIT | S&P 500 history since 1871 (price, CAPE, drawdowns) from historyofmarket.com, CC BY 4.0 data. Network calls to that site only. Spanish. |
| `uk-fig-investing` | written in this repository 2026-09-03 | n/a | this repo | Household-specific UK checks (FIG, reporting funds, ERI, situs, temporary non-residence, US-person risk) and the output contract for evaluating any investment. Applies on top of every skill above. |

None of the third-party skills knows UK tax rules. `uk-fig-investing` supplies
them; every evaluation is tested against `context/tax-constraints.md` before it
informs a decision.
