# Piece 17 — The immersion layer: the readers that teach you Japanese while you read — and the missing Komga client

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 17)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🦋 Chimahon — the Mihon fork that mines Anki
├── 📚 Hoshi Reader — the Japanese EPUB with a thousand tools
├── 🎐 Yomikai — OCR, voices and the floating mini-player
├── 🌗 Yomi Reader — the anime/manga/novel triple
├── 🏛️ Koharia — your Komga server, in your pocket
├── 🧩 The shops behind (shared dictionaries and more)
├── ⚖️ Who is this layer for?
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

There's a layer of the ecosystem the big maps barely see: the one of whoever reads Japanese WHILE LEARNING it — dictionaries at a tap, Anki cards on the fly, vertical text, Mokuro manga, voice over the page. This guide lists that layer's five living projects, all verified TODAY, September 14 — **two shipped a version today itself**:

```
Hoshi Reader   ★378   v1.3.3 (Aug 13)   Japanese EPUB + Yomitan + Anki + e-ink
Chimahon       ★198   v2.4.2 (TODAY, Sep 15)   a Mihon fork: dictionary, Mokuro, Anki
Koharia        ★148   v0.5.0 (Sep 14)      an Android client for Komga servers
Yomi Reader    ★10    v0.1.7 (Sep 6)    anime + manga + novel, Tadami-compatible
Yomikai        ★0     v1.9.84 (TODAY, Sep 15)  OCR + voices + floating mini-player
```

Small stars, big shops: here the fame numbers don't tell the story — cadence and features do.

## 🦋 Chimahon — the Mihon fork that mines Anki

https://github.com/Chimahon/chimahon

```
★198 · GPL-3.0
v2.4.2 (TODAY, Sep 15) · v2.4.1 · v2.4.0 (Sep 11) — three in four days
What it is: "an immersion fork of Mihon" (its description):
a native dictionary (Yomitan), Mokuro manga and anime,
an EPUB novel reader, and instant mining into Anki
```

It's Mihon with a classroom inside: you read your usual manga and, on tapping a word, the dictionary opens right there; whatever you want to keep, flies to your Anki deck without leaving the chapter. Its shop also maintains the components: Chimahon-ffmpeg and Chimahon-local-models (local processing), and it uses Hoshi's dictionaries — the layer weaves itself together.

## 📚 Hoshi Reader — the Japanese EPUB with a thousand tools

https://github.com/HuangAntimony/Hoshi-Reader-Android

```
★378 · GPL-3.0
v1.3.3 (Aug 13) — the layer's biggest
What it is: a Japanese EPUB reader with Yomitan
lookup, Anki mining, audiobook-accompanied
reading and e-ink support
```

Its README (read on Sep 14) lists what's its: single or batch EPUBs with visible progress, its own shelves, vertical or horizontal text with pagination or continuous scroll, Yomitan dictionaries imported and updated from the app, recursive lookup (you tap a word inside a definition and it keeps going), an immersive focus mode, page turning with the volume keys and e-ink-reader-specific options. And it's the tip of a complete shop: its author maintains the dictionaries (hoshidicts), a reference Japanese grammar, tools for web novels (narou-py) and contributes to Yomitan and mpvacious. The immersion layer has a center of gravity, and it's named HuangAntimony.

## 🎐 Yomikai — OCR, voices and the floating mini-player

