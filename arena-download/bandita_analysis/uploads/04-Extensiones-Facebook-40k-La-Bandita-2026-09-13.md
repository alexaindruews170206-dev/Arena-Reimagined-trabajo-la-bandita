# Publicación — Extensiones Mihon / Aniyomi / Animetail (La Bandita) · 2026-09-13
> BORRADOR · Facebook / La Bandita · no Discord. Perfil FACEBOOK (Manual 5.2).
> POST: copia desde la línea APPS Y EXTENSIONES hasta los hashtags (una pieza).
> COMENTARIO FIJADO: bloque del final. No publicar sin firma humana.
> Corte vivo: 2026-09-13. El texto de origen traía corte 2026-07-25; se verifica, no se recita.

APPS Y EXTENSIONES (MIHON, ANIYOMI, TADAMI, MIYOMI) · La Bandita · 2026-09-13 (BORRADOR · firma humana pendiente)
**Tiempo estimado de lectura: 32–42 min**
**Índice:** mapa + el mismo icono. Resumen: comentario.

# Mapa de apps y extensiones: Mihon, Aniyomi, Tadami, Miyomi y lo que el directorio no lista

**Corte de información:** 2026-09-13
**Clase predominante:** [Fuente] (GitHub API y páginas de proyecto abiertas hoy) y [Observación]. Sin instalar ninguna app ni ninguna extensión en un teléfono.
**Grado:** V2 parcial — repos y sitios de Keiyoushi, Yūzōnō, FelipeGFA, Kohi-den, Mihon, Aniyomi, Animetail, Komikku, TachiyomiSY, Miyomi, Tadami y MANGA Plus abiertos hoy. Wotaku.wiki (ficha a ficha) y Discord de Keiyoushi: no.
**Receptor:** La Bandita (Facebook). No va al ledger. No Discord.
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

keiyoushi/extensions
  Almacén (binarios / índice). 14.963 ★. 1.316 forks.
  Rama por defecto: repo. Público. No archivado.
  Último commit visto: keiyoushi-bot, «Update extensions
  repo», 12-sep-2026 (a7dd81d).
  Homepage: https://keiyoushi.github.io/
  README (hoy): índice en formato index.pb (no el
  index.min.json que recitaba el corte de julio como
  receta principal).
  [Fuente / Observación]

keiyoushi/extensions-source
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
yuzono/tachiyomi-extensions
  Código. 887 ★. Apache-2.0. Push 13-sep-2026.
  «Source code of extensions for Komikku / Mihon & forks.»
  CONTRIBUTING.md tocado 12-sep-2026
  («Fix outdated/contradictory claims»). [Fuente]

yuzono/anime-extensions
  426 ★. Apache-2.0. Push 13-sep-2026 (hoy). [Fuente]
  El corte de julio decía el índice de anime «caído».
  El repo de distribución yuzono/anime-repo (59 ★)
  se empujó hoy 13-sep-2026 17:38 UTC. Un GET al
  index.min.json de ese repo respondió 200.
  [Observación] «Caído» en julio no se sostiene hoy.

yuzono/manga-repo
  Fork de keiyoushi/extensions. 4 ★. Push 18-ago-2026.
  Archivos vistos: README, index.json, index.min.json,
  repo.json. index.pb: 404. [Observación]
  El corte de julio daba un index.pb de manga-repo
  como «el que debes usar». Ese path no está.

yuzono/https://yuzono.github.io
  18 ★. Fork de keiyoushi/https://keiyoushi.github.io.
  Push 7-sep-2026. Sitio abierto hoy:
  «Extension repository for Mihon, Aniyomi and variants»
  con entradas Manga y Anime. [Fuente]

yuzono/aniyomi-extensions
  La API de GitHub devolvió HTTP 451 en esta sesión.
  No se afirma el interior del repo. [Observación]

yuzono/kohi-den
  Fork de Kohi-den/extensions-source. 3 ★.
  Push 12-may-2026 (antes del archivo del original).
  [Fuente]
