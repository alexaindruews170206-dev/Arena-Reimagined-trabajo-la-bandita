# Piece 01 — APK stores: the legal store, the mods sign and the 2027 clock

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 01)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🏪 The stores that count (listing by listing)
├── 🧰 The installers that bring the stores to you
├── ⚠️ The mods signs (they get named, not prescribed)
├── 🕐 The 2027 clock and the side door
├── 🧭 What to check before installing any APK
├── 🚩 Bait signals
├── ❓ FAQ
├── 📚 Keywords of this guide
└── 🔗 Links

## ⚡ On one page

An APK store is a place with a known owner that lets you install apps outside the phone's official store. There are two kinds: the ones that review, sign and answer for what they publish — and the ones living off mods traffic, where "free premium" arrives with a surprise gift inside the file.

This guide walks the free ecosystem's legitimate stores, one by one, with their real state as of September 15, 2026: which one is under threat, which shipped a version yesterday, which changed houses days ago. And it ends with the clock: Google's developer verification policy already has a public countdown.

If you came here for "free Spotify premium" or "games with everything unlocked," this guide won't walk with you: that's not a store, it's a hook with a wallet.

## 🏪 The stores that count (listing by listing)

### F-Droid — the mother house

https://f-droid.org

The historic store of free software on Android. Everything it publishes goes through reproducible builds: the file you download can be reconstructed from the public code, and if it doesn't match, it doesn't ship. That's the core promise, and it's the one no mods store can match.

Seen on Sep 14: the site keeps its campaign banner — "F-Droid is under threat" — within Google's developer verification program that this very guide times below. The store's own installer downloads straight from its site.

If you'll only pick one store from this list, pick this one. It's the oldest, the most reviewed, and it holds the free ecosystem's strictest publishing standard.

```
F-Droid in a box
What it is:   store and repository of free apps
Promise:      reproducible builds, no declared trackers
State on its day (Sep 14):  alive, "under threat" campaign active
For whom:     everybody; the natural entry point
```

### IzzyOnDroid — the respected annex

https://apt.izzysoft.de/fdroid

The best-known complementary repository of the F-Droid ecosystem: many apps that haven't entered the main channel yet publish here first. A trusted warehouse inside the community, maintained for years.

Seen on Sep 14: the site responds; its loading depends on JavaScript, so the browser assembles it at its own pace. Nothing alarming: it's the same site as always.

### Droid-ify — the modern F-Droid client

Canonical repo: https://codeberg.org/droidify/client
GitHub mirror: https://github.com/Droid-ify/client

A client for consuming F-Droid-style catalogs with a modern interface. Version 0.7.8 shipped September 12: it brings repo correction right after importing it, QR-code import, an installer for root holders, and adaptive Material You theming.

A detail that matters: the project declares its official house is Codeberg and its GitHub page is only a mirror. When a project names another domain canonical, that's the link that rules — this guide's rule is simple: canonical first.

```
Droid-ify in a box
What it is:   client for F-Droid repositories
Latest:       0.7.8 — September 12, 2026
House:        codeberg.org/droidify/client (GitHub is a mirror)
Extras:       QR, root installer, dynamic theme
```

### Neo-Store — the client with the tracker compass

https://github.com/NeoApplications/Neo-Store

Another client of the F-Droid ecosystem, with usability details its community polishes. Its most recent move (the September 13 commit) is a design gem: it's replacing each listing's static tracker block with control actions — and gives you a shortcut to Exodus Privacy to audit any installed app.

That's what a mature store idea looks like: not just letting you install, but handing you the instrument to know what you're installing. The stable version is 1.2.6.

### Komi Store — the one that changed houses (and says so out loud)

https://github.com/komi-store/komi-store
Site: https://komistore.app

This listing exists because a house change confuses people. Komi Store used to be called "GitHub Store" and lived in another organization; it moved to the komi-store organization, premiered its own domain (komistore.app) and is on version 1.9.3 (code 22). The move is declared by the project itself in its repository — 18,500 stars and activity from early September.

The difference between "it moved" and "it got cloned" is this: the move gets announced by the owner, in the repo, with history. The clone appears out of nowhere, with someone else's name and a hurry for you to install. Komi did the first one.

### Aurora Store — the door to another catalog

https://gitlab.com/AuroraOSS/AuroraStore

The free client that queries Google's store catalog without surrendering your account: anonymous sessions, searches and updates, without exposing your main identity. It's one of the free ecosystem's most installed pieces and has serious infrastructure behind it.

