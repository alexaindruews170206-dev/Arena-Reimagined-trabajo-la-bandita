# Piece 09 — FOSS tools: the trade box, every piece with its sharpening date

**La Bandita · September 15, 2026 · US English edition (adapted from the Spanish original, piece 09)**

## 🗺️ Map of this guide

├── ⚡ On one page
├── 🖼️ Gallery and files
├── 🔐 Keys and second factor
├── 📲 Transferring and connecting
├── 🧰 The system drawer
├── 🗺️ Maps
├── 📦 How installations get managed
├── 📌 Why 20 pieces and not 200
├── ❓ FAQ
└── 🔗 Links

## ⚡ On one page

April's tools codex expired — old versions sold as current, lists inflated for the sake of inflating. This is the cutoff's box, September 15 (measured on the 14th, re-verified at the move): every piece with its repo opened in the last hours, its real state and its work. Short curation on purpose: twenty pieces covering the trade, all verified, zero filler.

The box, by drawers:

```
GALLERY AND FILES
Fossify Gallery ★3,696 · File-Manager ★1,753 · Phone ★1,329
Calendar ★2,156 · Clock ★698            (pushes verified Sep 14)
Amaze File Manager ★6,387               the material alternative

KEYS AND SECOND FACTOR
KeePassDX ★7,301 · September releases
Aegis Authenticator ★13,086             2FA with an encrypted vault

TRANSFER AND CONNECT
LocalSend ★91,047                       the free AirDrop
Orbot ★3,538                            Tor in your pocket

SYSTEM
Termux ★60,797 · App Manager ★8,972 (v4.1.1)
Shizuku ★30,121                         system APIs without root

MAPS
Organic Maps ★15,415                    offline, for real

INSTALLATIONS
Obtainium ★19.7k                        (listing in the stores guide)
```

## 🖼️ Gallery and files

### Fossify — the family that replaced the Simple ones

https://github.com/FossifyOrg

When Simple Mobile Tools filled up with ads, the community forked the whole set and kept it free: that's how Fossify was born. Today the family pushes code this very week, piece by piece:

- **Gallery** (★3,696) — the ad-free gallery that respects your photos.
- **File-Manager** (★1,753) — simple, honest files. Watch the name: FossifyOrg/Files doesn't exist; the canonical one is File-Manager.
- **Phone** (★1,329) — dialer and number blocking, with dual SIM.
- **Calendar** (★2,155) — a calendar with events and widgets, no tied account.
- **Clock** (★699) — clock, alarm, stopwatch and timer.

GPL-3.0 all of them. Their tagged versions are from February; their pushes, from September: the mature-project pattern — calm stables, continuous maintenance.

### Amaze File Manager — the alternative with pedigree

https://github.com/TeamAmaze/AmazeFileManager

★6,387 · alive. The good old material file manager, among the free Android ecosystem's most veteran. If Fossify feels too minimalist to you, this is the option with more years on it — and with roots in the community since the first ROMs era.

## 🔐 Keys and second factor

### KeePassDX — the compatible vault

https://github.com/Kunzisoft/KeePassDX

★7,301 · GPL-3.0 · push of Sep 11. The week brought three releases to the project, with cat names: "Scholarly Student" (Sep 2), "Cutie Cat" (Sep 4) and "Clever Cat" (Sep 10). A password vault compatible with the KeePass format: your databases open on any platform of the KeePass ecosystem, without staying anybody's prisoner. The data lives in YOUR file — cloud optional, not mandatory.

