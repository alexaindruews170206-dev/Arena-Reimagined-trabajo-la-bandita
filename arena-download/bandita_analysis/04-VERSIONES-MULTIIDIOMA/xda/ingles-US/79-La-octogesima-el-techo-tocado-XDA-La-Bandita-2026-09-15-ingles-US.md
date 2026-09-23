[INFO] Fortnight close: 80 verified publications and a 1,008-record census at 100% (Sep 15, 2026)

## [INFO] Fortnight close: 80 verified publications and a 1,008-record census at 100% (cutoff: Sep 15, 2026)

**What this is:** the closing record of a community open-source recommendation project. Not my software or my group's: a census of third-party repos, measured and published with a date. Small hobby project among friends, no official support — stated up front.

**How it was verified:** GitHub REST API (stars + activity) + liveness probes per house + HTML control re-scraping on 351 doubtful cases (the first API pass exhausted mid-census; no zero was published unverified). Forges outside GitHub probed directly; versions checked via each forge's public API, with nobody's keys.

## The numbers

- 1,008 records from the source file answered 100%.
- 136 forges and sites probed: 129 alive · 5×403 (no status declared) · 2 dead with an acta.
- 351 suspicious zeros re-scraped; 7 true zeros; 0 invented.
- 80 publications × 2 platforms, twins verified byte by byte; deduplicated top-20 (mirrors and renames count once).

## Method and lesson

"Better than what preceded, never perfect": dated corrections, never silent; invented statuses nowhere; a probe zero = an acta, not fiction.

## Changelog

- **Sep 15, 2026:** fortnight close; census 100%; probe actas published; deduplicated top.

## Credits

La Bandita project — dated verification, no further pretensions. The house meme:

> —Eighty and what?
> —Eighty and listed. Water doesn't celebrate the shore: it keeps going — but today the shore was the goal.

*La Bandita verifies before recommending: stars decorate; dates decide.*
