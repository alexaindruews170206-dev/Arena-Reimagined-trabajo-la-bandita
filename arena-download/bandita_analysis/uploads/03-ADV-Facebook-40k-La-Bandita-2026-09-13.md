# Publicación — Android Developer Verification (La Bandita) · 2026-09-13
> BORRADOR · Facebook / La Bandita · no Discord. Perfil FACEBOOK (Manual 5.2).
> Límite observado ~40k incluso con Meta Premium. POST: copia desde ANDROID DEVELOPER VERIFICATION hasta hashtags.
> Pedido de esta pieza: Facebook entre 30k y 40k. Lista completa = WhatsApp (63.000).
> COMENTARIO FIJADO: bloque del final. No publicar sin firma humana.
> Corte vivo: 2026-09-13. El texto original traía corte 2026-07-28 y tablas; ambas cosas se corrigen.

ANDROID DEVELOPER VERIFICATION · La Bandita · 2026-09-13 (BORRADOR · firma humana pendiente)
**Tiempo estimado de lectura: 28–35 min**
**Índice:** mapa de arriba + el mismo icono en cada título. Resumen en el comentario fijado.

# Android Developer Verification: cronograma, mecanismo e implicaciones (corte 2026-09-13)

**Corte de información:** 2026-09-13
**Clase predominante:** [Fuente] (Google) y [Observación] de páginas abiertas hoy. Sin prueba en un teléfono.
**Grado:** V2 parcial — hub, guías, FAQ, ADC (4-sep-2026) y limited-distribution de [https://developer.android.com](https://developer.android.com) abiertos hoy; F-Droid (29-sep-2025) y Keep Android Open (portada, FAQ, carta abierta 24-feb-2026) reabiertos hoy. Blogs de [https://android-developers.googleblog.com](https://android-developers.googleblog.com): fetch bloqueado (ERR_BLOCKED_BY_CLIENT); se citan como enlaces del hub, no como texto leído.
**Receptor:** La Bandita (Facebook / WhatsApp). No va al ledger. No Discord.
**No es:** asesoría legal, ni veredicto de si la medida es «buena» o «mala», ni una orden de registrarse o de no registrarse.

**Etiquetas:**
`[Fuente]` = lo que declara Google u otro proyecto en página abierta.
`[Observación]` = lo visto en esta sesión.
`[Inferencia]` = deducción marcada.
`[Reporte externo]` = medios; yo no abrí todas sus páginas.
`[No confirmado]` = no se pudo verificar al corte.

```
Mapa de esta guía. El mismo icono abre cada bloque.
Índice corto: primer comentario (fijado). Lista completa: WhatsApp.

├── ⚡  Resumen: ¿te toca el 30 de septiembre?
├── 📅  Cronograma (lo que Google publica hoy)
├── 🪪  Qué es la verificación
├── 📱  Cómo opera en el dispositivo
├── 🏪  Tiendas del 30 de septiembre
├── ↔️  Lo que no cambia (y lo que sí, en 2027)
├── 🛠️  Flujo avanzado y ADB
├── 👤  Impacto por perfil
├── ❓  FAQ de Google, pregunta por pregunta
├── 🔧  Android Developer Console
├── 🎓  Distribución limitada
├── 📜  Carta abierta (24-feb-2026)
├── 📣  Keep Android Open (campaña)
├── 📗  F-Droid, 29-sep-2025
├── 🏛️  Firmantes visibles
├── 📌  Correcciones al corte 28-jul
├── 🌍  República Dominicana y LATAM
├── 🔗  Relación con las otras guías
├── ⚖️  El debate, con fuentes
├── 🚧  Límites de este texto
├── ✅  Acciones concretas
└── 📚  Fuentes abiertas hoy
```

> La Bandita informa a partir de fuentes fechadas. Si vas a registrarte o a cambiar de ROM, reabre [https://developer.android.com/developer-verification](https://developer.android.com/developer-verification) el día que actúes.

---

## ⚡ Resumen: ¿te toca el 30 de septiembre?

Hoy es 13 de septiembre de 2026. Faltan 17 días para el hito que Google titula «Next milestone: September 30, 2026». [Fuente — hub]

Ese día **no** es, según la FAQ de Google (actualizada 15-jul-2026), un cierre mundial del sideload ni un bloqueo de F-Droid. El 30 de septiembre aplica a **tiendas participantes** en **cuatro países**, en **dispositivos certificados** con **Android 7 o superior**. [Fuente]

```
Situación                                         ¿El 30-sep-2026 te cambia la vía normal?
Solo Play / Galaxy / GetApps / etc.               Si el desarrollador está registrado, Google
(y el dev está verificado)                        dice que la experiencia no cambia. [Fuente]

Vives en República Dominicana (u otro país        Ese día no eres país piloto. El salto
fuera de BR / ID / SG / TH)                       «a todas las apps en certificados» es 2027.
                                                  [Fuente] Reabre la página: el mapa se mueve.

Instalas APK a mano o usas F-Droid / Obtainium    El 30-sep, Google dice que sideload directo
                                                  y tiendas no listadas AÚN no entran.
                                                  Keep Android Open confirma: F-Droid no está
                                                  en la lista de septiembre. [Fuente]
                                                  El 2027 es otra frase.

Desarrollas y publicas fuera de Play              Sí te toca prepararte: identidad + registrar
                                                  paquetes antes del despliegue que te aplique.
                                                  [Fuente]

Cuenta limitada (hobby / estudiante)              Hasta 20 dispositivos, sin ID gubernamental
                                                  ni tasa de 25 USD. Sigue pidiendo cuenta
                                                  Google, 2FA y perfil de pagos (nombre y
                                                  dirección). [Fuente — guía limited, 20-ago-2026]

ROM / dispositivo sin certificación Google        Google habla de certified Android devices.
                                                  No se probó LineageOS aquí. [No confirmado]
```

El texto que corregimos (corte 28-jul-2026) mezclaba el hito de septiembre con un bloqueo general de APKs. Eso ya no coincide con la FAQ de Google ni con Keep Android Open. [Observación]

Tres frases que hay que poder repetir sin mezclarlas:

```
1. 30-sep-2026 = 4 países + 7 tiendas + certificados Android 7+.
2. Sideload directo y tiendas no listadas: «won't apply … yet» (FAQ, 15-jul-2026).
3. 2027 = «all apps on certified devices». Sin mes en el hub.
```

Keep Android Open, en su FAQ de hoy, dice lo mismo sobre septiembre: el despliegue inicial se limitó a una lista de tiendas que no incluye F-Droid; «the date at which the lockdown will start impacting F-Droid users is not yet published». [Fuente — https://keepandroidopen.org/faq/](https://keepandroidopen.org/faq/) Su portada sigue hablando de 2027 y de una cuenta atrás. No unifico portada de campaña, FAQ de campaña y hub de Google: cada una dice lo suyo.

---

## 📅 Cronograma (lo que Google publica hoy)

Anuncio inicial: agosto 2025 (no «noviembre 2025»). F-Droid lo trató el 29-sep-2025. [Fuente / Observación] Keep Android Open, en portada, también sitúa el anuncio en agosto 2025 y enlaza el hub de [https://developer.android.com](https://developer.android.com). [Fuente — portada]

Hitos que el hub y las guías de Google muestran ahora (páginas last updated 18-ago-2026 / 27-ago-2026 / 20-ago-2026 / 4-sep-2026):

```
Ago 2025       Anuncio del programa. [Fuente — hub / F-Droid / KAO]

Marzo 2026     Apertura del proceso a todos (Play Console y
               Android Developer Console). El hub enlaza un blog
               de marzo que hoy no se pudo leer. [Fuente — hub]
               [No confirmado el texto del blog]

Jun 2026       El hub enlaza otro blog: «Building a safer
               ecosystem together» (junio 2026). Fetch bloqueado.
               [Observación]

Ago 2026       Cuentas de distribución limitada «available for
               everyone» (guía, actualizada 20-ago-2026).
               Flujo avanzado: Google lo anuncia para agosto.
               No se reprodujo en un teléfono. [Fuente / No confirmado]

4 sep 2026     Guía de Android Developer Console, last updated.
               [Fuente / Observación]

30 sep 2026    «Next milestone». Protecciones para instalaciones
               desde tiendas participantes en Brasil, Indonesia,
               Singapur y Tailandia, dispositivos certificados
               Android 7+. [Fuente — hub]

2027           «We'll expand this globally to all apps on
               certified devices.» Sin calendario regional
               publicado en el hub. [Fuente]
```

La guía de Google (guides, 18-ago-2026) dibuja además una línea de hitos técnicos que el diagrama nombra: junio 2026, servicio del sistema y acceso temprano a limited distribution; julio 2026, Status API global, Console API y limited distribution en early access; agosto 2026, Console API global, limited distribution y flujo avanzado; 30 de septiembre, el hito de las cuatro regiones. [Fuente — guides] El diagrama se vio; no se transcribe como captura. Las fechas de API no se probaron con una llamada. [No confirmado]

Keep Android Open (FAQ, abierta hoy): el cierre de septiembre se actualizó para limitarse a una lista de tiendas que **no incluye F-Droid**. [Fuente]

---

## 🪪 Qué es la verificación

No es el permiso de publicar en Play (eso ya existía). Es vincular una identidad (persona u organización) con los nombres de paquete y las claves de firma, también fuera de Play. [Fuente — guides]

La guía lo dice en una frase: «Android developer verification links real-world entities (individuals and organizations) with their Android applications.» Y añade que Android exigirá que las apps estén registradas por desarrolladores verificados para instalarse en dispositivos certificados. [Fuente]

Google, en «Why these changes are happening»: protege a los usuarios al disuadir a actores maliciosos y al hacer más difícil que repitan el daño. En «How this helps you»: disuade a quien prefiere operar en anónimo; vincula apps malas con sus autores; aumenta la confianza del usuario. [Fuente — guides] Eso es el marco de Google. F-Droid y Keep Android Open lo leen al revés: censo, no escáner. Cada voz se cita en su bloque.

Dos consolas:

Play Console                 Si distribuyes en Play (y, si quieres,
                             también fuera). Play registra el 99 %
                             de las apps automáticamente. [Fuente — hub]
                             Guía: [https://play.google.com/console/signup](https://play.google.com/console/signup)

Android Developer Console    Si distribuyes solo fuera de Play.
                             [https://android.google.com/developerconsole](https://android.google.com/developerconsole)
                             [Fuente]
                             Guía actualizada 4-sep-2026.

Tres caminos que Google dibuja en la guía (sin tabla; Facebook se las come):

```
Distribución completa
  Identidad: sí. Tasa ADC: 25 USD (FAQ, 25-mar-2026). [Fuente]
  Llegas a cualquier tienda o canal que elijas.
  Experiencia del usuario: Google dice que no cambia.
  Pensado para organizaciones y profesionales.

Distribución limitada (hobby, estudiante, aula)
  Identidad gubernamental: no. Tasa: no. Tope: 20 dispositivos
  autorizados por el usuario (QR o enlace). [Fuente]
  Sigue pidiendo cuenta Google, verificación en 2 pasos y
  perfil de pagos (nombre legal y dirección). [Fuente]
  Migración limitada → completa: sí. Al revés: no. [Fuente — FAQ]

Sideload de apps no registradas
  Identidad: no. El usuario usa flujo avanzado o ADB. [Fuente]
  Google: salvaguardas extra «to break the cycle of potential
  coercion». [Fuente — guides]
```

La guía insiste en dos notas al pie de esos caminos: tus apps se pueden seguir sideloadeando; la experiencia del usuario cambia según el camino; el flujo ADB no cambia. [Fuente]

Organizaciones: D-U-N-S (hasta 28 días, dice Google) y, en el marco de identidad, documentación. [Fuente] El D-U-N-S es un identificador de nueve dígitos de Dun & Bradstreet; Google enlaza dnb.com para pedirlo gratis. [Fuente — FAQ]

Si pierdes la clave de firma, no puedes registrar el paquete. [Fuente — FAQ]

Países sancionados: Google dice que quedan fuera de las comprobaciones; cualquier desarrollador puede seguir distribuyendo ahí sin verificación, «though users there won't benefit from the enhanced security benefits of the program». [Fuente — FAQ, 25-mar-2026]

Help Center que el hub nombra (no se abrieron hoy): support.google.com/android-developer-console y Play Console Help. [Observación — enlaces del hub, páginas no leídas]

---

## 📱 Cómo opera en el dispositivo

Google dice que los requisitos se aplican en dispositivos **certificados** con **Android 7 o superior**, y que las actualizaciones llegan por **Google Play services**. [Fuente — FAQ, 23-mar-2026] Enlace que Google usa para «certified»: android.com/certified/partners/. Esa lista de socios no se reabrió hoy. [No confirmado el catálogo de socios]

El nombre «Android Developer Verifier» circula en prensa. En las páginas de [https://developer.android.com](https://developer.android.com) abiertas hoy, Google habla de «protections» y de Play services, no se copió ese nombre de producto. [Observación] No se afirma aquí como nombre oficial leído.

Flujo que Google describe para la vía normal:

```
1. El sistema comprueba si la app está registrada por un
   desarrollador verificado.
2. Si sí: instalación como hasta ahora (según Google).
3. Si no: la vía normal no basta; ADB o flujo avanzado.
[Fuente — guides / FAQ]
```

El 30 de septiembre, eso se enfoca en las **siete tiendas listadas** y los **cuatro países**. Sideload directo y tiendas no listadas: «won't apply to your app yet» (FAQ, 15-jul-2026). [Fuente]

Formatos el 30-sep: si el desarrollador publica en Play, Google dice que hay que registrar las apps en todos los formatos. Fuera de Play, recomienda registrar todos los formatos «to future-proof», pero la aplicación del 30-sep fuera de Play es móvil y tablet, en las regiones seleccionadas. [Fuente — FAQ, 15-jul-2026]

Keep Android Open lee el mismo mecanismo como un cierre silencioso empujado por Play Services, no por el sistema, y dice que Google puede apretarlo sin OTA. [Fuente — campaña] Es la lectura de la campaña, no un test nuestro.

---

## 🏪 Tiendas del 30 de septiembre

Siete, no seis. Hub y guía, abiertos hoy. La guía las nombra con fabricante:

```
Google (Google Play)
Honor (HONOR App Market)
OPlus (OPPO App Market)
Samsung (Galaxy Store)
Transsion (Palm Store)
vivo (V-Appstore)
Xiaomi (GetApps)
```

F-Droid, Obtainium, Komi, Aurora, Appteka, IzzyOnDroid: **no** están en esa lista. [Observación] Keep Android Open lo dice explícito para F-Droid. [Fuente]

Google: «The verification capability will soon be expanded to all third-party Android app stores» y, en 2027, a todas las apps en certificados. [Fuente — guides] «Soon» no es una fecha. No se inventa.

La guía presenta el 30-sep como «a collective effort across the mobile industry». [Fuente] Eso es el marco de Google, no un acuerdo leído con Honor, OPPO, Samsung, Transsion, vivo o Xiaomi. No se abrieron comunicados de esas tiendas hoy. [No confirmado]

---

## ↔️ Lo que no cambia (y lo que sí, en 2027)

**Sideload.** Google insiste en que Android sigue abierto y que el sideload no desaparece. Cambia la fricción para apps no registradas, sobre todo cuando el requisito se extienda. [Fuente] FAQ (18-jun-2026): «Does this mean Android is becoming a closed system? No.» La mayoría de usuarios, dice, bajará apps de desarrolladores verificados y no notará cambio; los power users podrán instalar no verificadas tras el flujo avanzado de una vez, anunciado para agosto 2026. [Fuente]

**ADB.** Sin cambios. Sin espera de 24 h. [Fuente — FAQ]

**El 30 de septiembre vs 2027.** Mezclarlos es el error del texto de julio. Septiembre = tiendas participantes + 4 países. 2027 = «all apps on certified devices», sin mes en el hub. [Fuente]

**Empresa / EMM.** FAQ (3-sep-2025): apps de la tienda de la organización en dispositivos gestionados no necesitan completar la verificación; Google recomienda registrarlas igual por si salen del canal gestionado o van a un aparato no gestionado. [Fuente] La frase del borrador viejo («margen hasta septiembre de 2027 para EMM») **no** apareció en las páginas de Google abiertas hoy. Se deja fuera. [No confirmado]

**Play App Signing.** Si lo usas, Google dice que tiene lo necesario para identificar la propiedad y que las apps elegibles entran en el registro automático. [Fuente — FAQ]

**NDA.** Google dice que la verificación se centra en la identidad del desarrollador, no en el contenido de la app, y que no hay que compartir contenido confidencial. [Fuente — FAQ, 25-mar-2026] No se audita un NDA aquí.

---

## 🛠️ Flujo avanzado y ADB

Google lo describe como **configuración de una vez**, no como 24 h por cada APK. [Fuente — FAQ, 23-mar-2026]

Pasos que publica (no reproducidos aquí):

```
1. Activar modo desarrollador.
2. Confirmar que nadie te está «coaching» para bajar la seguridad.
3. Reiniciar y volver a autenticarte (corta llamadas/remoto, dice Google).
4. Esperar un día (24 h). Luego biometría o PIN.
5. Aceptar riesgos: 7 días o indefinido.
6. Al instalar una app no verificada, sigue saliendo aviso;
   «Install Anyway».
[Fuente — FAQ]
```

No hace falta dejar el modo desarrollador encendido después. Google lo dice porque algunas apps (bancos, etc.) no te dejan usarlas con Developer Mode on. [Fuente] No hay comando ADB para saltarse las 24 h «at this point»; «we will consider this for future versions». [Fuente] Si apagas el flujo avanzado, las apps no registradas no se instalan ni se actualizan (salvo ADB). [Fuente] Tampoco puedes actualizar las no registradas que ya tengas instaladas sin el flujo o ADB. [Fuente]

Keep Android Open describe un flujo de nueve pasos y dice que corre por Play Services, no por el sistema, y que Google puede apretarlo sin OTA. [Fuente — campaña] Los nueve pasos que publica la portada, parafraseados:

```
1. Ajustes → Acerca del teléfono.
2. Tocar el número de compilación siete veces (modo desarrollador).
3. Descartar pantallas de «coerción».
4. Introducir el PIN.
5. Reiniciar.
6. Esperar 24 horas.
7. Volver, descartar más pantallas.
8. Elegir «allow temporarily» (7 días) o «allow indefinitely».
9. Confirmar otra vez que entiendes «the risks».
[Fuente — portada KAO]
```

La campaña lo llama «escape hatch» que es una trampilla: nueve pasos, 24 h, enterrado en opciones de desarrollador, entregado por un servicio propietario que Google puede revocar. [Fuente — campaña] Es la lectura de la campaña, no un test nuestro.

Lanzamiento global del flujo: Google lo sitúa en agosto 2026. Hoy es 13-sep; no se comprobó en un aparato si ya está en tu teléfono. [No confirmado]

El hub enlaza un Short de YouTube («Preview how users can sideload your apps», WcPElxbOeXY) y un vídeo largo (A7DEhW-mjdc). No se vieron hoy. [No confirmado el contenido de los vídeos]

---

## 👤 Impacto por perfil

**Usuario en República Dominicana, solo Play.** El 30-sep no eres piloto. Si tus apps vienen de Play y están registradas, Google dice que no notas nada. El 2027 sí está en la hoja de ruta mundial. [Fuente / Inferencia de calendario]

**Usuario que sideloadea (F-Droid, Obtainium, APK de GitHub).** El 30-sep, según Google, todavía no. Prepárate para 2027: firmas, canal, y no confundir Obtainium-hacia-GitHub con Obtainium-hacia-un-portal-de-mods. [Inferencia] F-Droid sigue vivo y en alerta; no es «muerto el 30 de septiembre». [Fuente — KAO FAQ + portada F-Droid]

**Desarrollador que publica APKs (Kototoro, clientes FOSS, etc.).** Registrar paquete y clave. Play Console si ya estás en Play; si no, Android Developer Console. 25 USD en cuenta completa. Hobby: limitada, 20 dispositivos. [Fuente]

**Quien publica en anónimo.** Google: limitada sin ID, o usuarios con flujo avanzado. No hay vía anónima de distribución amplia en certificados cuando el requisito se extienda. [Fuente]

**IT / empresa.** Canal gestionado = excepción declarada. Registrar igual, recomienda Google. [Fuente]

**Estudiante / aula.** Limited distribution: compartir con compañeros y profesores, proyectos de curso. Sigue pidiendo cuenta Google + 2FA + perfil de pagos. [Fuente — guía limited]

**Quien vive en un país sancionado (según Google).** Queda fuera de las comprobaciones. [Fuente] Esta guía no lista países sancionados.

**Quien viaja.** Si sales de RD hacia BR/ID/SG/TH con un certificado y Play services, el hito de esas tiendas puede aplicarte allí. No se probó. [No confirmado]

---

## ❓ FAQ de Google, pregunta por pregunta

FAQ last updated 2026-08-27. [Fuente] Lo que más se malinterpreta, parafraseado. El resto de ítems (D-U-N-S, NDA, APIs, Studio Panda 4, claves múltiples) = WhatsApp.

```
Identidad ahora: responsabilidad; estafas con APK a
presión; el actor anónimo reemplaza la app tumbada.
11-may-2026.

Si no cumples: bloqueo en certificados, regiones
aplicables. 3-sep-2025. El 30-sep, «aplicable» =
4 países + 7 tiendas.

Hobby: limitada, 20 dispositivos, sin ID. 25-mar-2026.

Limitada → completa: sí. Al revés: no. 8-jun-2026.

ADB sin registro: sí. Sin espera de 24 h. 3-sep-2025
y 23-mar-2026.

Empresa / EMM: tienda de la org en gestionados, no
hace falta; Google recomienda registrar. 3-sep-2025.

Sancionados: fuera de las comprobaciones. 25-mar-2026.

Android 7+, certificados, Play services. 23-mar-2026.
No es Android 8+.

¿Se cierra Android? Google: no. Flujo avanzado
ago-2026. 18-jun-2026.

Tienda fuera de la lista / sideload el 30-sep:
aún no. Prepárate para 2027. 15-jul-2026 y 18-jun-2026.

Formatos el 30-sep: Play, todos si estás en Play;
fuera de Play, móvil y tablet en las regiones.
15-jul-2026.

25 USD: Full Distribution ADC, como Play; limitada
exenta. 25-mar-2026.

Sin ID: limitada. Sigue pidiendo perfil de pagos.
18-jun-2026.

Play + otros canales: Play Console único sitio.
Play App Signing: reclamo automático. 3-sep-2025.

Clave perdida: no registras. 23-mar-2026.

Flujo avanzado: de una vez, no 24 h por APK.
Developer Mode no hace falta dejarlo. No hay ADB
para saltar la espera «at this point». Sin flujo
y sin ADB, no instalas ni actualizas no registradas.
[Fuente — FAQ]
```

---

## 🔧 Android Developer Console

Guía 4-sep-2026. [Fuente] Solo fuera de Play. Alta con cuenta Google. Packages: nombre + SHA-256 → In review → APK firmado con snippet en assets → Registered y email. Status API (¿el nombre está cogido?) y Console API (registrar claves). OAuth para que una tienda de terceros actúe por ti. Duplicados: mayoría (>50 % installs conocidos); si nadie llega, cluster ≥50; si nadie llega a 50, first-come. [Fuente] Consola no se abrió con sesión. Detalle y ejemplos didácticos = WhatsApp.

---

## 🎓 Distribución limitada

Guía 20-ago-2026. [Fuente] Gratis. 20 dispositivos. Handshake QR/enlace. Sin ID gubernamental. Sí pide: cuenta Google, 2FA, perfil de pagos (nombre legal y dirección), correo de contacto no público. Perfiles: hobby, aprendiz, aula. La propia guía limited habla del 30-sep como fecha en la que los paquetes no registrados dejan de instalarse en los cuatro países; el FAQ (15-jul-2026) acota ese día a las tiendas participantes. No unifico las dos frases de Google. [Fuente / Observación]

---

## 📜 Carta abierta (24-feb-2026)

[https://keepandroidopen.org/open-letter](https://keepandroidopen.org/open-letter), abierta hoy. Campaña, no Google. [Fuente] A Pichai, Brin, Page y Vijaya Kaza. 71 orgs / 23 países. Seis preocupaciones: gatekeeping fuera de Play; barreras FOSS, sanctioned, humanitarias, academia; base de datos de devs; enforcement opaco; asimetría competitiva; reguladores (CE, DoJ). Piden rescindir el requisito para terceros, diálogo y neutralidad. Medidas que dan por suficientes: sandbox, permisos, avisos de sideload, Play Protect, certificados de firma. [Fuente] La Bandita informa, no ordena. Texto largo = WhatsApp.

---

## 📣 Keep Android Open (campaña)

«Your phone is about to stop being yours». 110 days, al corte. Starting 2027. Nueve pasos. Play Services, no el OS. «Do not sign up» es consigna de la campaña, no instrucción de esta guía. Petición change.org (>100.000, dice ella; no se recontó). tips@[https://keepandroidopen.org](https://keepandroidopen.org). Prensa que cita la portada: Ars Technica, 9to5Google, The Register, etc. — [Reporte externo], páginas no reabiertas. [Fuente — campaña] FAQ de KAO: septiembre no incluye F-Droid; fecha de impacto a F-Droid no publicada. [Fuente]

---

## 📗 F-Droid, 29-sep-2025

Quince años de repo FOSS. El decreto (tasa, términos, ID, enumerar application IDs) es amenaza existencial: no pueden exigir registro a autores ajenos ni «tomar» identificadores. Play Protect ya existe. Lo llaman consolidar poder. Right to Run. Piden escribir a Parlamento, Congreso, equipo DMA. [Fuente] No se usa un corte «febrero 2026».

---

## 🏛️ Firmantes visibles

KAO dice 71 / 23 países. [Fuente] Vistos en carta 01–17: AdGuard, App Fair, April, ARTICLE 19, ANSOL, Aurora Store, BEUC, Brave, Calyx, D64, CCC, Codeberg, CryptPad, Cryptee, Data Rights, Digitale Gesellschaft, Digital Rights Foundation. En portada, además: Tor, FUTO, F-Droid, GrapheneOS Foundation, microG, Obtainium, IzzyOnDroid, KDE, FSF, Nextcloud, Vivaldi, Fundación Karisma, y otros. No es 71/71 auditado. Lista larga = WhatsApp. Aparecer aquí no es recomendación de instalar.

---

## 📌 Correcciones al corte 28-jul-2026

```
Viejo: 30-sep = bloqueo de APKs.
Hoy:   30-sep = 4 países + 7 tiendas. Sideload aún no.

Viejo: Android 8+.
Hoy:   Android 7+.

Viejo: 6 tiendas.
Hoy:   7.

Viejo: anuncio noviembre 2025.
Hoy:   agosto 2025.

Viejo: F-Droid febrero 2026.
Hoy:   blog 29-sep-2025. KAO: F-Droid fuera de sep.

Viejo: 24 h por cada APK.
Hoy:   flujo de una vez.

Viejo: EMM hasta sep-2027.
Hoy:   no salió en páginas abiertas. Fuera.

Viejo: LineageOS no te afecta (afirmado).
Hoy:   Google dice certified devices. No se probó.

Viejo: 50× malware como hecho.
Hoy:   no en hub/FAQ. Fuera como cifra nuestra.

Viejo: tablas Markdown / anclas #1-resumen.
Hoy:   bloques de texto. Mapa + comentario fijado.

Viejo: limited = sin ID, y se acabó.
Hoy:   sin ID, con perfil de pagos, 2FA, cuenta Google.
```

---

## 🌍 República Dominicana y LATAM

Brasil sí es piloto el 30-sep. RD no. México, Colombia, Argentina, Chile, Perú, el Caribe: no aparecen en el hub como piloto. [Observación] Eso no salva 2027. Si viajas a BR/ID/SG/TH con un certificado y Play services, el hito de esas tiendas puede aplicarte allí. No se probó. [No confirmado] Fundación Karisma (Colombia) está en la parrilla de KAO. [Observación] No se abrió su sitio.

---

## 🔗 Relación con las otras guías de la banda

La guía de tiendas APK no se anula el 30-sep. F-Droid no está en las siete. Obtainium sigue siendo puente a GitHub, no aval de LiteAPKs. Kototoro (GitHub Releases) es sideload / canal propio: el 30-sep, según FAQ, aún no le aplica el bloqueo de vía normal. 2027 es la frase a releer. El desarrollador decide si se registra; esta guía no se lo ordena. Keep Android Open pide no apuntarse; se informa, no se convierte en regla de la banda. Discord no es receptor.

---

## ⚖️ El debate, con fuentes

Sin partido. Tres voces abiertas hoy, más la prensa que la campaña cita y que aquí no se reabrió.

**Google.** Identidad = responsabilidad. Estafas con APK en llamada. El sideload sigue, con salvaguardas. 99 % de Play ya registrado. Android no se cierra. Limited distribution para hobby. ADB igual. Flujo avanzado de una vez. 2027 = todas las apps en certificados. [Fuente — hub / FAQ / guides]

**F-Droid** (blog 29-sep-2025): el decreto es amenaza existencial; no pueden tomar los IDs de apps ajenas ni exigir cédula a cada autor FOSS; Play Protect ya existe; Play ha hospedado malware; lo llaman control, no seguridad; el derecho a ejecutar software en tu aparato. [Fuente]

**Keep Android Open.** Campaña. FAQ de hoy: septiembre ya no tumba F-Droid; la fecha que sí lo haría no está publicada. Portada: 2027, 110 días, flujo de nueve pasos, «Do not sign up», 71 orgs / 23 países, carta del 24-feb-2026. [Fuente]

La cifra «50 veces más malware en sideload que en Play» es el argumento que medios atribuyen a Google (p. ej. 9to5Google, 25-ago-2025). **No** estaba en el FAQ ni en el hub leídos hoy. Queda como [Reporte externo], no como dato medido por nosotros. No se recita como hecho.

Investigaciones de competencia en Brasil / EE. UU. / Europa: el borrador viejo las daba por en curso. No se abrió ningún expediente hoy. [No confirmado] Se omiten como hecho. La carta abierta las nombra como contexto; eso no prueba un caso abierto.

EFF, ACLU, Cory Doctorow, Ars Technica, The Register, Malwarebytes, TechCrunch: salen como citas de KAO o de F-Droid. Sus páginas no se reabrieron hoy. [Reporte externo / No confirmado el texto]

«Android Developer Verifier» como nombre de producto: prensa, no hub. [Observación]

Tres lecturas que esta guía no mezcla:

```
1. Google describe un programa de identidad + registro
   de paquetes, con un hito regional el 30-sep y un
   salto global en 2027, más un flujo avanzado y ADB.
2. F-Droid describe un decreto que, si se aplica a su
   modelo, acaba el proyecto tal como es.
3. Keep Android Open describe un lockdown mundial en
   2027 y pide no apuntarse.
```

Las tres están fechadas. Ninguna se «gana» por gritar más. Si un anuncio oficial mueve una fecha, gana el anuncio.

---

## 🚧 Límites de este texto

- No se ejecutó el flujo avanzado en un teléfono.
- No se instaló ningún APK para comprobar el bloqueo.
- No se inició sesión en ADC ni en Play Console.
- No se pagaron 25 USD ni se creó un perfil de pagos.
- No se reprodujo el handshake QR de limited distribution.
- Los blogs de [https://android-developers.googleblog.com](https://android-developers.googleblog.com) no se
  pudieron leer (ERR_BLOCKED_BY_CLIENT). Solo se usa lo
  que el hub enlaza y lo que sí cargó en
  [https://developer.android.com](https://developer.android.com).
- Los Shorts y el vídeo de YouTube del hub no se vieron.
- Help Center de ADC y de Play Console: no abiertos.
- policies.google.com/privacy: no abierta.
- android.com/certified/partners/: no reabierta.
- Chunks 3–9 de la carta abierta: no se numeró 18–71.
- change.org: no se recontaron firmas.
- Encuesta de Google: no se abrió.
- FreeDroidWarn: repo no abierto hoy.
- [https://keepandroidopen.org/cta/](https://keepandroidopen.org/cta/): no abierta.
- Páginas de EFF, ACLU, Doctorow, Ars, Register,
  Malwarebytes, TechCrunch: no reabiertas.
- Guía full-distribution de Google: no abierta como
  página aparte.
- Segundo chunk de la guía ADC: no se volvió a pedir;
  las reglas de duplicados se cortaron a mitad.
- República Dominicana no está en los cuatro países;
  eso no «salva» el 2027.
- Calendario 2027 sin mes: no se inventa.
- No se afirma que LineageOS, GrapheneOS o /e/ «queden
  fuera» o «dentro». Google dice certified devices.
- «50× malware» no se usa como cifra nuestra.
- Esta guía no es un envío. BORRADOR. Firma humana
  pendiente.

---

## ✅ Acciones concretas

**Si solo usas Play y no vives en BR/ID/SG/TH.** Nada urgente el 30-sep. Relee el hub en 2027 o si Google mueve el mapa.

**Si sideloadeas.** El 30-sep no es, hoy, el día de F-Droid. Sigue siendo buen momento para: F-Droid u Obtainium desde la fuente, anotar firmas, no portales de mods. Eso es la otra guía de la banda, no esta.

**Si desarrollas.** [https://developer.android.com/developer-verification](https://developer.android.com/developer-verification) — elige Play Console o Android Developer Console. Si eres hobby, lee la guía de limited distribution (actualizada 20-ago-2026): 20 dispositivos, sin ID, con perfil de pagos. Keep Android Open pide no apuntarte; eso es la campaña, no una orden de esta guía. La decisión es tuya, con la página de Google abierta el día que la tomes.

**Si gestionas flota.** FAQ de empresa: canal gestionado exceptuado; registra igual por si el APK sale del corral.

**Si escribes a un regulador.** F-Droid y KAO publican vías. Esta guía no redacta la carta.

**Si te llega un video de TikTok el 30-sep diciendo «se acabó Android».** El 30-sep es 4 países + 7 tiendas. Reabre el hub. No instales un «bypass» de un portal de mods.

No hace falta «instalar todo ahora por si cierran». El atajo sucio no se vuelve más justificable.

Procedimiento corto, si de verdad te toca registrar (desarrollador, no usuario de Play):

1. Reabre [https://developer.android.com/developer-verification](https://developer.android.com/developer-verification)
   el día que actúes, no este post.
2. ¿Estás en Play? Play Console. ¿Solo fuera?
   Android Developer Console.
3. ¿Hobby / aula / 20 dispositivos? Limited
   distribution. Cuenta Google + 2FA + perfil de
   pagos. Sin ID. Sin 25 USD.
4. ¿Org? D-U-N-S (hasta 28 días). No lo dejes para
   el 29-sep.
5. Nombre de paquete + SHA-256 + APK de reto.
6. Si la clave se perdió, Google dice que no
   registras. No hay «recuperar» en la FAQ.
7. ADB sigue. No es un atajo para usuarios finales
   en masa.

Procedimiento corto, si eres usuario en RD:

```
1. El 30-sep no eres piloto.
2. F-Droid / Obtainium / GitHub Releases: según
   Google, aún no les aplica ese día.
3. 2027 existe como frase. Sin mes. Reabre.
4. No bajes un «parche» de Telegram.
```

---

## 📚 Fuentes abiertas el 2026-09-13

[https://developer.android.com/developer-verification](https://developer.android.com/developer-verification)
  Hub. «Next milestone: September 30, 2026».
  Android 7+. 7 tiendas. 99 % Play. Limited
  «now available». Enlaces a blogs no leídos.

[https://developer.android.com/developer-verification/guides](https://developer.android.com/developer-verification/guides)
  Last updated 2026-08-18. Cuatro países, siete
  tiendas con fabricante, tres caminos, hitos.

[https://developer.android.com/developer-verification/guides/faq](https://developer.android.com/developer-verification/guides/faq)
  Last updated 2026-08-27. Sideload 30-sep aún no.
  25 USD. ADB. Android 7+. Flujo avanzado. D-U-N-S.
  Países sancionados. NDA. APIs.

[https://developer.android.com/developer-verification/guides/limited-distribution](https://developer.android.com/developer-verification/guides/limited-distribution)
  Last updated 2026-08-20. 20 dispositivos. Sin ID.
  Perfil de pagos. 2FA. Gratis. Handshake QR/enlace.

[https://developer.android.com/developer-verification/guides/android-developer-console](https://developer.android.com/developer-verification/guides/android-developer-console)
  Last updated 2026-09-04. Packages, SHA-256, APK
  de reto, Status API, Console API, OAuth,
  duplicados (majority / sizeable / first-come).

[https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html](https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html)
  Amenaza existencial. Anti-features. Reproducibles.
  Play Protect. Right to Run. Reguladores.

[https://keepandroidopen.org/](https://keepandroidopen.org/)
  Portada. 110 días. Starting 2027. Nueve pasos.
  Do not sign up. 71 / 23. Prensa citada.

[https://keepandroidopen.org/faq/](https://keepandroidopen.org/faq/)
  Septiembre no incluye F-Droid. Fecha de impacto
  a F-Droid: no publicada.

[https://keepandroidopen.org/open-letter/](https://keepandroidopen.org/open-letter/)
  24-feb-2026. Seis preocupaciones. Petición.
  Firmantes 01–17 vistos en esta pasada.

Blogs de Google enlazados por el hub (texto no leído hoy, fetch bloqueado):

[https://android-developers.googleblog.com/2026/06/android-developer-verification.html](https://android-developers.googleblog.com/2026/06/android-developer-verification.html)
[https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html](https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html)
[https://android-developers.googleblog.com/2026/03/android-developer-verification.html](https://android-developers.googleblog.com/2026/03/android-developer-verification.html)

Vídeos del hub (no vistos):

[https://youtube.com/shorts/WcPElxbOeXY](https://youtube.com/shorts/WcPElxbOeXY)
[https://youtube.com/watch?v=A7DEhW-mjdc](https://youtube.com/watch?v=A7DEhW-mjdc)

Consolas (sin sesión hoy):

[https://android.google.com/developerconsole](https://android.google.com/developerconsole)
[https://play.google.com/console/signup](https://play.google.com/console/signup)

---

**Cierre.** El 30 de septiembre de 2026 es fecha real, para cuatro países y siete tiendas, en certificados Android 7+. No es la muerte del sideload ni de F-Droid ese día. 2027 es el salto que Google nombra para «all apps on certified devices», sin mes. Keep Android Open y F-Droid siguen en alerta; no las contradice el hito de septiembre, las desplaza. La carta del 24-feb-2026 pide rescindir el requisito para terceros; eso es la campaña, no una sentencia. Quien tenga que registrarse, que lo haga leyendo la página de Google el día que lo haga, no este post. Quien decida no registrarse, que sepa qué dice Google que pasa en certificados cuando el requisito le aplique, y qué dice la campaña que haga.

Si un anuncio oficial mueve una fecha, gana el anuncio. Este texto se actualiza con lo verificado, no con el miedo.

> La Bandita informa a partir de fuentes fechadas.

#Android #DeveloperVerification #FDroid #Sideload #LaBandita #Septiembre2026

---
COMENTARIO FIJADO — no forma parte del post. Primer comentario, fijar.

Android Developer Verification — La Bandita
Fecha: 2026-09-13
Versión de esta publicación: BORRADOR 2026-09-13 (sustituye el corte 2026-07-28)

Índice (el mismo icono abre cada bloque)

⚡ ¿Te toca el 30 de septiembre?
📅 Cronograma
🪪 Qué es la verificación
📱 Cómo opera
🏪 Tiendas del 30-sep
↔️ Qué no cambia / 2027
🛠️ Flujo avanzado y ADB
👤 Por perfil
❓ FAQ de Google
🔧 Android Developer Console
🎓 Distribución limitada
📜 Carta abierta (24-feb-2026)
📣 Keep Android Open
📗 F-Droid, 29-sep-2025
🏛️ Firmantes visibles
📌 Correcciones al corte 28-jul
🌍 RD y LATAM
🔗 Otras guías de la banda
⚖️ Debate
🚧 Límites
✅ Acciones
📚 Fuentes

Corrección central: el 30-sep-2026 es 4 países + 7 tiendas, no el cierre mundial del sideload. F-Droid no está en esa lista. 2027 = «all apps» en certificados, sin mes.

Lista completa = WhatsApp de La Bandita.
