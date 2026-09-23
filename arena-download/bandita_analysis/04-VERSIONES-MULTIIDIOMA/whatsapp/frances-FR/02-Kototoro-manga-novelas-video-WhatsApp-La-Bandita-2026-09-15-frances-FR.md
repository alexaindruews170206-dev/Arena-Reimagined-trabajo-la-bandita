# Publicación 02 — Kototoro : mangas, romans et vidéo en une seule bibliothèque — v2.1.3 est sortie aujourd'hui (re-vérifiée 15-sep)

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 02)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── ℹ️ Ce qu'est Kototoro
├── 🧭 État du projet (vérifié aujourd'hui)
├── 📦 La version du jour : v2.1.3
├── 🏗️ Comment c'est construit
├── 🔌 Sources et extensions : ce qui se connecte
├── 📖 Romans et lecture par JSON
├── 🌳 Le voisinage : Mihon, Aniyomi, Komikku et Tadami
├── ♿ Confort de lecture et accessibilité
├── 🛠️ Résolution de problèmes
├── 🔒 Sécurité et chaîne d'approvisionnement
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Kototoro est une application Android open source qui réunit trois bibliothèques en une : mangas, romans et vidéo. Historique, favoris et synchronisation vivent dans un même flux, et par-dessus elle apporte la traduction par OCR dans le téléphone même, avec modèles téléchargeables.

La raison de cette édition : la version **v2.1.3** est sortie AUJOURD'HUI même, 15 septembre — un jour après la 2.1.2 — et voilà déjà quatre en cinq jours. Re-vérifié au matin du 15 : le projet s'est levé avec release neuve. Le projet bouge à un rythme presque quotidien, donc ce guide apporte les nombres d'aujourd'hui et t'apprend la seule horloge qui commande : sa page de versions.

L'idée en une image : une étagère à trois tiroirs où avant tu avais trois meubles séparés. Unifier épargne les sauts — et multiplie les dépendances. Ce guide regarde ce qu'elle joint et ce qu'elle te demande en échange.

## ℹ️ Ce qu'est Kototoro

https://github.com/Kototoro-app/Kototoro

Kototoro vient de la lignée des lecteurs type « source » : l'application n'apporte pas le contenu dedans, mais parle avec des sources que l'utilisateur ajoute. Sur cette base, elle y ajoute deux choses qui la distinguent : les romans (lecture longue par JSON, à la manière des lecteurs chinois de sources) et la vidéo, dans la même app.

```
Kototoro en une boîte
Dépôt :        github.com/Kototoro-app/Kototoro
Licence :      Apache-2.0
Paquet :       org.skepsun.kototoro
Android :      8.0 en avant (builds récents)
Docs :         kototoro-app.github.io/Kototoro
Origine :      lignée skepsun (kototoro-parsers)
Étoiles :      569 · activité : aujourd'hui même
```

Son site de documentation est vivant et a été lu aujourd'hui : il décrit le lecteur tout-en-un (mangas, romans, vidéo, historique, favoris et synchronisation), la traduction locale par OCR avec téléchargement de modèles, les flux de synchronisation et la référence d'intégration de sources.

## 🧭 État du projet (vérifié aujourd'hui)

L'API du dépôt, ouverte le 14 et rouverte AUJOURD'HUI, 15 septembre (re-vérification de déménagement) :

```
Étoiles :         569
Dernier push :    14-sep · release d'AUJOURD'HUI (15-sep) : v2.1.3
Branche de travail : devel (à la coupe du 13-sep : 8 branches,
                  196 tags, ~6 950 commits)
Versions :        v2.1.3 (AUJOURD'HUI, 15-sep) · v2.1.2 (14-sep) · v2.1.1 (13-sep) · v2.1.0 (11-sep)
Nightly :         dépôt Kototoro-Nightly, build N20260914 (14-sep)
```

Quatre versions en cinq jours. La Nightly — version d'essai quotidienne — est vivante elle aussi, avec build du 14-sep (dernière constatée à AUJOURD'HUI). Qu'est-ce que ça signifie pour toi ? Que n'importe quel nombre de ce guide (ou d'un autre) vieillit vite : la seule référence de version vigente est la page de versions du projet, ouverte le jour où tu installes.

## 📦 La version du jour : v2.1.3

Publiée AUJOURD'HUI, 15 septembre. Ses paquets, selon l'API (aucun n'a été téléchargé pour ce guide) :

```
arm64-v8a      125.446.780 octets    119 téléchargements à midi
armeabi-v7a    117.554.684 octets      5
universal      312.997.668 octets     14
x86            140.010.036 octets      1
x86_64         147.078.128 octets      2
```

Pour presque tous les téléphones modernes, l'archive correcte est l'arm64-v8a. L'universelle pèse plus du double parce qu'elle apporte tout — elle sert dans des cas spéciaux.

Les notes de la version (lues aujourd'hui) apportent du changement concret :

- Personnalisation du fond de couverture (artwork).
- Distance de défilement par touche de volume en lecture webtoon.
- Gestion et recherche améliorée des catégories dans les favoris.
- Réglages du lecteur sur écrans larges et récupération du défilement des marges à la reprise.

Ce qu'une version pareille NE prouve pas : que les épisodes anciens des sauvegardes (la série 1.4–1.7) soient fermés. Si tu viens avec une grande bibliothèque, la règle ne change pas : sauvegarde manuelle et essai à vide avant de migrer quoi que ce soit.

**Caches et miroirs vont avec retard.** La v2.1.3 est sortie il y a des heures : si une page te montre des versions de juillet ou la série 1.x, ce n'est pas de la fraude — c'est du retard. La seule référence vivante est Releases.

## 🏗️ Comment c'est construit

Kototoro hérite de l'architecture de sa lignée : l'application en Kotlin consommait une librairie de parsers propre — aujourd'hui indépendante — appelée kototoro-parsers (github.com/skepsun/kototoro-parsers, version 1.8, avec activité du 10 septembre). Cette séparation app/parsers est le patron de l'écosystème : la maison (app) et les rues (sources) se maintiennent séparément.

Dans l'app, chaque onglet (Manga / Romans / Vidéo) parle avec son type de source :

- Mangas : sources type lecteur (extensions compatibles avec l'écosystème Mihon).
- Romans : sources JSON à la manière Legado — livres de règles qui disent où est chaque chose.
- Vidéo : sources de streaming par JSON, profils type TVBox inclus.

Ce mélange est sa promesse et son risque : trois types de source, trois types de panne possible. La section de résolution de problèmes plus bas existe pour ça.

## 🔌 Sources et extensions : ce qui se connecte

Les extensions de mangas de Kototoro sont compatibles avec le format de l'écosystème Mihon. Les entrepôts de cet écosystème, avec leur état vérifié aujourd'hui :

```
Keiyoushi          ★14 980  push 14-sep      le hub principal
   https://github.com/keiyoushi/extensions
   (code : keiyoushi/extensions-source, ★4 678, vivant au 15-sep)
Yūzōnō anime       ★432     push 13-sep
   https://github.com/yuzono/anime-extensions
manga-repo         ★445     push 14-sep      pour Komikku/Mihon
   https://github.com/cuong-tran/manga-repo
Copymanga (CN)     ★2 753   v1.4.85 (8-sep)
   https://github.com/LittleSurvival/copymanga-copy20
```

La règle de cette famille de guides sur les entrepôts : on nomme le projet et sa page officielle ; la recette d'installation (l'index qui se colle dans l'app), chacun la lit dans le README du projet, le jour où il s'en sert. On ne la copie pas ici.

## 📖 Romans et lecture par JSON

Ici Kototoro parle la langue des lecteurs chinois de sources :

**Legado 3.0** — github.com/gedoor/legado — ★47 074, le géant du modèle « livre de sources » : chaque source est un JSON qui dit comment chercher, où est le texte et comment paginer.

**Yuedu (阅读)** — github.com/XIU2/Yuedu — ★12 268, collection communautaire de sources de lecture.

Kototoro importe ces flux JSON et y ajoute sa couche de traduction : OCR sur l'image, avec modèles téléchargeables qui tournent dans le téléphone, ou via API si tu préfères un service externe. Pour la vidéo, elle importe en plus des profils style TVBox — listes JSON qui pointent vers des médias, avec différents niveaux de complexité (liens directs, listes de lecture, CMS simples, et profils qui dépendent de JavaScript ou de composants distants, dans cet ordre d'essai).

## 🌳 Le voisinage : Mihon, Aniyomi, Komikku et Tadami

Kototoro n'est pas seule. Les lecteurs de l'écosystème libre, avec leurs nombres d'aujourd'hui :

```
Mihon        ★23 601  v0.20.4 (5-aoû)   push AUJOURD'HUI (15-sep)      mangas
Aniyomi      ★7 683   push 14-sep                       mangas+anime
Komikku      ★4 721   v1.14.1 (17-jui)  push 11-sep   mangas
Tadami       ★260     v0.62 (12-sep)    push 13-sep · vivante     mangas+anime+ranobe
Kototoro     ★569     v2.1.3 (AUJOURD'HUI) push AUJOURD'HUI      mangas+romans+vidéo
```

Mihon est le tronc de l'arbre mangas (le successeur de fait de Tachiyomi, fermé en 2024). Aniyomi et Tadami ajoutent l'anime. Komikku est le fork avec vie propre. Kototoro est la branche qui a voulu tout ensemble. Aucune n'est « la meilleure » en abstrait : la bonne est celle qui couvre ce que tu lis, avec dépôt vivant.

Et attention à la tentation de mélanger : les extensions d'un arbre ne servent pas dans l'autre. Kotatsu, Usagi et leurs parents utilisent des parsers propres (une autre famille de guides couvre cet arbre).

## ♿ Confort de lecture et accessibilité

Ce que l'app apporte d'usine pour l'œil et la main :

- Lecteurs par mode : page, continu et webtoon, avec réglage de défilement (maintenant aussi par volume, selon la v2.1.2 du 14-sep).
- OCR de traduction à deux niveaux (basique et avancé) avec modèles locaux téléchargeables — utile pour les mangas sans traduction officielle.
- Historique, favoris et catégories unifiés (la v2.1.2 du 14-sep a justement amélioré la gestion des catégories).
- Synchronisation du flux de lecture propre entre sessions.

Le conseil de toujours pour la vue : luminosité haute sur les pages à marges blancs, mode nuit pour le webtoon, et télécharger avant de lire en voyage — les trois lecteurs de l'écosystème le permettent.

## 🛠️ Résolution de problèmes

**Les sources n'apparaissent pas.**
Vérifie dans l'ordre : l'extension est-elle installée ? le dépôt a-t-il été ajouté et synchronisé ? es-tu dans le bon onglet (Manga / Romans / Vidéo) ? as-tu rafraîchi l'écran des extensions ? Le remède classique : réinstaller l'extension et rafraîchir.

**Un JSON de romans ne s'importe pas.**
D'abord : est-ce une source Legado ou un profil TVBox ? Ce sont des formats distincts qui s'importent par des menus distincts. Ensuite : le JSON est-il valide ? l'URL répond-elle ? Troisième : essaie d'abord en important depuis un fichier local — ça élimine la moitié des variables.

**Un profil TVBox s'importe mais ne charge pas.**
L'échelle d'essai, du simple au complexe : médias directs → listes de lecture → CMS simples → profils qui dépendent de JavaScript → profils avec composants distants. Un JSON peut importer parfaitement et quand même échouer parce qu'une dépendance externe a changé ou est morte. Ce n'est pas la faute de l'app.

**La traduction ne démarre pas.**
Liste courte : mode local ou API-seul selon ce que tu veux utiliser ; langues origine/destination correctes ; niveau d'OCR (basique/avancé) ; modèles effectivement téléchargés ; et si tu utilises l'API, endpoint, clé et modèle bien écrits. 80 % des cas, c'est un modèle jamais téléchargé.

**L'app consomme de l'espace.**
Elle est grande par design : parsers de trois médias + modèles d'OCR. Si le téléphone est juste, commence sans télécharger les modèles avancés et sans mode universel.

## 🔒 Sécurité et chaîne d'approvisionnement

Ce que le projet déclare : ses développeurs n'ont pas d'affiliation avec des fournisseurs de contenu et ne gouvernent pas de dépôts d'extensions — les sources, c'est l'utilisateur qui les met. L'app est un instrument ; le contenu est ta décision et ta responsabilité légale.

À la coupe de la semaine passée, le dépôt ne publiait ni politique de sécurité ni code de conduite (mais guide de contribution et licence, oui). Ça n'implique pas d'insécurité — mais dans une application qui charge des runtimes et des sources de tiers, c'est un signal à surveiller. Des builds concrets distribués par boutiques alternatives sont passés aux scans (ClamAV, APKiD, Quark-Engine) sans menaces : ça vaut pour cette archive exacte, pas pour la chaîne complète.

La règle de la maison : ne te fie pas à une source seulement parce qu'elle est dans une liste d'internet. Dépôt, commit, étiquette et signature se regardent avant d'installer. Et les étoiles n'installent rien.

## ❓ Questions fréquentes

**Quelle est la bonne version aujourd'hui ?**
Celle que dira Releases le jour où tu installes — aujourd'hui c'est la v2.1.2, publiée ce matin même. Demain ce peut être une autre ; trois releases en quatre jours disent tout.

**Je peux avoir mangas, romans et vidéo dans la même app ?**
Oui, c'est son point. Le prix : trois types de source avec trois types de panne. Sauvegarde séparée et patience avec l'échelle de diagnostic.

**Est-elle compatible avec les extensions de Mihon ?**
Le format des extensions de mangas, oui. Celles d'anime/romans ont leur propre chemin (JSON). Ce qui ne l'est pas : les sources de Kotatsu/Usagi sont un autre arbre, elles n'entrent pas.

**Je viens de la série 1.x, comment je migre ?**
Avec sauvegarde manuelle et essai à vide. L'épisode des sauvegardes 1.4–1.7 est documenté dans la communauté ; que la série 2.x aille vite ne prouve pas à elle seule que ce chapitre soit fermé.

**La traduction OCR a-t-elle besoin d'internet ?**
Le mode local non : il tourne dans le téléphone avec des modèles téléchargeables. Le mode API oui, et il dépend du service que toi tu configures.

**Et TVBox, qu'est-ce que c'est ?**
Des listes JSON qui pointent vers des médias vidéo. Importer est facile ; qu'elles chargent dépend de que les choses vers lesquelles elles pointent restent vivantes. Commence toujours par le simple de l'échelle.

**Combien ça pèse ?**
Le paquet arm64 de la v2.1.2 tourne autour de 125 Mo, et l'universel passe de 300 Mo. À cela ajoute les modèles d'OCR si tu les télécharges.

**Les 569 étoiles signifient-elles quelque chose ?**
Communauté petite mais en plein croissance, avec un rythme de développement que peu d'apps de la carte égalent aujourd'hui. Les étoiles n'installent pas : elles mesurent la renommée, pas la qualité.

## 🔗 Liens

- Dépôt : https://github.com/Kototoro-app/Kototoro
- Versions : https://github.com/Kototoro-app/Kototoro/releases
- Nightly : https://github.com/Kototoro-app/Kototoro-Nightly
- Documentation : https://kototoro-app.github.io/Kototoro/
- Parsers de l'origine : https://github.com/skepsun/kototoro-parsers
- Keiyoushi : https://github.com/keiyoushi/extensions · https://keiyoushi.github.io
- Yūzōnō anime : https://github.com/yuzono/anime-extensions
- manga-repo : https://github.com/cuong-tran/manga-repo
- Copymanga : https://github.com/LittleSurvival/copymanga-copy20
- Legado : https://github.com/gedoor/legado · Yuedu : https://github.com/XIU2/Yuedu
- Mihon : https://github.com/mihonapp/mihon · Aniyomi : https://github.com/aniyomiorg/aniyomi
- Komikku : https://github.com/komikku-app/komikku · Tadami : https://github.com/andarcanum/Tadami-Aniyomi-fork

> La Bandita rapporte à partir de sources datées. L'étagère est libre ; ce que tu y mets, c'est aussi ta décision.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : Kototoro re-vérifié (v2.1.3 d'AUJOURD'HUI), Mihon ★23 601, Keiyoushi ★14 980, Yūzōnō ★432, manga-repo ★445. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.

**Note de la vérification finale (15-sep, soir) :** la documentation propre (kototoro-app.github.io/Kototoro) renvoie 404 à cette heure, constaté en direct ; la maison GitHub reste vivante (★569, v2.1.3 d'AUJOURD'HUI). Le site peut être en déménagement ; le lien se rouvre le jour où on l'utilise.
