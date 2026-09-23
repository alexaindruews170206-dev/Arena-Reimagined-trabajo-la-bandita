# Publicación 09 — Outils FOSS : la boîte du métier, chaque pièce avec sa date d'aiguisage

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 09)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── 🖼️ Galerie et fichiers
├── 🔐 Clés et second facteur
├── 📲 Transférer et connecter
├── 🧰 Le tiroir de système
├── 🗺️ Cartes
├── 📦 Comment se gèrent les installations
├── 📌 Pourquoi 20 pièces et pas 200
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Le codex d'outils d'avril se périma — versions vieilles vendues comme vigentes, listes gonflées par gonfler. Cette boîte est celle de la coupe, 15 septembre (mesurée le 14, re-vérifiée au déménagement) : chaque pièce avec son dépôt ouvert dans les dernières heures, son état réel et son travail. Curatelle courte à dessein : vingt pièces qui couvrent le métier, toutes vérifiées, zéro remplissage.

La boîte, par tiroirs :

```
GALERIE ET FICHIERS
Fossify Gallery ★3 696 · File-Manager ★1 753 · Phone ★1 329
Calendar ★2 156 · Clock ★698            (pushes vérifiés le 14-sep)
Amaze File Manager ★6 387               l'alternative material

CLÉS ET SECOND FACTEUR
KeePassDX ★7 301 · releases de septembre
Aegis Authenticator ★13 086             2FA avec coffre chiffré

TRANSFÉRER ET CONNECTER
LocalSend ★91 047                       l'AirDrop libre
Orbot ★3 538                            Tor dans la poche

SYSTÈME
Termux ★60 797 · App Manager ★8 972 (v4.1.1)
Shizuku ★30 121                         APIs du système sans root

CARTES
Organic Maps ★15 415                    hors ligne, de vrai

INSTALLATIONS
Obtainium ★19,7k                        (fiche dans le guide de boutiques)
```

## 🖼️ Galerie et fichiers

### Fossify — la famille qui substitua les Simple

https://github.com/FossifyOrg

Quand les Simple Mobile Tools se remplirent de publicités, la communauté fourcha tout le set et le maintint libre : ainsi naquit Fossify. Aujourd'hui la famille pousse du code cette même semaine, pièce par pièce :

- **Gallery** (★3 696) — la galerie sans publicité qui respecte tes photos.
- **File-Manager** (★1 753) — fichiers simples et honnêtes. Œil au nom : FossifyOrg/Files n'existe pas ; le canonique est File-Manager.
- **Phone** (★1 329) — composeur et blocage de numéros, avec multi-SIM.
- **Calendar** (★2 155) — calendrier avec événements et widgets, sans compte attaché.
- **Clock** (★699) — horloge, alarme, chronomètre et minuteur.

GPL-3.0 toutes. Leurs versions étiquetées sont de février ; leurs pushes, de septembre : le patron de projet mûr — stables tranquilles, maintien continu.

### Amaze File Manager — l'alternative avec pédigré

https://github.com/TeamAmaze/AmazeFileManager

★6 387 · vivant. L'administrateur de fichiers material de toujours, des plus vétérans de l'écosystème libre Android. Si Fossify te semble trop minimaliste, c'est l'option avec plus d'années dessus — et avec racines dans la communauté depuis l'époque des premières ROMs.

## 🔐 Clés et second facteur

### KeePassDX — le coffre compatible

https://github.com/Kunzisoft/KeePassDX

★7 301 · GPL-3.0 · push du 11-sep. La semaine apporta trois releases au projet, aux noms de chat : « Scholarly Student » (2-sep), « Cutie Cat » (4-sep) et « Clever Cat » (10-sep). Coffre de mots de passe compatible avec le format KeePass : tes bases s'ouvrent sur n'importe quelle plateforme de l'écosystème KeePass, sans rester prisonnier de personne. Les données vivent dans TON fichier — nuage optionnel, pas obligatoire.

Si à un moment tu mis un mot de passe dans un site qui tomba ensuite (le guide de TMO de cette famille en compte un grand), c'est le type d'outil qui ordonne la maison après : un coffre, des mots de passe distincts par site, sauvegarde chiffrée.

### Aegis Authenticator — le second factor qui est tien

https://github.com/beemdevelopment/Aegis

