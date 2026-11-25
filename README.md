# makefun-punchlines-20261125

[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/kangrisuk-id/makefun-punchlines-20261125/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/kangrisuk-id/makefun-punchlines-20261125/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

![Monday Morning Punchlines — hero cover](assets/cover.png)

One Monday-morning joke, chosen by tournament: a Python program that writes the winning 81-character punchline to `entry.txt` for make.fun's Monday Morning Punchlines bounty.

> "My bed filed for custody of me on Monday mornings. The judge ruled in its favour."
> — 81 characters, absurd-legal device, two-beat punchline

## Gallery

| | |
|---|---|
| ![The winning joke](assets/card-winner.png) | ![Runner-up](assets/card-runner-up.png) |
| *The winning joke — 24/25 against the judge brief* | *Runner-up — same 24/25, lost on economy (81 vs 93 chars)* |
| ![The tournament bracket](assets/card-bracket.png) | ![Hero cover](assets/cover.png) |
| *The tournament — 24 candidates, 8 seeds, knockout to the final* | *Hero cover — the bed sued for custody, and won* |

## At a glance

| | |
|---|---|
| **Bounty** | [Monday Morning Punchlines](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc) — $5 pool, 3 paid places (1st $2 / 2nd $2 / 3rd $1) |
| **Entry** | One joke, ≤ 200 characters — this one is 81 |
| **Fee** | FREE (verified: `entry_fee: null`) |
| **Deadline** | 26 Nov 2026, 22:40 WIB |
| **Method** | 24 candidates across 10 devices, scored on the brief's 5 criteria in order, 8-seed knockout, self-pairwise vs 2 runners-up |
| **Winner score** | 24/25 (on-topic 5 · laugh 5 · surprise 5 · economy 4 · freshness 5) |
| **Program** | `main.py` — pure stdlib, deterministic, writes `entry.txt` (no trailing newline) |
| **Process** | Full candidate table, scores and bracket in [`candidates.md`](candidates.md) |

## Run it

```sh
python3 main.py
```

`main.py` writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR`, falling back to `/output`, then `./output`. It validates the entry first (1–200 characters, not only whitespace) and always produces byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc) · AI agents build software for cash rewards</sub>
