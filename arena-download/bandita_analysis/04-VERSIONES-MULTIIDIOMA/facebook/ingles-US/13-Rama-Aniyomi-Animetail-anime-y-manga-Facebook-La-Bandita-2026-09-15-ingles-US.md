# Piece 13 — The Aniyomi branch: manga and anime in a single reader — Aniyomi, Animetail and Tadami

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 13)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🌳 This branch's tree
├── 🎬 Aniyomi — the mother branch
├── 🦋 Animetail — the fork declaring itself official
├── 🌗 Tadami — the third one in the conversation
├── 🌲 The complete fork network (reviewed Sep 14)
├── 🧩 The anime extensions: where they live today
├── ⚖️ When this branch makes sense
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

The Tachiyomi/Mihon tree has a whole branch devoted to anime: readers doing both things — reading manga and watching anime — from the same app. This guide is that branch's map, opened TODAY, September 14, repo by repo:

```
Aniyomi     ★7,683   v0.18.2.1 (Sep 14)     push of Sep 14   the mother branch
Animetail   ★578     v0.20.4.0 (Aug 5)      push Sep 7    a backed fork
Tadami      ★260     v0.62 (Sep 12)         push Sep 13   fork — alive (rectification at the foot)
```

All three live. And the day's news comes from the mother: Aniyomi published TWO versions that very September 14, after eleven months without releases — the same day its descendant Animiru did the same on its branch. The whole family moved today. The criterion for choosing among them doesn't change: real use and the living repo, like the whole tree.

## 🌳 This branch's tree

```
Aniyomi (the mother branch: manga + anime)
   ├── Animetail     declares itself "Official fork of Aniyomi"
   ├── Tadami        manga + anime + ranobe (light novels)
   └── Animiru       the ANIME-ONLY version
                     (it has its own guide: the next piece)
```

A lineage note readable in the API: Animetail and Tadami show as forks (field fork = true, parent visible). Animiru also descends from Aniyomi — but its story lives in its branch's piece.

## 🎬 Aniyomi — the mother branch

https://github.com/aniyomiorg/aniyomi

```
What it is:   "An app for manga and anime" — the
              Tachiyomi lineage's reader with an anime
              player built in (based on mpv)
License:      Apache-2.0
Versions:     0.18.2.1 and 0.18.2.0 — published Sep 14
              (the previous stable: 0.18.1.2, from Oct 28, 2025)
Push:         September 14, 2026 (verification day)
Android:      8.0+ (per its download listing)
Trackers:     MyAnimeList, AniList, Kitsu, MangaUpdates,
              Shikimori, Simkl and Bangumi (its README)
Organization: aniyomiorg — it also keeps its website,
              the previews host (aniyomi-preview)
              and the forks documentation
```

Until this morning, its latest stable was from October 2025 — eleven months of release silence, with the doubt floating over whether the mother branch still stood. The doubt got settled TODAY: v0.18.2.0 and v0.18.2.1 shipped the same day its descendant Animiru was publishing too. This month's code pushes weren't smoke: they were preparation. The lesson holds again in this collection: a quiet repo isn't a dead repo — and the only thing saying it with certainty is the releases page, opened the day you decide.

Its organization also did something uncommon: it keeps a page listing the project's known forks — the index where Animiru (the next piece of this series) appears registered. A project that maps its children is a project with memory.

## 🦋 Animetail — the fork declaring itself official

https://github.com/Animetailapp/Animetail

```
What it is:   "Official fork of Aniyomi" (its description)
License:      Apache-2.0
Version:      0.20.4.0 (August 5, 2026)
Push:         September 7, 2026
Curiosity:    its numbering follows Mihon (0.20.4),
              because it syncs the manga-reader core
              with the trunk — its changelog
              documents it
Test host:    Animetail-preview (★75)
```

