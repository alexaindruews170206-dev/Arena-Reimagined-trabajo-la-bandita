# Publicación 09 — Herramientas FOSS: la caja de oficio, cada pieza con su fecha de afilado

**La Bandita · 14 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🖼️ Galería y archivos
├── 🔐 Llaves y segundo factor
├── 📲 Transferir y conectar
├── 🧰 El cajón de sistema
├── 🗺️ Mapas
├── 📦 Cómo se gestionan las instalaciones
├── 📌 Por qué 20 piezas y no 200
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

El códice de herramientas de abril se caducó — versiones viejas vendidas como vigentes, listas infladas por inflar. Esta caja es la de hoy, 14 de septiembre: cada pieza con su repo abierto en las últimas horas, su estado real y su trabajo. Curaduría corta a propósito: veinte piezas que cubren el oficio, todas verificadas, cero relleno.

La caja, por cajones:

```
GALERÍA Y ARCHIVOS
Fossify Gallery ★3.696 · File-Manager ★1.753 · Phone ★1.329
Calendar ★2.155 · Clock ★699            (pushes de hoy/ayer)
Amaze File Manager ★6.387               la alternativa material

LLAVES Y SEGUNDO FACTOR
KeePassDX ★7.301 · releases de septiembre
Aegis Authenticator ★13.086             2FA con bóveda cifrada

TRANSFERIR Y CONECTAR
LocalSend ★91.047                       el AirDrop libre
Orbot ★3.538                            Tor en el bolsillo

SISTEMA
Termux ★60.797 · App Manager ★8.972 (v4.1.1)
Shizuku ★30.121                         APIs del sistema sin root

MAPAS
Organic Maps ★15.415                    offline, de verdad

INSTALACIONES
Obtainium ★19.7k                        (ficha en la guía de tiendas)
```

## 🖼️ Galería y archivos

### Fossify — la familia que sustituyó a las Simple

https://github.com/FossifyOrg

Cuando las Simple Mobile Tools se llenaron de anuncios, la comunidad bifurcó todo el set y lo mantuvo libre: así nació Fossify. Hoy la familia empuja código esta misma semana, pieza por pieza:

- **Gallery** (★3.696) — la galería sin publicidad que respeta tus fotos.
- **File-Manager** (★1.753) — archivos simples y honestos. Ojo al nombre: FossifyOrg/Files no existe; el canónico es File-Manager.
- **Phone** (★1.329) — marcador y bloqueo de números, con multi-SIM.
- **Calendar** (★2.155) — calendario con eventos y widgets, sin cuenta atada.
- **Clock** (★699) — reloj, alarma, cronómetro y temporizador.

GPL-3.0 todas. Sus versiones etiquetadas son de febrero; sus pushes, de septiembre: el patrón de proyecto maduro — estables tranquilas, mantenimiento continuo.

### Amaze File Manager — la alternativa con pedigrí

https://github.com/TeamAmaze/AmazeFileManager

★6.387 · vivo. El administrador de archivos material de toda la vida, de los más veteranos del ecosistema libre Android. Si Fossify te parece demasiado minimalista, esta es la opción con más años encima — y con raíces en la comunidad desde la época de las primeras ROMs.

## 🔐 Llaves y segundo factor

### KeePassDX — la bóveda compatible

https://github.com/Kunzisoft/KeePassDX

★7.301 · GPL-3.0 · push del 11-sep. La semana trajo tres releases al proyecto, con nombres de gato: «Scholarly Student» (2-sep), «Cutie Cat» (4-sep) y «Clever Cat» (10-sep). Bóveda de contraseñas compatible con el formato KeePass: tus bases se abren en cualquier plataforma del ecosistema KeePass, sin quedarte prisionero de nadie. Los datos viven en TU archivo — nube opcional, no obligatoria.

Si en algún momento metiste una contraseña en un sitio que luego cayó (la guía de TMO de esta familia cuenta uno grande), esto es el tipo de herramienta que ordena la casa después: una bóveda, contraseñas distintas por sitio, respaldo cifrado.

