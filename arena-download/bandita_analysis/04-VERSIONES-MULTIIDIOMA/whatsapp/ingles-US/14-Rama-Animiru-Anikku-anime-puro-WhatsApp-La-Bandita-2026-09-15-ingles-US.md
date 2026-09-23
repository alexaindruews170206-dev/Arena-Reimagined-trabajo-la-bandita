# Piece 14 — The pure-anime branch: Animiru and Anikku — the clients that took the manga off their backs

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 14)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🌳 This branch's tree
├── 🍥 Animiru — the anime-only born of Aniyomi
├── 📺 Anikku — the Komikku organization's anime
├── 🌲 Both forks' network (reviewed Sep 14)
├── 🧩 These clients' extensions (the day's novelty)
├── ⚖️ Pure anime or anime+manga: how to decide
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

There's a branch of the anime tree that made the opposite decision to Aniyomi's: instead of adding manga to the player, they TOOK the manga out to keep only the anime. This guide opened, on September 14, the houses of that branch:

```
Animiru   ★864    v0.20.0.1 (Sep 14)   Aniyomi's anime-only fork
Anikku    ★1,028  v0.2.0 (Sep 11)           the Komikku organization's anime
```

The day's datum: **Animiru published two versions this very morning** (0.20.0.0 and 0.20.0.1). And on the Anikku front, there are extension warehouses dedicated to it with today's activity. The tree's small branch is, this week, the one that moved the most.

## 🌳 This branch's tree

```
Aniyomi (manga + anime)
   └── Animiru      it took the manga off: ANIME only
         └── AnimiruTv  a variant for Android TV

Komikku (manga, with an organization)
   └── Anikku       its anime client
         └── anikku-preview   the testing channel
```

Two different roads to the same destination: a free anime client. Animiru came out of the Aniyomi branch; Anikku came out of the Komikku organization. They aren't direct competition by birth — they're two families arriving at the same counter.

## 🍥 Animiru — the anime-only born of Aniyomi

https://github.com/Quickdesh/Animiru

```
What it is:   an Aniyomi fork that removes the manga
              part to be an ANIME-ONLY app
License:      Apache-2.0
Versions:     0.20.0.1 and 0.20.0.0 — published Sep 14
              (the previous: 0.19.8.1, from Aug 9)
Android:      8.0+ (its download listing)
Player:       built on mpv, configurable
Trackers:     MyAnimeList, AniList, Kitsu, Shikimori,
              Simkl, Bangumi and Hikka (its README)
Stars:        862
```

Three things make Animiru special within the tree:

**One: the official registration.** Animiru appears listed on the page of forks kept by Aniyomi's own organization (aniyomi.org/forks/Animiru). It isn't a clone that appeared from nowhere: it's a fork registered in the mother project's index — the difference between the recognized house and the ownerless shack.

**Two: the design decision.** They took the manga out on purpose. Less app, less weight, one job well done. For whoever never reads manga, it's exactly the right tool — and for whoever reads both, it's half a solution.

**Three: today's rhythm.** Two versions published the same morning of today. Whatever its author is adjusting, they're doing it right now — the repo feels alive from the front page.

Its strain has its own twig: AnimiruTv exists (an Android TV fork) plus minor copies with no activity. The canonical listing is Quickdesh/Animiru — the one keeping the rhythm and the registration.

## 📺 Anikku — the Komikku organization's anime

https://github.com/komikku-app/anikku

```
What it is:   "Free and open source anime watcher
              for Android" — the anime client of
              the organization keeping Komikku
License:      Apache-2.0
Version:      0.2.0 (September 11, 2026)
Push:         Sep 14 (verification day)
Testing channel: anikku-preview (★112, push Sep 10)
Stars:        1,028 — the biggest of this branch
```

