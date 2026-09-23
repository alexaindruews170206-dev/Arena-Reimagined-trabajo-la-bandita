# Piece 15 — The J2K branch: the grandfather returned — tachiyomiJ2K, Yōkai, Rokku, Reikai and the ghost Hayai showed up

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 15)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🌳 This branch's tree
├── ⚡ tachiyomiJ2K — the grandfather woke up
├── 👻 Yōkai — the trunk on active pause
├── 🪇 Rokku — the practical-maintenance fork
├── ⛩️ Reikai — manga and novels in one library
├── 🐇 Hayai — the ghost has a house (and it opens)
├── 🌲 The complete fork network (reviewed Sep 14)
├── 🧬 The branch's lesser cousins
├── 📜 The history explaining this branch
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

This is the beloved-interface branch: the one born of tachiyomiJ2K — the fork that redesigned Tachiyomi — and birthed a whole family. The first thing to say is the big news: **tachiyomiJ2K shipped versions again in August 2026 after two and a half years of silence.** And the second: **Hayai — the project that for months was a ghost with no accessible repo — today has a public house and can be opened.**

```
tachiyomiJ2K  ★5,383  v1.8.1 (Aug 15, 2026)  the grandfather, back
Yōkai         ★1,883  v1.10.1 (Sep 4)     yesterday's push (Sep 14) — the trunk
Rokku         ★51     v1.7.1 (Aug 29)     the maintenance one
Reikai        ★27     v0.3.2 (Sep 4)      manga + novels unified
Hayai         ★41     v1.13.0 (Apr 10)    the one no longer a ghost
```

All the listings were opened and verified TODAY, September 14. Where the maintainers' personal lives explain the projects' rhythms, it gets told the way they told it: quoted, dated, no gossip.

## 🌳 This branch's tree

```
tachiyomiJ2K (the redesigned interface)
         │   v1.7.4 (Jan 2024) → two years of silence
         │   → v1.8.0 and v1.8.1 (August 2026): IT CAME BACK
         │
         ├── Yōkai        null2264's personal fork
         │     ├── Rokku    a fork of Yōkai: maintenance
         │     ├── Reikai   started in Yōkai, rebased on Mihon
         │     └── Hayai    J2K-based, manga + novels
         │
         ├── yomu         J2K-based, small
         └── TachiyomiDNP small variant, active in August
```

## ⚡ tachiyomiJ2K — the grandfather woke up

https://github.com/Jays2Kings/tachiyomiJ2K

```
★5,383 · Apache-2.0
v1.7.4 → January 2024 (the old era's close)
v1.8.0 → August 9, 2026 "Warning: Funny numbers ahead"
v1.8.1 → August 15, 2026 "Wait, there's more?"
```

Its history in two acts: it was THE fork of the golden era — the one that invented the visual redesign half the family inherited — and then went quiet for two and a half years, until August 2026, when it dropped two versions in one week with its usual humor in the titles. The community considers it the father of mass library migration: it was the first to move whole libraries between readers.

Its return doesn't revive it as a daily candidate — two versions aren't a rhythm — but it does put it back on the map as living history: the grandfather didn't die, he was traveling. Whoever wants the "pure" J2K experience, its house is open again, with this year's versions.

## 👻 Yōkai — the trunk on active pause

https://github.com/null2264/yokai

```
★1,883 · Apache-2.0 · yesterday's push (Sep 14)
v1.10.0 and v1.10.1 (both on September 4)
Support: extension-lib 1.6 · Android 8+ (its release note)
```

Yōkai is null2264's personal fork: it took the J2K interface and holds it up alone. Its own maintainer explained it in the September version's note, with honesty worth quoting: he stepped back from his projects due to burnout, thesis and work on top, hoping to return "before New Year's" and reviewing contributions now and then. He called his own release "fairly unpolished." And the same note opens with an all-caps warning worth respecting: "BACKUP YOUR DATA."

What the Sep 14 datum said: the branch isn't abandoned — the repo pushed yesterday (Sep 14). What it also says: it's a one-person project with a life on top, and that life will set its rhythm. The whole branch's lesson comes from here: maintainers are people; burnout is real; and a changelog's honesty beats a fake roadmap.

## 🪇 Rokku — the practical-maintenance fork

https://github.com/rokku-app/rokku

```
★51 · Apache-2.0
v1.6.1 (Aug 15) · v1.7.0 (Aug 23) · v1.7.1 (Aug 29)
— three versions in two weeks: a firm cadence
Born of: Yōkai, to keep it current with the
extensions ecosystem and dependencies
```

Rokku exists for the world's most practical reason: when Yōkai paused, somebody decided to keep the experience alive and current — modern extensions, performance fixes, the dirty necessary work. Its August notes concentrate on exactly that: performance and download tuning, compatibility with the modern extension library, and interface care inherited from home — the work that never makes screenshots but keeps an app alive.

