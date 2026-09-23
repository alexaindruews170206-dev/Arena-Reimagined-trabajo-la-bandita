# Publicación 08 — Musique FOSS : clients avec dépôt et date de pouls — Spotify cracké n'entre pas

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 08)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── ⚖️ Ce que ce guide n'est pas
├── 🧬 La généalogie : de ViMusic à la famille actuelle
├── 🎧 Les clients de streaming, fiche par fiche
├── 📻 NewPipe : l'espèce à part
├── 📂 Auxio : ta musique, tes fichiers
├── 🎙️ AntennaPod : les podcasts
├── 🆕 Ceux qui manquaient : N-Zik et Gabi
├── 🚫 Ce qui ne se colle pas
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Guide des clients de musique open source, avec le pouls de chaque projet mesuré le 14 septembre et re-vérifié au déménagement (15-sep). La semaine apporta du mouvement de vrai dans cette famille : OuterTune inaugura version ce mois-ci, Metrolist suit dans sa rafale de lancements, et la lignée complète resta documentée.

```
STREAMING (YouTube Music comme fond)
SimpMusic      ★11 257   2.1.0 (7-sep)     push 11-sep   vivant
OuterTune      ★5 390    v0.11.1 (6-sep)   push 6-sep    vivant
Metrolist      ★12 789   13.7.0 (7-sep) · Nightly du 14 à vue    vivant          ← la plus active
InnerTune      ★6 088    push nov-2025                   endormi
Harmony-Music  ★3 081    v1.12.2 (déc-25)  multiplateforme
music-you      ★220      vivant            minimaliste
InterTune      ★12       fork ancré, niche

STREAMING (front-end général)
NewPipe        ★39 682   v0.29.1 (15-aoû)  push 31-aoû

FICHIERS LOCAUX
Auxio          ★4 274    v4.1.5 (4-aoû)    push 8-sep

PODCASTS
AntennaPod     ★8 153    3.12.1 (5-sep)    push 12-sep

ViMusic        ★9 480    l'ancêtre
```

## ⚖️ Ce que ce guide n'est pas

YouTube et YouTube Music ont leurs termes de service. Un client libre qui consulte ces serveurs peut les heurter — ce guide n'est pas un cabinet d'avocats : il ne dit ni « c'est légal » ni « ça ne l'est pas ». Il dit dépôt, licence (GPL dans toutes les fiches du jour, vérifiées sur leur page), version et dernier push. La décision de ce que tu utilises est tienne, avec ses conséquences.

Et la phrase de toujours : ici il n'y a pas d'APK de « Spotify premium gratuit » ni de mods de rien. Cette porte a son guide propre — celui des boutiques — et elle finit toujours pareil.

## 🧬 La généalogie : de ViMusic à la famille actuelle

Cette famille a un arbre généalogique documenté, et le connaître éclaircit une demi-douzaine de noms :

```
   l'app qui inventa le modèle : streaming de
   YouTube Music avec file, sans l'app officielle.
   Aujourd'hui archivée — mais son idée enfanta tout ceci.
   │
   ├── InnerTune (z-huang)
   │      l'héritier direct : Material 3, bibliothèque
   │      avec compte, paroles synchronisées. Son dernier
   │      push fut en novembre 2025 — le créateur
   │      se déplaça vers d'autres projets et le dépôt dort.
   │      │
   │      ├── OuterTune (son fork vivant le plus solide)
   │      │      il ajouta le support de FICHIERS LOCAUX
   │      │      à côté du streaming. Version 0.11.1
   │      │      le 6 septembre — le mois passé
   │      │      montrait encore un tag de décembre ;
   │      │      le 14-sep la ligne resta corrigée.
   │      │
   │      └── Metrolist (★12 789)
   │             la plus installée de la seconde
   │             génération : version 13.7.0 du 7-sep
   │             avec nightly propre. Des vivantes,
   │             celle à cadence plus régulière.
   │
   └── SimpMusic (projet parallèle, même fond)
          multiplateforme, avec une ligne de développement
          très active : 2.0.0 le 28 août et 2.1.0
          le 7 septembre.
```

Les parents mineurs complètent la photo : Harmony-Music (★3 081, multiplateforme de bureau et mobile, avec sa dernière stable de décembre 2025), music-you (★220, la minimaliste) et le cas curieux de InterTune (★12) : un fork resté ancré à la version 0.10.1 de OuterTune « pour son écran de lecture », maintenu par son auteur pour son usage propre et celui qui le trouverait utile. Son README recommande, pour qui cherche du maintien actif, Metrolist et un autre projet nommé ArchiveTune — de ce dernier, aucun dépôt ne s'ouvrit dans cette révision.

## 🎧 Les clients de streaming, fiche par fiche

### Metrolist — celle à cadence régulière

https://github.com/mostafaalagamy/Metrolist

