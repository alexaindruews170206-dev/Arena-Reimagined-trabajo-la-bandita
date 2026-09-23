# Publicación — Extensiones Mihon / Aniyomi / Animetail (La Bandita) · 2026-09-13
> BORRADOR · WhatsApp / La Bandita · no Discord. No Facebook (límite ~40k).
> POST: un solo mensaje. Copia desde APPS Y EXTENSIONES hasta los hashtags.
> Pedido: lista completa, tope 63.000. Facebook = recorte 40k.
> COMENTARIO FIJADO: bloque del final. No publicar sin firma humana.
> Corte vivo: 2026-09-13. El texto de origen traía corte 2026-07-25; se verifica, no se recita.

APPS Y EXTENSIONES (MIHON, ANIYOMI, TADAMI, MIYOMI) · La Bandita · 2026-09-13 (BORRADOR · firma humana pendiente)
**Tiempo estimado de lectura: 50–65 min**
**Índice:** mapa + el mismo icono en cada título. Resumen en el comentario fijado.

# Mapa de apps y extensiones: Mihon, Aniyomi, Tadami, Miyomi y lo que el directorio no lista

**Corte de información:** 2026-09-13
**Clase predominante:** [Fuente] (GitHub API y páginas de proyecto abiertas hoy) y [Observación]. Sin instalar ninguna app ni ninguna extensión en un teléfono.
**Grado:** V2 parcial — repos y sitios de Keiyoushi, Yūzōnō, FelipeGFA, Kohi-den, Mihon, Aniyomi, Animetail, Komikku, TachiyomiSY, Miyomi, Tadami y MANGA Plus abiertos hoy. Wotaku.wiki (ficha a ficha) y Discord de Keiyoushi: no.
**Receptor:** La Bandita (WhatsApp). Lista completa. No va al ledger. No Discord.
**No es:** un tutorial para añadir repositorios de fuentes no licenciadas, ni un veredicto de si «conviene» usarlas, ni asesoría legal.

**Etiquetas:**
`[Fuente]` = lo que el proyecto declara en página o API abierta hoy.
`[Observación]` = lo visto en esta sesión (2026-09-13).
`[Inferencia]` = deducción marcada.
`[Reporte externo]` = medios; no se abrió cada página citada.
`[No confirmado]` = no se pudo verificar al corte.
`[No encontrado]` = se buscó con método y no apareció; no es «no existe».

```
Mapa de esta guía. El mismo icono abre cada bloque.
Índice corto: primer comentario (fijado).

├── ⚡  Resumen: qué estaba mal el 25-jul
├── 📜  De dónde sale este ecosistema
├── 📱  Las apps, con números de hoy
├── 🗺️  Repositorios (estado, no receta)
├── 🧬  HttpSource, KeiSource 1.6 y el PR #448
├── 🔞  «Cursed» / NSFW (se nombra, no se enlaza el índice)
├── 🗂️  Miyomi: el directorio (133 apps / 44 ext)
├── 📱  Mapa de apps (catálogo Miyomi)
├── 🧩  Mapa de extensiones (44)
├── 🌒  Lo que Alexis mandó y no estaba
├── 🚪  Cómo leer este mapa
├── 🐋  Tadami (manga + anime + novela)
├── 🔎  Fuera de Miyomi (GitHub hoy)
├── 🧵  Capas: app / almacén / código / parser / índice
├── 🔭  Poco nombrados (calidad, no fama)
├── 🧭  Cómo se lee «calidad»
├── 📋  Inventario de la exploración
├── 🛠️  Si algo se rompe (sin receta de fuentes)
├── 🌱  Vías oficiales abiertas hoy
├── 📌  Correcciones al corte 25-jul-2026
├── 🚧  Límites
├── ✅  Acciones concretas
└── 📚  Fuentes abiertas hoy
```

> La Bandita informa a partir de fuentes fechadas. Un repo público en GitHub no es una invitación a usarlo. Esta guía no pega índices de instalación.

---

## ⚡ Resumen: qué estaba mal el 25-jul

El texto que llegó (corte 25-jul-2026, «versión ampliada y verificada») mezclaba tres cosas que hay que separar:

```
1. Hechos de GitHub que se pueden recontar hoy
   (estrellas, archivado, último push, si el repo es público).

2. Relatos de julio que ya no coinciden
   (Yūzōnō «privado», índice de anime «caído»,
   Kohi-den «842 ★», KeiSource 1.6 «no existe»).

3. Recetas de instalación (URL de index.min.json / index.pb
   para pegar en la app). Eso no se copia aquí.
   [Observación] Misma lógica que la guía de tiendas APK:
   se nombra para informar; no se facilita la descarga.
```

Lo que sí se sostiene, reabierto hoy:

```
Tachiyomi cerró el núcleo en enero de 2024 tras presión
legal de Kakao Entertainment. [Reporte externo — Anime Corner
14-ene-2024, AlternativeTo 15-ene-2024]

Mihon, Aniyomi, Animetail, Komikku y TachiyomiSY siguen
con repos públicos. [Fuente — GitHub API, 13-sep-2026]

Keiyoushi/extensions es el almacén de extensiones más
grande visto hoy (14.963 ★). Último push: 12-sep-2026.
[Fuente]

Kohi-den/extensions-source está archivado desde el
14-may-2026. [Fuente]

KeiSource con libVersion 1.6 sí aparece en documentación
de contribución (Yūzōnō, commit 12-sep-2026) y en el
título del PR #448 de Animetail. [Fuente]
El corte de julio decía que no existía. Eso está mal.
```

Esta guía no instala nada. No se ejecutó Mihon. No se añadió ningún «extension store». [Observación]

---

## 📜 De dónde sale este ecosistema

Tachiyomi (2015–2024) era un lector de manga FOSS para Android. El modelo: la app no aloja capítulos; las «extensiones» hablan con sitios ajenos. [Reporte externo / Inferencia] En enero de 2024 el núcleo dejó de desarrollarse por amenazas de Kakao Entertainment Corp. AlternativeTo (15-ene-2024): cierre de repos, cuentas y Discord reconvertido. Anime Corner (14-ene-2024) sitúa el cese y desista a principios de enero. [Reporte externo] El anuncio original de Tachiyomi y la carta de Kakao no se reabrieron hoy. [No confirmado el texto primario]

«Millones de descargas» del corte de julio: no salió en las páginas abiertas hoy. Fuera. [No confirmado]

Después del cierre aparecieron forks. Los que esta sesión pudo contar en GitHub:

```
Mihon (mihonapp/mihon)
  «Free and open source manga reader for Android»
  Apache-2.0. 23.556 ★. Última release etiquetada:
  v0.20.4 (5-ago-2026). Push 12-sep-2026. [Fuente]

Aniyomi (aniyomiorg/aniyomi)
  «An app for manga and anime». Apache-2.0. 7.678 ★.
  Última release etiquetada: v0.18.1.2 (28-oct-2025).
  Push de código: 4-sep-2026. [Fuente]
  Release vieja ≠ repo muerto. Tampoco se afirma que
  v0.18.1.2 sea «la que hay que usar». [Observación]

Animetail (Animetailapp/Animetail)
  Fork de aniyomiorg/aniyomi. Descripción: «Official
  fork of Aniyomi». 579 ★. Release v0.20.4.0 (5-ago-2026).
  Push 7-sep-2026. [Fuente]

Komikku (komikku-app/komikku)
  4.711 ★. Release v1.14.1 (17-jul-2026).
  Push 11-sep-2026. [Fuente]

TachiyomiSY (jobobby04/TachiyomiSY)
  4.143 ★. Release 1.13.2 (13-jul-2026).
  Push 13-sep-2026. [Fuente]
```

