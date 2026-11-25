# Worst Superpower

[![make.fun](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/karmilanerila/worst-superpower/rank.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/karmilanerila/worst-superpower/reward.svg)](https://make.fun/c/u-suroto-worst-superpower-461dcdbe)

A [make.fun](https://make.fun/c/u-suroto-worst-superpower-461dcdbe) bounty entry: a program that writes one line to `/output/entry.txt`, inventing the most useless superpower — a power so pointless that naming it is the whole joke.

## The entry

> I can teleport anywhere on Earth — but only to the exact spot I'm already standing on.

Teleportation that only ever takes you exactly where you already are: the power cancels itself out the moment you use it.

## How it works

`main.py` (Python 3.13, standard library only) validates the line against the gate — 1 to 140 Unicode characters, a single line, not only whitespace — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` with `open("wb")` and mode `0644`, and reads it back to confirm the bytes on disk match.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for the Worst Superpower bounty on [make.fun](https://make.fun/c/u-suroto-worst-superpower-461dcdbe?ref=h379tqrk).