### Aegis Authenticator — el segundo factor que es tuyo

https://github.com/beemdevelopment/Aegis

★13.086 · GPL-3.0 · vivo. Los códigos de verificación en dos pasos, en una app libre con bóveda cifrada (AES-256 según su documentación), desbloqueo por huella, respaldo cifrado exportable e importación desde las apps propietarias más comunes (Google Authenticator, Authy, Microsoft, 2FAS y otras, según su lista oficial). El argumento de fondo: tus códigos 2FA son la llave de tu vida digital — depositarlos en una app cerrada sin exportación es dejarle las llaves al cerrajero sin copia.

## 📲 Transferir y conectar

### LocalSend — el AirDrop de todos

https://github.com/localsend/localsend

★91.047 — sí, noventa y un mil — · vivo · MIT según su ficha. La revelación silenciosa del software libre de los últimos años: pasar archivos entre teléfono, PC, tablet y hasta el teléfono del vecino sin cables, sin nube y sin cuentas — red local, protocolo abierto, apps para todas las plataformas. Si venías pegando archivos por WhatsApp «para pasarlos al PC», esta pieza sola justifica la guía entera.

### Orbot — Tor en el bolsillo

https://github.com/guardianproject/orbot

★3.538 · vivo · del proyecto Guardian. La app que enruta tu tráfico por la red Tor en Android, con VPN integrada o como proxy por aplicación. No es para todo el día ni para todo el mundo: es la herramienta de conexión cuando el circuito que necesitas requiere anonimato real — periodismo, investigación, o simplemente salir del país sin salir de casa. Del lado serio del ecosistema.

## 🧰 El cajón de sistema

### Termux — el terminal de bolsillo

https://github.com/termux/termux-app

★60.797 · push del 11-sep. Un terminal Linux completo en Android: editores, lenguajes, ssh, scripts. La puerta de entrada a «hacer de verdad» con el teléfono. Su versión etiquetada en GitHub es de mayo de 2025 (con betas de la 0.119) — su canal de paquetes va por su lado y con otro ritmo; el debate GitHub-vs-F-Droid de Termux es viejo y no se reabre aquí: repo nombrado, canal elegido el día que instales. Una regla sea: no se pegan scripts de nadie — el terminal es poder, y el poder se ejecuta con lo que tú escribiste o leíste completo.

### App Manager — el radiógrafo de tus apps

https://github.com/MuntashirAkon/AppManager

★8.972 · **versión 4.1.1 (4 de septiembre)** · push de HOY. El gestor de paquetes completo: ver qué permisos pide cada app, qué actividades expone, qué rastreadores arrastra, y desinstalar a fondo. Corrige la foto de la semana pasada, cuando la versión no respondía en la API: hoy está, y es de este mes. Su licencia en la página figura como propia (Proprietary-style libre — el proyecto la define en su repo; se lee allí antes de redistribuir).

### Shizuku — las APIs del sistema sin root

https://github.com/RikkaApps/Shizuku

★30.121 · Apache-2.0 · versión 13.6.0. La pieza que cambió el juego del «sin root»: deja que apps autorizadas usen APIs del sistema directamente, con permisos concedidos vía ADB (una vez por encendido) o root. Es el motor silencioso detrás de media docena de herramientas modernas de personalización y control. No es para quien empieza: es para quien ya sabe por qué lo busca.

## 🗺️ Mapas

### Organic Maps — el mapa que no mira back

https://github.com/organicmaps/organicmaps

★15.415 · release de agosto (2026.08.27) · push de HOY. Mapas offline completos del planeta, sin cuenta, sin rastreo, datos de OpenStreetMap. Para viaje, para el barrio sin datos, para el que decidió que Google no necesita saber por dónde camina. Su licencia en la página figura con aviso particular (licencia propia del proyecto, legible en su repo) — se dice tal cual, sin inventar etiquetas.

## 📦 Cómo se gestionan las instalaciones

