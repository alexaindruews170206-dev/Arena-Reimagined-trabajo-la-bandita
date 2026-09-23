# Piece 16 — The SY/Komikku branch: the classic fork and the adopted child with an organization — TachiyomiSY and Komikku

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 16)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🌳 This branch's tree
├── 📗 TachiyomiSY — the classic that carries on
├── 📘 Komikku — the adopted child with an org
├── 🔀 The two schools of fork (and the counterexample)
├── 🧩 This branch's extensions
├── 🌲 The complete fork network (reviewed Sep 14)
├── 🏗️ The infrastructure: previews and sync
├── ⚖️ SY or Komikku: how to decide with criteria
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

This is the classic-style branch: TachiyomiSY — the fork that added the extra functions to the original Tachiyomi, the old guard's classic "SY" — and Komikku, the project born of that lineage that grew into having its own organization. Verified TODAY, September 14:

```
TachiyomiSY       ★4,143   1.13.2 (Jul 13)   push Sep 13   the classic
TachiyomiSYPreview ★484    previews host     push Aug 25
Komikku           ★4,717   v1.14.1 (Jul 17)  push Sep 11   the adopted child
komikku-preview   ★248     testing channel   push Sep 10
```

They are the ecosystem's two big living ones of the SY style — and the comparison between them is the lesson on how a fork becomes a project with a life of its own.

## 🌳 This branch's tree

```
TachiyomiSY (jobobby04)      the living classic
   ├── TachiyomiSYPreview     a test-build host
   └── Komikku (komikku-app)  a new repo inheriting the
               ├── komikku-preview  code that grew with an org
               ├── Anikku           its anime client
               └── (its branch has its own piece in this collection)
```