```

«Privado en GitHub»: no, al corte. [Observación] «Cada 6 horas fusiona Keiyoushi»: no salió en las páginas abiertas. [No confirmado]

### 📙 FelipeGFA (pt-br)

```
FelipeGFA/extensoes
  Fork de keiyoushi/extensions. 41 ★ (el corte decía 35).
  «mainly focus on pt-br updates». Push 13-sep-2026.
  Índice index.min.json: HEAD 200. [Fuente / Observación]

FelipeGFA/anime-extensoes
  5 ★. Push 30-jul-2026. Índice: HEAD 200, cuerpo largo
  (~77 kB). [Observación] Más viejo que el de manga.

FelipeGFA/anime-fonte-extensoes
  4 ★. Apache-2.0. Push 17-ago-2026. Código. [Fuente]

FelipeGFA/fonte-extensoes
  1 ★. Push 13-sep-2026. Descripción: source de
  keiyoushi/extensions. [Fuente]
```

El corte de julio mandaba a instalar anime-fonte-extensoes con la URL de yuzono/anime-repo. Eso mezcla proyectos. No se receta. [Observación]

### 📕 Kohi-den

```
Kohi-den/extensions-source
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

**HttpSource.** Clase base clásica. No se copia un esqueleto de scraper. [Observación]

