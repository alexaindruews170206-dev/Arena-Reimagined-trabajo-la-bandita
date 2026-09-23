# Publicación — Usagi (La Bandita) · 2026-09-13
> BORRADOR · Facebook / La Bandita · no Discord. Perfil FACEBOOK (Manual 5.2).
> POST: copia desde la primera línea del título hasta hashtags. COMENTARIO FIJADO al final, no es el post.
> No publicar sin firma humana.

USAGI (LECTOR KOTATSU-LIKE) · La Bandita · 2026-09-13 (BORRADOR · firma humana pendiente)
**Tiempo estimado de lectura: 24–32 min**
**Índice:** mapa + el mismo icono.

# Usagi no es Mihon. Es otro árbol. Los plugins no se recetan.

**Corte:** 2026-09-13. [Fuente] GitHub API y README de Gekkoushi/plugin abiertos hoy. Sin instalar la app. Sin bajar artefactos.
**Grado:** V2 parcial sobre repos. V0 sobre «funciona en tu teléfono».
**No es:** receta de plugins, ni JAR, ni Discord, ni «el nuevo Kotatsu».

```
Mapa de esta guía.

├── ⚡  En una página
├── 🌳  Otro árbol (Kotatsu, no Tachiyomi)
├── 📱  UsagiApp/Usagi
├── 🧩  Gekkoushi/plugin (artefactos)
├── 🧬  plugin-source (el código)
├── 🔌  UMA (InvalidDavid)
├── 🚫  Lo que no se pega
├── 📌  Correcciones
├── ❓  FAQ
├── 🚧  Límites
├── 📚  Fuentes
└── 🏁  Cierre
```

---

## ⚡ En una página

Kotatsu original está **archivado** (pub 06). Usagi se declara lectora FOSS de Android **inspirada en Kotatsu**. No es un fork de Mihon. No usa el índice de Keiyoushi. Si mezclas los dos árboles, rompes las dos fichas.

Hoy, API GitHub:

```
UsagiApp/Usagi
  255 ★  60 forks  GPL-3.0  no archivado
  push 11-sep-2026
  latest: v1.0 (9-sep-2026)

Gekkoushi/plugin
  7 ★  0 forks  license API = None
  push 13-sep-2026 (README)
  latest tag 75af884 (10-ago-2026)
  README: artefactos para Usagi / Tsuki
  «No updates, 1.3k sources»
  «Only for the Usagi App»
  UMA «Only for the 1.0 version»

Gekkoushi/plugin-source
  90 ★  72 forks  GPL-3.0
  push 13-sep-2026
  «Manga Parsers library for Kotlin/JVM and Android»

InvalidDavid/UMA
  68 ★  GPL-3.0
  push 13-sep-2026
  latest tag 7a60bfa (13-sep-2026)
  description: «UMA Plugin for the Usagi App or other Kotatsu Forks»

UsagiApp/plugins   10 ★  GPL-3.0  push 27-jul-2026
UsagiApp/Tsuki      7 ★  GPL-3.0  push 27-jul-2026
```

[Observación] YakaTeam/kotatsu-parsers, al pedirlo a la API, devolvió el HTML de Gekkoushi/plugin-source. No se trata como segundo proyecto. Se trata como el mismo repo visto con otro nombre, o como redirección. No se receta «YakaTeam».

---

## 🌳 Otro árbol (Kotatsu, no Tachiyomi)

Pub 06: Mihon / SY / Komikku / Aniyomi = Apache-2.0, extensiones tipo Keiyoushi.

Este mapa: GPL-3.0, parsers tipo Kotatsu. Kototoro (pub 02) vive aquí cerca y **no se duplica**. Usagi no es Kototoro. Kototoro no es Usagi.

[Fuente — README Usagi, abierto a medias hoy] «free and open-source manga reader for Android, inspired by Kotatsu». Android 5.0+ en badges. El README enlaza F-Droid (`org.draken.usagi`). **F-Droid no se abrió hoy.** La ficha de F-Droid queda [No confirmado]. El README no basta para decir «está en F-Droid ahora».

No se pega el Discord ni el Telegram que el README exhibe. Discord no es canal de envío.

---

## 📱 UsagiApp/Usagi

https://github.com/UsagiApp/Usagi

[Fuente — API] 255 ★, GPL-3.0, v1.0 publicada **9-sep-2026**, push **11-sep-2026**, 358 commits en la rama vista por la página. Org: UsagiApp. Sponsor visible: dragonx943.

[Observación] v1.0 es un número de nacimiento, no de madurez de diez años. Art. 245, puerta de madurez: docs, release, autor. Hay release. Hay README. «Autor que responde» no se recorrió en issues hoy. [No confirmado]

sang765/Usagi y dragonx943/Usagi (3 ★, push 2-ago) existen en el bosque. El canónico de esta ficha es **UsagiApp/Usagi**. Art. 246.

---

## 🧩 Gekkoushi/plugin (artefactos)

https://github.com/Gekkoushi/plugin

README abierto hoy (commit «Update links in README for Usagi App», 13-sep-2026, InvalidDavid):

