# Publicación 16 — Branche SY/Komikku : le fork classique et le second fils avec organisation — TachiyomiSY et Komikku

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 16)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🌳 L'arbre de cette branche
├── 📗 TachiyomiSY — le classique qui suit
├── 📘 Komikku — le second fils avec org
├── 🔀 Les deux écoles de fork (et le contre-exemple)
├── 🧩 Les extensions de cette branche
├── 🌲 Le réseau complet de forks (révisé le 14-sep)
├── 🏗️ L'infrastructure : previews et sync
├── ⚖️ SY ou Komikku : comment décider avec critère
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

C'est la branche du style classique : TachiyomiSY — le fork qui ajouta les fonctions extra au Tachiyomi original, le classique « SY » de la vieille garde — et Komikku, le projet qui naquit de cette lignée et grandit jusqu'à organisation propre. Vérifié AUJOURD'HUI, 14 septembre :

```
TachiyomiSY       ★4 143   1.13.2 (13-juil)   push 13-sep   le classique
TachiyomiSYPreview ★484    hôte de previews  push 25-aoû
Komikku           ★4 717   v1.14.1 (17-juil)  push 11-sep   le second fils
komikku-preview   ★248     canal d'essais    push 10-sep
```

Ce sont les deux grands vivants du style SY de l'écosystème — et la comparaison entre eux est la leçon sur comment un fork se convertit en projet avec vie propre.

## 🌳 L'arbre de cette branche

```
TachiyomiSY (jobobby04)      le classique vivant
   ├── TachiyomiSYPreview     hôte de builds d'essai
   └── Komikku (komikku-app)  dépôt neuf qui hérite le
               ├── komikku-preview  code et grandit avec org
               ├── Anikku           son client d'anime
               └── (sa branche a pièce propre dans cette collection)
```

Détail technique qui se lit dans l'API : Komikku NE figure pas comme fork (c'est un dépôt neuf) ; sa lignée la déclare sa propre documentation. C'est la différence entre le graphe de GitHub et la réalité — pour ça on lit les deux.

## 📗 TachiyomiSY — le classique qui suit

https://github.com/jobobby04/TachiyomiSY

```
★4 143 · Apache-2.0
Version :     1.13.2 (13 juillet 2026)
Push :        13 septembre — code d'HIER
Ce que c'est : le fork classique : le lecteur du tronc
              avec les fonctions extra du style SY
              (plus de sources par défaut, plus de réglages
              de lecture, l'expérience « complète »)
```

SY est le fork avec plus d'histoire continue de l'écosystème : il existait avant la fermeture de l'original, il survécut à janvier 2024 et il continue de pousser du code — il le fit le 13-sep, constance de sa vérification. Son rythme n'est pas celui des releases mensuelles : sa dernière stable est de juillet et son code bouge depuis lors. Le patron du vétéran : moins de bruit de versions, plus de maintien silencieux.

Son avis d'identité : **le SY vivant est jobobby04** — le jour où tu cherches SY, installe depuis son dépôt, celui qui pousse du code d'hier. Le nom ne suffit pas ; le propriétaire oui.

Son hôte de builds d'essai : jobobby04/TachiyomiSYPreview (★484) — versions expérimentales pour curieux et rapporteurs de bugs, pas la voie du quotidien.

## 📘 Komikku — le second fils avec organisation

https://github.com/komikku-app/komikku

```
★4 717 · Apache-2.0
Version :     1.14.1 (17 juillet 2026)
Push :        11 septembre
Ce que c'est : lecteur mangas de la lignée SY qui naquit
              comme dépôt neuf et grandit jusqu'à
              organisation complète :
              - komikku-preview (★248) : canal d'essais
              - Anikku (★1.028) : son client d'anime
              - traductions communautaires propres
```

Komikku est le cas d'étude de comment un fork devient institution : il hérita le code de la lignée, naquit avec maison propre, et construisit structure — org, canal de previews, projet frère d'anime, communauté de traduction. Ses versions vont par cadence régulière (1.14.1 en juillet, avec branche de développement poussant depuis lors).

En étoiles il dépasse déjà le SY classique (4 717 vs 4 143). Ça n'est pas verdict de qualité — c'est une donnée de communauté. Ce qui oui est verdict vérifiable : son atelier bouge (push du 11-sep) et son infrastructure est la plus complète de cette branche.

## 🔀 Les deux écoles de fork (et le contre-exemple)

Cette branche a les trois archétypes de l'écosystème, vivant dans la même maison :

