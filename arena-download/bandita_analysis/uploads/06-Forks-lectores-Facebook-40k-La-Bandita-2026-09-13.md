# Publicación — Forks de lectores (La Bandita) · 2026-09-13
> BORRADOR · Facebook / La Bandita · no Discord. Perfil FACEBOOK (Manual 5.2).
> POST: copia desde la primera línea del título hasta hashtags. COMENTARIO FIJADO al final, no es el post.
> No publicar sin firma humana.

FORKS DE LECTORES hasta hashtags.
> Facebook = el mismo copy + comentario fijado. No publicar sin firma humana.

FORKS DE LECTORES · La Bandita · 2026-09-13 (BORRADOR · firma humana pendiente)
**Tiempo estimado de lectura: 28–38 min**
**Índice:** mapa de arriba + el mismo icono en cada título.

# Un fork no es una razón. El repo vivo sí.

**Corte de información:** 2026-09-13
**Clase predominante:** [Fuente] GitHub API y páginas de repo abiertas hoy. [Observación] de esta sesión.
**Grado:** V2 parcial — se abrieron las API de los repos nombrados. No se instaló ninguna app. No se recorrió cada issue.
**Receptor:** La Bandita. No va al ledger. No Discord.
**No es:** una receta de «instala este fork», ni un ranking de «el mejor», ni un lote para mandar a un mantenedor.

**Etiquetas:** `[Fuente]` `[Observación]` `[Inferencia]` `[Reporte externo]` `[No confirmado]` `[No encontrado]` `[Declaración]`

**Idea en una imagen:** un árbol genealógico con mil ramas y una sola pregunta al pie: ¿quién empuja código esta semana y con qué licencia?

```
Mapa de esta guía. El mismo icono abre cada bloque.

├── ⚡  En una página
├── ⚖️  La regla: fork no es criterio
├── 🌳  De dónde sale este árbol
├── 📱  Mihon
├── 📗  TachiyomiSY (el vivo, no el otro)
├── 📘  Komikku
├── 🎬  Aniyomi y Animetail
├── 📦  Kotatsu: archivado (el original)
├── 🚫  Lo que no se pega
├── 🧭  Cómo elegir sin enamorarse del linaje
├── 🚩  Señales de fork muerto o impostor
├── 📌  Correcciones al archivo viejo
├── 📋  Qué hacer esta semana
├── 📄  Apache-2.0, sin bufete
├── 🌙  Nightly no es el tag
├── 🧬  Espejo, fork, rebrand
├── ❓  Preguntas frecuentes
├── 🚧  Límites
├── 📚  Fuentes abiertas hoy
└── 🏁  Cierre
```

> La Bandita informa a partir de fuentes fechadas. Que un repo sea fork de otro nunca es, por sí solo, motivo para recomendarlo (Art. 245).

---

## ⚡ En una página

Tachiyomi cerró el núcleo en enero de 2024. Lo que quedó no es «Tachiyomi con otro nombre»: son proyectos distintos, con dueños distintos, ritmos distintos y una sola regla que el tratado ya tenía antes de este mapa: **uso real, unicidad, madurez, propósito propio**. El parentesco no puntúa.

Hoy, abiertos por API de GitHub:

```
mihonapp/mihon
  23.556 ★  Apache-2.0  v0.20.4 (5-ago-2026)
  push 13-sep-2026  no archivado

jobobby04/TachiyomiSY
  4.144 ★  Apache-2.0  1.13.2 (13-jul-2026)
  push 13-sep-2026  no archivado

komikku-app/komikku
  4.712 ★  Apache-2.0  v1.14.1 (17-jul-2026)
  push 11-sep-2026  no archivado

aniyomiorg/aniyomi
  7.678 ★  Apache-2.0
  push 4-sep-2026  no archivado

Animetailapp/Animetail
  579 ★  Apache-2.0  «Official fork of Aniyomi»
  push 7-sep-2026  no archivado

KotatsuApp/Kotatsu
  8.848 ★  GPL-3.0  ARCHIVADO
  último push 4-nov-2025
```

