# Publicación — Kototoro (La Bandita) · 2026-09-13
> BORRADOR · WhatsApp / La Bandita · no Discord. No Facebook (límite ~40k).
> POST: un solo mensaje. Copia desde la línea KOTOTORO hasta el cierre.
> Tope 63k (cabe en un mensaje de WhatsApp). Lista completa: aquí vive.
> Si el chat permite fijar: el bloque del final. Si no, el mapa ya está arriba.
> No publicar sin firma humana.

KOTOTORO — GUÍA DE LA BANDITA · 2026-09-13 (BORRADOR · firma humana pendiente)


**Tiempo estimado de lectura: 40–50 min**
**Índice:** mapa de arriba + el mismo icono en cada título. Resumen en el comentario fijado.

# 📚 Kototoro — manga, novelas y vídeo en una sola biblioteca

**Corte de información:** 2026-09-13
**Clase de afirmación predominante:** declaración de fuente y observación.
**Grado:** V2 parcial — README, LICENSE, releases y docs leídos en vivo el 2026-09-13. Repos de extensiones revalidados por API de GitHub el mismo día. Sin instalación ni auditoría de binarios.

**Criterio:** utilidad + actividad + confianza comunitaria. «Mejor» aquí significa mejor según este criterio y este corte, nunca mejor para todo el mundo.

**Alcance:** ficha central de Kototoro; catálogo de lectura (lectores, extensiones y servidores de biblioteca); el resto es directorio de contexto con enlaces comprobados, no recomendación.

**Idea en una imagen:** tres apps con avisos por todas partes frente a una estantería de tres cajones (Manga, Novela, Vídeo). Unificar ahorra saltos, pero multiplica dependencias: mira qué junta y qué te pide a cambio.

```
Mapa de esta guía. El mismo icono abre cada bloque.
Índice corto: mensaje fijado si el chat lo permite; si no, este mapa.

├── ℹ️  Qué es Kototoro
├── 🧭  Estado verificado al corte
├── 🏗️  Arquitectura: cómo está construido
├── ⚙️  Características principales
├── 🔌  Extensiones y fuentes: qué se conecta y cómo
├── 🎯  Para quién puede tener sentido
├── ♿  Accesibilidad y comodidad de lectura
├── 🧪  Qué revisar antes de instalar
├── 💾  Instalación y primera prueba sin arriesgar tu biblioteca
├── 🧩  Compatibilidad declarada
├── 🔄  Migración desde otros lectores y archivos
├── 🪪  Entity Organize: identidad entre fuentes
├── 🛠️  Solución de problemas
├── ⚖️  Comparativas con criterio declarado
├── 🎚️  Curaduría consciente y arquitectura de filtrado
├── 🔒  Seguridad y cadena de suministro
├── 🗺️  Directorio del ecosistema
├── ❓  Preguntas frecuentes
├── 📖  Glosario
├── 👤  Configuraciones recomendadas por perfil
├── 📓  Historia de uso — contada por un miembro de la banda
├── 🕰️  Evolución reciente
└── 🏁  Conclusión, límites y no-asunciones
```

**Etiquetas usadas en el cuerpo:**
`[Fuente]` = lo que el proyecto declara de sí mismo.
`[Observación]` = señal localizada y comprobada al corte.
`[Inferencia]` = conclusión razonable a partir de hechos.
`[Declaración]` = lo que dice una persona de la banda, sin verificación propia.
`[No confirmado]` = dato sin validación cruzada al corte.

---

## ℹ️ Qué es Kototoro

