# Piece 02 — Kototoro: manga, novels and video in a single library — v2.1.3 shipped today (re-verified Sep 15)

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 02)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── ℹ️ What Kototoro is
├── 🧭 State of the project (verified today)
├── 📦 Today's version: v2.1.3
├── 🏗️ How it's built
├── 🔌 Sources and extensions: what connects
├── 📖 Novels and JSON reading
├── 🌳 The neighborhood: Mihon, Aniyomi, Komikku and Tadami
├── ♿ Reading comfort and accessibility
├── 🛠️ Troubleshooting
├── 🔒 Security and the supply chain
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

Kototoro is an open-source Android app that puts three libraries together in one: manga, novels and video. History, favorites and sync live in a single flow, and on top it brings OCR translation on the phone itself, with downloadable models.

The reason for this edition: version **v2.1.3** shipped TODAY itself, September 15 — one day after 2.1.2 — and that makes four in five days. Re-verified on the morning of the 15th: the project woke up with a new release. The project moves at an almost daily pace, so this guide carries today's numbers and teaches you the only clock that rules: its releases page.

The idea in one image: a bookshelf with three drawers where before you had three separate pieces of furniture. Unifying saves jumps — and multiplies dependencies. This guide looks at what it joins and what it asks in exchange.

## ℹ️ What Kototoro is

https://github.com/Kototoro-app/Kototoro

Kototoro comes from the "source"-style reader lineage: the app doesn't carry content inside, it talks to sources the user adds. On that base it adds two things that set it apart: novels (long-form reading by JSON, in the style of the Chinese source readers) and video, in the same app.

```
Kototoro in a box
Repo:          github.com/Kototoro-app/Kototoro
License:       Apache-2.0
Package:       org.skepsun.kototoro
Android:       8.0 and up (recent builds)
Docs:          kototoro-app.github.io/Kototoro
Origin:        the skepsun lineage (kototoro-parsers)
Stars:         569 · activity: today itself
```

Its documentation site is alive and got read today: it describes the all-in-one reader (manga, novels, video, history, favorites and sync), local OCR translation with model downloads, the sync flows and the source integration reference.

## 🧭 State of the project (verified today)

The repository's API, opened on the 14th and reopened TODAY, September 15 (the move's re-verification):

```
Stars:            569
Last push:        Sep 14 · TODAY's release (Sep 15): v2.1.3
Working branch:   devel (at the Sep 13 cutoff: 8 branches,
                  196 tags, ~6,950 commits)
Versions:         v2.1.3 (TODAY, Sep 15) · v2.1.2 (Sep 14) · v2.1.1 (Sep 13) · v2.1.0 (Sep 11)
Nightly:          the Kototoro-Nightly repo, build N20260914 (Sep 14)
```

Four versions in five days. The Nightly — the daily testing version — is alive too, with a Sep 14 build (the last one checked as of TODAY). What does that mean for you? That any number in this guide (or any other) ages fast: the only current version reference is the project's releases page, opened the day you install.

## 📦 Today's version: v2.1.3

Published TODAY, September 15. Its packages, per the API (none was downloaded for this guide):

```
arm64-v8a      125,446,780 bytes    119 downloads at noon
armeabi-v7a    117,554,684 bytes      5
universal      312,997,668 bytes     14
x86            140,010,036 bytes      1
x86_64         147,078,128 bytes      2
```

For most modern phones the right file is arm64-v8a. The universal weighs more than double because it carries everything — it's for special cases.

The release notes (read today) carry concrete change:

- Cover artwork customization.
- Scroll distance per volume key in webtoon reading.
- Better category management and search in favorites.
- Reader adjustments on wide screens and restored margin scrolling on resume.

What a release like this does NOT prove: that old backup episodes (the 1.4–1.7 series) are closed. If you come with a big library, the rule doesn't change: manual backup and a dry run before migrating anything.

**Caches and mirrors run late.** The v2.1.3 shipped hours ago: if a page shows you July versions or the 1.x series, it's not fraud — it's delay. The only living reference is Releases.

## 🏗️ How it's built

