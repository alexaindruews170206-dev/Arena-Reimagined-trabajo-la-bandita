# Publicación 15 — Branche J2K : le grand-père est revenu — tachiyomiJ2K, Yōkai, Rokku, Reikai et le fantôme Hayai apparut

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 15)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🌳 L'arbre de cette branche
├── ⚡ tachiyomiJ2K — le grand-père s'éveilla
├── 👻 Yōkai — le tronc en pause active
├── 🪇 Rokku — le fork de maintien pratique
├── ⛩️ Reikai — mangas et romans dans une bibliothèque
├── 🐇 Hayai — le fantôme a maison (et on peut l'ouvrir)
├── 🌲 Le réseau complet de forks (révisé le 14-sep)
├── 🧬 Les cousins mineurs de la branche
├── 📜 L'histoire qui explique cette branche
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

C'est la branche de l'interface aimé : celle qui naquit de tachiyomiJ2K — le fork qui redessina Tachiyomi — et enfanta une famille entière. La première chose à dire est la nouvelle grande : **tachiyomiJ2K se remit à publier des versions en août 2026 après deux ans et demi de silence.** Et la seconde : **Hayai — le projet qui pendant des mois fut un fantôme sans dépôt accessible — a aujourd'hui maison publique et on peut l'ouvrir.**

```
tachiyomiJ2K  ★5 383  v1.8.1 (15-aoû-2026)  le grand-père, de retour
Yōkai         ★1 883  v1.10.1 (4-sep)     push d'hier (14-sep) — le tronc
Rokku         ★51     v1.7.1 (29-aoû)     celui du maintien
Reikai        ★27     v0.3.2 (4-sep)      mangas + romans unifiés
Hayai         ★41     v1.13.0 (10-avr)    celui qui n'est déjà plus fantôme
```

Toutes les fiches s'ouvrirent et se vérifièrent AUJOURD'HUI, 14 septembre. Où la vie personnelle des mainteneurs explique les rythmes du projet, on la compte comme eux la racontèrent : citée, datée et sans commérage.

## 🌳 L'arbre de cette branche

```
tachiyomiJ2K (l'interface redessiné)
         │   v1.7.4 (jan-2024) → deux ans de silence
         │   → v1.8.0 et v1.8.1 (août 2026) : IL REVINT
         │
         ├── Yōkai        le fork personnel de null2264
         │     ├── Rokku    fork de Yōkai : maintien
         │     ├── Reikai   commença dans Yōkai, rebasé sur Mihon
         │     └── Hayai    J2K-based, mangas + romans
         │
         ├── yomu         J2K-based, petit
         └── TachiyomiDNP variante petite, active en août
```

## ⚡ tachiyomiJ2K — le grand-père s'éveilla

https://github.com/Jays2Kings/tachiyomiJ2K

```
★5 383 · Apache-2.0
v1.7.4 → janvier 2024 (la fermeture de l'ère vieille)
v1.8.0 → 9 août 2026 « Warning: Funny numbers ahead »
v1.8.1 → 15 août 2026 « Wait, there's more? »
```

Son histoire en deux actes : il fut LE fork de l'ère dorée — celui qui inventa le redessin visuel que la moitié de la famille hérita — puis se tut pendant deux ans et demi, jusqu'à août 2026, quand il lâcha deux versions en une semaine avec son humour de toujours dans les titres. La communauté le considère le père de la migration massive de bibliothèques : il fut le premier à bouger des bibliothèques complètes entre lecteurs.

Son retour ne le ressuscite pas comme candidat quotidien — deux versions ne sont pas un rythme — mais le rend bien à la carte comme histoire vivante : le grand-père n'est pas mort, il était en voyage. Qui veut l'expérience J2K « pure », sa maison est de nouveau ouverte et avec des versions de cette année.

## 👻 Yōkai — le tronc en pause active

https://github.com/null2264/yokai

```
★1 883 · Apache-2.0 · push d'hier (14-sep)
v1.10.0 et v1.10.1 (toutes deux le 4 septembre)
Support : extension-lib 1.6 · Android 8+ (sa note de version)
```

Yōkai est le fork personnel de null2264 : il prit l'interface J2K et le soutient seul. Son propre mainteneur l'expliqua dans la note de la version de septembre, avec une honnêteté qui vaut d'être citée : il fit un pas en arrière de ses projets par burnout, avec la thèse et le travail dessus, avec l'espoir de revenir « avant le nouvel an » et en révisant des contributions de temps en temps. Il appela sa propre version « assez peu polie ». Et la même note s'ouvre avec un avertissement en majuscules qu'il convient de respecter : « BACKUP YOUR DATA » — copie tes données avant d'actualiser.

Ce que disait la donnée du 14 : la branche n'est pas abandonnée — le dépôt poussa hier (14-sep). Ce que ça dit aussi : c'est un projet d'une personne avec une vie dessus, et son rythme le marquera cette vie. La leçon de la branche entière sort d'ici : les mainteneurs sont des personnes ; le burnout est réel ; et l'honnêteté d'un changelog vaut plus qu'une roadmap fausse.

## 🪇 Rokku — le fork de maintien pratique

https://github.com/rokku-app/rokku

```
★51 · Apache-2.0
v1.6.1 (15-aoû) · v1.7.0 (23-aoû) · v1.7.1 (29-aoû)
— trois versions en deux semaines : cadence ferme
Naît de : Yōkai, pour le maintenir au jour avec
l'écosystème d'extensions et dépendances
```

Rokku existe pour la raison plus pratique du monde : quand Yōkai se mit en pause, quelqu'un décida de maintenir l'expérience vivante et au jour — extensions modernes, corrections de performance, le travail sale et nécessaire. Ses notes d'août se concentrent en exactement ça : réglages de performance et de téléchargements, compatibilité avec la librairie d'extensions moderne et soins hérités de l'interface — le travail qui ne sort pas en captures mais maintient une app vivante.

C'est la fiche plus petite en étoiles de la branche et celle qui bouge plus en arrangements. L'étoilement mesure la renommée ; la cadence mesure l'atelier. Et il y a plus de signal d'atelier vivant : Rokku a canal nocturne propre (rokku-nightly) avec builds presque quotidiens — le dernier vu était d'hier. *(Re-vérifié le 15-sep : le dernier nightly est le r7091, du 13-sep — la cadence suit ; la date, actualisée.)* Quand une maison compile de nuit, elle travaille de jour.

## ⛩️ Reikai — mangas et romans dans une bibliothèque

https://github.com/unseensnick/Reikai · Site : https://reikai.app

```
★28 · Apache-2.0 · push du 14-sep (jour de la vérification) · v0.3.2 (4-sep)
v0.3.2 (4-sep) · v0.3.1 (9-aoû) · v0.3.0 (16-juil)
Naît de :     commença comme fork de Yōkai — le graphe de
              GitHub l'annote encore ainsi — et son projet
              raconte que le code fut rebasé après
              sur Mihon
A : version FOSS à part (sans reportes de crash ni
analytique) — reikai-foss dans ses releases
```

Reikai est l'idée plus différenciée de la branche : UNE bibliothèque où la même série de mangas et de romans légers vivent ensemble. Ses fonctions déclarées : groupement multi-source (plie la même série de sites distincts en une entrée), fusion manuelle quand les titres ne coïncident pas, lecture fusionnée avec liste de chapitres unifiée, synchronisation de trackers partagée dans le groupe, et bibliothèque de romans de premier niveau avec support du lecteur de LNReader.

Sa philosophie, dite par son auteur : construit d'abord pour son usage quotidien — le développement est sporadique et les fonctions suivent ses goûts. Cette honnêteté définit ce que c'est : un projet personnel très bien documenté (son site web complet le confirme), pas un produit avec promesses d'équipe.

## 🐇 Hayai — le fantôme a maison (et on peut l'ouvrir)

https://github.com/HayaiApp/hayai

```
★41 · Apache-2.0
v1.13.0 (10 avril 2026) · push du 6-sep
Ce que c'est : « Hayai est un lecteur Android basé sur
TachiyomiJ2K avec mangas et romans légers »
(selon sa propre description)
```

Ici est la surprise de cette branche : pendant des mois, Hayai fut le projet fantôme — mentionné dans des listes et des changelogs d'autrui, avec son dépôt inaccessible, impossible d'évaluer. Aujourd'hui le dépôt s'ouvre, on peut le lire, et il dit ce qu'il est : J2K-based, mangas et romans légers, avec version d'avril et activité du mois passé.

Ce qui est vérifiable aujourd'hui : la maison existe, la licence est déclarée, il y a release étiquetée. Et son README —lu entier AUJOURD'HUI— précise la recette avec une honnêteté rare : architecture J2K déclarée comme base et source de vérité, support de sources adult reconstruit sur les contrats de TachiyomiSY, plugins de romans au style LNReader, et « importation défensive » de la base de données du vieux Hayai — l'archive de l'ère fantôme soigne encore qui l'utilisa. Ce qui reste pas encore : si son développement est soutenu — sa dernière version a cinq mois, même si son dépôt bougea la semaine passée. Fiche neuve, suivi ouvert : au fantôme on donne un mois de vie publique avant n'importe quel verdict. C'est la règle de la maison — la rumeur se comprove dans la maison du projet, et parfois la maison apparaît.

**Et la famille Hayai grandit par le côté que personne ne regardait :** le même org publia **HayaiTTS** (★39) — un moteur de texte-à-voix neuronal OFFLINE pour Android : il s'enregistre dans le système entier et apporte 186 voix (Piper et Kokoro, via sherpa-onnx). Dernière version : 2.5.1, du 15 juin. La pièce qui manquait du casse-tête : lire le roman… ou l'écouter. Pour qui lit des romans légers dans le bus, c'est la clôture du cercle.

## 🌲 Le réseau complet de forks (révisé le 14-sep)

Les réseaux des cinq projets s'ouvrirent fork par fork aujourd'hui dans l'API de GitHub — incluse celle de J2K, qui cache au parent riche que presque personne ne nomme :

**Dans le réseau de J2K :**

- **TachiyomiS97** (Saud-97, ★125) — le prince de cette branche et son fork le plus suivi : « une version plus rapide de Tachiyomi ». Ses fonctions propres, de son README : actualisations globales jusqu'à 5× plus rapides, téléchargements jusqu'à 3× plus rapides, progression multi-appareil via trackers (expérimental), auto-téléchargement du chapitre suivant pendant que tu lis, et recherche par URL dans le global search. Et l'histoire se répète : v1.7.5 du 1er août 2026 après se taire depuis janvier 2024 — la paire du grand-père : tous deux s'éveillèrent cette année.

**Dans le réseau de Yōkai (100+ forks) :**

- **yurei** (NotBlankyu, v1.10.1 du 21-aoû) — la variante avec ambition : mangas + webnovels, mode texte qui rend le chapitre comme texte au lieu d'images, filtre NSFW hérité de SY, et lecture locale qui maintenant lit ComicInfo.xml par chapitre.
- **yokai-T** (KakarottoCake, v1.0.2 du 4-juil) — streaming et téléchargement par torrent, son pari propre.
- Un fork avec **dossiers personnalisés** (collections multi-série avec ordre et backup) poussa le 14-sep (constance du jour) — sans releases encore.
- Réseau complet avec noms propres : kagura, Mekuri (local-first), Miko, Karasu, et une variante Komga+galerie. Plus les copies ★0 d'usine, qui sont la majorité.

**Et les réseaux petites :** Rokku a 3 forks (tous ★0, un poussa le 14-sep — réseau nouveau-né) ; Reikai en a 5, avec **Nekoumy** (Zykrave, le même auteur de Kuro : « une bibliothèque pour mangas et romans », push du 12-sep) ; Hayai en a 4, toutes copies ★0. Plus la maison est jeune, plus sa traînée est petite — pour l'instant.

**L'expédition profonde (J2K : 999 membres · Yōkai : 125 — marché le 14-sep jusqu'aux feuilles) :** dans la couche habile de ces réseaux, le vivant avec proposition propre : **yurei** a déjà un fils actif — le fork pour utilisateurs **MIUI/HyperOS**, qui corrige ce que l'optimisation d'usine de Xiaomi encombre, et va par v1.11.0. Dans la ligne Yōkai, feuilles avec nom et pouls : **Miko**, **Karasu**, **kagura**, **Mekuri** (local-first), **shuo** (romans) et **MiruKan** (avec version propre, v1.0.1 de mai). Et l'atelier Hayai se complète : canal nocturne avec builds de cette semaine (hayai-nightly) *(re-vérifié le 15-sep : le dernier build daté du canal est le r6674, du 6-sep)* à côté du **HayaiTTS** fiché en haut. Le reste de la couche profonde sont des copies sans apports : hors de la carte.

