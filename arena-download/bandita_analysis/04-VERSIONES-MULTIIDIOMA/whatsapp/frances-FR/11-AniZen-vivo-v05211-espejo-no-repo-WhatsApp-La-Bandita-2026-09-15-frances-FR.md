# Publicación 11 — AniZen est vivant en v0.5.211 : le miroir n'est pas le dépôt et l'issue s'écrit bien ou ne s'écrit pas

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 11)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🧬 La lignée : Anikku → AniZen
├── 🪞 Canonique vs miroir
├── 🚫 Ce que N'EST pas AniZen (et son propre README le dit)
├── 📋 L'art du bon rapport de bug
├── 📵 Le cas du diagnostic vieux
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

```
AniZen — vérifié AUJOURD'HUI, 14 septembre
Dépôt :         github.com/salmanbappi/AniZen
État :          vivant · push du 13-sep
Version :       v0.5.211 (publiée le 13-sep)
                la série : 0.5.209 (23-aoû) · 0.5.210 (5-sep)
                · 0.5.211 (13-sep) — rythme de corrections
                hebdomadaire
Étoiles :       182 · Apache-2.0
Paquet :        app.anizen
```

**Pouls de re-vérification (14-sep, soir #20) :** ouvert le dépôt de nouveau AUJOURD'HUI : **v0.5.211 reste la dernière release** — il n'existe pas de version plus neuve que celle d'en haut. Le rythme réel de la série récente : cinq releases en trois semaines (0.5.207 → 0.5.211) — cadence hebdomadaire : la stable ne va pas à vitesse de train (la beta est une autre histoire — bloc suivant) — mais elle n'est pas arrêtée. Et œil aux boutiques : sous le paquet `app.anizen` **il n'y a pas de fiche publique sur Google Play** (comprobé AUJOURD'HUI) — si un groupe te montre une « version vieille de mois », c'est un miroir, pas la maison. Le miroir n'est pas le dépôt : pour ça ce guide ne donne que le lien du dépôt.

**La beta, fichée (14-sep, soir #21 — le lien qu'apporta le propriétaire) :** github.com/salmanbappi/anizen-preview — « Automated Preview Builds for AniZen ». Ici est le train, et de vrai : **981 releases** publiées en automatique (la r4620 est du 13 septembre ; huit builds en file entre le 12 et le 13 ; le commit initial le signa « Gemini Automation » — le dépôt compile et publie tout seul). Et le cas du « presque 1000 » resta résolu avec compte : ce n'étaient pas des ressenhas — c'étaient des **releases** : 981 et comptant. La stable (en haut) voyage à la semaine ; la beta, plusieurs fois par jour. Beta pour essayer ce de demain ; stable pour vivre ce d'aujourd'hui.

AniZen est un client libre d'anime pour Android, actif cette même semaine. Ce guide fait deux choses avec son nom : il te donne l'état réel du projet (en haut, du jour), et il enseigne la partie que presque personne n'enseigne — comment se rapporte un panne pour que le développeur puisse le réparer. Parce qu'il y a une différence entre se plaindre dans un groupe et ouvrir un rapport qui sert.

## 🧬 La lignée : Anikku → AniZen

Aucune app ne naît de nulle part, et AniZen a un pédigré documenté dans ses propres dépôts :

```
komikku-app/anikku          ★1.025
   « Free and open source anime watcher for Android »
   L'organisation de Komikku (un des lecteurs
   mangas plus actifs de l'écosystème) maintient ce
   client d'anime.
   Version 0.2.0 publiée le 11 septembre —
   cette même semaine.

        │  quelqu'un prend ce code

「Anikku Mod」
   une version modifiée, d'un autre auteur

        │  commit du 28 janvier 2026

AniZen
   le rebrand : « transform Anikku Mod into AniZen »,
   ça consta dans l'historique du dépôt. Même lignée
   déclarée, maison et nom propres.
```

Que signifie un rebrand, en créole ? Le projet changea de nom et de maison — et il le déclare. Ce n'est pas un clone (ça, il apparaît de nulle part avec le nom d'un autre) ; c'est une continuité documentée : même code base évolué, auteur identifié, historique public. La différence entre rebrand et clone est exactement cette déclaration avec historique — la même qui distingue un déménagement d'une perquisition.

Pour qui cherche le client d'anime de l'organisation Komikku directement : c'est Anikku, et sa 0.2.0 de ce mois est sa version plus fraîche. Deux maisons sœurs, deux rythmes : l'originale avec son organisation derrière, la rebaptisée avec son développeur individuel poussant chaque semaine.

## 🪞 Canonique vs miroir

```
github.com/salmanbappi/AniZen    ← LA MAISON
   Le dépôt canonique : ici pousse l'auteur,
   ici sortent les versions, ici on rapporte.

github.com/Gaijin81/anizen       ← LE MIROIR
   ★0, copie sans vie propre. Il existe ; il ne commande pas.
```

La règle qui épargne des demi-heures de confusion : **le miroir n'est pas le dépôt.** Au miroir on ne rapporte pas de bugs (personne là-bas ne va les lire ni les réparer), et ses versions peuvent avoir du retard par rapport à la maison. Comment sait-on laquelle est la maison ? Par où il y a de l'activité réelle : releases signées, push récent, auteur qui répond. Le reste sont des photocopies — quelques-unes fidèles, aucune avec atelier.

## 🚫 Ce que N'EST pas AniZen (et son propre README le dit)

La phrase est dans le projet même, et il convient de la souligner parce que le nom circule dans des conversations où on attend autre chose :

**« AniZen does not have or fix any extensions »** — AniZen n'apporte ni ne répare d'extensions.

Le client est l'app. Les sources sont une autre couche — celle des parsers de l'écosystème — et les problèmes de lecture d'une source concrète ne se rapportent pas au dépôt de l'app : là-bas ils les ferment hors de portée, avec raison. Avant d'ouvrir n'importe quel rapport, la première question est : ça échoue dans l'APP (ça se ferme, ça ne sauve pas, l'interface casse) ou dans la SOURCE (telle série ne charge pas, tel serveur va lent) ? La seconde n'est pas problème de l'app — même si ça fait mal.