★13 086 · GPL-3.0 · vivant. Les codes de vérification en deux pas, dans une app libre avec coffre chiffré (AES-256 selon sa documentation), déblocage par empreinte, sauvegarde chiffrée exportable et importation depuis les apps propriétaires plus communes (Google Authenticator, Authy, Microsoft, 2FAS et autres, selon sa liste officielle). L'argument de fond : tes codes 2FA sont la clé de ta vie digitale — les déposer dans une app fermée sans exportation, c'est laisser les clés au serrurier sans copie.

## 📲 Transférer et connecter

### LocalSend — l'AirDrop de tous

https://github.com/localsend/localsend

★91 047 — oui, quatre-vingt-onze mille — · vivant · MIT selon sa fiche. La révélation silencieuse du logiciel libre des dernières années : passer des fichiers entre téléphone, PC, tablette et jusqu'au téléphone du voisin sans câbles, sans nuage et sans comptes — réseau local, protocole ouvert, apps pour toutes les plateformes. Si tu venais collant des fichiers par WhatsApp « pour les passer au PC », cette pièce seule justifie le guide entier.

### Orbot — Tor dans la poche

https://github.com/guardianproject/orbot

★3 538 · vivant · du projet Guardian. L'app qui route ton trafic par le réseau Tor sur Android, avec VPN intégrée ou comme proxy par application. Ce n'est pas pour toute la journée ni pour tout le monde : c'est l'outil de connexion quand le circuit dont tu as besoin exige de l'anonymat réel — journalisme, investigation, ou simplement sortir du pays sans sortir de chez soi. Du côté sérieux de l'écosystème.

## 🧰 Le tiroir de système

### Termux — le terminal de poche

https://github.com/termux/termux-app

★60 797 · push du 11-sep. Un terminal Linux complet sur Android : éditeurs, langages, ssh, scripts. La porte d'entrée pour « faire de vrai » avec le téléphone. Sa version étiquetée sur GitHub est de mai 2025 (avec des betas de la 0.119) — son canal de paquets va par son côté et avec un autre rythme ; le débat GitHub-vs-F-Droid de Termux est vieux et ne se rouvre pas ici : dépôt nommé, canal choisi le jour où tu installes. Soit une règle : ne se collent pas les scripts de personne — le terminal est pouvoir, et le pouvoir s'exécute avec ce que toi tu as écrit ou lu complet.

### App Manager — le radiographe de tes apps

https://github.com/MuntashirAkon/AppManager

★8 985 · **version 4.1.1 (4 septembre)** · push d'AUJOURD'HUI (re-vérifié 15-sep). Le gestionnaire de paquets complet : voir quelles permissions demande chaque app, quelles activités elle expose, quels traqueurs elle traîne, et désinstaller à fond. Il corrige la photo de la semaine passée, quand la version ne répondait pas dans l'API : aujourd'hui elle y est, et elle est de ce mois. Sa licence sur la page figure comme propre (Proprietary-style libre — le projet la définit dans son dépôt ; à lire là-bas avant de redistribuer).

### Shizuku — les APIs du système sans root

https://github.com/RikkaApps/Shizuku

★30 121 · Apache-2.0 · version 13.6.0. La pièce qui changea le jeu du « sans root » : elle laisse des apps autorisées utiliser les APIs du système directement, avec permissions concédées via ADB (une fois par allumage) ou root. C'est le moteur silencieux derrière la moitié d'une douzaine d'outils modernes de personnalisation et de contrôle. Ce n'est pas pour qui commence : c'est pour qui sait déjà pourquoi il le cherche.

## 🗺️ Cartes

### Organic Maps — la carte qui ne regarde pas en arrière

https://github.com/organicmaps/organicmaps

★15 427 · release d'août (2026.08.27) · push d'AUJOURD'HUI (re-vérifié 15-sep). Cartes hors ligne complètes de la planète, sans compte, sans traque, données d'OpenStreetMap. Pour le voyage, pour le quartier sans données, pour qui décida que Google n'a pas besoin de savoir par où il marche. Sa licence sur la page figure avec avis particulier (licence propre du projet, lisible dans son dépôt) — dit tel quel, sans inventer d'étiquettes.

## 📦 Comment se gèrent les installations

**Obtainium** — https://github.com/ImranR98/Obtainium — ★19,7k (19 702), commit du 13-sep. L'outil qui surveille les dépôts de cette boîte et t'installe les versions neuves dès qu'elles sortent. Sa fiche complète vit dans le guide de boutiques de cette famille ; ici suffit sa phrase : le tiroir d'outils s'actualise aussi tout seul.