Repositorio:   [Kototoro-app/Kototoro](https://github.com/Kototoro-app/Kototoro)
Rama:          devel (confirmada) · 8 ramas · 196 tags · 6.950 commits
Métricas:      569 estrellas · 46 forks · 57 issues abiertos (GitHub API, 2026-09-13) [Observación]
Versión:       v2.1.1 (latest, publicada 2026-09-13 07:36 UTC) — ritmo casi diario:
               COMPRUEBA LA RELEASE VIGENTE en GitHub Releases
Licencia:      Apache-2.0 (LICENSE leído el 2026-09-11; SPDX reconfirmado por API el 2026-09-13) [Observación]
Documentación: [kototoro-app.github.io/Kototoro](https://kototoro-app.github.io/Kototoro/) (viva)
               (histórica: skepsun.github.io/Kototoro) [Observación]
Releases:      [Kototoro-app/Kototoro/releases](https://github.com/Kototoro-app/Kototoro/releases)
ID paquete:    org.skepsun.kototoro
Android:       builds recientes piden Android 8.0+ [Fuente]
Estado:        desarrollo muy activo

Kototoro es una app Android de código abierto que reúne manga, novelas y vídeo en un solo lector, combinando compatibilidad amplia de fuentes con OCR + traducción local, super-resolución de vídeo y sincronización multi-dispositivo por WebDAV. [Fuente]

Un lector sencillo abre capítulos, recuerda progreso y organiza favoritos; Kototoro suma biblioteca común con entidades que fusionan la misma obra entre fuentes, tracking externo unificado y lectura/reproducción desde un mismo entorno. [Observación]

**Núcleo técnico declarado.** La propuesta se sostiene sobre cuatro pilares verificables: una interfaz construida íntegramente en Jetpack Compose; un sistema de parsers cargables en tiempo de ejecución que permite sumar fuentes sin recompilar; una capa de entidades que da identidad estable a cada obra independientemente de dónde se sirva; y un motor de OCR + traducción que puede operar sin llamadas remotas si se configuran los modelos locales. [Fuente]

**Origen y licencia.** El README vigente (leído 2026-09-13, rama devel) declara: *«Originally derived from Kotatsu, Kototoro is now independently developed as a multi-format, Compose-first reading/player platform… it is no longer a Kotatsu fork»* — deriva de Kotatsu, pero se declara desarrollo independiente y ya no un fork. [Fuente] El linaje que circula en la banda —«fork de Kotatsu/Usagi»— es memoria del usuario: lo anoto como [Declaración], no como ficha. Lo que sí es comprobable: Kotatsu quedó descontinuado, y de su familia siguen activos forks como Usagi (que no trae fuentes integradas por defecto), Futon y Kotatsu-Redo, mientras Yumemi y Yukimi quedaron archivados. [Observación de la comunidad; no revalidado repo a repo] El proyecto acepta donaciones vía 爱发电 (ifdian) y tiene Discord oficial: señal de comunidad activa. [Fuente]

Fichas de versiones anteriores (v1.9.1, agosto 2026) aún declaraban que el proyecto seguía la licencia GPL-3.0 del Kotatsu original. [Observación previa, no revalidada] El LICENSE del repo es Apache-2.0; SPDX reconfirmado por la API el 2026-09-13. [Observación] La transición GPL→Apache queda confirmada como declaración, no como auditoría del código: revisar los archivos fuente uno por uno si se redistribuye.

La licencia Apache-2.0 cubre el código. Recursos gráficos, modelos de OCR y componentes de terceros pueden tener licencias propias: revísalas antes de redistribuir. [Inferencia]

> La Bandita informa a partir de fuentes fechadas. Comprueba permisos, licencia, procedencia y compatibilidad antes de usarlo.

### Descargas

La estructura de assets por arquitectura sigue el patrón habitual de Android:

```
Asset                       Para quién
──────────────────────────────────────────────────────────
arm64-v8a-release.apk       la mayoría de los teléfonos [Inferencia]
armeabi-v7a-release.apk     teléfonos viejos de 32 bits [Inferencia]
release.apk (universal)     solo si no sabes tu arquitectura
x86 / x86_64                emuladores y PCs [Inferencia]
```

Regla práctica: teléfono normal → arm64-v8a; universal solo si ignoras tu arquitectura. El paquete es `org.skepsun.kototoro` y pide Android 8.0 o superior. [Fuente] Verifica hash contra el publicado en la release antes de instalar.

---

## 🧭 Estado verificado al corte

```
Última release (GitHub Releases + API, 2026-09-13): v2.1.1 — 13-sep 07:36 UTC
Anteriores (tags): v2.1.0 · v2.0.10 · v2.0.9 · v2.0.8
Ritmo: casi diario
3 commits en devel por encima de v2.1.1 al corte [Observación]
```

APKs de v2.1.1 (API, tamaños y descargas de los assets; no se bajaron):

```
arm64-v8a     125.313.479 B   488 descargas
armeabi-v7a   117.421.379 B    20
universal     312.864.367 B    47
x86           139.876.735 B     2
x86_64        146.944.827 B     2
```

Notas de v2.1.1 (leídas 2026-09-13): UI inicial para TV; crash en chips de filtro de fuentes unificadas; chips de título del lector; «fix(backup): review and discard orphaned work state»; docs del plan de TV UI; layout de la pestaña de traducción. [Fuente] Eso no prueba que el episodio de respaldos 1.4–1.7 esté cerrado. [Inferencia] Cualquier cifra caduca en horas.

**Cachés y espejos van con retraso.** Las páginas de releases en caché pueden mostrar versiones de julio mientras el repositorio publica la serie 2.x. Las fichas de tiendas alternativas suelen ir una o dos versiones por detrás. La única referencia fiable es la página de releases consultada en vivo. [Inferencia]

**Nightly — corrección respecto al 2026-09-11.** Entonces era stub. Hoy [Kototoro-app/Kototoro-Nightly](https://github.com/Kototoro-app/Kototoro-Nightly) está vivo (8★, 1 fork, no archivado). Última vista: nightly-20260913 (13-sep 16:57 UTC, prerelease). La lista carga al menos desde nightly-20260909. Cada una, 5 APKs (arm64 / armeabi-v7a / universal / x86 / x86_64), nombres Kototoro-NYYYYMMDD-…. /releases/latest sigue 404 porque todas son prerelease. [Observación] Sirve para probar devel, no para biblioteca diaria. Estable = releases del repo principal.

---


## 🏗️ Arquitectura: cómo está construido

**Compose de punta a punta.** Kototoro se presenta como posiblemente una de las primeras apps de lectura de manga, novela y vídeo genuinamente all-Compose: el lector de cómics/novelas y el reproductor de vídeo también usan Compose, no solo las pantallas exteriores. Las capas antiguas de XML, Fragment y transiciones híbridas se redujeron al mínimo. [Fuente]

Esto importa porque no estamos ante un lector clásico con una capa moderna encima, sino ante un intento de reconstruir la experiencia de lectura y reproducción alrededor de Compose: gestos, animaciones Hero, paleta dinámica y transiciones se apoyan en el mismo motor. [Inferencia]

**Sistema de plugins dinámicos.** Antes los parsers iban compilados dentro de la app (kototoro-parsers + kotatsu-parsers-redo): acoplaba los releases, inflaba el APK y ralentizaba la compilación. La arquitectura vigente los extrae a `.jar` (Dex) que se cargan en tiempo de ejecución: intercambio en caliente sin tocar el APK principal. [Fuente] El contrato común es el módulo `parser-api` (interfaces `ContentParser`, `MangaParser`, `ContentSource`, `ContentLoaderContext`), que los plugins dependen como `compileOnly` vía JitPack (`com.github.skepsun.Kototoro:parser-api`), así no duplican las interfaces. [Fuente]

```text
Pipeline de un plugin (GitHub Actions):
código de parsers (repo aparte)
  -> compilación Kotlin (.jar)
  -> d8 (dexer de Android SDK) -> classes.dex -> plugin.jar
  -> generate_index.py -> index.min.json
  -> rama "repo" que espeja los repos de extensiones estilo Mihon
```

La carga usa un `PluginClassLoader` de «zero-overhead»: intercepta el namespace `org.koitharu.kotatsu.parsers.*` y lo delega al ClassLoader de la app anfitriona, así el host hace cast directo sin reflection; cada JAR vive en su propio classloader (aislamiento de clases). [Fuente] Hay **arquitectura dual**: carga colecciones Kotatsu (`MangaParserFactoryKt`) y colecciones nativas Kototoro (`ContentParserFactoryKt`) indistintamente, y `GlobalExtensionManager` es la única fuente de verdad que agrega JARs + APKs y deduplica por prefijo. [Fuente] Flujo de uso: Ajustes → Remote Sources → Installed Plugins → Import Plugin (.jar) → se copia a files/plugins/ y queda disponible al instante. [Fuente]

```
Nativo Kototoro    -> parsers propios integrados
Kotatsu-Redo       -> biblioteca completa de parsers incluida
Mihon / Aniyomi    -> se detectan como APK de extensión instalados
IReader            -> APK de extensión de novelas
Legado / TVBox     -> se importan como JSON (archivo, texto o URL)
CloudStream3       -> declarado en el README actual
```

Si los parsers se actualizan con la app, ganas comodidad y pierdes control fino: lee el changelog de cada release. [Inferencia]

**Actualizaciones delta.** Kototoro documenta un mecanismo OTA con `bsdiff/bspatch`: si vienes exactamente de la versión anterior esperada, la app puede descargar solo el parche diferencial; si saltaste versiones o vienes de una build custom, cae a descarga completa del APK. [Fuente]

**Navegador con manejo de desafíos.** Las fuentes protegidas por Cloudflare se resuelven con WebView sin interfaz o con flujo interactivo en el navegador integrado, siguiendo el enfoque que ya había usado kotatsu-redo. No es garantía de que toda fuente protegida funcione siempre: las webs cambian, y las extensiones pueden romperse. [Fuente]

**Entidades y espacios.** El sistema de entidades busca que una obra tenga una identidad estable aunque exista en varias fuentes, archivos locales o servicios de tracking. Favoritos, historial, progreso, estadísticas y seguimiento pertenecen a la «obra», no a una única URL o fuente reemplazable. [Fuente]

```
Obra / Work         -> identidad estable
Projection          -> entrada concreta desde fuente, archivo o extensión
Default projection  -> fuente preferida para abrir/leer/reproducir
Tracking binding    -> enlace a MAL, AniList, Kitsu, Bangumi, Shikimori, etc.
Espacios            -> agrupación por tipo, idioma y fuente (Manga, Novelas, Anime)
```

Esta separación es la que permite, por ejemplo, que una serie leída desde una extensión de Mihon y la misma serie leída desde un CBZ local no aparezcan como dos favoritos distintos, sino como dos proyecciones de la misma obra. [Inferencia]

```
Mapa de dependencias

Kototoro
├── Parsers nativos + Kotatsu-Redo (integrados)
├── Extensiones Mihon / Aniyomi / IReader (APK)
├── Fuentes Legado / TVBox / CloudStream3 (JSON / repositorio)
├── Modelos OCR y traducción (descargables, ocupan espacio)
├── WebDAV propio (sincronización, si la activas)
└── Servicios de seguimiento externos
```

---


## ⚙️ Características principales

**📚 Lectura unificada.** Una app para manga, novelas y vídeo, con OCR + traducción automática local directamente dentro del lector. Historial y favoritos compartidos entre los tres tipos de contenido. [Fuente]

**🔍 OCR y traducción en dos etapas.** El flujo declarado: detección y reconocimiento del texto de la página, envío al traductor configurado y resultado como capa sobre la imagen original. [Fuente]

```
Modo Local    -> modelo ONNX local si existe, luego ML Kit en el teléfono.
                 No llama a ninguna API remota de traducción.
Modo API only -> envía el texto reconocido al servicio en línea que
                 configures. Necesita endpoint y clave antes de activarse.
OCR Basic     -> ML Kit en el teléfono, sin paquete adicional.
OCR Advanced  -> paquete de 5 modelos con descarga y verificación previa.
```

Los ajustes viven en Ajustes → AI: modelos locales, servicio de traducción en línea, traducción, mejora de imagen (Anime4K, RealCUGAN, Real-ESRGAN), TTS para novelas y mejora de vídeo. [Fuente] Para manga hay re-traducción por página, capítulo o páginas fallidas, y panel de tareas con estados. Para novelas hay streaming por párrafos con caché y modos solo-traducción o bilingüe. [Fuente]

> [!WARNING] El OCR puede equivocarse con tipografías decorativas, texto vertical, onomatopeyas y baja resolución. No des por buena ninguna transcripción sin revisarla.

> [!IMPORTANT] En modo API el texto reconocido sale de tu teléfono hacia el proveedor que configures, y tu clave queda guardada en la app. En modo Local el reconocimiento ocurre en el teléfono, pero los modelos se descargan y ocupan espacio. Revisa en Ajustes qué tienes activado. [Inferencia]

Traducción en cadena: bocadillo → OCR → traducción → capa superpuesta. Si una página mixta falla, fija el idioma manual. [Fuente]

**🎬 Reproductor con super-resolución.** Filtros Anime4K para vídeo, envío DLNA por red local, selección de pistas de audio y subtítulos, controles de reproducción y gestos. [Fuente]

**☁️ Sincronización WebDAV.** Respaldo y sincronización multi-dispositivo por timestamp, sin cuenta cautiva (también declara Google Drive). Sincroniza favoritos, historial, progreso de lectura, grupos y, donde aplique, credenciales de acceso y estado de fuentes. [Fuente]

```
Flujo recomendado:

1. Ajustes -> Backup & Restore
2. Configura endpoint WebDAV, usuario y contraseña
3. Prueba backup/restore en un dispositivo
4. Usa un dispositivo como fuente de verdad
5. Restaura en el segundo dispositivo
6. Solo después activa rutina de sincronización normal
```

> [!IMPORTANT] WebDAV no significa nube segura por arte de magia. La seguridad depende del servidor, del TLS, de las credenciales y de quién administre ese servidor. Como puede sincronizar credenciales, verifica la configuración antes de depender de ella.

**🧩 Seguimiento externo.** MAL, Kitsu, AniList, Bangumi, Shikimori y MangaUpdates. [Fuente]

**🧭 Asistente inicial.** Tras instalar, la guía oficial pide completar el wizard integrado para configurar espejos de GitHub, descargar los plugins base de fuentes y definir los tipos de contenido. [Fuente]

**🧰 Extras.** Bot de Telegram, widget, estadísticas, import de favoritos, modo e-ink. README (devel, 2026-09-13): Discord https://discord.gg/xBXvPz7tr7 ; 爱发电 [www.ifdian.net/a/kototoro](https://www.ifdian.net/a/kototoro) ; QQ 560955275 ; issues del repo. [Fuente] v2.1.1 declara UI inicial para TV: en las notas, no se probó en televisor. [Fuente / Observación]

**Novedades recientes de la serie 2.x.** Notas con anotaciones multimedia y tarjetas de excerpt con imágenes, filtrado space/NSFW, decodificación JPEG XL, rediseño de los ajustes de Spaces con espacios personalizados para todos los tipos de contenido, modos de vista previa en tablet configurables, longitud de título de imagen guardada configurable, lector de novelas renovado (controles, marcas, diccionario, notas, extractos, export MD), descargas adaptativas, menús unificados, paginación del lector, tabs segmentados en ajustes, búsqueda dentro del contenido de capítulos de novela, pulido de bookmarks y feed. [Fuente]

### Favoritos importados desde sitios

Con login en sitios compatibles (CopyManga, Zaimanhua, Komiic, Baozi, Manhuagui, Pica y un séptimo declarado) se pueden importar o sincronizar favoritos desde Favoritos → Import/Sync to Site. [Fuente] Úsalo solo con tus propias cuentas y contenido legítimo.

---

## 🔌 Extensiones y fuentes: qué se conecta y cómo

Kototoro trabaja con parsers propios integrados y con ecosistemas externos. El README vigente (2026-09-13) declara soporte para seis: Mihon, Aniyomi, IReader, Legado, TVBox y CloudStream3. [Fuente] Ojo con el matiz: la portada de la documentación oficial lista solo cinco (sin CloudStream3); el README sí lo nombra. Tómalo como soporte declarado, con la página de Source Integrations sin desarrollarlo al mismo nivel que los otros cinco: a comprobar en uso real. [Observación] Tras configurarse, todo aparece en Explorar → Content Sources y se usa igual que lo integrado. [Fuente]

```
Built-in / Kototoro        -> parsers propios
Kotatsu-Redo               -> biblioteca de parsers integrada
Mihon                      -> extensiones APK de manga
Aniyomi                    -> extensiones APK de anime/vídeo
IReader                    -> extensiones APK de novelas
Legado                     -> fuentes JSON
TVBox                      -> fuentes JSON de vídeo
CloudStream3               -> declarado en el README actual
```

**Cómo se instala cada tipo.**

```
Mihon / Aniyomi / IReader:
-> extensiones APK instaladas en el dispositivo
-> Kototoro las detecta al abrir o al refrescar
-> también se pueden gestionar desde repositorios internos
   dentro de la app (Ajustes -> Content Sources -> Extensions)

Legado / TVBox:
-> JSON desde archivo local
-> JSON pegado como texto
-> JSON desde URL en línea
-> se administran en el JSON Sources Directory
```

**Repositorios de terceros.** El proyecto declara explícitamente que la app **no distribuye ni recomienda ningún repositorio concreto**. [Fuente] Los nombres que circulan en listados de terceros (Keiyoushi, Yuzono Tachiyomi Extensions, LittleSurvival CopyManga Copy20, Project Nox, Yuzono Anime Extensions, XIU2/Yuedu) son puntos de partida comunitarios que debes verificar tú, nunca aval oficial del proyecto. [Observación]

**Cinco capas separadas.** App ≠ servidor ≠ extensión ≠ proveedor ≠ obra: la licencia de la herramienta no autoriza la obra, y un parser no prueba fuente estable, legítima o segura. El propio proyecto declara que sus desarrolladores no tienen afiliación con los proveedores de contenido ni mantienen repositorios de extensiones. [Fuente]

> [!NOTE] Compatibilidad funcional no significa compatibilidad completa: una extensión puede cargar y aun así fallar en fuentes concretas. [Inferencia]

**Directorios de terceros van con retraso.** Las fichas de tiendas y agregadores muestran versiones muy anteriores a la vigente. [Observación] La referencia es siempre la página de releases.

### Límites que el propio proyecto declara

Disponibilidad = lo instalado o importado; compatibilidad = versión de extensión + sitio; Legado/TVBox = calidad del JSON externo; TVBox parcial en JS/JAR/guards; todo lo externo hereda roturas cuando cambia el sitio; Kotatsu-Redo atado a las releases de la app. [Fuente]

---


## 🎯 Para quién puede tener sentido

Puede interesarte si:

```
📖 Quieres reunir manga y novelas en una biblioteca común
🧠 Valoras una interfaz moderna y unificada
🔍 Te sirve el OCR o la traducción asistida
☁️ Usas varios teléfonos y ya administras WebDAV
🧩 Quieres fusionar duplicados bajo identidades estables
🧪 Te compensa experimentar con seis ecosistemas de fuentes
```

Quizá no sea lo más cómodo si:

```
📄 Solo lees archivos locales y buscas la mínima superficie posible
🔒 No quieres configurar servidores ni cuentas
🧩 Prefieres separar manga, novelas y vídeo en apps distintas
🛡️ Necesitas una versión muy estable con cambios mínimos
📱 Tu teléfono anda justo de almacenamiento (modelos + cachés pesan)
🧪 No quieres convivir con funciones en expansión
```

```
Dificultad real estimada

🟢 Principiante   leer archivos locales y navegar lo integrado
🟡 Intermedio     añadir repositorios y gestionar extensiones
🟠 Avanzado       WebDAV multi-teléfono, JSON de Legado/TVBox, OCR avanzado
🔴 Experto        auditar extensiones de terceros y depurar runtimes
```

---

## ♿ Accesibilidad y comodidad de lectura

Opciones declaradas: diseño configurable del lector de manga, TTS para novelas con motor y voz configurables, modo bilingüe, modo e-ink, selección de subtítulos y audio, descargas offline, animaciones Hero y paleta dinámica ajustables desde Apariencia. [Fuente]

Lo no auditado al corte: lector de pantalla, contraste real en temas claros y oscuros, navegación completa por teclado o control externo, accesibilidad para daltonismo, tamaño mínimo cómodo de controles, comportamiento en tablets y foldables más allá de lo declarado. Si dependes de estas funciones, prueba 5 títulos antes de migrar tu biblioteca. [Observación]

---

## 🧪 Qué revisar antes de instalar

```
Aspecto       Qué comprobar                        Por qué importa
──────────────────────────────────────────────────────────────────────
Versión       tag, release y fecha en GitHub       evita builds sin respaldo
Licencia      código, recursos y modelos           pueden diferir entre sí
Permisos      lo que pide el instalador            detecta accesos innecesarios
OCR           local, remoto o híbrido              afecta privacidad y espacio
Traducción    modo Local o API con clave           el texto puede salir del teléfono
Sincronía     qué sincroniza y dónde               puede incluir credenciales
Respaldo      exportar e importar funcionan        necesario para volver atrás
Formatos      CBZ, EPUB, TXT, MKV, MP4             define qué podrás abrir
Mantenimiento releases, commits, issues            estado observable del proyecto
```

**Permisos del manifiesto fuente.** La lista es extensa y varía por versión. Un análisis externo de una build reciente señala consulta/instalación/borrado de paquetes, gestión de cuentas y acceso amplio al almacenamiento; una build de la serie 0.8.x declaraba 29 permisos. [Observación] Lee el listado exacto de la versión que instales; el manifiesto fuente puede sumar más permisos al fusionarse con librerías. [Inferencia]

```
Grupo            Permisos típicos
──────────────────────────────────────────────────────────────────────
Red              INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE
DLNA             CHANGE_WIFI_MULTICAST_STATE (descubrimiento SSDP)
Ejecución        FOREGROUND_SERVICE (+ MEDIA_PLAYBACK, DATA_SYNC),
                 WAKE_LOCK, VIBRATE, RECEIVE_BOOT_COMPLETED,
                 REQUEST_IGNORE_BATTERY_OPTIMIZATIONS, POST_NOTIFICATIONS
Cuentas/sync     GET/MANAGE/AUTHENTICATE_ACCOUNTS, USE_CREDENTIALS,
                 READ_SYNC_STATS/SETTINGS, WRITE_SYNC_SETTINGS
Paquetes         REQUEST_INSTALL_PACKAGES, REQUEST_DELETE_PACKAGES,
                 QUERY_ALL_PACKAGES (detección de extensiones)
Almacenamiento   WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
```

Sensibles por uso inferido: consulta de paquetes (detectar extensiones); instalación de paquetes (instalar desde releases); almacenamiento amplio (biblioteca local); cuentas/sync (sincronización); batería y arranque (segundo plano). [Inferencia] Niega lo que no necesites; los accesos elevados solo con razón proporcional y respaldo probado.

```
🟢 Buena señal: docs claras, releases identificables, respaldo probado
🟡 Prudencia: muchas funciones experimentales o docs incompletas
🔴 Pausa: APK de origen dudoso, enlaces que no coinciden, sin respaldo
```

---

## 💾 Instalación y primera prueba sin arriesgar tu biblioteca

1. Respalda tu lector actual y guárdalo aparte
2. Descarga solo de [Kototoro-app/Kototoro/releases](https://github.com/Kototoro-app/Kototoro/releases)
   y compara hash
3. Instala tu arquitectura; revisa permisos; completa el wizard
4. Configura idioma y espacios, OCR desactivado al inicio
5. Prueba 5 títulos (2 locales, 2 integrados, 1 externo)
6. Si va bien, 10-15 antes de migrar más
7. Conserva tu app anterior hasta confirmar el regreso

> [!IMPORTANT] Antes de migrar conserva copia, hash y el camino de vuelta. No actives WebDAV hasta entender qué sincroniza, y prueba respaldo y restauración en un solo teléfono primero.

**Problemas previsibles y qué hacer.** [Observación]

```
Síntoma                  Comprobación                  Solución
────────────────────────────────────────────────────────────────────────
Extensión no aparece     ¿APK instalado? ¿pestaña      reinstala, refresca la
                         correcta?                     pantalla de extensiones
Fuente protegida         ¿desafío interactivo?         usa el flujo de navegador
JSON no importa          ¿tipo Legado o TVBox?         reimporta con el tipo
                         ¿URL alcanzable?              correcto
Traducción no arranca    ¿modo Local o API?            configura motor o clave
                         ¿idiomas origen/destino?      y reintenta por página
Dispositivos distintos   ¿quién tiene lo más nuevo?    respalda ahí y restaura
                                                       en el rezagado
```

**Mantenimiento.** Actualiza desde releases, revisa el changelog, respalda antes de cada salto y limpia cachés y modelos sin uso. Lo que se instala y se olvida deja de funcionar en silencio.

**Actualizar sin romper.** Dos caminos: en la app (delta si vienes de la versión anterior exacta, completa si saltaste) o manual desde releases. [Fuente] Tras cada salto abre la biblioteca, prueba una fuente por ecosistema y pasa Entity Organize primero sobre poco antes que sobre todo. Bajar de versión exige respaldo previo. [Inferencia]

---


## 🧩 Compatibilidad declarada

```
Área              Estado          Detalle
────────────────────────────────────────────────────────────────────────
Ext. Mihon        Confirmada      ecosistema declarado en README [Fuente]
Ext. Aniyomi      Confirmada      ecosistema declarado en README [Fuente]
Ext. IReader      Confirmada      ecosistema declarado en README [Fuente]
Legado / TVBox    Confirmada      JSON; calidad-dependiente [Fuente]
CloudStream3      Declarada       en README, ausente en la portada de
                                  la docs; a comprobar en uso [Observación]
Android           Confirmada      builds recientes piden Android 8.0+ [Fuente]
Servidores biblio No confirmada   sin integración directa documentada
                                  con Komga/Kavita/Suwayomi/OPDS
```

**Mihon.** La referencia técnica declara detección de APKs de extensión, carga de `Source`/`CatalogueSource`, adaptación de red, cache y UI, y una ventana de compatibilidad de librería entre 1.2 y 1.9; las extensiones fuera de ese rango se rechazan. La verificación de firma no se fuerza según la documentación técnica. [Fuente]

> [!WARNING] Que una extensión cargue no significa que todas sus fuentes funcionen. Una web puede cambiar, bloquear scraping, romper filtros, modificar Cloudflare o alterar su HTML o API.

**TVBox por niveles.**

```
Más fiable:
- medios directos
- playlists
- listas live simples
- APIs CMS simples

Parcial / en expansión:
- type 4 JavaScript con QuickJS
- type 3 / csp_* JAR spiders

Especial:
- Guard-native JAR spiders con JNI/nativo
```

La propia documentación advierte que TVBox no debe tratarse como «todo funciona igual»: depende de la forma del JSON, runtime, spider, dependencias y comportamiento del sitio. [Fuente]

**CloudStream3.** El README vigente declara soporte, y el archivo de build visible incluye preparación de un runtime jar de CloudStream3. La portada de la documentación no lo lista entre los ecosistemas principales: trátalo como soporte declarado, a comprobar en uso real. [Observación]

Rangos finos de versión de extensión, minSdk exacto y detalles de runtime TVBox requieren lectura del manifiesto y docs de la release vigente; no se revalidaron al corte.

---

## 🔄 Migración desde otros lectores y archivos

**Formatos por tipo** (la importación bloquea extensiones que no correspondan al tipo elegido):

```
Manga / cómics:
- .zip
- .cbz
- carpetas con imágenes: .jpg, .png, .webp

Novelas:
- .epub
- .txt

Vídeo / anime:
- .mp4
- .mkv
- .ts
- .webm
- .avi
- .m3u8
```

En autodetección, el tipo se adivina por extensión; con `.txt` o carpetas mixtas conviene elegir el tipo explícito. [Fuente]

**Estructura de carpetas.**

```
Carpeta única = una serie

Attack on Titan Season 1/
├── Episode 01.mp4
├── Episode 02.mp4
└── Episode 03.mkv
```

```
Carpeta múltiple = biblioteca con varias series

Mi Biblioteca/
├── Naruto/
│   ├── Ep01.mp4
│   └── Ep02.mp4
└── Bleach/
    ├── Ep01.mkv
    └── Ep02.mkv
```

**Metadatos con `index.json`.** Si tu carpeta o CBZ trae un `index.json` válido, se lee (títulos, autores, descripción, portada, etiquetas, grupos); si no existe, la app puede generarlo; y puedes editarlo a mano (la app lo respeta en el siguiente escaneo) o retocarlo desde la interfaz. [Fuente] Importar: Ajustes → Content Sources → Local Storage → + → tipo → archivo/carpeta → espera el aviso. Los archivos se copian a su estructura interna. [Fuente]

**Respaldos de otras apps.** En el código fuente hay repositorios de exportación/importación de respaldos de Mihon, Aniyomi y Usagi (`MihonBackupExportRepository`, `AniyomiBackupExportRepository`, `UsagiBackupExportRepository`): la app puede traer el estado desde esos formatos. [Observación del código] Está en el código, no lo encontré desarrollado en la documentación pública — trátalo como capacidad presente, a comprobar en la release que instales. Conecta con la historia de la banda: hoy ese puente existe, pero la regla de oro no cambia — respaldo aparte y probado antes de saltar de versión.

**Puente de plugins LNReader.** En el árbol del repo existe `core/lnreader/LNReaderPluginBridge.kt`: un puente hacia plugins de LNReader que no aparece en la documentación pública. [Observación del código] Como todo lo que solo está en código sin docs: señal de dirección, no función garantizada en la build vigente.

---

## 🪪 Entity Organize: identidad entre fuentes

Entity Organize sirve para problemas de identidad:

```
- la misma obra aparece duplicada en favoritos
- una favorita abre una fuente mala o antigua
- tracking mal enlazado
- una obra fue fusionada por error
- importaste o restauraste una biblioteca grande
```

La documentación recalca que Entity Organize no es tarea diaria: es herramienta de mantenimiento y revisión. [Fuente]

```
Merge
-> confirma que varias proyecciones son la misma obra
-> no debe basarse solo en título parecido

Split
-> separa una proyección mal unida
-> no borra favorito, historial ni entrada fuente

Default source
-> cambia la fuente preferida para leer/reproducir
-> no cambia la identidad de la obra
```

Fusión: Find merge candidates → revisa grupos estrictos → selecciona solo lo claro → Merge selected; en modo manual, dos obras del mismo tipo. Los datos remotos se mapean a obras locales, nunca se copian IDs. [Fuente]

Regla práctica: si no puedes explicar por qué dos entradas son la misma obra, no las fusiones.

---

## 🛠️ Solución de problemas

**Fuentes que no aparecen.**

```
Comprobar:
- ¿APK de extensión instalado?
- ¿repositorio agregado y sincronizado?
- ¿pestaña correcta: Manga / Vídeo / Novelas?
- ¿se refrescó la pantalla de extensiones?

Solución:
- reinstala extensión
- refresca pantalla de extensiones
- prueba con una sola fuente antes de cargar muchas
```

**JSON no importa.**

```
Comprobar:
- ¿es Legado o TVBox?
- ¿el JSON es válido?
- ¿la URL responde?
- ¿se importó desde el menú correcto?

Solución:
- reimporta con el tipo correcto
- prueba archivo local primero
- revisa JSON Sources Directory
```

**TVBox importa pero no carga.**

```
Primero:
- medios directos
- playlists
- CMS simple

Luego:
- type 4 JS
- type 3 JAR
- Guard-native / JNI
```

No todo fallo de TVBox es igual. Un JSON puede importar bien y aun así fallar por dependencias JS, JAR, nativas o cambios del proveedor. [Inferencia]

**Traducción no arranca.**

```
Comprobar:
- modo Local o API only
- idioma origen y destino
- OCR Basic o Advanced
- modelos descargados
- endpoint / clave / modelo si usas API
```

La documentación indica que Local no es un fallback automático hacia API; API only requiere configuración previa. [Fuente]

**WebDAV muestra datos distintos.**

```
1. Elige el dispositivo con la biblioteca más actual
2. Haz backup manual ahí
3. Restaura desde ese backup en el dispositivo rezagado
4. Verifica favoritos, historial y progreso
5. No dejes dispositivos meses sin sincronizar
```

**DLNA y vídeo.**

```
- misma red para emisor y receptor
- DLNA/UPnP real, no solo multicast
- espera SSDP; en redes públicas puede estar bloqueado
- sin subtítulos: comprueba si la fuente los trae
- Anime4K se nota en 480p/720p; en alta resolución el cambio es sutil
```

**Nota honesta.** Las webs cambian, las versiones difieren y que algo funcione en la app compañera no garantiza idéntico comportamiento aquí. [Fuente]

---


## ⚖️ Comparativas con criterio declarado

Criterio: utilidad + actividad + confianza, corte 2026-09-13. Ninguna opción es mejor para todo el mundo.

```
Necesidad    Kototoro encaja si…          Lector sencillo mejor si…
────────────────────────────────────────────────────────────────────────
Manga local  quieres combinarlo con más   solo abrir archivos y leer
Novelas      quieres biblioteca común     prefieres lector especializado
Vídeo        quieres centralizar          no quieres reproductor integrado
OCR          necesitas reconocimiento     no usas texto reconocido
Sincronía    ya administras WebDAV        prefieres respaldos manuales
Privacidad   puedes revisar conexiones    quieres superficie mínima
Extensiones  aceptas capas externas       quieres una sola fuente controlada
```

> [!INFO] Alternativa directa
> Mejor para: leer manga con extensiones en una app madura.
> Opción: Mihon — [mihonapp/mihon](https://github.com/mihonapp/mihon)
> Límite: no unifica novelas ni vídeo como Kototoro. [Inferencia]

> [!RECOMMENDATION] Elige Kototoro si necesitas unificar manga, novelas, vídeo, tracking, OCR y fuentes en una sola app. Elige un lector más simple si solo quieres leer archivos locales con la menor superficie posible.

---

## 🎚️ Curaduría consciente y arquitectura de filtrado

```
Censura   -> imposición externa que dicta qué pueden consumir otros
Curaduría -> ejercicio soberano para proteger tu tiempo y atención
```

Cada etiqueta bloqueada no es una prohibición universal: es una hora que decides no gastar. Cada etiqueta priorizada es una puerta que abres.

> [!NOTE] Sección con lenguaje neutral para filtrado. Clasificación orientativa 16+. Las listas son reconstrucción normalizada propia de esta guía, no material del proyecto. [Observación]

### Arquitectura en 6 capas

```
Capa  Función              Prioridad  Acción
────────────────────────────────────────────────────────
🟪 0  Espacios             Ámbito     definir entorno (tipo/idioma/fuente)
🟥 1  Bloqueo crítico      Siempre    excluir permanente
🟧 2  Bloqueo temático     Alta       excluir por defecto
🟨 3  Bloqueo contextual   Media      opcional según etiqueta
🟩 4  Inclusión            Alta       priorizar lo que sí quieres
🟦 5  Descubrimiento       Media      búsqueda manual sin filtro auto
```

### Listas normalizadas (base propia, adapta a tu caso)

```
🚫 N1 BLOQUEO DURO — 72 etiquetas
Adulto explícito, abuso, gore extremo, autolesión, suicidio.
Incluye: Hentai, Ecchi, +18, NSFW, Loli, Shota, NTR, Gore y variantes.

⚠️ N2 BLOQUEO TEMÁTICO OPCIONAL — 68 etiquetas
No implica contenido sexual por sí mismo.
Yaoi, Yuri, BL, GL, Harem, Fanservice, Romance, Drama, Shoujo,
Josei, Gender Bender, Coming of age, Love Triangle, etc.

☠️ N3 HORROR — 17 etiquetas
Terror, Horror, Slasher, Body Horror, Jump Scare, Gore, Splatter,
Monster, Creepypasta, Serial Killer, etc.

🧹 N4 RUIDO — 32 etiquetas (metadatos sin valor de filtro)
One Shot, Webcomic, Indefinido, Miscellaneous, Anthology, Unknown,
General, Cartoon, Gaming, etc.
```

```
Priorización — 13 familias (reconstrucción propia de la guía, no del proyecto)

01 Artes marciales / cultivo     Murim, Cultivation, Wuxia, Xianxia
02 Fantasía / aventura           Fantasy, Adventure, Magic, Dungeon
03 Isekai / sistema              Isekai, Reincarnation, System, Leveling
04 Ciencia ficción / futuro      Sci-Fi, Cyberpunk, Mecha, Space
05 Misterio / crimen             Mystery, Thriller, Crime, Detective
06 Guerra / supervivencia        War, Military, Survival, Battle
07 Deportes / e-sports           Sports, Football, E-Sports
08 Comedia / cotidiana           Comedy, Slice of Life, School, Cooking
09 Formato / publicación         Manhwa, Manhua, Webtoon, Full Color
10 Personajes / arquetipos       Overpowered MC, Female Lead, Antihero
11 Mitología / folclore          Mythology, Gods, Demons, Yokai
12 Mar / exploración             Pirates, Sea, Navy
13 Gastronomía / cultura         Food, Cooking, Festival

Los conteos exactos de etiquetas de ediciones anteriores no se recontaron hoy: usa las familias, no el número.
```

### Distinciones críticas para no sobrefiltrar

```
No auto-bloquear: Drama, Romance, Action, Adventure, Fantasy,
Historical, Mystery, Psychological, Slice of Life, Game, VR,
Isekai, Martial Arts, Wuxia, Xianxia, Magic, Dungeon, System,
Player, Leveling, Skill, Evolution

Identidad (representación, no contenido sexual):

LGBT, Gay, Lesbian, Transgender, Non-binary, Queer, Pride
❌ No equivale a contenido sexual
✅ Temática representativa: no la bloquees como medida de seguridad
```

### Procedimiento de filtrado en la app

```
PASO 1 Instalación
- Descarga desde releases oficiales y compara el hash

PASO 2 Asistente inicial
- Completa el wizard: espejos, plugins base y tipos de contenido

PASO 3 Fuentes
- Ajustes -> Content Sources -> Extensions (pestañas Manga / Vídeo)
- JSON Legado/TVBox -> Import JSON Sources -> JSON Sources Directory

PASO 4 Tipos de contenido
- Activa solo lo que vayas a usar: Manga, Novelas, Vídeo

PASO 5 Perfiles sugeridos
- BLOCK-EXPLICIT N1 · BLOCK-EXTREME N1+N3 · BLOCK-TROPES N2
- PRIORITY-FANTASY 02,06,07,10,11 · SCIFI 04,05,08 · ISEKAI 01,03,09

PASO 6 Lista de bloqueo
- Si no hay filtro global efectivo: no instales repos con contenido
  indeseado, usa filtros guardados y limita tipo e idioma

PASO 7 Lista de priorización
- Crea filtros guardados por categoría y actívalos según tu interés

PASO 8 Espacios
- Ajustes -> Spaces: Isekai / Local / Shonen / Anime
```

### Regla de oro

```
FUENTE -> METADATOS -> NORMALIZACIÓN -> ETIQUETAS -> FILTRO -> RESULTADO

Si la fuente no entrega etiquetas, ningún filtro basado solo en
etiquetas puede garantizar la detección.
```

No existe una lista de bloqueo universal perfecta. [Inferencia]

---


## 🔒 Seguridad y cadena de suministro

El proyecto declara que sus desarrolladores no tienen afiliación con los proveedores de contenido ni mantienen o gobiernan repositorios de extensiones: las fuentes las proporciona el usuario. [Fuente]

Un análisis externo de repositorio no encontró política de seguridad ni código de conducta publicados, aunque sí guía de contribución y licencia visibles. [Observación] Esto no implica inseguridad, pero es una señal a vigilar en un proyecto que carga runtimes de terceros. Builds concretas distribuidas en tiendas alternativas pasaron escaneo con ClamAV, APKiD y Quark-Engine sin amenazas detectadas; eso vale para ese APK concreto, no para la cadena completa. [Observación]

> [!WARNING] No confíes en una fuente solo porque aparezca en una lista de internet. Comprueba repositorio, commit, tag y firma antes de instalar nada.

```
Riesgos a tener presentes

- Las extensiones de terceros cambian sin aviso
- Fuentes web se rompen o bloquean acceso
- Cloudflare puede cambiar
- JSON Legado/TVBox depende de calidad externa
- JAR y plugins añaden superficie de ataque
- QUERY_ALL_PACKAGES amplía visibilidad de apps instaladas
- REQUEST_INSTALL_PACKAGES permite instalar APK si el usuario concede permiso
- MANAGE_EXTERNAL_STORAGE amplía acceso a archivos
- La sincronización puede incluir credenciales: verifica servidor y TLS
- OCR/API puede enviar texto fuera del dispositivo si lo configuras así
```

```
Capas separadas

App          -> Kototoro
Parser       -> código que entiende una fuente
Extensión    -> APK/JAR/JSON externo
Proveedor    -> sitio o servicio consultado
Obra         -> contenido final
Usuario      -> quien decide qué instalar y configurar
```

Descarga/conversión: solo obras propias, dominio público, licencias que permitan copia, respaldos legítimos o permisos explícitos. Privilegios elevados: solo con razón proporcional, respaldo y vuelta.

---


## 🗺️ Directorio del ecosistema

Directorio informativo, no recomendación. Fechas de auditoría entre 2026-09-08 y 2026-09-10 (HTTP 200 = responde, no seguro ni vigente); el núcleo Kototoro y TODOS los repos de extensiones/parsers fueron revalidados el 2026-09-13 vía API de GitHub (archivado/activo, estrellas y última actividad). Los repos señalados con ◆ aparecen en listados de terceros como configuraciones habituales, no como aval del proyecto.

> [!WARNING] **Sobre los repositorios de extensiones (◆).** Apuntan a fuentes no oficiales de manga y anime. El proyecto Kototoro no los recomienda ni los respalda; están aquí como mapa de lo que la comunidad usa, para que verifiques cada uno antes de tocarlo. La regla de la banda: úsalos solo con contenido legítimo o de dominio público, y revisa repositorio, commit y licencia de cada extensión antes de instalarla. No descargues de espejos que imiten estos nombres.

**📖 Lectores y bibliotecas**

Mihon — Apache-2.0 — [mihonapp/mihon](https://github.com/mihonapp/mihon)
Yokai — Apache-2.0 — [null2264/yokai](https://github.com/null2264/yokai)
Aniyomi — Apache-2.0 — [aniyomiorg/aniyomi](https://github.com/aniyomiorg/aniyomi)
Komikku — Apache-2.0 — [komikku-app/komikku](https://github.com/komikku-app/komikku)
KOReader — AGPL-3.0 — [koreader/koreader](https://github.com/koreader/koreader)
Librera — [foobnix/LibreraReader](https://github.com/foobnix/LibreraReader)
Book's Story — GPL-3.0 — [Acclorite/book-story](https://github.com/Acclorite/book-story)
Koodo Reader — AGPL-3.0 — [koodo-reader/koodo-reader](https://github.com/koodo-reader/koodo-reader)
Anx Reader — MIT — [Anxcye/anx-reader](https://github.com/Anxcye/anx-reader)
Tadami — andarcanum/Tadami-Aniyomi-fork v0.62 — [andarcanum/Tadami-Aniyomi-fork](https://github.com/andarcanum/Tadami-Aniyomi-fork)

**🔌 Extensiones y repositorios** (◆ = habitual en listados de terceros; ver advertencia arriba). Estados verificados el 2026-09-13 vía API de GitHub (★ y última actividad).

CANÓNICO — Keiyoushi
Keiyoushi extensions ◆ — 14.962★ — [keiyoushi/extensions](https://github.com/keiyoushi/extensions)
Keiyoushi extensions-source ◆ — 4.667★ — [keiyoushi/extensions-source](https://github.com/keiyoushi/extensions-source)

Yuzono — espejo de Keiyoushi para manga (anime aparte)
Yuzono tachiyomi-extensions ◆ — 887★ (API hoy) — [yuzono/tachiyomi-extensions](https://github.com/yuzono/tachiyomi-extensions)
  -> fuente; hace cherry-pick automático de Keiyoushi: trátalo como espejo
Yuzono manga-repo — 4★ — [yuzono/manga-repo](https://github.com/yuzono/manga-repo)
  -> repo compilado; fork de keiyoushi/extensions
Yuzono anime-extensions ◆ — 426★ — [yuzono/anime-extensions](https://github.com/yuzono/anime-extensions)

Project Nox — antes Awerkori (pt-BR); misma cuenta, marca nueva
Awerkori extensoes (compilado) — [Awerkori/extensoes](https://github.com/Awerkori/extensoes)
Awerkori fonte-extensoes (Project Nox, fuente) — [Awerkori/fonte-extensoes](https://github.com/Awerkori/fonte-extensoes)
Awerkori anime-extensoes (Project Nox Anime) — [Awerkori/anime-extensoes](https://github.com/Awerkori/anime-extensoes)
Awerkori project-nox-manga (plataforma) — [Awerkori/project-nox-manga](https://github.com/Awerkori/project-nox-manga)

Komikku — cambió de URL
cuong-tran manga-repo (antes komikku-app/extensions) — 445★ — [cuong-tran/manga-repo](https://github.com/cuong-tran/manga-repo)

Otros — activos al corte
LittleSurvival copymanga-copy20 ◆ (= TheNano) — 2.742★ — [LittleSurvival/copymanga-copy20](https://github.com/LittleSurvival/copymanga-copy20)
Mangayomi extensions — 101★ — [m2k3a/mangayomi-extensions](https://github.com/m2k3a/mangayomi-extensions)
Mangayomi anime-extensions — 17★ — [Mallyd11/mangayomi-anime-extensions](https://github.com/Mallyd11/mangayomi-anime-extensions)
IReader-extensions — MPL-2.0 — 32★ — [IReaderorg/IReader-extensions](https://github.com/IReaderorg/IReader-extensions)
NovelSourcery extensions-source — 13★ — [NovelSourcery/extensions-source](https://github.com/NovelSourcery/extensions-source)
XIU2 Yuedu — GPL-3.0 — 12.255★ — [XIU2/Yuedu](https://github.com/XIU2/Yuedu)
Legado (app origen del ecosistema Legado) — 47.070★ — [gedoor/legado](https://github.com/gedoor/legado)
Tadami extensions (Freitez93) — 0★ — [Freitez93/Tadami-Extensions](https://github.com/Freitez93/Tadami-Extensions)  (madurez baja; no sustituye el mapa Miyomi)
Kototoro parsers — GPL-3.0 — 14★ — [skepsun/kototoro-parsers](https://github.com/skepsun/kototoro-parsers)

ELIMINADO de esta edición:
Kohi-den extensions-source ◆ — ARCHIVADO (~2026-05); ya no sirve.

**☁️ Servidores y autoalojamiento**

Suwayomi-Server — MPL-2.0 — [Suwayomi/Suwayomi-Server](https://github.com/Suwayomi/Suwayomi-Server)
Komga — MIT — [gotson/komga](https://github.com/gotson/komga)
Kavita — GPL-3.0 — [Kareadita/Kavita](https://github.com/Kareadita/Kavita)
Calibre-Web — GPL-3.0 — [janeczku/calibre-web](https://github.com/janeczku/calibre-web)
Stump — MIT — [stumpapp/stump](https://github.com/stumpapp/stump)
Jellyfin — GPL-2.0 — [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)
Navidrome — GPL-3.0 — [navidrome/navidrome](https://github.com/navidrome/navidrome)
Nextcloud — AGPL-3.0 — [nextcloud/server](https://github.com/nextcloud/server)

**🛠️ Sistema y privilegios** (solo con razón proporcional, respaldo probado y camino de vuelta)

Shizuku — [RikkaApps/Shizuku](https://github.com/RikkaApps/Shizuku)
Magisk — [topjohnwu/Magisk](https://github.com/topjohnwu/Magisk)
KernelSU — [tiann/KernelSU](https://github.com/tiann/KernelSU)
LSPosed — [LSPosed/LSPosed](https://github.com/LSPosed/LSPosed)
Vector — [JingMatrix/Vector](https://github.com/JingMatrix/Vector)
Dhizuku — [iamr0s/Dhizuku](https://github.com/iamr0s/Dhizuku)
APatch — [bmax121/APatch](https://github.com/bmax121/APatch)
aShellYou — [DP-Hridayan/aShellYou](https://github.com/DP-Hridayan/aShellYou)
Shevery — [HmnDev-Tech/shevery](https://github.com/HmnDev-Tech/shevery)

**⬇️ Descarga y conversión** (solo obras propias, dominio público o copia permitida)

yt-dlp — [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
Seal — [JunkFood02/Seal](https://github.com/JunkFood02/Seal)
YTDLnis — [deniscerri/ytdlnis](https://github.com/deniscerri/ytdlnis)
NewPipe — [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe)
LibreTube — [libre-tube/LibreTube](https://github.com/libre-tube/LibreTube)
PipePipe — [InfinityLoop1308/PipePipe](https://github.com/InfinityLoop1308/PipePipe)
SkyTube — [SkyTubeTeam/SkyTube](https://github.com/SkyTubeTeam/SkyTube)

**🎥 Streaming y multimedia**

Cloudstream — [recloudstream/cloudstream](https://github.com/recloudstream/cloudstream)
Miru — [miru-project/miru-app](https://github.com/miru-project/miru-app)
Dantotsu — [itsmechinmoy/Dantotsu](https://github.com/itsmechinmoy/Dantotsu)
AniHyou — [axiel7/AniHyou-android](https://github.com/axiel7/AniHyou-android)
Kitsu-X — [richtunic/Kitsu-X](https://github.com/richtunic/Kitsu-X)
mpvRx — [Riteshp2001/mpvRx](https://github.com/Riteshp2001/mpvRx)

**🏪 Tiendas y catálogos FOSS**

F-Droid — [f-droid.org](https://f-droid.org)
IzzyOnDroid — [apt.izzysoft.de/fdroid/repo](https://apt.izzysoft.de/fdroid/repo)
Obtainium — [ImranR98/Obtainium](https://github.com/ImranR98/Obtainium)
ObtainX — [bikram-agarwal/ObtainX](https://github.com/bikram-agarwal/ObtainX)
Neo Store — [NeoApplications/Neo-Store](https://github.com/NeoApplications/Neo-Store)
Aurora Store — [AuroraOSS/AuroraStore](https://gitlab.com/AuroraOSS/AuroraStore)
Droid-ify — [Droid-ify/client](https://github.com/Droid-ify/client)
Accrescent — [accrescent.app](https://accrescent.app)
Appteka — [solkin/appteka-android](https://github.com/solkin/appteka-android)

**📚 Wikis y directorios** (para encontrar candidatos, no como prueba)

FMHY — [fmhy.net](https://fmhy.net)
Wotaku Wiki — [wotaku.wiki](https://wotaku.wiki)
EverythingMoe — [everythingmoe.com](https://everythingmoe.com)
Miyomi — [miyomi.app/software/kototoro](https://miyomi.app/software/kototoro)
The Index — [theindex.moe](https://theindex.moe)

**📄 Documentación oficial de Kototoro**

Páginas leídas al corte: inicio, getting-started, source-integrations, webdav-sync, automatic-translation, entity-system, local-import, reference/tvbox-runtime, architecture/dynamic_plugin_system, architecture/incremental-updates, faq, troubleshooting, reader-features, reference/mihon-integration. Nuevas desde la edición anterior: architecture/architecture-review, architecture/architecture-roadmap, architecture/external-extension-integration-guide, plugin_development_guide y un plan de UI para TV.

---


## ❓ Preguntas frecuentes

**¿Cuál es la última versión?** v2.1.1, publicada el 2026-09-13 a las 07:36 UTC (vista en la página de releases ese día). El ritmo sigue siendo casi diario. Cualquier cifra citada caduca en horas. [Observación]

**¿Es seguro?** El código es abierto y auditable, y la app no trae contenido: la seguridad depende de las extensiones y fuentes que configures. Esta guía no auditó binarios en ejecución. Builds concretas en tiendas alternativas pasaron escaneo antimalware sin amenazas detectadas, lo cual es señal, no garantía. [Observación]

**¿Trae contenido?** No. El proyecto declara que la app no aloja ni empaqueta contenido, y que las fuentes dependen de extensiones o endpoints configurados por el usuario. [Fuente]

**¿Qué extensiones acepta?** Mihon, Aniyomi, IReader, Legado, TVBox y CloudStream3 (este último en el README, no en la portada de la docs), más los parsers nativos y la biblioteca Kotatsu-Redo integrada. [Fuente / Observación]

**¿Recomienda el proyecto algún repositorio?** No: la app no distribuye ni recomienda ningún repositorio de terceros concreto. Los nombres que circulan vienen de listados comunitarios. [Fuente]

**¿El OCR funciona sin internet?** El OCR + traducción automática local funciona dentro del lector; el modo API es aparte y requiere servicio y clave. [Fuente]

**¿Cómo se configura WebDAV?** Ajustes → Backup & Restore → endpoint, usuario y contraseña → prueba en un teléfono primero → reutiliza el destino. [Fuente]

**¿WebDAV sincroniza credenciales?** La documentación dice que puede sincronizar credenciales y estado de fuentes donde aplique. Revisa servidor, TLS y carpeta dedicada antes de usarlo. [Fuente]

**¿Es un fork de Kotatsu?** El README actual (2026-09-13) dice que deriva de Kotatsu pero que ya es desarrollo independiente, no un fork. Kotatsu está descontinuado; de su familia quedan forks como Usagi, Futon y Kotatsu-Redo. La lectura «fork de Kotatsu/Usagi» que circula en la banda es memoria del usuario: [Declaración], pendiente de cotejo contra la historia del repo. [Fuente / Declaración]

**¿Por qué un directorio muestra otra versión?** Porque el proyecto publica con frecuencia y los directorios van detrás. La referencia es la página de releases. [Inferencia]

**¿Bloqueo las etiquetas de identidad por seguridad?** No: son representación, no contenido sexual. Bloquearlas no te protege de nada.

---

## 📖 Glosario

```
Entity System   identidad estable de una obra entre fuentes
Projection      entrada concreta desde una fuente, extensión o archivo
Default         fuente preferida para abrir una obra
Tracking binding vínculo con MAL, AniList, Kitsu, Bangumi, Shikimori o MangaUpdates
ML Kit          kit de ML en el teléfono (OCR y traducción base)
ONNX            formato de modelos para inferencia local
TVBox           ecosistema de fuentes de vídeo basadas en JSON
Legado          ecosistema de fuentes de lectura basadas en reglas/JSON
CloudStream3    ecosistema de extensiones de streaming
WebDAV          protocolo para sincronizar vía HTTP en tu servidor
DLNA / SSDP     descubrimiento y envío multimedia en red local
JAR / Dex       archivo de código cargable; en Android adaptado a bytecode compatible
ABI             contrato binario entre app anfitriona y plugin
index.json      metadatos editables de tu contenido local
```

---

## 👤 Configuraciones recomendadas por perfil

```
📚 Acción y fantasía
Núcleo -> priorización 01, 02, 03, 06, 07 · Bloqueo -> N1 + N3 + N4
Espacios -> Shonen solo manga, fuentes habituales de listados

🎌 Novelas ligeras isekai / sistema
Núcleo -> priorización 03, 04, 05, 08 · Bloqueo -> N1 + N4
Espacios -> Novelas con IReader o JSON, OCR opcional

🗂️ Coleccionista organizador
Núcleo -> priorización amplia, N2 según gusto · Bloqueo -> N1 + N3 + N4
Espacios -> por idioma; sincronía contra nube propia

🔍 Local primero, privacidad
Núcleo -> solo CBZ / EPUB locales · Bloqueo -> ninguno
Espacios -> Local sin internet, OCR desactivado

🎥 Anime y vídeo
Núcleo -> priorización 04, 05, 08, 11 · Bloqueo -> N1 + N3
Espacios -> Anime solo vídeo, super-resolución opcional
```

---


## 📓 Historia de uso — contada por un miembro de la banda

Esta parte no es la ficha del proyecto: es la memoria de uso de Alexis, que la usa desde antes de la 0.80. [Declaración] En el método de la banda eso vale mucho: es el «uso real acreditado por un humano», la puerta que un asistente no puede cruzar solo. Vale como experiencia, no como verificación técnica: cada dato de abajo es su recuerdo, y va marcado como tal.

- **Antes de la 0.80** ya la usaba; la dejó un tiempo. [Declaración]
- **Volvió en la 1.40.0.** De ahí en adelante, la evolución fue enorme. [Declaración]
- **El golpe de los respaldos (1.4.0–1.7.0).** Según su recuerdo, cuando abrió el issue de reporte de errores, el administrador explicó que la biblioteca se perdió por cambios en el motor y el formato de la app, y que entre la 1.4.0 y la 1.7.0 las copias de seguridad se volvieron incompatibles. [Declaración]
  - **Lo que sí comprobé** en los issues públicos del repo (vistos 2026-09-11, no reabiertos hoy): hubo problemas reales de respaldo en ese rango — «Can't create or restore backup in latest version 1.4.6» (#357, cerrado completado), «Backup from 1.3.13 to 1.5.6 issue» (#380, cerrado "not planned"), «problem with restoring from local backup and WEBDAV backup» (#245, cerrado completado) y «上传备份的问题» (#489, abierto). [Observación]
  - **Lo que NO encontré:** un issue que diga textualmente «cambios en el motor/formato» como causa, ni uno titulado «library lost». La explicación exacta del admin queda como [Declaración] de Alexis, no como cita verificada. [No encontrado]
  - La lección, sea cual sea la causa exacta: el respaldo se guarda APARTE y se prueba antes de cada salto. Nadie pierde por respaldar; se pierde por confiar en que el respaldo de la app basta.
- **La recuperación.** Al final usó AniZen para recuperar la biblioteca, esperó a que ambas apps actualizaran para ser compatibles, y volvió a restaurar en Kototoro. [Declaración — nombre tal como lo dijo Alexis. El repo salmanbappi/AniZen existe (verificado 2026-09-10); no se comprobó que esa sea la app del episodio de recuperación]
- **Desde la 1.9.0** mejoró el diseño: el color y una interfaz moderna. [Declaración] Coincide con lo que el propio README declara hoy — paleta dinámica y animaciones Hero ajustables desde Apariencia. [Fuente]
- **La versión de hoy.** En la página de releases consultada el 2026-09-13, la última es **v2.1.1** (13-sep 07:36 UTC) y la anterior **v2.1.0** (11-sep); el ritmo es casi diario. [Observación]

---

## 🕰️ Evolución reciente

Ritmo de releases alto: casi una por día. Cualquier versión puede quedar desactualizada en horas.

```
v2.1.1   2026-09-13   (latest; vista en releases ese día) [Observación]
v2.1.0   2026-09-11   (vista en releases) [Observación]
v2.0.10  2026-09-10   (vista en releases) [Observación]
v2.0.9   2026-09-09   (vista en releases) [Observación]
v2.0.8   2026-09-08   (vista en releases) [Observación]
v2.0.3   2026-09-03   (ficha Appteka, edición anterior)
v2.0.0   2026-08-22   (directorio de análisis, no revalidado hoy)
v1.9.1   2026-08-05   (ficha Appteka, no revalidada hoy)
```

Novedades de v2.1.1 (notas de la release, 2026-09-13): primera UI para TV; fix de crash en chips de filtro de fuentes unificadas; chips de título del lector; «fix(backup): review and discard orphaned work state»; docs del plan de TV UI. [Fuente] Eso no prueba que el episodio de respaldos 1.4–1.7 esté cerrado: es un arreglo de estado huérfano en la serie 2.x, no una auditoría del formato viejo. [Inferencia]

Novedades de v2.1.0 (edición anterior): notas con anotaciones multimedia, filtrado space/NSFW, JPEG XL, Spaces personalizados. [Observación 2026-09-11]

---

## 🏁 Conclusión, límites y no-asunciones

Kototoro unifica manga, novelas y vídeo (all-Compose, parsers integrados + ecosistemas externos incluido CloudStream3 declarado en README, OCR/traducción local, WebDAV). Reduce saltos entre apps, pero aumenta la superficie a revisar. [Inferencia]

**Límites de esta edición.**

```
⚠️ No se instaló ni se probó la app en ningún teléfono.
⚠️ No se auditó la seguridad de binarios ni se verificaron hashes.
⚠️ No se probó OCR, traducción ni WebDAV con muestras reales.
⚠️ La versión v2.1.1 se confirmó en vivo el 2026-09-13, pero caduca en horas.
⚠️ Las listas de filtrado son reconstrucción normalizada, no auditoría.
⚠️ Detalles finos (permisos exactos, minSdk, rangos LIB Mihon) requieren
   lectura del manifiesto y docs de la release vigente.
⚠️ El cambio GPL-3.0 → Apache-2.0 está declarado (LICENSE leído hoy),
   no auditado archivo por archivo.
⚠️ La «independencia de Kotatsu» es declaración del README; el linaje
   histórico completo no se auditó commit a commit.
```

**Lo que no debes asumir de esta guía.**

```
- Que los enlaces sigan activos o seguros sin volver a comprobarlos.
- Que el OCR o la traducción estén auditados por terceros.
- Que las listas de filtrado sean exhaustivas o sirvan sin adaptar.
- Que los privilegios elevados estén recomendados por defecto.
- Que la versión citada siga siendo la última: el ritmo es alto.
- Que los repositorios listados en el directorio estén respaldados por
  el proyecto: declara explícitamente que no recomienda ninguno.
- Que esta publicación sea una recomendación universal: es un mapa
  con criterio declarado y fecha de corte.
```

**Pendientes para una auditoría completa.**

```
1. Instalar la release vigente y verificar su hash publicado.
2. Confirmar número de versión exacto y changelog en la página de releases.
3. Leer manifiesto de la build instalada (permisos reales fusionados).
4. Probar 5-15 títulos mixtos, locales y remotos.
5. Probar el ecosistema CloudStream3 (declarado en README, sin cobertura extensa).
6. Probar respaldo y restauración en dos teléfonos.
7. Probar lectura con lector de pantalla.
8. Revalidar los enlaces del directorio antes de republicar.
9. Cerrar la verificación del episodio 1.4.0–1.7.0: localizar el issue
   exacto donde el admin explicó el cambio de motor/formato. Parcialmente
   verificado hoy (issues #357, #380, #245, #489); la explicación textual
   sigue como [Declaración] de Alexis.
10. Confirmar el nombre exacto de la app usada para recuperar la biblioteca
    («AniZen» tal como lo dijo Alexis; verificar si es AniZen, Aniyomi u otra).
```

> La Bandita informa a partir de fuentes fechadas. Comprueba permisos, licencia, procedencia y compatibilidad antes de usarlo.

**Fuentes de esta edición:** repo oficial (API + README raw devel + releases/latest, 2026-09-13), documentación oficial ([kototoro-app.github.io](https://kototoro-app.github.io), abierta 2026-09-13), LICENSE SPDX por API, repos de extensiones por API el mismo día. Fichas de Miyomi/Appteka y el resto del directorio de lectores/servidores: auditoría 2026-09-08 a 2026-09-11, no reabiertos uno a uno hoy. Revalidar antes de republicar.

**Imagen (opcional).** Una pieza: avisos vs estantería Manga/Novela/Vídeo. A ojo. Sin ella también se publica.

#Android #FOSS #OpenSource #Kototoro #Manga #Manhwa #NovelaLigera #Anime #Isekai #Wuxia #Xianxia #WebDAV #OCR #GuíaMasiva #Septiembre2026 #v211

---
MENSAJE FIJADO (WhatsApp, si el chat lo permite) — no hace falta si el mapa de arriba basta.

Kototoro — Guía de La Bandita
Fecha: 2026-09-13
Versión de esta publicación: BORRADOR 2026-09-13 (corte vivo, tarde)
App citada al corte: Kototoro v2.1.1

Índice (el mismo icono abre cada bloque del post)

ℹ️ Qué es Kototoro
🧭 Estado al corte
🏗️ Arquitectura
⚙️ Características
🔌 Extensiones y fuentes
🎯 Para quién
♿ Accesibilidad
🧪 Antes de instalar
💾 Instalación
🧩 Compatibilidad
🔄 Migración
🪪 Entity Organize
🛠️ Problemas
⚖️ Comparativas
🎚️ Filtrado
🔒 Seguridad
🗺️ Directorio
❓ FAQ
📖 Glosario
👤 Perfiles
📓 Historia de uso
🕰️ Evolución
🏁 Cierre