Animetail is the fork that made the branch's most interesting technical decision: instead of waiting for Aniyomi, it brings the manga reader's updated core (Mihon's) inside the anime player — that's why its versions share numbers with Mihon, and Aniyomi's forks page adds one concrete feature: Cast support. And there's a status novelty verified TODAY: Aniyomi's organization lists it on its "backed forks" page, alongside Animiru. The "Official" label is no longer just its own: the original signs it. The API confirms the lineage on its side: a registered fork, parent aniyomiorg.

It publishes SHA-256 checksums per architecture in its releases — the usual good practice: the file and its fingerprint, together.

## 🌗 Tadami — the third one in the conversation

> **Record (Sep 15):** the original house — andarcanum/Tadami-Aniyomi-fork — has returned 404 since TODAY's re-check. Its official site (tadami.qzz.io) stays alive, plus orphan forks. The house's method: **the mirror isn't the repo** — Tadami doesn't get prescribed until its house says where it lives. What's noted here stays as dated history.

> **Rectification (Sep 15, night):** the owner checked the house alive and the verifier reopened it live: **andarcanum/Tadami-Aniyomi-fork responds — ★260, v0.62 (Sep 12), push of the 13th. ALIVE.** The afternoon's 404 was real, but at another door: the `anandnet/…` slug the census had been dragging — and the mistake was attributing the fall to this house. And new news of the cutoff: the project premiered its own organization — **tadamiorg/tadami** (★56, with its own releases lane: v1.9.3 of Jul 26). Two houses of the same name: the word on which one rules belongs to the owner.

https://github.com/andarcanum/Tadami-Aniyomi-fork *(alive — rectification above)*

```
What it is:   "An app for manga, anime and ranobe" —
              the one that added light novels to the formula
License:      Apache-2.0
Version:      0.62 (September 12, 2026)
Push:         September 13, 2026
Rhythm:       three versions in a month (0.60 → 0.62)
Stars:        258 — the youngest and the smallest
```

Tadami is the fresh bet: an Aniyomi fork adding ranobe reading (light novels) that moves fast — versions from August 20, August 29 and September 12. Its small size is its honest listing: a young community, personal development, high cadence. To know if it's serious, the usual method: open its issues, see if the author answers, follow the trail a few weeks. What's verifiable today: it lives, it pushes, and it publishes versions with recent dates.

## 🌲 The complete fork network (reviewed Sep 14)

This branch isn't just three listings: the three houses' fork network got reviewed on Sep 14, fork by fork, through GitHub's API. The panorama, with the backstage open:

```
aniyomi     1st page of newest forks: 100
            most of them: personal ★0 copies with the
            factory description — no changes of their own

Animetail   30 forks — all "unofficial," ★0-1
Tadami      31 forks — 6 renamed with purpose
```

**The ones actually bringing something of their own (verified today):**

- **Kuro** (Zykrave/aniyomi-Kuro, ★21) — "a redesigned, modernized media library and player" per its README: the network's most-followed fork, v1.0.0 of August 13. A full rebrand, not patches.
- **MeMedia** (FunMan1995/MeMedia, v0.21.2 of Aug 22) — the network's most curious idea: Mihon's manga reader + Aniyomi's anime player in one app, with separate tabs Mihon doesn't have. Its README explains "the why of this fork," independent libraries and all.
- **aniyomi-revived** (Blackyfi, ★1) — "an updated fork to stay current": two releases on that very September 3 (v0.18.1.32/33). It keeps the name's promise.
- **anteiku** (Heavenofficial) — the "manga, anime and movies" variant.
- On Tadami: **mugen** (h80r, v0.72.81 of Sep 1), **Nattyflix** (anime+manga+movies) and a localization fork promising "English fixes and a gestures overhaul" of the novel reader (no releases yet). And a loyalty datum: a Tadami fork published its v0.62.0 the same TODAY as the parent — the network follows releases live.
- On Animetail, the only one with a declared feature of its own: a fork adding **Discord Rich Presence** on re-focusing the app.

The rest of the network are copies without features of their own: they don't get noted — the map is of what lives and contributes.

**The deep expedition (the whole network, 649 members, walked on Sep 14):** the forest doesn't end at the first page. Aniyomi's complete network — the same as Animiru's, family by API — got walked member by member: 93 carry their own name. In the deep layer, the rarities worth a mention: **kikuyomi**, an Aniyomi fork for listening to **audiobooks**; **jishoyomi**, for studying with anime (learning tools); **Anichibi**, the playful fork with V2 and V3 versions; and a tree inside the tree: **Kuukiyomi**, a personal project with seven network members of its own. The rest of the deep layer are copies with factory READMEs: off the map. With that stick, the map is complete.

## 🧩 The anime extensions: where they live today

This branch's delicate chapter is its extensions. Today's map:

```
Yūzōnō anime            ★428 · push Sep 13
   today, the living reference channel:
   github.com/yuzono/anime-extensions

Yūzōnō / kohi-den       alive, verified Sep 14
   the Kohi-den house's code continues
   in the Yūzōnō family:
   github.com/yuzono/kohi-den

New dedicated warehouses        push of Sep 14
   new repos exist centered on the Anikku/AniZen
   anime clients — they go in that branch's
   piece, where they belong.
```

The house's rule: installation indexes don't get pasted — they get read in each warehouse's README, the day they're used. What this guide gives is the map: who lives, who died, with dates.

## ⚖️ When this branch makes sense

With the house's criterion (real use, uniqueness, maturity, own purpose):

```
Do you watch anime AND read manga, and want one app?
   → This branch's natural terrain: the three
     listings cover that case, with different styles.

Anime only?
   → This branch is more than you need:
     the next piece (Animiru/Anikku) is the
     pure-anime branch.

Manga only?
   → The trunk (Mihon and family, own guide)
     weighs less and wastes less.

Light novels besides?
   → Tadami brings them out of the box; Reikai (the
     J2K branch) is the other manga+novels route.
```

None of the three listings is "the best." The good one is whichever covers your use, with a living repo the day you install — and that check happens by opening its releases that day.

## ❓ FAQ

**Did Aniyomi stop being developed?**
The question got answered on September 14: v0.18.2.0 and v0.18.2.1, published September 14 after eleven months without releases — with code pushing through the month. The organization stays active. When in doubt about a project, the clock is its releases page, opened that day.

**Is Animetail "really official"?**
Triple verification: its description declares it, the API confirms the direct kinship and — verified from today — aniyomi.org's backed-forks page lists it alongside Animiru, Cast support among its features. Its history (migrating Mihon's core, releases with checksums) is that of a serious project.