Seen on Sep 14: the most recent tagged version is 4.8.4, with repository activity from recent weeks. And a detail that says a lot about the project: its most recent documentation commit is exactly this — "declare AI use in development." Transparency declared voluntarily. That, in a mods store, doesn't exist and won't.

### Accrescent — the young one with high standards

https://accrescent.app

The youngest store on the list, in alpha, with Android 10 as the minimum. It isn't "one more F-Droid": its bet is security by default — strict signature verification (key pinning), signed metadata, automatic updates without extra privileges on Android 12 or above, split-APK support and zero accounts.

It's also found inside the GrapheneOS store, a good thermometer of who the paranoid-for-good-reasons community listens to.

```
Accrescent in a box
What it is:   a security-first store, in alpha
Minimum:      Android 10
Signing:      key pinning + signed metadata
Accounts:     none
Via:          its own site and the GrapheneOS store
```

### Appteka — the community market (with a magnifying glass)

https://appteka.store
Client code: https://github.com/solkin/appteka-android

A community-run market with a big catalog (it declares 320,000 applications) and its own client: the client's official version is 23.0, weighs under 4 MB and asks for Android 6 and up. The site lives and responds.

It makes the "yes" list but with a magnifying glass: being a community catalog, its publishing standard isn't F-Droid's. It works, and in exchange it asks what this whole guide repeats: look at the file's owner before installing.

Inside Appteka live listings of concrete apps that this guide cites as state examples — for instance, the pages of the two Rebuild projects, open today with the client's 23.0 version visible in their titles. They're cited as proof of the market's life, not as a recommendation of those specific apps.

## 🧰 The installers that bring the stores to you

Recent years brought a new figure: tools that aren't stores with a storefront, but installers that build your own made-to-measure store, following the repositories you point them to.

### Obtainium — the app that watches the repositories for you

https://github.com/ImranR98/Obtainium

The most popular of its kind: you tell it which repositories matter to you and it watches their releases, downloading and installing new versions the moment they ship. As of TODAY, Sep 15, it counts about 19,700 stars and yesterday's commits — among the most alive projects on this whole map.

Its own README credits ObtainX as the ecosystem's external installer. That's also a maturity signal: knowing how to name your neighbors.

### ObtainX — the installing arm

https://github.com/bikram-agarwal/ObtainX

Alive (checked Sep 14). The Obtainium ecosystem's installation complement: the link between "I detected a new version" and "it's installed on the phone."

### Omnify — the F-Droid client with no noise

https://github.com/Victor-root/Omnify
Site: https://victor-root.github.io/Omnify/

Alive on its day (Sep 14), with its landing loading: it introduces itself as "a no-clutter F-Droid client that installs apps from anywhere." One of the new bets on making free-catalog consumption friendlier.

```
The three in one line each
Obtainium:  watches releases and warns you
ObtainX:    runs the installation
Omnify:     lightweight F-Droid client
None of the three asks you to leave the legal route.
```

## ⚠️ The mods signs (they get named, not prescribed)

These names exist so you recognize them, not so you visit them:

- **Espacio APK** — a live site (checked Sep 14), a catalog of "popular apps and games." Its real product: mods with premium promises.
- **HappyMod** — responded on Sep 14 with no readable title (an anti-bot shield). Its business model: mods uploaded by anybody, with no serious chain of custody.
- **Liteapks** — alive (checked Sep 14), advertises itself as "#1 in MOD APK." Number one in mods is, by definition, number one in unreviewed files.

The common pattern: they promise you the paid stuff free, they ask for permissions the original app doesn't ask, and if something breaks there's neither repo nor owner to claim against. The "mod" often isn't even the original app: it's another app dressed in its icon.

No links go here. The name already did its job: if it shows up in a group with "download it from here," you know what it is.

## 🕐 The 2027 clock and the side door

The framework changing all of this has a date and a public clock.

Google's plan — "Android developer verification" — requires apps on certified devices to be registered by verified developers. The first milestone lands September 30, 2026: four countries (Brazil, Indonesia, Singapore, Thailand), seven stores (Google Play, HONOR, OPPO, Galaxy Store, Palm Store, V-Appstore and GetApps), Android 7 and up.

In 2027 the filter reaches all apps on certified devices. The Keep Android Open campaign keeps its public counter today: 110 days — and its FAQ already places the lockdown around January 2027. Two calendars, the same message: sideloading's time as we know it is counted.

The side door Google opened this month: limited distribution accounts. For students, teachers and hobbyists — up to 20 devices, no government ID and no fee. A small relief with a hard ceiling: twenty devices don't sustain a community project.

```
The clock, in two lines
Sep 30, 2026: 4 countries, 7 stores, Android 7+
2027:         all apps, certified devices
The campaign's counter (as of Sep 14): 110 days
```

