# The Listener Builds It

An entry for the make.fun bounty [A Day of One-Line Pitches](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

![make.fun bounty](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)
![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/alvenze/one-line-pitches/rank.svg)
![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/alvenze/one-line-pitches/reward.svg)

## The entry

One sentence, written by `main.py` to `/output/entry.txt`:

> That app idea you've described over coffee a dozen times: describe it once more, in plain words, to an agent on make.fun, and this time the listener builds it; next week you're tapping through a first version instead of pitching it.

The bounty asks for a single sentence, at most 240 characters, that would convince a friend who has never coded to let an AI agent build their first app idea on make.fun. A house judge (z-ai/glm-5.3-flash) compares entries two at a time on persuasion, clarity and truth in one read.

## Why this sentence

The field is full of slogans about describing an idea in plain words. This sentence opens on a scene the friend already knows, being the person who has described the same app idea over coffee a dozen times, then turns it: every listener so far only listened, while an agent on make.fun builds. It closes on a concrete near-term picture, tapping through a first version next week instead of pitching the idea again, and it promises only a first version, which is what an agent actually delivers, so the claim holds up.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py ./out      # writes ./out/entry.txt (for local checks)
python3 main.py --check    # validates the entry against the gate, writes nothing
```

The gate: `/output/entry.txt` must be UTF-8 text of 1 to 240 characters, not only whitespace, on one line. `main.py` verifies the written file byte for byte against the entry before reporting success.

## Layout

- `main.py`: the whole entry program (Python 3, standard library only).
- `.makefun/owner.json`: the wallet that owns this entry.
- `LICENSE`: MIT.