## 📋 L'art du bon rapport de bug

Le template du dépôt demande, checkboxes incluses, exactement ce qu'un développeur a besoin pour reproduire ton problème. L'anatomie du rapport qui sert, elle :

```
Titre :         une ligne, spécifique
                ✗ "L'app ne marche pas"
                ✓ "Crash en ouvrant l'onglet Historique
                   avec plus de 500 entrées"

Pas :           comment arriver au panne, numéroté,
                depuis app ouverte
                1. J'ouvre AniZen
                2. Je vais à Historique
                3. ...

J'attendais :   ce qui devrait se passer
J'ai obtenu :   ce qui se passe à la place

Crash log :     si l'app se ferme toute seule, le log
                qu'elle-même offre de partager
                (sans données personnelles au milieu)

Version :       le nombre EXACT — à AUJOURD'HUI 15-sep, v0.5.211.
                « La dernière » n'est pas un nombre : demain
                c'en est une autre. L'onglet À propos le dit.

Téléphone :     modèle et version d'Android

Avant d'envoyer (les checkboxes du template) :
   □ Ce n'est pas un doublon d'une issue ouverte
   □ Le titre est spécifique
   □ Je suis dans la dernière version
   □ Les nombres sont spécifiques
```

Et la grammaire du canal : les issues de ce dépôt s'écrivent en anglais, courtes, sans emojis, UN problème par rapport. Les rapports vagues — « ça marche pas, réparez » — meurent fermés comme « not planned », et l'exemple de la maison est l'issue #50 : une plante de ce qui N'EST pas un rapport. Ce n'est pas méchanceté de mainteneur : c'est qu'un bug qui ne peut pas se reproduire ne peut pas se réparer.

La règle de fond de cette famille : le rapport l'écrit une personne, avec ses mains et son compte — jamais il ne s'envoie au nom de personne ni par personne. Un rapport de bug est du courrier institutionnel de l'ère digitale : avec expéditeur, avec données, avec manières.

## 📵 Le cas du diagnostic vieux

