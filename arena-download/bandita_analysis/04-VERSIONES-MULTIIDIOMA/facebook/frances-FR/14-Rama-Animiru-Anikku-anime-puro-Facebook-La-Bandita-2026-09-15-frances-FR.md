# Publicación 14 — Branche anime pur : Animiru et Anikku — les clients qui se retirèrent le mangas de dessus

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 14)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🌳 L'arbre de cette branche
├── 🍥 Animiru — l'anime-only qui naquit d'Aniyomi
├── 📺 Anikku — l'anime de l'organisation Komikku
├── 🌲 Le réseau de forks des deux (révisé le 14-sep)
├── 🧩 Les extensions de ces clients (nouveauté du jour)
├── ⚖️ Anime pur ou anime+mangas : comment décider
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Il y a une branche de l'arbre anime qui prit la décision contraire à celle d'Aniyomi : au lieu d'ajouter le mangas au lecteur, on lui RETIRA le mangas pour rester seulement avec l'anime. Ce guide ouvrit le 14 septembre les maisons de cette branche :

```
Animiru   ★864    v0.20.0.1 (14-sep)   fork anime-only d'Aniyomi
Anikku    ★1 028  v0.2.0 (11-sep)           anime de l'organisation Komikku
```

Donnée du jour : **Animiru publia deux versions cette même matinée** (0.20.0.0 et 0.20.0.1). Et sur le front Anikku, il y a des entrepôts d'extensions dédiés à lui avec activité du jour. La branche petite de l'arbre est, cette semaine, celle qui bougea le plus.

## 🌳 L'arbre de cette branche

```
Aniyomi (mangas + anime)
   └── Animiru      il retira le mangas : SEULEMENT anime
         └── AnimiruTv  variante pour Android TV

Komikku (mangas, avec organisation)
   └── Anikku       son client d'anime
         └── anikku-preview   le canal d'essais
```

Deux chemins distincts vers la même destination : un client d'anime libre. Animiru sortit de la branche Aniyomi ; Anikku sortit de l'organisation Komikku. Ils ne sont pas compétition directe par naissance — ce sont deux familles arrivées au même comptoir.

## 🍥 Animiru — l'anime-only qui naquit d'Aniyomi

https://github.com/Quickdesh/Animiru

```
Ce que c'est :  fork d'Aniyomi qui élimine la partie
                de mangas pour être une app SEULEMENT d'anime
Licence :       Apache-2.0
Versions :      0.20.0.1 et 0.20.0.0 — publiées le 14-sep
                (la précédente : 0.19.8.1, du 9-aoû)
Android :       8.0+ (sa fiche de téléchargement)
Lecteur :       construit sur mpv, configurable
Trackers :      MyAnimeList, AniList, Kitsu, Shikimori,
                Simkl, Bangumi et Hikka (son README)
Étoiles :       862
```

Trois choses font d'Animiru un spécial dans l'arbre :

**Un : le registre officiel.** Animiru figure listé dans la page de forks que maintient l'organisation même d'Aniyomi (aniyomi.org/forks/Animiru). Ce n'est pas un clone apparu de nulle part : c'est un fork enregistré dans l'index du projet mère — la différence entre la maison reconnue et la cabane sans propriétaire.

**Deux : la décision de design.** On lui retira le mangas à dessein. Moins d'app, moins de poids, un seul travail bien fait. Pour qui ne lit jamais de mangas, c'est exactement l'outil correct — et pour qui lit les deux, c'est la moitié d'une solution.

**Trois : le rythme du jour.** Deux versions publiées la même matinée d'aujourd'hui. Quoi que ce soit que son auteur est en train d'ajuster, il le fait en ce moment même — le dépôt se sent vivant depuis la couverture.

Sa lignée a sa ramette propre : existe AnimiruTv (fork pour Android TV) et des copies mineures sans activité. La fiche canonique est Quickdesh/Animiru — celui qui maintient le rythme et le registre.

## 📺 Anikku — l'anime de l'organisation Komikku

https://github.com/komikku-app/anikku

```
Ce que c'est :  « Free and open source anime watcher
                for Android » — le client d'anime de
                l'organisation qui maintient Komikku
Licence :       Apache-2.0
Version :       0.2.0 (11 septembre 2026)
Push :          14-sep (jour de la vérification)
Canal d'essais : anikku-preview (★112, push 10-sep)
Étoiles :       1.028 — la plus grande de cette branche
```

Anikku est le pari institutionnel : ce n'est pas un projet d'une personne, c'est la pièce d'anime d'une organisation qui démontre déjà du métier avec Komikku (un des lecteurs mangas plus actifs de l'écosystème, ★4 717). Sa version 0.2.0 de cette semaine le met dans la phase jeune mais sponsorée : il y a une org derrière, il y a canal de previews, il y a des traductions communautaires.

Le nom, attention au ressemblance : existe une famille entière de clients à racine « Ani- » (Aniyomi, Animetail, Animiru, Anikku, et le rebaptisé AniZen, qui a son propre guide). Chacun avec son dépôt et son propriétaire. Le nom n'hérite rien ; le dépôt, lui, explique tout.

## 🌲 Le réseau de forks des deux (révisé le 14-sep)

Le vivant et avec proposition dans les deux réseaux (révisé le 14-sep, fork par fork) :