```
ÉCOLE 1 — maintenir le patronyme
TachiyomiSY : continue le fork classique, conserve
le nom et le style, évolue avec soin.
Sa valeur : continuité. Son utilisateur : celui qui veut
ce de toujours, vivant.

ÉCOLE 2 — grandir avec maison neuve
Komikku : hérite le code, baptise son nom,
construit organisation et jusqu'à branche d'anime.
Sa valeur : évolution avec structure. Son utilisateur :
celui qui veut le projet qui bouge le plus
en structure.
```

## 🌲 Le réseau complet de forks (révisé le 14-sep)

S'ouvrirent le 14-sep, fork par fork, les réseaux de SY (238 forks, trois pages, deux ordres) et de Komikku (200 forks). C'est le réseau plus riche de l'écosystème — et celui qui montre mieux la différence entre copier et apporter :

**Dans le réseau de SY :**

```
Chai (Smol-Ame)          ★12 · push 22-aoû
   le fork vivant le plus suivi : filtre « lewd » pour
   cacher le piquant de la bibliothèque, recherche
   par état de tracking et édition d'info du
   mangas — sans releases encore (seulement du code)

SY avec Discord RPC (jeryjs)  ★10 · preview-43 (23-juil)
   presence de Discord pendant que tu lis

Faxyomi                  ★4 · v9 (29-aoû)
   « pour avoir DEUX SY dans le même téléphone » —
   le cas d'usage plus honnête de l'écosystème

Shinyomi ★5 (1.0.0, mai-25) · Mizu ★2 · Dyomi
(build 8-sep) · Fukuro (push 4-sep) · variante
desktop en chantier · le fork de l'équipe SyncYomi
(push 10-sep)
```

**Dans le réseau de Komikku :**

```
Houri (PineappleTwilight)  ★10 · v1.22.1 (AUJOURD'HUI 15-sep) *(la v1.22.0 sortit le 14 — deux jours de suite : la cadence suit)*
   le fork avec proposition propre plus actif :
   support de RELECTURE avec trackers connectés
   (rereads par mangas), Discord RPC amélioré qui
   respecte sous-catégories, filtres par défaut par
   source et un feed amélioré opt-in

komikku_img_upscale · r10647 (13-sep)
   upscale d'images de pages — plus trois
   forks de plus du même sujet (upscaling/scaling)

mikku (Syncthing intégré) · komikku avec
marqueurs de page · kokomikku (KOReader) ·
un fork avec tracker propre · komikku2 (13-sep)
```

La donnée fine : l'auteur de Houri maintient aussi un fork d'Anikku (anikku-pineapple) — un seul dev tissant entre les deux branches de la maison Komikku.

**La couche que le graphe cache (cinq maisons vérifiées le 14-sep à la demande des groupes)**

Ces cinq N'apparaissent pas dans le réseau de forks directe de SY ni de Komikku : ce sont des forks rebasés avec maison neuve, ou des petits-fils — invisibles pour le graphe du père. Ils s'ouvrirent un à un, avec leurs options propres lues de leurs README :

```
ShinKu (Harrys-HQ)         ★31 · v2.6.9 (13-sep)
   « fork modernisé et rebaptisé de
   TachiyomiSY/Mihon » — cadence hebdomadaire.
   Le sien : recherche en langue naturelle avec
   découverte assistée (« Vibe Search » et
   « For You »), carte de statistiques de
   lecture, audio ambiant qui accorde avec le
   genre, interface qui mue de couleur avec la
   couverture, catégoriseur automatique, scanner
   de sources mortes pour migrer ton mangas, et
   menu pour migrer les actualisations
   échouées.

MihonSY (ruzhe85)          ★13 · v1.0.7 (22-aoû)
   fork chinois de SY (son README vient en chinois).
   Le sien : scroll par touché en webtoon avec
   distance ajustable (½, ¾ ou écran
   complet) et animation réglable, détection
   automatique de webtoon par résolution de
   l'image, progression Komga synchronisée chapitre
   à chapitre (pas par lots), amélioration d'image
   Lanczos3 légère —sans modèles pesants— et
   résolution native 1:1.

Pokomi (pokedo0)           ★11 · v1.0.9 (16-aoû)
   fork de Komikku avec une idée propre claire :
   « Author Following » — s'abonner pour
   suivre tes auteurs. Il hérite les fonctions
   uniques de Komikku.

NEXUS (the-nexus-app)      ★3 · v1.2.1 (8-sep)
   fork de Komikku : suggestions qui lisent les
   recommandations du site même de la
   source, catégories cachées AVEC
   authentification pour les ouvrir ou les effacer, et
   marqueurs de chapitres et de pages au
   vol.

bchan (geograms)           ★5 · v1.12.1 (19-juin)
   « fork simplifié de TachiyomiSY/Mihon » :
   extensions Keiyoushi prêtes d'usine,
   lecture webtoon par défaut, téléchargements qui
   pausent et reprennent seuls entre réseaux, et
   noms d'archive plats et prévisibles.
```

