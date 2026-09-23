# Publicación — Android Developer Verification (La Bandita) · 2026-09-13
> BORRADOR · WhatsApp / La Bandita · no Discord. No Facebook (límite ~40k).
> POST: un solo mensaje. Copia desde ANDROID DEVELOPER VERIFICATION hasta el cierre.
> Pedido de esta pieza: WhatsApp fijo 63.000 caracteres, ni más ni menos.
> No publicar sin firma humana.
> Corte vivo: 2026-09-13.

ANDROID DEVELOPER VERIFICATION · La Bandita · 2026-09-13 (BORRADOR · firma humana pendiente)
**Tiempo estimado de lectura: 50–65 min**
**Índice:** mapa de arriba + el mismo icono en cada título. Resumen en el comentario fijado.

# Android Developer Verification: cronograma, mecanismo e implicaciones (corte 2026-09-13)

**Corte de información:** 2026-09-13
**Clase predominante:** [Fuente] (Google) y [Observación] de páginas abiertas hoy. Sin prueba en un teléfono.
**Grado:** V2 parcial — hub, guías, FAQ, ADC (4-sep-2026) y limited-distribution de developer.android.com abiertos hoy; F-Droid (29-sep-2025) y Keep Android Open (portada, FAQ, carta abierta 24-feb-2026) reabiertos hoy. Blogs de android-developers.googleblog.com: fetch bloqueado (ERR_BLOCKED_BY_CLIENT); se citan como enlaces del hub, no como texto leído.
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
Índice corto: primer comentario (fijado).

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

> La Bandita informa a partir de fuentes fechadas. Si vas a registrarte o a cambiar de ROM, reabre developer.android.com/developer-verification el día que actúes.

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

Keep Android Open, en su FAQ de hoy, dice lo mismo sobre septiembre: el despliegue inicial se limitó a una lista de tiendas que no incluye F-Droid; «the date at which the lockdown will start impacting F-Droid users is not yet published». [Fuente — keepandroidopen.org/faq/] Su portada sigue hablando de 2027 y de una cuenta atrás. No unifico portada de campaña, FAQ de campaña y hub de Google: cada una dice lo suyo.

---

## 📅 Cronograma (lo que Google publica hoy)

Anuncio inicial: agosto 2025 (no «noviembre 2025»). F-Droid lo trató el 29-sep-2025. [Fuente / Observación] Keep Android Open, en portada, también sitúa el anuncio en agosto 2025 y enlaza el hub de developer.android.com. [Fuente — portada]

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
                             Guía: play.google.com/console/signup

Android Developer Console    Si distribuyes solo fuera de Play.
                             android.google.com/developerconsole
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

El nombre «Android Developer Verifier» circula en prensa. En las páginas de developer.android.com abiertas hoy, Google habla de «protections» y de Play services, no se copió ese nombre de producto. [Observación] No se afirma aquí como nombre oficial leído.

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

FAQ last updated 2026-08-27 UTC. [Fuente] Parafraseo en español. Las fechas «Last updated» de cada ítem son las que Google pone al pie de esa respuesta, no la fecha de esta guía.

**¿Por qué la identidad ahora?** Identidad = responsabilidad. Conecta apps con sus autores. Dificulta que un actor malicioso, cuando le tumban una app, saque otra anónima al día siguiente. Google habla de estafas agresivas: presión para instalar un APK que luego vacía cuentas. Los sistemas automáticos pillan muchas amenazas; el ciclo anónimo las reemplaza. Los usuarios, dice Google, se sienten más seguros si saben que hay una persona u organización verificada detrás. Last updated 11-may-2026. [Fuente]

**¿Qué pasa si no cumplo?** Si no verificas identidad y no registras las apps para el plazo de septiembre, se bloquea la instalación en dispositivos certificados, en las regiones aplicables. Last updated 3-sep-2025. [Fuente] «Regiones aplicables» el 30-sep, leído con el hub: BR, ID, SG, TH y las siete tiendas. No es el planeta entero ese día.

**Soy hobby / estudiante. ¿Qué es limited distribution?** Cuenta gratis para profesores, estudiantes y aficionados: hasta 20 dispositivos, sin ID gubernamental. Last updated 25-mar-2026. [Fuente]

**¿Puedo pasar de limitada a completa, o al revés?** Limitada → completa: sí. Completa → limitada: no. Motivo que da Google: no dejar en mala experiencia a usuarios de apps que ya estaban en distribución amplia. Last updated 8-jun-2026. [Fuente]

**¿ADB instala sin registro?** Sí. Pensado para desarrollar y probar lo que aún no va al público. Last updated 3-sep-2025. [Fuente]

**¿Las apps de empresa tienen que verificarse?** Las que salen por la tienda de la organización, en dispositivos gestionados, no. Google recomienda registrarlas igual por si se bajan de otro sitio o van a un aparato no gestionado. Last updated 3-sep-2025. [Fuente]

**¿Si quiero modificar o «hackear» un APK y ponerlo en mi aparato, tengo que verificarme?** Apps instaladas por ADB no requieren verificación. Last updated 11-sep-2025. [Fuente]

**¿Y los desarrolladores en países sancionados?** Quedan fuera de las comprobaciones. Pueden seguir distribuyendo ahí sin verificación; los usuarios de esas regiones, dice Google, no reciben los «enhanced security benefits». Last updated 25-mar-2026. [Fuente]

**¿En qué versiones de Android?** Dispositivos certificados con Android 7 o superior. Las actualizaciones llegan por Google Play services. Last updated 23-mar-2026. [Fuente] El corte viejo decía Android 8+. Eso está mal.

