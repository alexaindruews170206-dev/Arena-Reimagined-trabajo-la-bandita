# Publicación 06 — Forks de lecteurs : la carte vivante de Mihon, Aniyomi et leurs secondes générations

**La Bandita · 15 de septiembre de 2026 · édition française (adaptée de l'original espagnol, pièce 06)**

## 🗺️ Carte de ce guide

├── ⚡ En une page
├── ⚖️ La règle : fork n'est pas critère
├── 🌳 L'arbre complet d'aujourd'hui
├── 📱 Les fiches des vivants
├── 🧬 Ce qu'est un « fork de vrai » (et ce qu'est un second fils)
├── 🏗️ L'infrastructure que personne ne voit
├── 📜 Licences, dit sans avocat
├── 🚩 Signes d'imposteur
├── 🔍 Comment lire un dépôt en dix minutes
├── 🔄 Sauvegardes et déménagements de bibliothèque
├── ❓ Questions fréquentes
└── 🔗 Liens

## ⚡ En une page

Tachiyomi — le lecteur de mangas libre qui marqua une époque — ferma son noyau en janvier 2024. Ce qui resta n'est pas « Tachiyomi avec un autre nom » : c'est une famille de projets distincts, avec propriétaires, rythmes et licences propres. Cette carte se lut AUJOURD'HUI, 14 septembre, dépôt par dépôt :

```
━━ Le tronc mangas ━━
Mihon              ★23 601   v0.20.4 (5-aoû)    push AUJOURD'HUI (15-sep)
TachiyomiSY        ★4 146    1.13.2 (13-juil)   push 13-sep    fork
TachiyomiSYPreview ★483      hôte de previews   push 25-aoû
Komikku            ★4 721    v1.14.1 (17-juil)  push 11-sep  second fils
Neko               ★2 792    lecteur MangaDex   push 14-sep     spécialiste

━━ La branche anime (mangas + anime) ━━
Aniyomi            ★7 683    push 14-sep         branche mère
Anikku             ★1 032    v0.2.0 (11-sep)    anime, org Komikku
Aniyomi-preview    ★641      hôte de previews   push 14-sep
Animetail          ★579      v0.20.4.0 (5-aoû)  push 7-sep   fork
Tadami             ★260      v0.62 (12-sep)     push 13-sep  fork (vivante)

```

Aucune étoile n'installe rien. Aucun parenté ne garantit rien. La règle va d'abord.

## ⚖️ La règle : fork n'est pas critère

Que quelque chose soit fork, variante ou rebaptisé d'un projet aimé n'est pas, par soi seul, raison pour l'utiliser. Les quatre portes qui comptent, elles :

```
Usage réel        quelqu'un de chair et d'os l'utilise
                  et peut raconter comment ça va
Unicité           fait-il quelque chose que ce que tu as
                  déjà ne couvre pas ? « C'est un fork de X »
                  n'est pas une fonction
Maturité publique docs, versions signées, un auteur
                  qui répond. Un dernier push de 2024
                  ne passe pas cette porte sans marque
Propre dessein    une icône neuve n'est pas un dessein ;
                  un changement de moteur, oui
```

Ce guide nomme des dépôts avec URL, licence, version et dernier push — lus le 14 et relus au déménagement (15-sep). « Le meilleur » n'apparaît pas : il n'existe pas en abstrait. Existe celui qui couvre ce que tu lis, avec atelier ouvert.

## 🌳 L'arbre complet d'aujourd'hui

```
Mihon (le tronc vivant de l'écosystème)
   ├── Mihon            le successeur de fait (le plus grand)
   ├── TachiyomiSY      le fork classique qui reste vivant
   ├── Komikku          second fils avec vie propre (dépôt neuf)
   ├── Neko             le spécialiste de MangaDex
   └── (dizaines de forks sans projet propre :
        non listés pour être des forks)

Aniyomi (mangas + anime, de la même lignée)
   ├── Animetail        se déclare « Official fork »
   ├── Tadami           mangas + anime + ranobe (le plus jeune)
   └── Anikku           le client-anime de l'org Komikku

Kotatsu : AUTRE arbre (GPL, parsers propres)
   → Kotatsu-Redo, Futon, Kototoro, Usagi
   → ont leur propre guide dans cette famille
```

