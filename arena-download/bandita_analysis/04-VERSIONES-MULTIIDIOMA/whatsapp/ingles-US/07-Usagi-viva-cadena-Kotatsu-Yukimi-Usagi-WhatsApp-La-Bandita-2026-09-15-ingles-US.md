# Piece 07 — Usagi is alive: the Kotatsu → Yukimi → Usagi chain and the tree's four living ones

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 07)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🧬 The complete chain: Kotatsu → Yukimi → Usagi
├── 🏗️ What actually got archived (and it wasn't the app)
├── 📱 Listing: UsagiApp/Usagi
├── 🌳 The Kotatsu tree's four living ones
├── 🧩 Plugins and parsers: how this tree eats
├── 🍴 Usagi's forks
├── 🎭 The week's impostors
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

It's running around the groups: "Usagi got archived," "Usagi died." It was verified on September 14, at the project's own house (re-verified as of Sep 15: still alive):

```
UsagiApp/Usagi — what got seen today
✓ No archive banner on the repo page
✓ Push verified on Sep 14
✓ A living README: "free manga reader for Android,
  inspired by Kotatsu"
✓ An active F-Droid listing: org.draken.usagi
✓ An organization with 16 repositories
✓ One single stable version: 1.0 (with rc2 and rc1 behind)
```

**Usagi is alive.** What died was something else — and that's where the confusion comes from: the organization did archive its old plugins layer (two concrete repos), and Usagi's predecessor, named Yukimi, was indeed discontinued by its own developer. That whole story goes below, with dates.

## 🧬 The complete chain: Kotatsu → Yukimi → Usagi

The Kotatsu tree has a three-act genealogy. The first part is verified on GitHub; the middle transition comes from community reports (threads from November 2025 and early 2026):

```
ACT 1 — Kotatsu
KotatsuApp/Kotatsu · ★8,855
ARCHIVED on November 4, 2025 (confirmed Sep 14)
The original closes after Kakao Entertainment's
legal pressure and, per its own authors, also
because of the coming developer verification
policy. Last version: 9.4.1.

ACT 2 — Yukimi (community reports)
The same developers announce a successor:
Yukimi. Weeks later, its author discontinues it
and pulls its site. The threads of the time call it
finished — "the project ended today."
No living repo was left to verify that day: that's why
this guide counts it as told history,
not as a listing.

ACT 3 — Usagi
The community continues by another road: Usagi,
with the same Kotatsu spirit but one key design
decision: it ships NO built-in sources.
The sources are brought by the user. That decision
is, probably, the reason Usagi stays alive
where others died.
```

The reports of the time also named Kotatsu-Redo, Kototoro and Futon as the tree's survivors. All four live — listings below, all opened today.

## 🏗️ What actually got archived (and it wasn't the app)

The UsagiApp organization has 16 repositories, opened today. Two are archived — and they're the rumor's real source:

```
ARCHIVED (the old architecture)
UsagiApp/core-parsers   "library for the plugins repo"
UsagiApp/core-exts      "core for loading external plugins"

ALIVE (what replaces them)
UsagiApp/TsukiMix       the new core for reading and building
                        extensions and parsers
UsagiApp/plugins        plugins and examples for creators
UsagiApp/syncserver     a data-sync server
                        "for Kotatsu / Usagi"
UsagiApp/Tsuki          the ecosystem's shared library
```

It's the gesture of every living house: demolishing the old scaffolding while the building stays open. Whoever passed by the organization, saw two "archived" without reading names, and carried the rumor off. The names say something else: the old plugins layer got archived — the app didn't even notice from outside.

## 📱 Listing: UsagiApp/Usagi

https://github.com/UsagiApp/Usagi

```
What it is:   a free manga reader for Android,
              inspired by Kotatsu, with NO built-in sources
License:      GPL-3.0
Version:      1.0 (the only stable; rc2 on Sep 2,
              rc1 on Aug 9)
Stars:        257 · push of Sep 14 (verification day; release 1.0 of Sep 10)
Android:      5.0 and up (README badges)
House:        github.com/UsagiApp/Usagi
Channels:     GitHub, F-Droid (org.draken.usagi),
              Obtainium and OpenAPK per its README
```

Its F-Droid page loads today — the app is published there, with its org.draken.usagi package. The Discord and Telegram the README shows don't get linked here: this family neither uses nor recommends delivery channels, and the community links belong to the project itself.

A "1.0" is a birth number, not a maturity one. The app has a release, a README, a house and a small but living community. What hasn't been audited: how much its author answers reports — open a couple of issue threads before trusting it your library, as with any young project.

## 🌳 The Kotatsu tree's four living ones

### Kotatsu-Redo — the one that inherited the name

https://github.com/Kotatsu-Redo/Kotatsu-Redo

★867 · version **9.8.3 (September 6)** · GPL-3.0 · alive. The community fork the community names first since the original archived. Its organization holds four repos: the app, its parsers (kotatsu-parsers-redo), a telemetry server and a sync one. It carries the "Kotatsu" name forward with 9.8.x-series versions.

### Futon — the one with its own engine

https://github.com/AppFuton/Futon

★427 · version **9.8.1 (August 16)** · GPL-3.0 · alive. Its organization has eight repos, including its own parser library (AppFuton/futon-parsers, archived — frozen while the app advances; a signal to watch) and even its landing page. A curiosity of the tree: Futon's and Kotatsu-Redo's version numbers look alike — both inherited the original's numbering.

And a detour notice: MikuX-Dev/Futon exists (3 stars, something else with the same name). The valid listing is AppFuton.

### Kototoro — the one that wanted it all together

https://github.com/Kototoro-app/Kototoro

★569 · **v2.1.2 published Sep 14 — and on the 15th it woke up with v2.1.3** (Piece 02) · Apache-2.0 per its declared license. Manga, novels and video in one app — the tree's busiest this week (three versions in four days). It has its own complete guide in this family.

### Usagi — the one that brings no sources

The listing above. Its design difference from the other three is its identity card: no built-in sources, the user brings their own via plugins.

## 🧩 Plugins and parsers: how this tree eats

The Kotatsu tree doesn't use Mihon-style extensions: it uses parser libraries and compiled plugins. The day's pieces:

**Gekkoushi/plugin** — https://github.com/Gekkoushi/plugin — the ready artifacts for Usagi and apps with Tsuki structure. Its README (re-verified today) says: "Only for the Usagi App," "No updates, 1.3k sources" — thirteen hundred compiled sources frozen at their current state — and the UMA plugin "for version 1.0 only." That last condition matches today's reality: Usagi's only stable is 1.0.

**Gekkoushi/plugin-source** — https://github.com/Gekkoushi/plugin-source — ★90, GPL-3.0, push of Sep 13, version 1.2.6. This is where you contribute and where broken sources get reported.

**InvalidDavid/UMA** — https://github.com/InvalidDavid/UMA — ★69, GPL-3.0, tags from September 12 and 13. Automatic or manual installation of plugins for Usagi and other Kotatsu forks.

**Tsuki and TsukiMix** — the organization's own shared libraries: Tsuki (the plugins era's) and TsukiMix (the current evolution). With syncserver, the organization covers the whole sandwich: app, loading layer, parsers and sync.

