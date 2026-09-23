# Publicación 17 — La couche d'immersion : les lecteurs qui enseignent le japonais pendant que tu lis — et le client Komga qui manquait

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 17)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🦋 Chimahon — le fork de Mihon qui mine Anki
├── 📚 Hoshi Reader — l'EPUB japonais à mille outils
├── 🎐 Yomikai — OCR, voix et le mini-lecteur flottant
├── 🌗 Yomi Reader — le triple anime/mangas/roman
├── 🏛️ Koharia — ton serveur Komga, dans ta poche
├── 🧩 Les ateliers derrière (dictionnaires partagés et plus)
├── ⚖️ Pour qui est cette couche ?
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Il y a une couche de l'écosystème que les cartes grandes ne voient presque pas : celle de qui lit en japonais en l'APRENDAnt — dictionnaires au toucher, cartes d'Anki à la volée, texte vertical, mangas Mokuro, voix sur la page. Ce guide fiche les cinq projets vivants de cette couche, tous vérifiés AUJOURD'HUI, 14 septembre — **deux publièrent version ce jour même** :

```
Hoshi Reader   ★378   v1.3.3 (13-aoû)   EPUB japonais + Yomitan + Anki + e-ink
Chimahon       ★198   v2.4.2 (AUJOURD'HUI, 15-sep)   fork de Mihon : dictionnaire, Mokuro, Anki
Koharia        ★148   v0.5.0 (14-sep)      client Android pour serveurs Komga
Yomi Reader    ★10    v0.1.7 (6-sep)    anime + mangas + roman, compat. Tadami
Yomikai        ★0     v1.9.84 (AUJOURD'HUI, 15-sep)  OCR + voix + mini-lecteur flottant
```

Étoiles petites, ateliers grands : ici les nombres de renommée ne racontent pas l'histoire — la cadence et les fonctions, oui.

## 🦋 Chimahon — le fork de Mihon qui mine Anki

https://github.com/Chimahon/chimahon

```
★198 · GPL-3.0
v2.4.2 (AUJOURD'HUI, 15-sep) · v2.4.1 · v2.4.0 (11-sep) — trois en quatre jours
Ce que c'est : « fork d'immersion de Mihon » (sa description) :
dictionnaire natif (Yomitan), mangas Mokuro et anime,
lecteur de romans EPUB, et minage instantané vers Anki
```

C'est Mihon avec salle de classe dedans : tu lis ton mangas de toujours et, en touchant un mot, le dictionnaire s'ouvre là même ; ce que tu veux garder, il vole vers ton paquet d'Anki sans sortir du chapitre. Son atelier maintient en plus les composants : Chimahon-ffmpeg et Chimahon-local-models (traitement local), et il utilise les dictionnaires de Hoshi — la couche se tisse entre elle.

## 📚 Hoshi Reader — l'EPUB japonais à mille outils

https://github.com/HuangAntimony/Hoshi-Reader-Android

```
★378 · GPL-3.0
v1.3.3 (13-aoû) — le plus grand de la couche
Ce que c'est : lecteur d'EPUB japonais avec recherche
Yomitan, minage vers Anki, lecture accompagnée de
livre audio et support d'encre électronique
```

Son README (lu le 14-sep) liste le sien : EPUB individuels ou par lots avec progression visible, étagères propres, texte vertical ou horizontal avec pagination ou scroll continu, dictionnaires Yomitan qui s'importent et s'actualisent depuis l'app, recherche récursive (tu touches un mot dedans une définition et ça suit), mode focus immersif, passage de page avec les touches de volume et options spécifiques pour lecteurs e-ink. Et c'est la pointe d'un atelier complet : son auteur maintient les dictionnaires (hoshidicts), une grammaire japonaise de référence, des outils pour romans web (narou-py) et contribue à Yomitan et mpvacious. La couche d'immersion a centre de gravité, et il s'appelle HuangAntimony.

## 🎐 Yomikai — OCR, voix et le mini-lecteur flottant