- Artefactos para Usagi y apps con estructura Tsuki.
- **Only for the Usagi App.**
- UMA: Automatic or Manual, **Only for the 1.0 version.**
- Este repo: «No updates, 1.3k sources».
- Código: plugin-source.
- Issues: plugin-source.
- Dice GPL en prosa; la API de license del repo plugin es **None**. Se marca la discrepancia: README habla de GPL; el campo SPDX de la API no está. plugin-source sí trae GPL-3.0.

**No se pega** `releases/latest/download/…`. Misma regla que JAR de Kotatsu y que mods: se nombra el repo; no se facilita el clic de instalación.

«1.3k sources» es la cifra del README. No se recontaron 1.300 parsers hoy. [Fuente: README, no recuento propio]

---

## 🧬 plugin-source (el código)

https://github.com/Gekkoushi/plugin-source

[Fuente — API] 90 ★, 72 forks, GPL-3.0, push **hoy**. Descripción: librería de parsers Kotlin/JVM y Android.

Aquí se contribuye, según el README del repo de artefactos. Aquí no se pega un índice tipo `index.min.json`. Otro protocolo, otro árbol.

Shebyyy/kotatsu-multi-parsers (13 ★, push hoy) ya está en Miyomi (pub 04). No se receta el JAR.

---

## 🔌 UMA (InvalidDavid)

https://github.com/InvalidDavid/UMA

[Fuente — API] 68 ★, GPL-3.0, push hoy, latest **7a60bfa** publicada **13-sep-2026**. Description: plugin UMA para Usagi u otros forks de Kotatsu.

El README de Gekkoushi/plugin dice «Only for the 1.0 version». Usagi latest es v1.0. Eso **encaja en números**. No prueba que UMA 7a60bfa se haya instalado en un teléfono. No se receta.

---

## 🚫 Lo que no se pega

```
- URL de descarga de artefactos / JAR
- index.min.json / index.pb
- Discord / Telegram de Usagi o de Gekkoushi
- F-Droid como hecho (no se abrió)
- YakaTeam como repo distinto (la API redirigió)
```

---

## 📌 Correcciones

```
ANTES                         AHORA
Usagi = YakaTeam a ciegas     App canónica = UsagiApp/Usagi
                              v1.0 (9-sep)

Plugins = pegar el zip        Se nombra Gekkoushi/plugin
                              No se pega la descarga

UMA «solo v1.0» como rumor    README de plugin lo dice hoy.
                              UMA empujó un tag hoy (7a60bfa).
                              No se mezclan sin marca.

Kotatsu original vivo         Archivado (4-nov-2025).
```

---

## ❓ FAQ

**¿Usagi reemplaza a Kototoro?**
No se afirma. Son fichas distintas. Kototoro v2.1.1 es pub 02.

**¿Puedo ponerle fuentes de Keiyoushi?**
No se verificó. Son árboles distintos. No se receta.

**¿Está en F-Droid?**
El README lo afirma. F-Droid no se abrió hoy. [No confirmado]

**¿1.3k fuentes son reales?**
Cifra del README. No recontadas.

**¿YakaTeam?**
No se usa como destino. La API apuntó a Gekkoushi/plugin-source.

**¿Discord?**
No hay envío.

**¿Lo usó Alexis?**
Esta guía no lo afirma. Art. 245, uso real: él firma.

---

## 🚧 Límites

```
CAMPO DE VERDAD — Usagi · 2026-09-13
Abierto: API UsagiApp/Usagi, plugins, Tsuki,
Gekkoushi/plugin + README, plugin-source,
InvalidDavid/UMA + latest.
No abierto: F-Droid, Discord, cada parser,
APK instalada.
No se pega descarga de plugin.
```

---

## 📚 Fuentes

https://github.com/UsagiApp/Usagi
https://github.com/UsagiApp/plugins
https://github.com/UsagiApp/Tsuki
https://github.com/Gekkoushi/plugin
https://github.com/Gekkoushi/plugin-source
https://github.com/InvalidDavid/UMA
https://github.com/KotatsuApp/Kotatsu

---

## 🏁 Cierre

Usagi es v1.0, GPL, árbol Kotatsu. Los artefactos se nombran; no se pegan. Kotatsu original está archivado. Si sirve, que sea para no tratar a Usagi como un Mihon con orejas.

> La Bandita informa a partir de fuentes fechadas.

#Usagi #Kotatsu #Gekkoushi #UMA #FOSS #LaBandita #Septiembre2026

---
COMENTARIO FIJADO — no forma parte del post. Primer comentario, fijar.

Usagi — La Bandita
Fecha: 2026-09-13
Versión: BORRADOR 2026-09-13

Índice (el mismo icono abre cada bloque)

⚡ En una página
🌳 Otro árbol
📱 UsagiApp/Usagi
🧩 Gekkoushi/plugin
🧬 plugin-source
🔌 UMA
🚫 No se pega
📌 Correcciones
❓ FAQ
🚧 Límites
📚 Fuentes
🏁 Cierre

Corrección: app = UsagiApp/Usagi v1.0. Artefactos se nombran, no se descargan aquí. YakaTeam no es destino.
