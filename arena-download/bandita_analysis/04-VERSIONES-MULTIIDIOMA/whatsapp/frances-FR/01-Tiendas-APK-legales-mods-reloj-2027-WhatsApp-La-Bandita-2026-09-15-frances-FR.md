# Publicación 01 — Boutiques d'APK : la boutique légale, le panneau des mods et l'horloge de 2027

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 01)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🏪 Les boutiques qui oui (fiche par fiche)
├── 🧰 Les installateurs qui t'apportent les boutiques
├── ⚠️ Les panneaux des mods (nommés, pas prescrits)
├── 🕐 L'horloge de 2027 et la petite porte
├── 🧭 Quoi regarder avant d'installer n'importe quel APK
├── 🚩 Signes d'appât
├── ❓ Questions fréquentes
├── 📚 Mots-clés de ce guide
└── 🔗 Liens

## ⚡ En une page

Une boutique d'APK est un lieu au propriétaire connu qui te laisse installer des applications hors de la boutique officielle du téléphone. Il y en a de deux classes : celles qui révisent, signent et se rendent responsables de ce qu'elles publient — et celles qui vivent du trafic de mods, où le « premium gratuit » arrive avec un cadeau-surprise dans l'archive.

Ce guide parcourt les boutiques légitimes de l'écosystème libre, une par une, avec leur état réel au 15 septembre 2026 : laquelle est sous menace, laquelle a inauguré une version hier, laquelle a changé de maison il y a des jours. Et il finit avec l'horloge : la politique de vérification des développeurs de Google a déjà un compte à rebours public.

Si tu viens pour « Spotify premium gratuit » ou « jeux tout débloqués », ce guide ne t'accompagnera pas : ça n'est pas une boutique, c'est un hameçon avec portefeuille.

## 🏪 Les boutiques qui oui (fiche par fiche)

### F-Droid — la maison mère

https://f-droid.org

La boutique historique du logiciel libre sur Android. Tout ce qu'elle publie passe par compilation reproductible : l'archive que tu télécharges peut se reconstruire depuis le code public, et si elle ne coïncide pas, elle ne sort pas. C'est la promesse de fond, celle qu'aucune boutique de mods ne peut égaler.

Vu le 14-sep : le site maintient sa bannière de campagne — « F-Droid is under threat » — dans le cadre du programme de vérification des développeurs de Google que ce guide-même chronomètre plus bas. L'installateur de la boutique elle-même se télécharge directement de son site.

Si tu ne dois choisir qu'une boutique de cette liste, choisis celle-ci. C'est la plus vieille, la plus révisée et celle qui a le standard de publication le plus exigeant de l'écosystème libre.

```
F-Droid en une boîte
Qu'est-ce :      boutique et dépôt d'apps libres
Promesse :       compilation reproductible, sans traqueurs déclarés
État à son jour (14-sep) :  vivante, avec campagne active « under threat »
Pour qui :       tout le monde ; c'est le point d'entrée naturel
```

### IzzyOnDroid — l'annexe respectée

https://apt.izzysoft.de/fdroid

Le dépôt complémentaire le plus connu de l'écosystème F-Droid : beaucoup d'apps qui n'entrent pas encore au canal principal se publient d'abord ici. C'est un entrepôt de confiance dans la communauté, maintenu depuis des années.

Vu le 14-sep : le site répond ; sa charge dépend de JavaScript, donc le navigateur le monte à son rythme. Rien d'alarmant : c'est le même site de toujours.

### Droid-ify — le client F-Droid moderne

Dépôt canonique : https://codeberg.org/droidify/client
Miroir sur GitHub : https://github.com/Droid-ify/client

Un client pour consommer des catalogues type F-Droid avec interface moderne. La version 0.7.8 est sortie le 12 septembre : elle apporte la correction du dépôt après import, l'import par code QR, un installateur pour qui a root, et un thème adaptatif Material You.

Détail qui compte : le projet déclare que sa maison officielle est Codeberg et que sa page GitHub n'est que miroir. Quand un projet nomme canonique un autre domaine, c'est ce lien qui commande — la règle de ce guide est simple : le canonique d'abord.

```
Droid-ify en une boîte
Qu'est-ce :      client de dépôts F-Droid
Dernière :       0.7.8 — 12 septembre 2026
Maison :         codeberg.org/droidify/client (GitHub est miroir)
Extras :         QR, installateur root, thème dynamique
```

### Neo-Store — le client à boussole de traqueurs

https://github.com/NeoApplications/Neo-Store

