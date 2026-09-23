[GUIDE] La règle par les forges I — GitLab et Codeberg parlent désormais (API publique, sans clés) (15 sept 2026)

**XDA · frances-FR · fuente: pieza 69 (15-sep) · verificado: 15 de septiembre de 2026**

**Ce que c'est :** la méthode propre que la pièce 53 a laissée en attente : Codeberg en /api/v1/.../releases et GitLab en /api/v4/projects/.../releases — première ronde avec versions réelles (Eternity v0.2.1, lxreader 0.8.6, styncynotes v1.3) et PV honnêtes des silences. Sans versions inventées.

**Comment c'est vérifié :** requêtes aux APIs publiques le 15 sept, sans les clés de personne ; les silences se PV, on ne les remplit pas.

**La langue des forges (sans clés de personne) :** Codeberg parle en `/api/v1/.../releases` et GitLab en `/api/v4/projects/.../releases` — et AUJOURD'HUI on leur a fait la première ronde de questions. Versions réelles, et PV honnêtes de ce qui n'a pas répondu. **Sans versions inventées.**

**Codeberg — première ronde :** **Eternity** v0.2.1 (vivant 200) · **apps-android-wikipedia** — sans releases (vivant : fiche par activité) · **prayer-book** 0.10.3 · **nontrinsic/android** v2026.08.26 · **natinfo_flutter** v1.13.1 · **prosereader-android** — n/d avec PV (dépôt vivant 200 ; l'API de releases répond 404 : on note le silence, on n'invente pas de version)

**GitLab — première ronde :** **styncynotes** v1.3 · **lxreader** 0.8.6 · **BibleTheLife** note-appimage-1.39.1 · **BibleMultiTheLight** note-apk-4.00 · **libre-librivox-listener** — sans releases (fiche par activité)

**Les PV de la ronde :** prosereader (n/d avec PV, pas inventée) · **Quoter** (GitLab) : l'URL porte la variante `/tree/HEAD` et l'API de releases donne 404 — on la repasse à la maison propre au prochain balayage · **2 sans releases** : la date commande, pas l'étiquette.

**Pourquoi API et pas écran ?** Parce que l'écran décore et l'API répond : un scrape se casse avec un redessin ; un endpoint est un contrat. La maison préfère les contrats — et s'il manque, PV, pas fiction.
## Changelog

- **15-sept-2026 :** première ronde d'APIs publiques ; versions Eternity v0.2.1, lxreader 0.8.6, styncynotes v1.3.

## Crédits et liens

Fil 69 de la série : « La règle par les forges I — GitLab et Codeberg parlent désormais (API publique, sans clés) ». Chaque projet renvoie à sa maison sur GitHub — route complète auteur/dépôt, sans raccourcisseurs. La coupe de ce fil — « La règle par les forges I — GitLab et Codeberg parlent désormais (API publique, sans clés) » — a été lue dans sa maison le 15 sept ; si un nombre change, le fil 69 s'édite avec date — jamais en silence. Le mème du métier :

> — Et si la forge ne parle pas GitHub ?
> — On lui demande dans sa langue. Et si elle se tait, on lève un PV du silence — qui aussi est une réponse.

*La Bandita vérifie avant de recommander : les étoiles décorent, les dates décident.*