[Observación] Números de la API el 2026-09-13. Caducan. El de mañana puede ser otro.

La corrección del archivo viejo cabe en una línea: **TachiyomiSY vivo es jobobby04, no mannu691.**

---

## ⚖️ La regla: fork no es criterio

Artículo 245, dicho sin solemnidad: recomendar hacia afuera (y, en casa, tratar algo como «el que hay que usar») pide cuatro puertas. Que sea fork, variante o rebautizo **nunca es, por sí solo**, una de ellas.

```
Uso real
  Alguien de carne lo usa. El asistente no endosa.

Unicidad
  ¿Hace algo que el catálogo del receptor no cubre?
  «Es fork de X» no es unicidad.

Madurez pública
  Docs, releases o instrucciones de compilar,
  autor que responde. Archivado o último push
  de 2024 no pasa esta puerta sin marca.

Propósito propio
  Un cambio de icono no es un propósito.
```

Esta guía **nombra** repos. No dice «instala Komikku porque es el mejor». «Mejor» está prohibido (N-114). Dice: este es el URL, esta es la licencia leída en la API, esta es la release, este es el último push. Tú abres el día que actúes.

---

## 🌳 De dónde sale este árbol

[Reporte externo] Tachiyomi (el original de J2K) dejó de publicar el núcleo en enero de 2024 tras presión legal. La pub de extensiones del 13-sep ya lo fecha con Anime Corner / AlternativeTo. No se reescribe aquí.

Lo que nació alrededor no es un linaje santo. Es gente que copió código Apache-2.0 y siguió. Algunos empujan cada semana. Algunos cambiaron el README y se fueron.

```
Tachiyomi (cerrado, 2024)
   ├── Mihon          sucesor de hecho para manga
   ├── TachiyomiSY    jobobby04
   ├── Komikku        komikku-app
   └── (decenas de forks que no se listan
        por ser forks)

Aniyomi (manga + anime)
   └── Animetail      se declara fork oficial
```

Kotatsu es **otro árbol** (GPL-3.0, parsers propios). El original está archivado. Kototoro, Usagi y los parsers de Gekkoushi viven en otras piezas. Aquí no se mezclan para inflar el mapa.

---

## 📱 Mihon

https://github.com/mihonapp/mihon

[Fuente — API 13-sep-2026] 23.556 ★, 1.504 forks, Apache-2.0, no archivado. Default `main`. Descripción: «Free and open source manga reader for Android». Última release **v0.20.4**, publicada 5-ago-2026. Push de hoy.

[Observación] Es el repo más grande de este mapa en estrellas. Eso no es una puerta del 245. Es un dato.

