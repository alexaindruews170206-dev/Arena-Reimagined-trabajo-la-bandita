# Publicación 12 — FMHY est un wiki de pistes, pas un catalogue : discovery ≠ vérification

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 12)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🌐 Ce qu'est FMHY et comment ça marche
├── 🧩 Ce que sa navigation révèle aujourd'hui
├── 🔒 L'interstitiel Base64 (ce que c'est et ce que ce n'est pas)
├── 📦 Le dépôt derrière le wiki
├── 🧭 Discovery ≠ vérification : l'entonnoir complet
├── 🔬 Un exemple réel, de bout en bout
├── 📌 La correction à la « grande vague » d'avril
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

FMHY — « freemediaheckyeah » — se présente comme « la plus grande collection de choses gratis d'internet ». C'est un wiki communautaire énorme, vivant aujourd'hui, et avec un rôle précis dans la carte de la connaissance : **c'est un découvreur de premier niveau et un vérificateur de rien.**

La différence importe parce qu'avril le démontra avec du dégât : quelqu'un vida une portion du wiki dans un fil de 340 mil caractères et le vendit comme catalogue vérifié. Il ne l'était pas. Chaque piste de FMHY est un premier maillon — ouvrir la maison du projet, lire sa licence, comprober sa version et son propriétaire est le travail que personne ne peut faire pour toi, ni ce wiki ni ce guide.

État d'aujourd'hui, 14 septembre : le site répond avec son post mensuel de septembre actif, son guide de débutants charge, et le dépôt qui le génère cumule ★14 592 — avec la particularité que son code git ne pousse pas depuis mai, et le wiki n'en est pas pour ça mort. Les deux choses, comptées plus bas.

## 🌐 Ce qu'est FMHY et comment ça marche

https://fmhy.net

FMHY est un wiki maintenu par sa communauté : des milliers d'entrées d'outils, de sites et de ressources organisés par catégories — privacy, AI, video, audio, gaming, reading, downloading, torrenting, educational, mobile, linux-macos, non-english, misc, parmi d'autres. Sa mécanique :