Et le fond de la boîte, pour tous les tiroirs : **F-Droid** — la boutique libre où bonne partie de ces pièces vit aussi publiée. Trois voies (dépôt de GitHub, F-Droid, Obtainium) pointant vers le même logiciel : ça, c'est la redondance saine de l'écosystème libre.

## 📌 Pourquoi 20 pièces et pas 200

Le codex d'avril apportait 88 outils. De ceux-là, beaucoup étaient en version vieille vendue comme neuve, et plusieurs répétaient fonction quatre fois. Le critère de cette boîte est le contraire :

```
Une fonction, une pièce   si deux apps font la même chose,
                          reste la plus vivante — pas la plus mentionnée
Tout vérifié aujourd'hui  si le nombre ne s'ouvrit pas aujourd'hui,
                          il ne va pas avec date d'aujourd'hui
Creux déclaré             ce qui N'EST pas dans la boîte (navigateurs,
                          courriel, messagerie, nuages), c'est parce que
                          ça mérite guide propre, pas parce que ça n'existe pas
```

La boîte du métier n'a pas besoin d'être infinie. Elle a besoin d'être vraie.

## ❓ Questions fréquentes

**Ces apps sont-elles dans Play Store ?**
Plusieurs oui (Aegis, LocalSend, Organic Maps parmi elles). La voie de l'écosystème libre est F-Droid ou le dépôt — le guide de boutiques de cette famille explique les trois portes. Ce guide n'ouvre pas Play : la fiche de chaque boutique est sujet de sa propre pièce.

**Fossify ou Amaze pour les fichiers ?**
Fossify : minimaliste, de la famille complète (galerie, contacts, calendrier). Amaze : plus de fonction par écran, plus d'années de vol. Essaie les deux : ils sont gratis en tous les sens.

**KeePassDX ou Bitwarden ?**
Philosophies distinctes : KeePassDX garde TON fichier (compatible KeePass, zéro dépendance) ; Bitwarden est service avec synchronisation propre. Pas comparés à fond ici : sans comparatif inventé.

**Shizuku est-il dangereux ?**
Il donne du pouvoir de système à des apps que TOI tu autorises, via ADB ou root. Il est aussi dangereux que la clé que tu laisses sous le paillasson si tu autorises n'importe qui. La tête froide, c'est le pont parfait entre « sans root » et « contrôle total ».

**LocalSend marche-t-il entre iPhone et Android ?**
Oui : ça fait partie de son point — multiplateforme complète (Android, iOS, Windows, macOS, Linux), réseau local, sans nuage.

**Orbot ralentit-il tout ?**
Tor paie son anonymat avec de la latence. Pour la navigation sensible, c'est le prix. Pour toute la journée, ce n'est pas pensé — et sa propre documentation le dit mieux que ce résumé.

**Termux a-t-il besoin de root ?**
Non. Sa puissance ne dépend pas du root — elle dépend de ce que tu sais faire avec un terminal. Le root ouvre d'autres chapitres, avec d'autres risques (le guide de GLTools de cette famille raconte pourquoi on ne joue pas avec ça depuis le canapé).

**Tous les combien se re-vérifie cette boîte ?**
Chaque fois qu'on s'en sert. Aujourd'hui fut la coupe ; les nombres qui ne s'ouvrent pas un autre jour ne se citent pas comme frais.

## 🔗 Liens

- Fossify : https://github.com/FossifyOrg/Gallery · https://github.com/FossifyOrg/File-Manager · https://github.com/FossifyOrg/Phone · https://github.com/FossifyOrg/Calendar · https://github.com/FossifyOrg/Clock
- Amaze : https://github.com/TeamAmaze/AmazeFileManager
- KeePassDX : https://github.com/Kunzisoft/KeePassDX · Aegis : https://github.com/beemdevelopment/Aegis
- LocalSend : https://github.com/localsend/localsend · Orbot : https://github.com/guardianproject/orbot
- Termux : https://github.com/termux/termux-app · App Manager : https://github.com/MuntashirAkon/AppManager · Shizuku : https://github.com/RikkaApps/Shizuku
- Organic Maps : https://github.com/organicmaps/organicmaps
- Obtainium : https://github.com/ImranR98/Obtainium

> La Bandita rapporte à partir de sources datées. Une boîte de métier ne se gonfle pas : elle s'aiguise.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : AppManager ★8 985 et OrganicMaps ★15 427 avec push d'AUJOURD'HUI ; Calendar ★2 156, Clock ★698. Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