## 📱 Les fiches des vivants

### Mihon — le tronc

https://github.com/mihonapp/mihon

★23 601 · version 0.20.4 (5 août) · push d'AUJOURD'HUI (re-vérifié 15-sep) · Apache-2.0. C'est le lecteur de mangas libre le plus grand de la carte, et le successeur de fait de Tachiyomi. Sa communauté de traductions pousse du code chaque jour ; ses versions sortent quand elles sortent — celle d'août est la vigente, et le push d'aujourd'hui ne signifie pas APK neuf.

Keiyoushi (le guide d'extensions de cette famille) le nomme premier dans sa liste d'apps compatibles.

### TachiyomiSY — le vivant au vieux nom

https://github.com/jobobby04/TachiyomiSY

★4 146 · version 1.13.2 (13 juillet) · push du 13-sep · Apache-2.0. Le fork classique — sources extra, réglages de lecture — qui reste ouvert. Et l'avis qui vaut son entrée : le SY vivant est celui-ci — le nom ne suffit pas ; le propriétaire oui.

Son projet mère maintient en plus un hôte de builds d'essai : TachiyomiSYPreview (★483) — versions expérimentales pour curieux, pas la voie du quotidien.

### Komikku — le second fils à atelier propre

https://github.com/komikku-app/komikku

★4 721 · version 1.14.1 (17 juillet) · push du 11-sep · Apache-2.0. L'API de GitHub ne le déclare pas fork (c'est un dépôt neuf) ; son README raconte la lignée. Ce sont les « seconds fils » : projets qui héritent le code et naissent avec leur propre maison. Son organisation maintient aussi Anikku (plus bas).

### Neko — le spécialiste

https://github.com/nekomangaorg/Neko

★2 792 · push d'hier (14-sep) · « Unofficial MangaDex Reader for Android 8+ ». Un lecteur entier dédié à une seule source : MangaDex. Il est de la lignée des forks de Tachiyomi, mais son dessein propre est clairnet : faire une chose bien. Pour qui vit dans MangaDex, c'est fiche à part ; pour le reste, c'est un marteau en forme de tournevis.

### Aniyomi et ses héritiers

https://github.com/aniyomiorg/aniyomi

★7 683 · push du 14-sep · Apache-2.0. La branche mère du mangas+anime. Presque un an sans version neuve mais avec du code bougeant ce mois-ci : branche mûre, pas cadavre. Son hôte de previews : aniyomiorg/aniyomi-preview (★641).

**Anikku** — https://github.com/komikku-app/anikku — ★1 032 · version 0.2.0 publiée le 11 septembre · release r8932 à vue AUJOURD'HUI 15-sep · « anime watcher » de l'organisation Komikku. La plus active de la branche anime ce mois-ci.

**Animetail** — https://github.com/Animetailapp/Animetail — ★579 · v0.20.4.0 · push du 7-sep · Apache-2.0. Se déclare « Official fork of Aniyomi » dans sa description. L'étiquette, c'est lui qui la met — on n'a pas vu de sceau d'aniyomiorg le ratifiant ; dit tel quel.

**Tadami** — https://github.com/andarcanum/Tadami-Aniyomi-fork — ★260 · version 0.62 (12 septembre) · push du 13-sep · Apache-2.0. **Rectification (15-sep, soir) : VIVANTE — ★260, push du 13-sep ; le PV de l'après-midi s'était trompé de maison (détail dans la Publicación 13).** La plus jeune de la branche : trois versions en un mois (0.60 → 0.62), mangas + anime + romans légers (ranobe). Des forks déclarés, celui qui évolue le plus vite.

## 🈁 La couche d'immersion (guide propre dans la pièce 17)

La carte d'aujourd'hui inaugure du territoire : deux projets vivants de la couche japonaise de l'écosystème. **Chimahon** (★198, GPL-3.0, v2.4.2 d'AUJOURD'HUI 15-sep) est un fork de Mihon pour étudier en lisant : dictionnaire natif Yomitan, mangas Mokuro, romans EPUB et minage instantané vers Anki. **Yomi Reader** (★10, Apache-2.0, v0.1.7 du 6-sep) est le triple jeune — anime, mangas et roman — compatible avec les extensions Tadami/Aniyomi. Les fiches complètes, avec Hoshi Reader, Yomikai et le client Komga « Koharia », vivent dans la pièce 17.