Kototoro inherits its lineage's architecture: the Kotlin app used to consume its own parser library — independent today — called kototoro-parsers (github.com/skepsun/kototoro-parsers, version 1.8, with activity on September 10). That app/parsers split is the ecosystem's pattern: the house (the app) and the streets (the sources) are maintained separately.

Inside the app, each tab (Manga / Novels / Video) talks to its kind of source:

- Manga: reader-style sources (extensions compatible with the Mihon ecosystem).
- Novels: Legado-style JSON sources — rule books that say where everything is.
- Video: JSON streaming sources, including TVBox-style profiles.

That mix is its promise and its risk: three kinds of source, three kinds of possible failure. The troubleshooting section below exists for that.

## 🔌 Sources and extensions: what connects

Kototoro's manga extensions are compatible with the Mihon ecosystem's format. That ecosystem's warehouses, with their state verified today:

```
Keiyoushi          ★14,980  push Sep 14      the main hub
   https://github.com/keiyoushi/extensions
   (code: keiyoushi/extensions-source, ★4,678, alive as of Sep 15)
Yūzōnō anime       ★432     push Sep 13
   https://github.com/yuzono/anime-extensions
manga-repo         ★445     push Sep 14      for Komikku/Mihon
   https://github.com/cuong-tran/manga-repo
Copymanga (CN)     ★2,753   v1.4.85 (Sep 8)
   https://github.com/LittleSurvival/copymanga-copy20
```

This guide family's rule on warehouses: the project and its official page get named; the installation recipe (the index pasted into the app) everyone reads in the project's README, the day they use it. It doesn't get copied here.

## 📖 Novels and JSON reading

Here Kototoro speaks the language of the Chinese source readers:

**Legado 3.0** — github.com/gedoor/legado — ★47,074, the giant of the "source book" model: every source is a JSON that says how to search, where the text is and how to paginate.

**Yuedu (阅读)** — github.com/XIU2/Yuedu — ★12,268, a community collection of reading sources.

Kototoro imports those JSON flows and adds its translation layer on top: OCR over the image, with downloadable models running on the phone, or via API if you prefer an external service. For video it also imports TVBox-style profiles — JSON lists pointing at media, with different levels of complexity (direct links, playlists, simple CMS, and profiles depending on JavaScript or remote components, in that test order).

## 🌳 The neighborhood: Mihon, Aniyomi, Komikku and Tadami

Kototoro isn't alone. The free ecosystem's readers, with today's numbers:

```
Mihon        ★23,601  v0.20.4 (Aug 5)   push TODAY (Sep 15)     manga
Aniyomi      ★7,683   push Sep 14                        manga+anime
Komikku      ★4,721   v1.14.1 (Jul 17)  push Sep 11    manga
Tadami       ★260     v0.62 (Sep 12)    push Sep 13 · alive    manga+anime+ranobe
Kototoro     ★569     v2.1.3 (TODAY)    push TODAY    manga+novels+video
```

Mihon is the manga tree's trunk (Tachiyomi's de facto successor, closed in 2024). Aniyomi and Tadami add anime. Komikku is the fork with a life of its own. Kototoro is the branch that wanted it all together. None is "the best" in the abstract: the good one is whichever covers what you read, with a living repo.

And watch the temptation to mix: one tree's extensions don't work in the other. Kotatsu, Usagi and their relatives use their own parsers (another guide family covers that tree).

## ♿ Reading comfort and accessibility

What the app brings out of the box for the eye and the hand:

- Readers per mode: page, continuous and webtoon, with scroll tuning (now by volume key too, per the 2.1.2 of Sep 14).
- Translation OCR at two levels (basic and advanced) with downloadable local models — useful for manga with no official translation.
- Unified history, favorites and categories (the 2.1.2 of Sep 14 improved exactly category management).
- Sync of your own reading flow between sessions.

The usual advice for your eyes: high brightness on white-margin pages, night mode for webtoon, and download before reading on a trip — the ecosystem's three readers allow it.

## 🛠️ Troubleshooting

**The sources don't show up.**
Check in order: is the extension installed? was the repo added and synced? are you in the right tab (Manga / Novels / Video)? did you refresh the extensions screen? The classic cure: reinstall the extension and refresh.

**A novels JSON won't import.**
First: is it a Legado source or a TVBox profile? They're different formats imported from different menus. Second: is the JSON valid? does the URL respond? Third: try importing from a local file first — it removes half the variables.

