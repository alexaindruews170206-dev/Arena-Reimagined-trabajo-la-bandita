[GUIDE] Verified open-source top 20 — 493 repos का census (cutoff: 15 सितंबर 2026)

## [GUIDE] Verified open-source top 20 — 493 repos का census (cutoff: 15 सितंबर 2026)

**ये क्या है:** verified numbers के साथ open source recommendations की छोटी list। ये मेरा software नहीं है — तीसरे पक्ष के repos का census है, जो measured और dated है। दोस्तों का छोटा project, कोई official support नहीं — शुरू में ही साफ़ कर रहा हूँ ताकि कोई guarantee ना माने।

**Verification कैसे हुई:** GitHub REST API (stars + activity) + हर repo की liveness probe + 351 suspicious zeros पर HTML cross-scraping (पहली API pass census के बीच rate-limit हो गई थी — zeros publish नहीं किए: दोबारा जाँचे)। एक ही cutoff: 15 सितंबर 2026। नंबर बदले तो dated correction — silent change कभी नहीं।

## List (top 20, deduplicated, stars से)


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

- **ente** सोर्स फ़ाइल में दो बार है (same code, दो orgs): mirror — एक बार गिना।
- **ImageToolbox (T8RIN)** = ImageResizer का नया नाम — same author, same stars: एक row। Deduplicate करने पर Operit और NewsBlur आए।
- **llama.cpp** (rank 2) ने cutoff दिन को code push किया: live active।
- बड़ा census: 1,008 records 100% answered, 7 true zeros, 0 invented।

## Changelog

- **15-Sep-2026:** initial publication; census 100%; deduplicated top (2 mirrors noted)।

## Credits और links

हर नाम GitHub पर अपने घर से जुड़ता है — हर पंक्ति अपना पूरा owner/repo रास्ता रखती है। La Bandita project — dated verification, उससे ज़्यादा कोई दावा नहीं। Meme:

> — पहला कौन?
> — lists की list: 319,420 stars कह रही हैं "यहाँ से शुरू करो।"

*La Bandita पहले जाँच करता है, फिर सुझाता है — stars सजाते हैं, dates फ़ैसला करती हैं।*

**सुधार (15 सित, रात):** समापन पंक्ति में एक प्रारूप जैसा छद्म लिंक था; अपनी भाषा के गद्य में दोबारा लिखा गया। बाकी कुछ नहीं बदला।