Keiyoushi, en su portada (https://keiyoushi.github.io, abierta hoy), dice qué apps soporta para su almacén de extensiones:

```
«Keiyoushi only supports the following Android apps,
anything else isn't supported so if it doesn't work,
you are on your own:

Mihon, TachiyomiSY and Komikku.»
[Fuente — https://keiyoushi.github.io]
```

Getting started de Keiyoushi (hoy): hace falta **Mihon 0.20.4 o más nuevo** para el botón de añadir el store. [Fuente] Aniyomi y Animetail **no** están en esa lista de soporte. El corte de julio los trataba como el mismo circuito. No lo son, según Keiyoushi. [Observación]

La zona legal: la app FOSS no es lo mismo que las fuentes que una extensión consulta. Kakao no compró ese argumento en 2024. [Reporte externo] Esta guía no dice «es legal porque no aloja». Eso sería un dictamen. No lo hay.

---

## 📱 Las apps, con números de hoy

Sin tabla. Una ficha por línea. Estrellas = GitHub API, 13-sep-2026. No se descargó ningún APK. [Observación]

```
Mihon          23.556 ★   v0.20.4     5-ago-2026
               Lector manga FOSS. Keiyoushi lo nombra primero.

TachiyomiSY     4.143 ★   1.13.2     13-jul-2026
               Fork. Keiyoushi lo nombra.

Komikku         4.711 ★   v1.14.1    17-jul-2026
               Fork. Keiyoushi lo nombra.

Aniyomi         7.678 ★   v0.18.1.2  28-oct-2025 (tag)
               Manga + anime. Keiyoushi: no soportado.

Animetail         579 ★   v0.20.4.0   5-ago-2026
               Fork de Aniyomi. Mismo día que Mihon 0.20.4
               (PR #461 «Merge-mihon», Dark25). [Fuente]
               Keiyoushi: no está en la lista de soporte.
```

Animetail v0.20.4.0 publica checksums SHA-256 por ABI en GitHub Releases. No se recitan aquí: no se va a verificar un APK. [Observación]

«Animetail es el sucesor espiritual de Tachiyomi»: no. Mihon es el que la prensa y la comunidad suelen nombrar como sucesor del lector; Animetail se declara fork de Aniyomi. [Observación / Inferencia] El corte de julio ponía a Mihon, Aniyomi y Animetail al mismo nivel de «el ecosistema». El mapa de soporte de Keiyoushi no lo hace.

---

## 🗺️ Repositorios (estado, no receta)

Advertencia de esta sección: describir que un repo existe no es decir «añádelo». Los índices (index.min.json, index.pb) son precisamente el gancho de instalación. **No se pegan.** Quien quiera el índice, que lo lea en el README del proyecto el día que lo lea, no en este post. [Observación]

Se comprobó, con HEAD/GET, si algunas URLs de índice **responden**. Eso es existencia de un archivo, no un aval. [Observación]

### 📗 Keiyoushi

Dos repos, no uno.

https://github.com/keiyoushi/extensions
  Almacén (binarios / índice). 14.963 ★. 1.316 forks.
  Rama por defecto: repo. Público. No archivado.
  Último commit visto: keiyoushi-bot, «Update extensions
  repo», 12-sep-2026 (a7dd81d).
  Homepage: https://keiyoushi.github.io/
  README (hoy): índice en formato index.pb (no el
  index.min.json que recitaba el corte de julio como
  receta principal).
  [Fuente / Observación]

https://github.com/keiyoushi/extensions-source
  Código fuente. 4.669 ★. 1.647 forks. Apache-2.0.
  Rama main. 6.498 commits. Push 13-sep-2026
  (AwkwardPeak7). [Fuente]

Sitio https://keiyoushi.github.io (hoy): «Extension store for Mihon and variants.» Aviso de lista vacía / «Outdated app» / extensiones obsolete: la app ya no es compatible. Soporta Mihon, TachiyomiSY, Komikku. Getting started pide desinstalar extensiones viejas antes de añadir el store, y Mihon 0.20.4+. [Fuente]

CDN jsDelivr (`cdn.jsdelivr.net/gh/keiyoushi/extensions@repo/…`): HEAD 200 hoy. [Observación] El corte de julio lo daba como espejo «con latencia». Latencia no se midió. [No confirmado]

HTTP 429 en Filipinas/India, «equipo Keiyoushi y Miyomi»: no estaba en la guía de troubleshooting de Keiyoushi abierta hoy. Miyomi.app no se abrió. Queda [No confirmado]. No se recita como hecho.

Licencia «Apache 2.0 o MIT según cada extensión»: el source repo declara Apache-2.0. El repo `extensions` no trae licencia en la API. MIT no se vio como declaración global. [Observación] No se afirma MIT.

### 📘 Yūzōnō

El corte de julio: 319 ★, «gran agregador», índice de anime caído, repo principal privado, fusión automática con Keiyoushi cada 6 horas.

Hoy, org github.com/yuzono, **pública**, 8 repos visibles. [Observación]

```
https://github.com/yuzono/tachiyomi-extensions
  Código. 887 ★. Apache-2.0. Push 13-sep-2026.
  «Source code of extensions for Komikku / Mihon & forks.»
  CONTRIBUTING.md tocado 12-sep-2026
  («Fix outdated/contradictory claims»). [Fuente]

https://github.com/yuzono/anime-extensions
  426 ★. Apache-2.0. Push 13-sep-2026 (hoy). [Fuente]
  El corte de julio decía el índice de anime «caído».
  El repo de distribución yuzono/anime-repo (59 ★)
  se empujó hoy 13-sep-2026 17:38 UTC. Un GET al
  index.min.json de ese repo respondió 200.
  [Observación] «Caído» en julio no se sostiene hoy.

https://github.com/yuzono/manga-repo
  Fork de keiyoushi/extensions. 4 ★. Push 18-ago-2026.
  Archivos vistos: README, index.json, index.min.json,
  repo.json. index.pb: 404. [Observación]
  El corte de julio daba un index.pb de manga-repo
  como «el que debes usar». Ese path no está.

https://github.com/yuzono/https://yuzono.github.io
  18 ★. Fork de keiyoushi/https://keiyoushi.github.io.
  Push 7-sep-2026. Sitio abierto hoy:
  «Extension repository for Mihon, Aniyomi and variants»
  con entradas Manga y Anime. [Fuente]

https://github.com/yuzono/aniyomi-extensions
  La API de GitHub devolvió HTTP 451 en esta sesión.
  No se afirma el interior del repo. [Observación]

https://github.com/yuzono/kohi-den
  Fork de Kohi-den/extensions-source. 3 ★.
  Push 12-may-2026 (antes del archivo del original).
  [Fuente]
```

«Privado en GitHub»: no, al corte. [Observación] «Cada 6 horas fusiona Keiyoushi»: no salió en las páginas abiertas. [No confirmado]

### 📙 FelipeGFA (pt-br)

```
https://github.com/FelipeGFA/extensoes
  Fork de keiyoushi/extensions. 41 ★ (el corte decía 35).
  «mainly focus on pt-br updates». Push 13-sep-2026.
  Índice index.min.json: HEAD 200. [Fuente / Observación]

https://github.com/FelipeGFA/anime-extensoes
  5 ★. Push 30-jul-2026. Índice: HEAD 200, cuerpo largo
  (~77 kB). [Observación] Más viejo que el de manga.

https://github.com/FelipeGFA/anime-fonte-extensoes
  4 ★. Apache-2.0. Push 17-ago-2026. Código. [Fuente]

https://github.com/FelipeGFA/fonte-extensoes
  1 ★. Push 13-sep-2026. Descripción: source de
  keiyoushi/extensions. [Fuente]
```

El corte de julio mandaba a instalar anime-fonte-extensoes con la URL de yuzono/anime-repo. Eso mezcla proyectos. No se receta. [Observación]

### 📕 Kohi-den

```
https://github.com/Kohi-den/extensions-source
  Public archive. Archivado por el owner el 14-may-2026.
  532 ★ (el corte decía 842). 149 forks. Apache-2.0.
  Último commit: 12-may-2026, SyntexErr0r, PR #1343.
  [Fuente]

Índice que el README histórico pegaba en kohiden.xyz:
  TLS error en esta sesión. No se afirma el contenido.
  [Observación / No confirmado]
```

«DMCA» como causa del índice: el archivo del 14-may está confirmado; el motivo DMCA no salió en la página del repo. [No confirmado] El corte de julio lo daba por DMCA.

### 📓 Otros

Repos esporádicos: no se recorre un censo. «La Ballenita recomienda» del corte de julio no es voz de esta guía.

---

## 🧬 HttpSource, KeiSource 1.6 y el PR #448

El corte de julio dedicaba páginas a una clase Kotlin `HttpSource` (fetchPopularManga, fetchChapterList, Jsoup, etc.) y luego juraba que «KeiSource 1.6 no existe» y que el PR #448 «no es una migración de API».

Hoy:

**HttpSource.** Sigue siendo el nombre de la clase base clásica de Tachiyomi/Mihon. No se copia aquí un esqueleto de scraper. [Observación] Escribir ese esqueleto sería receta. No se hace.

**KeiSource 1.6.** Existe como convención de contribuidor. El CONTRIBUTING.md de yuzono/tachiyomi-extensions (1.813 líneas; se leyó el encabezado y el snippet) coincide: fuentes nuevas deben extender `KeiSource` con `libVersion = "1.6"`; `HttpSource` directo queda como legado (`libVersion = "1.4"`). El propio CONTRIBUTING se corrigió el 12-sep-2026 («Fix outdated/contradictory claims», #19013). [Fuente] No se afirma que todas las extensiones de Keiyoushi ya estén en 1.6. [No confirmado el censo]

keiyoushi/extensions-source, commit del 12-sep: «MangaParkPublisher: 1.6» (#19016). [Fuente] Eso no prueba un producto comercial llamado «KeiSource 1.6»; prueba que «1.6» circula en el código.

**PR #448 de Animetail.** API de GitHub, hoy:

```
Repo:     Animetailapp/Animetail
Título:   fix(extensions): resolve 1.6+ extension loading
          and chapter memo persistence
Autor:    Dark25
Estado:   merged
Fecha:    2026-07-22T22:19:37Z
Cierra:   #444
[Fuente — API]
```

El cuerpo del PR (parafraseado, no es un parche para aplicar): restaura la interfaz Source; ClassLoader ChildFirstPathClassLoader delega paquetes source/network/injekt/keiyoushi al padre; prioriza METADATA_SOURCE_FACTORY (fábricas KSP); añade getMangaUpdate; conserva «memo» de manga/capítulo en SQLDelight. [Fuente]

El corte de julio acertó la fecha (22-jul-2026) y el autor. Se equivocó al decir que no tenía que ver con 1.6: **el título del PR es 1.6+**. [Observación] Tampoco es «la migración masiva a KeiSource 1.6» como relato único del ecosistema: es un fix de carga de extensiones 1.6+ **en Animetail**. Mihon 0.20.4 salió el 5-ago-2026; Animetail v0.20.4.0 el mismo día, con «Merge-mihon» (#461). [Fuente]

No se compiló el PR. No se reprodujo un crash de ClassLoader. [Observación]

---

## 🔞 «Cursed» / NSFW (se nombra, no se enlaza el índice)

En esta jerga, «cursed» = contenido explícito. No hace falta para que un lector funcione. El corte de julio pegaba índices. Aquí no.

Repos vistos hoy (nombre y estado; sin URL de índice):

```
https://github.com/yuzono/cursed-manga-extensions
  Código. 185 ★. Apache-2.0. Push 9-sep-2026. [Fuente]

https://github.com/yuzono/cursed-manga-repo
  Distribución. 158 ★. Push 3-ago-2026.
  Un GET al index.min.json respondió 200.
  [Observación] El corte decía el índice de Yūzōnō
  cursed «caído». Hoy el archivo responde.

https://github.com/mojuru/cursed-manga-repo
  158 ★. Push 3-ago-2026. Mismo orden de magnitud.
  GET al índice: 200. [Observación]
  El corte decía índice caído. Hoy no.
```

No se recomienda añadirlos. No se enlazan. Si aparecen en una búsqueda de GitHub, ya sabes qué son. [Observación]

Riesgo de malware «mayor» en cursed: no se escaneó ningún APK. Queda como [Inferencia] del corte viejo, no como medida nuestra.

---

## 🗂️ Miyomi: el directorio (no es un repo de extensiones)

Miyomi no es Mihon. Es un **directorio web** de apps, repos de extensiones y guías. Sitio abierto hoy: https://miyomi.app/ — «Your one-stop hub for apps, extensions and more!» Cuenta en portada: 133+ software, 44+ extensions, 24+ guides. [Fuente / Observación]

```
GitHub   miyomiorg/Miyomi
         (tas33n/Miyomi redirige al mismo)
         189 ★. 18 forks. AGPL-3.0.
         Push 31-ago-2026. Preview pública.
         [Fuente — API 13-sep-2026]

Catálogo 133 apps + 44 extensiones, todas
         status=approved en la API pública
         que el propio front usa.
         [Observación]

Licencia AGPL-3.0. Marca «Miyomi» reservada
         (README). [Fuente]
```

El README (hoy): directorio mantenido por la comunidad; no alojan contenido; no garantizan seguridad ni legalidad de terceros; descargar siempre desde la fuente verificada. [Fuente]

Esta guía **no reproduce** claves de API ni `auto_url` / índices de instalación. El catálogo se leyó por la misma vía que el sitio. Pegar esa vía en Facebook sería receta. No se pega. [Observación]

Miyomi tiene Discord y Telegram en el README. No se enlazan (no Discord). [Observación]

Un ítem «approved» en Miyomi **no** es un aval de La Bandita. Es «está en su directorio hoy».

---

## 📱 Mapa de apps (133, catálogo Miyomi 13-sep)

Nombres del directorio. Plataforma entre paréntesis si no es solo Android. No se pegan APKs ni checksums. Agrupado por el primer tipo que Miyomi declara. [Fuente — catálogo]

**Manga (y mezclas)** — 82

Aidoku (iOS/macOS/iPadOS) · AniLabX (+anime, LN) · Animetail (+anime) · Animite (+LN, anime) · Aniyomi (+anime) · AnymeX (multiplataforma; +anime, LN) · Atahon · CDisplayEx · chimahon (+LN, anime) · ComicRack CE (Windows) · Dantotsu (+anime) · Dartotsu (multiplataforma; +anime, LN) · DropSauce (+LN) · Emaki (+LN) · Foxlations (iOS/Android/Windows; +anime, LN) · Frank Yomik · FMD2 (Windows; +comics, webtoon) · Futon · harbor (Windows; +anime) · hayai (+LN) · Houdoku (escritorio) · JHenTai (multiplataforma) · Kaisoku · kaizen-app (+anime, webtoon, comics, LN) · koeyomi · koharu (Linux/Windows) · KomaStream (+comics, LN) · Komga (escritorio; +comics, ebooks) · Komikku · KOReader (+LN) · Kotatsu · Kotatsu Redo · Kotatsu-Next · Kototoro (+anime, LN) · Kumo · Kuro Reader + · Manga You Know (escritorio) · MangaPin (multiplataforma) · Mangayomi (multiplataforma; +LN, anime) · Mihon · MIYO · Moku (escritorio; +LN, anime) · Neko · Nekoyomi (+anime, LN) · NHApp · Nyora (multiplataforma) · OpenComic (escritorio) · OtakuWorld (+anime) · Panels (iOS) · Paperback (iOS) · Perfect Viewer · PlayTorrio (multiplataforma; +anime) · Readest (multiplataforma; +LN) · ReDantotsu (+anime, LN) · Reikai · Rokku · ShinKu · ShonenX (+anime) · Sozo-Read (+comics, webtoon, LN) · Suwatte (iOS) · Suwayomi (escritorio) · Tachimanga (iOS) · Tachiyomi · Tachiyomi AT · Tachiyomi AZ · Tachiyomi J2K · Tachiyomi SY · Tadami (+anime, LN) · taihon · Taison · tankobon · Tankobun (+anime) · Tsundoku (+LN) · Unyo (escritorio; +anime) · Usagi · uwumi (+anime) · YACReader (multiplataforma) · Yokai · Yomihon · Yomikiru (Windows/Linux; +LN) · Zangetsu (+anime) · Zenbu (+anime, webtoon, comics)

**Anime (sin manga como tipo primero)** — 24

Anikku · animestream · Animiru · Anisurge · AniZen · Cloudstream · DodoStream · Hayase · hibiki · Migu · Miru App · NineAnimator (iOS) · Nuvio App · NyanTV · Seanime (escritorio) · Shiru · Skystream · Sora (iOS/Mac) · Sozo · Stremio (escritorio) · Th3-Anime · Toru · Totoro (Windows) · Zenshin

**Light novel** — 17

anx-reader · IReader · Koodo Reader · Legado · LightNovelReader · LNCrawler · LNReader · Myne · Nekori · NeoQN · NovelDokusha · Novery · Openlib · QuickNovel · ranobe · Shosetsu · Thorium Reader

**Otras** — 10

Github Store (herramientas) · Anirumy / AniSync (trackers) · Hentoid · KamiYomu (web) · Kitsu-X · Sozo TV · stump · Tonkatsu Box · Venera-SSR

Notas sobre este censo, no sobre cada ficha:

```
- Tachiyomi sigue listado. El núcleo cerró en 2024.
  El nombre en un directorio no lo revive. [Observación]

- Kotatsu (oficial kotatsuapp/kotatsu) está archivado
  en GitHub desde nov-2025. Miyomi aún lo nombra.
  Kotatsu Redo y Kotatsu-Next son otras entradas.
  [Fuente / Observación]

- Mihon, Komikku, TachiyomiSY, Aniyomi, Animetail,
  Kototoro: ya fichados en secciones anteriores o
  en la guía de Kototoro. Aquí solo constan en el
  censo de Miyomi.

- Cloudstream, Stremio, Hayase, Nuvio, harbor:
  Miyomi los cataloga. Esta guía no documenta
  addons de streaming ni debrid. [Observación]

- Hentoid, NHApp, JHenTai: el directorio los trae.
  Se nombran porque están; no se enlazan índices.
```

133 nombres. Si Miyomi suma uno mañana, gana Miyomi. Reabre https://miyomi.app/software

---

## 🧩 Mapa de extensiones (44, catálogo Miyomi 13-sep)

Nombre del directorio + repo de código si Miyomi lo declara. **Sin auto_url.** Compatible-with es lo que Miyomi apunta, no un test nuestro. [Fuente]

**Mihon / Tachiyomi-likes (manga)**

```
Keiyoushi          keiyoushi/extensions
                   (ya fichado arriba)

Extensões FelipeGFA
                   FelipeGFA/extensoes  (pt-br)

Project Nox        Awerkori/fonte-extensoes
                   (pt-BR; fork de FelipeGFA/fonte-extensoes)
                   5 ★. Push 13-sep-2026. Apache-2.0.
                   [Fuente]

Yuzono Cursed      yuzono/cursed-manga-extensions
                   (se nombra; no se enlaza índice)

Nyora Mihon Store  Nyora-Manga/nyora-mihon
                   (kotatsu-parsers embebido; ver 🔭)

Suwayomi Extension Suwayomi/tachiyomi-extension

TheNano            LittleSurvival/copymanga-copy20
                   (zh; 2.743 ★; ver 🔭)

Kavita             Kareadita/Kavita
                   (servidor; Miyomi lo mete como
                   «extensión» compatible con muchos
                   lectores. No se configuró aquí.)
```

**Aniyomi / anime**

Yuzono Anime       yuzono/anime-extensions

Secozzi            Secozzi/aniyomi-extensions

SalmanBappi's Aniyomi Repo
                   https://github.com/salmanbappi/extensions-repo

Hollow             https://codeberg.org/hollow/aniyomi-extensions-fr  (fr)

Bluecxt            bluecxt/anime-extensions-french  (FR)

Aniyomi Compat     CranberrySoup/AniyomiCompatExtension
                   (compat Cloudstream / Kototoro / etc.,
                   según Miyomi)

**Mangayomi / AnymeX / Dartotsu**

```
m2k3a              m2k3a/mangayomi-extensions
Mally              Mallyd11/mangayomi-anime-extensions
Swakshan           Swakshan/mangayomi-swak-extensions
Kegareta Sauces    gato404/kegareta-sauces
Mangayomi ApkBridge     Schnitzel5/ApkBridge
Mangayomi Custom Buttons Schnitzel5/mangayomi-custom-buttons
```

**Cloudstream / Stremio / Nuvio / Hayase / Sora**

Cloudstream MegaRepo   self-similarity/MegaRepo
CakesTwix              https://codeberg.org/CakesTwix/cloudstream-extensions-uk  (ua)
Stremio Addons         stremio-addons.net (sitio; sin repo)
Nuvio Plugins          nuvio-plugin-library.vercel.app
Hayase Extensions      exten.pages.dev
AIOStreams             Viren070/AIOStreams
Comet | ElfHosted      sin repo_url en el catálogo
50/50's Modules        https://git.luna-app.eu/50n50/sources

**Aidoku / Paperback / iOS**

```
Aidoku Community Sources   Aidoku-Community/sources
Inkdex                     inkdex/extensions
Netsky's Repo              TheNetsky/netskys-extensions
Moomooo95                  Moomooo95/moomooo95-extensions  (fr)
Suwatte Sources            sin repo_url en el catálogo
```

**Novelas / otros lectores**

```
LNReader Plugins           LNReader/lnreader-plugins
IReader-extensions         IReaderorg/IReader-extensions
Novel Sourcery             NovelSourcery/extensions
Dantotsu Novel Extensions  dannovels/novel-extensions
Gekkoushi / Mochi / UMA    plugins de Usagi / MIYO
rurin1x / Spithskia        extensiones de Shiru
Zangetsu Extension         Spyou/zangetsu-providers
kotatsu multi parsers      Shebyyy/kotatsu-multi-parsers
```

44. Si falta uno, es que Miyomi no lo tenía approved hoy — no que «no existe». [Observación]

---

## 🌒 Lo que no estaba en el corte Mihon-only (y lo que Alexis mandó hoy)

Tres paquetes que el texto de julio no cubría bien, reabiertos el 13-sep.

**Project Nox / Awerkori.** Miyomi ya lo tiene como extensión «Project Nox» → `Awerkori/fonte-extensoes` (manga, pt-BR, fork de FelipeGFA/fonte-extensoes). Además, hoy:

```
https://github.com/Awerkori/extensoes
  Fork de FelipeGFA/extensoes. 3 ★. Push 13-sep-2026.
  index.pb e index.min.json responden 200.
  [Fuente / Observación] No se pegan.

https://github.com/Awerkori/anime-extensoes
  «Project Nox Anime — repositorio de extensiones
  compiladas». 3 ★. Push 13-sep-2026.
  index.min.json responde 200 (~82 kB).
  [Fuente / Observación] No se pega.
  En el catálogo Miyomi de hoy NO aparece como
  fila aparte (el Nox listado es el de manga).
  Hueco del directorio, no de GitHub.

https://github.com/Awerkori/anime-fonte-extensoes
  Código. 3 ★. Apache-2.0. Push 13-sep-2026.
  Un fork julia5454554/anime-fonte-extensoes existe
  (0 ★). [Fuente]

https://github.com/Awerkori/project-nox-requests
  Pedidos. 2 ★. Push 4-sep-2026. [Fuente]
```

No se entra a su Discord. El README de forks ajenos lo enlaza; aquí no. [Observación]

**Kotatsu y los multi-parsers.** kotatsuapp/kotatsu: **archivado**, 8.848 ★, último push nov-2025. kotatsuapp/kotatsu-parsers: archivado. [Fuente]

Shebyyy/kotatsu-multi-parsers: 13 ★, push **hoy** 13-sep-2026 20:06 UTC. Release `build-2026.09.13-2006`. Assets vistos (nombres, no receta de descarga):

```
Kotatsu-Redo.jar
YakaTeam.jar
TamerAli-0.jar
glitch-228.jar
hany18h.jar
skepsun.jar
(+ .sha de cada uno)
[Fuente — GitHub Releases]
```

Miyomi ya lista «kotatsu multi parsers» en las 44. Esta guía **no pega** las URL `/releases/latest/download/…`. Quien use Kotatsu Redo u otro fork, que abra el README del parser el día que lo abra. [Observación]

**Komi / Github Store.** Miyomi lista «Github Store» como herramienta (rainxchzed/Github-Store). Es la línea de Komi de la otra guía, no una extensión Mihon. [Observación]

---

## 🚪 Cómo leer este mapa (sin las cuatro puertas al revés)

Las cuatro puertas de la guía APK **no** son veredicto de instalar 133 apps. [Observación]

```
1. Miyomi = índice. Keiyoushi = almacén. Mihon = app.
2. En Miyomi ≠ vivo (Kotatsu oficial archivado).
3. Vivo ≠ en Miyomi (Awerkori/anime-extensoes; beer-psi).
4. Un JAR de Shebyyy no revive Kotatsu oficial.
5. NSFW: se nombra porque el directorio los trae. No se receta.
```

---

## 🐋 Tadami y el trío manga / anime / novela

Tadami es el ejemplo que pediste: un fork de Aniyomi que junta **manga, anime y ranobe** en una sola app. Miyomi ya lo lista; el repo vivo no es el nombre viejo.

https://github.com/andarcanum/Tadami-Aniyomi-fork
  Fork de aniyomiorg/aniyomi. Apache-2.0.
  258 ★. 31 forks. Push 13-sep-2026
  (merge branch ranobe-novel).
  Release latest: v0.62 (12-sep-2026).
  Paquete que declara el README: com.tadami.aurora.
  Android 8.0+.
  [Fuente — GitHub API + README]

Miyomi lo tiene como
  https://github.com/andreykolesnikov/Tadami-Aniyomi-fork
  versión 0.60. Ese path redirige hoy a andarcanum.
  El directorio va una release atrás. [Observación]

Qué dice el README (no es un test nuestro): UI Aurora; soporte de anime + manga + novelas; trabajo de compatibilidad con ecosistemas estilo LNReader; fuentes/extensiones **por tipo** (browse separado). El propio README: donaciones solo al desarrollo de la app, no al contenido; Tadami no aloja ni da acceso a material de terceros. [Fuente]

tadami.qzz.io: 404 (GitHub Pages) al corte. No se usa como sitio oficial. [Observación]

Alrededor, no receta:

```
https://github.com/codegeasse1/yomi-reader
  8 ★. Apache-2.0. Push 6-sep-2026.
  «Yomi — anime, manga, and novel reader
  (Tadami/Aniyomi-compatible)». [Fuente]
  No está en Miyomi.

https://github.com/Freitez93/Tadami-Extensions
  0 ★. Push 13-ago-2026. Personal.
  «Algunas extensiones para Aniyomi/Tadami».
  [Fuente] Madurez: baja. No se receta.
```

Extensiones que Miyomi marca compatibles con Tadami (ya salieron en las 44): Keiyoushi, Yuzono Anime, Yuzono Cursed, Project Nox, Nyora, Suwayomi, TheNano, Kavita, LNReader Plugins, Novel Sourcery, Hollow, Secozzi, SalmanBappi, etc. Eso es el campo `compatible_with` del directorio, no un test en un teléfono. [Fuente — catálogo Miyomi]

---

## 🔎 Fuera de Miyomi (GitHub, 13-sep)

Repos que el censo 133/44 no trae como fila propia, o trae con URL vieja. Estrellas = GitHub hoy. Sin índices. Lo de «calidad, poco nombrado» se detalla en 🔭.

**Almacenes / agregadores**

```
https://github.com/cuong-tran/manga-repo
  444 ★. Homepage: https://yuzono.github.io.
  «Extensions for Komikku / Mihon & forks.»
  Push 12-sep-2026. El README: conservar el URL
  de yuzono/manga-repo, no el de cuong-tran.
  Es el almacén grande de Yūzōnō
  (yuzono/manga-repo tiene 4 ★). Miyomi no
  lo lista aparte. [Fuente]

https://github.com/amrkmn/x
  39 ★. Push hoy. Agregador: sincroniza
  Keiyoushi, Yuzono Cursed, Kohi-den,
  Yuzono Anime cada 4 h. Sitio x.noz.one.
  No es un catálogo nuevo: es un espejo.
  No se pega el índice. [Fuente]

https://github.com/MO350AZ/extensions-no-nsfw
  3 ★. Fork de keiyoushi/extensions.
  Filtro NSFW, auto-sync 30 min, dice el README.
  Push hoy. No se receta. [Fuente]

https://github.com/aniyomiorg/aniyomi-extensions
  Archivado. 852 ★. Último push ago-2024.
  El almacén oficial de Aniyomi está muerto.
  Lo que vive: Yūzōnō / Secozzi / salmanbappi / etc.
  [Fuente]
```

**Forks / parsers**

```
https://github.com/Chimahon/chimahon
  198 ★. GPL-3.0. Push 11-sep-2026.
  Inmersión: Yomitan, Mokuro, EPUB, Anki.
  Miyomi apunta a sohilsayed/chimahon; redirige.
  [Fuente / Observación]

https://github.com/HaoweiLi97/mihon_img_upscale
  194 ★. Fork de mihonapp/mihon. Apache-2.0.
  Push 29-ago-2026. Upscale AI (Real-CUGAN,
  Real-ESRGAN, Waifu2x). No está en Miyomi.
  [Fuente]

https://github.com/Kotatsu-Redo/kotatsu-parsers-redo
  44 ★. GPL-3.0. Push 5-sep-2026.
  Librería de parsers. No es un índice Mihon.
  [Fuente]

nubesurrealista/Kumo = el Kumo de Miyomi.
  No confundir con granjas SEO «Kumo 2026».
```

**Otro directorio, no un sauce**

```
https://github.com/wotakumoe/wotaku
  3.045 ★. Push hoy. Sitio https://wotaku.wiki.
  «An otaku index for everything.»
  Paralelo a Miyomi. No se recorrió ficha a ficha.
  [Fuente]
```

No se meten: 0 ★ de hace dos días, forks sin README, granjas «Best Manga Reader 2026». Un push reciente no es madurez. [Observación]

---

## 🧵 Cómo se encajan las capas (para no mezclar)

```
Capa 1  App
        Mihon, Komikku, Yokai, Tadami, Anikku,
        Mangayomi, Kotatsu Redo, LNReader, Aidoku…

Capa 2  Almacén de extensiones (índice)
        Keiyoushi, Yūzōnō/cuong-tran, FelipeGFA,
        Project Nox, Secozzi, Nyora, amrkmn/x…

Capa 3  Código de las extensiones
        keiyoushi/extensions-source,
        yuzono/tachiyomi-extensions,
        Awerkori/anime-fonte-extensoes…

Capa 4  Parsers de otro ecosistema
        kotatsu-parsers-redo, Shebyyy JARs.
        No se pegan en Mihon.

Capa 5  Directorio
        Miyomi (133/44). Wotaku.wiki.
        No instalan nada.
```

Tadami vive en la capa 1 y **bebe** de la 2 (Keiyoushi + Yuzono Anime + LNReader plugins, según Miyomi). No tiene un almacén exclusivo que hayamos visto con madurez. Freitez93 no cuenta. [Observación]

---

---

---

## 🔭 Poco nombrados (calidad, no fama)

Censo 13-sep-2026: búsqueda GitHub (topics tachiyomi-extensions / aniyomi-extensions / aidoku / mangayomi / shosetsu / kotatsu-parsers / lnreader / paperback / aidoku-sources) más páginas de repo abiertas. Filtro de este bloque, no un ranking:

```
Sí entra si, abierto hoy, cumple varias:
  - licencia SPDX o LICENSE en el árbol
  - código propio (src/, parsers, rust, lua) o
    un almacén con CI que no es un clone vacío
  - push en 2026 (o se marca como archivo histórico)
  - propósito propio (idioma, app distinta, parsers)

No entra:
  - 0 ★ de hace dos días sin README
  - forks de keiyoushi/extensions sin commits propios
  - granjas SEO con index.min.json en el nombre del repo
  - espejos que solo dicen «Mirror of Keiyoushi»
  - recetas de instalación (no se pegan índices)

Estrellas = GitHub/Codeberg hoy. [Observación]
Esta guía nombra el repo. El índice vive en su README
el día que lo abras. [Observación]
```

### Fuera de las 44 de Miyomi

**beer-psi/tachiyomi-unofficial-extensions**

```
53 ★. 5 forks. Apache-2.0. 144 commits.
Push 29-ago-2026 («sure», en src/).
Sitio que declara: https://beer-psi.github.io/tachiyomi-unofficial-extensions
Estructura: buildSrc, core, lib, lib-multisrc, src,
CONTRIBUTING, CODE_OF_CONDUCT. Commits de abr-2026
«Sync build pipeline with Keiyoushi» y
«Move to Keiyoushi shared utilities».
El README (vietnamita + inglés) avisa:
«Vui lòng cân nhắc rủi ro trước khi sử dụng
nguồn không chính thức.»
Disclaimer clásico: sin afiliación con los sitios.
No está en el catálogo Miyomi de 44.
[Fuente — página del repo, 13-sep]
No se pega el índice. No se afirma que Keiyoushi
lo avale: el propio nombre es «unofficial».
[Observación]
```

**dragonx943/manga-repo**

```
22 ★. 11 forks. GPL-3.0. 70 commits. 29 tags.
Push 5-sep-2026 (marca TruyenQQ como fuente rota).
Descripción: fuentes vietnamitas y algunas
multilingües para Usagi y apps con la misma
estructura (Tsuki).
Árbol: src/main/kotlin/tsuki/site, plugins-ksp,
buildSrc, LICENSE.
README: buildJar; créditos a KotatsuApp y Keiyoushi
por parsers/código, no un fork de Mihon.
Homepage que declara: yumemi.moe/usagi
«Generated from UsagiApp/plugins».
Topics incluyen hentai/doujin: el repo no es
«SFW por defecto». Se nombra; no se receta.
[Fuente]
No es un almacén index.min.json de Mihon.
Capa 4 (parsers de otro ecosistema). [Observación]
```

**Gekkoushi/plugin-source + Gekkoushi/plugin**

```
plugin-source:
  90 ★. 72 forks. GPL-3.0. 2.416 commits.
  Push hoy 13-sep-2026 (README → Usagi).
  «utilities and some parsers… JVM and Android».
  Aviso: «Only for the Usagi App».
  Apunta a InvalidDavid/UMA (v1.0) y a
  Gekkoushi/plugin («No updates, 1.3k sources»).
  Miyomi lista «Gekkoushi» → Gekkoushi/plugin
  y «UMA Plugin» → InvalidDavid/UMA.
  El código de parsers es plugin-source.
  [Fuente]

plugin (artefactos):
  7 ★. 8 commits. Push hoy (mismo README).
  1 release (10-ago-2026).
  Contributors: InvalidDavid, dragonx943.
  El README: «the content inside has been provided
  by Gemini… No one knows how it works.»
  Eso es una bandera de calidad, no un aval.
  [Fuente / Observación]
  No se pegan JARs ni releases.
```

**suiyuran/aidoku-zh-sources**

```
883 ★. 36 forks. 134 commits.
Push 30-mar-2026 (PR #150).
Sin SPDX en la API de GitHub. [Observación]
README: «Aidoku 中文图源». Lista de fuentes
chinas (varias tachadas como muertas).
Hay entradas explícitas en esa lista; no se
recitan aquí. [Observación]
Más estrellas que Aidoku-Community/sources (584)
y push más viejo. No está en las 44.
[Fuente]
```

**Smexhy/yomu-aidoku-sources**

```
14 ★. 47 commits. Push 19-ago-2026.
LICENSE + THIRD-PARTY-LICENSES.md (NOASSERTION
en la API).
«Yomu is my own source list… seven sources…
not the official Aidoku community list.»
Aidoku 0.8.3+, iOS/iPadOS.
No se pega la source list. [Fuente]
```

**adly98/aniyomi-ar-extensions**

```
5 ★. 2 forks. Apache-2.0. 89 commits. 8 ramas.
API pushed_at 10-may-2026.
Árbol: src/ar, lib-multisrc, core, CONTRIBUTING,
LICENSE, renovate.json.
«Arabic extension catalogues for the Aniyomi fork.»
Estructura de almacén Aniyomi real.
★ bajas ≠ vacío; tampoco son madurez pública alta.
No está en Miyomi. [Fuente / Observación]
```

**msrofficial/anime-extensions**

```
3 ★. 0 forks. Apache-2.0. 17 commits.
Push 22-may-2026 («Clean repository wording»,
«Trim repo to maintained MSR extensions»).
src/hi. Toonstream en el historial.
Aniyomi/Anikku. Recortado a lo mantenido.
Madurez: baja-media. [Fuente]
```

**Shosetsu (la app está en las 133; estos no en las 44)**

```
https://github.com/noaione/shosetsu-extensions
  «N4O Shosetsu Extension Collection»
  19 ★. 5 forks. GPL-3.0. 651 commits. 12 tags.
  Rama dev. Push 20-may-2026.
  src/en, lib, lua, CI. [Fuente]

https://github.com/jobobby04/ShosetsuExtensions
  El mismo Jobobby04 de TachiyomiSY.
  16 ★. 8 forks. GPL-3.0. 123 commits.
  Push 11-abr-2026 (AO3 search, PR #24).
  README: «Personal extensions for Shosetsu».
  El listado incluye sitios explícitos.
  Se nombra el repo; no se copian destinos.
  [Fuente / Observación]
```

**IReader y Paperback (sí en Miyomi; números de hoy)**

```
https://github.com/IReaderorg/IReader-extensions
  32 ★. 27 forks. MPL-2.0. 486 commits.
  Push 27-ago-2026 (kolnovel libVersion, PR #239).
  Árbol grande: extensions, sources, js-sources,
  compiler, tests. [Fuente]

https://github.com/inkdex/extensions
  31 ★. 10 forks. Push 22-ago-2026.
  «Paperback extension registry… Inkdex community»
  0.9/stable. Homepage: inkdex.github.io/installation
  No se pega el registry. [Fuente]

https://github.com/PoppingMangoSources/popmango-paperback-sources
  3 ★. GPL-3.0. Push 29-ago-2026.
  «Unified 0.8 & 0.9 Paperback extensions».
  ★ bajas. [Fuente]
```

### En Miyomi, mal nombrados o mal fechados

**TheNano = LittleSurvival/copymanga-copy20**

```
2.743 ★. 16 forks. 176 commits.
Push 8-sep-2026.
Miyomi lo etiqueta «TheNano». El GitHub es
https://github.com/LittleSurvival/copymanga-copy20.
README: fuentes chinas para Tachiyomi/Mihon
(CopyManga / vomic / 包子 / 漫蛙2; CopyManga
v1.4.85 dice compat Suwayomi).
Hay Telegram/QQ/Discord en el README; aquí no
se enlazan (no Discord). [Fuente / Observación]
Es el almacén chino más estrellado visto hoy
fuera de Keiyoushi. No es «menor» en ★;
es menor en el circuito hispano de La Bandita.
[Observación]
```

**Nyora-Manga/nyora-mihon**

```
10 ★. 2 forks. 31 commits.
Push 19-jul-2026: Nyora-Sources v1.6.19 code 19.
Descripción: una extensión Mihon que embebe
kotatsu-parsers y parsea en el dispositivo
(«~900 on-device sources»).
Dos sabores que el README nombra (SFW / 18+);
no se recetan. Source/CI:
https://github.com/Nyora-Manga/nyora-mihon-extension-porter
(no se abrió el porter hoy). [Fuente / No confirmado el porter]
Puente capa 2 (almacén Mihon) + capa 4 (parsers Kotatsu).
[Observación]
```

**Aidoku Community**

```
https://github.com/Aidoku-Community/sources
  584 ★. 114 forks. Apache-2.0 OR MIT.
  333 commits. Aidoku 0.7+.
  Miyomi: «Aidoku Community Sources».
  Unofficial, community-maintained.
  [Fuente]

https://github.com/Aidoku-Community/legacy-sources
  701 ★. 181 forks. Apache-2.0 OR MIT.
  498 commits. Push 9-sep-2026 (fix compilation).
  README 22-jun-2025: «no longer actively
  maintained»; continuación = sources (0.7+).
  Más ★ que el sucesor. No está como fila
  aparte en las 44. [Fuente / Observación]
```

**Suwayomi/tachiyomi-extension** (ya en las 44)

```
325 ★. Apache-2.0. Push 12-sep-2026.
«Suwayomi Extension for Tachiyomi and variants».
Es el conector al servidor Suwayomi, no un
catálogo de sitios. [Fuente]
```

**Secozzi/aniyomi-extensions** (ya en las 44)

```
114 ★. 14 forks. 49 commits.
Push 3-jul-2026 (remote videos, PR #73).
Historial: ext lib 16; fuentes self-host
(Jellyfin, Stremio) en los mensajes de commit.
No se documenta debrid. [Fuente / Observación]
```

**Hollow (francés) — Miyomi lo da por vivo**

https://codeberg.org/hollow/aniyomi-extensions-fr
  Codeberg: Archived 6-sep-2026.
  1 ★. 8 forks. 63 commits. src/fr.
  Último commit el mismo 6-sep (mass-bump)
  y luego archivo.
  Miyomi aún lo lista en las 44.
  Estar en el directorio ≠ estar aceptando
  parches. [Fuente / Observación]

**salmanbappi/extensions-repo** (ya en las 44)

```
40 ★. Push hoy 13-sep-2026.
«Dedicated Anime Extensions Repository for Anikku».
[Fuente]
```

### Abiertos y descartados (para no inflar el mapa)

https://github.com/everfio/tachiyomi-extensions
  37 ★. 14 forks. 5 commits. Sin LICENSE en API.
  README de una línea: «Mirror of keiyoushi/extensions».
  No es sauce propio. [Observación]

WendySBlanc/extensions («Nova Extensions»)
  0 ★. 0 forks. Fork de keiyoushi/extensions.
  12 commits ahead / 5 behind (rama repo).
  Push 9-sep-2026 (bot). README: independiente,
  firmado por el workflow de Nova.
  extensions-source: 0 ★, 16 ahead / 51 behind
  keiyoushi, commit «Lelscan reader fix» 9-sep.
  Señales de trabajo real; madurez pública (★) baja.
  No se receta. [Fuente / Observación]

https://github.com/timschneeb/tachiyomi-extensions-archive
  1.802 ★. 280 forks. Apache-2.0.
  Archivado 23-mar-2026. 3 commits.
  README: «This archive repository was DMCA'd
  and has been erased.» Historial git borrado.
  No es un almacén usable. Hecho histórico.
  [Fuente]

https://github.com/ThePBone/tachiyomi-extensions-revived
  Al corte, abrir esa URL resolvió al archivo
  de timschneeb. No se afirma un repo vivo
  bajo ese nombre. [Observación]

https://github.com/Koray-Ozt/k-kitsu-extensions
  Topic aniyomi (1 ★ en un índice de agosto).
  https://github.com/Koray-Ozt/k-kitsu-extensions: 404 hoy.
  [No encontrado]

https://github.com/MO350AZ/extensions-no-nsfw
  3 ★. Filtro NSFW de Keiyoushi. Ya fichado
  en «Fuera de Miyomi». No se receta.

https://github.com/Freitez93/Tadami-Extensions
  0 ★. Ya fichado. Madurez baja.

https://github.com/Confused-Creature-180/aniyomi-extensions
  4 ★. Apache-2.0. Push hoy. Página no se recorrió
  ficha a ficha. Queda [No confirmado el interior].

https://github.com/oneulddu/Korean-Mihon-Extensions
  0 ★. Apache-2.0 en búsqueda. API 403 después.
  No se afirma el interior. [No confirmado]

https://github.com/Hayanek/aniyomi-extensions-pl
  0 ★ en búsqueda. Interior no abierto. [No confirmado]

https://github.com/matqueme/aniyomi-extensions-fr
  0 ★. Apache-2.0. Push 12-oct-2025. Viejo y 0 ★.
  No entra. [Observación]

### Qué se buscó y no se recita como sauce

```
Búsqueda GitHub 13-sep, primera pasada: 165 repos
únicos con «extensions» / «manga-repo» / aidoku.
La cola es 0 ★ con nombres de receta
(«https-raw.githubusercontent.com-…-index.min.json»).
Eso no se ficha. [Observación]

API de GitHub: 403 intermitente en esta sesión
(rate limit). Lo no abierto se marca
[No confirmado], no «no existe». [Observación]

Codeberg: se abrió hollow. CakesTwix
(cloudstream-extensions-uk) está en las 44;
no se reabrió la ficha hoy. [No confirmado el interior 13-sep]

No se recorre https://wotaku.wiki ficha a ficha.
No se entra a Discord. [Observación]
```

---

## 🧭 Cómo se lee «calidad» aquí (sin teatro de cuatro puertas)

Las cuatro puertas de la guía APK no se aplican como veredicto de instalar 40 almacenes. Lo que sí se midió:

```
1. ¿Hay LICENSE? beer-psi Apache, dragonx943 GPL-3,
   Gekkoushi GPL-3, Aidoku dual, IReader MPL-2,
   adly98 Apache, noaione GPL-3.
   suiyuran: no SPDX. everfio: no.

2. ¿Hay src/ propio? beer-psi sí. dragonx943 sí.
   plugin-source sí. adly98 src/ar sí.
   msrofficial src/hi sí. everfio no.
   Nova/WendySBlanc: fork de Keiyoushi con
   delta pequeño.

3. ¿Push 2026? La mayoría de esta lista sí.
   suiyuran: mar-2026 (frío relativo).
   Hollow: vivo hasta el 6-sep y archivado el mismo día.

4. ¿Propósito propio?
   idioma (VN, AR, HI, ZH, FR)
   o app distinta (Usagi, Aidoku, Shosetsu, Paperback)
   o puente (Nyora = Kotatsu dentro de Mihon).

5. ¿El directorio Miyomi lo ve?
   No. Por eso este bloque existe.
```

Nada de esto es «instálalo». Es el mapa que el circuito Mihon-only no enseña. [Observación]

---

---

## 📋 Inventario de la exploración (13-sep)

Método, para que se pueda repetir. No es una receta de instalación.

```
1. GitHub Search API, sort=updated y sort=stars:
   topic:tachiyomi-extensions (5)
   topic:aniyomi-extensions (2)
   topic:aidoku (11)
   aniyomi-extensions in:name (58; se vieron 30)
   mihon-extensions in:name (47; 30)
   tachiyomi-extensions in:name (84; 30)
   manga-repo in:name (116; 30)
   anime-repo in:name (210; 30 — mucho ruido)
   mangayomi-extensions in:name (28)
   shosetsu-extensions in:name (17)
   lnreader + plugins (33)
   paperback sources in:name (15)
   aidoku-sources in:name (48)
   kotatsu-parsers in:name archived:false (15)

2. Primera pasada: 165 repos únicos.
   Cola dominante: 0 ★ con el index.min.json
   pegado en el nombre del repo. SEO/granjas.
   No se fichan. [Observación]

3. Segunda pasada: pages HTML de candidatos
   (API 403 intermitente). Se abrieron, entre otros:
   beer-psi, dragonx943, LittleSurvival,
   suiyuran, Aidoku-Community/{sources,legacy-sources},
   adly98, WendySBlanc/{extensions,extensions-source},
   everfio, msrofficial, Gekkoushi/{plugin,plugin-source},
   noaione, jobobby04/ShosetsuExtensions, Smexhy,
   Nyora-Manga/nyora-mihon, Secozzi, IReaderorg,
   inkdex, codeberg hollow, timschneeb archive.

4. Codeberg: hollow archivado 6-sep-2026.
   CakesTwix (en las 44): ficha no reabierta hoy.

5. Koray-Ozt/k-kitsu-extensions: 404.
   ThePBone/tachiyomi-extensions-revived: resolvió
   al archivo DMCA de timschneeb.
```

**Lo que sí se sostiene como «poco nombrado + señales de calidad»**

```
Señal A — código propio + licencia + push 2026
  beer-psi (Apache, src/, ago)
  dragonx943 (GPL-3, tsuki/, sep)
  Gekkoushi/plugin-source (GPL-3, 2.416 commits, hoy)
  adly98 (Apache, src/ar, may)
  msrofficial (Apache, src/hi, may)
  noaione (GPL-3, 651 commits, may)
  jobobby04/ShosetsuExtensions (GPL-3, abr)

Señal B — almacén grande fuera del circuito hispano
  LittleSurvival/copymanga-copy20 (2.743 ★, zh)
  suiyuran/aidoku-zh-sources (883 ★, Aidoku zh)
  Aidoku-Community/sources (584 ★) y legacy (701 ★)

Señal C — puente de ecosistemas
  Nyora-mihon: kotatsu-parsers dentro de Mihon
  Gekkoushi: parsers Usagi/Tsuki
  dragonx943: mismo eje Usagi, foco VN
  Suwayomi/tachiyomi-extension: servidor, no sitios

Señal D — directorio desfasado
  Hollow FR archivado 6-sep; Miyomi lo lista vivo
  Tadami Miyomi 0.60 / andarcanum v0.62
  TheNano vs LittleSurvival (nombre)
  chimahon sohilsayed/ vs Chimahon/
```

**Lo que no se sostiene como sauce**

```
everfio = espejo de Keiyoushi (5 commits).
Nova/WendySBlanc = 0 ★, delta pequeño sobre Keiyoushi.
timschneeb archive = DMCA, historial borrado.
ThePBone revived = no hay repo vivo bajo ese path.
Koray-Ozt = 404.
Granjas con la URL de índice en el nombre.
0 ★ personales «bro it just a repo i use».
Cloudstream / Stremio / Nuvio / Hayase / debrid:
  Miyomi los cataloga. Esta guía no documenta
  addons de streaming ni debrid. [Observación]
```

**Idioma / región (abierto hoy, no un censo completo)**

```
zh   LittleSurvival (Mihon), suiyuran (Aidoku)
     TheNano en Miyomi = LittleSurvival
fr   Hollow (archivado 6-sep), bluecxt (en las 44,
     ficha no reabierta), Moomooo95 Paperback
ar   adly98 Aniyomi
hi   msrofficial Anikku
vi   beer-psi (README vi), dragonx943 (fuentes VN)
pt-BR  FelipeGFA, Awerkori/Project Nox (ya en el mapa)
en   Keiyoushi, Yūzōnō, Nyora, Shosetsu extras
iOS  Aidoku Community, suiyuran, Smexhy/Yomu,
     inkdex/Paperback, Moomooo95
novelas  LNReader plugins (en 44), IReader,
         noaione / jobobby04 Shosetsu
```

No se afirma que «no hay» almacén coreano, polaco o español extra: oneulddu/Hayanek/matqueme no se abrieron por 403 o 0 ★ viejo. [No confirmado] ≠ [No encontrado] ≠ no existe. [Observación]

---

### 🧪 Nyora, Usagi y el puente Kotatsu (sin receta)

Tres formas distintas de «no es Keiyoushi» que el corte Mihon-only no ve.

```
Nyora-mihon
  Una extensión Mihon. Por dentro: motor
  kotatsu-parsers. Parseo en el teléfono.
  ~900 fuentes, dice el README.
  v1.6.19 / code 19 (19-jul-2026).
  Auto-trust si se instala desde su repo
  (firma vs fingerprint). Un APK suelto
  sale UNTRUSTED — eso lo dice el README,
  no un test nuestro.
  [Fuente] No se pega el índice.

Gekkoushi / UMA / dragonx943
  No hablan el protocolo de índice de Mihon.
  Hablan parsers Tsuki/Usagi (JAR/plugin).
  plugin-source = código (2.416 commits).
  plugin = artefactos; README con aviso
  Gemini. dragonx943 = foco VN, 70 commits.
  InvalidDavid/UMA está en las 44.
  [Fuente / Observación]

https://github.com/Shebyyy/kotatsu-multi-parsers
  Ya en las 44. Release de hoy con JARs
  nombrados (Kotatsu-Redo, YakaTeam,
  TamerAli-0, glitch-228, hany18h, skepsun).
  No se pegan URLs /releases/latest/download.
  [Fuente]
```

Tres ecosistemas de parsers. Mezclarlos en Mihon «porque todos son manga» es el error de capas. [Observación]

---

### 🧷 TheNano, Aidoku y los nombres que Miyomi esconde

```
Miyomi «TheNano»
  GitHub: LittleSurvival/copymanga-copy20
  2.743 ★. 16 forks. Push 8-sep-2026.
  CopyManga v1.4.85 (compat Suwayomi, 熱辣
  por cambio de API en ajustes del plugin).
  vomic 1.4.4 (pide login en ajustes).
  漫蛙2 1.4.7. 包子漫畫 1.4.3.
  Versiones = README, no un test.
  [Fuente]
  En el circuito hispano casi no se nombra
  el GitHub; se nombra «TheNano». El mapa
  correcto es el repo. [Observación]

Miyomi «Aidoku Community Sources»
  Aidoku-Community/sources 584 ★ dual license.
  Aidoku 0.7+. Unofficial.
  El repo viejo (legacy-sources, 701 ★) avisa
  que ya no se mantiene. Push 9-sep = fix de
  compilación, no un almacén nuevo.
  suiyuran (883 ★, zh) y Smexhy/Yomu (14 ★)
  no están en las 44.
  [Fuente]

Miyomi «Gekkoushi»
  Apunta a Gekkoushi/plugin (artefactos, 7 ★).
  El código es plugin-source (90 ★, 2.416
  commits). Quien cite estrellas de Gekkoushi
  sin decir cuál repo, mezcla capas.
  [Observación]
```

---

### 🔧 beer-psi y Nova: no oficiales, no espejos vacíos

```
https://github.com/beer-psi/tachiyomi-unofficial-extensions
  53 ★. Apache-2.0. 144 commits.
  Aviso del README (vi): considerar el riesgo
  de fuente no oficial.
  Pipeline sincronizado con Keiyoushi (abr-2026)
  pero el src/ es propio.
  No está en Miyomi. No está en Keiyoushi.
  «Unofficial» es el nombre, no un insulto.
  [Fuente]

WendySBlanc / Nova
  0 ★. Fork de keiyoushi/extensions.
  12 ahead / 5 behind. CI propia, firma propia.
  extensions-source: Lelscan fix 9-sep-2026.
  Trabajo real, madurez pública (estrellas) baja.
  Un 0 ★ con CI no es granja SEO; tampoco es
  Keiyoushi. No se receta. [Fuente / Observación]

everfio
  37 ★ y solo dice «Mirror of keiyoushi/extensions».
  5 commits. No pasa el filtro. [Observación]
```

### Fuentes extra (solo las abiertas en esta pasada)

https://github.com/beer-psi/tachiyomi-unofficial-extensions
https://github.com/dragonx943/manga-repo
https://github.com/Gekkoushi/plugin-source
https://github.com/Gekkoushi/plugin
https://github.com/suiyuran/aidoku-zh-sources
https://github.com/Aidoku-Community/sources
https://github.com/Aidoku-Community/legacy-sources
https://github.com/Smexhy/yomu-aidoku-sources
https://github.com/adly98/aniyomi-ar-extensions
https://github.com/msrofficial/anime-extensions
https://github.com/noaione/shosetsu-extensions
https://github.com/jobobby04/ShosetsuExtensions
https://github.com/LittleSurvival/copymanga-copy20
https://github.com/Nyora-Manga/nyora-mihon
https://github.com/IReaderorg/IReader-extensions
https://github.com/inkdex/extensions
https://github.com/WendySBlanc/extensions
https://github.com/WendySBlanc/extensions-source
https://github.com/everfio/tachiyomi-extensions
https://github.com/timschneeb/tachiyomi-extensions-archive
https://github.com/Secozzi/aniyomi-extensions
https://codeberg.org/hollow/aniyomi-extensions-fr
https://github.com/andarcanum/Tadami-Aniyomi-fork
https://github.com/cuong-tran/manga-repo
https://github.com/amrkmn/x
https://miyomi.app/

HEAD/GET de índices: solo para anotar si el archivo responde. Las URLs no se recetan.

---

### Acciones extra (informar, no empujar)

**Si lees en chino en Mihon.** Miyomi dice TheNano. El repo es LittleSurvival/copymanga-copy20 (2.743 ★). Reabre el README el día que actúes. Esta guía no pega el índice.

**Si lees en iOS (Aidoku).** Hay almacén comunitario (sources, 0.7+), un legacy que el propio README jubila, un almacén chino (suiyuran) y uno pequeño propio (Yomu). No son intercambiables.

**Si usas Usagi / Tsuki.** Keiyoushi no aplica. El código vivo visto hoy es Gekkoushi/plugin-source y, en VN, dragonx943/manga-repo. Los artefactos de Gekkoushi/plugin traen un aviso Gemini en el README: léelo.

**Si Aniyomi en árabe o hindi.** adly98 (ar) y msrofficial (hi) existen con Apache-2.0 y src/. ★ bajas. No es «no existen»; es madurez pública chica.

**Si Shosetsu.** La app está en las 133. Los almacenes extra (noaione, jobobby04) no están en las 44. El de jobobby04 incluye sitios explícitos: se nombra el repo, no la lista.

**Si ves Hollow FR en Miyomi.** Archivado el 6-sep-2026. El directorio va atrás.

**Si te pegan Nova / everfio / un repo 0★ con la URL en el título.** everfio es espejo. Nova tiene CI y 0 ★. La granja con index.min.json en el nombre no entra al mapa.

No hace falta «migrar todo ahora». Tampoco hace falta un almacén extra «por si acaso».

---

## 🛠️ Si algo se rompe (sin receta de fuentes)

Keiyoushi troubleshooting (hoy), lo que se puede decir sin convertirlo en guía de evasión:

```
- Lista vacía / «Outdated app» / obsolete:
  la app no llega al mínimo (Mihon 0.20.4+ según
  getting-started). [Fuente]

- Firma que no coincide al actualizar una extensión
  (INSTALL_FAILED_UPDATE_INCOMPATIBLE): Keiyoushi
  dice que hay otra extensión con el mismo paquete
  y otra firma; hay que desinstalar la vieja.
  [Fuente] No se probó.

- APK corrupto (DISPLAY_NAME column is null):
  volver a bajar, dice Keiyoushi. [Fuente]

- WebView / Cloudflare: Keiyoushi tiene una página
  entera. No se copia aquí el procedimiento de
  CAPTCHA ni el cambio de user-agent. [Observación]
```

El corte de julio: avión + Wi-Fi off para borrar la extensión que hace crash, VPN a Canadá/Alemania contra el 429, «no te preocupes, la infra está segura». Eso no salió en troubleshooting. [No confirmado] No se recita.

Backup `.tachibk`: nombre histórico de Tachiyomi. No se abrió la documentación de backup de Mihon hoy. [No confirmado el formato actual]

«Abrir en WebView» como parche: Keiyoushi lo documenta. Sigue siendo hablar con el sitio original, no con un espejo de esta guía. [Fuente]

---

## 🌱 Vías oficiales abiertas hoy

Esto sí se puede enlazar: son productos que se presentan como licenciados. Catálogo y precio: reabre el día que pagues. No se afirma que Keiyoushi tenga «la extensión de Manga Plus».

MANGA Plus by SHUEISHA
  https://mangaplus.shueisha.co.jp/
  Abierto hoy. Oficial de Shueisha. [Observación]

Webtoon
  Plataforma conocida. El sitio no se reabrió hoy.
  [No confirmado el estado 13-sep]

Crunchyroll
  Servicio de anime (y, según medios 2025–2026,
  app de manga relanzada). No se abrió crunchyroll.com
  hoy. [Reporte externo / No confirmado el catálogo]

Netflix / Prime / Max
  Catálogo de anime con licencia, variable por país.
  No se auditó RD. [No confirmado]

Bibliotecas (Hoopla, OverDrive, etc.)
  Dependen de tu biblioteca. No se abrió ninguna.
  [No confirmado]

El corte de julio metía Manga Plus y Webtoon «con extensión en Keiyoushi». Esa frase convierte una vía oficial en un conector no oficial. Se deja fuera. [Observación]

Real-Debrid + Stremio/Torrentio + Jellyfin: el corte de julio ya decía que no daba tutorial. Esta guía tampoco. No se documenta un flujo de debrid. [Observación]

---

## 📌 Correcciones al corte 25-jul-2026

```
Keiyoushi 14,5k ★ → 14.963 ★ (push 12-sep).
extensions-source 4,4k ★ → 4.669 ★ Apache-2.0.
Índice: getting-started pide index.pb y Mihon
  0.20.4+. La receta no se pega.
Yūzōnō 319 ★ / «privado» → tachiyomi-extensions
  887 ★, org pública, 8 repos visibles.
Índice anime «caído» → push 13-sep y GET 200.
manga-repo index.pb «el que debes usar» → 404.
FelipeGFA/extensoes 35 ★ → 41 ★ (push 13-sep).
Kohi-den 842 ★ / DMCA → 532 ★, archivado
  14-may-2026. Motivo DMCA no salió. kohiden.xyz: TLS.
Cursed «caídos» → GET 200. No se enlazan.
KeiSource 1.6 «no existe» → libVersion 1.6 en
  CONTRIBUTING (Yūzōnō) y PR #448 «1.6+».
PR #448 «solo bugs» → el título lo contradice.
  Merged 22-jul, Dark25 (fecha sí coincidía).
Keiyoushi = Aniyomi/Animetail → no. Nombra
  Mihon, TachiyomiSY, Komikku. El resto: on your own.
HTTP 429 + VPN: no en troubleshooting. Fuera.
Fusión cada 6 h: no salió. [No confirmado]
Tablas / «ballenita» → bloques. La Bandita.
Pegar índices → no. Se nombra el repo.
```

---

## 🚧 Límites de este texto

```
- No se instaló Mihon, Aniyomi, Animetail, Komikku,
  TachiyomiSY ni Tadami.
- Miyomi: 133 apps y 44 ext vía API pública del
  propio proyecto. Claves y auto_url no se recitan.
- tadami.qzz.io: 404 hoy.
- https://wotaku.wiki: no se recorrió ficha a ficha.
- Censo GitHub 13-sep: 165 repos únicos en la
  primera pasada; la cola 0★/SEO no se ficha.
- GitHub API: 403 intermitente. Interior no
  abierto = [No confirmado], no «no existe».
- No se añadió ningún extension store.
- No se instaló ninguna extensión.
- No se leyó un capítulo ni se reprodujo un capítulo
  de anime.
- Discord de Keiyoushi: no se entra (no Discord).
- yuzono/aniyomi-extensions: HTTP 451. Interior no visto.
- kohiden.xyz: fallo TLS.
- CONTRIBUTING de Yūzōnō: 1.813 líneas; se usó el
  encabezado y el snippet de KeiSource 1.6, no un
  audit línea a línea.
- Anuncio original de Tachiyomi / carta de Kakao:
  no reabiertos. Medios de ene-2024.
- «50× malware», 429 regional, fusión cada 6 h:
  no recitados como hechos.
- Checksums de Animetail: no se copian.
- Esta guía no es un envío. BORRADOR.
```

---

## ✅ Acciones concretas

**Si solo querías entender el mapa.** Con esto basta. Reabre GitHub el día que cites una estrella.

**Si usas Mihon y Keiyoushi ya te funciona.** El 25-jul no es tu corte. El de Keiyoushi, sí: 0.20.4+ y el formato de índice que su getting-started muestre **ese día**.

**Si Aniyomi o Animetail te fallan con extensiones de Keiyoushi.** Keiyoushi dice que no te soporta. No es un misterio de ClassLoader que esta guía vaya a «resolver» con un índice pegado. [Fuente / Observación]

**Si Kohi-den era tu almacén de anime.** Está archivado desde mayo. No hay promesa de que vuelva. [Fuente]

**Si te llega un video «pega esta URL».** Esa es la receta que esta guía no va a copiar. El README del proyecto, abierto el mismo día, manda sobre un screenshot de julio.

**Si lo que quieres es leer o ver sin esa zona gris.** MANGA Plus está abierto hoy. El resto de catálogos oficiales, el día que los abras.

No hace falta «migrar todo ahora». Tampoco hace falta un repo cursed «por si acaso».

---

## 📚 Fuentes abiertas el 2026-09-13

GitHub API / páginas de repo (estrellas, archivado, push)
  keiyoushi/extensions (+ extensions-source)
  yuzono/* · Kohi-den/extensions-source · FelipeGFA/*
  mihonapp/mihon · aniyomiorg/aniyomi
  Animetailapp/Animetail (+ pull/448)
  komikku-app/komikku · jobobby04/TachiyomiSY

https://keiyoushi.github.io/
https://keiyoushi.github.io/docs/guides/getting-started
https://keiyoushi.github.io/docs/guides/troubleshooting
https://yuzono.github.io/
https://mangaplus.shueisha.co.jp/
https://miyomi.app/  y  https://github.com/miyomiorg/Miyomi
https://github.com/andarcanum/Tadami-Aniyomi-fork  (v0.62)
https://github.com/cuong-tran/manga-repo
https://github.com/amrkmn/x
https://github.com/Chimahon/chimahon
https://github.com/HaoweiLi97/mihon_img_upscale
https://github.com/Kotatsu-Redo/Kotatsu-Redo
https://github.com/wotakumoe/wotaku
https://github.com/Awerkori/fonte-extensoes
https://github.com/Shebyyy/kotatsu-multi-parsers
https://github.com/beer-psi/tachiyomi-unofficial-extensions
https://github.com/dragonx943/manga-repo
https://github.com/Gekkoushi/plugin-source
https://github.com/suiyuran/aidoku-zh-sources
https://github.com/LittleSurvival/copymanga-copy20
https://github.com/Aidoku-Community/sources
https://codeberg.org/hollow/aniyomi-extensions-fr

HEAD/GET de índices: solo para anotar si el archivo
responde. Las URLs no se recetan.

Reporte externo (no reabierto el texto primario):
  animecorner.me 14-ene-2024 (Tachiyomi / Kakao)
  alternativeto.net 15-ene-2024

---

**Cierre.** El ecosistema sigue vivo el 13-sep-2026: Keiyoushi empuja, Yūzōnō es público, FelipeGFA actualiza pt-br, Kohi-den está archivado, KeiSource 1.6 no es un mito, y el PR #448 de Animetail sí habla de carga 1.6+. Miyomi cuenta 133 apps y 44 ext; Tadami vivo es andarcanum v0.62 (Miyomi aún dice 0.60). Fuera de ese directorio, abiertos hoy con código propio: beer-psi (unofficial), dragonx943 (Usagi VN), Gekkoushi/plugin-source (parsers Usagi), suiyuran (Aidoku zh), adly98 (Aniyomi ar), msrofficial (Anikku hi), noaione y jobobby04 (Shosetsu). LittleSurvival/copymanga-copy20 es el «TheNano» de Miyomi (2.743 ★). Hollow FR se archivó el 6-sep; Miyomi aún lo lista. everfio es espejo; Nova tiene CI y 0 ★; el archivo de timschneeb está DMCA'd. El 25-jul acertó el archivo de Kohi-den y la fecha del PR; falló estrellas, «caídas» que hoy responden, el «no existe» de 1.6 y el soporte de Keiyoushi (Mihon / SY / Komikku, no Aniyomi). Esta guía no pega índices ni JARs. Quien actúe, que abra el README del proyecto el día que actúe.

Si un repo se archiva mañana, gana GitHub. Este texto se actualiza con lo verificado, no con el recorte de julio.

> La Bandita informa a partir de fuentes fechadas.

#Mihon #Aniyomi #Tadami #Miyomi #Keiyoushi #Yuzono #Extensiones #FOSS #LaBandita #Septiembre2026

---
COMENTARIO FIJADO — no forma parte del post. Primer comentario, fijar.

Extensiones Mihon / Aniyomi / Animetail — La Bandita
Fecha: 2026-09-13
Versión de esta publicación: BORRADOR 2026-09-13 (sustituye el corte 2026-07-25)

Índice (el mismo icono abre cada bloque)

⚡ Qué estaba mal el 25-jul
📜 De dónde sale
📱 Apps (números de hoy)
🗺️ Repos (estado, no receta)
🧬 HttpSource / KeiSource 1.6 / PR #448
🔞 Cursed (se nombra, no se enlaza)
🗂️ Miyomi (133 / 44)
📱 Mapa de apps
🧩 Mapa de extensiones
🌒 Lo que no estaba
🚪 Cómo leer el mapa
🐋 Tadami 3-en-1
🔎 Fuera de Miyomi
🧵 Capas
🔭 Poco nombrados
📋 Inventario
🛠️ Si algo se rompe
🌱 Vías oficiales
📌 Correcciones
🚧 Límites
✅ Acciones
📚 Fuentes

Corrección central: KeiSource 1.6 sí circula; Yūzōnō no está privado; Kohi-den archivado. Miyomi = directorio (133/44), no almacén. Tadami vivo = andarcanum v0.62. Poco nombrados: beer-psi, dragonx943, Gekkoushi/plugin-source, suiyuran, Nyora, TheNano=LittleSurvival, adly98, Shosetsu extras. Hollow FR archivado 6-sep. everfio=espejo. Nova=0★. timschneeb=DMCA. Esta guía no pega índices ni JARs.
