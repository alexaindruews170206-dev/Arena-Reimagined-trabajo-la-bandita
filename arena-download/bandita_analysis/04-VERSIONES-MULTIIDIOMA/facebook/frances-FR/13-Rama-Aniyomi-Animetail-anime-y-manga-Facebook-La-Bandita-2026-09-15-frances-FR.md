# Publicación 13 — Branche Aniyomi : mangas et anime en un seul lecteur — Aniyomi, Animetail et Tadami

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 13)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🌳 L'arbre de cette branche
├── 🎬 Aniyomi — la branche mère
├── 🦋 Animetail — le fork qui se déclare officiel
├── 🌗 Tadami — le troisième dans la conversation
├── 🌲 Le réseau complet de forks (révisé le 14-sep)
├── 🧩 Les extensions d'anime : où elles vivent aujourd'hui
├── ⚖️ Quand cette branche a du sens
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

L'arbre Tachiyomi/Mihon a une branche entière dédiée à l'anime : des lecteurs qui font les deux choses — lire des mangas et voir de l'anime — depuis la même application. Ce guide est la carte de cette branche, ouverte AUJOURD'HUI, 14 septembre, dépôt par dépôt :

```
Aniyomi     ★7 683   v0.18.2.1 (14-sep)     push du 14-sep  la branche mère
Animetail   ★578     v0.20.4.0 (5-aoû)      push 7-sep    fork appuyé
Tadami      ★260     v0.62 (12-sep)         push 13-sep   fork — vivante (rectification au pied)
```

Les trois vivent. Et la nouvelle du jour la donne la mère : Aniyomi publia DEUX versions ce même 14 septembre, après onze mois sans releases — le même jour où sa descendante Animiru faisait de même dans sa branche. La famille entière bougea aujourd'hui. Le critère pour choisir entre elles ne change pas : l'usage réel et le dépôt vivant, comme avec tout l'arbre.

## 🌳 L'arbre de cette branche

```
Aniyomi (la branche mère : mangas + anime)
   ├── Animetail     se déclare « Official fork of Aniyomi »
   ├── Tadami        mangas + anime + ranobe (romans légers)
   └── Animiru       la version SEULEMENT anime
                     (a son guide propre : pièce suivante)
```

Une note de lignée qui se lit dans l'API : Animetail et Tadami figurent comme forks (champ fork = true, père visible). Animiru descend aussi d'Aniyomi — mais son histoire est dans la pièce de sa branche.

## 🎬 Aniyomi — la branche mère

https://github.com/aniyomiorg/aniyomi

```
Ce que c'est :  « An app for manga and anime » — le lecteur
                de la lignée Tachiyomi avec lecteur d'anime
                intégré (basé sur mpv)
Licence :       Apache-2.0
Versions :      0.18.2.1 et 0.18.2.0 — publiées le 14-sep
                (la précédente stable : 0.18.1.2, du 28-oct-2025)
Push :          14 septembre 2026 (jour de la vérification)
Android :       8.0+ (selon sa fiche de téléchargement)
Trackers :      MyAnimeList, AniList, Kitsu, MangaUpdates,
                Shikimori, Simkl et Bangumi (son README)
Organisation :  aniyomiorg — maintient en plus son site web,
                l'hôte de previews (aniyomi-preview)
                et la documentation des forks
```

Jusqu'à ce matin, sa dernière version stable était d'octobre 2025 — onze mois de silence de releases, avec le doute flottant de si la branche mère restait debout. Le doute resta résolu AUJOURD'HUI : v0.18.2.0 et v0.18.2.1 sortirent le même jour où sa descendante Animiru publiait aussi. Les coups de pouce de code de ce mois n'étaient pas de la fumée : c'était de la préparation. La leçon se accomplit encore dans cette collection : un dépôt silencieux n'est pas un dépôt mort — et la seule chose qui le dit avec certitude est la page de releases, ouverte le jour où on décide.

Son organisation fit en plus quelque chose d'peu commun : elle maintient une page qui liste les forks connus du projet — l'index où Animiru (branche suivante de cette série) figure enregistré. Un projet qui cartographie ses fils est un projet avec mémoire.

## 🦋 Animetail — le fork qui se déclare officiel

https://github.com/Animetailapp/Animetail

```
Ce que c'est :  « Official fork of Aniyomi » (sa description)
Licence :       Apache-2.0
Version :       0.20.4.0 (5 août 2026)
Push :          7 septembre 2026
Curiosité :     sa numérotation suit Mihon (0.20.4),
                parce qu'il synchronise le noyau du lecteur mangas
                avec le tronc — son historique de changements
                le documente
Hôte d'essais : Animetail-preview (★75)
```

Animetail est le fork qui prit la décision technique plus intéressante de la branche : au lieu d'attendre Aniyomi, il apporte le noyau actualisé du lecteur de mangas (celui de Mihon) dedans le lecteur d'anime — pour ça ses versions partagent nombre avec Mihon, et la page de forks d'Aniyomi lui ajoute une fonction concrète : le support Cast. Et il y a nouveauté d'status vérifiée AUJOURD'HUI : l'organisation d'Aniyomi le liste dans sa page de « forks appuyés », à côté d'Animiru. L'étiquette « Official » n'est déjà plus seulement sienne : l'original la signe. L'API confirme la lignée par son côté : fork enregistré, père aniyomiorg.