https://github.com/sj0404-collab/yomikai
(the "yomihon-custom" going around: https://github.com/sj0404-collab/yomihon-custom)

```
Apache-2.0
v1.9.84 (TODAY, Sep 15) · v1.9.83 (the 15th's early morning) · v1.9.79 (Sep 14) · v1.9.78/76 (Sep 13)
— a truly daily cadence
What it is: a manga reader with OCR and ovoz
(roles and voices), dictionaries, and a
mini-player floating over every app
```

Its description (from the Russian original) says it whole: manga with text OCR, per-role voices, dictionaries and a mini player floating over any app — you hear the chapter's voice while reading somewhere else. Two map notes: the root project is **Yomihon** (yomihon/yomihon, ★125, "now with OCR", v0.4.0 of Jul 30) — the repo name "yomihon-custom" comes from there — and the active house is Yomikai, with a web sister (yomikai-pwa, React+TSX, with a browser and an AI chat inside). Having no stars means nothing: it publishes versions every day.

## 🌗 Yomi Reader — the anime/manga/novel triple

https://github.com/codegeasse1/yomi-reader

```
★10 · Apache-2.0
v0.1.7 (Sep 6) — young, at 0.1
What it is: "an open-source reader of anime,
manga and novels for Android (Tadami/Aniyomi
compatible)" — its description
```

The triple bet on the Aniyomi lineage: the three media in one app, eating extensions compatible with Tadami. It's on 0.1 — an honest age — and its shop brings more: Nekoread (a manga reader, v2.2.5 of Sep 10) and hikari (universal streaming with Stremio addons and CloudStream plugins, v0.3.67 of Sep 13). A builder with five irons in the fire — open tracking on all.

## 🏛️ Koharia — your Komga server, in your pocket

https://github.com/Mister-album/Koharia

```
★147 · Apache-2.0
v0.5.0 (Sep 14) · v0.4.5 (Sep 6)
What it is: "an independent third-party Android
reader for browsing and reading content from
Komga servers" — its description (from Chinese)
```

Komga is the library server the big readers already sync; Koharia is the app devoted to it: your server, your app, with the reader made to measure. v0.5.0 published Sep 14. From the same author: the project's web and its own fork of the komga server — whoever builds the client understands the server, and the other way around.

**The layer's other half, verified tonight by free exploration:** **Komga** (gotson/komga, ★6,659, MIT, 1.26.3 of Aug 12) — a comics, mangas and eBooks server with API, OPDS and Kobo and KOReader sync; and **Kavita** (Kareadita/Kavita, ★11,677, GPL-3.0, v0.9.1.4 of Sep 2), the multi-platform reading server. Koharia lives because these live — and the other way: a server without clients is an archive, a client without a server is a shell.

## 🧩 The shops behind (shared dictionaries and more)

The layer stands on shared infrastructure worth naming: **Chimahon** also uses the **hoshidicts** dictionaries; **Yomitan** (the browser's pop-up dictionary, the niche's absolute reference) connects with everybody; and this week's observation caught a small but living companion: **android-koreader-companion** (★9, MIT, a version of Sep 14) — it shows what you read in KOReader and Mihon, the progress between the two worlds.

## ⚖️ Who is this layer for?

```
Do you read manga in Japanese and study?
   → Chimahon (if you come from Mihon) or
     Yomikai (if you want voice and OCR).

Do you read light novels in Japanese EPUB?
   → Hoshi Reader: it's ITS terrain, with
     e-ink included for the ink reader.

Anime + manga + novel in one app
(and Japanese isn't your focus)?
   → Yomi Reader — and look at Tadami (piece 13),
     the Aniyomi lineage's triple with years on it.

Do you have a Komga server?
   → Koharia, the devoted app.
```

No listing passes on fame: it passes on cadence, own features and an open repo — and all five live, re-verified as of TODAY Sep 15.

## ❓ FAQ

**Do these replace Mihon/Komikku/Aniyomi?**
No: they're layers on top of or beside. Chimahon IS a Mihon fork (your library migrates with the usual rules); Koharia needs a Komga server; Hoshi is for Japanese EPUB; Yomikai and Yomi Reader are separate houses. Each covers what the trunk doesn't.

**And the extensions? Do the usual ones work?**
Yomi Reader declares Tadami/Aniyomi compatibility; Chimahon, being a Mihon fork, inherits the Mihon ecosystem. Hoshi (EPUB) and Koharia (Komga) don't eat extensions: they eat books and servers. Yomikai builds its own sources — its README rules the day you use it.

**Why such small stars if they're so active?**
Because a niche is a niche: whoever studies Japanese with manga are thousands, not millions. The house's stick was never fame — it's cadence and own contribution, and here there's plenty.

**Do they work without knowing Japanese?**
Chimahon, Hoshi and Yomikai EXIST to learn it — the dictionary and the voice are the point. For Spanish/English reading, pieces 13–16's trunks remain the house.

## 🔗 Links

- Hoshi Reader: https://github.com/HuangAntimony/Hoshi-Reader-Android
- Chimahon: https://github.com/Chimahon/chimahon
- Yomikai: https://github.com/sj0404-collab/yomikai · web twin: https://github.com/sj0404-collab/yomikai-pwa · the name's root: https://github.com/yomihon/yomihon
- Koharia: https://github.com/Mister-album/Koharia
- Yomi Reader: https://github.com/codegeasse1/yomi-reader — sibling: https://github.com/codegeasse1/Nekoread
- The progress companion: https://github.com/woxakv/android-koreader-companion
- The servers: https://github.com/Kareadita/Kavita · https://github.com/gotson/komga

> La Bandita reports from dated sources. Reading with a dictionary at hand — now, on the same finger.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: Chimahon v2.4.2, Yomikai 1.9.84, Koharia ★148 (all of TODAY). Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