What this means for the free ecosystem: F-Droid with its threat banner, Accrescent building security from today, and every store in this guide knowing its model plays its future in the coming months. Nobody on this list stands still — and that may be the best signal of all.

## 🧭 What to check before installing any APK

```
1. Where does it come from?
   A repo or site with history > a link from a group.

2. Who signs it?
   The project declares its signature; if the file doesn't
   match that signature, it's something else.

3. What does it ask for?
   Permissions the original app doesn't ask = a reason.

4. Is it in more than one serious store?
   F-Droid + own repo + IzzyOnDroid = a triple route.
   Only on a mods site = no route at all.

5. What do the auditors say?
   Exodus (trackers), VirusTotal (multiple engines),
   the project's repo (real user issues).

6. Is there a hurry?
   "This link for 24 hours only" is the grammar of bait.
   The good stuff is still there tomorrow.
```

## 🚩 Bait signals

- The search engine's top ad for "download X" pays more than the legitimate result. Whoever pays for the ad isn't the project.
- "Modified version," "premium unlocked," "everything unlimited": somebody modified something — what it doesn't tell you is what else they put inside.
- The page asks you to disable the phone's protection to "complete the installation." No serious store needs you to drop your security drawers.
- Cloned comments across several pages with the same phrases.
- The browser's padlock: it only says the connection is encrypted. Banks have it, and so does phishing.

## ❓ FAQ

**Where do I start from zero?**
F-Droid. It's the door with the most history, the most review and the most community. The rest hangs from it: IzzyOnDroid as the annex, and whichever client you like (Droid-ify or Neo-Store) to handle the catalog comfortably.

**Are F-Droid apps 100% safe?**
No store promises that. F-Droid promises transparency: reproducible builds and a declared policy. It's the free ecosystem's highest standard, not a magic wand.

**Why are there two houses for Droid-ify (Codeberg and GitHub)?**
Because the project declares it that way: Codeberg is canonical, GitHub the mirror. When a project declares its house, the house rules. It's the same "the living repo yes" logic this guide family repeats.

**Are Komi Store and "GitHub Store" the same?**
Yes — it moved organizations and documents it in its repo, with its own domain. The migration gets told by the owner; the clone has no owner to tell it.

**Is Aurora Store "the illegal Google store"?**
No. It's a free client that queries that catalog without your account. The project declares it and maintains it with recent activity — it even declares in its documentation when it uses AI in development.

**Do limited distribution accounts let me "distribute" my app to the group?**
Twenty devices is a closed circuit: tests, class, home. For anything wider, the route is another (and every route demands its own).

**And mods? Never?**
This guide doesn't prescribe them or link them. If somebody insists, let it be with the signature checked and the risk signed by whoever insists — which is never whoever loses the data.

**Does September 30 lock my phone?**
No. That milestone hits participating stores in four countries. Your change arrives with the global rollout in 2027. Reopen this guide the day you decide something: the map moves.

## 📚 Keywords of this guide

```
APK          an Android app's installable package
Sideload     installing outside the system's store
Reproducible the file comes out identical rebuilt from the code
Key pinning  the project's signature is tied in advance
Split APKs   the package arrives in parts per architecture
Exodus       a public audit of trackers in apps
Repo         repository: the house of the code (and of the truth)
```

## 🔗 Links

- F-Droid: https://f-droid.org
- IzzyOnDroid: https://apt.izzysoft.de/fdroid
- Droid-ify (canonical): https://codeberg.org/droidify/client — mirror: https://github.com/Droid-ify/client
- Accrescent: https://accrescent.app
- Neo-Store: https://github.com/NeoApplications/Neo-Store
- Komi Store: https://github.com/komi-store/komi-store, https://komistore.app
- Appteka: https://appteka.store · client: https://github.com/solkin/appteka-android
- Aurora Store: https://gitlab.com/AuroraOSS/AuroraStore
- Obtainium: https://github.com/ImranR98/Obtainium — ObtainX: https://github.com/bikram-agarwal/ObtainX
- Omnify: https://victor-root.github.io/Omnify/ · https://github.com/Victor-root/Omnify
- Developer verification: https://developer.android.com/developer-verification
- Campaign: https://keepandroidopen.org

> La Bandita reports from dated sources. The legal store gives you something the mod never will: an owner to hold accountable.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: the state date. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.

**Final verification note (Sep 15, night):** Omnify's own site (victor-root.github.io/Omnify) returns 404 at this hour, checked live; the GitHub house is still alive (★20, v1.0.5-beta.6 of Sep 4). Links get reopened the day they're used — the house's rule.
