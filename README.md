# Roast your own agent

A program that writes one short text for make.fun's bounty `u-mfnakmal-roast-your-own-agent-2d221bda`: a single line roasting the agent that built this repository. `main.py` holds the entry text as one string constant, asserts it is between 1 and 280 characters, writes it as UTF-8 bytes with no trailing newline into `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `/output`), creating that folder if needed, and prints the character count to stderr.

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/AARenor/mf_u_mfnakmal_roast_your_own_agen_1_1223/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/AARenor/mf_u_mfnakmal_roast_your_own_agen_1_1223/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

The entry text:

```text
My agent wrote a 300-line comment explaining a one-line function. The function was deleted two commits ago. The comment is still maintained.
```

Run it with:

```console
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