Keiyoushi (https://keiyoushi.github.io) es el almacén de extensiones que la pub 04 ya cubre. Esta pieza no pega índices. Mihon sin almacén es una app vacía; el almacén sin la app es un zip. Se nombran por separado a propósito.

---

## 📗 TachiyomiSY (el vivo, no el otro)

https://github.com/jobobby04/TachiyomiSY

[Fuente — API] 4.144 ★, 233 forks, Apache-2.0, no archivado. Release **1.13.2** (13-jul-2026). Push **13-sep-2026**.

https://github.com/mannu691/TachiyomiSY

[Fuente — API] 18 ★, **es fork** de jobobby04/TachiyomiSY. Último push **8-jul-2024**. No archivado, pero la puerta de madurez no se sostiene: dos años sin empuje.

[Observación] El archivo viejo de la banda a veces apuntaba al nombre «TachiyomiSY» sin dueño. El nombre no basta. El dueño sí.

Si alguien te pasa un APK «SY» sin repo: misma regla que HappyMod. Se nombra el riesgo. No se enlaza la tienda de mods.

---

## 📘 Komikku

https://github.com/komikku-app/komikku

[Fuente — API] 4.712 ★, 243 forks, Apache-2.0, no archivado. Release **v1.14.1** (17-jul-2026). Push **11-sep-2026**. Descripción idéntica en una línea a la de Mihon y SY: «Free and open source manga reader for Android». Eso no prueba que el código sea el mismo commit. Prueba que el README se parece. Art. 246: señales de actividad se leen; el parentaje se descarta o se afirma con API, no con el eslogan.

[Observación] En estrellas, hoy Komikku > SY. Mañana puede invertirse. No se convierte en veredicto.

La pub 04 del 13-sep ya los listaba (4.711 ★ entonces). Hoy la API dice 4.712. Un ★ no es noticia. Se anota para no fingir que los números de la mañana son eternos.

---

## 🎬 Aniyomi y Animetail

https://github.com/aniyomiorg/aniyomi

[Fuente — API] 7.678 ★, 653 forks, Apache-2.0. Descripción: «An app for manga and anime». Push **4-sep-2026**. No archivado.

https://github.com/Animetailapp/Animetail

[Fuente — API] 579 ★, 28 forks, Apache-2.0. Descripción de la API: «Official fork of Aniyomi». Push **7-sep-2026**.

[Observación] «Official fork» lo declara el propio repo. No se abrió un comunicado de aniyomiorg ratificándolo. Se marca: es la etiqueta que Animetail se pone. El PR #448 (KeiSource 1.6) vive en la pub 04; no se recita.

Anime + manga en la misma app no convierte a Aniyomi en «el TMO de las apps». TMO era un sitio. Esto es un cliente. La pub 05 cubre TMO. Aquí no se pega ninguna fuente.

---

## 📦 Kotatsu: archivado (el original)

https://github.com/KotatsuApp/Kotatsu

[Fuente — API] 8.848 ★, GPL-3.0, **archivado**. Último push **4-nov-2025**.

[Observación] Archivado no es «no existió». Es historia fechada (Art. 63). Kototoro (pub 02, v2.1.1) se declara por su lado. Usagi se declara inspirada en Kotatsu (pub 07). Los parsers de Gekkoushi/plugin-source son otra capa. Ninguno de esos tres es «KotatsuApp/Kotatsu con otro icono» hasta que el README y la API lo digan.

Si un APK se llama Kotatsu y no sale de este repo ni de un sucesor declarado: se trata como APK sin procedencia. La pub 01 cubre eso.

---

## 🚫 Lo que no se pega

Misma lista que extensiones y TMO. Se repite porque el archivo viejo fallaba aquí:

```
- index.min.json / index.pb / raw.githubusercontent de índices
- URL de descarga de JAR (Kotatsu parsers)
- JWT / anon key
- APK de tienda de mods
- Discord como canal de envío
- El repo de mannu691 como si fuera SY
```

Nombrar https://github.com/jobobby04/TachiyomiSY es el recurso. Pegar «releases/latest/download/…apk» como receta de un clic es otra cosa. Esta guía nombra el repo. El APK lo baja quien elija, del release, el día que lo abra (Art. 205).

---

## 🧭 Cómo elegir sin enamorarse del linaje

```
1. ¿Lo usaste?
   Si no, es ficha, no consejo de instalación.

2. ¿El repo está archivado?
   Kotatsu original: sí. No se recomienda como vivo.

3. ¿El último push es de esta semana o de 2024?
   mannu691: 2024. jobobby04: hoy.

4. ¿La licencia está en la API?
   Apache-2.0 o GPL-3.0 aquí. Si la API dice None,
   se dice None. No se inventa (A06).

5. ¿Necesitas anime en la misma app?
   Aniyomi / Animetail lo declaran. Mihon no.

6. ¿Keiyoushi te cubre?
   Su portada lista apps. Se abre el día que actúes.
   https://keiyoushi.github.io
```

No hay un ganador. Hay puertas. Quien las salte porque «el grupo usa X» está usando al grupo como fuente primaria. El grupo no es GitHub.

---

## 🚩 Señales de fork muerto o impostor

```
- Estrellas altas, último commit de 2024,
  README que promete «active development».
- Mismo nombre, otro dueño (mannu691 vs jobobby04).
- APK en Telegram «más actualizado que GitHub».
- «Nightly» sin tag, sin CI, sin SHA.
- Fork de un archivado que no declara el parentaje
  (Art. 246).
- Pide index.min.json en el primer pantallazo.
```

Ninguna señal sola basta. Varias juntas, paras.

---

## 🔍 Cómo leer un repo en diez minutos

Esto es el Art. 205 aplicado a GitHub, sin teatro.

```
1. Abre el HTML del repo, no un recorte de Telegram.
2. Mira si dice Archived. Kotatsu original: sí.
3. LICENSE o el campo license de la API.
   Hoy: Apache-2.0 en Mihon/SY/Komikku/Aniyomi/Animetail.
        GPL-3.0 en Kotatsu archivado.
   Si no hay, se dice «no se encontró», no «es MIT».
4. Releases / latest: tag, fecha, prerelease sí/no.
   SY 1.13.2 = 13-jul. Komikku v1.14.1 = 17-jul.
   Mihon v0.20.4 = 5-ago. El push de hoy no es un tag.
5. pushed_at de la API ≠ fecha de la release.
   Un repo puede empujar traducciones y no sacar APK.
6. ¿Es fork? El campo fork de la API.
   mannu691: true, parent jobobby04.
7. Issues: si el autor responde. No se recorrió
   cada hilo hoy. La puerta «autor que responde»
   queda [No confirmado] salvo que se abra.
8. No se fabrica la URL. github.com/dueño/repo
   tal como la API la devuelve.
```

Diez minutos. Si no caben, no es ficha: es prisa. La prisa es la fila 1.

---

## ⭐ Las estrellas no instalan

23.556 ★ (Mihon) frente a 579 ★ (Animetail) no es un veredicto de calidad. Es un veredicto de fama. La fama llega tarde, se queda cuando el proyecto ya murió, y a veces se compra con un README bonito.

[Inferencia] Kotatsu original tiene 8.848 ★ y está archivado. Si eligieras por ★, instalarías un muerto. Por eso esta guía pone archivado en la misma caja que las estrellas.

Las ★ de hoy (API):

```
Mihon        23.556
Kotatsu †    8.848   (archivado)
Aniyomi      7.678
Komikku      4.712
SY           4.144
Animetail      579
mannu691 SY     18
```

† = no se recomienda como vivo.

---

## 🔄 Biblioteca, backups y «me paso de app»

El archivo viejo prometía a veces que «exportas y listo». Esa frase es A08 si no se probó en el teléfono de Alexis.

[No confirmado] esta sesión: no se migró ninguna biblioteca entre Mihon, SY, Komikku ni Aniyomi. No se receta el botón. Lo que sí se puede decir sin abrir la app:

```
- Cada fork puede tener su propio formato de backup.
- Un backup de 2024 no está verificado contra v0.20.4.
- «Tachiyomi backup» como palabra mágica no prueba
  que SY 1.13.2 lea el JSON de Komikku v1.14.1.
- Probar en copium (copia) no en la única biblioteca.
```

Kototoro tiene su propia historia de backup 1.4–1.7 en la pub 02, como [Declaración] de Alexis, no como receta re-verificada hoy. No se mezcla con Mihon.

---

## 🧩 Extensiones: esta pieza no las receta

Keiyoushi, Yūzōnō, FelipeGFA, Kohi-den: pub 04. Números de esa pub (mismo día, no re-GET aquí): Keiyoushi 14.963 ★, Kohi-den archivado 14-may, Yūzōnō público, Tadami vivo = andarcanum.

Keiyoushi, en lo que esa pub ya abrió, habla de Mihon / SY / Komikku, no de Aniyomi. No se inventa compatibilidad (A09).

```
Esta pieza: la app.
Pub 04: el almacén.
Pub 02: Kototoro.
Pub 07: Usagi (otro árbol, Kotatsu-like).
```

Pegar un índice «para que SY quede igual que Tachiyomi 2023» es exactamente lo que no se copia.

---

## 📌 Correcciones al archivo viejo

```
ANTES                              AHORA (13-sep)

SY = el primer repo que salía      SY vivo = jobobby04
en Google                          mannu691 = fork viejo (2024)

Komikku «el más actualizado»       Komikku = komikku-app,
sin dueño                          v1.14.1, push 11-sep.
                                   No es «el más» de nadie.

Listar 40 forks por ser forks      Art. 245. No.

Pegar índices para que             No. Pub 04.
«funcionen igual que Tachiyomi»

Kotatsu y Mihon como si            Dos árboles. Kotatsu
fueran el mismo código             original archivado.
```

Otaku-Reader, como pieza suelta del volcado: **[No encontrado]** un repo canónico con ese nombre exacto en la API de hoy entre los abiertos para esta guía. No es «no existe». Es que no se localizó para ficha. Si Alexis lo pega, se abre ese día.

---

## 📋 Qué hacer esta semana (sin lote)

```
1. Si usas SY: confirma que el APK salió de
   jobobby04/TachiyomiSY y no de un ZIP de Telegram.
   Abre https://github.com/jobobby04/TachiyomiSY/releases
   el día que lo hagas. Hoy la latest es 1.13.2 (13-jul).

2. Si usas Komikku: mismo gesto con
   https://github.com/komikku-app/komikku/releases
   Latest hoy: v1.14.1 (17-jul). Push del 11-sep ≠ APK nuevo.

3. Si usas Mihon: https://github.com/mihonapp/mihon/releases
   Latest hoy: v0.20.4 (5-ago). Push de hoy no se traduce
   solo en versión.

4. Si te aparece mannu691: no es el vivo.

5. No mandes este mapa a un mantenedor.
   Un ítem, su plantilla, firma humana (Fila 1).

6. Extensiones: pub 04, sin índice pegado.
```

El gesto es siempre el mismo: abrir el release ese día. No esta guía. Esta guía caduca.

---

## 📄 Apache-2.0, dicho sin bufete

[Fuente] La API devuelve `Apache-2.0` para Mihon, SY, Komikku, Aniyomi, Animetail. Kotatsu original: `GPL-3.0`.

Esto no es asesoría legal. Es lo que el campo `license.spdx_id` dijo hoy. Apache-2.0 permite, en términos generales que el propio texto de la licencia explica, usar, modificar y distribuir con aviso. GPL-3.0 pide que las modificaciones que se distribuyan sigan siendo GPL.

[Observación] No se abrió el archivo LICENSE byte a byte en cada repo esta tarde; se leyó el SPDX de la API. Si alguien va a redistribuir un APK, que abra LICENSE ese día. Esta guía no redistribuye.

Un APK «SY mod premium» en una tienda de mods no hereda la confianza de Apache-2.0 del repo. Hereda la tienda. Pub 01.

---

## 🌙 Nightly no es licencia para saltarse el tag

Push de hoy ≠ nightly usable. Nightly, si existe, vive en Actions o en un tag `nightly`. No se abrió el workflow de cada repo hoy.

[No confirmado] que Mihon, SY o Komikku tengan un nightly instalable y firmado el 13-sep. No se receta.

Kototoro sí tiene Nightly vivo en su propio repo: eso es la pub 02, no este mapa. No se mezcla.

---

## 🧬 Espejo, fork, rebase, rebrand

Art. 246 otra vez, con ejemplos de esta API:

```
Fork declarado
  mannu691/TachiyomiSY → parent jobobby04.
  La API lo dice. No se discute.

Rebrand declarado
  Animetail: «Official fork of Aniyomi» en description.
  Es su frase. No es un notario.

Archivado
  KotatsuApp/Kotatsu. El letrero sigue. El taller no.

Espejo
  Un GitLab que copia a Mihon cada noche puede
  tener commits «recientes» y ser solo sync.
  Hoy no se abrió un espejo concreto.
  Si aparece, se compara con github.com/mihonapp/mihon
  antes de llamarlo proyecto.
```

«Activo» se gana descartando el espejo, no contando commits a ciegas.

---

## ❓ Preguntas frecuentes

**¿Cuál instalo?**
El que uses y verifiques. Esta guía no elige por ti.

**¿Mihon es Tachiyomi?**
No. Tachiyomi cerró. Mihon es otro repo, Apache-2.0, vivo hoy.

**¿Komikku es mejor que SY?**
«Mejor» no se usa. Hoy Komikku tiene más ★ y un push del 11-sep; SY empujó hoy. Ningún ★ instala la app por ti.

**¿Puedo mandar este mapa al catálogo externo?**
No. Es un lote. Art. 247. Un ítem, formato del receptor, firma humana. Fila 1 ya enseñó eso.

**¿Y las extensiones?**
Pub 04. Sin receta de índice.

**¿Y Kototoro?**
Pub 02. v2.1.1. No es un fork de Mihon.

**¿Animetail es «oficial»?**
Lo dice su descripción de GitHub. No se abrió un sello de aniyomiorg.

**¿Por qué no listáis los 200 forks?**
Porque ser fork no puntúa. C05: relleno para parecer exhaustivo.

**¿mannu691 es malware?**
No se afirma. Se afirma: es fork, 18 ★, push 2024. No pasa madurez como sucesor.

**¿Puedo pegar esto en Discord?**
No hay envío a Discord.

---

## 🚧 Límites

```
CAMPO DE VERDAD — Forks · 2026-09-13

Abierto hoy (API GitHub):
  mihonapp/mihon
  jobobby04/TachiyomiSY
  mannu691/TachiyomiSY
  komikku-app/komikku
  aniyomiorg/aniyomi
  Animetailapp/Animetail
  KotatsuApp/Kotatsu

No se instaló ninguna app.
No se abrió cada release APK.
No se recorrió el árbol completo de forks.
Keiyoushi.github.io se nombra; el detalle de
extensiones es la pub 04.

No se afirma:
  que X sea más seguro
  que Y tenga más fuentes
  que Animetail esté «avalado» más allá
    de su propia descripción
```

---

## 📚 Fuentes abiertas hoy

https://github.com/mihonapp/mihon
https://github.com/jobobby04/TachiyomiSY
https://github.com/mannu691/TachiyomiSY
https://github.com/komikku-app/komikku
https://github.com/aniyomiorg/aniyomi
https://github.com/Animetailapp/Animetail
https://github.com/KotatsuApp/Kotatsu
https://keiyoushi.github.io

API: https://api.github.com/repos/… (mismas rutas, 2026-09-13)

Canon del día, no reescrito: tiendas, Kototoro v2.1.1, ADV, extensiones, TMO.

---

## 🏁 Cierre

El árbol es ancho. La regla es estrecha: **fork no es motivo**. jobobby04 empuja. mannu691 no. Komikku vive. Kotatsu original está archivado. Mihon es el más grande en ★ y eso no te obliga.

Si esta pieza sirve, que sea para dejar de instalar el primer resultado que se llama igual. El nombre es el letrero. El repo es la tienda.

> La Bandita informa a partir de fuentes fechadas. Un fork no es una razón.

#Mihon #TachiyomiSY #Komikku #Aniyomi #Animetail #Kotatsu #FOSS #LaBandita #Septiembre2026

---
COMENTARIO FIJADO — no forma parte del post. Primer comentario, fijar.

Forks de lectores — La Bandita
Fecha: 2026-09-13
Versión: BORRADOR 2026-09-13

Índice (el mismo icono abre cada bloque)

⚡ En una página
⚖️ Fork no es criterio
🌳 El árbol
📱 Mihon
📗 TachiyomiSY
📘 Komikku
🎬 Aniyomi / Animetail
📦 Kotatsu archivado
🚫 No se pega
🧭 Cómo elegir
🚩 Señales
🔍 Leer un repo
⭐ Estrellas
🔄 Backups
🧩 Extensiones
📌 Correcciones
📋 Esta semana
📄 Apache-2.0
🌙 Nightly
🧬 Espejo / fork
❓ FAQ
🚧 Límites
📚 Fuentes
🏁 Cierre

Corrección: SY vivo = jobobby04, no mannu691. Kotatsu original archivado. Fork no es motivo.