Un autre client de l'écosystème F-Droid, avec des détails d'utilisabilité que sa communauté soigne. Son mouvement le plus récent (commit du 13 septembre) est un joyau de design : il remplace le bloc statique de traqueurs de chaque fiche par des actions de contrôle — et te donne un raccourci vers Exodus Privacy pour auditer n'importe quelle app installée.

C'est une idée de boutique mûre : non seulement te laisser installer, mais te donner l'instrument pour savoir ce qui s'installe. La version stable est la 1.2.6.

### Komi Store — celle qui a changé de maison (et le crie)

https://github.com/komi-store/komi-store
Site : https://komistore.app

Cette fiche existe parce que le changement de maison embrouille. Komi Store s'appelait avant « GitHub Store » et vivait dans une autre organisation ; elle a migré vers l'organisation komi-store, inauguré son propre domaine (komistore.app) et va par la version 1.9.3 (code 22). Le mouvement est déclaré par le projet lui-même dans son dépôt — 18 500 étoiles et activité de début septembre.

La différence entre « a migré » et « on l'a clonée » est celle-ci : la migration, le propriétaire l'annonce, dans le dépôt, avec historique. Le clone apparaît de nulle part, avec le nom d'un autre et la hâte que tu installes. Komi a fait le premier.

### Aurora Store — la porte vers un autre catalogue

https://gitlab.com/AuroraOSS/AuroraStore

Le client libre qui consulte le catalogue de la boutique de Google sans livrer ton compte : sessions anonymes, recherches et mises à jour, sans exposer ton identité principale. C'est une des pièces les plus installées de l'écosystème libre et elle a de l'infrastructure série derrière.

Vu le 14-sep : la version étiquetée la plus récente est la 4.8.4, avec activité de dépôt des dernières semaines. Et un détail qui en dit long sur le projet : son commit de documentation le plus récent est exactement ceci — « déclarer l'usage de l'IA dans le développement ». Transparence déclarée volontairement. Ça, dans une boutique de mods, ça n'existe pas et n'existera pas.

### Accrescent — la jeune aux standards hauts

https://accrescent.app

La boutique la plus jeune de la liste, en phase alpha, avec Android 10 comme minimum. Ce n'est pas « une F-Droid de plus » : son pari est la sécurité d'entrée — vérification stricte des signatures (key pinning), métadonnées signées, mises à jour automatiques sans privilèges additionnels sur Android 12 ou supérieur, support des APK divisés et zéro comptes.

On la trouve aussi dans la boutique de GrapheneOS, ce qui est un bon thermomètre de qui la communauté paranoïaque — à raison — écoute.

```
Accrescent en une boîte
Qu'est-ce :      boutique centrée sécurité, en alpha
Minimum :        Android 10
Signature :      key pinning + métadonnées signées
Comptes :        aucun
Voie :           site propre et boutique de GrapheneOS
```

### Appteka — le marché de communauté (à la loupe)

https://appteka.store
Code du client : https://github.com/solkin/appteka-android

Un marché géré par communauté avec grand catalogue (il déclare 320 000 applications) et client propre : la version officielle du client est la 23.0, pèse moins de 4 Mo et demande Android 6 en avant. Le site vit et répond.

Elle va dans la liste des « oui » mais à la loupe : étant un catalogue de communauté, le standard de publication n'est pas celui de F-Droid. Elle sert, et en échange elle demande ce que tout ce guide répète : regarder le propriétaire de l'archive avant d'installer.

Dans Appteka vivent des fiches d'apps concrètes que ce guide cite comme exemple d'état — par exemple, les pages des deux projets Rebuild, ouvertes aujourd'hui avec la version 23.0 du client visible dans les titres. Citées comme exemple de vie du marché, pas comme recommandation de ces apps concrètes.

## 🧰 Les installateurs qui t'apportent les boutiques

Les dernières années ont apporté une figure neuve : des outils qui ne sont pas des boutiques à vitrine, mais des installateurs qui construisent ta propre boutique sur mesure, suivant les dépôts que tu leur signales.

### Obtainium — l'app qui surveille les dépôts pour toi

https://github.com/ImranR98/Obtainium

La plus populaire de son espèce : tu lui dis quels dépôts t'importent et elle surveille leurs lancements, téléchargeant et installant les versions neuves dès qu'elles sortent. AUJOURD'HUI 15-sep elle cumule près de 19 700 étoiles et des commits d'hier — un des projets les plus vivants de toute cette carte.

Son propre README crédite ObtainX comme l'installateur externe de l'écosystème. C'est aussi un signe de maturité : savoir nommer les voisins.

### ObtainX — le bras installateur

https://github.com/bikram-agarwal/ObtainX