## 🧬 Ce qu'est un « fork de vrai » (et ce qu'est un second fils)

Le graphe de GitHub et la réalité ne coïncident pas toujours :

```
Fork déclaré      l'API le dit : champ fork = true,
                  avec père visible. Animetail, Tadami. On ne discute pas.

Second fils       dépôt NEUF qui hérite le code et déclare
                  la lignée dans son README. Mihon, Komikku,
                  Anikku. Le graphe dit « ce n'est pas un fork » ;
                  le README dit d'où il vient. Les deux
                  sont vrais : c'est pour ça qu'on lit les deux.

Hôte de builds    ce n'est pas une app : c'est un appareil de
                  lancement de versions d'essai du projet mère.
                  SYPreview, aniyomi-preview.

Fork de fork      ce qui monte le contre-exemple : copie d'une
                  copie sans atelier propre. Meurt d'ordinaire
                  sans le dire.
```

Quand quelqu'un te recommande « un fork », la question utile n'est pas de qui est-il fils ? mais qui pousse du code cette semaine ?

## 🏗️ L'infrastructure que personne ne voit

Deux pièces de l'écosystème ne sont pas des lecteurs mais soutiennent tous :

**SyncYomi** — https://github.com/syncyomi/syncyomi — ★710, push d'hier (14-sep) · v1.5.4 (10-sep). Synchronisation de bibliothèques entre appareils et entre forks de la lignée Tachiyomi : ta progression te suit si tu changes de lecteur de la famille. Un serveur léger et le client dans le téléphone.

**Suwayomi** — le serveur de bureau de l'écosystème (ta bibliothèque tournant sur le PC, lue depuis le navigateur). Son extension fut révisée dans le guide d'extensions de cette famille ; le projet vit avec activité de ce mois-ci.

Les nommer ici, c'est éviter l'erreur classique : confondre l'app avec la couche qui l'accompagne.

## 📜 Licences, dit sans avocat

Ce que la page de chaque dépôt déclara le jour de la vérification (14-sep) :

- **Apache-2.0** — Mihon, TachiyomiSY, Komikku, Aniyomi, Animetail, Tadami. En termes généraux : utiliser, modifier et redistribuer en conservant les avis et la note de changements.
- **GPL-3.0** — l'arbre Kotatsu (Kotatsu-Redo, Futon, Usagi, Kototoro en sa licence déclarée). Qui redistribue des modifications, les distribue avec la même licence.

Ceci n'est pas du conseil légal : c'est le champ de licence de chaque page, lu aujourd'hui. Si quelqu'un va redistribuer un APK avec modifications, qu'il ouvre le texte complet de la licence ce jour-là. Et un avis qui vaut de l'or : un APK « SY mod premium » dans une boutique de mods N'hérite pas la confiance d'Apache-2.0 du dépôt — il hérite celle de la boutique.

## 🚩 Signes d'imposteur