Il publie des checksums SHA-256 par architecture dans ses releases — la bonne pratique de toujours : l'archive et son empreinte, ensemble.

## 🌗 Tadami — le troisième dans la conversation

> **PV (15-sep) :** la maison originale — andarcanum/Tadami-Aniyomi-fork — renvoie 404 depuis la reverificación d'AUJOURD'HUI. Restent son site officiel (tadami.qzz.io) vivant et des forks orphelins. Méthode de la maison : **le miroir n'est pas le dépôt** — Tadami ne se prescrit pas jusqu'à ce que sa maison dise où elle vit. Ce qui est noté ici reste comme histoire datée.

> **Rectification (15-sep, soir) :** le propriétaire constata la maison vivante et le vérificateur rouvrit en direct : **andarcanum/Tadami-Aniyomi-fork répond — ★260, v0.62 (12-sep), push du 13-sep. VIVANTE.** Le 404 de l'après-midi fut réel, mais d'une autre porte : le slug `anandnet/…` que le recensement traînait — et l'erreur fut d'attribuer à cette maison la chute. Et nouvelle neuve de la coupe : le projet inaugura organisation propre — **tadamiorg/tadami** (★56, avec couloir de releases propre : v1.9.3 du 26-juil). Deux maisons du même nom : le mot sur laquelle commande, le propriétaire l'a.

https://github.com/andarcanum/Tadami-Aniyomi-fork *(vivante — rectification en haut)*

```
Ce que c'est :  « An app for manga, anime and ranobe » —
                celui qui ajouta les romans légers à la formule
Licence :       Apache-2.0
Version :       0.62 (12 septembre 2026)
Push :          13 septembre 2026
Rythme :        trois versions en un mois (0.60 → 0.62)
Étoiles :       258 — la plus jeune et la plus petite
```

Tadami est le pari frais : fork d'Aniyomi qui ajoute la lecture de ranobe (romans légers) et bouge vite — versions du 20 août, du 29 août et du 12 septembre. Sa taille petite est sa fiche honnête : communauté jeune, développement personnel, cadence haute. Pour savoir s'il va au sérieux, la méthode de toujours : ouvrir ses issues, regarder si l'auteur répond, et le suivre quelques semaines. Ce qui est vérifiable aujourd'hui : il vit, il pousse, et il publie des versions avec date récente.

## 🌲 Le réseau complet de forks (révisé le 14-sep)

Cette branche n'est pas seulement trois fiches : le réseau de forks des trois maisons se révisa le 14-sep, fork par fork, dans l'API de GitHub. Le panorama, avec la coulisse ouverte :

```
aniyomi     1ʳᵉ page des forks plus neufs : 100
            la majorité : copies personnelles ★0 avec la
            description d'usine — sans changements propres

Animetail   30 forks — tous « non officiels », ★0-1
Tadami      31 forks — 6 renommés avec dessein
```

**Ceux qui apportent quelque chose de propre (vérifié aujourd'hui) :**

- **Kuro** (Zykrave/aniyomi-Kuro, ★21) — « une bibliothèque multimédia et lecteur redessinés au moderne » selon son README : le fork le plus suivi du réseau, v1.0.0 du 13 août. Rebrand complet, pas des rustines.
- **MeMedia** (FunMan1995/MeMedia, v0.21.2 du 22-aoû) — l'idée plus curieuse du réseau : lecteur mangas de Mihon + lecteur anime d'Aniyomi dans une seule app, avec des onglets séparés que Mihon n'a pas. Son README explique le « pourquoi de ce fork » avec bibliothèques indépendantes par milieu.
- **aniyomi-revived** (Blackyfi, ★1) — « fork actualisé pour rester au jour » : deux releases le même 3 septembre (v0.18.1.32/33). Il accomplit ce que promet le nom.
- **anteiku** (Heavenofficial) — la variante « mangas, anime et films ».
- Dans Tadami : **mugen** (h80r, v0.72.81 du 1-sep), **Nattyflix** (anime+mangas+films) et un fork de localisation qui promet « arranger l'anglais et refonte des gestes » du lecteur de romans (sans releases encore). Et donnée de loyauté : un fork de Tadami publia sa v0.62.0 le même AUJOURD'HUI que le père — le réseau suit les releases en direct.
- Dans Animetail, le seul avec fonction propre déclarée : un fork qui ajoute **Discord Rich Presence** au re-focaliser l'app.

Le reste du réseau sont des copies sans fonctions propres : elles ne se notent pas — la carte est de ce qui vit et apporte.

**L'expédition profonde (le réseau entier, 649 membres, marché le 14-sep) :** la forêt ne finit pas dans la première page. Le réseau complet d'Aniyomi — qui est le même d'Animiru, famille par API — se marcha membre à membre : 93 portent nom propre. Dans la couche profonde, les raretés qui valent mention : **kikuyomi**, un fork d'Aniyomi pour écouter des **livres audio** ; **jishoyomi**, pour étudier avec l'anime (outils d'apprentissage) ; **Anichibi**, le fork ludique avec versions V2 et V3 ; et un arbre dedans l'arbre : **Kuukiyomi**, projet personnel avec sept membres de réseau propres. Le reste de la couche profonde sont des copies avec README d'usine : hors de la carte. Avec cette règle, la carte reste complète.

