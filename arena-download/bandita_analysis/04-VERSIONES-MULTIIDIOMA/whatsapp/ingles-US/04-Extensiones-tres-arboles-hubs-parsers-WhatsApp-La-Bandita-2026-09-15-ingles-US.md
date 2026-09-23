# Piece 04 — The three trees' extensions: living hubs and the impostor brood

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 04)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🧩 What an extension is (the three layers)
├── 📗 Keiyoushi: the main hub
├── 📘 Yūzōnō: anime and the "cursed" shelf
├── 📙 The other living warehouses
├── 🧬 The KeiSource 1.6 convention (and the PR that saved it)
├── 🗂️ Miyomi: the directory of all this
├── 🎭 The impostor brood
├── 🧭 How to read a warehouse without swallowing anything
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

Extensions are the layer connecting a free reader to the sources. They don't live inside the app: they live in warehouses with owners, and each warehouse's state changes week to week. This guide reviewed today — September 14 — all the ecosystem's living warehouses, the ones that died with dates, the technical convention keeping everything running, and a brood of impostor repos that showed up this week.

The morning's state:

```
ALIVE (all with recent activity)
Keiyoushi extensions        ★14,980   push Sep 14     the main one
Keiyoushi extensions-source ★4,678    alive as of Sep 15  the code
Yūzōnō anime                ★432      push Sep 13
Yūzōnō cursed               ★185      push Sep 9
cuong-tran/manga-repo       ★445      push Sep 14
mojuru/cursed-manga-repo    ★160      push Aug 3
Suwayomi/tachiyomi-extension ★327     push Sep 12  (for the server)
Copymanga (CN community)    ★2,753    v1.4.85
ZGQ-inc/source (CN)         ★1,268    megacollection

tachiyomiorg/extensions       ★546    Jan 2024
stevenyomi/copymanga        ★1,918    Feb 2024
```

## 🧩 What an extension is (the three layers)

```
The app        the reader (Mihon, Komikku, Tadami...)
The warehouse  the place where extensions live
               (this guide)
The index      the recipe the app uses to read
               the warehouse — an installation file
```

This guide family's rule on the third layer: the index does NOT get pasted. Not because it's secret — it's in every project's README — but because pasting installation recipes into a post is exactly the gesture that turns a guide into a hook. Whoever wants the index, reads it at the project's house, the day they use it.

## 📗 Keiyoushi: the main hub

https://github.com/keiyoushi/extensions
Code: https://github.com/keiyoushi/extensions-source
Site: https://keiyoushi.github.io

The Mihon ecosystem's reference warehouse: over a thousand sources, a bot updating the index daily (the "Repository Update" runs of September 12, 13 and 14 show in its history), and a translator community pushing code every day.

Its website, opened today, carries the notice that settles half the world's doubts: if your extension list comes up empty, or everything shows "obsolete," with the "Outdated app" message — your app is no longer compatible with the warehouse. They support Mihon, TachiyomiSY and Komikku. The fix isn't hunting a mirror: it's updating the app from its repo.

A transparency detail: the binary warehouse declares no license on its page (the code does: Apache-2.0). It gets said as it is — no visible license, none invented.

## 📘 Yūzōnō: anime and the "cursed" shelf

Anime: https://github.com/yuzono/anime-extensions
Successor code: https://github.com/yuzono/kohi-den
Site: https://yuzono.github.io

The living reference channel for anime extensions on the Tachiyomi tree — and alongside it, the Kohi-den house's code stays alive in the Yūzōnō family (verified Sep 14). And the rule that rules this family: the map gets noted with the living — every link gets reopened the day it's used.

The third piece few name: yuzono/cursed-manga-extensions — the adult-content shelf (NSFW), with activity from September 9. It gets named because it exists and updates; its index doesn't get pasted nor its content recommended. What each person reads is their business and their jurisdiction's.

## 📙 The other living warehouses

**cuong-tran/manga-repo** — ★445, push of Sep 14. Extensions for Komikku/Mihon and forks. Of the independent warehouses, the most active.

**mojuru/cursed-manga-repo** — ★160, push of August 3. The ecosystem's second "cursed" shelf. Same treatment: name yes, index no.

**Copymanga-copy20** (LittleSurvival) — ★2,753, version 1.4.85 of September 8 and a "vomic" 1.4.4 of Sep 4. The Chinese source community for Mihon/Tachiyomi: its README links its community groups. Sources centered on copymanga and Chinese resources.

**ZGQ-inc/source** — ★1,268. A Chinese megacollection joining books, images, rules and even streaming sources. Named as a map of the Chinese ecosystem; what's inside doesn't get prescribed.

**Suwayomi/tachiyomi-extension** — ★327, push of September 12. A case apart: it's not for the phone, it's the extension for Suwayomi — the Tachiyomi ecosystem's desktop server (your library running on the PC, read from the browser). One more layer: server.