It's the branch's smallest listing in stars and the busiest in fixes. The starry sky measures fame; cadence measures the shop. And there's more living-shop signal: Rokku has its own nightly channel (rokku-nightly) with almost daily builds — the last one seen was from yesterday. *(Re-verified on Sep 15: the latest nightly is r7091, of Sep 13 — the cadence holds; the date, updated.)* When a house compiles at night, it works by day.

## ⛩️ Reikai — manga and novels in one library

https://github.com/unseensnick/Reikai · Site: https://reikai.app

```
★28 · Apache-2.0 · push of Sep 14 (verification day) · v0.3.2 (Sep 4)
v0.3.2 (Sep 4) · v0.3.1 (Aug 9) · v0.3.0 (Jul 16)
Born of:     it started as a fork of Yōkai — GitHub's graph
             still notes it that way — and its project
             says the code was later rebased
             onto Mihon
It has:      a separate FOSS version (no crash reporting or
             analytics) — reikai-foss in its releases
```

Reikai is the branch's most differentiated idea: ONE library where the same manga and light-novel series live together. Its declared features: multi-source grouping (it folds the same series from different sites into one entry), manual merging when titles don't match, merged reading with a unified chapter list, shared tracker sync across the group, and a first-class novel library with LNReader reader support.

Its philosophy, in its author's words: built first for their own daily use — development is sporadic and features follow their tastes. That honesty defines what it is: a very well-documented personal project (its complete website confirms it), not a product with team promises.

## 🐇 Hayai — the ghost has a house (and it opens)

https://github.com/HayaiApp/hayai

```
★41 · Apache-2.0
v1.13.0 (April 10, 2026) · push of Sep 6
What it is: "Hayai is an Android reader based on
TachiyomiJ2K with manga and light novels"
(per its own description)
```

Here's this branch's surprise: for months, Hayai was the ghost project — mentioned in lists and in other projects' changelogs, its repo inaccessible, impossible to evaluate. Today the repo opens, can be read, and says what it is: J2K-based, manga and light novels, an April version and last month's activity.

What's verifiable today: the house exists, the license is declared, there's a tagged release. And its README — read in full TODAY — spells the recipe out with rare honesty: J2K architecture declared as base and source of truth, adult sources support rebuilt over TachiyomiSY's contracts, novels plugins in LNReader style, and "defensive import" of old Hayai's database — the ghost era's archive still caring for whoever used it. What's still unknown: whether its development is sustained — its latest version is five months old, though its repo moved last week. New listing, open tracking: the ghost gets a month of public life before any verdict. It's the house's rule — the rumor gets checked at the project's house, and sometimes the house shows up.

**And the Hayai family grew on the side nobody watched:** the same org published **HayaiTTS** (★39) — an OFFLINE neural text-to-speech engine for Android: it registers across the whole system and brings 186 voices (Piper and Kokoro, via sherpa-onnx). Latest version: 2.5.1, of June 15. The puzzle's missing piece: read the novel… or hear it. For whoever reads light novels on the bus, this closes the circle.

## 🌲 The complete fork network (reviewed Sep 14)

The five projects' networks got opened fork by fork today through GitHub's API — including J2K's, which hides the rich relative almost nobody names:

**In J2K's network:**

- **TachiyomiS97** (Saud-97, ★125) — this branch's prince and its most-followed fork: "a faster version of Tachiyomi." Its own features, from its README: global updates up to 5× faster, downloads up to 3× faster, multi-device progress via trackers (experimental), auto-download of the next chapter while you read, and URL search in the global search. And history repeats: v1.7.5 of August 1, 2026 after going silent since January 2024 — the grandfather's pair: both woke this year.

**In Yōkai's network (100+ forks):**

- **yurei** (NotBlankyu, v1.10.1 of Aug 21) — the ambitious variant: manga + webnovels, a text mode rendering the chapter as text instead of images, an NSFW filter inherited from SY, and local reading that now reads ComicInfo.xml per chapter.
- **yokai-T** (KakarottoCake, v1.0.2 of Jul 4) — streaming and torrent downloading, its own bet.
- A fork with **custom folders** (multi-series collections with ordering and backup) pushed on Sep 14 (the day's record) — no releases yet.
- The full network with names of its own: kagura, Mekuri (local-first), Miko, Karasu, and a Komga+gallery variant. Plus the factory ★0 copies, which are the majority.

**And the small networks:** Rokku has 3 forks (all ★0, one pushed on Sep 14 — a newborn network); Reikai has 5, with **Nekoumy** (Zykrave, the same author as Kuro: "a library for manga and novels," push of Sep 12); Hayai has 4, all ★0 copies. The younger the house, the smaller its wake — for now.

**The deep expedition (J2K: 999 members · Yōkai: 125 — walked on Sep 14 down to the leaves):** in these networks' deep layer, the living with a proposal of their own: **yurei** already has an active child — the fork for **MIUI/HyperOS** users, fixing what Xiaomi's factory optimization gets in the way of, and on v1.11.0. On the Yōkai line, named and pulsing leaves: **Miko**, **Karasu**, **kagura**, **Mekuri** (local-first), **shuo** (novels) and **MiruKan** (with a version of its own, v1.0.1 of May). And the Hayai shop completes: a nightly channel with this week's builds (hayai-nightly) *(re-verified on Sep 15: the channel's latest dated build is r6674, of Sep 6)* next to the **HayaiTTS** listed above. The rest of the deep layer are copies without contributions: off the map.