- Étoiles hautes, dernier commit de 2024, README qui promet « active development ».
- Même nom, autre propriétaire — et les imposteurs de SEO de cette semaine (titres d'annonce, étoiles cloniques).
- APK sur Telegram « plus à jour que GitHub ». L'à-jour vit dans Releases, avec tag et date.
- « Nightly » sans CI, sans tag, sans registre de compilation.
- Fork d'un projet archivé qui ne déclare pas son parenté.
- Il demande de coller un index d'extensions au premier écran.

Aucun signe seul ne suffit. Plusieurs ensemble, tu restes debout.

## 🔍 Comment lire un dépôt en dix minutes

```
1. Ouvre le HTML du dépôt, pas un découpé d'un groupe.
2. Dit-il Archived ? Les morts se lisent aussi vite.
3. Licence : le champ de la page (ou le fichier LICENSE).
4. Releases : tag et date de la dernière version.
   Le push d'aujourd'hui n'est pas une version neuve.
5. pushed_at ≠ release : un dépôt peut pousser
   des traductions tout le mois sans sortir d'APK.
6. Est-ce un fork ? Le champ fork de la page/de l'API le dit ;
   si c'est un second fils, le README le raconte.
7. L'auteur répond-il aux issues ? Regarde-le dans deux fils
   au hasard avant de lui fier ta bibliothèque.
```

## 🔄 Sauvegardes et déménagements de bibliothèque

Ce qu'on peut dire sans rien prescrire :

- Chaque lecteur de la famille a son format de sauvegarde ; les formats se ressemblent, pas de garantie qu'ils soient égaux entre versions ni entre cousins.
- Une sauvegarde de 2024 n'est pas vérifiée contre la version d'août 2026 — d'aucun lecteur.
- « Tu exportes et voilà » est une promesse de publicité, pas d'ingénierie : essaie TOUJOURS en copie, jamais sur ta seule bibliothèque.
- Si ta progression t'importe, SyncYomi (en haut) existe pour ça — et se sauvegarde aussi en sauvegardant : exportation manuelle périodique.
- L'épisode des sauvegardes de Kototoro (série 1.4–1.7) est documenté dans son propre guide ; il vaut comme rappel que les migrations grandes s'essayent à vide.

## ❓ Questions fréquentes

**Lequel j'installe ?**
Celui que tu utilises et vérifies. Mangas en général : Mihon est le tronc avec le plus de communauté. Style classique SY avec extras : TachiyomiSY de jobobby04. MangaDex exclusivement : Neko. L'anime en plus des mangas : Aniyomi ou ses héritiers (Anikku est celle qui bougea le plus ce mois-ci). Aucune recommandation ne substitue d'ouvrir la release le jour où tu installes.

**Mihon est-il Tachiyomi ?**
Non. Tachiyomi a fermé. Mihon est un autre dépôt, vivant aujourd'hui, qui hérita le modèle.

**Komikku ou TachiyomiSY ?**
Deux vivants au style distinct. Aujourd'hui Komikku a plus d'étoiles (4 721 vs 4 146) ; SY poussa le 13-sep et Komikku le 11 — constances du 14, tous vivants au 15. Aucun nombre ne choisit pour toi.

**Anikku est-elle AniZen ?**
Non — mais c'est de la famille. AniZen se déclare rebrand de « Anikku Mod » (a son propre guide dans cette famille). Anikku est l'app de l'organisation Komikku, avec version 0.2.0 du 11 septembre. Parentèle déclarée, dépôts distincts.

**Neko sert pour tout ?**
Pour MangaDex, à merveille. Pour le reste de l'univers mangas, utilise un lecteur général.

**Les hôtes de « preview » sont pour installer ?**
Ils sont pour essayer et rapporter. Pour le quotidien, la version stable du dépôt mère.

**Et les 200 forks que tu n'as pas listés ?**
Être fork ne marque pas des points. Ceux avec projet propre sont en haut ; ceux sans, sont des copies à horloge.

**Discord ?**
Cette famille n'a pas de canal d'envoi par Discord. Ses guides vivent ici.

## 🔗 Liens

- Mihon : https://github.com/mihonapp/mihon
- TachiyomiSY : https://github.com/jobobby04/TachiyomiSY · previews : https://github.com/jobobby04/TachiyomiSYPreview
- Komikku : https://github.com/komikku-app/komikku · Anikku : https://github.com/komikku-app/anikku
- Neko : https://github.com/nekomangaorg/Neko
- Aniyomi : https://github.com/aniyomiorg/aniyomi · previews : https://github.com/aniyomiorg/aniyomi-preview
- Animetail : https://github.com/Animetailapp/Animetail · Tadami : https://github.com/andarcanum/Tadami-Aniyomi-fork
- SyncYomi : https://github.com/syncyomi/syncyomi
- Extensions de l'écosystème : guide 04 de cette famille · Arbre Kotatsu : guide 07

> La Bandita rapporte à partir de sources datées. Un fork n'est pas une raison. Le dépôt vivant oui. Et le propriétaire, plus.

---

**Note de déménagement (15-sep) :** guide passé de la fournée du 14 à celle-ci, avec re-vérification contre les maisons : 8 fiches re-comptées (Mihon ★23 601, Komikku ★4 721, SY ★4 146, Neko ★2 792, Anikku ★1 032 + r8932) et rectification Tadami (vivante). Ce qui n'est pas mentionné reste constaté à son jour (14-sep). PV complet : Registre #71.
