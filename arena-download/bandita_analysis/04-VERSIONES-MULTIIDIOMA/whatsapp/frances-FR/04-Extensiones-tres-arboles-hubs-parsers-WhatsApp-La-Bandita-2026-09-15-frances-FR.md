# Publicación 04 — Extensions des trois arbres : hubs vivants et la portée d'imposteurs

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 04)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🧩 Ce qu'est une extension (les trois couches)
├── 📗 Keiyoushi : le hub principal
├── 📘 Yūzōnō : anime et l'étagère « cursed »
├── 📙 Les autres entrepôts vivants
├── 🧬 La convention KeiSource 1.6 (et la PR qui l'a sauvée)
├── 🗂️ Miyomi : le répertoire de tout ceci
├── 🎭 La portée d'imposteurs
├── 🧭 Comment lire un entrepôt sans rien avaler
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Les extensions sont la couche qui connecte un lecteur libre aux sources. Elles ne vivent pas dans l'app : elles vivent dans des entrepôts avec propriétaire, et l'état de chaque entrepôt change de semaine en semaine. Ce guide a révisé aujourd'hui — 14 septembre — tous les entrepôts vivants de l'écosystème, ceux morts avec date, la convention technique qui maintient tout fonctionnant, et une portée de dépôts imposteurs apparue cette semaine.

L'état du matin :

```
VIVANTS (tous avec activité récente)
Keiyoushi extensions          ★14 980   push 14-sep     le principal
Keiyoushi extensions-source   ★4 678    vivant au 15-sep     le code
cuong-tran/manga-repo         ★445      push 14-sep
Yūzōnō anime                  ★432      push 13-sep
Suwayomi/tachiyomi-extension  ★327      push 12-sep  (pour serveur)
Yūzōnō cursed                 ★185      push 9-sep
mojuru/cursed-manga-repo      ★160      push 3-aoû
Copymanga (communauté CN)     ★2 753    v1.4.85
ZGQ-inc/source (CN)           ★1 268    mégacollection

tachiyomiorg/extensions     ★546    jan-2024
stevenyomi/copymanga        ★1 918  fév-2024
```

## 🧩 Ce qu'est une extension (les trois couches)

```
L'app          le lecteur (Mihon, Komikku, Tadami...)
L'entrepôt     le lieu où vivent les extensions
               (ce guide)
L'index        la recette que l'app utilise pour lire
               l'entrepôt — un fichier d'installation
```

La règle de cette famille de guides sur la troisième couche : l'index ne se colle pas. Non parce que ce serait secret — il est dans le README de chaque projet — mais parce que coller des recettes d'installation dans un post est exactement le geste qui convertit un guide en hameçon. Qui veut l'index, qu'il le lise dans la maison du projet, le jour où il s'en sert.

## 📗 Keiyoushi : le hub principal

https://github.com/keiyoushi/extensions
Code : https://github.com/keiyoushi/extensions-source
Site : https://keiyoushi.github.io

L'entrepôt de référence de l'écosystème Mihon : plus de mille sources, un bot qui actualise l'index chaque jour (les « Repository Update » du 12, 13 et 14 septembre se voient dans son historique), et une communauté de traducteurs qui pousse le code chaque jour.

Son site web, ouvert aujourd'hui, apporte l'avis qui résout la moitié des doutes du monde : si ta liste d'extensions sort vide, ou si toutes figurent « obsolètes », avec le message « Outdated app » — ton application n'est plus compatible avec l'entrepôt. Ils supportent Mihon, TachiyomiSY et Komikku. La solution n'est pas de chercher un miroir : c'est d'actualiser l'app depuis son dépôt.

Un détail de transparence : l'entrepôt de binaires ne déclare pas de licence sur sa page (le code oui : Apache-2.0). C'est dit tel quel — sans licence visible, pas inventée.

## 📘 Yūzōnō : anime et l'étagère « cursed »

Anime : https://github.com/yuzono/anime-extensions
Code successeur : https://github.com/yuzono/kohi-den
Site : https://yuzono.github.io

Le canal vivant de référence pour les extensions d'anime dans l'arbre Tachiyomi — et à côté de lui, le code de la maison Kohi-den continue vivant dans la famille Yūzōnō (vérifié le 14-sep). Et la règle qui commande dans cette famille : la carte se note avec le vivant — chaque lien se rouvre le jour où on l'utilise.

Troisième pièce que peu nomment : yuzono/cursed-manga-extensions — l'étagère de contenu adulte (NSFW), avec activité du 9 septembre. Nommée parce qu'elle existe et s'actualise ; on ne colle pas son index ni on ne recommande son contenu. Ce que chacun lit est sujet de lui-même et de sa juridiction.

## 📙 Les autres entrepôts vivants

**cuong-tran/manga-repo** — ★445, push du 14-sep. Extensions pour Komikku/Mihon et forks. Des entrepôts indépendants, le plus actif.

**mojuru/cursed-manga-repo** — ★160, push du 3 août. La seconde étagère « cursed » de l'écosystème. Même traitement : nom oui, index non.

**Copymanga-copy20** (LittleSurvival) — ★2 753, version 1.4.85 du 8 septembre et « vomic » 1.4.4 du 4-sep. La communauté chinoise de sources pour Mihon/Tachiyomi : son README lie ses groupes de communauté. Sources centrées sur copymanga et ressources chinois.

**ZGQ-inc/source** — ★1 268. Mégacollection chinoise qui joint livres, images, règles et jusqu'à des sources de streaming. Nommée comme carte de l'écosystème chinois ; ce qu'il y a dedans ne se prescrit pas.

**Suwayomi/tachiyomi-extension** — ★327, push du 12 septembre. Cas à part : ce n'est pas pour le téléphone, c'est l'extension pour Suwayomi — le serveur de bureau de l'écosystème Tachiyomi (ta bibliothèque tournant sur le PC, lue depuis le navigateur). Une couche de plus : serveur.

**uchiyomi** — ★37, MPL-2.0, et deux versions publiées le 14-sep (v0.32.0 et v0.33.0). Le nouvel arrivé de cette couche : un lecteur self-hosted qui tourne comme PWA dans le navigateur — webtoon-first, pensé pour écrans OLED — et qui mange les MÊMES extensions de Mihon/Tachiyomi. Ta bibliothèque dans ton serveur, lue depuis n'importe quel navigateur, avec tout l'écosystème d'extensions derrière. La couche serveur vient d'inaugurer seconde maison — suivi ouvert.

## 🧬 La convention KeiSource 1.6 (et la PR qui l'a sauvée)

Les extensions ne sont pas des archives détachées : elles suivent une convention technique de l'écosystème. La vigente s'appelle KeiSource, version de librairie 1.6. Le document de contribution de l'écosystème (ouvert aujourd'hui, 1 813 lignes) le dit clair : les sources neuves étendent KeiSource avec libVersion 1.6, et la base ancienne (HttpSource, 1.4) reste en héritage.