**A TVBox profile imports but won't load.**
The test ladder, simple to complex: direct media → playlists → simple CMS → profiles depending on JavaScript → profiles with remote components. A JSON can import perfectly and still fail because an external dependency changed or died. That's not the app's fault.

**Translation won't start.**
Short list: local or API-only mode depending on what you want; correct source/target languages; OCR level (basic/advanced); the models actually downloaded; and if you use API, endpoint, key and model written right. 80% of cases is a model that never got downloaded.

**The app eats space.**
It's big by design: parsers for three media + OCR models. If the phone is tight, start without the advanced models and without universal mode.

## 🔒 Security and the supply chain

What the project declares: its developers have no affiliation with content providers and don't govern extension repositories — the sources are put in by the user. The app is an instrument; the content is your decision and your legal responsibility.

As of last week's cutoff, the repo published no security policy or code of conduct (it does have a contribution guide and a license). It doesn't imply insecurity — but in an app that loads runtimes and third-party sources, it's a signal to watch. Concrete builds distributed by alternative stores passed scans (ClamAV, APKiD, Quark-Engine) with no threats: that holds for that exact file, not the whole chain.

The house's rule: don't trust a source just because it's on an internet list. Repo, commit, tag and signature get looked at before installing. And stars install nothing.

## ❓ FAQ

**Which is the good version today?**
Whichever Releases says the day you install — today it's v2.1.2, published this very morning. Tomorrow it may be another; three releases in four days say it all.

**Can I have manga, novels and video in the same app?**
Yes, that's its point. The price: three kinds of source with three kinds of failure. Back up separately and be patient with the diagnostic ladder.

**Is it compatible with Mihon's extensions?**
The manga extension format, yes. The anime/novels ones have their own path (JSON). What's a no: Kotatsu/Usagi sources are another tree, they don't come in.

**I'm coming from the 1.x series — how do I migrate?**
With manual backup and a dry run. The 1.4–1.7 backup episode is documented in the community; that the 2.x series moves fast doesn't by itself prove that chapter is closed.

**Does the OCR translation need internet?**
Local mode doesn't: it runs on the phone with downloadable models. API mode does, and it depends on the service you configure.

**And TVBox, what's that?**
JSON lists pointing at video media. Importing is easy; loading depends on the things they point at staying alive. Always start with the simple end of the ladder.

**How big is it?**
The arm64 package of v2.1.2 is around 125 MB, and the universal passes 300 MB. Add OCR models on top if you download them.

**Do the 569 stars mean anything?**
A small community in full growth, with a development pace few apps on the map match today. Stars don't install: they measure fame, not quality.

## 🔗 Links

- Repo: https://github.com/Kototoro-app/Kototoro
- Releases: https://github.com/Kototoro-app/Kototoro/releases
- Nightly: https://github.com/Kototoro-app/Kototoro-Nightly
- Docs: https://kototoro-app.github.io/Kototoro/
- Origin parsers: https://github.com/skepsun/kototoro-parsers
- Legado: https://github.com/gedoor/legado · Yuedu: https://github.com/XIU2/Yuedu
- manga-repo: https://github.com/cuong-tran/manga-repo
- Yūzōnō anime: https://github.com/yuzono/anime-extensions
- Keiyoushi: https://github.com/keiyoushi/extensions · https://keiyoushi.github.io
- Komikku: https://github.com/komikku-app/komikku
- Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork
- Copymanga: https://github.com/LittleSurvival/copymanga-copy20
- Mihon: https://github.com/mihonapp/mihon · Aniyomi: https://github.com/aniyomiorg/aniyomi

> La Bandita reports from dated sources. The shelf is free; what you put on it is your decision too.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: Kototoro re-verified (v2.1.3 of TODAY), Mihon ★23,601, Keiyoushi ★14,980, Yūzōnō ★432, manga-repo ★445. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.

**Final verification note (Sep 15, night):** its own documentation (kototoro-app.github.io/Kototoro) returns 404 at this hour, checked live; the GitHub house stays alive (★569, v2.1.3 of TODAY). The site may be mid-move; the link gets reopened the day it's used.