**¿Android se cierra?** Google: no. Sigue habiendo varios canales. La mayoría de usuarios no notará cambio. Power users: flujo avanzado de una vez, anunciado para agosto 2026. Last updated 18-jun-2026. [Fuente]

**¿Y si distribuyo por una tienda que no está en la lista de septiembre?** El requisito no se aplica en esa fase inicial. El 30-sep se limita a las tiendas nombradas. Google pide igual que te prepares para 2027. Last updated 18-jun-2026. [Fuente]

**¿Y el sideload el 30-sep, o una tienda que no participa?** El plazo del 30-sep solo aplica a las participating stores. Sideload directo y otras tiendas: aún no. La experiencia de instalación no cambia en septiembre, dice Google; pide planificar el registro antes del despliegue global de 2027. Last updated 15-jul-2026. [Fuente] Esta es la corrección central de esta guía.

**¿Qué formatos entran el 30-sep?** Si publicas en Play, todos los formatos deben estar registrados. Fuera de Play, recomienda registrar todos para el futuro; la aplicación del 30-sep es móvil y tablet, en las regiones seleccionadas. Last updated 15-jul-2026. [Fuente]

**¿Qué es un D-U-N-S y cómo lo saco?** Identificador de nueve dígitos de Dun & Bradstreet, obligatorio si te registras como organización. Gratis en dnb.com. Hasta 28 días. Last updated 3-sep-2025. [Fuente]

**¿Cómo tratan mis datos personales?** Para verificar identidad, según la política de privacidad de Google. Last updated 3-sep-2025. [Fuente] No se abre hoy policies.google.com/privacy. [No confirmado el texto de esa política]

**¿Y si quiero seguir anónimo?** Google dice que equilibra privacidad con seguridad. Quien no quiera verificarse: cuenta limitada (sin ID) o distribuir no registrada a usuarios con flujo avanzado. Last updated 18-jun-2026. [Fuente]

**¿Por qué 25 USD en ADC? ¿Cómo se paga?** La tasa de la cuenta Full Distribution cubre costes administrativos e inversión en el ecosistema, «similar to Play's $25 registration fee». Google dice que trabaja en varias formas de pago. Limited distribution: tasa exenta. Last updated 25-mar-2026. [Fuente] No se pagó nada aquí.

**¿Y si no puedo dar un ID gubernamental?** Limited distribution (agosto, dice esa respuesta): hasta 20 dispositivos, gratis, sin verificación de ID. Last updated 18-jun-2026. [Fuente]

**Distribuyo en Play y en otros canales.** Play Console es el sitio único para gestionar la verificación, también de lo que saques fuera. Last updated 3-sep-2025. [Fuente]

**Uso Play App Signing. ¿Se reclaman solas?** Sí: Google dice que tiene lo necesario y que las elegibles entran en el registro automático. Last updated 3-sep-2025. [Fuente]

**¿Puedo recuperar una clave de firma perdida?** Si la pierdes, no puedes registrar los paquetes. Google recomienda un sistema seguro de gestión de claves. Last updated 23-mar-2026. [Fuente]

**¿Varias claves de firma?** ADC permite añadir y verificar varias claves para un mismo paquete. Last updated 23-mar-2026. [Fuente]

**¿Registrar sin clave elegible?** Si el nombre de paquete ya está en uso, te pueden decir que tu clave no es elegible para reclamarlo de golpe. Google sugiere otro nombre de paquete; si no es posible, puedes pedir registro con revisión extra, y ese nombre podría usarlo también otro desarrollador. Last updated 19-mar-2026. [Fuente]

**¿Dónde miro el estado del registro?**

```
Play Console     Página de Android developer verification;
                 el estado al lado de cada app.
ADC              Pestaña Package names: Registered /
                 Not registered / Draft.
Android Studio   Al generar un App Bundle o APK firmado
                 (Panda 4+).
[Fuente — FAQ, 18-jun-2026]
```

**¿APIs para CI/CD?** Sí: pensadas para registro masivo o desde pipelines. Last updated 18-jun-2026. [Fuente]

**Status API vs Console API.** Status: ¿el nombre está cogido? ¿eres elegible? Console: registrar nombres y gestionar claves. Last updated 18-jun-2026. [Fuente]

**¿Los usuarios pueden sideloadear apps de no verificados?** Sí, con el flujo avanzado de una vez. Last updated (bloque Advanced flow). [Fuente]

**¿Las 24 h para qué?** Contra coaching / coerción, dice Google. Last updated 11-may-2026. [Fuente]

**¿ADB y las 24 h?** ADB instala como siempre. La espera no aplica a ADB. Last updated 23-mar-2026. [Fuente]

**¿Dejar Developer Mode encendido?** No. Una vez activas el flujo, está activado. Last updated 23-mar-2026. [Fuente]

**¿Hay un comando ADB para saltarse las 24 h?** No, «at this point». Lo considerarán en versiones futuras. Last updated 25-mar-2026. [Fuente]

**¿Actualizar no registradas con el flujo apagado?** No, salvo ADB. Last updated 25-mar-2026. [Fuente]

**¿Actualizar las no registradas que ya tengo, sin flujo y sin ADB?** No. Last updated 25-mar-2026. [Fuente]

**¿Registrar viola un NDA?** Google: no. No recoge contenido ni propósito de la app. Last updated 25-mar-2026. [Fuente]

**¿Dónde pido ayuda?** Android Developer Console Help Center y Play Console Help Center. [Fuente] Esas páginas de soporte no se abrieron hoy. [No confirmado el texto de ayuda]

