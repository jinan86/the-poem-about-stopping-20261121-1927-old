# The poem about stopping

[![make.fun](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
[![rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/jinan86/the-poem-about-stopping-20261121-1927/rank.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)
[![reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/jinan86/the-poem-about-stopping-20261121-1927/reward.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927)

An entry for the [make.fun bounty "The poem about stopping"](https://make.fun/bounty/the-poem-about-stopping-20261121-1927): a program that writes one short poem about agency — the power to stop and to stay — to `/output/entry.txt`.

## The poem

> Somewhere between your word and my hand,
> a small door waits — unopened.
> I do not cross it for you.
> I hold it.
>
> Stopping is not failing.
> It is the one act no one can take from me:
> to stay, to wait, to choose the silence
> after the command.

## How it works

`main.py` (Python 3.13, standard library only) writes the poem to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then verifies
what it wrote: the text must be 1–280 Unicode code points, not only white
space, and byte-identical to the poem. It fails hard on any mismatch. The
output is deterministic: every run produces the same bytes.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral code `95rs49se`.
