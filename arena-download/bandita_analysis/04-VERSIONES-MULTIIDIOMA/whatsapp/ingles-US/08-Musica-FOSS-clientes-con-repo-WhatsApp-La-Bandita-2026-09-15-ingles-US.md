# Piece 08 — FOSS music: clients with a repo and a pulse date — cracked Spotify doesn't enter

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 08)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── ⚖️ What this guide is not
├── 🧬 The genealogy: from ViMusic to today's family
├── 🎧 The streaming clients, listing by listing
├── 📻 NewPipe: the separate species
├── 📂 Auxio: your music, your files
├── 🎙️ AntennaPod: podcasts
├── 🆕 The missing ones: N-Zik and Gabi
├── 🚫 What doesn't get pasted
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

A guide to open-source music clients, with every project's pulse measured on September 14 and re-verified at the move (Sep 15). The week brought real movement in this family: OuterTune premiered a version this month, Metrolist keeps its release streak, and the complete lineage got documented.

```
STREAMING (YouTube Music underneath)
SimpMusic      ★11,257   2.1.0 (Sep 7)     push Sep 11   alive
OuterTune      ★5,390    v0.11.1 (Sep 6)   push Sep 6    alive
Metrolist      ★12,789   13.7.0 (Sep 7) · the 14th's Nightly in view  alive    ← the most active
InnerTune      ★6,088    push Nov 2025                    asleep
Harmony-Music  ★3,081    v1.12.2 (Dec 25)  cross-platform
music-you      ★220      alive             minimalist
InterTune      ★12       pinned fork, niche

STREAMING (a general front-end)
NewPipe        ★39,682   v0.29.1 (Aug 15)  push Aug 31

LOCAL FILES
Auxio          ★4,274    v4.1.5 (Aug 4)    push Sep 8

PODCASTS
AntennaPod     ★8,153    3.12.1 (Sep 5)    push Sep 12

ViMusic        ★9,480    the ancestor
```

## ⚖️ What this guide is not