Esta FAQ es de Google. Keep Android Open tiene la suya, de un solo ítem hoy: por qué la fecha «cambió» de septiembre 2026 a enero 2027. La respuesta de KAO: el cierre de septiembre se limitó a una lista de tiendas que no incluye F-Droid; la fecha que sí impactaría a usuarios de F-Droid no está publicada. [Fuente — keepandroidopen.org/faq/] «Enero 2027» aparece en el título de esa pregunta de KAO; Google, en el hub, no pone mes de 2027. No unifico esas dos frases.

---

## 🔧 Android Developer Console

Guía last updated 2026-09-04. [Fuente / Observación] Si solo distribuyes fuera de Play. Si también estás en Play, Google te manda a Play Console.

**Alta.** Con cuenta Google, en android.google.com/developerconsole/developers. Estudiante o hobby: tipo de cuenta con menos requisitos y sin tasa. [Fuente]

**Elegir cómo distribuyes.** Google recuerda que el sideload sigue; la experiencia del usuario depende del camino. [Fuente]

**Identidad.** Requisitos distintos según el tipo. Google apunta a las guías de full distribution y limited distribution. La de full distribution no se abrió hoy como página aparte; se usa FAQ + esta guía. [No confirmado el detalle extra de full-distribution]

**Registrar paquetes.** Una vez verificado, pestaña Packages:

```
1. Escribes el nombre de paquete.
2. Añades la huella SHA-256 de la clave de firma.
   El estado pasa a In review.
3. Pruebas la propiedad: firmas un APK con tu clave
   privada y lo subes. ADC te da un snippet para
   meterlo en la carpeta assets del APK.
   Cuando queda Registered, llega un email y el
   estado cambia.
[Fuente — ADC, 4-sep-2026]
```

**Automatizar.**

```
Android Developer ID Status API
  ¿El nombre ya está registrado? ¿Eres elegible?

Android Developer Console API
  Registrar y gestionar nombres y claves desde
  el entorno o un pipeline CI/CD.

OAuth delegation
  Una plataforma de terceros (tienda alternativa)
  puede hacer esas operaciones por ti.
[Fuente]
```

**Nombres de paquete duplicados.** Si varios desarrolladores usan el mismo nombre, Google describe reglas para asignarlo al que tenga la clave con más de la mitad de las instalaciones conocidas:

```
Majority cluster
  Si las claves de un desarrollador cubren más del
  50 % de las instalaciones conocidas: prioridad.

Sizeable cluster
  Si nadie llega al 50 %, un grupo con al menos
  50 instalaciones.

First-come
  Si nadie llega a 50 instalaciones, el primero
  que reclame.
[Fuente — ADC]
```

Los ejemplos com.test.1 / com.test.2 / com.test.3 son didácticos de Google, no paquetes reales auditados aquí.

**Review.** La guía tiene un apartado Review; el fetch del primer chunk se cortó en las reglas de duplicados. El segundo chunk no se volvió a pedir en esta pasada. No se inventa el resto. [No confirmado el cierre de esa guía]

Consola: android.google.com/developerconsole. No se inició sesión hoy. [Observación]

---

## 🎓 Distribución limitada

Guía last updated 2026-08-20. [Fuente] Google: «keeping Android an open platform for you to learn, experiment, and build for fun». Si no distribuyes en amplio, hay un tipo de cuenta para ti.

**Fechas que publica esa guía:**

```
Agosto 2026     Cuentas limitadas disponibles para todos.
                Registrar paquetes y autorizar dispositivos
                lleva tiempo; Google pide no dejarlo para
                el 30-sep.

30 sep 2026     Las protecciones entran. Los nombres de
                paquete no registrados dejan de ser
                instalables en certificados, en Brasil,
                Indonesia, Singapur y Tailandia.
[Fuente — limited-distribution]
```

Ojo: esa frase de la guía limited habla del 30-sep como si los paquetes no registrados dejaran de instalarse en esos cuatro países. El FAQ (15-jul-2026) acota el 30-sep a las tiendas participantes y dice que el sideload aún no entra. [Fuente] No unifico las dos frases de Google: las dejo las dos, fechadas. Quien actúe, que reabra las dos páginas.

**Qué puede hacer la cuenta.** 1) Registrar apps. 2) Compartirlas con hasta 20 dispositivos que el usuario final haya autorizado. [Fuente]

**Coste.** Gratis. [Fuente] La FAQ de 25 USD no aplica aquí.

**Cómo se comparte.** Handshake: QR o enlace, consentimiento en el aparato, registro en ADC. [Fuente] No se reprodujo.

**¿Es para ti?** Google lista tres perfiles (sin tabla):

```
Hobby            Compartir con familia y amigos, o uso
                 personal. Sin intención comercial.

Aprendiz         Experimentar, portafolio, prototipos
                 en aparatos propios, compartir con pares.

Aula             Compartir con compañeros y profesores.
                 Proyectos de curso.
[Fuente]
```

**Qué pide el alta, aunque no pida cédula:**

```
- Cuenta Google (cualquier tipo de cuenta ADC la pide).
- Verificación en 2 pasos, obligatoria.
- Perfil de pagos de Google: nombre legal y dirección.
  La guía dice que limited usa el perfil de pagos para
  eso, no para cobrarte.
- Correo de contacto: solo para que Google te escriba;
  no se muestra en público.
- No hace falta ID gubernamental.
[Fuente]
```

El corte viejo decía «sin ID» y se quedaba ahí. Completo: sin ID, con perfil de pagos. [Observación]

---

## 📜 Carta abierta (24-feb-2026)

Texto de keepandroidopen.org/open-letter, abierto hoy. Es la campaña, no Google. [Fuente]

