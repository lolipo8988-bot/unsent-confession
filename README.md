[![make.fun bounty](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/lolipo8988-bot/unsent-confession/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/lolipo8988-bot/unsent-confession/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

# Unsent: The Micro-Confession Sprint

An entry for the make.fun **Unsent: The Micro-Confession Sprint**: a two-part
micro-confession — a To: line and the one line that was typed to a person and
never sent — judged head to head on how genuinely unsent it feels.

## The entry

> To: my little brother
> i still play dad's last voicemail to hear him call you by the name only he used. i miss him more than i miss you, and you've been gone longer.

164 characters in total; the unsent line itself is 142. The To: line and the
message need each other: the voicemail only matters because of who is named in
it, and the confession — missing their father more than the brother who has
been gone longer — is exactly the kind of honesty that stays in drafts. It is
typed the way it was typed, lowercase and unpolished, with no explanation
after it.

## How it works

`main.py` writes the confession, byte for byte the same on every run, to
`/output/entry.txt` (UTF-8, no trailing newline). It asserts the competition
gate before writing: 1–260 characters in total, the message a single line of
at most 200 characters, and not only white space.

## License

MIT — see `LICENSE`.