## 🧩 Les extensions d'anime : où elles vivent aujourd'hui

Le chapitre délicat de cette branche sont ses extensions. La carte du jour :

```
Yūzōnō anime            ★428 · push 13-sep
   aujourd'hui, le canal vivant de référence :
   github.com/yuzono/anime-extensions

Yūzōnō / kohi-den       vivant, vérifié le 14-sep
   le code de la maison Kohi-den continue
   dans la famille Yūzōnō :
   github.com/yuzono/kohi-den

Nouveaux entrepôts dédiés      push du 14-sep
   existent des dépôts neufs centrés sur les clients
   anime de la famille Anikku/AniZen — ils vont dans la
   pièce de cette branche, où ils leur reviennent.
```

La règle de la maison : les index d'installation ne se collent pas — ils se lisent dans le README de chaque entrepôt, le jour où on les utilise. Ce que ce guide donne, c'est la carte : qui vit, qui mourut, avec date.

## ⚖️ Quand cette branche a du sens

Avec le critère de la maison (usage réel, unicité, maturité, dessein propre) :

```
Tu vois de l'anime ET tu lis des mangas, et tu veux une seule app ?
   → Le terrain naturel de cette branche : les trois
     fiches couvrent ce cas, à styles distincts.

Seulement anime ?
   → Cette branche est plus que ce dont tu as besoin :
     la pièce suivante (Animiru/Anikku) est la
     branche d'anime pur.

Seulement mangas ?
   → Le tronc (Mihon et famille, guide propre)
     pèse moins et sobre moins.

Romans légers en plus ?
   → Tadami les apporte d'usine ; Reikai (branche
     J2K) est l'autre voie mangas+romans.
```

Aucune des trois fiches n'est « la meilleure ». La bonne est celle qui couvre ton usage, avec dépôt vivant le jour où tu installes — et cette comprobation se fait en ouvrant ses releases ce jour-là.

## ❓ Questions fréquentes

**Aniyomi a-t-il cessé de se développer ?**
La question resta répondue le 14 septembre : v0.18.2.0 et v0.18.2.1, publiées le 14 septembre après onze mois sans releases — avec le code se poussant pendant le mois. L'organisation suit active. Quand tu doutes d'un projet, l'horloge est sa page de releases, ouverte ce jour-là.

**Animetail est-il « officiel de vrai » ?**
Triple vérification : sa description le déclare, l'API confirme le parenté direct et — depuis aujourd'hui vérifié — la page de forks appuyés de aniyomi.org le liste à côté d'Animiru, avec support Cast parmi ses fonctions. Son historique (migrer le noyau de Mihon, releases avec checksums) est de projet sérieux.

**Pourquoi les versions d'Animetail portent-elles le nombre de Mihon ?**
Parce qu'il synchronise le lecteur de mangas avec le tronc : c'est sa proposition de valeur — anime + lecteur actualisé sans attendre personne.

**Tadami n'est-il pas trop petit ?**
Il est jeune. Petit n'est pas invalide : c'est la porte de maturité en attente de démontrer. Avec cadence de releases de cette semaine, il va en chemin.

**Les extensions de l'entrepôt vieux servent-elles encore ?**
Celles déjà installées, suivent ; les neuves, sortent par les entrepôts vivants. L'officiel s'arrêta en août 2024 — la date commande.

**Animiru entre dans ce guide ?**
Il partage grand-père, mais sa branche a pièce propre (la suivante) : là-bas vit sa fiche complète, avec les deux versions qu'il publia le 14-sep.

## 🔗 Liens

- Aniyomi : https://github.com/aniyomiorg/aniyomi · https://github.com/aniyomiorg/aniyomi-preview
- Animetail : https://github.com/Animetailapp/Animetail · https://github.com/Animetailapp/Animetail-preview
- Tadami : https://github.com/andarcanum/Tadami-Aniyomi-fork
- Distingués du réseau : https://github.com/Zykrave/aniyomi-Kuro · https://github.com/FunMan1995/MeMedia · https://github.com/Blackyfi/aniyomi-revived
- Extensions d'anime vivantes : https://github.com/yuzono/anime-extensions · succession de Kohi-den : https://github.com/yuzono/kohi-den
- Forks appuyés par Aniyomi : https://aniyomi.org/forks/
- Archivés (histoire) : https://github.com/aniyomiorg/aniyomi-extensions · https://github.com/kohi-den/extensions-source

> La Bandita rapporte à partir de sources datées. Mangas et anime dans la même main — avec le dépôt vivant devant l'étiquette.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : Aniyomi ★7 683 + PV et rectification Tadami. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