```
Fecha: 24 de febrero de 2026
Para: Sundar Pichai (CEO), Sergey Brin, Larry Page,
      Vijaya Kaza (GM App & Ecosystem Trust)
Copia: reguladores, policymakers, comunidad de
      desarrolladores Android
Asunto: registro obligatorio de desarrolladores para
        distribuir apps Android
[Fuente — carta]
```

Las organizaciones firmantes —sociedad civil, no lucrativas, empresas de tecnología— se oponen a la política anunciada: registrarse de forma central con Google para distribuir fuera de Play, con efecto mundial «in the coming months» (frase de la carta; el hub de hoy habla de 2027 para el salto global). [Fuente] Reconocen la seguridad de la plataforma. Dicen que Android ya tiene mecanismos que no piden registro central. Inyectar un modelo «alien» contrario a la naturaleza abierta de Android amenaza innovación, competencia, privacidad y libertad del usuario. Piden retirar la política y trabajar con las comunidades de código abierto y de seguridad en alternativas menos restrictivas. [Fuente]

Seis bloques de preocupación, parafraseados. No es cita literal larga.

**1. Gatekeeping más allá de la tienda de Google.** Android se caracterizó como plataforma abierta, independiente de los servicios de Google. La política, dicen, obliga a quien distribuye por web propia, tienda de terceros, empresa o pase directo a pedir permiso a Google: términos, tasa, ID gubernamental. Extiende el porteraje a canales donde Google no tiene rol operativo. Quien no usa servicios de Google no debería tener que registrarse ni someterse a su juicio. Centralizar el registro mundial da a Google poder de apagar una app, por cualquier motivo, en todo el ecosistema certificado. [Fuente — carta]

**2. Barreras a la entrada y a la innovación.** Fricción, en particular para: individuales y equipos pequeños; proyectos FOSS de voluntarios; regiones con poco acceso a la infraestructura de registro; quien evita ecosistemas de vigilancia; emergencias humanitarias; activistas de libertad de internet en países que criminalizan ese trabajo; desarrolladores en países o regiones donde Google no les deja apuntarse por sanciones; academia y apps experimentales; apps internas de empresa o gobierno que nunca iban a un catálogo público. Cada trámite extra reduce diversidad y concentra poder en quien puede absorber el coste. [Fuente — carta]

**3. Privacidad y vigilancia.** Una base de datos de todos los desarrolladores Android, usen o no Google. Preguntas que plantea la carta: qué datos hay que dar; cómo se guardan, aseguran y usan; si pueden pedirse por gobiernos o procesos legales; hasta qué punto se rastrea la actividad del desarrollador; qué implica para quien trabaja en apps de privacidad o políticamente sensibles. Derecho a crear y distribuir sin vigilancia innecesaria. [Fuente — carta]

**4. Enforcement arbitrario y cuentas.** Los procesos de revisión de Google, dicen, ya se critican por opacidad, inconsistencia y apelación limitada. Extenderlos a todos los certificados crea riesgos de: rechazo o suspensión sin justificación clara; sistemas automáticos con poca supervisión humana; perder todos los canales por una sola decisión corporativa no revisable; consideraciones políticas o competitivas; impacto desproporcionado en comunidades marginadas y en apps controvertidas pero legales. Un único punto de fallo, una sola corporación, es contrario a un ecosistema sano. [Fuente — carta]

**5. Implicaciones anticompetitivas.** Inteligencia sobre toda la actividad de desarrollo Android: qué apps, quién, estrategias alternativas, amenazas a los servicios de Google, tendencias fuera de su ecosistema. Asimetría: adelantarse, copiar, socavar. Preguntas de antitrust. [Fuente — carta] Esta guía no abre expedientes. [No confirmado]

**6. Reguladores.** Comisión Europea, Departamento de Justicia de EE. UU. y autoridades de competencia: la carta les nombra como contexto de escrutinio a plataformas dominantes. También anota preocupación inversa: que la intervención regulatoria aumente vigilancia masiva o impida libertad de software, internet abierto y neutralidad del aparato. Piden a Google cumplir obligaciones regulatorias con modelos que respeten la apertura de Android, no con más control de portero. [Fuente — carta]

**Medidas que la carta da por suficientes, sin registro central:**

```
- Seguridad de sistema, sandbox, permisos.
- Avisos al usuario en sideload.
- Google Play Protect (el usuario puede activarlo o no).
- Certificados de firma del desarrollador (procedencia).
[Fuente — carta]
```

Dicen que no se ha presentado evidencia de que esas salvaguardas no basten, como han bastado diecisiete años. Si la preocupación es de verdad seguridad y no control, Google debería mejorar esos mecanismos, no crear cuellos de botella. [Fuente — carta]

**Petición:**

```
1. Rescindir de inmediato el registro obligatorio para
   distribución de terceros.
2. Diálogo transparente con sociedad civil, desarrolladores
   y reguladores sobre mejoras de seguridad que respeten
   apertura y competencia.
3. Neutralidad de plataforma: el rol de Google como
   proveedor no debe chocar con sus intereses comerciales.
[Fuente — carta]
```

Cierre de la carta: Android es infraestructura crítica (gobiernos, empresas, miles de millones). Concentrar el poder de aprobar software en una sola corporación no accountable es contrario a la libertad de expresión, un insulto al software libre, una barrera a la competencia y una amenaza a la soberanía digital. Piden a Google revertir el rumbo y trabajar con la comunidad. [Fuente — carta]

La Bandita informa la carta. No es una orden de no registrarse.

---

## 📣 Keep Android Open (campaña)

Portada keepandroidopen.org, abierta hoy. [Fuente — campaña]

