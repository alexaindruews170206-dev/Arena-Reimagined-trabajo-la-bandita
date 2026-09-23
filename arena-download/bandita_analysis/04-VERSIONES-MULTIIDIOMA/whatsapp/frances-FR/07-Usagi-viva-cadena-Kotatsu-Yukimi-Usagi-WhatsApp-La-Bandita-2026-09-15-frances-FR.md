# Publicación 07 — Usagi est vivante : la chaîne Kotatsu → Yukimi → Usagi et les quatre vivants de l'arbre

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 07)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🧬 La chaîne complète : Kotatsu → Yukimi → Usagi
├── 🏗️ Ce qui fut bien archivé (et ce ne fut pas l'app)
├── 📱 Fiche : UsagiApp/Usagi
├── 🌳 Les quatre vivants de l'arbre Kotatsu
├── 🧩 Plugins et parsers : comment mange cet arbre
├── 🍴 Les forks de Usagi
├── 🎭 Les imposteurs de la semaine
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Ça court dans les groupes : « Usagi fut archivée », « Usagi est morte ». On a vérifié le 14 septembre, dans la maison même du projet (re-vérifié au 15-sep : elle reste vivante) :

```
UsagiApp/Usagi — ce qu'on a vu aujourd'hui
✓ Sans bannière d'archivage sur la page du dépôt
✓ Push vérifié le 14-sep
✓ README vivant : « lecteur de mangas libre pour Android,
  inspiré de Kotatsu »
✓ Fiche active sur F-Droid : org.draken.usagi
✓ Organisation avec 16 dépôts
✓ Unique version stable : 1.0 (avec rc2 et rc1 derrière)
```

**Usagi est vivante.** Ce qui est mort fut autre chose — et de là vient la confusion : l'organisation a bien archivé sa vieille couche de plugins (deux dépôts concrets), et la prédécesseuse de Usagi, nommée Yukimi, fut bien décontinuée par son propre développeur. Cette histoire complète va plus bas, avec dates.

## 🧬 La chaîne complète : Kotatsu → Yukimi → Usagi

L'arbre Kotatsu a une généalogie de trois actes. La première partie est vérifiée sur GitHub ; la transition du milieu vient des reportages de la communauté (fils de novembre 2025 et de début 2026) :

```
ACTE 1 — Kotatsu
KotatsuApp/Kotatsu · ★8 855
ARCHIVÉ le 4 novembre 2025 (confirmé le 14-sep)
L'original ferme après la pression légale de Kakao
Entertainment et, selon ses propres auteurs, aussi
à cause de la politique de vérification de développeurs
qui venait. Dernière version : 9.4.1.

ACTE 2 — Yukimi (reportages de la communauté)
Les mêmes développeurs annoncent une successeuse :
Yukimi. Semaines après, son auteur la décontinue
et retire son site. Les fils de l'époque la donnent
pour terminée — « the project ended today ».
Il ne resta aucun dépôt vivant à vérifier ce jour-là : c'est pourquoi
ce guide la compte comme histoire racontée,
pas comme fiche.

ACTE 3 — Usagi
La communauté continue par un autre chemin : Usagi,
avec le même esprit Kotatsu mais avec une décision
de design clé : elle N'apporte PAS de sources intégrées.
Les sources, c'est l'utilisateur qui les apporte. Cette décision
est, probablement, la raison pour laquelle Usagi
reste vivante où d'autres moururent.
```

Les reportages de l'époque nommaient aussi Kotatsu-Redo, Kototoro et Futon comme les survivants de l'arbre. Les quatre vivent — fiches plus bas, tous ouverts aujourd'hui.

## 🏗️ Ce qui fut bien archivé (et ce ne fut pas l'app)

L'organisation UsagiApp a 16 dépôts, ouverts aujourd'hui. Deux sont archivés — et ils sont la vraie source de la rumeur :

```
ARCHIVÉS (l'architecture vieille)
UsagiApp/core-parsers   « librairie pour le dépôt de plugins »
UsagiApp/core-exts      « noyau pour charger des plugins externes »

VIVANTS (ce qui les remplace)
UsagiApp/TsukiMix       le noyau neuf pour lire et compiler
                        extensions et parsers
UsagiApp/plugins        plugins et exemple pour créateurs
UsagiApp/syncserver     serveur de synchronisation de données
                        « pour Kotatsu / Usagi »
UsagiApp/Tsuki          la librairie partagée de l'écosystème
```

C'est le geste de toute maison vivante : démolir l'échafaudage vieux pendant que le bâtiment reste ouvert. Qui passa par l'organisation et vit deux « archived » sans lire les noms emporta la rumeur. Les noms disent autre chose : fut archivée la couche de plugins ancienne — l'app ne l'a même pas remarqué dehors.

## 📱 Fiche : UsagiApp/Usagi

https://github.com/UsagiApp/Usagi

```
Ce que c'est :  lecteur de mangas libre pour Android,
                inspiré de Kotatsu, SANS sources intégrées
Licence :       GPL-3.0
Version :       1.0 (la seule stable ; rc2 le 2-sep,
                rc1 le 9-aoû)
Étoiles :       257 · push du 14-sep (jour de la vérification ; release 1.0 du 10-sep)
Android :       5.0 en avant (badges du README)
Maison :        github.com/UsagiApp/Usagi
Canaux :        GitHub, F-Droid (org.draken.usagi),
                Obtainium et OpenAPK selon son README
```

Sa page de F-Droid charge aujourd'hui — l'app y est publiée, avec son paquet org.draken.usagi. Le Discord et le Telegram que le README exhibe ne se lient pas ici : cette famille n'utilise ni ne recommande de canaux d'envoi, et les liens de communauté, c'est le projet propre qui les a.

Un « 1.0 » est un nombre de naissance, pas de maturité. L'app a release, README, maison et communauté petite mais vivante. Ce qui n'a pas été audité : combien son auteur répond aux reportes — ouvre une paire de fils d'issues avant de te fier ta bibliothèque, comme avec tout projet jeune.

## 🌳 Les quatre vivants de l'arbre Kotatsu

### Kotatsu-Redo — celui qui hérita le nom

https://github.com/Kotatsu-Redo/Kotatsu-Redo

★867 · version **9.8.3 (6 septembre)** · GPL-3.0 · vivant. Le fork communautaire que la communauté nomme d'abord depuis que l'original archiva. Son organisation soutient quatre dépôts : l'app, ses parsers (kotatsu-parsers-redo), un serveur de télémétrie et un autre de synchronisation. Il porte le nom « Kotatsu » en avant avec des versions de la série 9.8.x.

### Futon — celui au moteur propre

https://github.com/AppFuton/Futon

★427 · version **9.8.1 (16 août)** · GPL-3.0 · vivant. Son organisation a huit dépôts, parmi eux sa propre librairie de parsers (AppFuton/futon-parsers, archivée — gelée pendant que l'app avance ; signal à surveiller) et jusqu'à sa landing page. Curiosité de l'arbre : les nombres de version de Futon et Kotatsu-Redo se ressemblent — tous deux héritèrent la numérotation de l'original.

Et un avis de détour : existe MikuX-Dev/Futon (3 étoiles, autre chose avec le même nom). La fiche valide est AppFuton.

### Kototoro — celui qui voulut tout ensemble

https://github.com/Kototoro-app/Kototoro

★569 · **v2.1.2 publiée le 14-sep — et le 15 se leva avec la v2.1.3** (Publicación 02) · Apache-2.0 en sa licence déclarée. Mangas, romans et vidéo dans une seule app — la plus movida de l'arbre cette semaine (trois versions en quatre jours). Elle a son guide complet propre dans cette famille.

### Usagi — celle qui n'apporte pas de sources

La fiche d'en haut. Sa différence de design avec les trois autres est sa lettre d'identité : sans sources intégrées, l'utilisateur apporte les siennes via plugins.

## 🧩 Plugins et parsers : comment mange cet arbre

L'arbre Kotatsu n'utilise pas d'extensions type Mihon : il utilise des librairies de parsers et des plugins compilés. Les pièces du jour :

**Gekkoushi/plugin** — https://github.com/Gekkoushi/plugin — les artefacts prêts pour Usagi et les apps à structure Tsuki. Son README (re-vérifié aujourd'hui) dit : « Only for the Usagi App », « No updates, 1.3k sources » — mille trois cents sources compilées gelées en leur état actuel — et le plugin UMA « seulement pour la version 1.0 ». Cette dernière condition encaisse avec la réalité d'aujourd'hui : la seule stable de Usagi est la 1.0.

**Gekkoushi/plugin-source** — https://github.com/Gekkoushi/plugin-source — ★90, GPL-3.0, push du 13-sep, version 1.2.6. Ici on contribue et ici on signale les sources cassées.

**InvalidDavid/UMA** — https://github.com/InvalidDavid/UMA — ★69, GPL-3.0, tags du 12 et du 13 septembre. Installation automatique ou manuelle de plugins pour Usagi et d'autres forks de Kotatsu.

**Tsuki et TsukiMix** — les librairies partagées de l'organisation même : Tsuki (celle de l'ère plugins) et TsukiMix (l'évolution actuelle). Avec syncserver, l'organisation couvre tout le sandwich : app, couche de charge, parsers et synchronisation.

La règle de toujours sur les téléchargements : les artefacts se nomment, ne se collent pas. Le clic d'installation, chacun le donne dans la maison du projet, le jour où il s'en sert.

## 🍴 Les forks de Usagi

La liste publique des forks montre aujourd'hui 30 dans sa première page, avec activité majoritairement récente — et aucun avec projet propre. Un fork sans identité est une copie de sécurité avec date : il existe, il ne se passe rien. Si l'un grandit, il aura fiche le jour où il la méritera.

## 🎭 Les imposteurs de la semaine

La recherche de cette semaine apporta une portée au même costume — étoiles gonflées et identiques (115–120 mil), naissance le 13-sep, titres de classement : « usagi-nightly », « usagi-sora-vn-sources », « komikku-scans », « translation-hub-stringsets ». Aucun n'est fork de Usagi ni source vérifiée : ce sont des aimants à clics au nom prêté.

```
Le costume de l'imposteur
★ identiques entre plusieurs dépôts
Titre d'annonce, pas de projet
Sans historique : nés cette semaine
Hâte que tu lies « avant qu'ils l'effacent »
```

Si « le nouveau fork de Usagi » qu'on t'a passé finit dans l'un de ceux-ci, c'est exactement là qu'entre le malware. La maison de Usagi est une et a propriétaire : UsagiApp.

## ❓ Questions fréquentes

**Usagi est-elle morte ?**
Non. Push d'aujourd'hui, organisation active, F-Droid publiée. Ce qui fut archivé, c'est la vieille couche de plugins ; ce qui fut décontinué, c'est Yukimi, sa prédécesseuse. Chaque chose avec sa date en haut.

**Quel est « le nouveau fork » alors ?**
De l'arbre Kotatsu vivent aujourd'hui quatre : Kotatsu-Redo, Futon, Kototoro et Usagi. Il n'y a pas de successeur de Usagi parce qu'il n'en a pas fallu.

**Usagi ou Kotatsu-Redo ?**
Designs distincts : Usagi sans sources intégrées (tu les apportes, toi) ; Kotatsu-Redo hérite le modèle de l'original. Celle qui couvre ton usage, avec le dépôt que tu ouvres ce jour-là.

**Futon et Kotatsu-Redo sont-ils les mêmes par les nombres de version ?**
Ils partagent l'héritage de numérotation, pas le dépôt. Fiches séparées, maisons séparées.

**Où sont les sources de Usagi ?**
Dans la couche de plugins : Gekkoushi/plugin (artefacts), plugin-source (code), UMA (installateur). Sans recettes collées ici — la maison du projet les explique.

**Je peux lui mettre des extensions de Mihon ?**
Non : autre arbre, autre protocole. Les arbres ne se greffent pas par déssoin.

**Et si on me passe un APK « Usagi Plus » ?**
S'il ne sort pas de UsagiApp ou de F-Droid (org.draken.usagi), c'est une enseigne. Les imposteurs de la semaine sont la raison pour laquelle cette règle existe.

**Pourquoi F-Droid importe tant ici ?**
Parce que sa publication passa par le processus de la boutique : paquet identifié, compilation vérifiable. C'est la différence entre « télécharge-le de ce lien » et « il est dans une maison avec processus ».

## 🔗 Liens

- Usagi : https://github.com/UsagiApp/Usagi · F-Droid : https://f-droid.org/en/packages/org.draken.usagi/
- Organisation : https://github.com/orgs/UsagiApp/repositories
- Plugins : https://github.com/Gekkoushi/plugin · https://github.com/Gekkoushi/plugin-source · https://github.com/InvalidDavid/UMA
- Kotatsu-Redo : https://github.com/Kotatsu-Redo/Kotatsu-Redo
- Futon : https://github.com/AppFuton/Futon
- Kotatsu original (archivé) : https://github.com/KotatsuApp/Kotatsu
- Kototoro : https://github.com/Kototoro-app/Kototoro

> La Bandita rapporte à partir de sources datées. L'app vit ; l'échafaudage vieux, non. Et la rumeur, tu vois, voyage plus vite que le changelog.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : Usagi ★257 vivante, Kotatsu ★8 855, Redo ★867, Futon ★427, Kototoro v2.1.3. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