A technical detail readable in the API: Komikku does NOT show as a fork (it's a new repo); its own documentation declares the lineage. That's the difference between GitHub's graph and reality — that's why both get read.

## 📗 TachiyomiSY — the classic that carries on

https://github.com/jobobby04/TachiyomiSY

```
★4,143 · Apache-2.0
Version:      1.13.2 (July 13, 2026)
Push:         September 13 — YESTERDAY's code
What it is:   the classic fork: the trunk's reader
              with the SY style's extra functions
              (more sources by default, more reading
              tweaks, the "complete" experience)
```

SY is the ecosystem's fork with the most continuous history: it existed before the original's closing, survived January 2024, and keeps pushing code — it did on Sep 13, the record of its verification. Its rhythm isn't monthly releases: its latest stable is from July and its code has moved since then. The veteran's pattern: less version noise, more silent maintenance.

Its identity notice: **the living SY is jobobby04's** — the day you look for SY, install from its repo, the one pushing yesterday's code. The name isn't enough; the owner is.

Its test-build host: jobobby04/TachiyomiSYPreview (★484) — experimental versions for the curious and bug reporters, not the daily route.

## 📘 Komikku — the adopted child with an organization

https://github.com/komikku-app/komikku

```
★4,717 · Apache-2.0
Version:      1.14.1 (July 17, 2026)
Push:         September 11
What it is:   the SY lineage's manga reader that was
              born as a new repo and grew into a
              full organization:
              - komikku-preview (★248): testing channel
              - Anikku (★1,028): its anime client
              - its own community translations
```

Komikku is the case study of how a fork becomes an institution: it inherited the lineage's code, was born with its own house, and built structure — an org, a previews channel, a sibling anime project, a translation community. Its versions run on a regular cadence (1.14.1 in July, with a development branch pushing since then).

In stars it already passes the classic SY (4,717 vs 4,143). That isn't a quality verdict — it's a community datum. What IS a verifiable verdict: its shop moves (the Sep 11 push) and its infrastructure is this branch's most complete.

## 🔀 The two schools of fork (and the counterexample)

This branch has the ecosystem's three archetypes, living in the same house:

```
SCHOOL 1 — keeping the last name
TachiyomiSY: continues the classic fork, keeps
the name and the style, evolves with care.
Its value: continuity. Its user: whoever wants
the usual thing, alive.

SCHOOL 2 — growing with a new house
Komikku: inherits the code, baptizes its own name,
builds an organization and even an anime branch.
Its value: evolution with structure. Its user:
whoever wants the project moving the most
in structure.
```

## 🌲 The complete fork network (reviewed Sep 14)

On Sep 14, fork by fork, SY's network got opened (238 forks, three pages, two orderings) and Komikku's (200 forks). It's the ecosystem's richest network — and the one best showing the difference between copying and contributing:

**In SY's network:**

```
Chai (Smol-Ame)          ★12 · push Aug 22
   the most-followed living fork: a "lewd" filter to
   hide the spicy stuff from the library, search
   by tracking state and manga info editing —
   no releases yet (code only)

SY with Discord RPC (jeryjs)  ★10 · preview-43 (Jul 23)
   Discord presence while you read

Faxyomi                  ★4 · v9 (Aug 29)
   "to have TWO SYs on the same phone" —
   the ecosystem's most honest use case

Shinyomi ★5 (1.0.0, May 25) · Mizu ★2 · Dyomi
(Sep 8 build) · Fukuro (Sep 4 push) · a desktop
variant under construction · the SyncYomi team's
fork (Sep 10 push)
```

**In Komikku's network:**

```
Houri (PineappleTwilight)  ★10 · v1.22.1 (TODAY Sep 15) *(v1.22.0 shipped on the 14th — two days in a row: the cadence holds)*
   the most active fork with its own proposal:
   REREAD support with trackers connected
   (rereads per manga), an improved Discord RPC
   respecting subcategories, default filters per
   source and an improved opt-in feed

komikku_img_upscale · r10647 (Sep 13)
   page image upscaling — plus three
   more forks of the same topic (upscaling/scaling)

mikku (Syncthing built in) · komikku with
page bookmarks · kokomikku (KOReader) ·
a fork with its own tracker · komikku2 (Sep 13)
```

The fine datum: Houri's author also keeps an Anikku fork (anikku-pineapple) — one dev weaving between both branches of the Komikku house.

**The layer the graph hides (five houses verified on Sep 14 at the groups' request)**

These five do NOT appear in SY's or Komikku's direct fork network: they're rebased forks with new houses, or grandchildren — invisible to the parent's graph. They got opened one by one, their own options read from their READMEs:

```
ShinKu (Harrys-HQ)         ★31 · v2.6.9 (Sep 13)
   "a modernized, renamed fork of
   TachiyomiSY/Mihon" — weekly cadence.
   Its thing: natural-language search with
   assisted discovery ("Vibe Search" and
   "For You"), a reading statistics card,
   ambient audio matching the genre, an
   interface shifting color with the cover,
   automatic categorization, a dead-sources
   scanner to migrate your manga, and a menu
   for migrating failed updates.

MihonSY (ruzhe85)          ★13 · v1.0.7 (Aug 22)
   a Chinese fork of SY (its README is in Chinese).
   Its thing: tap-scroll in webtoon with
   adjustable distance (½, ¾ or full
   screen) and tunable animation, automatic
   webtoon detection by image resolution,
   Komga progress synced chapter
   by chapter (not batched), a light Lanczos3
   image enhancement —no heavy models— and
   native 1:1 resolution.

Pokomi (pokedo0)           ★11 · v1.0.9 (Aug 16)
   a Komikku fork with one clear idea of its own:
   "Author Following" — subscribe to follow
   your authors. It inherits Komikku's unique
   features.

NEXUS (the-nexus-app)      ★3 · v1.2.1 (Sep 8)
   a Komikku fork: suggestions reading the
   source site's own recommendations, hidden
   categories WITH authentication to open
   or delete them, and on-the-fly chapter
   and page bookmarks.

bchan (geograms)           ★5 · v1.12.1 (Jun 19)
   "a simplified fork of TachiyomiSY/Mihon":
   Keiyoushi extensions factory-installed,
   webtoon reading by default, downloads that
   pause and resume on their own across networks,
   and flat, predictable file names.
```

And the second generation delivered too: **Yomiko** (petalya, ★8, push of Sep 12), the Discord-RPC fork's daughter — the chain doesn't break.

The method's lesson stays in the text: the parent's fork list doesn't show the rebased ones or the grandchildren. Mapping the tree means walking the chains and reading each README's credits — and when somebody names a house that didn't come up in the sweep, the link rules.

**The deep expedition (SY: over 1,000 members · Komikku: 244 · anikku: 71 — all walked on Sep 14):** the second generation already compiles: **leassapie/houri**, Houri's child, with its own version v1.21.0 (August 30) — the Houri → its child chain, alive. **Yomiko**, the Discord-RPC fork's granddaughter — a dated nuance (corrected on Sep 15 by the house's audit): the house showed pushing, but its stable version (v.1.8.1 — dated correction on Sep 15 via REST and git: release of Sep 25, 2025, not Aug 2026; and genealogy CERTIFIED by fork: Yomiko ← SY-Discord-RPC ← TachiyomiSY — the SY line, not J2K). Let the date say what the date says. ShinKu, NEXUS, MihonSY, Pokomi and bchan are leaves for now: when they root, they get noted with a date.

## 🧩 This branch's extensions

The SY/Komikku branch keeps the most warehouses alive. The Sep 14 batch's map (its complete guide has its own piece in this collection):

```
Keiyoushi              the main hub
   the ecosystem's most-used warehouse: it declares
   support for Mihon, TachiyomiSY and Komikku
   (complete guide: piece 04 of this collection)

Yūzōnō manga           ★890 · a MIRROR of Keiyoushi
   an automatic mirror, no contributions of its own —
   discontinued (not archived): today's "push" is the
   mirror syncing, not its own life. For manga,
   the house is Keiyoushi

cuong-tran/manga-repo  ★445 · push of Sep 14
   "Extensions for Komikku / Mihon & forks"
   (its description)

"cursed" shelves       ★185/★158  name yes, index no
```

Keiyoushi's notice remains the ecosystem's key: if your extension list comes up empty with "Outdated app," your app is no longer compatible — update it from its repo. And the moment's technical convention (KeiSource 1.6) gets told in the extensions guide: it's the reason old apps stop seeing new extensions.

## 🏗️ The infrastructure: previews and sync

Two pieces this branch shares with the ecosystem, worth knowing:

- **The previews hosts** (SYPreview, komikku-preview) are each project's testing channel: experimental builds for whoever reports bugs. Installing them is a tester's decision, not a daily user's.
- **tracker-extensions** (komikku-app, ★14): the Komikku house's tracker extensions — trackers get served apart from the core, as extensions (verified Sep 14).
- **SyncYomi** is library sync between devices and between forks of the family — useful exactly for this guide's gesture: if you test SY and Komikku, your progress can follow you between both. Its complete listing, in this series' tools collection.

## ⚖️ SY or Komikku: how to decide with criteria

The house's four doors, applied without "betters":

```
Continuity           if you came from the everyday SY,
                     jobobby04's is the same house with
                     the lights on.

Structure            if you value an org, a previews channel,
                     a sibling anime project and
                     a release cadence: Komikku.

Compatibility        both read the same main warehouses
                     (Keiyoushi declares it
                     for both). The tiebreaker
                     isn't in the sources: it's in the
                     use you'll give it.

Maturity             both pushed this week.
                     Neither passes the door with
                     hands in its pockets.
```

The rest is personal taste — and real use: whoever uses it and checks it. The stars (4,717 vs 4,143) are the day's fame datum, not a recommendation.

## ❓ FAQ

**Are SY and Komikku the same code?**
They share a lineage, not a repo or owner. The API doesn't declare Komikku a fork; its own documentation tells where it's from. Declared kinship, separate houses.

**Which has more sources?**
Sources live in the warehouses (Keiyoushi, Yūzōnō…), not in the app — and the main warehouses declare support for both. The real tiebreaker is the app fitting your hand better.

**And the repos with the same sign that no longer move?**
They don't get noted: the map is of the living. The practical rule: install SY from jobobby04's repo — and nobody else's.

**And the repos advertising themselves as "the 2026 reader"?**
The Sep 14 scan caught another brood of the known pattern: new repos with serious projects' names — a "komikku-scans," a "Neko-Manga-Pearl" borrowing the real MangaDex fork's name, a "kumo-surreal" calling itself optimized Mihon — all three created the same day, with almost identical stars and the year "2026" in the description. Meanwhile the brood grows: a "weeb-index" ("Best Otaku Directory 2026") and a "manga-zen-reader" ("Best Alternatives 2026") repeat the suit with the same fake stars. Named without linking: it's SEO to harvest the downloads of whoever searches in a hurry. The real project doesn't need to put the year in the name.

**And the Japanese-sounding forks people mention (like "ShinKu")?**
Listed above, with a date: ShinKu exists (★31, v2.6.9 with weekly cadence, of the SY/Mihon lineage) — it didn't show in the previous re-check because rebased forks and grandchildren don't appear in the parent's fork network. Two rules remain for the reader: a name without a link neither verifies nor discards — and the link, always, closes the case.

**Did Komikku come from SY or from Tachiyomi?**
Its documentation declares the ecosystem lineage; GitHub's graph shows it as a new repo. Both things are true: declared inheritance, own house.

**Can I have both installed?**
Technically yes (different packages). The useful question is the usual one: what does the second add that the first doesn't cover? If the answer is "nothing," one reader is enough.

**And Anikku?**
It's the Komikku organization's anime client — it has its own guide in this collection (the pure-anime branch). The family extends: manga (Komikku), anime (Anikku), and the renamed AniZen on its separate branch.

**Which shipped the most recent version?**
Neither in September: SY 1.13.2 and Komikku 1.14.1 are from July — with both moving code this month. The push doesn't re-tag: the release gets opened the day you install.

## 🔗 Links

- Komikku: https://github.com/komikku-app/komikku-preview · https://github.com/komikku-app/komikku
- TachiyomiSY: https://github.com/jobobby04/TachiyomiSY — https://github.com/jobobby04/TachiyomiSYPreview
- Network standouts: https://github.com/PineappleTwilight/houri · https://github.com/jeryjs/TachiyomiSY-with-discord-RPC — https://github.com/Smol-Ame/Chai · https://github.com/Viel0320/komikku_img_upscale · https://github.com/nas3ts/mikku
- The layer the graph hides: https://github.com/ruzhe85/MihonSY — https://github.com/Harrys-HQ/ShinKu · https://github.com/pokedo0/Pokomi · https://github.com/the-nexus-app/NEXUS · https://github.com/geograms/bchan
- Branch warehouses: https://github.com/yuzono/tachiyomi-extensions · https://github.com/keiyoushi/extensions · https://github.com/cuong-tran/manga-repo
- Sync: https://github.com/syncyomi/syncyomi
- Sister guides: extensions (piece 04) · the trunk's forks (piece 06) · pure anime (piece 14) of this collection

> La Bandita reports from dated sources. Two schools, one lineage — and the sign, you know, installs nothing.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: Houri's v1.22.1 of TODAY, manga-repo ★445, SY/Komikku re-counted. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