- **AnimiruTv** reste la variante canonique pour Android TV.
- **Vidi** est la seule variante d'Animiru avec builds propres et frais : v0.19.12, du 4 septembre.
- Dans le réseau d'anikku : le **port vers macOS** reste en chantier (push d'août) et **anikku-pineapple** tisse avec Houri dans la branche mangas — le même auteur dans les deux branches de la maison Komikku (voir le guide SY/Komikku).

Le reste des deux réseaux (32 et 68 forks) sont des copies sans fonctions propres déclarées : elles ne se notent pas. La carte est de ce qui vit et apporte — et le jour où quelqu'un apporte, il entrera avec date.

## 🧩 Les extensions de ces clients (nouveauté du jour)

Un client d'anime sans sources ne fait rien — et cette semaine la branche inaugura ses propres entrepôts. Vérifiés aujourd'hui :

```
salmanbappi/extensions-repo      ★40 · push d'AUJOURD'HUI (re-vérifié 15-sep)
   « Répositoire d'extensions d'anime
   dédié à Anikku » — selon sa description

salmanbappi/aniyomi-extensions   ★15 · push 12-jan
   « Extensions pour Anikku / Aniyomi & forks »
```

Le détail qui connecte des guides : l'auteur de ces entrepôts est le même développeur d'AniZen — le rebrand d'Anikku Mod qui a son propre guide dans cette collection. Il y a un écosystème petit en train de se construire autour du client de l'organisation Komikku : client, canal de previews, et entrepôts d'extensions. Ça, en maillots, c'est comment naît une branche sérieuse.

Le contexte historique, avec date : l'entrepôt officiel d'anime d'Aniyomi archiva en août 2024 et le communautaire (Kohi-den) en mai 2026 — ce que ces dépôts neufs existent est la réponse de l'écosystème à ces creux. Les index d'installation ne se collent pas ici : ils se lisent dans le README de chaque entrepôt, le jour où on s'en sert.

## ⚖️ Anime pur ou anime+mangas : comment décider

```
Tu vois de l'anime et tu NE touches JAMAIS le mangas ?
   → Animiru ou Anikku : l'app pèse moins,
     l'interface ne t'encombre pas avec la moitié
     que tu n'utilises pas.

Tu vois de l'anime et tu lis des mangas, à humeurs distinctes ?
   → La branche précédente (Aniyomi/Animetail/Tadami) :
     les deux choses en une main.

Anime à la télé ?
   → AnimiruTv existe — avec l'avertissement de
     toujours : fork petit, vérifie-le le jour
     où tu l'essaies.

Tu utilises déjà Komikku pour le mangas ?
   → Anikku a la logique de la même équipe :
     la famille se sent dans l'interface.
```

Les deux fiches du jour passent les portes de la maison : usage réel (communautés actives), unicité (l'anime pur est sa niche), maturité (releases de cette semaine, structure d'org dans un cas) et dessein propre (retirer le mangas EST le dessein — ce n'est pas cosmétique).

## ❓ Questions fréquentes

**Animiru est « Aniyomi sans mangas » rien que ça ?**
Sa base est Aniyomi et sa différence est ça — mais il additionne des détails propres (le set de trackers inclut Simkl et Hikka, le lecteur mpv va affiné à chaque version). Deux versions en une matinée disent que le « rien que ça » est en train d'être travaillé.

**Pourquoi Anikku va par 0.2 si Komikku va par 1.14 ?**
Ce sont des apps distinctes : le mangas porte des années d'avance. 0.2 avec organisation derrière est une phase normale d'un projet jeune — le canal de previews et les traductions sont signaux de structure, pas de jouet.

**Anikku et AniZen sont les mêmes ?**
Famille, pas jumeaux : AniZen se déclare rebrand de « Anikku Mod » (son guide le compte avec dates). Anikku est l'original de l'organisation. Même lignée déclarée, maisons distinctes.

**Quelle extension va à Animiru ?**
Celles de l'écosystème d'Aniyomi — c'est son héritage — avec la carte vivante du guide précédent. Pour Anikku, ses entrepôts dédiés d'en haut. Dans les deux cas : l'index se lit dans la maison de l'entrepôt, pas dans un post.

**Ont-ils version pour TV ou bureau ?**
AnimiruTv (TV, fork petit). Anikku : on ne lui connaît pas de variantes — son org se concentre sur le mobile. Ce qui existera demain, ses organisations le diront.

**Laquelle des deux fiches va plus vite ?**
Animiru, sans discussion : deux releases aujourd'hui. Mais la vitesse n'est pas le critère — le dépôt vivant oui, et les deux vivent.

## 🔗 Liens

- Animiru : https://github.com/Quickdesh/Animiru · registre de forks d'Aniyomi : https://aniyomi.org/forks/Animiru/
- AnimiruTv : https://github.com/Znabil/AnimiruTv
- Anikku : https://github.com/komikku-app/anikku · essais : https://github.com/komikku-app/anikku-preview
- Entrepôts neufs : https://github.com/salmanbappi/extensions-repo · https://github.com/salmanbappi/aniyomi-extensions
- Guide croisé : branche Aniyomi/Animetail (pièce 13) · AniZen (pièce 11) de cette collection

> La Bandita rapporte à partir de sources datées. Retirer le mangas est aussi un dessein — et cette semaine il le publia deux fois.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : Animiru ★864, extensions-repo push d'AUJOURD'HUI. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