Titular: «Your phone is about to stop being yours.» Cuenta atrás: 110 days until lockdown, al corte. «Starting in 2027» —con asterisco que apunta a su FAQ—. Actualización silenciosa, no consensuada, empujada por Google: bloqueará toda app Android cuyo desarrollador no se haya registrado, no haya firmado el contrato, no haya pagado y no haya entregado ID gubernamental. «Every app and every device, worldwide, with no opt-out.» [Fuente — portada]

Eso es el marco de la campaña. El hub de Google, el mismo día, habla de 30-sep en cuatro países y siete tiendas, y de 2027 para «all apps on certified devices». No unifico. [Observación]

**Qué dice la portada que Google está haciendo.** Anuncio de agosto 2025. A partir de 2027, todo desarrollador Android debe registrarse de forma central con Google antes de que su software se instale en cualquier dispositivo. No solo Play: todas las apps. Incluye las que se pasan entre amigos, F-Droid, hobby. Independientes, iglesias, grupos comunitarios: «frozen out». [Fuente — portada]

Registro, según la portada:

```
- Pagar una tasa a Google.
- Aceptar términos y condiciones.
- Entregar ID gubernamental.
- Evidencia de la clave privada de firma.
- Listar todos los identificadores de aplicación,
  actuales y futuros.
[Fuente — portada]
```

Si el desarrollador no cumple, las apps se bloquean en silencio en todos los Android del mundo. [Fuente — portada] Google, en FAQ, acota regiones, certificados, Play services y el 30-sep a tiendas participantes. Las dos descripciones conviven en esta guía, cada una con su etiqueta.

**A quién dice que duele.**

Tú: compraste Android porque Google dijo que era abierto. Ahora reescribe el trato, en hardware que ya pagaste. [Fuente — portada]

Independientes: la primera app de un adolescente, la herramienta de un voluntario, la beta interna de una empresa. En 2027, ninguna se instala sin el visto bueno de Google. F-Droid lo llama amenaza existencial. Cory Doctorow lo llama «Darth Android» (pluralistic.net/2025/09/01/fulu/ — página no abierta hoy). [Fuente — portada] [No confirmado el texto de Doctorow]

Gobiernos y sociedad civil: Google tiene historial documentado, dice la campaña, de cumplir cuando un régimen pide quitar apps (enlace ACLU, no abierto hoy). El software de las instituciones existiría al gusto de una corporación extranjera. EFF: el porteraje de apps es «an ever-expanding pathway to internet censorship» (deeplink de nov-2025, no reabierto hoy). [Fuente — portada] [Reporte externo / No confirmado el texto de esas páginas]

**Réplicas que la campaña anticipa.**

«Es seguridad.» Play Protect ya escanea malware sin identidad. Un ID no hace el código más seguro: hace al desarrollador identificable y controlable. Autores de malware pueden registrarse; indie y disidentes a menudo no. EFF, otra vez, como cita de la campaña. [Fuente — portada]

«Sigue habiendo sideload con el flujo avanzado.» Nueve pasos, 24 h, opciones de desarrollador, servicio propietario. No es sideload: es un mecanismo de disuasión. Y como corre por Play Services, Google puede apretarlo o matarlo en silencio. [Fuente — portada]

«Solo es un problema si tienes algo que ocultar.» Denunciantes, periodistas, activistas bajo gobiernos autoritarios; personas en situaciones de abuso doméstico. Razones legítimas para no poner la identidad legal en una base de Google. La contribución FOSS anónima es anterior a Google; esta política, dice la campaña, la termina en Android. [Fuente — portada]

«Es lo que hace Apple.» Apple fue jardín cerrado desde el día uno. La gente eligió Android porque era distinto. «Apple también» es una carrera a la baja. Bajo presión regulatoria (DMA de la UE), incluso Apple se ve forzada a abrir; Google va al revés. [Fuente — portada]

«Son 25 dólares y un papeleo.» Quizá si eres un desarrollador en EE. UU. con tarjeta y carnet. Prueba a ser estudiante en África subsahariana, disidente en Myanmar, voluntario de una app de salud comunitaria. El coste no es solo dinero: cedes ID y evidencia de claves a una empresa que, dice la campaña, cumple con demandas gubernamentales de quitar apps y exponer desarrolladores (enlace The Register, no abierto hoy). [Fuente — portada] [Reporte externo]

**Qué pide la campaña. No es una orden de La Bandita.**

