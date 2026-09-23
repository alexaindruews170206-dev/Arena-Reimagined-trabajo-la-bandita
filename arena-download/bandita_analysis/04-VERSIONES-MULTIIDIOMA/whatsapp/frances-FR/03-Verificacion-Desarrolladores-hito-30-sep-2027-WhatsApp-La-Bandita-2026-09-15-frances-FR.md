# Publicación 03 — Vérification des Développeurs : 15 jours jusqu'au jalon et l'horloge vers 2027

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 03)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 📅 Le chronogramme complet
├── 🪪 Ce qu'est la vérification (dans les mots de Google)
├── 🛒 Les deux consoles et le flux d'enregistrement
├── 🏪 Les sept boutiques du 30 septembre
├── 🎓 Comptes de distribution limitée : la petite porte
├── 🛠️ Le flux avancé (celui de la lettre de 24 heures)
├── 👤 À qui ça touche et à qui non (encore)
├── 📜 La lettre ouverte : les trois objections
├── 📣 La campagne et son horloge
├── 📗 La lecture contraire : F-Droid
├── 📌 Corrections que ce sujet a déjà subies
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Google est en train d'installer un recensement de développeurs pour Android. Le programme s'appelle « vérification des développeurs d'Android » et fonctionne ainsi : pour qu'une application s'installe sur des appareils Android certifiés, son développeur devra être enregistré et vérifié — avec identité réelle, noms de paquet déclarés et clés de signature liées.

Aujourd'hui nous sommes le 15 septembre. Il manque **15 jours** pour le premier jalon public : le 30 septembre, quatre pays et sept boutiques entrent dans le filtre. Si tu vis en République dominicaine — ou dans n'importe quel pays hors du pilote — ta date est une autre : 2027, quand le filtre atteindra toutes les apps des appareils certifiés.

Les voix sont en deux camps que ce guide cite par leur nom : Google, qui le vend comme redevabilité contre le malware ; et F-Droid avec la campagne Keep Android Open, qui le lisent comme un recensement qui rompt la distribution libre d'applications. Ce que tout le monde a, en revanche : une horloge. La campagne maintient un compteur public : 110 jours constatés le 14-sep — le compteur court tout seul.

## 📅 Le chronogramme complet

```
Ago 2025        Google annonce le programme.

29-sep-2025     F-Droid publie son analyse critique :
                « le décret d'enregistrement des développeurs ».

Mar 2026        Le processus s'ouvre à tous les développeurs
                (Play Console et la nouvelle Android Developer
                Console). Blog officiel lu sur sa page.

Jun 2026        Google publie « Building a safer ecosystem
                together » : confirme le départ en 7 boutiques
                et 4 pays, présente des APIs d'automatisation
                et répète le plan global de 2027.

Ago 2026        Les comptes de distribution limitée deviennent
                disponibles pour tous.

30-sep-2026     PREMIER JALON : 4 pays (Brésil, Indonésie,
                Singapour, Thaïlande) · 7 boutiques · Android 7+
                sur appareils certifiés.

2027            Déploiement global : toutes les apps sur
                appareils certifiés.
~Ene 2027       La campagne situe ici le blocage effectif
                et le compte avec horloge publique : 110 jours à la coupe du 14-sep.
```

Les trois documents officiels (hub du programme, guides et blogs) se sont ouverts aujourd'hui ; leurs dates de mise à jour sont de fin août et début septembre. La carte bouge : ce guide porte la date de coupe dans le titre pour une raison.

## 🪪 Ce qu'est la vérification (dans les mots de Google)

La définition officielle tient en une phrase : « la vérification des développeurs d'Android lie des entités du monde réel —personnes et organisations— à leurs applications Android ».

Le cadre de Google : établir la redevabilité (accountability). Décourage les acteurs malveillants, rend plus difficile pour celui qui a fait du mal de répéter sous un autre nom, et donne à l'utilisateur plus de confiance sur qui est derrière une app. Le tarif de l'enregistrement se compare dans la FAQ même à la cotisation historique de 25 dollars de la boutique de Google.