- La communauté propose et cure des entrées continûment.
- Un changelog enregistre ce qui changea — et son rythme est visible : le wiki publie **des posts mensuels de nouveautés** (celui de septembre 2026 est en ligne aujourd'hui).
- Il y a variante SFW (sans contenu adulte) pour qui la préfère.
- La culture du projet est celle d'un index : décrire, lier, ne pas garantir.

Sa taille est sa vertu et sa limite : il couvre tout, il n'audite rien. C'est la bibliothèque plus grande du monde en son genre — et comme toute bibliothèque grande, la valeur n'est pas de la posséder entière : elle est de savoir utiliser le catalogue.

## 🧩 Ce que sa navigation révèle aujourd'hui

La barre du site, ouverte aujourd'hui, est une leçon de ce que le wiki pense de lui-même :

```
📑 Changelog    ce qui changea et quand
📖 Glossary     le dictionnaire de ses termes
💾 Backups      comment obtenir le wiki entier
🌱 Ecosystem    les variantes et projets germains
❓ FAQs         les questions du projet
✅ SafeGuard    son chapitre de sécurité
🚀 Startpage    sa proposition de page de départ
🔎 SearXNG      recherche propre
😇 SFW FMHY     la version sans adulte
🏠 Selfhosting  comment tu la montes dans ton serveur
```

Remarque ce que cette barre dit sans le dire : un projet qui publie son changelog, maintient un glossaire, offre des backups de lui-même et a un chapitre de sécurité se prend au sérieux comme infrastructure. Il reste un index de pistes — mais des organisées.

## 🔒 L'interstitiel Base64 (ce que c'est et ce que ce n'est pas)

En entrant, FMHY montre parfois un avis sur des liens codés en Base64. Ce qu'il y a derrière, sans détours :

```
C'est :    une mesure de design. Quelques liens du
           wiki se publient codés pour que les
           traqueurs automatiques ne les indexent pas.
           Le site même offre un décodeur en page.

Ce n'est pas : un système de sécurité, ni un rite obligatoire,
           ni une instruction de ce guide. L'utilisateur
           décide s'il utilise cette voie ; le décodeur est
           du site et tourne dans ton navigateur.

Et ce n'est pas : motif pour copier des liens codés dans
           un post. Ici vont des liens en clair ou ne vont pas.
```

Le wiki fait son ingénierie pour survivre aux indexeurs ; cette famille de guides fait la sienne pour ne pas coller de recettes. Chacun protège le sien.

## 📦 Le dépôt derrière le wiki

https://github.com/fmhy/FMHY

★14 592 · dernier push du 13 mai 2026 · licence : sans classification sur sa page (dit tel quel — le wiki définit sa propre politique de contenu sur son site).

La curiosité qui enseigne quelque chose : le git porte des mois tranquille et le wiki est vivant — re-vérifié AUJOURD'HUI, 15-sep : il charge avec son post de septembre. Comment ? Le wiki se sert par voies propres (sa web et ses déploiements) et le dépôt public ne reflète pas chaque mouvement. La leçon générale que tu as déjà vue dans cette famille : **git tranquille ≠ projet mort ; projet vivant ≠ tout vérifié.** Un dépôt est une couche, pas le projet entier.

## 🧭 Discovery ≠ vérification : l'entonnoir complet

La règle de la maison tient en une ligne — trouver n'est pas vérifier. Déployé, l'entonnoir qui convertit une piste en quelque chose de citable :

```
1. DÉCOUVERTE
   FMHY (ou un groupe, ou un ami) dit :
   « cette app est bonne ».
   ── ça vaut exactement zéro comme vérification.

2. OUVERTURE
   S'ouvre la maison du projet — son dépôt ou site —
   CE JOUR-LÀ. Pas le découpé du groupe : la maison.

3. LECTURE
   Qui est le propriétaire ? Depuis quand existe-t-il ?
   Quelle licence déclare-t-il ? Quand fut sa dernière
   version et son dernier push ? Est-il archivé ?

4. CONTRASTE
   D'autres sources indépendantes le nomment-elles ?
   Sa communauté répond-elle aux issues ?
   Sa signature/checksums sont-ils publics ?

5. USAGE RÉEL
   Quelqu'un de chair et d'os l'utilise-t-il et peut
   raconter comment ça lui va ? L'usage réel est la
   dernière porte — et la seule que personne ne peut
   ouvrir pour toi.

6. FICHE
   Seulement alors : une fiche avec date, dans un
   guide comme celui-ci. Et avec date de péremption.
```

N'importe quel raccourci qui saute des pas — « il est dans FMHY, point », « ils le recommandent sur Telegram, point » — est le geste exact qui fit du fil d'avril un encombrant de 340 mil caractères.

## 🔬 Un exemple réel, de bout en bout

Pour que l'entonnoir ne reste en théorie, le parcours que cette famille fit déjà avec une entrée réelle :

```
1. Le wiki (et la moitié d'internet) mentionne « Mihon »
   comme lecteur de mangas.

2. S'ouvre la maison : github.com/mihonapp/mihon

3. On lit : 23.575 étoiles · Apache-2.0 ·
   version 0.20.4 d'août · push d'AUJOURD'HUI ·
   organisation mihonapp avec historique depuis 2024.

4. On contraste : Keiyoushi (l'entrepôt de
   extensions) le liste premier parmi les apps
   supportées ; ses issues ont de l'activité ; la
   communauté de l'écosystème le nomme comme le
   successeur de fait de Tachiyomi.

5. Usage réel : la gente de la bande qui l'utilise,
   avec son opinion.

6. Fiche : aujourd'hui Mihon a guide propre dedans
   cette famille (celle des forks de lecteurs), avec sa
   date de coupe.
```

Six pas. Tout ce qu'il faut pour que « Mihon » passe de piste à information. Et tout ce que NE passa pas le jour où quelqu'un colla un wiki entier dans un fil.

## 📌 La correction à la « grande vague » d'avril

```
Ce que fit avril                  Ce que fait cette famille
Vider FMHY dans un post           Ouvrir la maison de chaque piste
Vendre le wiki comme vérification Présenter le wiki comme découverte
340 mil caractères sans propriétaire  Fiches courtes, datées, avec maison
Index d'installation collés       L'index se lit dans la maison du
                                  projet, jamais dans un post
« Tout gratis, tout sûr »         Chaque fiche avec sa limite et sa date
```

Le wiki n'était pas le problème. Le problème était le geste : présenter l'accumulation comme vérification. Ce geste est ce pour quoi cette famille de guides existe : ne pas le répéter.

## ❓ Questions fréquentes

**Je peux utiliser FMHY ?**
Tu peux le lire : c'est public et son rôle comme index est légitime. Ce que ce guide ne fait pas, c'est t'envoyer vers ses destinations ni le vider ici. Chaque clic dedans est une découverte — la vérification va à part, avec l'entonnoir d'en haut.

**Est-il plus sûr que googler ?**
On ne l'affirme pas. C'est une autre liste, curée par d'autres gens, avec d'autres incitatifs. Les moteurs t'envoient vers des annonces payées ; les wikis, vers ce que la communauté nota. Aucune des deux portes ne vérifie pour toi.

**Sa section Android remplace-t-elle le guide de boutiques de cette famille ?**
Non. Le guide de boutiques ouvrit chaque projet le jour de la coupe ; une section de wiki est une liste avec une autre date et un autre critère.

**Et sa section de musique ?**
Même réponse : la famille a guide de musique avec les fiches vérifiées. Le wiki peut pointer vers la même chose — ou vers des choses que personne n'ouvrit encore.

**Le dépôt dit mai mais le wiki est vivant, laquelle est la vérité ?**
Les deux : le wiki se sert par déploiements propres et le dépôt ne reflète pas chaque changement. Git tranquille n'est pas projet mort — la leçon du dépôt le disait déjà.

**Base64 est de la piraterie ?**
C'est de l'encodage de texte — la même technique que ton téléphone utilise pour envoyer des images par courriel. L'usage que chacun en donne aux liens est son affaire et sa loi. Ici on ne décode rien pour personne.

**Alors à quoi sert FMHY, à la fin ?**
À ce que dit sa définition : l'index plus grand de l'écosystème. Comme carte de ce QUI EXISTE, il n'a pas de rival. Comme preuve de ce qui marche et est sûr, il ne vaut rien — et il ne prétend pas le valoir.

## 🔗 Liens

- Le wiki : https://fmhy.net
- Guide de débutants : https://fmhy.net/beginners-guide
- Post de septembre : https://fmhy.net/posts/sept-2026
- Le dépôt : https://github.com/fmhy/FMHY

> La Bandita rapporte à partir de sources datées. Le wiki de pistes n'est pas un catalogue — et qui découvre, n'a pas encore vérifié.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : wiki re-vérifiée vivante à AUJOURD'HUI. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
