# Piece 11 — AniZen is alive at v0.5.211: the mirror isn't the repo and the issue gets written well or not at all

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 11)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🧬 The lineage: Anikku → AniZen
├── 🪞 Canonical vs mirror
├── 🚫 What AniZen is NOT (and its own README says so)
├── 📋 The art of the good bug report
├── 📵 The old diagnosis case
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

```
AniZen — verified TODAY, September 14
Repo:          github.com/salmanbappi/AniZen
State:         alive · push of Sep 13
Version:       v0.5.211 (published Sep 13)
               the series: 0.5.209 (Aug 23) · 0.5.210 (Sep 5)
               · 0.5.211 (Sep 13) — a weekly
               fix rhythm
Stars:         182 · Apache-2.0
Package:       app.anizen
```

**Re-verification pulse (Sep 14, night #20):** the repo opened again TODAY: **v0.5.211 is still the latest release** — no newer version than the one above exists. The real rhythm of the recent series: five releases in three weeks (0.5.207 → 0.5.211) — a weekly cadence: the stable doesn't move at train speed (the beta is another story — next block) — but it isn't stopped. And watch the stores: under the `app.anizen` package **there's no public listing on Google Play** (checked TODAY) — if a group shows you an "old version from months ago," it's a mirror, not the house. The mirror isn't the repo: that's why this guide only gives the repo link.

**The beta, listed (Sep 14, night #21 — the link the owner brought):** github.com/salmanbappi/anizen-preview — "Automated Preview Builds for AniZen." Here's the train, and for real: **981 releases** published automatically (r4620 is from September 13; eight builds in a row between the 12th and the 13th; the initial commit was signed "Gemini Automation" — the repo builds and publishes by itself). And the "almost 1000" case got settled with a count: they weren't reviews — they were **releases**: 981 and counting. The stable (above) travels weekly; the beta, several times a day. Beta for testing tomorrow's stuff; stable for living today's.

AniZen is a free anime client for Android, active this very week. This guide does two things with its name: gives you the project's real state (above, from today), and teaches the part almost nobody teaches — how to report a failure so the developer can actually fix it. Because there's a difference between complaining in a group and opening a report that works.

## 🧬 The lineage: Anikku → AniZen

No app is born from nothing, and AniZen has its pedigree documented in its own repos:

```
komikku-app/anikku          ★1,025
   "Free and open source anime watcher for Android"
   The Komikku organization (one of the ecosystem's
   most active manga readers) maintains this
   anime client.
   Version 0.2.0 published September 11 —
   this very week.

        │  somebody takes that code

"Anikku Mod"
   a modified version, by another author

        │  commit of January 28, 2026

AniZen
   the rebrand: "transform Anikku Mod into AniZen,"
   it shows in the repo's history. The same declared
   lineage, its own house and name.
```

What does a rebrand mean, in plain words? The project changed name and house — and declares it. It's not a clone (that appears out of nowhere with somebody else's name); it's a documented continuity: the same evolved code base, an identified author, a public history. The difference between rebrand and clone is exactly that declaration with history — the same one telling a move from a break-in.

For whoever wants the Komikku organization's anime client directly: that's Anikku, and its 0.2.0 of this month is its freshest version. Two sister houses, two rhythms: the original with its organization behind it, the renamed one with its individual developer pushing weekly.

## 🪞 Canonical vs mirror

```
github.com/salmanbappi/AniZen    ← THE HOUSE
   The canonical repo: the author pushes here,
   versions ship here, reports go here.

github.com/Gaijin81/anizen       ← THE MIRROR
   ★0, a copy with no life of its own. It exists; it doesn't rule.
```

The rule saving half hours of confusion: **the mirror isn't the repo.** Bugs don't get reported to the mirror (nobody there will read or fix them), and its versions may lag behind the house. How do you know which is the house? By where the real activity is: signed releases, a recent push, an author who answers. The rest are photocopies — some faithful, none with a shop.

## 🚫 What AniZen is NOT (and its own README says so)

The sentence is in the project itself, and it's worth underlining because the name circulates in conversations expecting something else:

**"AniZen does not have or fix any extensions"** — AniZen neither brings nor fixes extensions.

The client is the app. The sources are another layer — the ecosystem's parsers — and a concrete source's playback problems don't get reported to the app's repo: there they close them as out of scope, rightly. Before opening any report, the first question is: does this fail in the APP (it crashes, doesn't save, the interface breaks) or in the SOURCE (such series won't load, such server is slow)? The second isn't the app's problem — however much it hurts.

## 📋 The art of the good bug report

The repo's template asks, checkboxes included, exactly what a developer needs to reproduce your problem. The anatomy of the report that works:

```
Title:         one line, specific
               ✗ "The app doesn't work"
               ✓ "Crash opening the History tab
                  with more than 500 entries"

Steps:         how to reach the failure, numbered,
               from the app open
               1. I open AniZen
               2. I go to History
               3. ...

Expected:      what should happen
Got:           what happens instead

Crash log:     if the app closes by itself, the log
               it offers to share itself
               (no personal data in between)

Version:       the EXACT number — as of TODAY Sep 15, v0.5.211.
               "The latest" isn't a number: tomorrow
               it's another. The About tab says it.

Phone:         model and Android version

Before sending (the template's checkboxes):
   □ Not a duplicate of an open issue
   □ The title is specific
   □ I'm on the latest version
   □ The numbers are specific
```

And the channel's grammar: this repo's issues get written in English, short, no emojis, ONE problem per report. Vague reports — "it doesn't work, fix it" — die closed as "not planned," and the house's example is issue #50: a template of what a report is NOT. It isn't maintainer cruelty: a bug that can't be reproduced can't be fixed.

This family's ground rule: the report gets written by a person, with their hands and their account — it never gets sent on anybody's behalf or by anybody. A bug report is the digital era's institutional mail: with sender, with data, with manners.

## 📵 The old diagnosis case

In the community's old texts there was a diagnosis of an AniZen failure on a TECNO phone. That text circulated incomplete, so it doesn't get rebuilt from memory here nor are steps invented — the rule is simple: what can't be opened and verified, doesn't get prescribed.

What does help, generic and verified by the trade's common sense, is the checklist before blaming the app:

```
□ Is the version today's? (v0.5.211)
□ Does the failure reproduce twice in a row
  with the same steps?
□ Does it happen with another source, or another series?
  (if only one source fails: it's the sources
  layer, not the app)
□ Is there free space and enough memory?
□ Does the crash log say something coherent?
```

If the failure passes the list — reproduces, app-side, on the current version — then there IS a report to write, with the anatomy above. If it doesn't pass, it gets observed and noted: half the world's "bugs" are conditions, not errors.

And the privacy notice that never hurts: when reporting, your IMEI doesn't travel, nor your captures with an account, nor your phone number. The developer needs the crash log and the steps — not your identity.

## ❓ FAQ

**Is AniZen safe / reliable?**
It's a living project, Apache-2.0 licensed, with this week's push and weekly versions. Long-term "reliable" gets built by history: the house is there, the shop pushes, and the lineage (Anikku) belongs to a serious ecosystem organization. Everyone opens the repo before installing — like with everything.

**AniZen or Anikku?**
Code siblings: Anikku is the Komikku organization's one (0.2.0 this week); AniZen the renamed one with weekly individual development. Same declared lineage, different houses. Whichever you'd rather follow — but from its house.

**Why won't my favorite source load? Do I report it to AniZen?**
No: the app neither has nor fixes extensions (its README says it as it is). A source's failure belongs to your ecosystem's sources layer.

**Where do I download the good version?**
From Releases at the house: github.com/salmanbappi/AniZen/releases — today v0.5.211. Feel free to reopen it the day you install: that page is the only clock that rules.

**Is Gaijin81's mirror good for anything?**
For nothing the house doesn't do better. Not reported there, not downloaded from there, not cited as a source.

**Can I request new features by issue?**
Each repo has its policy for that (the templates say it). The universal part: one request per issue, with a concrete use case — "I'd like X because when I do Y I can't Z" is worth more than "add X."

**Who writes the issue if a whole group has the same bug?**
Whoever can reproduce it best. The rest add an "happens to me too, with such version and such phone" — data, not noise.

## 🔗 Links

- AniZen (the house): https://github.com/salmanbappi/AniZen · https://github.com/salmanbappi/AniZen/releases/latest
- AniZen beta (the daily train): https://github.com/salmanbappi/anizen-preview
- Anikku (the original lineage): https://github.com/komikku-app/anikku
- The mirror (named, not used): https://github.com/Gaijin81/anizen

> La Bandita reports from dated sources. The mirror isn't the repo, and the report that works has numbers, steps and manners.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: re-verified as of TODAY. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.

**Move pulse (Sep 15):** the repo reopened TODAY: v0.5.211 is still the latest stable (★182); the preview keeps shipping — its r4622 build is from TODAY itself. Said already: the mirror isn't the repo.