Et la seconde génération donna aussi le sien : **Yomiko** (petalya, ★8, push du 12-sep), fille du fork de Discord-RPC — la chaîne ne se coupe pas.

La leçon de méthode reste dans le texte : la liste de forks du père ne montre ni les rebasés ni les petits-fils. Cartographier l'arbre, c'est marcher les chaînes et lire les crédits de chaque README — et quand quelqu'un nomme une maison qui ne sortit pas dans le balayage, le lien commande.

**L'expédition profonde (SY : plus de 1 000 membres · Komikku : 244 · anikku : 71 — tout marché le 14-sep) :** la seconde génération compile déjà : **leassapie/houri**, fils de Houri, avec version propre v1.21.0 (30 août) — la chaîne Houri → son fils, vivante. **Yomiko**, la petite-fille du fork de Discord-RPC — nuance datée (corrigé le 15-sep par audit de la maison) : la maison montrait poussée, mais sa version stable (v.1.8.1 — correction datée 15-sep par REST et git : release du 25-sep-2025, pas aoû-2026 ; et généalogie CERTIFIÉE par fork : Yomiko ← SY-Discord-RPC ← TachiyomiSY — ligne SY, pas J2K). Que la date dise ce que la date dit. ShinKu, NEXUS, MihonSY, Pokomi et bchan sont pour l'instant des feuilles : quand ils jetteront racines, ils se notent avec date.

## 🧩 Les extensions de cette branche

La branche SY/Komikku est celle que plus d'entrepôts vivants desservent. La carte de la fournée du 14 (son guide complet a pièce propre dans cette collection) :

```
Keiyoushi              le hub principal
   l'entrepôt plus utilisé de l'écosystème : il déclare
   support pour Mihon, TachiyomiSY et Komikku
   (guide complet : pièce 04 de cette collection)

Yūzōnō mangas           ★890 · MIROIR de Keiyoushi
   miroir automatique, sans apports propres —
   décontinué (pas archivé) : le « push de
   aujourd'hui » est le miroir se synchronisant, pas vie
   propre. Pour le mangas, la maison est Keiyoushi

cuong-tran/manga-repo  ★445 · push du 14-sep
   « Extensions for Komikku / Mihon & forks »
   (sa description)

Étagères "cursed"      ★185/★158  nom oui, index non
```

L'avis de Keiyoushi reste la clé de l'écosystème : si ta liste d'extensions sort vide avec « Outdated app », ton app n'est déjà plus compatible — actualise-la depuis son dépôt. Et la convention technique du moment (KeiSource 1.6) se compte dans le guide d'extensions : c'est la raison pour laquelle les apps vieilles cessent de voir des extensions neuves.

## 🏗️ L'infrastructure : previews et sync

Deux pièces que cette branche partage avec l'écosystème et qui convient de connaître :

- **Les hôtes de previews** (SYPreview, komikku-preview) sont le canal d'essais de chaque projet : builds expérimentaux pour qui rapporte des bugs. Les installer est une décision de tester, pas d'utilisateur quotidien.
- **tracker-extensions** (komikku-app, ★14) : les extensions de trackers de la maison Komikku — les trackers se servent à part du noyau, comme extensions (vérifié le 14-sep).
- **SyncYomi** est la synchronisation de bibliothèques entre appareils et entre forks de la famille — utile exactement pour le geste de ce guide : si tu essaies SY et Komikku, ta progression peut t'accompagner entre les deux. Sa fiche complète, dans la collection d'outils de cette série.

## ⚖️ SY ou Komikku : comment décider avec critère

Les quatre portes de la maison, appliquées sans « meilleurs » :

```
Continuité           si tu venais du SY de toute la vie,
                     jobobby04 est la même maison avec
                     les lumières allumées.

Structure            si tu values org, canal de previews,
                     projet frère d'anime et
                     cadence de releases : Komikku.

Compatibilité        les deux lisent les mêmes entrepôts
                     principaux (Keiyoushi le déclare
                     pour les deux). Le critère de départage
                     n'est pas dans les sources : il est dans
                     l'usage que tu vas lui donner.

Maturité             les deux poussèrent cette semaine.
                     Aucun ne passe la porte avec les
                     mains dans les poches.
```

Le reste est goût personnel — et l'usage réel : qui l'utilise et le comprobe. Les étoiles (4 717 vs 4 143) sont la donnée de renommée du jour, pas une recommandation.