Vivant (constaté le 14-sep). Complément d'installation de l'écosystème Obtainium : le maillon entre « j'ai détecté une version neuve » et « elle est installée dans le téléphone ».

### Omnify — le client F-Droid sans bruit

https://github.com/Victor-root/Omnify
Site : https://victor-root.github.io/Omnify/

Vivant à son jour (14-sep), avec sa landing qui charge : il se présente comme « un client F-Droid sans désordre qui installe des applications de n'importe où ». Un des paris neufs pour rendre la consommation de catalogues libres plus aimable.

```
Les trois en une phrase
Obtainium :  surveille les releases et t'avise
ObtainX :    exécute l'installation
Omnify :     client F-Droid léger
Aucune des trois ne te demande de sortir de la voie légale.
```

## ⚠️ Les panneaux des mods (nommés, pas prescrits)

Ces noms existent pour que tu les reconnaisses, pas pour que tu les visites :

- **Espacio APK** — site vivant (constaté le 14-sep), catalogue d'« apps et jeux populaires ». Son produit réel : des mods à promesses premium.
- **HappyMod** — a répondu le 14-sep sans titre lisible (bouclier anti-bot). Son modèle d'affaires : téléverser des mods téléversés par n'importe qui, sans chaîne de garde sérieuse.
- **Liteapks** — vivant (constaté le 14-sep), il s'annonce comme « #1 en MOD APK ». Le numéro un des mods est, par définition, le numéro un des archives sans révision.

Le patron commun : ils te promettent le payant gratis, ils te demandent des permissions que l'app originale ne demande pas, et si quelque chose tourne mal il n'y a ni dépôt ni propriétaire à qui réclamer. Le « mod » bien souvent n'est même pas l'app originale : c'est une autre app déguisée avec son icône.

Ici, pas de liens. Le nom accomplit déjà sa fonction : s'il t'apparaît dans un groupe avec « télécharge-le d'ici », tu sais ce que c'est.

## 🕐 L'horloge de 2027 et la petite porte

Le cadre qui change tout ceci a une date et une horloge publiques.

Le plan de Google — « vérification des développeurs d'Android » — exige que les apps des appareils certifiés soient enregistrées par des développeurs vérifiés. Le 30 septembre 2026 arrive le premier jalon : quatre pays (Brésil, Indonésie, Singapour, Thaïlande), sept boutiques (Google Play, HONOR, OPPO, Galaxy Store, Palm Store, V-Appstore et GetApps), Android 7 en avant.

En 2027 le filtre arrive à toutes les apps des appareils certifiés. La campagne Keep Android Open maintient aujourd'hui son compteur public : 110 jours — et sa FAQ situe déjà le blocage autour de janvier 2027. Deux calendriers, le même message : le temps du sideloading tel qu'on le connaît est compté.

La petite porte que Google a ouverte ce mois-ci : les comptes de distribution limitée. Pour étudiants, enseignants et amateurs — jusqu'à 20 appareils, sans identification gouvernementale et sans tarif. C'est un petit soulagement à plafond dur : vingt appareils ne soutiennent pas un projet communautaire.

```
L'horloge, en deux lignes
30-sep-2026 : 4 pays, 7 boutiques, Android 7+
2027 :        toutes les apps, appareils certifiés
Compteur de la campagne (au 14-sep) : 110 jours
```

Ce que ça signifie pour l'écosystème libre : F-Droid avec sa bannière de menace, Accrescent construisant la sécurité depuis aujourd'hui, et chaque boutique de ce guide sachant que son modèle joue son avenir dans les prochains mois. Personne de cette liste ne reste immobile — et c'est ça, peut-être, le meilleur signal de tous.

## 🧭 Quoi regarder avant d'installer n'importe quel APK

```
1. D'où sort-il ?
   Dépôt ou site avec historique > lien d'un groupe.

2. Qui signe ?
   Le projet déclare sa signature ; si l'archive ne
   coïncide pas avec cette signature, c'est autre chose.

3. Que demande-t-il ?
   Permissions que l'app originale ne demande pas = motif.

4. Est-il dans plus d'une boutique sérieuse ?
   F-Droid + dépôt propre + IzzyOnDroid = triple voie.
   Seulement sur un site de mods = aucune voie.

5. Que disent les auditeurs ?
   Exodus (traqueurs), VirusTotal (plusieurs moteurs),
   le dépôt du projet (issues réelles d'utilisateurs).

6. Y a-t-il hâte ?
   « Dernières 24 heures avec ce lien » est la grammaire
   de l'appât. Le bon reste là demain.
```

## 🚩 Signes d'appât