★12 789 · version **13.7.0 (7 septembre)** · GPL · vivant. La seconde génération la plus stable de la lignée InnerTune : versions mensuelles, nightly propre, et une base d'utilisateurs qui la mit parmi les recommandations fixes des communautés du sujet. Si tu viens de InnerTune endormi, c'est la maison naturelle. Pouls du jour : en plus de la 13.7.0, le dépôt publie une **Nightly** — compilation quotidienne vue AUJOURD'HUI, 14 septembre. *Déménagement certifié le 15-sep : la maison est maintenant l'organisation MetrolistGroup (les vieux liens redirigent) — la dynastie complète dans la Publicación 27.*

### OuterTune — celle qui joint streaming et fichiers

https://github.com/OuterTune/OuterTune

★5 390 · version **0.11.1 (6 septembre)** · GPL · vivant. Le fork qui ajouta à la ligne InnerTune la lecture de fichiers locaux : ta musique téléchargée et le catalogue de streaming dans le même lecteur. Material 3, thème dynamique. Le mois dernier son dernier tag était de décembre — ce guide l'enregistrait ainsi ; le 6-sep corrigea la photo. Aussi vite qu'un nombre périt.

### SimpMusic — l'incansable multiplateforme

https://github.com/maxrave-dev/SimpMusic

★11 257 · **2.1.0 (7-sep)** et 2.0.0 (28-aoû) · GPL · vivant. Deux versions majeures en dix jours. Son pari : le même fond de YouTube Music avec fonctions extra — paroles synchronisées, audio sans perte déclaré dans sa fiche, multiplateforme. Celle de développement le plus inquiet de la famille.

### InnerTune — l'ancêtre qui se repose

https://github.com/z-huang/InnerTune

★6 088 · push du 13 novembre 2025 · GPL · sans archivage mais endormi : presque dix mois sans code neuf, releases de 2024. Sa place dans l'histoire est garantie — c'est la source de laquelle boit la moitié de la famille. Pour installer aujourd'hui, ses héritiers font le travail.

### Harmony-Music et music-you — les alternatives

https://github.com/anandnet/Harmony-Music — ★3 081 · v1.12.2 (7-déc-2025) · multiplateforme (Android et bureau), GPL. Rythme lent mais projet sérieux.

https://github.com/DanielSevillano/music-you — ★220 · GPL · l'option minimaliste de la famille, pour qui veut juste le nécessaire.

### InterTune — le cas de niche

https://github.com/ItzSkyeYT/InterTune — ★12 · GPL · vivant par décision de son auteur : ancré à la version 0.10.1 de OuterTune pour conserver un écran de lecture concret. « Je l'utilise chaque jour et je le laisse public parce que à quelques-uns il servit », dit son README. L'honnêteté est aussi un trait de projet sain — et sa recommandation d'alternatives actives (Metrolist) le confirme.

## 📻 NewPipe : l'espèce à part

https://github.com/TeamNewPipe/NewPipe

★39 682 · v0.29.1 (15 août) · push du 31-aoû · GPL · vivant. NewPipe n'est pas un client de YouTube Music : c'est un front-end libre de TOUT l'univers YouTube — vidéos, musique, abonnements, sans compte et sans publicité. En musique il demande moins de confort de bibliothèque que les clients d'en haut ; en échange, il couvre tout le reste. Il est des projets plus vétérans et respectés du logiciel libre Android. Son canal historique de distribution est F-Droid — la fiche de la boutique de cette famille s'applique.

## 📂 Auxio : ta musique, tes fichiers

https://github.com/OxygenCobalt/Auxio

★4 274 · v4.1.5 (4 août) · push du 8-sep · GPL · vivant. Pour la musique que tu as DÉJÀ : lecteur local, rationnel, sans se connecter à aucun catalogue ni aucun nuage. Si ta bibliothèque vit dans le téléphone (copiée avec les outils du guide de fichiers de cette famille), c'est la fiche. Sans compte, sans streaming, sans frayeurs.

## 🎙️ AntennaPod : les podcasts

https://github.com/AntennaPod/AntennaPod

★8 153 · 3.12.1 (5-sep) · push du 12-sep · GPL · vivant. Gestionnaire de podcasts complet : flux RSS, téléchargements automatiques, vitesse variable, chapitres. Il ne rivalise avec aucun d'en haut : une autre catégorie que les vieux fils mélangeaient avec la musique en mille caractères de bruit. Ici, chaque chose dans son tiroir.

## 🆕 Ceux qui manquaient (addition du 14 septembre)

### N-Zik — le fils multilingue de Kreate

https://github.com/N-Zik-Group/N-Zik · v7.5.1-f (1er septembre ; à AUJOURD'HUI 15-sep ses releases danse avec une dev v8.0.0) · boutique : https://appteka.store/app/4abr315772

Bifurcation multilingue de Kreate déclarée dans son propre README : il transmet et garde en cache de la musique de YouTube Music, avec téléchargements hors connexion, paroles synchronisées mot à mot, visualiseur, Discord Rich Presence, widgets et support Android Auto/TV/Automotive. Il alterne l'interface moderne N-Zik avec la classique de ViMusic — la généalogie vivante de ce guide. Qualité Premium optionnelle en entrant avec compte de YouTube Music. Mises à jour OTA. Honnêteté de l'auteur, incluse : il développe assisté par IA avec révision humaine, il le déclare, et recommande des alternatives plus mûres (Metrolist, VIVI Music, RiPlay) si tu préfères la stabilité éprouvée. Cet avis est signal de métier, pas faiblesse. Pouls de clôture (14-sep, soir) : le dépôt cuisine déjà la **v8.0.0-dev d'AUJOURD'HUI** — la stable de la boutique reste la 7.5.1-f.