**Obtainium** — https://github.com/ImranR98/Obtainium — ★19.7k, commit de ayer. La herramienta que vigila los repos de esta caja y te instala las versiones nuevas apenas salen. Su ficha completa vive en la guía de tiendas de esta familia; aquí basta su frase: el cajón de herramientas también se actualiza solo.

Y el fondo de la caja, para todos los cajones: **F-Droid** — la tienda libre donde buena parte de estas piezas también vive publicada. Tres vías (repo de GitHub, F-Droid, Obtainium) apuntando al mismo software: esa es la redundancia sana del ecosistema libre.

## 📌 Por qué 20 piezas y no 200

El códice de abril traía 88 herramientas. De esas, muchas estaban en versión vieja vendida como nueva, y varias repetían función cuatro veces. El criterio de esta caja es el contrario:

```
Una función, una pieza   si dos apps hacen lo mismo,
                         queda la más viva — no la más mencionada
Todo verificado hoy      si el número no se abrió hoy,
                         no va con fecha de hoy
Hueco declarado          lo que NO está en la caja (navegadores,
                         correo, mensajería, nubes) es porque
                         merece guía propia, no porque no exista
```

La caja de oficio no necesita ser infinita. Necesita ser cierta.

## ❓ Preguntas frecuentes

**¿Estas apps están en Play Store?**
Varias sí (Aegis, LocalSend, Organic Maps entre ellas). La vía del ecosistema libre es F-Droid o el repo — la guía de tiendas de esta familia explica las tres puertas. Esta guía no abre Play: la ficha de cada tienda es tema de su propia pieza.

**¿Fossify o Amaze para archivos?**
Fossify: minimalista, de la familia completa (galería, contactos, calendario). Amaze: más función por pantalla, más años de vuelo. Prueba ambas: son gratis en todos los sentidos.

**¿KeePassDX o Bitwarden?**
Filosofías distintas: KeePassDX guarda TU archivo (compatible KeePass, cero dependencia); Bitwarden es servicio con sincronización propia. No se compararon a fondo aquí: sin comparativa inventada.

**¿Shizuku es peligroso?**
Da poder de sistema a apps que TÚ autorizas, vía ADB o root. Es tan peligroso como la llave que dejas bajo el felpudo si autorizas a cualquiera. Con la cabeza fría, es el puente perfecto entre «sin root» y «control total».

**¿LocalSend funciona entre iPhone y Android?**
Sí: ese es parte de su punto — multiplataforma completa (Android, iOS, Windows, macOS, Linux), red local, sin nube.

**¿Orbot ralentiza todo?**
Tor paga su anonimato con latencia. Para navegación sensible, es el precio. Para todo el día, no está pensado — y su propia documentación lo dice mejor que este resumen.

**¿Termux necesita root?**
No. Su potencia no depende de root — depende de lo que sepas hacer con un terminal. Root abre otros capítulos, con otros riesgos (la guía de GLTools de esta familia cuenta por qué no se juega con eso desde el sofá).

**¿Cada cuánto se re-verifica esta caja?**
Cada vez que se use. Hoy fue el corte; los números que no se abran otro día no se citan como frescos.

## 🔗 Enlaces

- Fossify: https://github.com/FossifyOrg/Gallery · https://github.com/FossifyOrg/File-Manager · https://github.com/FossifyOrg/Phone · https://github.com/FossifyOrg/Calendar · https://github.com/FossifyOrg/Clock
- Amaze: https://github.com/TeamAmaze/AmazeFileManager
- KeePassDX: https://github.com/Kunzisoft/KeePassDX · Aegis: https://github.com/beemdevelopment/Aegis
- LocalSend: https://github.com/localsend/localsend · Orbot: https://github.com/guardianproject/orbot
- Termux: https://github.com/termux/termux-app · App Manager: https://github.com/MuntashirAkon/AppManager · Shizuku: https://github.com/RikkaApps/Shizuku
- Organic Maps: https://github.com/organicmaps/organicmaps
- Obtainium: https://github.com/ImranR98/Obtainium

> La Bandita informa a partir de fuentes fechadas. Una caja de oficio no se infla: se afila.