## ❓ Questions fréquentes

**SY et Komikku sont le même code ?**
Ils partagent lignée, pas dépôt ni propriétaire. L'API ne déclare pas Komikku comme fork ; sa propre documentation raconte d'où il vient. Parentèle déclarée, maisons séparées.

**Lequel a plus de sources ?**
Les sources vivent dans les entrepôts (Keiyoushi, Yūzōnō…), pas dans l'app — et les entrepôts principaux déclarent support pour les deux. Le départage réel est dans l'app qui te rentre mieux dans la main.

**Et les dépôts au même panneau qui ne bougent plus ?**
Ils ne se notent pas : la carte est du vivant. La règle pratique : installe SY depuis le dépôt de jobobby04 — et personne d'autre.

**Et les dépôts qui s'annoncent comme « le lecteur de 2026 » ?**
Dans le scan du 14-sep apparut une autre portée du patron déjà connu : des dépôts neufs aux noms de projets sérieux — un « komikku-scans », un « Neko-Manga-Pearl » qui emprunte le nom du fork réel de MangaDex, un « kumo-surreal » qui se dit Mihon optimisé — créés les trois le même jour, avec des étoiles presque identiques entre eux et l'année « 2026 » dans la description. La portée grandit pendant ce temps : un « weeb-index » (« Best Otaku Directory 2026 ») et un « manga-zen-reader » (« Best Alternatives 2026 ») répètent le costume avec les mêmes étoiles de mensonge. Nommés sans lier : c'est du SEO pour moissonner des téléchargements de qui cherche vite. Le projet réel n'a pas besoin de mettre l'année au nom.

**Et les forks aux noms qui sonnent japonais que la gente mentionne (type « ShinKu ») ?**
Fichés en haut, avec date : ShinKu existe (★31, v2.6.9 avec cadence hebdomadaire, de la lignée SY/Mihon) — dans le repassage précédent il n'apparut pas parce que les forks rebasés et les petits-fils ne sortent pas dans le réseau de forks du père. Deux règles restent pour le lecteur : un nom sans lien ne se vérifie ni ne se discarte — et le lien, toujours, ferme le cas.

**Komikku sortit-il de SY ou de Tachiyomi ?**
Sa documentation déclare la lignée de l'écosystème ; le graphe de GitHub le montre comme dépôt neuf. Les deux choses sont vraies : héritage déclarée, maison propre.

**Je peux avoir les deux installés ?**
Techniquement oui (paquets distincts). La question utile est celle de toujours : qu'apporte le second que le premier ne couvre pas ? Si la réponse est « rien », un lecteur suffit.

**Et Anikku ?**
C'est le client d'anime de l'organisation Komikku — il a son propre guide dans cette collection (branche anime pur). La famille s'étend : mangas (Komikku), anime (Anikku), et le rebaptisé AniZen dans sa branche à part.

**Lequel sortit la version plus récente ?**
Aucun des deux en septembre : SY 1.13.2 et Komikku 1.14.1 sont de juillet — avec du code des deux bougeant ce mois-ci. Le push ne retagge pas : la release s'ouvre le jour où on installe.

## 🔗 Liens

- TachiyomiSY : https://github.com/jobobby04/TachiyomiSY · https://github.com/jobobby04/TachiyomiSYPreview
- Komikku : https://github.com/komikku-app/komikku · https://github.com/komikku-app/komikku-preview
- Distingués du réseau : https://github.com/PineappleTwilight/houri · https://github.com/Smol-Ame/Chai · https://github.com/jeryjs/TachiyomiSY-with-discord-RPC · https://github.com/Viel0320/komikku_img_upscale · https://github.com/nas3ts/mikku
- La couche que le graphe cache : https://github.com/Harrys-HQ/ShinKu · https://github.com/ruzhe85/MihonSY · https://github.com/pokedo0/Pokomi · https://github.com/the-nexus-app/NEXUS · https://github.com/geograms/bchan
- Entrepôts de la branche : https://github.com/keiyoushi/extensions · https://github.com/yuzono/tachiyomi-extensions · https://github.com/cuong-tran/manga-repo
- Synchronisation : https://github.com/syncyomi/syncyomi
- Guides sœurs : extensions (pièce 04) · forks du tronc (pièce 06) · anime pur (pièce 14) de cette collection

> La Bandita rapporte à partir de sources datées. Deux écoles, une même lignée — et le panneau, tu sais déjà, n'installe rien.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : Houri v1.22.1 d'AUJOURD'HUI, manga-repo ★445, SY/Komikku re-comptés. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