Anikku is the institutional bet: it isn't a one-person project, it's the anime piece of an organization already proving its craft with Komikku (one of the ecosystem's most active manga readers, ★4,717). Its 0.2.0 of this week puts it in the young-but-sponsored phase: there's an org behind it, a previews channel, community translations.

The name — careful with the resemblance: a whole family of clients with the "Ani-" root exists (Aniyomi, Animetail, Animiru, Anikku, and the renamed AniZen, which has its own guide). Each with its repo and its owner. The name inherits nothing; the repo explains everything.

## 🌲 Both forks' network (reviewed Sep 14)

The living-with-a-proposal in both networks (reviewed Sep 14, fork by fork):

- **AnimiruTv** remains the canonical Android TV variant.
- **Vidi** is the only Animiru variant with its own fresh builds: v0.19.12, from September 4.
- In anikku's network: the **macOS port** is still under construction (an August push) and **anikku-pineapple** weaves with Houri on the manga branch — the same author on both branches of the Komikku house (see the SY/Komikku guide).

The rest of both networks (32 and 68 forks) are copies without declared features of their own: they don't get noted. The map is of what lives and contributes — and the day somebody contributes, they'll enter with a date.

## 🧩 These clients' extensions (the day's novelty)

An anime client with no sources does nothing — and this week the branch premiered its own warehouses. Verified today:

```
salmanbappi/extensions-repo      ★40 · TODAY's push (re-verified Sep 15)
   "An anime extension repository
   dedicated to Anikku" — per its description

salmanbappi/aniyomi-extensions   ★15 · push Jan 12
   "Extensions for Anikku / Aniyomi & forks"
```

The detail connecting guides: those warehouses' author is the same developer as AniZen — the rebrand of Anikku Mod that has its own guide in this collection. There's a small ecosystem building itself around the Komikku organization's client: client, previews channel, and extension warehouses. That, in diapers, is how a serious branch is born.

The historical context, dated: Aniyomi's official anime warehouse archived in August 2024 and the community one (Kohi-den) in May 2026 — these new repos existing is the ecosystem's answer to those gaps. Installation indexes don't get pasted here: they get read in each warehouse's README, the day it's used.

## ⚖️ Pure anime or anime+manga: how to decide

```
Do you watch anime and NEVER touch manga?
   → Animiru or Anikku: the app weighs less,
     the interface doesn't bother you with the half
     you don't use.

Do you watch anime and read manga, depending on the mood?
   → The previous branch (Aniyomi/Animetail/Tadami):
     both things in one hand.

Anime on the TV?
   → AnimiruTv exists — with the usual warning:
     a small fork, verify it the day
     you try it.

Already using Komikku for manga?
   → Anikku has the same team's logic:
     the family shows in the interface.
```

Today's two listings pass the house's doors: real use (active communities), uniqueness (pure anime is their niche), maturity (this week's releases, an org structure in one case) and own purpose (taking the manga out IS the purpose — it isn't cosmetic).

## ❓ FAQ

**Is Animiru just "Aniyomi without manga"?**
Its base is Aniyomi and that's its difference — but it adds details of its own (the tracker set includes Simkl and Hikka, the mpv player gets tuned in every version). Two versions in one morning say the "just" is being worked on.

**Why is Anikku on 0.2 if Komikku is on 1.14?**
They're different apps: manga has years of head start. 0.2 with an organization behind it is a normal phase of a young project — the previews channel and the translations are signals of structure, not of a toy.

**Are Anikku and AniZen the same?**
Family, not twins: AniZen declares itself a rebrand of "Anikku Mod" (its guide tells it with dates). Anikku is the organization's original. Same declared lineage, different houses.

**Which extension fits Animiru?**
The Aniyomi ecosystem's — it's its inheritance — with the previous guide's living map. For Anikku, its dedicated warehouses above. In both cases: the index gets read at the warehouse's house, not in a post.

**Do they have a TV or desktop version?**
AnimiruTv (TV, a small fork). Anikku: no variants known — its org concentrates on mobile. Whatever exists tomorrow, its organizations will say.

**Which of the two listings moves faster?**
Animiru, no argument: two releases today. But speed isn't the criterion — the living repo is, and both live.

## 🔗 Links

- Animiru: https://github.com/Quickdesh/Animiru · Aniyomi's forks registry: https://aniyomi.org/forks/Animiru/
- AnimiruTv: https://github.com/Znabil/AnimiruTv
- Anikku: https://github.com/komikku-app/anikku · testing: https://github.com/komikku-app/anikku-preview
- New warehouses: https://github.com/salmanbappi/extensions-repo · https://github.com/salmanbappi/aniyomi-extensions
- Cross-guides: the Aniyomi/Animetail branch (piece 13) · AniZen (piece 11) of this collection

> La Bandita reports from dated sources. Taking the manga out is also a purpose — and this week it published it twice.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: Animiru ★864, extensions-repo's TODAY push. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