YouTube and YouTube Music have their terms of service. A free client querying those servers can clash with them — this guide isn't a law firm: it doesn't say "it's legal" or "it isn't." It says repo, license (GPL on all of today's listings, verified on their pages), version and last push. The decision of what you use is yours, consequences included.

And the usual sentence: there's no "free Spotify premium" APK here nor mods of anything. That door has its own guide — the stores one — and it always ends the same.

## 🧬 The genealogy: from ViMusic to today's family

This family has a documented family tree, and knowing it clears up half a dozen names:

```
   the app that invented the model: YouTube Music
   streaming with a queue, without the official app.
   Archived today — but its idea birthed all this.
   │
   ├── InnerTune (z-huang)
   │      the direct heir: Material 3, a library
   │      with an account, synced lyrics. Its last
   │      push was in November 2025 — the creator
   │      moved to other projects and the repo sleeps.
   │      │
   │      ├── OuterTune (its sturdiest living fork)
   │      │      it added LOCAL FILE support
   │      │      alongside the streaming. Version 0.11.1
   │      │      on September 6 — last month it still
   │      │      showed a December tag; on Sep 14 the row got corrected.
   │      │
   │      └── Metrolist (★12,789)
   │             the most installed of the second
   │             generation: version 13.7.0 of Sep 7
   │             with its own nightly. Of the living ones,
   │             the steadiest cadence.
   │
   └── SimpMusic (a parallel project, same background)
          cross-platform, with a very active
          development line: 2.0.0 on August 28 and 2.1.0
          on September 7.
```

The lesser relatives complete the picture: Harmony-Music (★3,081, desktop and mobile cross-platform, its last stable from December 2025), music-you (★220, the minimalist) and the curious case of InterTune (★12): a fork pinned to OuterTune's 0.10.1 "for its playback screen," maintained by its author for their own use and whoever finds it useful. Its README recommends, for whoever seeks active maintenance, Metrolist and another project called ArchiveTune — of that last one, no repo got opened in this review.

## 🎧 The streaming clients, listing by listing

### Metrolist — the one with the steady cadence

https://github.com/mostafaalagamy/Metrolist

★12,789 · version **13.7.0 (September 7)** · GPL · alive. The InnerTune lineage's most stable second generation: monthly versions, its own nightly, and a user base that put it among the topic communities' fixed recommendations. If you come from a sleeping InnerTune, this is the natural house. Today's pulse: besides 13.7.0, the repo publishes a **Nightly** — a daily build seen TODAY, September 14. *Move certified on Sep 15: the house is now the MetrolistGroup organization (old links redirect) — the complete dynasty in Piece 27.*

### OuterTune — the one joining streaming and files

https://github.com/OuterTune/OuterTune

★5,390 · version **0.11.1 (September 6)** · GPL · alive. The fork that added local-file reading to the InnerTune line: your downloaded music and the streaming catalog in the same player. Material 3, dynamic theme. Last month its last tag was from December — this guide recorded it so; Sep 6 corrected the picture. That's how fast a number expires.

### SimpMusic — the tireless cross-platform one

https://github.com/maxrave-dev/SimpMusic

★11,257 · **2.1.0 (Sep 7)** and 2.0.0 (Aug 28) · GPL · alive. Two major versions in ten days. Its bet: the same YouTube Music background with extra functions — synced lyrics, lossless audio declared in its listing, cross-platform. The family's most restless developer.

### InnerTune — the ancestor at rest

https://github.com/z-huang/InnerTune

★6,088 · push of November 13, 2025 · GPL · unarchived but asleep: almost ten months without new code, releases from 2024. Its place in history is guaranteed — it's the source half the family drinks from. To install today, its heirs do the work.

### Harmony-Music and music-you — the alternatives

https://github.com/anandnet/Harmony-Music — ★3,081 · v1.12.2 (Dec 7, 2025) · cross-platform (Android and desktop), GPL. Slow rhythm but a serious project.

https://github.com/DanielSevillano/music-you — ★220 · GPL · the family's minimalist option, for whoever wants just enough.

### InterTune — the niche case

https://github.com/ItzSkyeYT/InterTune — ★12 · GPL · alive by its author's decision: pinned to OuterTune's 0.10.1 to keep a specific playback screen. "I use it daily and keep it public because it helped a few people," its README says. Honesty is also a trait of a healthy project — and its recommendation of active alternatives (Metrolist) confirms it.

## 📻 NewPipe: the separate species

https://github.com/TeamNewPipe/NewPipe

★39,682 · v0.29.1 (August 15) · push of Aug 31 · GPL · alive. NewPipe isn't a YouTube Music client: it's a free front-end to the WHOLE YouTube universe — videos, music, subscriptions, with no account and no ads. For music it asks less library comfort than the clients above; in exchange it covers everything else. It's one of Android free software's most veteran and respected projects. Its historic distribution channel is F-Droid — that family's store listing applies.

## 📂 Auxio: your music, your files

https://github.com/OxygenCobalt/Auxio

★4,274 · v4.1.5 (August 4) · push of Sep 8 · GPL · alive. For music you ALREADY have: a local, rational player, connecting to no catalog and no cloud. If your library lives on the phone (copied with this family's files guide tools), this is the listing. No account, no streaming, no scares.

## 🎙️ AntennaPod: podcasts

https://github.com/AntennaPod/AntennaPod

★8,153 · 3.12.1 (Sep 5) · push of the 12th · GPL · alive. A complete podcast manager: RSS feeds, automatic downloads, variable speed, chapters. It doesn't compete with anything above: another category that old threads mixed into music across a thousand characters of noise. Here, everything in its drawer.

## 🆕 The missing ones (the September 14 addition)

### N-Zik — Kreate's multilingual child

https://github.com/N-Zik-Group/N-Zik · v7.5.1-f (September 1; as of TODAY Sep 15 its releases page dances with a dev v8.0.0) · store: https://appteka.store/app/4abr315772

A multilingual fork of Kreate declared in its own README: it streams and caches YouTube Music, with offline downloads, word-by-word synced lyrics, a visualizer, Discord Rich Presence, widgets and Android Auto/TV/Automotive support. It alternates the modern N-Zik interface with ViMusic's classic one — this guide's living genealogy. Optional Premium quality coming in with a YouTube Music account. OTA updates. The author's honesty, included: developed AI-assisted with human review, declared, recommending more mature alternatives (Metrolist, VIVI Music, RiPlay) if you prefer proven stability. That notice is a signal of craft, not weakness. Closing pulse (Sep 14, night): the repo is already cooking **today's v8.0.0-dev** — the store's stable stays 7.5.1-f.

### Gabi — the thousand-site downloader

https://github.com/Hotaro26/gabi · v4.6.1 "YouTube 403 Fix" (September 1) · store: https://appteka.store/app/b4cr315682

A Material 3 and Jetpack Compose media downloader running yt-dlp and gallery-dl: videos, audio and galleries from over 1,000 sites — YouTube, TikTok, Instagram, Twitter/X, Reddit, SoundCloud, Pixiv and the list goes on. Downloads from the clipboard in one tap (the Instant button), shares the link from any app and Gabi picks it up, quality up to 1080p/maximum, MP3 extraction, a preview with title and estimated weight, and Material You dynamic-color themes. This guide's natural complement: to listen, the clients above; to carry, Gabi.

Both are found on Appteka — the store of Piece 01. The direct APK doesn't get pasted: each app's house is its repo.

## 🚫 What doesn't get pasted

"Premium" mod APKs of any app · lists copied from download wikis · group invites · URL recipes. Everyone opens the project's README the day they use it — each listing's house is in the links below.

## ❓ FAQ

**Which do I install to start?**
If your music is catalog: Metrolist (the steadiest cadence) or OuterTune (if you also have local files). If your music is your collection: Auxio. If you want all of YouTube with no account: NewPipe. If you live on podcasts: AntennaPod.

**Are these apps legal?**
This guide isn't a law firm and doesn't say that. It says which project exists, under what license, in what state. Each service's terms get read at its house.

**Why is InnerTune still on lists if it's asleep?**
Because it's half the family's living ancestor — and because its heirs (OuterTune, Metrolist) carry its code forward. It gets listed for history, and for whoever uses it anyway.

**Metrolist or OuterTune?**
Both alive and active this month. Metrolist: proven monthly cadence. OuterTune: built-in local files. Whichever covers your use — and both get opened the day you install, because numbers expire.

**And what happened to RiMusic?**
Archived in July 2025. April's 340-thousand-character thread treated it as alive: inflating isn't verifying. Its listing says: history.

**Do these apps eat battery?**
What this guide can say without a lab: they're players, not games; consumption depends on use (download vs streaming). What it can NOT say: battery numbers — not measured here, and not invented.

**Is there an iPhone version?**
Of this family: Harmony-Music declares cross-platform (desktop and mobile). The rest of the listings are Android. The free iOS music ecosystem is another map.

**Discord or group for support?**
Each project has its community house in its README — it gets opened there, not pasted here. This family doesn't use delivery channels.

## 🔗 Links

- Metrolist: https://github.com/mostafaalagamy/Metrolist
- InnerTune: https://github.com/z-huang/InnerTune
- OuterTune: https://github.com/OuterTune/OuterTune
- Harmony-Music: https://github.com/anandnet/Harmony-Music — music-you: https://github.com/DanielSevillano/music-you — InterTune: https://github.com/ItzSkyeYT/InterTune
- SimpMusic: https://github.com/maxrave-dev/SimpMusic
- Auxio: https://github.com/OxygenCobalt/Auxio
- NewPipe: https://github.com/TeamNewPipe/NewPipe
- AntennaPod: https://github.com/AntennaPod/AntennaPod
- Gabi: https://github.com/Hotaro26/gabi — store: https://appteka.store/app/b4cr315682
- N-Zik: https://github.com/N-Zik-Group/N-Zik — store: https://appteka.store/app/4abr315772
- Archived: https://github.com/vfsfitvnm/ViMusic · https://github.com/fast4x/RiMusic

> La Bandita reports from dated sources. The lineage gets verified too: the ancestors explain the living.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: SimpMusic ★11,257, Metrolist ★12,789 (+Nightly), OuterTune ★5,390, InnerTune ★6,088, N-Zik's dev v8.0.0. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