If at some point you typed a password into a site that later fell (this family's TMO guide tells one big story), this is the kind of tool that puts the house in order afterward: one vault, distinct passwords per site, encrypted backup.

### Aegis Authenticator — the second factor that's yours

https://github.com/beemdevelopment/Aegis

★13,086 · GPL-3.0 · alive. Two-step verification codes, in a free app with an encrypted vault (AES-256 per its documentation), fingerprint unlock, an exportable encrypted backup and imports from the most common proprietary apps (Google Authenticator, Authy, Microsoft, 2FAS and others, per its official list). The background argument: your 2FA codes are the key to your digital life — depositing them in a closed app with no export is leaving the keys with the locksmith without a copy.

## 📲 Transferring and connecting

### LocalSend — everybody's AirDrop

https://github.com/localsend/localsend

★91,047 — yes, ninety-one thousand — · alive · MIT per its listing. The quiet revelation of recent free software: passing files between phone, PC, tablet and even the neighbor's phone with no cables, no cloud and no accounts — local network, open protocol, apps for every platform. If you came from pasting files through WhatsApp "to get them to the PC," this piece alone justifies the whole guide.

### Orbot — Tor in your pocket

https://github.com/guardianproject/orbot

★3,538 · alive · from the Guardian Project. The app routing your traffic through the Tor network on Android, with a built-in VPN or as a per-app proxy. It's not for all day nor for everybody: it's the connection tool when the circuit you need requires real anonymity — journalism, research, or simply leaving the country without leaving home. From the ecosystem's serious side.

## 🧰 The system drawer

### Termux — the pocket terminal

https://github.com/termux/termux-app

★60,797 · push of Sep 11. A complete Linux terminal on Android: editors, languages, ssh, scripts. The entry door to "doing it for real" with the phone. Its GitHub-tagged version is from May 2025 (with 0.119 betas) — its package channel goes its own way at its own rhythm; the old GitHub-vs-F-Droid Termux debate doesn't get reopened here: repo named, channel chosen the day you install. One rule though: nobody's scripts get pasted — the terminal is power, and power gets executed with what you wrote or read in full.

### App Manager — your apps' X-ray machine

https://github.com/MuntashirAkon/AppManager

★8,985 · **version 4.1.1 (September 4)** · TODAY's push (re-verified Sep 15). The complete package manager: see what permissions each app asks, what activities it exposes, what trackers it drags, and uninstall deep. It corrects last week's picture, when the version didn't answer in the API: today it's there, and from this month. Its license shows on the page as its own (a proprietary-style free license — the project defines it in its repo; read there before redistributing).

### Shizuku — the system's APIs without root

https://github.com/RikkaApps/Shizuku

★30,121 · Apache-2.0 · version 13.6.0. The piece that changed the "without root" game: it lets authorized apps use system APIs directly, with permissions granted via ADB (once per boot) or root. It's the silent engine behind half a dozen modern customization and control tools. Not for beginners: for whoever already knows why they're looking for it.

## 🗺️ Maps

### Organic Maps — the map that doesn't look back

https://github.com/organicmaps/organicmaps

★15,427 · August release (2026.08.27) · TODAY's push (re-verified Sep 15). Complete offline maps of the planet, no account, no tracking, OpenStreetMap data. For travel, for the neighborhood with no data, for whoever decided Google doesn't need to know where you walk. Its license shows on the page with a particular notice (the project's own license, readable in its repo) — said as it is, no labels invented.

## 📦 How installations get managed

**Obtainium** — https://github.com/ImranR98/Obtainium — ★19.7k (19,702), commit of Sep 13. The tool watching this box's repos and installing new versions the moment they ship. Its full listing lives in this family's stores guide; here its sentence is enough: the toolbox updates itself too.

And the box's bottom, for all the drawers: **F-Droid** — the free store where a good part of these pieces also lives published. Three routes (GitHub repo, F-Droid, Obtainium) pointing at the same software: that's the free ecosystem's healthy redundancy.

## 📌 Why 20 pieces and not 200

April's codex carried 88 tools. Of those, many were in old versions sold as new, and several repeated one function four times. This box's criterion is the opposite:

```
One function, one piece   if two apps do the same,
                          the livelier one stays — not the more mentioned
Everything verified today if the number wasn't opened today,
                          it doesn't carry today's date
A declared gap            what is NOT in the box (browsers,
                          mail, messaging, clouds) is because
                          it deserves its own guide, not because it doesn't exist
```

The trade box doesn't need to be infinite. It needs to be true.

## ❓ FAQ

**Are these apps on the Play Store?**
Several are (Aegis, LocalSend, Organic Maps among them). The free ecosystem's route is F-Droid or the repo — this family's stores guide explains the three doors. This guide doesn't open Play: each store's listing is its own piece's topic.

**Fossify or Amaze for files?**
Fossify: minimalist, from the complete family (gallery, contacts, calendar). Amaze: more function per screen, more flight years. Try both: they're free in every sense.

**KeePassDX or Bitwarden?**
Different philosophies: KeePassDX keeps YOUR file (KeePass-compatible, zero dependency); Bitwarden is a service with its own sync. Not compared in depth here: no invented comparison.

**Is Shizuku dangerous?**
It gives system power to apps YOU authorize, via ADB or root. It's as dangerous as the key under the doormat if you authorize anybody. With a cool head, it's the perfect bridge between "no root" and "total control."

**Does LocalSend work between iPhone and Android?**
Yes: that's part of its point — full cross-platform (Android, iOS, Windows, macOS, Linux), local network, no cloud.

**Does Orbot slow everything down?**
Tor pays for its anonymity with latency. For sensitive browsing, that's the price. It isn't meant for all day — and its own documentation says it better than this summary.

**Does Termux need root?**
No. Its power doesn't depend on root — it depends on what you know how to do with a terminal. Root opens other chapters, with other risks (this family's GLTools guide tells why that isn't played with from the couch).

**How often does this box get re-verified?**
Every time it gets used. Today was the cutoff; numbers not opened another day don't get quoted as fresh.

## 🔗 Links

- Fossify: https://github.com/FossifyOrg/Gallery — https://github.com/FossifyOrg/File-Manager — https://github.com/FossifyOrg/Phone, https://github.com/FossifyOrg/Clock · https://github.com/FossifyOrg/Calendar
- Amaze: https://github.com/TeamAmaze/AmazeFileManager
- LocalSend: https://github.com/localsend/localsend — Orbot: https://github.com/guardianproject/orbot
- Termux: https://github.com/termux/termux-app — Shizuku: https://github.com/RikkaApps/Shizuku · App Manager: https://github.com/MuntashirAkon/AppManager
- Obtainium: https://github.com/ImranR98/Obtainium
- KeePassDX: https://github.com/Kunzisoft/KeePassDX · Aegis: https://github.com/beemdevelopment/Aegis
- Organic Maps: https://github.com/organicmaps/organicmaps

> La Bandita reports from dated sources. A trade box doesn't get inflated: it gets sharpened.

---

**Move note (Sep 15):** guide moved from the Sep 14 batch to this one, with re-verification against the houses: AppManager ★8,985 and OrganicMaps ★15,427 with TODAY's push; Calendar ★2,156, Clock ★698. Whatever isn't mentioned stays checked on its day (Sep 14). Full record: Register #71.