https://github.com/sj0404-collab/yomikai
(le « yomihon-custom » qui circule : https://github.com/sj0404-collab/yomihon-custom)

```
Apache-2.0
v1.9.84 (AUJOURD'HUI, 15-sep) · v1.9.83 (nuit du 15) · v1.9.79 (14-sep) · v1.9.78/76 (13-sep)
— cadence quotidienne de vrai
Ce que c'est : lecteur de mangas avec OCR et ovoz
(rôles et voix), dictionnaires, et un
mini-lecteur flottant sur toutes les apps
```

Sa description (du russe original) le dit entier : mangas avec OCR de texte, ovoz par rôles, dictionnaires et un lecteur mini qui flotte sur n'importe quelle application — tu écoutes la voix du chapitre pendant que tu lis ailleurs. Deux notes de carte : le projet racine est **Yomihon** (yomihon/yomihon, ★125, « maintenant avec OCR », v0.4.0 du 30-juil) — le nom du dépôt « yomihon-custom » vient de là — et la maison active est Yomikai, avec sœur web (yomikai-pwa, React+TSX, avec navigateur et chat IA dedans). Qu'il n'ait pas d'étoiles ne signifie rien : il publie des versions chaque jour.

## 🌗 Yomi Reader — le triple anime/mangas/roman

https://github.com/codegeasse1/yomi-reader

```
★10 · Apache-2.0
v0.1.7 (6-sep) — jeune, en 0.1
Ce que c'est : « lecteur open source d'anime,
mangas et romans pour Android (compatible
Tadami/Aniyomi) » — sa description
```

Le pari du triple dans la lignée d'Aniyomi : les trois médias dans une app, mangeant des extensions compatibles Tadami. Il va par 0.1 — âge honnête — et son atelier apporte plus : Nekoread (lecteur de mangas, v2.2.5 du 10-sep) et hikari (streaming universel avec addons de Stremio et plugins CloudStream, v0.3.67 du 13-sep). Un constructeur avec cinq fers au feu — suivi ouvert pour tous.

## 🏛️ Koharia — ton serveur Komga, dans ta poche

https://github.com/Mister-album/Koharia

```
★147 · Apache-2.0
v0.5.0 (14-sep) · v0.4.5 (6-sep)
Ce que c'est : « lecteur Android indépendant de
tiers pour naviguer et lire du contenu de
serveurs Komga » — sa description (du chinois)
```

Komga est le serveur de bibliothèque que les grands lecteurs synchronisent déjà ; Koharia est l'app dédiée à lui : ton serveur, ton app, avec le lecteur mis à mesure. v0.5.0 publiée le 14-sep. Du même auteur : la web du projet et son propre fork du serveur komga — qui construit le client entend le serveur, et inversement.

**L'autre moitié de la couche, vérifiée ce soir par exploration libre :** **Komga** (gotson/komga, ★6 659, MIT, 1.26.3 du 12 août) — serveur de comics, mangas et eBooks avec API, OPDS et synchronisation Kobo et KOReader ; et **Kavita** (Kareadita/Kavita, ★11 677, GPL-3.0, v0.9.1.4 du 2-sep), le serveur de lecture multiplateforme. Koharia vit parce que ceux-ci vivent — et inversement : le serveur sans clients est une archive, le client sans serveur est une coquille.

## 🧩 Les ateliers derrière (dictionnaires partagés et plus)

La couche se soutient sur de l'infrastructure partagée qu'il convient de nommer : les **dictionnaires hoshidicts** les utilise aussi Chimahon ; **Yomitan** (le dictionnaire-pop-up du navigateur, référence absolue du niche) connecte avec tous ; et dans l'observation de cette semaine resta un compagnon petit mais vivant : **android-koreader-companion** (★9, MIT, version du 14-sep) — montre ce que tu lis dans KOReader et Mihon, la progression entre les deux mondes.

## ⚖️ Pour qui est cette couche ?

```
Tu lis des mangas en japonais et tu étudies ?
   → Chimahon (si tu viens de Mihon) ou
     Yomikai (si tu veux voix et OCR).

Tu lis des romans légers en EPUB japonais ?
   → Hoshi Reader : c'est SON terrain, avec
     e-ink inclus pour le lecteur d'encre.

Anime + mangas + roman dans une seule app
(et le japonais n'est pas ton focus) ?
   → Yomi Reader — et regarde Tadami (pièce 13),
     le triple de la lignée Aniyomi avec années dessus.

Tu as un serveur Komga ?
   → Koharia, l'app dédiée.
```

Aucune fiche passe par la renommée : elle passe par cadence, fonctions propres et dépôt ouvert — et les cinq vivent, re-vérifiées à AUJOURD'HUI 15-sep.

## ❓ Questions fréquentes

**Ceux-ci remplacent-ils Mihon/Komikku/Aniyomi ?**
Non : ce sont des couches dessus ou à côté. Chimahon EST un fork de Mihon (ta bibliothèque migre avec les règles de toujours) ; Koharia a besoin d'un serveur Komga ; Hoshi est pour l'EPUB japonais ; Yomikai et Yomi Reader sont maisons à part. Chacun couvre ce que le tronc ne couvre pas.

**Et les extensions ? Servent-elles, celles de toujours ?**
Yomi Reader déclare compatibilité Tadami/Aniyomi ; Chimahon, étant fork de Mihon, hérite l'écosystème Mihon. Hoshi (EPUB) et Koharia (Komga) ne mangent pas d'extensions : ils mangent livres et serveurs. Yomikai construit ses sources propres — son README commande le jour où tu l'utilises.

**Pourquoi des étoiles si petites s'ils sont si actifs ?**
Parce que le niche est niche : qui étudie le japonais avec des mangas sont des milliers, pas des millions. La règle de la maison ne fut jamais la renommée — c'est la cadence et l'apport propre, et ici ils sobrent.

**Marchent-ils sans savoir le japonais ?**
Chimahon, Hoshi et Yomikai EXISTENT pour l'apprendre — le dictionnaire et la voix sont le point. Pour lecture en espagnol/anglais, les troncs des pièces 13–16 restent la maison.

## 🔗 Liens

- Chimahon : https://github.com/Chimahon/chimahon
- Hoshi Reader : https://github.com/HuangAntimony/Hoshi-Reader-Android
- Yomikai : https://github.com/sj0404-collab/yomikai · jumelle web : https://github.com/sj0404-collab/yomikai-pwa · racine du nom : https://github.com/yomihon/yomihon
- Yomi Reader : https://github.com/codegeasse1/yomi-reader · frères : https://github.com/codegeasse1/Nekoread
- Koharia : https://github.com/Mister-album/Koharia
- Compagnon de progression : https://github.com/woxakv/android-koreader-companion
- Les serveurs : https://github.com/gotson/komga · https://github.com/Kareadita/Kavita

> La Bandita rapporte à partir de sources datées. Lire avec dictionnaire dans la main — maintenant, dans le même doigt.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : Chimahon v2.4.2, Yomikai 1.9.84, Koharia ★148 (toutes d'AUJOURD'HUI). Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
