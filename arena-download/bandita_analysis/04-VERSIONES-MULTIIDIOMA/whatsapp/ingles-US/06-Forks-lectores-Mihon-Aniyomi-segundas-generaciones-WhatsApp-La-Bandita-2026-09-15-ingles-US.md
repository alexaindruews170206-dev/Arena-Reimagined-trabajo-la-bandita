# Piece 06 — Reader forks: the living map of Mihon, Aniyomi and their second generations

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 06)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── ⚖️ The rule: being a fork isn't a criterion
├── 🌳 Today's complete tree
├── 📱 The living ones' listings
├── 🧬 What a "real fork" is (and what an adopted child is)
├── 🏗️ The infrastructure nobody sees
├── 📜 Licenses, said without a law firm
├── 🚩 Impostor signals
├── 🔍 How to read a repo in ten minutes
├── 🔄 Backups and library moves
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

Tachiyomi — the free manga reader that marked an era — closed its core in January 2024. What remained isn't "Tachiyomi with another name": it's a family of distinct projects, with their own owners, rhythms and licenses. This map got read TODAY, September 14, repo by repo:

```
━━ The manga trunk ━━
Mihon              ★23,601   v0.20.4 (Aug 5)    push TODAY (Sep 15)
TachiyomiSY        ★4,146    1.13.2 (Jul 13)    push Sep 13    fork
TachiyomiSYPreview ★483      previews host      push Aug 25
Komikku            ★4,721    v1.14.1 (Jul 17)   push Sep 11   adopted
Neko               ★2,792    MangaDex reader    push Sep 14     specialist

━━ The anime branch (manga + anime) ━━
Aniyomi            ★7,683    push Sep 14         mother branch
Anikku             ★1,032    v0.2.0 (Sep 11)    anime, the Komikku org
Aniyomi-preview    ★641      previews host      push Sep 14
Animetail          ★579      v0.20.4.0 (Aug 5)  push Sep 7    fork
Tadami             ★260      v0.62 (Sep 12)     push Sep 13   fork (alive)

```

No star installs anything. No kinship guarantees anything. The rule goes first.

## ⚖️ The rule: being a fork isn't a criterion

Something being a fork, variant or renaming of a beloved project isn't, by itself, a reason to use it. The four doors that do count:

```
Real use          someone of flesh and bone uses it
                  and can tell how it goes
Uniqueness        does it do something what you already
                  have doesn't? "It's a fork of X" is not
                  a feature
Public maturity   docs, signed versions, an author
                  who answers. A last push from 2024
                  doesn't pass this door unflagged
A purpose of      a new icon isn't a purpose;
its own           a changed engine is
```

This guide names repos with URL, license, version and last push — read on the 14th and re-read at the move (Sep 15). "The best" doesn't appear: it doesn't exist in the abstract. The one existing is whichever covers what you read, with the shop open.

## 🌳 Today's complete tree

```
Mihon (the ecosystem's living trunk)
   ├── Mihon            the de facto successor (the largest)
   ├── TachiyomiSY      the classic fork that stays alive
   ├── Komikku          adopted child with its own life (a new repo)
   ├── Neko             the MangaDex specialist
   └── (dozens of forks with no project of their own:
        not listed for being forks)

Aniyomi (manga + anime, of the same lineage)
   ├── Animetail        declares itself "Official fork"
   ├── Tadami           manga + anime + ranobe (the youngest)
   └── Anikku           the Komikku org's anime client

Kotatsu: ANOTHER tree (GPL, own parsers)
   → Kotatsu-Redo, Futon, Kototoro, Usagi
   → they have their own guide in this family
```

## 📱 The living ones' listings

### Mihon — the trunk

https://github.com/mihonapp/mihon

★23,601 · version 0.20.4 (August 5) · TODAY's push (re-verified Sep 15) · Apache-2.0. It's the map's largest free manga reader, and Tachiyomi's de facto successor. Its translation community pushes code daily; its versions ship when they ship — August's is the current one, and today's push doesn't mean a new APK.