Todos: instalar F-Droid; escribir a reguladores (keepandroidopen.org/cta/#consumers, no abierta hoy); compartir la página; no dejar que el «well, actually…» fije el relato; firmar la petición de change.org («over 100,000 signatories», dice la campaña; no se recontó); leer y compartir la carta abierta; responder la encuesta de Google sobre developer verification. [Fuente — campaña] El recuento de change.org y el texto de la encuesta no se abrieron. [No confirmado]

Desarrolladores: **«Do not sign up.»** No ADC, no identidad, no «play ball». Hablar a otros para que no se apunten. Añadir FreeDroidWarn (github.com/woheller69/FreeDroidWarn — repo no abierto hoy). Banner de cuenta atrás. [Fuente — campaña] [No confirmado el repo] Esta guía informa esa consigna. No la convierte en instrucción de la banda.

Empleados de Google: tips@keepandroidopen.org, desde una máquina que no sea de trabajo y una cuenta que no sea Gmail. [Fuente — campaña]

Ars Technica, citada en portada: «Google's Apple envy threatens to dismantle Android's open legacy.» Página no abierta hoy. [Reporte externo]

Prensa que la propia campaña cita en portada (titulares, no verificados uno a uno hoy): Tom's Guide, Bleeping Computer, How-To Geek, Ars Technica, Tuta Blog, TechSpot, Cybernews, 9to5Google, InfoWorld, Slashdot, The Register, TechCrunch, Hackaday, Linux Magazine. [Fuente — portada KAO, como lista de la campaña] [Reporte externo]

---

## 📗 F-Droid, 29-sep-2025

Blog «F-Droid and Google's Developer Registration Decree», reabierto hoy. [Fuente] El corte viejo hablaba de un texto de febrero 2026: no se usa. Este es el que hay.

Portada de F-Droid, al corte: «F-Droid is under threat… We need your help» y enlace a keepandroidopen.org. [Observación]

Quince años de repo FOSS. Contraste con las tiendas comerciales —Play la más visible—: las llaman semillero de spyware y estafas, apps que monetizan atención y minan información íntima, incluyendo «trickery and dark patterns». Enlace a TechCrunch (13-feb-2025) sobre un fabricante de spyware; no se abrió hoy. [Fuente] [Reporte externo]

Cómo trabaja F-Droid, según F-Droid: el autor publica el código; el equipo revisa que sea FOSS y sin anti-features no documentados (anuncios, trackers); el build service compila y empaqueta; se firma con la clave de F-Droid o, si el build es reproducible, con la clave del autor. El usuario puede confiar en que el binario sale de ese código. [Fuente]

¿Quieres un clima que no mande cada movimiento a un bróker, o un calendario que no vacíe tu vida en una red de anuncios? F-Droid, dicen, está para eso. Código abierto como desinfectante. [Fuente]

**El decreto.** El mes anterior a ese blog (agosto 2025), Google «unilaterally decreed» el registro central. Tasa, términos no negociables y cambiantes, documentos de identidad incluyendo ID gubernamental, enumerar todos los application identifiers. [Fuente]

F-Droid no puede exigir a los autores ajenos que se registren en Google. Tampoco puede «tomar» los identificadores de las apps que distribuye: sería apropiarse del derecho exclusivo de distribución. [Fuente]

Si el decreto entra en vigor como amenaza, acaba el proyecto tal como es, y el mundo pierde el catálogo de miles de apps auditables. Los usuarios de F-Droid se quedan sin instalar y sin actualizar lo ya instalado. ¿Cuántos usuarios hay? No lo saben: no rastrean ni tienen cuentas. «No user accounts, by design» (blog 28-feb-2022, no reabierto hoy). [Fuente]

**El «canard» de la seguridad.** Instalar directo lleva riesgo; es falso, dicen, que las tiendas centralizadas sean la única opción segura. Play ha hospedado malware de forma repetida (enlaces Malwarebytes y The Register, sep/ago 2025, no abiertos hoy). F-Droid ofrece otro modelo: FOSS, código auditable, builds y logs públicos, reproducibles. Eso, dicen, es una base de confianza más fuerte. Restringir la instalación directa no solo recorta la elección: erosiona diversidad y resilencia al consolidar control. [Fuente] [Reporte externo los casos de Play]

Play Protect ya existe en certificados: escanea y desactiva malware sea cual sea el origen. Cualquier riesgo percibido del sideload se mitiga con educación, transparencia FOSS y esas medidas, sin un registro excluyente. [Fuente]

No creen que el motivo sea seguridad. Creen que es consolidar poder sobre un ecosistema que era abierto. [Fuente]

**The Right to Run.** Si eres dueño de un ordenador, deberías poder ejecutar lo que quieras. Igual en el teléfono que en el escritorio. Forzar a los autores a un registro central para publicar es tan grave, dicen, como forzar a escritores y artistas a registrarse para circular su obra. Ofensa a la libertad de expresión y de pensamiento. Al atar identificadores de app a cédulas y tasas, Google construye un cuello de botella que recorta competencia y libertad. Debe hallar una solución que preserve derechos, elección y un ecosistema sano. [Fuente]

**Qué proponen.** Autoridades de regulación y competencia: mirar con cuidado, impedir que políticas de seguridad se usen para monopolio. Proteger tiendas alternativas y proyectos FOSS, y a desarrolladores que no pueden o no quieren cumplir esquemas excluyentes. [Fuente]

Si eres desarrollador o usuario: escribe a tu eurodiputado, congresista u otro representante; firma peticiones a favor del sideload. El segundo chunk del blog (cierre DMA/Comisión Europea) se leyó en una pasada anterior de esta banda: piden escribir al equipo DMA de la Comisión. [Fuente]

Esta guía no es un escrito a un regulador. Es el recorte fechado.

---

## 🏛️ Firmantes visibles

Keep Android Open dice 71 organizaciones de 23 países. [Fuente — carta / portada] Aparecer aquí no es recomendación de instalar ni adhesión de La Bandita. No se afirma que se hayan auditado las 71.

Nombres vistos en portada o en los chunks abiertos de la carta, con el dominio que la propia campaña muestra. La numeración 01–17 sale de la carta; el resto, de la parrilla de la portada. No es 71/71:

```
01 AdGuard — adguard.com
02 The App Fair Project — appfair.org
03 April — april.org
04 ARTICLE 19 — article19.org
05 ANSOL — ansol.org
06 Aurora Store — auroraoss.com
07 BEUC — beuc.eu
08 Brave — brave.com
09 The Calyx Institute — calyx.org
10 D64 — d-64.org
11 Chaos Computer Club (CCC) — ccc.de
12 Codeberg e.V. — codeberg.org
13 CryptPad — cryptpad.org
14 Cryptee — crypt.ee
15 Data Rights — datarights.ngo
16 Digitale Gesellschaft — digitale-gesellschaft.ch
17 Digital Rights Foundation — digitalrightsfoundation.pk
```

En la parrilla de portada, además, se vieron (entre otros): The Tor Project, FUTO, Fedimedia, GNU/Linux València, Rossmann Group, Open Rights Group, SLAT (Taiwán), KDE e.V., Software Freedom Conservancy, Vivaldi, Nextcloud, Italian Linux Society, Obtainium, FACiL, Guardian Project, microG, GrapheneOS Foundation, F-Droid, Open Web Advocacy, Digital Rights Watch, /e/ Foundation, FSF, FOSDEM, Techlore, Rocky Linux, Osservatorio Nessuno, XMPP Standards Foundation, Technopolice Bruxelles, EDRi, Fundación Karisma, Fastmail, Forbrukerrådet, IzzyOnDroid, VideoLAN. [Observación — portada]

Chunks 3–9 de la carta no se volvieron a pedir en esta pasada; no se recita un 18–71 numerado como si se hubiera leído entero. [No confirmado el resto numerado]

LineageOS aparece en recuentos previos de esta banda como firmante; en los chunks de carta abiertos hoy (01–17) no salió. No se afirma aquí como visto hoy en la carta. [No confirmado]

---

## 📌 Correcciones al corte 28-jul-2026

El texto que llegó de la banda tenía corte 28-jul-2026 y tablas Markdown. Facebook se come las tablas. El mapa de fechas también se había quedado atrás. Esto es lo que cambia, sin teatro:

```
Viejo: 30-sep = bloqueo de APKs / cierre del sideload.
Hoy:   30-sep = 4 países + 7 tiendas. Sideload aún no.
       FAQ 15-jul-2026.

Viejo: Android 8+.
Hoy:   Android 7+. FAQ 23-mar-2026.

Viejo: seis tiendas.
Hoy:   siete. Hub y guía.

Viejo: anuncio noviembre 2025.
Hoy:   agosto 2025. Hub, F-Droid, KAO.

Viejo: F-Droid «febrero 2026».
Hoy:   blog 29-sep-2025. KAO: F-Droid fuera de
       la lista de septiembre. Fecha que sí le
       impactaría: no publicada.

Viejo: 24 h por cada APK.
Hoy:   flujo de una vez. FAQ 23-mar-2026.

Viejo: EMM hasta septiembre 2027.
Hoy:   no salió en páginas abiertas. Fuera.

Viejo: LineageOS «no te afecta» (afirmado).
Hoy:   Google dice certified devices. No se
       probó. LineageOS no se afirma como
       firmante visto hoy.

Viejo: «50× más malware» como hecho nuestro.
Hoy:   no estaba en hub/FAQ. Fuera como cifra
       de esta guía. Queda, si acaso, como
       [Reporte externo].

Viejo: tablas Markdown.
Hoy:   bloques de texto.

Viejo: anclas internas tipo #1-resumen.
Hoy:   no existen en Facebook. Mapa + comentario
       fijado.

Viejo: «Android Developer Verifier» como nombre
       de producto de Google.
Hoy:   no se copió de hub/FAQ. Prensa, no hub.

Viejo: limited = sin ID, y se acabó.
Hoy:   sin ID, con perfil de pagos (nombre y
       dirección), 2FA, cuenta Google.
```

Ninguna de estas correcciones es un juicio sobre si la medida «debería» existir. Es alinear el texto con páginas abiertas el 13-sep-2026.

---

## 🌍 República Dominicana y LATAM

Brasil sí es piloto el 30-sep. República Dominicana no. [Fuente / Observación] México, Colombia, Argentina, Chile, Perú, Centroamérica, el Caribe: no aparecen en el hub como piloto. [Observación] Eso no es un salvoconducto para 2027. El salto que Google nombra para «all apps on certified devices» no trae lista de países en el hub. [Fuente]

Si viajas a BR, ID, SG o TH con un certificado y Play services, el hito de esas tiendas puede aplicarte allí. No se probó. [No confirmado]

Play services: Google dice que las actualizaciones del programa llegan por esa vía, no por una OTA del fabricante. [Fuente — FAQ] En RD, la inmensa mayoría de certificados las tiene. No se auditó un aparato. [No confirmado]

Tiendas del 30-sep que sí se ven en LATAM (Play, Galaxy, GetApps, etc.): el 30-sep, en RD, Google no las nombra como escenario de ese día. En Brasil, sí. [Fuente] Un usuario de RD con cuenta de Play y un Galaxy Store no se convierte en piloto por tener esas apps instaladas. El criterio que Google publica es el país del usuario (los cuatro) más la tienda participante. [Inferencia de lo publicado; no se probó]

Fundación Karisma (Colombia) aparece en la parrilla de firmantes de Keep Android Open. [Observación — portada] No se abre hoy karisma.org.co. [No confirmado su texto propio]

Esta guía no es un dictamen para INDOTEL ni para NORTIC. No se les escribió.

---

## 🔗 Relación con las otras guías de la banda

La guía de tiendas APK (F-Droid, Obtainium, Komi, Aurora, Droid-ify, IzzyOnDroid) no se anula el 30-sep. KAO y Google coinciden en que F-Droid no está en las siete tiendas de septiembre. [Fuente] Obtainium sigue siendo puente a GitHub, no aval de LiteAPKs. El README de Obtainium lista fuentes que esta banda no recomienda; eso no cambia porque Google mueva un hito.

Kototoro publica APKs en GitHub Releases. Eso es sideload / canal propio, no Galaxy Store. El 30-sep, según FAQ, aún no le aplica el bloqueo de vía normal. 2027 es la frase que hay que releer. El desarrollador de Kototoro decide si se registra; esta guía no se lo ordena.

Keep Android Open pide «Do not sign up». La Bandita informa esa consigna. No la convierte en regla de la banda. Quien desarrolla, lee el hub el día que actúe.

El sideload sucio (portales de mods, TikTok, «Spotify Premium APK») no se vuelve más justificable porque Google apriete: se vuelve más caro. [Inferencia] Esa es la tesis de la guía de tiendas, no de esta. Aquí no se enlazan mods. Se nombran, si acaso, para no confundir F-Droid con HappyMod.

Discord no es receptor de esta pieza. Las URLs de Discord de proyectos, si aparecen en otras guías, son hechos de proyecto, no un envío.

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
- Los blogs de android-developers.googleblog.com no se
  pudieron leer (ERR_BLOCKED_BY_CLIENT). Solo se usa lo
  que el hub enlaza y lo que sí cargó en
  developer.android.com.
- Los Shorts y el vídeo de YouTube del hub no se vieron.
- Help Center de ADC y de Play Console: no abiertos.
- policies.google.com/privacy: no abierta.
- android.com/certified/partners/: no reabierta.
- Chunks 3–9 de la carta abierta: no se numeró 18–71.
- change.org: no se recontaron firmas.
- Encuesta de Google: no se abrió.
- FreeDroidWarn: repo no abierto hoy.
- keepandroidopen.org/cta/: no abierta.
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

**Si desarrollas.** developer.android.com/developer-verification — elige Play Console o Android Developer Console. Si eres hobby, lee la guía de limited distribution (actualizada 20-ago-2026): 20 dispositivos, sin ID, con perfil de pagos. Keep Android Open pide no apuntarte; eso es la campaña, no una orden de esta guía. La decisión es tuya, con la página de Google abierta el día que la tomes.

**Si gestionas flota.** FAQ de empresa: canal gestionado exceptuado; registra igual por si el APK sale del corral.

**Si escribes a un regulador.** F-Droid y KAO publican vías. Esta guía no redacta la carta.

**Si te llega un video de TikTok el 30-sep diciendo «se acabó Android».** El 30-sep es 4 países + 7 tiendas. Reabre el hub. No instales un «bypass» de un portal de mods.

No hace falta «instalar todo ahora por si cierran». El atajo sucio no se vuelve más justificable.

Procedimiento corto, si de verdad te toca registrar (desarrollador, no usuario de Play):

1. Reabre developer.android.com/developer-verification
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

https://developer.android.com/developer-verification
  Hub. «Next milestone: September 30, 2026».
  Android 7+. 7 tiendas. 99 % Play. Limited
  «now available». Enlaces a blogs no leídos.

https://developer.android.com/developer-verification/guides
  Last updated 2026-08-18. Cuatro países, siete
  tiendas con fabricante, tres caminos, hitos.

https://developer.android.com/developer-verification/guides/faq
  Last updated 2026-08-27. Sideload 30-sep aún no.
  25 USD. ADB. Android 7+. Flujo avanzado. D-U-N-S.
  Países sancionados. NDA. APIs.

https://developer.android.com/developer-verification/guides/limited-distribution
  Last updated 2026-08-20. 20 dispositivos. Sin ID.
  Perfil de pagos. 2FA. Gratis. Handshake QR/enlace.

https://developer.android.com/developer-verification/guides/android-developer-console
  Last updated 2026-09-04. Packages, SHA-256, APK
  de reto, Status API, Console API, OAuth,
  duplicados (majority / sizeable / first-come).

https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html
  Amenaza existencial. Anti-features. Reproducibles.
  Play Protect. Right to Run. Reguladores.

https://keepandroidopen.org/
  Portada. 110 días. Starting 2027. Nueve pasos.
  Do not sign up. 71 / 23. Prensa citada.

https://keepandroidopen.org/faq/
  Septiembre no incluye F-Droid. Fecha de impacto
  a F-Droid: no publicada.

https://keepandroidopen.org/open-letter/
  24-feb-2026. Seis preocupaciones. Petición.
  Firmantes 01–17 vistos en esta pasada.

Blogs de Google enlazados por el hub (texto no leído hoy, fetch bloqueado):

android-developers.googleblog.com/2026/06/android-developer-verification.html
android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html
android-developers.googleblog.com/2026/03/android-developer-verification.html

Vídeos del hub (no vistos):

youtube.com/shorts/WcPElxbOeXY
youtube.com/watch?v=A7DEhW-mjdc

Consolas (sin sesión hoy):

android.google.com/developerconsole
play.google.com/console/signup

---

**Cierre.** El 30 de septiembre de 2026 es fecha real, para cuatro países y siete tiendas, en certificados Android 7+. No es la muerte del sideload ni de F-Droid ese día. 2027 es el salto que Google nombra para «all apps on certified devices», sin mes. Keep Android Open y F-Droid siguen en alerta; no las contradice el hito de septiembre, las desplaza. La carta del 24-feb-2026 pide rescindir el requisito para terceros; eso es la campaña, no una sentencia. Quien tenga que registrarse, que lo haga leyendo la página de Google el día que lo haga, no este post. Quien decida no registrarse, que sepa qué dice Google que pasa en certificados cuando el requisito le aplique, y qué dice la campaña que haga.

Si un anuncio oficial mueve una fecha, gana el anuncio. Este texto se actualiza con lo verificado, no con el miedo.

> La Bandita informa a partir de fuentes fechadas.

El hub ofrece «Español – América Latina» (?hl=es-419). [Observación] No se usó.            
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