- L'annonce en haut du moteur « télécharge X » paie plus cher que le résultat légitime. Celui qui paie l'annonce n'est pas le projet.
- « Version modifiée », « premium débloqué », « tout illimité » : quelqu'un a modifié quelque chose — ce qu'il ne te dit pas, c'est ce qu'il a mis dedans en plus.
- La page te demande de désactiver la protection du téléphone pour « compléter l'installation ». Aucune boutique sérieuse n'a besoin que tu baisses ta culotte de sécurité.
- Commentaires clonés sur plusieurs pages avec les mêmes phrases.
- Le cadenas du navigateur : il dit seulement que la connexion est chiffrée. La banque l'a, et le phishing aussi.

## ❓ Questions fréquentes

**Par laquelle je commence si je pars de zéro ?**
F-Droid. C'est la porte avec le plus d'histoire, de révision et de communauté. De là pend le reste : IzzyOnDroid comme annexe, et le client que tu préfères (Droid-ify ou Neo-Store) pour manier le catalogue avec commodité.

**Les apps de F-Droid sont-elles 100 % sûres ?**
Aucune boutique ne promet ça. F-Droid promet la transparence : compilation reproductible et politique déclarée. C'est le standard le plus haut de l'écosystème libre, pas une baguette magique.

**Pourquoi y a-t-il deux maisons pour Droid-ify (Codeberg et GitHub) ?**
Parce que le projet le déclare ainsi : Codeberg est canonique, GitHub miroir. Quand un projet déclare sa maison, la maison commande. C'est la même logique de « le dépôt vivant oui » que cette famille de guides répète.

**Komi Store et « GitHub Store » sont-ils les mêmes ?**
Oui — elle a migré d'organisation et le documente dans son dépôt, avec domaine propre. La migration, le propriétaire la raconte ; le clone n'a pas de propriétaire qui raconte.

**Aurora Store est-elle « la boutique de Google illégale » ?**
Non. C'est un client libre qui consulte ce catalogue sans ton compte. Le projet le déclare et le maintient avec activité récente — jusqu'à déclarer dans sa documentation quand il utilise l'IA dans le développement.

**Les comptes de distribution limitée me servent-ils à « distribuer » mon app au groupe ?**
Vingt appareils, c'est un circuit fermé : essais, classe, maison. Pour quelque chose de plus large, la voie est une autre (et chaque voie exige la sienne).

**Et les mods ? Jamais ?**
Ce guide ne les prescrit ni ne les lie. Si quelqu'un insiste, que ce soit avec la signature révisée et le risque signé par celui qui insiste — qui n'est jamais celui qui va perdre les données.

**Le 30 septembre me bloque-t-il le téléphone ?**
Non. Ce jalon touche les boutiques participantes de quatre pays. Ton changement arrive avec le déploiement global de 2027. Rouvre ce guide le jour où tu décides quelque chose : la carte bouge.

## 📚 Mots-clés de ce guide

```
APK           le paquet installable d'une app Android
Sideload      installer hors de la boutique du système
Reproductible l'archive sort pareille recompilée depuis le code
Key pinning   la signature du projet est attachée d'avance
Split APKs    le paquet vient en parties par architecture
Exodus        audit public de traqueurs dans les apps
Dépôt         dépôt : la maison du code (et de la vérité)
```

## 🔗 Liens

- F-Droid : https://f-droid.org
- IzzyOnDroid : https://apt.izzysoft.de/fdroid
- Droid-ify (canonique) : https://codeberg.org/droidify/client · miroir : https://github.com/Droid-ify/client
- Neo-Store : https://github.com/NeoApplications/Neo-Store
- Komi Store : https://github.com/komi-store/komi-store · https://komistore.app
- Aurora Store : https://gitlab.com/AuroraOSS/AuroraStore
- Accrescent : https://accrescent.app
- Appteka : https://appteka.store · client : https://github.com/solkin/appteka-android
- Obtainium : https://github.com/ImranR98/Obtainium · ObtainX : https://github.com/bikram-agarwal/ObtainX
- Omnify : https://github.com/Victor-root/Omnify · https://victor-root.github.io/Omnify/
- Vérification des développeurs : https://developer.android.com/developer-verification
- Campagne : https://keepandroidopen.org

> La Bandita rapporte à partir de sources datées. La boutique légale te donne ce que le mod jamais : un propriétaire à qui exiger des comptes.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : date d'état. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.

**Note de la vérification finale (15-sep, soir) :** le site propre d'Omnify (victor-root.github.io/Omnify) renvoie 404 à cette heure, constaté en direct ; la maison GitHub reste vivante (★20, v1.0.5-beta.6 du 4-sep). Les liens se rouvrent le jour où on les utilise — règle de la maison.