## 🧬 Les cousins mineurs de la branche

Pour compléter la carte, les dépôts petits que la recherche du jour apporta — nommés avec leur taille réelle :

```
yomu (HugoFMiranda)          ★3   J2K-based, push juil-2026
TachiyomiDNP                 ★4   variante, push 16-aoû
Hiirbaf/yokai                ★3   fork de Yōkai, push du 13-sep
```

Aucun n'atteint la porte de maturité pour se recommander comme alternative quotidienne — mais ils se nomment parce qu'exister aussi est information, et parce que n'importe lequel peut être le prochain Rokku (qui il y a six mois était aussi petit). Les copies sans propriétaire actif, même pas ça : des copies à horloge.

## 📜 L'histoire qui explique cette branche

Cette branche est la meilleure classe d'histoire de l'écosystème : celle de l'héritage qui se répartit.

```
2019–2023   tachiyomiJ2K définit l'interface moderne
            du lecteur mangas libre. La migration
            massive de bibliothèques naît ici.

jan-2024    Tachiyomi original ferme (pression légale).
            J2K se tut. Les utilisateurs de l'interface J2K
            restent orphelins.

2024–2025   Yōkai recueille l'héritage de l'interface.

2026        La famille se ramifie par nécessité :
            Rokku maintient, Reikai joint des formats,
            Hayai sort de l'ombre, et le grand-père
            même revient en août.
```