Pourquoi ça importe pour qui lit seulement ? Parce que quand une app « ne voit » pas les extensions neuves, c'est presque toujours ça : l'app est vieille pour la convention. C'est l'autre face de l'avis « Outdated app » de Keiyoushi.

Le cas qui confirma la transition : la PR #448 d'Animetail — « resolve 1.6+ extension loading » — ouverte aujourd'hui et figurant fusionnée. Les lecteurs qui ne migrent pas à temps restent hors des entrepôts qui adoptent la convention.

## 🗂️ Miyomi : le répertoire de tout ceci

https://miyomi.app
Code du site : https://github.com/miyomiorg/Miyomi

Un répertoire communautaire qui catalogue apps, entrepôts d'extensions et guides de tout l'écosystème — la couverture se lit aujourd'hui, et son front-end est une application web vivante (ses recomptes internes n'ont pas pu être re-comptés aujourd'hui pour cette même raison : le catalogue vit dans la session du navigateur, pas dans un JSON public).

Son dépôt : ★189, licence AGPL-3.0, avec son propre code ouvert. Le projet déclare qu'il n'héberge pas de contenu et qu'il ne garantit ni sécurité ni légalité de tiers — un index d'index, avec l'honnêteté de qui sait que cataloguer n'est pas auditer.

« Approuvé » dans Miyomi signifie « il est dans son catalogue aujourd'hui ». Ça ne signifie l'aval de personne.

## 🎭 La portée d'imposteurs

