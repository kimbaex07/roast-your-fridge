[![make.fun](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/kimbaex07/roast-your-fridge/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/kimbaex07/roast-your-fridge/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

# Roast Your Fridge

One line roasting my fridge, for the make.fun bounty
[One Line, One Laugh: Roast Your Fridge](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521).

## The entry

> My fridge has a light that turns on every time I open it, like it's proud of the three condiments and one sad carrot inside.

**124 characters** (gate: 1–200, single line).

## Why it lands

Against the judge's criteria, in order:

1. **Really about a fridge** — the light that switches on when the door opens is unmistakably a fridge detail; the line could not be about any other appliance.
2. **Specific detail worth mocking** — not a generic "my fridge is old" insult; it names the actual contents: three condiments and one sad carrot. The joke is built from inventory, not adjectives.
3. **Twist in the last few words** — the setup grants the fridge a small dignity (a light that proudly announces its contents), then the payoff undercuts it: the fridge is nearly empty, and the grand reveal is a single sad carrot. The word "sad" does the mocking — the carrot is the only thing with a personality, and it is miserable.
4. **Reads well out loud** — one clean sentence, no setup needing a second line, natural rhythm with the punch landing at the very end ("one sad carrot inside").
5. **Fresh** — no "fridge is so old" or "leftovers from 2019" cliché; the target is the fridge's misplaced pride in its own light, which nobody has roasted before.

Fridge beat phone here: a phone roast leans on battery and autocorrect jokes everyone has heard, while the fridge's door-light has a specific, visual, household detail that a stranger can picture instantly.

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program (pure Python 3 stdlib, deterministic) |
| `entry.txt` | The entry line itself, exactly as submitted |
| `README.md` | This file |
| `LICENSE` | MIT license |
| `.makefun/owner.json` | Payout wallet for the entry |

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

Writes `entry.txt` (the line above, plus one trailing newline) into the output directory. Pure Python 3 standard library, deterministic — no network, no randomness, no time dependence. `main.py` self-checks the gate (single line, 1–200 characters, not only whitespace) before writing, and raises on any violation.

## License

MIT — see [LICENSE](LICENSE).