Dans les vieux textes de la communauté existait un diagnostic d'un panne de AniZen sur un téléphone TECNO. Ce texte circula incomplet, donc ici on ne le reconstruit pas de mémoire ni on n'invente des pas — la règle est simple : ce qu'on ne peut pas ouvrir et vérifier, ne se prescrit pas.

Ce qui sert, générique et vérifié par le sens commun du métier, c'est la liste de cheque avant de blâmer l'app :

```
□ La version est-elle celle d'aujourd'hui ? (v0.5.211)
□ Le panne se reproduit-il deux fois de suite
  avec les mêmes pas ?
□ Ça arrive aussi avec une autre source, ou une autre série ?
  (si une seule source échoue : c'est la couche de
  sources, pas l'app)
□ Y a-t-il espace libre et mémoire suffisants ?
□ Le log du crash dit-il quelque chose de cohérent ?
```

Si le panne passe la liste — il se reproduit, de l'app, en version vigente — alors oui existe un rapport à écrire, avec l'anatomie d'en haut. S'il ne passe pas, on observe et on note : la moitié des « bugs » du monde sont des conditions, pas des erreurs.

Et l'avis de confidentialité qui ne sobre jamais : en rapportant ne voyagent ni ton IMEI, ni tes captures avec compte, ni ton numéro de téléphone. Le développeur a besoin du crash log et des pas — pas de ton identité.

## ❓ Questions fréquentes

**AniZen est-il sûr / fiable ?**
C'est un projet vivant, avec licence Apache-2.0, push de cette semaine et versions hebdomadaires. « Fiable » à long terme le construit l'historique : la maison y est, l'atelier pousse, et la lignée (Anikku) est d'une organisation sérieuse de l'écosystème. Chacun ouvre le dépôt avant d'installer — comme avec tout.

**AniZen ou Anikku ?**
Frères de code : Anikku est celui de l'organisation Komikku (0.2.0 cette semaine) ; AniZen le rebaptisé avec développement individuel hebdomadaire. Même lignée déclarée, maisons distinctes. Celui que tu préfères suivre — mais depuis sa maison.

**Pourquoi ma source favorite ne charge pas ? Je le rapporte à AniZen ?**
Non : l'app n'a ni ne répare d'extensions (son README le dit tel quel). Le panne d'une source est sujet de la couche de sources de ton écosystème.

**Où je télécharge la bonne version ?**
De Releases dans la maison : github.com/salmanbappi/AniZen/releases — aujourd'hui v0.5.211. Sens-toi libre de la rouvrir le jour où tu installes : cette page est la seule horloge qui commande.

**Le miroir de Gaijin81 sert à quelque chose ?**
À rien que la maison ne fasse mieux. On n'y rapporte pas, on n'y télécharge pas, on ne le cite pas comme source.

**Je peux demander des fonctions neuves par issue ?**
Chaque dépôt a sa politique pour ça (les templates le disent). L'universel : une pétition par issue, avec cas d'usage concret — « j'aimerais X parce que quand je fais Y je ne peux pas Z » vaut plus que « ajoutez X ».

**Qui écrit l'issue si un groupe entier a le même bug ?**
Celui qui saura le mieux le reproduire. Les autres ajoutent un « ça m'arrive pareil, avec telle version et tel téléphone » — donnée, pas bruit.

## 🔗 Liens

- AniZen (la maison) : https://github.com/salmanbappi/AniZen · https://github.com/salmanbappi/AniZen/releases/latest
- AniZen beta (le train quotidien) : https://github.com/salmanbappi/anizen-preview
- Anikku (la lignée originale) : https://github.com/komikku-app/anikku
- Le miroir (nommé, pas utilisé) : https://github.com/Gaijin81/anizen

> La Bandita rapporte à partir de sources datées. Le miroir n'est pas le dépôt, et le rapport qui sert a des nombres, des pas et des manières.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : re-vérifié à AUJOURD'HUI. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.

**Pouls de déménagement (15-sep) :** rouvert le dépôt AUJOURD'HUI : v0.5.211 reste la dernière stable (★182) ; la preview continue de lâcher — son build r4622 est d'AUJOURD'HUI même. Ce qui fut dit : le miroir n'est pas le dépôt.