**KeiSource 1.6.** Convención de contribuidor. CONTRIBUTING de yuzono/tachiyomi-extensions (1.813 líneas; encabezado + snippet): fuentes nuevas extienden `KeiSource` con `libVersion = "1.6"`; `HttpSource` queda legado (`1.4`). Corregido 12-sep-2026 (#19013). [Fuente] No se afirma que todo Keiyoushi ya esté en 1.6. [No confirmado el censo]

keiyoushi/extensions-source, ayer: «MangaParkPublisher: 1.6» (#19016). [Fuente] Prueba que «1.6» circula, no un producto comercial.

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
yuzono/cursed-manga-extensions
  Código. 185 ★. Apache-2.0. Push 9-sep-2026. [Fuente]

yuzono/cursed-manga-repo
  Distribución. 158 ★. Push 3-ago-2026.
  Un GET al index.min.json respondió 200.
  [Observación] El corte decía el índice de Yūzōnō
  cursed «caído». Hoy el archivo responde.

mojuru/cursed-manga-repo
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
                   salmanbappi/extensions-repo

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
Awerkori/extensoes
  Fork de FelipeGFA/extensoes. 3 ★. Push 13-sep-2026.
  index.pb e index.min.json responden 200.
  [Fuente / Observación] No se pegan.

Awerkori/anime-extensoes
  «Project Nox Anime — repositorio de extensiones
  compiladas». 3 ★. Push 13-sep-2026.
  index.min.json responde 200 (~82 kB).
  [Fuente / Observación] No se pega.
  En el catálogo Miyomi de hoy NO aparece como
  fila aparte (el Nox listado es el de manga).
  Hueco del directorio, no de GitHub.

Awerkori/anime-fonte-extensoes
  Código. 3 ★. Apache-2.0. Push 13-sep-2026.
  Un fork julia5454554/anime-fonte-extensoes existe
  (0 ★). [Fuente]

Awerkori/project-nox-requests
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

andarcanum/Tadami-Aniyomi-fork
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
codegeasse1/yomi-reader
  8 ★. Apache-2.0. Push 6-sep-2026.
  «Yomi — anime, manga, and novel reader
  (Tadami/Aniyomi-compatible)». [Fuente]
  No está en Miyomi.

Freitez93/Tadami-Extensions
  0 ★. Push 13-ago-2026. Personal.
  «Algunas extensiones para Aniyomi/Tadami».
  [Fuente] Madurez: baja. No se receta.
```

Extensiones que Miyomi marca compatibles con Tadami (ya salieron en las 44): Keiyoushi, Yuzono Anime, Yuzono Cursed, Project Nox, Nyora, Suwayomi, TheNano, Kavita, LNReader Plugins, Novel Sourcery, Hollow, Secozzi, SalmanBappi, etc. Eso es el campo `compatible_with` del directorio, no un test en un teléfono. [Fuente — catálogo Miyomi]

---
## 🔎 Fuera de Miyomi (GitHub, 13-sep)

Lo que el censo 133/44 no trae como fila, o trae con URL vieja. Sin índices. Detalle de calidad: 🔭.

```
cuong-tran/manga-repo     444 ★  almacén grande de Yūzōnō
                         (yuzono/manga-repo tiene 4 ★)
amrkmn/x                  39 ★  espejo Keiyoushi+Yuzono+Kohi-den
MO350AZ/extensions-no-nsfw 3 ★  filtro NSFW de Keiyoushi
aniyomiorg/aniyomi-extensions  archivado, 852 ★, ago-2024
Chimahon/chimahon         198 ★  Miyomi aún dice sohilsayed/
HaoweiLi97/mihon_img_upscale 194 ★  fork Mihon + upscale
Kotatsu-Redo/kotatsu-parsers-redo  44 ★  parsers, no índice Mihon
wotakumoe/wotaku        3.045 ★  otro índice (no se recorrió)
```

[Fuente — GitHub 13-sep] No se recetan. 0★/SEO: fuera.

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

## 🔭 Poco nombrados (calidad, no fama)

Censo GitHub/Codeberg 13-sep. Filtro: código propio o licencia, push 2026, no espejo vacío de Keiyoushi, no granja SEO, no 0★ de dos días. Estrellas = página o API hoy. **Sin índices.** [Observación]

**Fuera de las 44 de Miyomi**

```
beer-psi/tachiyomi-unofficial-extensions
  53 ★. Apache-2.0. 144 commits. Push 29-ago-2026.
  src/ propio. Pipeline alineado a Keiyoushi.
  El README avisa el riesgo de fuente no oficial.
  [Fuente]

dragonx943/manga-repo
  22 ★. GPL-3.0. 70 commits. Push 5-sep-2026.
  Parsers vietnamitas (Tsuki) para Usagi, no Mihon.
  [Fuente]

Gekkoushi/plugin-source
  90 ★. GPL-3.0. 2.416 commits. Push hoy.
  Código de parsers Usagi. Miyomi lista Gekkoushi/plugin
  (artefactos; README: «no updates, 1.3k sources»).
  [Fuente / Observación]

suiyuran/aidoku-zh-sources
  883 ★. Push 30-mar-2026. Aidoku chino.
  Sin SPDX en la API. Más ★ que el almacén comunitario;
  menos fresco. [Fuente]

Smexhy/yomu-aidoku-sources
  14 ★. Push 19-ago-2026. 7 fuentes Aidoku propias.
  No es Aidoku-Community. [Fuente]

adly98/aniyomi-ar-extensions
  5 ★. Apache-2.0. src/ar. Push 10-may-2026.
  Árabe. Estructura real, ★ bajas. [Fuente]

msrofficial/anime-extensions
  3 ★. Apache-2.0. src/hi. Push 22-may-2026.
  Anikku/Aniyomi, recortado a lo que mantienen. [Fuente]

noaione/shosetsu-extensions
  19 ★. GPL-3.0. 651 commits. Push 20-may-2026.
jobobby04/ShosetsuExtensions
  16 ★. GPL-3.0. 123 commits. Push 11-abr-2026.
  Shosetsu está en las 133; estos almacenes no en las 44.
  [Fuente]
```

**En Miyomi, mal nombrados o mal fechados**

LittleSurvival/copymanga-copy20 = «TheNano»
  2.743 ★. Chino. Push 8-sep-2026. [Fuente]

Nyora-Manga/nyora-mihon
  10 ★. Un paquete que embebe kotatsu-parsers
  (~900 fuentes en el dispositivo). v1.6.19 (19-jul).
  [Fuente]

Aidoku-Community/sources
  584 ★. Apache-2.0 OR MIT. Aidoku 0.7+.
Aidoku-Community/legacy-sources
  701 ★. README: ya no se mantiene; sucesor = sources.
  [Fuente]

IReaderorg/IReader-extensions
  32 ★. MPL-2.0. 486 commits. Push 27-ago-2026.
inkdex/extensions
  31 ★. Registry Paperback 0.9. Push 22-ago. [Fuente]

https://codeberg.org/hollow/aniyomi-extensions-fr
  Archivado 6-sep-2026. Miyomi aún lo lista vivo.
  [Observación]

**Abiertos y descartados**

```
everfio/tachiyomi-extensions 37 ★: espejo de Keiyoushi,
  5 commits, sin código propio. [Observación]
WendySBlanc/extensions («Nova») 0 ★: fork con CI
  (12 commits de ventaja); madurez pública baja.
timschneeb/tachiyomi-extensions-archive 1.802 ★:
  archivado 23-mar-2026. README: DMCA, historial
  borrado. No es almacén.
ThePBone/tachiyomi-extensions-revived: al corte
  resuelve a ese archivo. [Observación]
Koray-Ozt/k-kitsu-extensions: 404. [No encontrado]
Repos con index.min.json en el nombre: granja.
```

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
- Checksums Animetail: no se copian.
- No es envío.
```
---
## ✅ Acciones concretas

**Si solo querías entender el mapa.** Con esto basta. Reabre GitHub el día que cites una estrella.

**Si usas Mihon y Keiyoushi ya te funciona.** El 25-jul no es tu corte. El de Keiyoushi, sí: 0.20.4+ y el formato de índice que su getting-started muestre **ese día**.

**Si Aniyomi o Animetail te fallan con extensiones de Keiyoushi.** Keiyoushi dice que no te soporta. No es un misterio de ClassLoader que esta guía vaya a «resolver» con un índice pegado. [Fuente / Observación]

**Si Kohi-den era tu almacén de anime.** Está archivado desde mayo. No hay promesa de que vuelva. [Fuente]

**Si te llega un video «pega esta URL».** Esa es la receta que esta guía no va a copiar. El README del proyecto, abierto el mismo día, manda sobre un screenshot de julio.

**Si lo que quieres es leer o ver sin esa zona gris.** MANGA Plus está abierto hoy. El resto de catálogos oficiales, el día que los abras.

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
**Cierre.** El ecosistema sigue vivo el 13-sep-2026: Keiyoushi empuja, Yūzōnō es público, FelipeGFA actualiza pt-br, Kohi-den está archivado, KeiSource 1.6 no es un mito, y el PR #448 de Animetail sí habla de carga 1.6+. Miyomi cuenta 133 apps y 44 ext; Tadami vivo es andarcanum v0.62 (Miyomi aún dice 0.60). El 25-jul acertó el archivo de Kohi-den y la fecha del PR; falló estrellas, «caídas» que hoy responden, el «no existe» de 1.6 y el soporte de Keiyoushi (Mihon / SY / Komikku, no Aniyomi). Esta guía no pega índices ni JARs. Quien actúe, que abra el README del proyecto el día que actúe.

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
🛠️ Si algo se rompe
🌱 Vías oficiales
📌 Correcciones
🚧 Límites
✅ Acciones
📚 Fuentes

Corrección central: KeiSource 1.6 sí circula; Yūzōnō no está privado; Kohi-den archivado. Miyomi = directorio (133/44), no almacén. Tadami vivo = andarcanum v0.62. Poco nombrados abiertos hoy: beer-psi, dragonx943, Gekkoushi/plugin-source, suiyuran, Nyora (kotatsu en Mihon), TheNano=LittleSurvival. Hollow FR archivado 6-sep. Esta guía no pega índices ni JARs.