Cinq projets vivants où il y en avait un silencieux. La leçon de la branche : quand un atelier ferme, ce n'est pas la fin du métier — c'est le partage des outils.

## ❓ Questions fréquentes

**tachiyomiJ2K « revint » de vrai ou ce fut ponctuel ?**
Deux versions en une semaine d'août, avec étiquettes et notes — c'est un retour réel d'activité. S'il y aura cadence, l'automne le dira ; sa releases page est l'horloge.

**Yōkai ou Rokku si je venais de l'interface J2K ?**
Yōkai est le tronc avec le mainteneur original en pause active ; Rokku est la branche de maintien avec cadence d'août. La différence pratique est dans son rythme — et toutes deux s'ouvrent le jour où on décide.

**Reikai remplace-t-il mon lecteur de mangas normal ?**
Il ne vient pas remplacer : il apporte la fonction que presque personne n'a — mangas et romans dans UNE bibliothèque, avec la même série groupée même si elle vient de sources distinctes. Si tu ne lis pas de romans, c'est plus d'app que ce dont tu as besoin.

**Hayai était une mythe alors ?**
C'était un projet réel sans porte. Aujourd'hui la porte existe, la licence est déclarée et il y a version étiquetée. Le mythe resta en histoire — et cette correction est exactement pour quoi les guides portent date.