**uchiyomi** — ★37, MPL-2.0, and two versions published Sep 14 (v0.32.0 and v0.33.0). This layer's newcomer: a self-hosted reader running as a PWA in the browser — webtoon-first, designed for OLED screens — eating the SAME Mihon/Tachiyomi extensions. Your library on your server, read from any browser, with the whole extension ecosystem behind it. The server layer just premiered a second house — open tracking.

## 🧬 The KeiSource 1.6 convention (and the PR that saved it)

Extensions aren't loose files: they follow the ecosystem's technical convention. The current one is called KeiSource, library version 1.6. The ecosystem's contribution document (opened today, 1,813 lines) says it plainly: new sources extend KeiSource with libVersion 1.6, and the old base (HttpSource, 1.4) is legacy.

Why does it matter to someone who only reads? Because when an app "doesn't see" the new extensions, it's almost always this: the app is old for the convention. It's the other face of Keiyoushi's "Outdated app" notice.

The case confirming the transition: Animetail's PR #448 — "resolve 1.6+ extension loading" — opened today and shows merged. Readers that don't migrate in time get left out of the warehouses adopting the convention.

## 🗂️ Miyomi: the directory of all this

https://miyomi.app
Site code: https://github.com/miyomiorg/Miyomi

A community directory cataloging apps, extension warehouses and guides of the whole ecosystem — the front page reads today, and its front-end is a living web app (its internal counts couldn't be re-counted today for that same reason: the catalog lives in the browser session, not in a public JSON).

Its repo: ★189, AGPL-3.0 license, with its own code open. The project declares it hosts no content and guarantees no third party's security or legality — an index of indexes, with the honesty of someone who knows cataloging isn't auditing.

"Approved" in Miyomi means "it's in its catalog today." It doesn't mean anybody's endorsement.

## 🎭 The impostor brood

This week's search caught repos in the same suit: stars identical to each other (115–120 in several cases), same-day activity, and classified-ad titles — "Best Manga Reader App 2026," "Top Komikku Open Source Alternative," "Ultimate Multilanguage Hub for Usagi."

```
The impostor's suit
★ identical to each other (115–120 in several cases)
A propaganda title, not a project title
No history of its own: born Sep 13
A known project's name + a sales word
```

They aren't warehouses, forks or sources: they're click magnets — and, reasonably suspected, poisoned-install magnets too. The practical rule that doesn't fail: if the title sounds like an ad and the stars don't match the project's history, don't open it, don't link it, don't install it.

## 🧭 How to read a warehouse without swallowing anything

```
1. Who maintains it?
   An org's bot with history > a faceless
   account born this month.

2. How long has it pushed?
   Months/years of commit history > a single
   week of activity.

3. Is the code in the open?
   Published extensions-source > binaries only.

4. Does its site admit what it doesn't know?
   Keiyoushi warns which apps it no longer supports.
   Whoever confesses limits earns more trust
   than whoever promises infinity.

5. Does the install come from the house?
   The index gets read in the project's README,
   never in a third party's post. Not even this one.
```

## ❓ FAQ

**Which warehouse do I use with Mihon?**
Keiyoushi: its own site declares it (Mihon, TachiyomiSY, Komikku). If your list comes up empty with "Outdated app," the problem is your app's version.

**And for anime?**
Yūzōnō anime-extensions is the living reference channel; Aniyomi's official one archived in August 2024 and Kohi-den in May 2026.

**Are the "cursed" shelves dangerous?**
Their risk isn't the mechanism but the content and your jurisdiction. They get named to complete the map; the installation index doesn't get pasted in this guide family, for any of them.

**Do Keiyoushi extensions work in Usagi or Kotatsu?**
No: another tree, another parser protocol. Those live in their own houses and have their own guide.

**Is a Miyomi "approved" warehouse trustworthy?**
It's cataloged, not audited. The difference is exactly the contact-guide phone's: it's on the list, it didn't pass the exam.

**How often do I check my warehouse is still alive?**
Every time something stops updating. That's why this guide only notes the living — and every link gets reopened the day it's used.

**Where do I report a broken extension?**
At the extension code's repo (for Keiyoushi: extensions-source), with app version, source and steps. Maintainers answer steps better than complaints.

## 🔗 Links

- Yūzōnō: https://yuzono.github.io — https://github.com/yuzono/tachiyomi-extensions · https://github.com/yuzono/anime-extensions · https://github.com/yuzono/cursed-manga-extensions
- Keiyoushi: https://github.com/keiyoushi/extensions · https://keiyoushi.github.io · https://github.com/keiyoushi/extensions-source
- Warehouses: https://github.com/mojuru/cursed-manga-repo · https://github.com/cuong-tran/manga-repo
- The Chinese ecosystem: https://github.com/LittleSurvival/copymanga-copy20 · https://github.com/ZGQ-inc/source
- Desktop server: https://github.com/Suwayomi/tachiyomi-extension
- Miyomi: https://miyomi.app · https://github.com/miyomiorg/Miyomi

> La Bandita reports from dated sources. The map goes with the living.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: 7 warehouses re-counted as of TODAY (Keiyoushi ★14,980, Yūzōnō ★432, manga-repo ★445). Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
