# Publicación 80 — L'ému dans la poche : WinNative apporte les jeux de Windows sur Android — et GDealz et Axekin complètent la donne

**La Bandita · 20 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 80)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🪟 WinNative — l'ému communautaire de Windows x86_64
├── 🎯 GDealz — le chien de chasse des bonnes affaires
├── 🏪 Axekin — la boutique derrière la porte anti-bot
├── ⚖️ Comment joue le trio
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Cette pièce naît de liens du propriétaire — comme Debrify dans la Publicación 23 — et ouvre un terrain nouveau dans la collection : **l'émulation**. Trois maisons, vérifiées AUJOURD'HUI, 20 septembre : celle qui **exécute** les jeux de Windows sur Android (WinNative, ★591), celle qui **signale** où sont les bonnes affaires et les cadeaux gratuits de ces mêmes boutiques (GDealz, ★52), et la **boutique** qui arrive avec sa propre porte (Axekin). Tout vérifié à source ouverte, avec date — et ce que la machine n'a pas pu lire, dit sans déguisement.

## 🪟 WinNative — l'ému communautaire de Windows x86_64

https://github.com/WinNative-Emu/WinNative

```
★591 · GPL-3.0
v0.6.2-beta (12 septembre 2026)
Ce que c'est : « An Android app for playing Windows games
from Steam, Epic Games, GOG, and more on your
device » — sa description ; et son README (lu
AUJOURD'HUI) le précise : environnement d'émulation
Windows (x86_64) haute performance qui unifie le
meilleur de Winlator Bionic et de Pluvia
```

Ce que sa maison déclare, avec date :