## 🧬 The branch's lesser cousins

To complete the map, the small repos today's search brought — named with their real size:

```
yomu (HugoFMiranda)          ★3   J2K-based, push Jul 2026
TachiyomiDNP                 ★4   a variant, push Aug 16
Hiirbaf/yokai                ★3   a fork of Yōkai, push of Sep 13
```

None reaches the maturity door to be recommended as a daily alternative — but they get named because existing is also information, and because any of them can be the next Rokku (which six months ago was just as small). The copies with no active owner, not even that: copies with a clock.

## 📜 The history explaining this branch

This branch is the ecosystem's best kind of history: the inheritance getting split up.

```
2019–2023   tachiyomiJ2K defines the modern
            interface of the free manga reader.
            Mass library migration is born here.

Jan 2024    The original Tachiyomi closes (legal pressure).
            J2K goes quiet. The J2K interface's
            users are left orphaned.

2024–2025   Yōkai picks up the interface's inheritance.

2026        The family branches out of necessity:
            Rokku maintains, Reikai joins formats,
            Hayai steps out of the shadow, and the
            grandfather himself returns in August.
```

Five living projects where there was one silence. The branch's lesson: when a shop closes, it isn't the end of the trade — it's the tools getting handed out.

## ❓ FAQ

**Did tachiyomiJ2K "really" come back or was it a one-off?**
Two versions in one week of August, with tags and notes — that's a real return of activity. Whether there'll be cadence, autumn will say; its releases page is the clock.

**Yōkai or Rokku if I came from the J2K interface?**
Yōkai is the trunk with the original maintainer on active pause; Rokku is the maintenance branch with an August cadence. The practical difference is in its rhythm — and both get opened the day you decide.

**Does Reikai replace my normal manga reader?**
It doesn't come to replace: it brings the feature almost nobody has — manga and novels in ONE library, the same series grouped even if it comes from different sources. If you don't read novels, it's more app than you need.

**So Hayai was a myth?**
It was a real project with no door. Today the door exists, the license is declared and there's a tagged version. The myth became history — and this correction is exactly why guides carry dates.

**Which has the branch's freshest version?**
Yōkai and Reikai: September 4. Rokku: August 29. Hayai: April 10. J2K: August 15. Numbers expire — each one's releases page doesn't.

**And the "faster" fork (TachiyomiS97)?**
It's J2K's network's most-followed fork (★125) and its promises are written in its README: it revived in August 2026 with update and download optimizations. The rule doesn't change: any fork's performance numbers get checked in your own use — and its releases page, opened the day you decide.

**The lesser cousins (yomu, DNP)?**
Named, measured, not recommended: they don't pass the maturity door yet. Tomorrow may be another story — it'll be said, dated.

**Why so much "its own maintainer says" in this guide?**
Because in a branch of personal projects, the maintainer's word IS the primary source: Yōkai explained its pause, Reikai explains its philosophy, J2K signs its returns with humor. Quoting them with dates is verifying them.

## 🔗 Links

- Yōkai: https://github.com/null2264/yokai
- tachiyomiJ2K: https://github.com/Jays2Kings/tachiyomiJ2K
- Reikai: https://reikai.app · https://github.com/unseensnick/Reikai
- Rokku: https://github.com/rokku-app/rokku
- Hayai: https://github.com/HayaiApp/hayai
- Primos: https://github.com/theordinaryguy23/TachiyomiDNP · https://github.com/HugoFMiranda/yomu · https://github.com/cuong-tran/tachiyomiJ2K
- Network standouts: https://github.com/NotBlankyu/yurei — https://github.com/Saud-97/TachiyomiS97 · https://github.com/KakarottoCake/yokai-T · https://github.com/Zykrave/Nekoumy

> La Bandita reports from dated sources. The grandfather returned, the ghost has a house — and the whole branch got verified today.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: Yōkai ★1,883 (the 14th's push), Reikai ★28 (v0.3.2 of Sep 4), the small networks re-dated. The J2K and its 999-member network, checked on its day (Sep 14). Full record: Register #71.