The usual rule on downloads: artifacts get named, not pasted. The install click is each person's, at the project's house, the day they use it.

## 🍴 Usagi's forks

The public forks list shows 30 today on its first page, with mostly recent activity — and none with a project of its own. A fork without identity is a backup with a date: it exists, it doesn't happen. If one grows, it gets a listing the day it earns it.

## 🎭 The week's impostors

This week's search brought a brood in the same suit — inflated, identical stars (115–120 thousand), born Sep 13, classified-ad titles: "usagi-nightly," "usagi-sora-vn-sources," "komikku-scans," "translation-hub-stringsets." None is a Usagi fork or a verified source: they're click magnets with a borrowed name.

```
The impostor's suit
★ identical across several repos
An ad title, not a project title
No history: born this week
A hurry for you to link them "before they get taken down"
```

If "the new Usagi fork" somebody passed you ends up being one of these, that's exactly where the malware gets in. Usagi's house is one and has an owner: UsagiApp.

## ❓ FAQ

**Is Usagi dead?**
No. Today's push, an active organization, published on F-Droid. What got archived was the old plugins layer; what got discontinued was Yukimi, its predecessor. Each thing with its date above.

**So which is "the new fork"?**
Of the Kotatsu tree, four live today: Kotatsu-Redo, Futon, Kototoro and Usagi. There's no Usagi successor because none has been needed.

**Usagi or Kotatsu-Redo?**
Different designs: Usagi with no built-in sources (you bring them); Kotatsu-Redo inherits the original's model. Whichever covers your use, with the repo you open that day.

**Are Futon and Kotatsu-Redo the same for sharing version numbers?**
They share a numbering inheritance, not a repository. Separate listings, separate houses.

**Where are Usagi's sources?**
In the plugins layer: Gekkoushi/plugin (artifacts), plugin-source (code), UMA (installer). No recipes pasted here — the project's house explains them.

**Can I put Mihon extensions in it?**
No: another tree, another protocol. Trees don't get grafted by carelessness.

**What if somebody passes me a "Usagi Plus" APK?**
If it doesn't come from UsagiApp or F-Droid (org.draken.usagi), it's a sign. The week's impostors are the reason that rule exists.

**Why does F-Droid matter so much here?**
Because its publication went through the store's process: an identified package, a verifiable build. It's the difference between "download it from this link" and "it's in a house with a process."

## 🔗 Links

- Usagi: https://github.com/UsagiApp/Usagi · F-Droid: https://f-droid.org/en/packages/org.draken.usagi/
- Organization: https://github.com/orgs/UsagiApp/repositories
- Plugins: https://github.com/Gekkoushi/plugin-source, https://github.com/Gekkoushi/plugin — https://github.com/InvalidDavid/UMA
- Futon: https://github.com/AppFuton/Futon
- Kotatsu-Redo: https://github.com/Kotatsu-Redo/Kotatsu-Redo
- The original Kotatsu (archived): https://github.com/KotatsuApp/Kotatsu
- Kototoro: https://github.com/Kototoro-app/Kototoro

> La Bandita reports from dated sources. The app lives; the old scaffolding doesn't. And the rumor, you see, travels faster than the changelog.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: Usagi ★257 alive, Kotatsu ★8,855, Redo ★867, Futon ★427, Kototoro v2.1.3. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