La lecture contraire (F-Droid, Keep Android Open, signataires de la lettre) : ça n'est pas un scanner de malware — c'est un recensement. Il n'analyse pas des archives : il analyse des personnes. Et il met le poids de l'enregistrement sur celui qui distribue, pas sur celui qui distribue mal. Les deux lectures se citent complètes plus bas ; ce guide ne choisit pas de camp pour toi.

## 🛒 Les deux consoles et le flux d'enregistrement

Il y a deux portes, selon par où tu distribues :

- **Play Console** — si tes apps vivent dans la boutique de Google. L'enregistrement s'intègre à ce qui existait déjà.
- **Android Developer Console** — la console neuve, pour tout le reste : boutiques alternatives, distribution directe, sideload organisé.

Le flux de la console neuve, selon son guide officiel (ouvert aujourd'hui), en sept pas :

```
1. Créer le compte
2. Choisir comment tu distribues tes apps
3. Compléter la vérification d'identité
   (les exigences changent selon le type de compte)
4. Enregistrer les noms de paquet de tes apps
5. Automatiser le flux avec les APIs neuves
6. Résoudre les doublons de nom de paquet
   (quand deux projets réclament le même)
7. Révision
```

Les points délicats que la documentation confirme : l'enregistrement exige de déclarer TOUS les noms de paquet que tu distribues, et l'évidence que tu contrôles les clés de signature. Autrement dit : ce n'est pas un formulaire — c'est un inventaire complet de ce que tu as publié.

## 🏪 Les sept boutiques du 30 septembre

Le jalon du 30 septembre ne touche pas « toutes les boutiques » : il touche les participantes déclarées.

```
1.  Google Play
2.  Galaxy Store   (Samsung)
3.  GetApps        (Xiaomi)
4.  HONOR Store
5.  OPPO Store
6.  Palm Store
7.  V-Appstore     (vivo)
```

Quatre pays dans le pilote : Brésil, Indonésie, Singapour et Thaïlande. Appareils certifiés avec Android 7 ou supérieur. Si ton app vit dans ces boutiques et ces pays, le 30 septembre exige que son développeur soit vérifié. Si tu vis hors du pilote, ton calendrier est celui de 2027 — mais le processus peut se devancer, et Google le recommande.

Ce que le 30 septembre NE change pas : le sideload direct d'un APK (installer une archive à la main), F-Droid et les boutiques alternatives hors de la liste. Ça, c'est le sujet de 2027.

## 🎓 Comptes de distribution limitée : la petite porte

La nouveauté du mois, confirmée aujourd'hui dans trois sources officielles (la FAQ, le guide dédié et le blog de juin) :

```
Pour qui :    étudiants, enseignants, amateurs,
              qui apprend
Ce que ça permet :  enregistrer des apps et les partager avec jusqu'à
              20 appareils — que l'utilisateur final
              autorise explicitement
Ce que ça demande : ni identification gouvernementale, ni tarif
Son guide apporte : dates clés, ce que le compte peut faire,
              coût, comment marche le partage, si c'est pour
              toi, et ce qu'il te faut pour t'enregistrer
```

C'est une fenêtre réelle pour la salle de classe, l'atelier et le hobby. Avec plafond dur : vingt appareils ne soutiennent pas un projet communautaire ni une distribution ouverte. C'est la porte pour apprendre, pas la porte pour vivre.

## 🛠️ Le flux avancé (celui de la lettre de 24 heures)

Pour qui ne peut pas ou ne veut pas passer par l'enregistrement complet, il existe un flux avancé. Selon la documentation de la campagne (vérifiée aussi la semaine passée), ça fonctionne ainsi :

- Neuf pas, décrits dans le guide.
- Une attente d'environ 24 heures.
- Ça court à travers Play Services — du service de Google, pas du système ouvert.

Ce dernier point est celui qui génère le plus de discussion : le chemin alternatif passe par le même composant propriétaire que le chemin standard. Si Play Services n'y est pas — téléphones sans Google — le flux ne s'applique pas.

La FAQ officielle maintient sa section « Advanced flow » comme voie reconnue.

## 👤 À qui ça touche et à qui non (encore)

```
Ta situation                                  Ça change le 30-sep ?
Publies dans les 7 boutiques, pays pilote     Oui : dev vérifié
                                              ou ton app n'entre pas
Publies dans les 7 boutiques, hors pilote     Ta date est 2027
Installes des APK à la main (sideload)        Non. Encore. Ton sujet : 2027
Utilises F-Droid                              Non. Encore. La campagne
                                              dit que sa date d'impact
                                              n'est pas publiée
Téléphone sans certification de Google        Un autre monde : le filtre
                                              va sur les certifiés
```

La phrase qui résume tout : qui distribue dans le monde certifié est dans le recensement — aujourd'hui dans quatre pays, demain dans tous. Qui vit hors de ce monde a une fenêtre d'un an de plus.

## 📜 La lettre ouverte : les trois objections

Keep Android Open a organisé une lettre ouverte à Google (lue aujourd'hui sur sa page). Sa structure est de trois blocs :

**1. Nos préoccupations.** L'enregistrement avec identité convertit la distribution de logiciel en un acte identifié devant une corporation ; l'impact tombe sur les développeurs petits, les projets anonymes par sécurité et les communautés hors des circuits formels.

**2. Les mesures existantes suffisent.** Play Protect scanne déjà ; les boutiques filtrent déjà ; les mécanismes de sécurité du système existent déjà. Le recensement n'ajoute pas un scanner : il ajoute un registre de personnes.

**3. La pétition.** Que Google retire l'exigence d'enregistrement avec identité comme condition de distribution.

Les chiffres que la lettre même montre : 71 signataires, 23 pays. Parmi les visibles : AdGuard, Aurora Store, BEUC, Brave, Calyx, CCC, Codeberg, F-Droid, FUTO, GrapheneOS, IzzyOnDroid, KDE, microG, Nextcloud, Obtainium, Tor, Vivaldi et la Fundación Karisma, entre autres. Apparaître dans la liste n'est pas recommandation d'installer quoi que ce soit — c'est la carte de qui a signé.

## 📣 La campagne et son horloge

https://keepandroidopen.org

La campagne maintenait en couverture son compteur public : **110 jours** (constaté le 14-sep) — vers ce que sa FAQ appelle le blocage, le situant autour de janvier 2027. Sa phrase de couverture : « Your phone is about to stop being yours ».

Ce que la campagne documente de l'enregistrement standard : tarif, identification gouvernementale, évidence de possession de la clé de signature, et la déclaration de tous les noms de paquet. Sa consigne — « Do not sign up » — est de la campagne ; ce guide la cite, ne la dicte pas.

Sa FAQ clarifie aussi la question que la communauté répète le plus : septembre N'inclut pas F-Droid ; la date à laquelle le filtre atteint F-Droid n'est pas publiée. Le compteur de la campagne est la seule compte à rebours publique qui existe sur 2027 — pour ça ce guide la cite avec sa date.

## 📗 La lecture contraire : F-Droid

https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html

L'analyse de F-Droid (publiée le 29 septembre 2025, ouverte aujourd'hui) titre le programme « le décret d'enregistrement des développeurs de Google » et le démonte en quatre sections :

- **Le mouvement pour rompre la distribution libre** — la thèse : sans identité, pas de distribution ; sans distribution, pas de logiciel libre sur Android.
- **L'appât de la sécurité** — le malware se combat déjà avec de l'analyse ; le recensement n'analyse pas des archives, il analyse des auteurs.
- **Le droit d'exécuter** — ton téléphone, ton logiciel : la ligne de fond que la lettre défend.
- **Ce qu'ils proposent** — des alternatives qui ne passent pas par l'enregistrement avec identité.

F-Droid maintient en plus sa bannière « under threat » sur tout son site, avec la campagne active. Pour l'écosystème libre, c'est LE sujet de l'année.

## 📌 Corrections que ce sujet a déjà subies

Cette affaire corrige des versions antérieures d'elle-même. Historique de ce qu'on a cru et qui a cessé d'être vrai :

```
On croyait avant             Ce qui fut confirmé après
« Le 30-sep bloque les APKs »  30-sep = 4 pays, 7 boutiques.
                              Le blocage large est 2027.
« Android 8+ »                Android 7+.
« 6 boutiques »               7.
« Annoncé en nov-2025 »       Août 2025.
« Le flux avancé prend        C'est d'une seule fois :
24 h par chaque APK »         9 pas + une attente de ~24 h.
« Limited = sans ID et voilà »  Sans ID, mais avec profil de paiements,
                              2FA et compte Google pour opérer.
« Le blog de juin ne se       Il fut lu : confirme 7 boutiques,
peut pas lire »               4 pays, APIs et plan 2027.
```

La leçon du sujet : chaque mois apporte sa correction. Rouvre les sources le jour où tu décides quelque chose — celles d'en haut sont d'aujourd'hui.

## ❓ Questions fréquentes

**Le 30 septembre me bloque-t-il d'installer des APKs à la main ?**
Non. Ce jalon touche les boutiques participantes de quatre pays. Le sideload direct et F-Droid restent dehors — pour l'instant. Ton horloge sérieuse est 2027.

**Je dois faire quelque chose AUJOURD'HUI ?**
Si tu vis dans le pilote ou publies dans ces boutiques : oui, te vérifier. Sinon : non — mais il convient de connaître le processus avant que ce soit ton tour.

**La vérification coûte-t-elle ?**
L'enregistrement se compare dans la FAQ aux 25 dollars de Play. Les comptes de distribution limitée ne paient ni tarif ni ne demandent d'ID.

**Et si je ne fais des apps que pour moi ?**
Vingt appareils, c'est le monde des comptes limitées : sans ID, sans tarif. Pour un cercle intime, ça suffit.

**Ça tue F-Droid en septembre ?**
Non — et il n'est pas publié quand, si ça arrive. C'est la question la plus répétée et la réponse honnête est : personne hors de Google n'a cette date.

**C'est quoi ces « appareils certifiés » ?**
Ceux qui sortent d'usine avec les services de Google. Un téléphone sans certification vit hors de la portée du filtre — avec tout le reste que ça implique.

**Le compteur de 110 jours est-il officiel ?**
Il est de la campagne, pas de Google. Sa date — le blocage autour de janvier 2027 — est sa lecture du calendrier. Google dit « 2027 » sèche. Deux horloges, deux voix.

**Où je lis les sources sans l'interprétation de personne ?**
Dans les liens d'en bas : hub, guides, FAQ et blogs sont de Google ; la lettre et la FAQ, de la campagne ; l'analyse, de F-Droid. Tout s'ouvre aujourd'hui.

## 🔗 Liens

- Hub officiel : https://developer.android.com/developer-verification
- FAQ officielle : https://developer.android.com/developer-verification/guides/faq
- Distribution limitée : https://developer.android.com/developer-verification/guides/limited-distribution
- Console neuve : https://developer.android.com/developer-verification/guides/android-developer-console
- Blog de mars : https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html
- Blog de juin : https://android-developers.googleblog.com/2026/06/android-developer-verification.html
- Campagne : https://keepandroidopen.org · https://keepandroidopen.org/faq/ · https://keepandroidopen.org/open-letter
- F-Droid : https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html

> La Bandita rapporte à partir de sources datées. L'horloge court ; qui lit les sources à temps choisit à temps.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : horloge : 15 jours restants ; compteur 110 constaté au 14. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
