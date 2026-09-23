[INFO] Fortnight close: 80 verified publications और 1,008 records का census 100% (15 सितंबर 2026)

## [INFO] Fortnight close: 80 verified publications और 1,008 records का census 100% (cutoff: 15 सितंबर 2026)

**ये क्या है:** community open-source recommendations project का closing record। ये मेरा software नहीं — तीसरे पक्ष के repos का census है, measured और dated। दोस्तों का छोटा project, कोई official support नहीं — शुरू में ही साफ़।

**Verification कैसे:** GitHub REST API (stars + activity) + हर house की liveness probe + 351 doubtful cases पर HTML cross-scraping (पहली API pass census के बीच थक गई; कोई zero बिना re-check publish नहीं हुआ)। GitHub से बाहर की forges direct probe की गईं; versions हर forge की public API से — किसी की keys नहीं।

## नंबर

- Source file के 1,008 records 100% answered।
- 136 forges और sites probed: 129 alive · 5×403 (status नहीं बताया) · 2 मृत, acta के साथ।
- 351 suspicious zeros re-scrape; 7 true zeros; 0 invented।
- 80 publications × 2 platforms, twins byte-by-byte verified; deduplicated top-20 (mirrors और renames एक बार गिने)।

## Method और सबक

"जो पहले था उससे बेहतर, कभी perfect नहीं": dated corrections, कभी silent नहीं; invented status कहीं नहीं; probe का zero = acta, fiction नहीं।

## Changelog

- **15-Sep-2026:** fortnight close; census 100%; probe actas publish हुईं; deduplicated top।

## Credits

La Bandita project — dated verification, उससे ज़्यादा कोई दावा नहीं। Meme:

> — अस्सी और क्या?
> — अस्सी और listed। पानी किनारे का जश्न नहीं मनाता: चलता रहता है — पर आज किनारा ही goal था।

*La Bandita पहले जाँच करता है, फिर सुझाता है — stars सजाते हैं, dates फ़ैसला करती हैं।*