- **Bibliothèques connectées :** Steam, Epic et GOG — les jeux s'ajoutent à la main ou la bibliothèque se synchronise. Ton compte, tes jeux, ton toujours.
- **Consoles rétro à côté :** de la NES à la PlayStation 2, avec sa documentation propre (docs/RETRO-CONSOLES.md) — l'ému de Windows et la rétrovivienda sous le même toit.
- **Génération d'images :** LSFG et DIS, documentées dans son README (docs/FRAME-GENERATION.md) — le remplissage d'images qui avant était chose de PC chers.
- **Installation :** l'APK se prend dans ses Releases ; au premier lancement il laisse installer l'ImageFS et on joue. Quatre variantes, la même app avec un nom de paquet différent : **Vanilla** (standard, pour cohabiter avec d'autres forks), **Ludashi** (force GPU et CPU au maximum sur certains appareils), **Antutu** (force les horloges GPU sur la plupart — spoof de benchmark, son propre README le dit) et **Pubg** (nom de paquet de PUBG qui débloque des fonctions de Game Booster).

Les variantes Antutu et Ludashi méritent la leçon de la maison : dans la Publicación 10 on a raconté pourquoi un benchmark sans source ne se cite pas même par erreur. Ici le repo **déclare ouvertement** ce que ses variantes font — et c'est ça, le bon chemin : qui mesure, qu'il sache ce qu'il mesure. La fiche s'annote avec cette date et cette honnêteté.

Communauté propre sur Discord, licence GPL-3.0 et version bêta qui se dit bêta : v0.6.2-beta. On teste, on enregistre, on attend — comme le TTS de la Publicación 18. Projet jeune avec du métier : son arbre de documents (BUILDING, CREDITS, EMULATOR_CREDITS) trahit un atelier bien rangé.

## 🎯 GDealz — le chien de chasse des bonnes affaires

https://github.com/Rajkumarbhakta/GDealz/

```
★52 · GPL-3.0
v1.3.4 (22 juillet 2026)
Ce que c'est : « PC GAME deals application. » — sa
description ; son README (lu AUJOURD'HUI) étire :
« PC Game Deals Tracker (Android) », sans publicités
et open source
```

Le compagnon naturel de l'ému : si WinNative exécute la bibliothèque, GDealz surveille le prix de ce qui y entre. Ce que son README déclare : des bonnes affaires quotidiennes de **Steam, Epic Games Store, GOG, Fanatical et plus** ; des alertes pour les **jeux gratuits** et les giveaways ; filtres par boutique, fourchette de prix et pourcentage de remise ; tri par prix, popularité ou réduction ; liste d'envies pour les favoris et les cadeaux marqués comme réclamés ou en attente. Sans publicités — ce qui, à cette porte, est déjà une déclaration de principes.

## 🏪 Axekin — la boutique derrière la porte anti-bot

https://www.axekin.com/

```
HTTP 200 (20-sep) — mais avec un mur
Ce qu'il y a : une porte anti-bot (Anubis) qui demande
JavaScript pour distinguer le lecteur du robot
Ce qu'il n'y a PAS : du contenu lisible par machine
```

Ici la maison applique sa règle la plus vieille : **ce que la source ne laisse pas lire, ne se cite pas**. Axekin a répondu AUJOURD'HUI avec HTTP 200 — vivant — mais sa porte est un mur anti-bot (Anubis, la même protection que les projets libres utilisent contre le scraping agressif des IA). Cette maison respecte les portes : on ne force pas une web pour la citer. Le fiché reste ainsi : **la boutique existe, répond, et s'ouvre dans le navigateur le jour où on l'utilise** — comme toutes les boutiques de la Publicación 01. Son catalogue, ses conditions et son contenu : quand le propriétaire de cette maison les piétinera avec un lien en main, ils entreront avec date. Pas une donnée ne se simule.

## ⚖️ Comment joue le trio

```
EXÉCUTER   → WinNative : la bibliothèque de Windows
             (et les consoles rétro) dans le téléphone.
ÉCONOMISER → GDealz : signale les bonnes affaires et les
             jeux gratuits AVANT d'acheter.
PORTE      → Axekin : la boutique du propriétaire —
             s'ouvre au navigateur, avec sa serrure anti-bot.
```

La bibliothèque de PC se nourrit pas cher (GDealz) et se joue dans le canapé (WinNative). Le cercle, chacun le ferme avec ses comptes et ses lois — la maison fiche des outils, pas des comptes étrangers.

## ❓ Questions fréquentes

**WinNative est-il officiel de Valve, Epic ou GOG ?**
Non : c'est un environnement communautaire (community-built, dit son README) qui connecte tes bibliothèques — comme un lecteur connecte tes sources. Ton compte, tes jeux, tes conditions.

**Pourquoi « bêta » avec 591 étoiles ?**
Les étoiles mesurent la communauté, pas la maturité. Sa propre release dit v0.6.2-beta — et la maison préfère la parole du repo à l'enthousiasme du nombre.

**Les variantes Ludashi et Antutu trichent aux benchmarks ?**
Elles forcent les horloges au maximum, et leur README le déclare sans détour. La maison ne prescrit pas de benchmarks — mais elle annote quand un projet dit la vérité d'usine. La leçon de la Publicación 10, à l'envers : voilà comment on fait.

**GDealz offre les jeux ?**
Non : il signale les cadeaux que d'autres boutiques donnent. Le giveaway vient de la boutique ; l'app est le chien de chasse qui t'empêche de le rater.

**Et Axekin, pourquoi il ne s'ouvre pas ?**
Il s'ouvre — pour les personnes, pas pour les machines. Son mur anti-bot est légitime et respecté : la boutique se teste dans ton navigateur, le jour où tu en as besoin.

## 🔗 Liens

- WinNative: https://github.com/WinNative-Emu/WinNative
- GDealz: https://github.com/Rajkumarbhakta/GDealz/
- Axekin: https://www.axekin.com/
- Familles de la maison : Publicación 01 (les boutiques) · 10 (GLTools et l'éthique du benchmark) · 23 (Debrify, l'autre lien du propriétaire)

## Le mème du corte

> —J'ai mis Windows sur mon téléphone.
> —Et il a tourné ?
> —Il a tourné la bibliothèque : Steam, Epic, GOG. Et ce qui restait à payer, GDealz l'a signalé gratis avant que le portefeuille ne pose la question.

> La Bandita informa a partir de fontes datadas. L'ému se vérifie comme tout : lien ouvert aujourd'hui, fiche avec date — et les portes d'autrui, respectées.