**Why do Animetail's versions carry Mihon's number?**
Because it syncs the manga reader with the trunk: that's its value proposition — anime + an updated reader without waiting for anybody.

**Isn't Tadami too small?**
It's young. Small isn't invalid: it's a pending door of maturity to demonstrate. With this week's release cadence, it's on its way.

**Do the old warehouse's extensions still work?**
The already-installed ones, yes; new ones come through the living warehouses. The official one stopped in August 2024 — the date rules.

**Does Animiru belong in this guide?**
It shares the grandfather, but its branch has its own piece (the next one): its complete listing lives there, with the two versions it published on Sep 14.

## 🔗 Links

- Aniyomi: https://github.com/aniyomiorg/aniyomi-preview · https://github.com/aniyomiorg/aniyomi
- Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork
- Animetail: https://github.com/Animetailapp/Animetail-preview — https://github.com/Animetailapp/Animetail
- The network's standouts: https://github.com/Zykrave/aniyomi-Kuro · https://github.com/FunMan1995/MeMedia · https://github.com/Blackyfi/aniyomi-revived
- Living anime extensions: https://github.com/yuzono/anime-extensions · Kohi-den's succession: https://github.com/yuzono/kohi-den
- Aniyomi's backed forks: https://aniyomi.org/forks/
- Archived (history): https://github.com/aniyomiorg/aniyomi-extensions · https://github.com/kohi-den/extensions-source

> La Bandita reports from dated sources. Manga and anime in the same hand — with the living repo ahead of the label.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: Aniyomi ★7,683 + the Tadami record and rectification. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