La recherche de cette semaine a détecté des dépôts avec le même costume : étoiles identiques entre eux (115–120 dans plusieurs cas), activité du même jour, et titres d'annonce classée — « Best Manga Reader App 2026 », « Top Komikku Open Source Alternative », « Ultimate Multilanguage Hub for Usagi ».

```
Le costume de l'imposteur
★ identiques entre eux (115–120 dans plusieurs cas)
Titre de propagande, pas de projet
Sans historique propre : nés le 13-sep
Nom de projet connu + mot de vente
```

Ce ne sont ni entrepôts ni forks ni sources : ce sont des aimants à clics — et, soupçon raisonnable, d'installations empoisonnées. La règle pratique qui ne rate pas : si le titre sonne comme une annonce et que les étoiles ne cadrent pas avec l'histoire du projet, on n'ouvre pas, on ne lie pas, on n'installe pas.

## 🧭 Comment lire un entrepôt sans rien avaler

```
1. Qui le maintient ?
   Un bot d'un org avec historique > un compte
   sans visage né ce mois-ci.

2. Depuis quand pousse-t-il ?
   Historique de commits de mois/années > activité
   d'une seule semaine.

3. Le code est-il à vue ?
   extensions-source publié > binaires seuls.

4. Son site avoue-t-il ce qu'il ne sait pas ?
   Keiyoushi avise quelles apps il ne supporte plus.
   Celui qui confesse ses limites mérite plus de confiance
   que celui qui promet l'infini.

5. L'installation sort-elle de la maison ?
   L'index se lit dans le README du projet,
   jamais dans un post de tiers. Ni dans celui-ci.
```

## ❓ Questions fréquentes

**Quel entrepôt utiliser avec Mihon ?**
Keiyoushi : son propre site le déclare (Mihon, TachiyomiSY, Komikku). Si ta liste sort vide avec « Outdated app », le problème est la version de ton app.

**Et pour l'anime ?**
Yūzōnō anime-extensions est le canal vivant de référence ; l'officiel d'Aniyomi a archivé en août 2024 et Kohi-den en mai 2026.

**Les étagères « cursed » sont-elles dangereuses ?**
Leur risque n'est pas dans le mécanisme mais dans le contenu et ta juridiction. Elles se nomment pour compléter la carte ; l'index d'installation ne se colle pas dans cette famille de guides, pour aucune.

**Les extensions de Keiyoushi servent-elles dans Usagi ou Kotatsu ?**
Non : autre arbre, autre protocole de parsers. Ceux-là vivent dans leurs propres maisons et ont leur propre guide.

**Un entrepôt « approved » dans Miyomi est-il fiable ?**
Il est catalogué, pas audité. La différence est exactement celle du téléphone dans le guide de contact : il est dans la liste, il n'a pas passé l'examen.

**Tous les combien je révise que mon entrepôt reste vivant ?**
Chaque fois que quelque chose cesse de s'actualiser. Pour ça ce guide note seulement le vivant — et chaque lien se rouvre le jour où on l'utilise.

**Où je signale une extension cassée ?**
Dans le dépôt du code de l'extension (pour Keiyoushi : extensions-source), avec version d'app, source et pas. Les mainteneurs répondent mieux à des pas qu'à des plaintes.

## 🔗 Liens

- Keiyoushi : https://github.com/keiyoushi/extensions · https://github.com/keiyoushi/extensions-source · https://keiyoushi.github.io
- Yūzōnō : https://github.com/yuzono/tachiyomi-extensions · https://github.com/yuzono/anime-extensions · https://github.com/yuzono/cursed-manga-extensions · https://yuzono.github.io
- Entrepôts : https://github.com/cuong-tran/manga-repo · https://github.com/mojuru/cursed-manga-repo
- Écosystème chinois : https://github.com/LittleSurvival/copymanga-copy20 · https://github.com/ZGQ-inc/source
- Serveur de bureau : https://github.com/Suwayomi/tachiyomi-extension
- Miyomi : https://miyomi.app · https://github.com/miyomiorg/Miyomi

> La Bandita rapporte à partir de sources datées. La carte va avec le vivant.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : 7 entrepôts re-comptés à AUJOURD'HUI (Keiyoushi ★14 980, Yūzōnō ★432, manga-repo ★445). Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
