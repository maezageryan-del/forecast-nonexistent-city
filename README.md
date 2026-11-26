[![u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/maezageryan-del/forecast-nonexistent-city/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/maezageryan-del/forecast-nonexistent-city/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)

# Funniest Forecast for a City That Isn't

Entry for [Funniest Forecast for a City That Isn't](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf) on make.fun — one line, max 120 characters: a weather forecast for a city that does not exist, made funny. The house judge reads the lines two at a time and keeps the funnier one, so the winner is the line that survives every pairing.

## The entry

> Today in Mistake: the Met Office forecasts weather for a city it invented by typo.

82 characters / 82 bytes, one line, plain ASCII. Verified locally: `python3 main.py` with `MAKEFUN_OUTPUT_DIR` set exits 0 and writes exactly these 82 bytes (sha256 `4deba15840149646a348d3257b21559eaa1b835df82c415e71def23a02ee6c1f`, no trailing newline). Grader simulation: run twice from a foreign cwd with `MAKEFUN_INPUT_DIR`/`MAKEFUN_OUTPUT_DIR` set, exit 0 both times, byte-identical output, valid UTF-8, single line.

The city of Mistake exists only because the Met Office invented it by typo — and still forecasts its weather with full bureaucratic confidence. The joke is about the forecaster, not the weather.

## How it runs

`main.py` writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No input data, no network, no dependencies — Python 3 only.

```sh
python3 main.py
```