**Laquelle a la version plus fraîche de la branche ?**
Yōkai et Reikai : 4 septembre. Rokku : 29 août. Hayai : 10 avril. J2K : 15 août. Les nombres périssent — la page de releases de chacun non.

**Et le fork « plus rapide » (TachiyomiS97) ?**
C'est le fork le plus suivi du réseau de J2K (★125) et ses promesses sont écrites dans son README : il revit en août 2026 avec optimisations d'actualisations et téléchargements. La règle ne change pas : les nombres de performance de n'importe quel fork se comprovent en usage propre — et sa page de releases, ouverte le jour où on décide.

**Les cousins mineurs (yomu, DNP) ?**
Ils se nomment, ils se mesurent, ils ne se recommandent pas : ils ne passent pas encore la porte de maturité. Demain peut être une autre histoire — avec date, on le dira.

**Pourquoi autant de « son propre mainteneur dit » dans ce guide ?**
Parce que dans une branche de projets personnels, la parole du mainteneur EST la source primaire : Yōkai expliqua sa pause, Reikai explique sa philosophie, J2K signe avec humour ses retours. Les citer avec date, c'est les vérifier.

## 🔗 Liens

- tachiyomiJ2K : https://github.com/Jays2Kings/tachiyomiJ2K
- Yōkai : https://github.com/null2264/yokai
- Rokku : https://github.com/rokku-app/rokku
- Reikai : https://github.com/unseensnick/Reikai · https://reikai.app
- Hayai : https://github.com/HayaiApp/hayai
- Distingués du réseau : https://github.com/Saud-97/TachiyomiS97 · https://github.com/NotBlankyu/yurei · https://github.com/KakarottoCake/yokai-T · https://github.com/Zykrave/Nekoumy
- Cousins : https://github.com/HugoFMiranda/yomu · https://github.com/theordinaryguy23/TachiyomiDNP · https://github.com/cuong-tran/tachiyomiJ2K

> La Bandita rapporte à partir de sources datées. Le grand-père revint, le fantôme a maison — et la branche entière se vérifia aujourd'hui.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : Yōkai ★1 883 (push du 14), Reikai ★28 (v0.3.2 du 4-sep), réseaux petites re-datées. Le J2K et ses 999 membres de réseau, constatés à son jour (14-sep). PV complet : Registre #71.