### Gabi — le téléchargeur de mille sites

https://github.com/Hotaro26/gabi · v4.6.1 « YouTube 403 Fix » (1er septembre) · boutique : https://appteka.store/app/b4cr315682

Téléchargeur de médias en Material 3 et Jetpack Compose qui fait courir yt-dlp et gallery-dl : vidéos, audio et galeries de plus de 1 000 sites — YouTube, TikTok, Instagram, Twitter/X, Reddit, SoundCloud, Pixiv et la liste suit. Télécharge depuis le presse-papiers d'un toucher (bouton Instant), partage le lien depuis n'importe quelle app et Gabi le ramasse, qualité jusqu'à 1080p/maximale, extraction en MP3, vue préalable avec titre et poids estimé, et thèmes aux couleurs dynamiques Material You. Le complément naturel de ce guide : pour écouter, les clients d'en haut ; pour emporter, Gabi.

Tous deux se obtiennent dans Appteka — la boutique de la Publicación 01. L'APK direct ne se colle pas : la maison de chaque app est son dépôt.

## 🚫 Ce qui ne se colle pas

APK de mods « premium » de n'importe quelle app · listes copiées de wikis de téléchargement · invitations de groupes · recettes d'URLs. Chacun ouvre le README du projet le jour où il s'en sert — la maison de chaque fiche est dans les liens d'en bas.

## ❓ Questions fréquentes

**Lequel j'installe pour commencer ?**
Si ta musique est catalogue : Metrolist (celle à cadence plus régulière) ou OuterTune (si en plus tu as des fichiers locaux). Si ta musique est ta collection : Auxio. Si tu veux tout YouTube sans compte : NewPipe. Si tu vis des podcasts : AntennaPod.

**Ces apps sont-elles légales ?**
Ce guide n'est pas un cabinet et ne dit pas ça. Il dit quel projet existe, avec quelle licence, et en quel état. Les termes de chaque service se lisent dans sa maison.

**Pourquoi InnerTune reste-t-il dans les listes s'il est endormi ?**
Parce que c'est l'ancêtre vivant de la moitié de la famille — et parce que ses héritiers (OuterTune, Metrolist) portent son code en avant. Fiché par histoire et par qui l'utiliserait quand même.

**Metrolist ou OuterTune ?**
Toutes deux vivantes et actives ce mois-ci. Metrolist : cadence mensuelle éprouvée. OuterTune : fichiers locaux intégrés. Celle qui couvre ton usage — et toutes deux s'ouvrent le jour où tu installes, parce que les nombres périssent.

**Et que se passa-t-il avec RiMusic ?**
Archivée en juillet 2025. Le fil de 340 mil caractères d'avril la traitait comme vivante : gonfler n'est pas vérifier. Sa fiche dit : histoire.

**Ces apps consomment-elles beaucoup de batterie ?**
Ce que ce guide peut dire sans laboratoire : ce sont des lecteurs, pas des jeux ; la consommation dépend de l'usage (téléchargement vs streaming). Ce qu'il NE peut pas dire : des nombres de batterie — pas mesurés ici, et pas inventés.

**Y a-t-il une version pour iPhone ?**
De cette famille : Harmony-Music se déclare multiplateforme (bureau et mobile). Le reste des fiches est Android. L'écosystème iOS libre de musique est une autre carte.

**Discord ou groupe pour du support ?**
Chaque projet a sa maison de communauté dans son README — ça s'ouvre là-bas, ça ne se colle pas ici. Cette famille n'utilise pas de canaux d'envoi.

## 🔗 Liens

- Metrolist : https://github.com/mostafaalagamy/Metrolist
- OuterTune : https://github.com/OuterTune/OuterTune
- SimpMusic : https://github.com/maxrave-dev/SimpMusic
- InnerTune : https://github.com/z-huang/InnerTune
- Harmony-Music : https://github.com/anandnet/Harmony-Music · music-you : https://github.com/DanielSevillano/music-you · InterTune : https://github.com/ItzSkyeYT/InterTune
- NewPipe : https://github.com/TeamNewPipe/NewPipe
- Auxio : https://github.com/OxygenCobalt/Auxio
- AntennaPod : https://github.com/AntennaPod/AntennaPod
- N-Zik : https://github.com/N-Zik-Group/N-Zik · boutique : https://appteka.store/app/4abr315772
- Gabi : https://github.com/Hotaro26/gabi · boutique : https://appteka.store/app/b4cr315682
- Archivés : https://github.com/vfsfitvnm/ViMusic · https://github.com/fast4x/RiMusic

> La Bandita rapporte à partir de sources datées. La lignée se vérifie aussi : les ancêtres expliquent les vivants.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : SimpMusic ★11 257, Metrolist ★12 789 (+Nightly), OuterTune ★5 390, InnerTune ★6 088, dev N-Zik v8.0.0. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
