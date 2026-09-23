# Publicación — Kototoro (La Bandita) · 2026-09-13
> BORRADOR · Facebook / La Bandita · no Discord. Perfil FACEBOOK (Manual 5.2).
> Límite observado ~40k incluso con Meta Premium. POST: copia desde KOTOTORO hasta hashtags.
> Lista completa (directorio, fichas largas) = mensaje de WhatsApp.
> COMENTARIO FIJADO: bloque del final. No publicar sin firma humana.

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
Índice corto: primer comentario (fijado). Lista completa: WhatsApp.

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

Repositorio:   [https://github.com/Kototoro-app/Kototoro](https://github.com/Kototoro-app/Kototoro)
Rama:          devel (confirmada) · 8 ramas · 196 tags · 6.950 commits
Métricas:      569 estrellas · 46 forks · 57 issues abiertos (GitHub API, 2026-09-13) [Observación]
Versión:       v2.1.1 (latest, publicada 2026-09-13 07:36 UTC) — ritmo casi diario:
               COMPRUEBA LA RELEASE VIGENTE en GitHub Releases
Licencia:      Apache-2.0 (LICENSE leído el 2026-09-11; SPDX reconfirmado por API el 2026-09-13) [Observación]
Documentación: [https://kototoro-app.github.io/Kototoro/](https://kototoro-app.github.io/Kototoro/) (viva)
               (histórica: skepsun.github.io/Kototoro) [Observación]
Releases:      [https://github.com/Kototoro-app/Kototoro/releases](https://github.com/Kototoro-app/Kototoro/releases)
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

**Nightly — corrección respecto al 2026-09-11.** Entonces era stub. Hoy [https://github.com/Kototoro-app/Kototoro-Nightly](https://github.com/Kototoro-app/Kototoro-Nightly) está vivo (8★, 1 fork, no archivado). Última vista: nightly-20260913 (13-sep 16:57 UTC, prerelease). La lista carga al menos desde nightly-20260909. Cada una, 5 APKs (arm64 / armeabi-v7a / universal / x86 / x86_64), nombres Kototoro-NYYYYMMDD-…. /releases/latest sigue 404 porque todas son prerelease. [Observación] Sirve para probar devel, no para biblioteca diaria. Estable = releases del repo principal.

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

(Detalle = WhatsApp.)

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

(Detalle = WhatsApp.)

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

(Detalle = WhatsApp.)

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

(Detalle = WhatsApp.)

---

## 💾 Instalación y primera prueba sin arriesgar tu biblioteca

```
1. Respalda tu lector actual y guárdalo aparte
2. Descarga solo de [https://github.com/Kototoro-app/Kototoro/releases](https://github.com/Kototoro-app/Kototoro/releases)
   y compara hash
3. Instala tu arquitectura; revisa permisos; completa el wizard
4. Configura idioma y espacios, OCR desactivado al inicio
5. Prueba 5 títulos (2 locales, 2 integrados, 1 externo)
6. Si va bien, 10-15 antes de migrar más
7. Conserva tu app anterior hasta confirmar el regreso
```

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

(Detalle = WhatsApp.)

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

(Detalle = WhatsApp.)

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

(Detalle = WhatsApp.)

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

(Detalle = WhatsApp.)

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
> [!INFO] Alternativa directa
> Mejor para: leer manga con extensiones en una app madura.
> Opción: Mihon — [https://github.com/mihonapp/mihon](https://github.com/mihonapp/mihon)
> Límite: no unifica novelas ni vídeo como Kototoro. [Inferencia]

> [!RECOMMENDATION] Elige Kototoro si necesitas unificar manga, novelas, vídeo, tracking, OCR y fuentes en una sola app. Elige un lector más simple si solo quieres leer archivos locales con la menor superficie posible.

---

## 🎚️ Curaduría consciente y arquitectura de filtrado

Censura = imposición externa. Curaduría = tú eliges qué no gastar. Listas = reconstrucción propia de la guía, no del proyecto. 16+ orientativo. [Observación]

Capa 0  Espacios (tipo / idioma / fuente)
Capa 1  Bloqueo crítico (siempre)
Capa 2  Bloqueo temático (por defecto)
Capa 3  Bloqueo contextual (opcional)
Capa 4  Inclusión (lo que sí quieres)
Capa 5  Descubrimiento (búsqueda sin auto-filtro)
```

N1 duro: adulto explícito, abuso, gore extremo, autolesión. N2 temático opcional (no es sexo por sí). Identidad (LGBT y similares) no se bloquea como si fuera contenido sexual. Listas de etiquetas completas = WhatsApp.

Regla: el respaldo se guarda aparte y se prueba antes de cada salto.

---

## 🔒 Seguridad y cadena de suministro

El proyecto declara que sus desarrolladores no tienen afiliación con los proveedores de contenido ni mantienen o gobiernan repositorios de extensiones: las fuentes las proporciona el usuario. [Fuente]

Un análisis externo de repositorio no encontró política de seguridad ni código de conducta publicados, aunque sí guía de contribución y licencia visibles. [Observación] Esto no implica inseguridad, pero es una señal a vigilar en un proyecto que carga runtimes de terceros. Builds concretas distribuidas en tiendas alternativas pasaron escaneo con ClamAV, APKiD y Quark-Engine sin amenazas detectadas; eso vale para ese APK concreto, no para la cadena completa. [Observación]

> [!WARNING] No confíes en una fuente solo porque aparezca en una lista de internet. Comprueba repositorio, commit, tag y firma antes de instalar nada.

```
Riesgos a tener presentes

(Detalle = WhatsApp.)

---

## 🗺️ Directorio del ecosistema

Informativo, no recomendación. Núcleo y extensiones revalidados por API el 2026-09-13. **Lista completa (lectores, servidores, parsers, wikis) = mensaje de WhatsApp.**

◆ = sale en listados de terceros. Kototoro no los avala. Kohi-den: archivado, no usar.

Mihon v0.20.4 — 23.555★ — [https://github.com/mihonapp/mihon](https://github.com/mihonapp/mihon)
Aniyomi — 7.678★ — [https://github.com/aniyomiorg/aniyomi](https://github.com/aniyomiorg/aniyomi)
Komikku v1.14.1 — 4.711★ — [https://github.com/komikku-app/komikku](https://github.com/komikku-app/komikku)
Keiyoushi extensions ◆ — 14.962★ — [https://github.com/keiyoushi/extensions](https://github.com/keiyoushi/extensions)
Keiyoushi extensions-source ◆ — 4.667★ — [https://github.com/keiyoushi/extensions-source](https://github.com/keiyoushi/extensions-source)
Yuzono tachiyomi-extensions ◆ — 887★ (espejo de Keiyoushi) — [https://github.com/yuzono/tachiyomi-extensions](https://github.com/yuzono/tachiyomi-extensions)
Yuzono anime-extensions ◆ — 426★ — [https://github.com/yuzono/anime-extensions](https://github.com/yuzono/anime-extensions)
cuong-tran manga-repo — 445★ — [https://github.com/cuong-tran/manga-repo](https://github.com/cuong-tran/manga-repo)
LittleSurvival copymanga-copy20 ◆ (= TheNano) — 2.742★ — [https://github.com/LittleSurvival/copymanga-copy20](https://github.com/LittleSurvival/copymanga-copy20)
Tadami v0.62 — [https://github.com/andarcanum/Tadami-Aniyomi-fork](https://github.com/andarcanum/Tadami-Aniyomi-fork)
XIU2 Yuedu — 12.255★ — [https://github.com/XIU2/Yuedu](https://github.com/XIU2/Yuedu)
Legado — 47.070★ — [https://github.com/gedoor/legado](https://github.com/gedoor/legado)
kototoro-parsers — 14★ · GPL-3.0 — [https://github.com/skepsun/kototoro-parsers](https://github.com/skepsun/kototoro-parsers)

Docs: [https://kototoro-app.github.io/Kototoro/](https://kototoro-app.github.io/Kototoro/) — portada 5 ecosistemas (sin CloudStream); README nombra seis.

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

(Detalle = WhatsApp.)

---

## 📖 Glosario
## 👤 Configuraciones recomendadas por perfil

Completos en el mensaje de WhatsApp (parser, entity, proyección, espacio, nightly, firmas).

---

## 📓 Historia de uso — contada por un miembro de la banda

Esta parte no es la ficha del proyecto: es la memoria de uso de Alexis, que la usa desde antes de la 0.80. [Declaración] En el método de la banda eso vale mucho: es el «uso real acreditado por un humano», la puerta que un asistente no puede cruzar solo. Vale como experiencia, no como verificación técnica: cada dato de abajo es su recuerdo, y va marcado como tal.

- **Antes de la 0.80** ya la usaba; la dejó un tiempo. [Declaración]
- **Volvió en la 1.40.0.** De ahí en adelante, la evolución fue enorme. [Declaración]
- **El golpe de los respaldos (1.4.0–1.7.0).** Según su recuerdo, cuando abrió el issue de reporte de errores, el administrador explicó que la biblioteca se perdió por cambios en el motor y el formato de la app, y que entre la 1.4.0 y la 1.7.0 las copias de seguridad se volvieron incompatibles. [Declaración]
  - **Lo que sí comprobé** en los issues públicos del repo (vistos 2026-09-11, no reabiertos hoy): hubo problemas reales de respaldo en ese rango — «Can't create or restore backup in latest version 1.4.6» (#357, cerrado completado), «Backup from 1.3.13 to 1.5.6 issue» (#380, cerrado "not planned"), «problem with restoring from local backup and WEBDAV backup» (#245, cerrado completado) y «上传备份的问题» (#489, abierto). [Observación]

(El relato completo, con el episodio de respaldos, está en WhatsApp.) [Declaración]

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

Kototoro es un lector/reproductor Compose-first, Apache-2.0, vivo (v2.1.1 hoy). Útil si quieres manga+novela+vídeo en una biblioteca y aceptas extensiones de terceros. No es un «todo gratis». Nightly no es canal diario. [Inferencia]

Límites: ningún APK se ejecutó; docs vs README (5 vs 6 ecosistemas); AniZen del relato es [Declaración] (repo salmanbappi/AniZen visto 2026-09-10, no reabierto hoy); backup 1.4–1.7 no se da por cerrado.

No asumas que los enlaces siguen, ni que «recomendable» es universal, ni que Nightly sustituye a v2.1.1.

Lista completa, directorio y relato de uso = WhatsApp.

---

**Fuentes (2026-09-13):** GitHub API + README devel + releases/latest + docs hub + Nightly lista. Extensiones por API. Revalidar el día del post.

> La Bandita informa a partir de fuentes fechadas. Comprueba permisos, licencia y procedencia.

#Android #FOSS #OpenSource #Kototoro #Manga #Manhwa #NovelaLigera #Anime #Isekai #Wuxia #Xianxia #WebDAV #OCR #GuíaMasiva #Septiembre2026 #v211

---
COMENTARIO FIJADO — no forma parte del post. Primer comentario, fijar.

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

Lista completa = WhatsApp de La Bandita.
