[GUIDE] Verified open-source top 20 — a 493-repo census (cutoff: Sep 15, 2026)

## [GUIDE] Verified open-source top 20 — a 493-repo census (cutoff: Sep 15, 2026)

**What this is:** a short list of open-source recommendations with verified numbers. This is not my software or my group's: it's a census of third-party repos, measured and published with a date. Small hobby project among friends, no official support — saying it up front so nobody expects guarantees.

**How it was verified:** GitHub REST API (stars + activity) + liveness probes per repo + HTML control re-scraping on 351 suspicious zeros (the first API pass hit its rate limit mid-census — the zeros weren't published: they were re-checked). Single cutoff: September 15, 2026. If a number changes, there's a dated correction, never a silent one.

## The list (top 20, deduplicated, by stars)


1. **awesome-selfhosted** — ★319,420 — github.com/awesome-selfhosted/awesome-selfhosted
2. **llama.cpp** — ★128,330 — github.com/ggml-org/llama.cpp
3. **immich** — ★114,266 — github.com/immich-app/immich
4. **photoprism** — ★40,195 — github.com/photoprism/photoprism
5. **sing-box** — ★38,031 — github.com/SagerNet/sing-box
6. **SmartTube** — ★33,687 — github.com/yuliskov/SmartTube
7. **ente** — ★28,906 — github.com/ente/ente
8. **mlc-llm** — ★23,160 — github.com/mlc-ai/mlc-llm
9. **xbmc** — ★21,221 — github.com/xbmc/xbmc
10. **komi-store** — ★18,518 — github.com/kurikomi-labs/komi-store
11. **FreshRSS** — ★16,028 — github.com/FreshRSS/FreshRSS
12. **FlareSolverr** — ★15,600 — github.com/FlareSolverr/FlareSolverr
13. **ImageToolbox** — ★14,628 — github.com/T8RIN/ImageToolbox
14. **thunderbird-android** — ★13,998 — github.com/thunderbird/thunderbird-android
15. **android-foss** — ★11,200 — github.com/offa/android-foss
16. **uhabits** — ★10,250 — github.com/iSoron/uhabits
17. **flutter_server_box** — ★8,705 — github.com/lollipopkit/flutter_server_box
18. **floccus** — ★8,456 — github.com/floccusaddon/floccus
19. **Operit** — ★7,836 — github.com/AAswordman/Operit
20. **NewsBlur** — ★7,620 — github.com/samuelclay/NewsBlur


## Census notes

- **ente** appears twice in the source file (same code, two orgs): a mirror, counted once.
- **ImageToolbox (T8RIN)** is ImageResizer renamed — same author, same stars: one row. Deduplicating brings in Operit and NewsBlur.
- **llama.cpp** (rank 2) pushed code on the cutoff day: actively alive.
- Larger census: 1,008 records answered 100%, 7 true zeros, 0 invented.

## Changelog

- **Sep 15, 2026:** initial publication; census 100% complete; deduplicated top (2 mirrors noted).

## Credits and links

Every name links to its own house on GitHub — every line carries its full owner/repository route. La Bandita project — dated verification, no further pretensions. The house meme:

> —So which one's first?
> —It's a list of lists: 319,420 stars saying "start here."

*La Bandita verifies before recommending: stars decorate; dates decide.*

**Correction (Sep 15, night):** the closing line carried a format pseudo-link that read like an unfilled template; rewritten as prose of its own language. Nothing else changes.