Keiyoushi (this family's extensions guide) names it first in its compatible-apps list.

### TachiyomiSY — the living one with the old name

https://github.com/jobobby04/TachiyomiSY

★4,146 · version 1.13.2 (July 13) · push of Sep 13 · Apache-2.0. The classic fork — extra sources, reading tweaks — still open. And the notice worth its entry: the living SY is this one — the name isn't enough; the owner is.

Its mother project also keeps a test-build host: TachiyomiSYPreview (★483) — experimental versions for the curious, not the daily route.

### Komikku — the adopted child with its own shop

https://github.com/komikku-app/komikku

★4,721 · version 1.14.1 (July 17) · push of Sep 11 · Apache-2.0. GitHub's API doesn't declare it a fork (it's a new repo); its README tells the lineage. These are the "adopted children": projects that inherit the code and are born with their own house. Its organization also maintains Anikku (below).

### Neko — the specialist

https://github.com/nekomangaorg/Neko

★2,792 · yesterday's push (Sep 14) · "Unofficial MangaDex Reader for Android 8+". A whole reader devoted to a single source: MangaDex. It's of the Tachiyomi fork lineage, but its own purpose is crystal clear: doing one thing well. For whoever lives on MangaDex, it's a listing of its own; for the rest, it's a hammer shaped like a screwdriver.

### Aniyomi and its heirs

https://github.com/aniyomiorg/aniyomi

★7,683 · push of Sep 14 · Apache-2.0. The manga+anime mother branch. Almost a year without a new version but with code moving this month: a mature branch, not a corpse. Its previews host: aniyomiorg/aniyomi-preview (★641).

**Anikku** — https://github.com/komikku-app/anikku — ★1,032 · version 0.2.0 published September 11 · release r8932 in view TODAY Sep 15 · the Komikku organization's "anime watcher." The most active of the anime branch this month.

**Animetail** — https://github.com/Animetailapp/Animetail — ★579 · v0.20.4.0 · push of Sep 7 · Apache-2.0. It declares itself "Official fork of Aniyomi" in its description. The label is its own — no aniyomiorg seal was seen ratifying it; it gets said as it is.

**Tadami** — https://github.com/andarcanum/Tadami-Aniyomi-fork — ★260 · version 0.62 (September 12) · push of Sep 13 · Apache-2.0. **Rectification (Sep 15, night): ALIVE — ★260, push of the 13th; the afternoon's record got the wrong house (detail in Piece 13).** The branch's youngest: three versions in a month (0.60 → 0.62), manga + anime + light novels (ranobe). Of the declared forks, the fastest-evolving.

## 🈁 The immersion layer (its own guide in piece 17)

Today's map premieres territory: two living projects of the ecosystem's Japanese layer. **Chimahon** (★198, GPL-3.0, v2.4.2 of TODAY Sep 15) is a Mihon fork for studying while reading: native Yomitan dictionary, Mokuro manga, EPUB novels and instant mining into Anki. **Yomi Reader** (★10, Apache-2.0, v0.1.7 of Sep 6) is the young triple — anime, manga and novel — compatible with Tadami/Aniyomi extensions. The complete listings, with Hoshi Reader, Yomikai and the Komga client "Koharia," live in piece 17.

## 🧬 What a "real fork" is (and what an adopted child is)

GitHub's graph and reality don't always agree:

```
Declared fork    the API says it: field fork = true,
                 with a visible parent. Animetail, Tadami.
                 Not argued.

Adopted child    a NEW repo that inherits the code and declares
                 the lineage in its README. Mihon, Komikku,
                 Anikku. The graph says "not a fork";
                 the README says where it's from. Both
                 are true: that's why both get read.

Build host       not an app: it's a launching apparatus
                 for the mother project's test versions.
                 SYPreview, aniyomi-preview.

Fork of a fork   what builds the counterexample: a copy of
                 a copy with no shop of its own. Usually dies
                 without announcing it.
```

When somebody recommends you "a fork," the useful question isn't whose child is it? but who's pushing code this week?

## 🏗️ The infrastructure nobody sees

Two pieces of the ecosystem aren't readers but hold everybody up:

**SyncYomi** — https://github.com/syncyomi/syncyomi — ★710, yesterday's push (Sep 14) · v1.5.4 (Sep 10). Library sync between devices and between forks of the Tachiyomi lineage: your progress follows you if you switch readers within the family. A light server and the client on the phone.

**Suwayomi** — the ecosystem's desktop server (your library running on the PC, read from the browser). Its extension got reviewed in this family's extensions guide; the project lives with activity from this month.

Naming them here is avoiding the classic error: confusing the app with the layer accompanying it.

## 📜 Licenses, said without a law firm

What each repo's page declared the day of verification (Sep 14):

- **Apache-2.0** — Mihon, TachiyomiSY, Komikku, Aniyomi, Animetail, Tadami. In general terms: use, modify and redistribute keeping the notices and the change note.
- **GPL-3.0** — the Kotatsu tree (Kotatsu-Redo, Futon, Usagi, Kototoro per its declared license). Whoever redistributes modifications, distributes them under the same license.

This isn't legal advice: it's each page's license field, read today. If someone is going to redistribute a modified APK, let them open the license's full text that day. And a golden notice: an "SY mod premium" APK in a mods store does NOT inherit the repo's Apache-2.0 trust — it inherits the store's.

## 🚩 Impostor signals

- High stars, last commit from 2024, a README promising "active development."
- Same name, other owner — and this week's SEO impostors (ad titles, clonic stars).
- An APK on Telegram "more updated than GitHub." The updated lives in Releases, with tag and date.
- A "Nightly" with no CI, no tag, no build record.
- A fork of an archived project that doesn't declare its parentage.
- It asks you to paste an extension index on the first screen.

No single signal is enough. Several together, you parasitize.

## 🔍 How to read a repo in ten minutes

```
1. Open the repo's HTML, not a group's screenshot.
2. Does it say Archived? The dead get read just as fast.
3. License: the page's field (or the LICENSE file).
4. Releases: tag and date of the last version.
   Today's push isn't a new version.
5. pushed_at ≠ release: a repo can push
   translations all month without shipping an APK.
6. Is it a fork? The page's/API's fork field says so;
   if it's an adopted child, the README tells it.
7. Does the author answer issues? Look at two random
   threads before trusting it your library.
```

## 🔄 Backups and library moves

What can be said without prescribing anything:

- Each reader of the family has its backup format; formats look alike, no guarantee they're identical across versions or cousins.
- A 2024 backup isn't verified against the August 2026 version — of any reader.
- "Export and done" is an advertising promise, not an engineering one: ALWAYS test on a copy, never on your only library.
- If your progress matters to you, SyncYomi (above) exists for that — and also back up the backups: periodic manual export.
- Kototoro's backup episode (the 1.4–1.7 series) is documented in its own guide; it works as a reminder that big migrations get rehearsed dry.

## ❓ FAQ

**Which do I install?**
The one you'll use and verify. Manga in general: Mihon is the trunk with the most community. Classic SY style with extras: jobobby04's TachiyomiSY. MangaDex exclusively: Neko. Anime besides manga: Aniyomi or its heirs (Anikku moved the most this month). No recommendation replaces opening the release the day you install.

**Is Mihon Tachiyomi?**
No. Tachiyomi closed. Mihon is another repo, alive today, that inherited the model.

**Komikku or TachiyomiSY?**
Two living ones with different styles. Today Komikku has more stars (4,721 vs 4,146); SY pushed Sep 13 and Komikku the 11th — records of the 14th, both alive as of the 15th. No number chooses for you.

**Is Anikku AniZen?**
No — but they're family. AniZen declares itself a rebrand of "Anikku Mod" (it has its own guide in this family). Anikku is the Komikku organization's app, with version 0.2.0 of September 11. Declared kin, different repos.

**Does Neko work for everything?**
For MangaDex, wonderfully. For the rest of the manga universe, use a general reader.

**Are the "preview" hosts for installing?**
They're for testing and reporting. For the day to day, the mother repo's stable version.

**And the 200 forks you didn't list?**
Being a fork doesn't score. The ones with a project of their own are up top; the ones without are copies with a clock.

**Discord?**
This family has no Discord delivery channel. Its guides live here.

## 🔗 Links

- Mihon: https://github.com/mihonapp/mihon
- Neko: https://github.com/nekomangaorg/Neko
- TachiyomiSY: https://github.com/jobobby04/TachiyomiSY — previews: https://github.com/jobobby04/TachiyomiSYPreview
- Aniyomi: https://github.com/aniyomiorg/aniyomi, previews: https://github.com/aniyomiorg/aniyomi-preview
- Komikku: https://github.com/komikku-app/komikku · Anikku: https://github.com/komikku-app/anikku
- SyncYomi: https://github.com/syncyomi/syncyomi
- Animetail: https://github.com/Animetailapp/Animetail — Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork
- The Kotatsu tree: guide 07 · The ecosystem's extensions: guide 04 of this family

> La Bandita reports from dated sources. A fork isn't a reason. The living repo is. And the owner, more.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: 8 listings re-counted (Mihon ★23,601, Komikku ★4,721, SY ★4,146, Neko ★2,792, Anikku ★1,032 + r8932) and the Tadami rectification (alive). Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
