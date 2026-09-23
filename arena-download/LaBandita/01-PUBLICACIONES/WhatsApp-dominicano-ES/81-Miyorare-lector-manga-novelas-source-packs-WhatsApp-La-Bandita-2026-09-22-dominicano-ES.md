───────────────────

*Miyorare: el lector nuevo que llegó al barrio con sus propios sobres de semillas*

*La Bandita · 22 de septiembre de 2026 · edición dominicano-español*

> *Semilla de esta guía (léela entero, te sirve para todo):* imagina que en tu barrio llevan años las mismas tres colmado-librerías donde todo el mundo compra sus novelas y sus cómics. Un día abre frente a tu casa un cuarto colmado, pequeño todavía, pero con dos detalles que hoy no veías en ninguno: trae *sus propios sobres de semillas* —paquetes de fuentes que él mismo cultiva, revisa y empaca— y vende las plantas de los colmados viejos también, porque aprendió a hablar con todos. ¿Le compras? No de inmediato: primero le miras el registro, le preguntas de dónde saca la mercancía y esperas a ver si abre mañana. Eso es lo que esta guía hace contigo y con *Miyorare*: mirarle el pulso al lector nuevo del barrio, antes de sentarte a leer en su mostrador.

───────────────────

*🗺️ Mapa de esta guía*

```
├── 🌱 Semilla principal — el colmado nuevo frente a tu casa
├── ⚡ En una página — lo indispensable de Miyorare
├── 🌐 Mapa mental — la familia lectura y su nieto nuevo
├── 📖 La ficha completa de Miyorare (todo lo verificado 22-sep-2026)
│     ├── Qué es y qué no es
│     ├── Los canales estable y beta
│     ├── Los Source Packs oficiales (ID y EN)
│     ├── La compatibilidad declarada (cinco ecosistemas)
│     ├── Seguridad, Shizuku y Play Protect
│     └── El pulso del proyecto (números contados)
├── 🧬 La historia de la familia (por qué Miyorare habla tantos idiomas)
├── 🛡️ El modelo de confianza: quién empaca qué
├── 🪜 Cómo instalarlo con la vara en la mano (paso a paso)
├── 🔍 Cómo medirle el pulso a cualquier lector nuevo (método transferible)
├── 📦 Tus archivos locales: CBZ, EPUB, PDF y el respaldo feliz
├── 🧊 Mitos que caen con la vara
├── ❓ Preguntas frecuentes (las de verdad)
├── 📚 Glosario
├── 🔗 Enlaces comprobados
└── 🏷️ #tags
```

───────────────────

*⚡ En una página*

*Miyorare* es un lector libre y abierto de manga, cómics y novelas para Android, del proyecto *Noirero*. Su propia casa lo presenta así: _«Open-source Android reader for manga, comics, and novels, with extensible source support, offline reading, local files, and personal library management»_. Traducido al patio: lee manga y novelas en la misma app, baja para leer sin señal donde la fuente lo permite, traga tus archivos locales (CBZ, ZIP, EPUB, PDF), guarda tu biblioteca con favoritos, categorías, marcadores, notas e historial, y hace respaldo y restauración.

Lo que lo hace noticia dentro del ecosistema: *sus Source Packs oficiales* —paquetes de fuentes que el proyecto cura, compila, verifica y distribuye aparte de la app— y una *compatibilidad declarada* con cinco ecosistemas a la vez (Kotatsu, Mihon, Keiyoushi, UMA y Gekkoushi). Además existe en dos vías: *estable* y *beta*, instalables lado a lado porque usan identificaciones distintas.

Estado contado a 22-sep-2026: versión *v1.4.3*, licencia *GPL-3.0*, ★11 estrellas, 1 fork, 3.561 commits, 40 etiquetas y último empuje de código el *21-sep-2026* —un día antes de esta verificación—. Joven en fama, activo en el taller. Su declaración honesta: el aviso de Play Protect no quiere decir malware, y el APK oficial solo se baja de su GitHub. La nuestra: su «README» no declara todavía paquete de fuentes en español al día de hoy — se dice como está, sin adornarlo.

*Para quién es esta guía:* para quien lee manga/cómics/novelas en el teléfono y quiere saber si el vecino nuevo merece mostrador, y para quien quiere aprender a medirle el pulso a cualquier app nueva con la misma vara.

───────────────────

*🌐 Mapa mental — la familia lectura y su nieto nuevo*

> *Semilla:* antes de entrarle al recién llegado, mírale el árbol. Miyorare no cayó del cielo: creció en la huerta de dos familias grandes (la de los lectores de manga y la de las fuentes-parser), y eso explica casi todo lo que hace.

```
                 LA FAMILIA LECTORA (árbol simple)
│
├── 🧓 Los abuelos (las escuelas)
│     ├── Tachiyomi — la escuela original (archivada; su linaje sigue)
│     ├── Mihon — la heredera directa del guante del manga
│     └── Kotatsu — el otro gran tronco, con su propio parser
│
├── 👨‍👩‍👧 Los padres de las fuentes (de donde Miyorare aprendió)
│     ├── Keiyoushi — extensiones de la era moderna
│     ├── UMA — plugins y fuentes del ecosistema compatible
│     └── Gekkoushi — plugin-source de la misma hornada
│
├── 🧒 El nieto nuevo — MIYORARE (Noirero)
│     ├── Lee: manga + cómics + novelas, en una sola app
│     ├── Habla con los 5 ecosistemas de arriba (compatibilidad declarada)
│     ├── Trae Source Packs propios: Miyorare-ID y Miyorare-EN
│     ├── Dos puertas: estable (org.noirero.miyorare) y beta (…beta)
│     ├── Archivos locales: CBZ · ZIP · EPUB · PDF
│     └── Licencia GPL-3.0 — la casa tiene el plano a la vista
│
└── 🧰 La escolta de la casa
      ├── Shizuku (portero, documentado en su SECURITY.md)
      ├── GitHub Releases (única vía oficial del APK)
      └── Fuentes externas: cada una es su propio nivel de riesgo
```

*Lectura rápida del mapa:* lo importante de Miyorare no es que sea «otro lector más», sino dos cosas: (1) *no se encadena a un solo ecosistema* —declara cinco— y (2) *se declara dueño de la curaduría de sus propios paquetes de fuentes*, que es donde viven los riesgos y los aciertos de esta clase de apps. Todo lo demás de esta guía son esas dos ideas explicadas con calma.

───────────────────

*📖 La ficha completa de Miyorare (todo lo verificado 22-sep-2026)*

───────────────────

*Qué es (y qué no es)*

Miyorare es una *app lectora*, no una fuente de contenido. Ella no «trae» mangas ni novelas: te da el mostrador, la biblioteca y el casillero, y tú le conectas los corredores —las fuentes— de donde ella lee. Dicho de su propia casa: lector con _extensible source support_, lectura sin conexión _donde la fuente lo permita_, archivos locales y gestión de biblioteca personal.

*Qué sí es:*
• Un lector de manga, cómics y novelas en una sola app.
• De código abierto, licencia *GPL-3.0* (su LICENCIA trae guía ampliada de aplicación, retocada en abril de 2026).
• Una app con dos vías de instalación (estable y beta).
• Un proyecto que mantiene *sus propios paquetes de fuentes* oficiales, distribuidos aparte.
• Un proyecto joven pero con el taller en marcha: 3.561 commits y empuje de ayer al 22-sep-2026.

*Qué no es:*
• Ni Mihon ni Kotatsu: es una casa nueva que declara compatibilidad con ellos, no un fork declarado en su portada. _(Incertidumbre fichada: su portada pública no declara línea de fork; se describe como proyecto propio.)_
• Ni una tienda de mods: su repo es público, su historial es visible y su dueño tiene nombre de casa (Noirero).
• Ni una promesa de contenido en español: al 22-sep sus Source Packs oficiales son *ID* (indonesio) y *EN* (inglés); un paquete ES no está declarado en su documentación. Eso se dice sin suavizarlo.

───────────────────

*Las dos puertas: estable y beta*

El proyecto publica dos canales, y la diferencia importa:

```
Canal            · Para qué                                 · Application ID              · ¿Juntos?
────────────────────────────
`main` (estable) · Uso general, el carro de diario          · `org.noirero.miyorare`      · Sí, conviven
`beta`           · Pruebas de lo último, la calle de ensayo · `org.noirero.miyorare.beta` · Sí, conviven
```

Como las dos usan identificadores distintos, *pueden instalarse al mismo tiempo* sin pelearse. Eso, contado por el proyecto mismo en su documentación, permite tener la estable para leer en paz y la beta para mirar lo que está armando, sin que una pise a la otra. La verificación de la última entrega (v1.4.3) se mantiene al día en su propio README, con el identificador del commit de la rama estable (vimos la sección actualizada al 21-sep-2026).

> Regla del barrio aplicada: la puerta beta no es tienda de raritos, es el taller a cielo abierto. Entras si te gusta ver el andamiaje, no porque la estable «te quede chiquita».

───────────────────

*Los Source Packs oficiales (la parte que de verdad importa)*

Esta es la pieza que define a Miyorare, y la que más honestidad exige. *Un Source Pack es un paquete de fuentes preparado por el proyecto*: conectores que le dicen a la app dónde y cómo leer. Miyorare declara mantener *oficiales*, con estos rasgos constatados en su documentación:

• *Curados, construidos, verificados y distribuidos por el propio proyecto.* Es decir: Noirero no solo los lista, los empaca él.
• *Distribuidos aparte del APK:* los paquetes se actualizan a su propio ritmo, sin esperar a que salga otra versión de la app. Ventaja práctica: una fuente rota no exige reinstalar nada.
• *Dos paquetes a 22-sep-2026:* *Miyorare-ID* (contenido en indonesio) y *Miyorare-EN* (contenido en inglés).
• *Hechos desde ecosistemas compatibles conocidos:* la documentación nombra como referencia y ajuste a *Keiyoushi, UMA y Gekkoushi* para integrarlos a la arquitectura propia.
• *Con modelo de confianza escrito:* su SECURITY.md documenta el _modelo de seguridad del Source Pack_ —qué significa que sea «oficial» y dónde empieza el riesgo de la fuente externa—, y el proyecto aclara algo clave con franqueza inusual: que un paquete sea «oficial Miyorare» *no significa que Miyorare sea dueño de los sitios, servicios ni contenidos* a los que esas fuentes apuntan. La curaduría es del conector, no del contenido.

> *Traducción al patio:* el vecino nuevo no te dice «yo vendo mangas». Te dice: «yo te hago y te firmo las *llaves* que abren esas puertas, y te explico qué hicimos para revisar cada llave; lo que haya dentro de cada casa es cosa de cada casa». Esa frase, honesta y escrita, vale más que mil letreros de «100% seguro».

*La incertidumbre que esta guía no se calla:* al 22-sep-2026 no vimos declarado un Source Pack en español. Si tu lectura es en español, hoy por hoy el ecosistema con nombre de la casa —Mihon, Kotatsu y sus ramas, en las guías de lectura de esta misma serie— sigue siendo la vía documentada; Miyorare se fichará de nuevo cuando su paquete ES exista con fecha.

───────────────────

*La compatibilidad declarada (cinco ecosistemas a la vez)*

El proyecto enumera con quién es compatible, y cada uno significa una cosa distinta:

1. *Kotatsu* — compatibilidad del ecosistema de fuentes/_parser_ (el otro gran tronco lector).
2. *Mihon* — compatibilidad de extensiones (su formato de conectores).
3. *Keiyoushi* — compatibilidad y referencia de fuentes/extensiones (la casa de extensiones de la era moderna).
4. *UMA* — compatibilidad de plugins/fuentes.
5. *Gekkoushi* — compatibilidad de plugins/fuentes.

La propia app advierte, con buena letra, que *el nivel de compatibilidad puede variar según la fuente, la extensión, el plugin, el sitio y la versión*, y que esos cinco proyectos son terceros independientes: Miyorare no está afiliado a ellos, no lo respaldan oficialmente ni responde por sus contenidos. Eso también es un dato de higiene de proyecto: declara sus límites por escrito.

───────────────────

*Seguridad, Shizuku y Play Protect*

Su documentación de seguridad, directa:

• *El aviso de Play Protect no significa malware por defecto.* La app hace cosas de nivel avanzado —instalar extensiones-APK, acceso a almacenamiento, comprobar apps instaladas y soporte de *Shizuku*— y eso puede disparar el aviso del sistema por tratarse de permisos sensibles, no por maldad comprobada.
• *El APK estable oficial solo se baja de GitHub Releases* del repo Noirero/Miyorare. El proyecto lo dice; esta guía lo subraya: «clones» del APK en sitios ajenos son la semilla pintada de siempre.
• *La seguridad de extensiones y fuentes de terceros es otra capa distinta* de la seguridad del núcleo: la app puede estar limpia y la fuente que tú conectes, no. Por eso los Source Packs oficiales existen: para que haya una opción curada con dueño.

> Conexión con la pieza de tiendas de esta serie: el portero Shizuku vuelve a aparecer. Miyorare lo documenta en su mismo modelo de seguridad, y la regla de esta casa no cambia de barrio: el puente *se lo concedes tú*, a la app que *tú* verificaste.

───────────────────

*El pulso del proyecto (números contados, no adivinados)*

Contado en su casa pública el 22-sep-2026:

• *Estrellas: 11* · *Forks: 1.* Chiquito en fama — y se dice así, sin maquillarlo: es un proyecto de barrio nuevo, no un monumento de miles de ojos.
• *Commits: 3.561* en el historial de la rama principal. El taller no está quieto ni de lejos.
• *Etiquetas de versión: 40 · Ramas: 204.* Hay proceso, no solo empuje desordenado.
• *Último commit: 21-sep-2026* («ayer», al momento de esta verificación), con README de la v1.4.3 empaquetada en merge del mismo día.
• *Historial reciente:* carpeta `extensions` con sincronización de fuentes aprobadas de su _Compatibility Farm_ (18-sep), documentación de reorganización segura de ajustes (13-sep), modelo de seguridad de Source Packs (13-sep) y mantenimiento de compatibilidad (17-sep). O sea: la semana pasada estuvo de lleno en el taller.

*Cómo se lee ese cuadro con cabeza fría:* poca fama + mucho trabajo = _proyecto en ciernes con oficio_, no «proyecto fantasma». La prueba de vida no son las estrellas de ayer, son los commits de la semana. La cabeza fría también dice lo otro: 11 estrellas quieren decir *pocos ojos auditando*, y por eso mismo en esta ficha manda el método (vara) más que la recomendación cerrada.

───────────────────

*🧬 La historia de la familia (por qué Miyorare habla tantos idiomas)*

*Semilla del árbol:* en el barrio lector hubo una tienda-manga legendaria que cerró hace tiempo. Sus hijas abrieron cada una su colmado: una se quedó con el mostrador clásico (Mihon), otra armó el suyo con balanza propia (Kotatsu). Los proveedores de mercancía —las extensiones y parsers— se organizaron en casas de empaque (Keiyoushi, UMA, Gekkoushi). Y ahora aparece un nieto que *habla el idioma de todas las casas a la vez* y, de paso, *aprendió a empacar su propia mercancía* con sello de la casa. Ese nieto es Miyorare.

Por eso su compatibilidad declarada no es magia ni reclamo vacío: es *aprendizaje de ecosistema*. Cuando un proyecto dice «entiendo extensiones de Mihon, parser de Kotatsu y fuentes de estas tres empacadoras», está diciendo que estudió los formatos ya probados por años de uso comunitario, en lugar de inventar un formato nuevo que nadie conoce. Para ti, la lectura práctica es doble:

• *Si vienes del mundo Mihon/Kotatsu*, Miyorare te habla en tu idioma de fuentes (con la cautela oficial de la compatibilidad variable, arriba).
• *Si el proyecto crece*, sus Source Packs ID/EN de hoy pueden ser la plantilla del ES de mañana — y esta guía quedó fechada para contarlo cuando exista.

También por eso esta familia se habla en varias guías de la serie: las ramas de lectura del lector (Mihon, sus forks y la cadena Kotatsu-Yukimi-Usagi) tienen casas propias en esta colección, y el nieto de hoy aprende de todos esos cuadernos. Nada de lo viejo se invalida por lo nuevo: se verifica de nuevo, con fecha nueva.

───────────────────

*🛡️ El modelo de confianza: quién empaca qué*

La pregunta adulta de toda app lectora es una sola: *¿quién empaca las llaves que abren las fuentes?* Tres respuestas posibles en el mercado:

```
1. Nadie: fuentes sueltas, de grupos y enlaces voladores  → puesto sin dueño
2. La comunidad en gran lista abierta                     → mercado popular (con lupa)
3. El proyecto mismo, curado y firmado                    → colmado con sello propio
```

Miyorare declaró vivir en la puerta 3 para sus paquetes oficiales: los * Source Packs pasan por curaduría, compilación y verificación de la casa* antes de distribuirse, y el modelo de seguridad está escrito en su SECURITY.md. Eso no borra el riesgo de la fuente externa (el sitio de lectura al que apunta el conector), pero cambia la pregunta: ya no es «¿de dónde salió esta llave?» sino «¿confío en la casa que la revisó?», y para eso están sus commits, sus documentos y sus fechas visibles — todos contados arriba, no pedidos en fe.

> La regla del barrio, repetida porque nunca sobra: la *llave* la revisa quien la empaca; el *contenido* de cada cuarto lo revisas tú entrando con la vara (fuente declarada, casa visible, nada de enlaces de grupo).

───────────────────

*🪜 Cómo instalarlo con la vara en la mano (paso a paso)*

1. *Entra por la puerta oficial:* el repo `github.com/Noirero/Miyorare`, sección *Releases*. La casa del código es la única autoridad admitida por esta guía para su APK — el proyecto mismo lo declara.
2. *Elige puerta:* estable (`main`) si lo tuyo es leer tranquilo; beta si quieres mirar el taller. Al 22-sep, la estable es la *v1.4.3*.
3. *Confirma la identidad del paquete:* la estable declara `org.noirero.miyorare` y la beta `org.noirero.miyorare.beta`. Si el APK que te pasan trae otra identidad, es otra cosa disfrazada — reacción: no se instala, se borra el enlace y se anota el intento.
4. *Lee el aviso de Play Protect con cerebro:* si aparece, recuerda la explicación propia del proyecto (permisos avanzados documentados: instalar extensiones, almacenamiento, apps instaladas, Shizuku). Aviso que ya explicaste ≠ bandera roja automática. Aviso sin proyecto ni documentación detrás, sí.
5. *Conecta fuentes con dueño:* primero los Source Packs oficiales (repo `Noirero/Miyorare-Source-Packs`), o los ecosistemas compatibles con casa pública. Lo suelto, de grupo y volador, se queda afuera.
6. *Shizuku solo si lo necesitas y lo conoces:* la app lo soporta; eso no te obliga a encenderlo. Si lo usas, es el portero de siempre: lo concedes tú, consciente.
7. *Prueba con calma y respaldo:* antes de enamorarte de la biblioteca nueva, mira dónde están el respaldo y la restauración dentro de los ajustes. Biblioteca sin respaldo = novela que el agua se lleva.

> *Si algo falla:* la app no abre con la fuente conectada → la fuente cambió o el plugin quedó atrás (la compatibilidad es variable, dicho por la propia casa); actualiza el Source Pack —por eso se distribuye aparte—. La beta se comporta rara → es beta: repórtalo por el canal oficial y vuelve a la estable, que convive a su lado sin pelea. El APK «alternativo» te pide raropepe → lo mismo que en el paso 3: lo que no sale de la casa oficial, esa chaqueta no es de Miyorare.

───────────────────

*🔍 Cómo medirle el pulso a cualquier lector nuevo (método transferible)*

Todo lo que hicimos arriba con Miyorare cabe en cinco miradas, y sirven igual para el próximo vecino que abra:

1. *¿La casa está visible?* Repo público con historial, dueño con nombre (Noirero), licencia clara (GPL-3.0 con guía ampliada). Sin casa, no hay ficha — hay sospecha con icono.
2. *¿Trabaja esta semana?* 3.561 commits y empuje de ayer = taller en marcha. Un lector dormido acumula fuentes rotas como polvo.
3. *¿Quién empaca las fuentes?* Si hay paquetes oficiales con modelo de seguridad escrito, hay cadena de custodia. Si todo viene «de un listado por ahí», la custodia la pones tú — y se dice así.
4. *¿Declara sus límites?* Miyorare declara: compatibilidad variable, terceros independientes, oficial ≠ dueño del contenido, en español nada aún. Los proyectos serios ponen los bordes en la mesa; los anzuelos solo ponen «lo mejor de todos».
5. *¿Te vende paz o prisa?* Nada en su casa te apura. La gramática del cebo («últimas 24 horas») no existe en un repo serio: lo bueno sigue mañana, y mañana se vuelve a verificar.

> *Plantilla de bolsillo para el lector nuevo del futuro:* casa visible + taller en marcha + empacador con nombre + límites escritos + cero prisa. Cinco «sí» y se le mira el mostrador; un «no» y se espera con la vara afinada. Esa plantilla no es de Miyorare ni de La Bandita: es tuya desde hoy, para cualquier app que se te paree frente a la casa.

───────────────────
*📦 Tus archivos locales: CBZ, EPUB, PDF y el respaldo feliz*

*Semilla del baúl:* hay libros que llegan a tu casa en sobre del empaque (las fuentes) y hay libros que tú ya tienes doblados en el bolsillo desde hace años: los CBZ de aquellas tardes, los EPUB que te pasó tu primo, el PDF de aquel trabajo guardado. El colmado serio no te obliga a botarlos: te da un cajón donde guardarlos con su propia ficha. Miyorare declara ese cajón explícito: *local files*: CBZ, ZIP, EPUB, PDF.

───────────────────

*Qué es cada formato sin traductor de diccionario*

```
Formato  · Peso típico               · Lector afinado                    · Lo que debes saber
────────────────────────────
CBZ  · Alto (imágenes empacadas) · Manga y cómics escaneados         · Contenedor de imágenes en ZIP: calidad = la del escaneo original
ZIP  · Variable                  · Lo mismo, sin etiqueta de «cómic» · El empaque crudo de páginas
EPUB · Liviano (texto con flujo) · Novelas, libros                   · El texto se reordena a tu letra/tamaño: la lectura larga descansa
PDF  · Variable                  · Documentos de hoja fija           · La hoja va como foto: en pantalla chiquita se pelea a veces
```

La recomendación de la casa, dicho sin adornos: los CBZ/ZIP van donde la imagen es el cuento (manga, cómics, webtoons escaneados), el EPUB va donde el texto es el cuento (novelas), y el PDF va donde la hoja importa tal cual salió (propuestas, guiones, manuales). Un mismo teléfono puede las cuatro cosas, y Miyorare las declara todas en su ficha.

───────────────────

*El respaldo feliz*

Su documentación enumera respaldo y restauración como función explícita. Traducido a costumbre:

1. *Cuando cambias de teléfono:* primero respaldo → carpeta segura → nuevo teléfono → restauración. En ese orden, nunca al revés.
2. *Cuando te enamoras de una beta:* respaldo desde la estable *antes* de abrirle el taller. Estable y beta conviven, pero el respaldo feliz te dice qué libro estabas leyendo si el taller truena.
3. *Cuando cambian las fuentes:* un Source Pack nuevo no borra tu librería ni tus notas si el respaldo existe. Semilla simple: _el respaldo no se hace cuando el teléfono se daña; se hace cuando el teléfono todavía funciona contento_.

───────────────────

*Orden del cajón: biblioteca, categorías y el historial honesto*

La app declara Biblioteca con favoritos, categorías, marcadores, notas e historial. Eso son seis muebles distintos y conviene no mezclarlos:

• *Favoritos* = los que volverían contigo hoy. De cabecera.
• *Categorías* = los cajones por tema: «manga en curso», «novela quieta», «leer con lupa». Tu orden, tu nombre, nada impuesto.
• *Marcadores* = la página doblada de la noche anterior, dentro de una obra.
• *Notas* = lo que pensaste leyendo. La lectura con nota no se te pierde igual que la lectura a secas.
• *Historial* = el recibo de lo que pasó. Útil para retomar y también para darte cuenta —con honestidad de biblioteca— de qué leíste de verdad y qué solo acumulaste.

> Regla de vida de librería: la biblioteca gorda sin orden se convierte en caja debajo de la cama. Cien títulos con categorías valen más que mil títulos mirándose entre sí.

───────────────────

*📅 La semana observada en el taller (todo con fecha)*

*Semilla del taller:* un vecino se conoce en dos fotos: la de su puerta, que es fija, y la de su semana, que se actualiza sola. Esta guía le tomó la segunda foto a Miyorare entre el 13 y el 22 de septiembre de 2026, directo del historial público de la casa. Esto es lo que pasó de verdad, sin inflarlo ni ensalzarlo:

• *13-sep-2026 — dos movimientos de casa seria el mismo día:* se documentó (y se movió de paso) la *reorganización segura de los ajustes* —protegiendo la configuración guardada y las rutas de las fuentes/extensiones ya cargadas— y se escribió el *modelo de seguridad de los Source Packs* (su SECURITY.md de los paquetes). Traducción: el 13 no se hizo «una mejora bonita», se hizo la póliza del taller.
• *17-sep-2026 — mantenimiento de compatibilidad:* carpeta `extensions` y herramientas de compatibilidad, en el canal beta. Traducción: el puente con los cinco ecosistemas vecinos no es una declaración al aire, es trabajo que se regresa a revisar.
• *18-sep-2026 — la «Compatibility Farm» trabajó:* sincronización y _promoción_ de fuentes aprobadas desde su granja de compatibilidad hacia la carpeta de extensiones (19 archivos movidos entre `farm`, `plugins` y fuentes disponibles). Traducción al barrio: la curaduría de las llaves corre por asamblea y fuego real, no por promesa.
• *21-sep-2026 — la única entrega del mes:* se fusionó el README de la *v1.4.3* con su sección de verificación actualizada (versión + identificador del commit de la rama estable). Ayer respecto a esta verificación.

*Qué concluye la foto sin pasión:* una semana con ajustes, seguridad, compatibilidad, curaduría y versión estable en siete días —eso no es taller ornamentado, es taller con rutina— y, a la vez, una casa cuya fama sigue siendo la de recién llegado (11 estrellas contadas). Las dos verdades pueden dormir en el mismo cuarto: *tiene oficio + tiene por ganar su vecindario*. Recomendar eso no es recomendar ni descartar: es fichar con fecha —lo que esta guía acaba de hacer contigo.

> Regla del barrio ampliada: no le creas al proyecto que te enseña su puerta bonita; créele al que te deja mirar su semana. Por eso esta ficha empieza con fechas y termina con fecha — y por eso la ficha vieja de un proyecto dormido (mira el caso Aurora Store Crxmson, de la pieza madre de tiendas) y la ficha joven de un proyecto despierto no pesan lo mismo.

───────────────────

*🧭 Anatomía de una página de GitHub: dónde mirar qué (método para toda app)*

*Semilla del mostrador:* la cartelera pública de cualquier proyecto libre tiene los mismos cinco carteles, y se leen en el mismo orden. Aprende los cinco y nunca vas a necesitar que nadie te diga si una app nueva vale la primera mirada — la primera mirada te la das tú sola.

───────────────────

*Cartel 1 — La barra gris de arriba (la cédula)*

`usuario/repositorio` con su ⭐ estrellas, su 🍴 bifurcaciones (forks) y sus “issues” (asuntos) y “pull requests” (empujes revisados). Lo que esa barra te dice y lo que no te dice:

• *Estrellas = fama.* 11 estrellas dicen “vecino nuevo”, no “vecino malo”; 11 mil estrellas dicen “hace mucho que vive aquí”, no “sigue vivo hoy”.
• *Forks = confianza entre constructores.* Uno solo en Miyorare a 22-sep-2026; enormes en los archivos vivos de la familia lectora. El fork es cuando otro obrero dice “la obra es tan seria que yo también quiero tablones de la misma”.
• *Issues abiertos/cerrados = la calle que habla.* Un numero alto de asuntos no es maldad: es uso. Un proyecto sin asuntos es un colmado sin fila: o es perfecto, o nadie compra ahí.

───────────────────

*Cartel 2 — La línea del último commit (el pulso)*

Arriba del listado de archivos hay una línea con el último “paso” del taller: su nombre, su identificador corto (hash) y su hora/fecha relativa. Si dice “yesterday”/“hace X horas”, el taller respira. Si dice “hace 14 meses”, la puerta dejó de abrirse hace rato. En Miyorare, fichado el 22-sep: *último paso el día anterior*. En el taller no se cree en promesas de futuro — se mira el paso de ayer.

───────────────────

*Cartel 3 — La pestaña Releases (la tienda de versiones)*

Ahí viven las entregas oficiales: v1.4.3 (la estable a 22-sep), sus notas y sus archivos (el APK vive ahí si el proyecto lo hace por la vía sana — como Miyorare declara). Regla práctica: *si el APK no está donde vive el código, el APK no es de la casa*.

───────────────────

*Cartel 4 — La pestaña de seguridad (SECURITY.md)*

Más del 95% de los repos no escriben el suyo. Cuando uno escribe el suyo (y encima escribe la póliza de sus paquetes de fuentes), te está diciendo por dónde se reportan las fallas y qué modelo de confianza manda. Miyorare lo escribió. Léelo antes de borrar el proyecto por un aviso de Play Protect; léelo también antes de concederle permisos sensibles.

───────────────────

*Cartel 5 — Los “topics” y el About (la presentación de tres líneas)*

Los carteles de bajo presupuesto pero alta franqueza: `manga`, `android`, `reader`, `novel`, `gpl-3.0` — cada uno declara letra chica por lo que la casa se define. El About de Miyorare (te lo citamos sin traducirlo completo ya arriba) menciona lector open-source, fuentes extensibles, offline, archivos locales y biblioteca. Eso es, exactamente, lo que la casa declara hacer. Ni más (no declara ser dueña de contenidos) ni menos (no declara estar en español todavía).

> *Juego de práctica:* aplica los cinco carteles a una app cualquiera que uses hoy. Si puedes llenar la ficha en veinte minutos sin preguntarle a nadie, la vara ya es tuya. No necesitarás que esta guía ni ninguna otra te diga dónde estaba la verdad: estaba en la cartelera pública, esperando miradas.

───────────────────

*🚚 Mudarse de lector sin perder la biblioteca (guía de mudanza honesta)*

*Semilla de la mudanza:* mudarse de lectura no es mudarse de cuarto: es mudarse con libros, con página doblada y con recuerdos. Por eso la mudanza seria se hace en cinco camiones y nunca con la librería en brazos en la calle.

───────────────────

*Camión 1 — Respaldo desde la casa vieja*

En tu lector actual (Mihon, Kotatsu, Usagi, el que sea), busca *Ajustes → Respaldo* y exporta el archivo de respaldo. Sácalo del teléfono a un sitio seguro (carpeta en nube tuya, equipo tuyo, con nombre y fecha: `respaldo-lector-viejo-22-sep-2026.ext`). Ese archivo es tu librería entera: títulos seguidos, capítulos leídos, categorías, y a veces hasta la página doblada. Si ese archivo no existe, no hay mudanza seria; hay cruzar los dedos.

───────────────────

*Camión 2 — Instalar la casa nueva SIN desmontar la vieja*

Miyorare estable, desde su Releases oficial. Se instala *al lado* del lector viejo, no encima. El lector viejo se queda abierto, funcionando, mientras la casa nueva se prueba. Regla dura: la casa vieja no se cierra hasta que la nueva ya abrió tranquila por lo menos una semana.

───────────────────

*Camión 3 — El reconocimiento (la semana de doble lectura)*

Durante unos días, lee lo urgente y sigue lo tuyo en el lector viejo, pero vas pasando a la casa nueva las categorías: las fuentes que te mantienen al día y el fichaje de cada obra. Miyorare declara compatibilidad con varios ecosistemas, pero tú vas obra por obra — no de golpe — y vas notando dónde la compatibilidad «variable» se manifiesta. Eso también es tu ficha personal, no la de la casa nueva: la de tu barrio, la tuya.

───────────────────

*Camión 4 — Los que no se mudan solos: biblioteca, historial, notas*

Muchas mudanzas pierden el historial y las notas porque se pensaban mover solos. *No se mueven solos.* La app nueva (cualquiera) parte su biblioteca de cero, y tus notas del lector viejo pueden no viajar entre formatos ajenos. Dicho con dureza de mudanza: si una nota vale mucho, cópiala al papel de hoy. El respaldo se hace de la app vieja y de la app nueva por separado, cada una con su fecha.

───────────────────

*Camión 5 — Cierre con verificación, no con nostalgia*

Cuando la semana de doble lectura termine, verifica contra tu respaldo: ¿están mis títulos? ¿Mis favoritos? ¿Mis categorías? ¿Dobladuras al menos las memorables? Cierra el lector viejo solamente cuando todo cuadre — y desinstálalo, no lo «dejes ahí» por apego. Un teléfono no es un desván de tres lectores dormidos; uno temático basta y sobra.

> *La vara aplicada a la mudanza:* respaldo primero, casas superpuestas una semana, obras una a una, historial manual, cierre contra el respaldo. Si te saltas el camión 1, el barrio entero no te puede salvar la biblioteca — y esa responsabilidad no es de ninguna app recordada con cariño: es tuya desde que lees en digital.

───────────────────

*🧪 Tres casos prácticos con la vara (declarados ficticios para entrenar)*

*Semilla del entrenamiento:* para que la vara no sea tarea de escuela, aquí van tres pueblos de mentira (declarado) con vecinos-de-ejercicio. Mídeles el pulso tú primero; debajo va la lectura de La Bandita.

───────────────────

*Caso A — «ComicNube APK Premium 100% gratis»*

Letrero: «Todas las revistas de cómics del mundo, sin límites ni permisos, descarga directa, únete por el canal». Sin repo, sin casa, con palabra clave Premium y con prisa («oferta de lanzamiento»).

*Lectura vara:* sin casa visible → *0/5*. La firma no cuadra porque no hay firma alguna. Permisos «sin permisos» por escrito → bandera roja al revés: todo APK toca algo; el que no te dice qué toca, te lo está tocando sin pedirte. La prisa «de lanzamiento» es la gramática del anzuelo. *Medida:* no se instala. Se anota como cebo y se alerta al canal que lo manda.

───────────────────

*Caso B — «LentoLecto» (repo público, 3 estrellas, último commit hace 11 meses)*

Letrero: repo visible, licencia MIT declarada, solo tres archivos en la carpeta `app`, sin releases. El autor responde a un asunto del año pasado con «tengo poco tiempo pero vuelvo».

*Lectura vara:* casa visible ✔; permisos no constan porque no hay entrega; ninguna escritura de límites; tallercito dormido; cero prisa (pero eso no lo salva). *Medida:* no se instala como lector de diario, pero se queda en el acta con fecha: «repo dormido, revisar a los seis meses». La vara no es machete: no mata por caridad, deja durmiendo con fecha.

───────────────────

*Caso C — «LeeLeo Beta Plus» (puerta de Discord, APK por Drive)*

Letrero: «la beta exclusiva del lector que viene». Solo por canal de invitación, APK por Drive «temporalmente porque GitHub no nos deja». Los usuarios lo defienden con cariño en el canal.

*Lectura vara:* nombre híbrido con palabra clave «Plus» → ya suena a chaqueta ajena; *GitHub no les deja* es la frase del que no quiere casa pública. La invitación como puerta pone la confianza antes que la verificación. *Medida:* no se instala; se manda la vara al canal. El cariño de los usuarios —declarado— no sustituye los cinco carteles. No es «odio a la comunidad»: es higiene básica para que el cariño no acabe en ojal-colector.

> *Prueba del nueve:* si en los tres casos tu veredicto fue el mismo que el de la casa antes de leerlo, ya llevas la vara adentro. Si no, reintenta el paso 4 del taller: los cinco carteles, en orden, sin pasión. La vara no lee «con qué me siento cómodo»; lee «qué consta con fecha».

───────────────────

*📇 Cuaderno de campo: la ficha imprimible de evaluación*

*Semilla del cuaderno:* cada app nueva que llegue al barrio pasa por esta ficha, en papel o en mensaje guardado, antes de instalarse. La ficha no le pregunta nada a la app: le pregunta todo a la cartelera pública ya la cartelera le responde con datos, no con marketing. Usa este molde con Miyorare, con la hermana siguiente, con cualquiera.

```
FICHA DE EVALUACIÓN — Lector/app nueva (molde de La Bandita)
Fecha de apertura: __________________  Verificador: __________________

1) CASA VISIBLE
   Repo/casa: __________________  ¿Existe hoy? [ ]sí [ ]no
   Licencia declarada: __________________  Dueño/nombre: __________________

2) TALLER EN MARCHA
   Último commit: __________  Estrellas: ____  Forks: ____  Releases: ____
   ¿Trabajó esta semana/mes? [ ]sí [ ]no   Evidencia: __________________

3) EMPACADOR CON NOMBRE
   ¿Quién cura/distribuye las fuentes o el contenido? __________________
   ¿Hay modelo de seguridad escrito? [ ]sí [ ]no  Dónde: __________________

4) LÍMITES ESCRITOS
   ¿Declara compatibilidad variable/dueños terceros/lo que no hace? [ ]sí [ ]no
   ¿Play Protect/permisos explicados por escrito? [ ]sí [ ]no

5) CERO PRISA
   ¿Gramática de anzuelo presente? (Premium, últimas horas, solo hoy) [ ]sí [ ]no
   ¿Se te presiona a instalar YA? [ ]sí [ ]no

VEREDICTO:
   [ ] Se abre el mostrador en período de prueba (5/5 o 4/5)
   [ ] Se anota y se revisa en: __________________ (3/5)
   [ ] No se instala; se anota como cebo/chaqueta (0–2/5)

NOTA DE INCERTIDUMBRE (si aplica): ______________________________________
```

> *Cómo se pasa la ficha sin trampas:* dos «no» en las cinco —sin pasión— ya basta para dejar dormida la app con fecha. Un «sí» a «¿te presionan a instalar YA?» es un «no» automático, no compensable, ni por todo el cariño del canal. Y la línea de incertidumbre está para llenarse, no para quedar bonita en blanco: lo que no consta hoy se anota hoy para que mañana, cuando conste, la ficha nueva herede la verdad y no el rumor.

*Uso real con Miyorare (ya hecho en esta guía):* casa visible ✔, taller en marcha ✔ (commit de ayer), empacador con nombre ✔ (Source Packs con SECURITY.md), límites escritos ✔ (compatibilidad variable + oficial ≠ dueño del contenido + ES no declarado), cero prisa ✔. Veredicto de esta casa: *abrir el mostrador en período de prueba* y volver estrictamente con fecha (la ficha heredada de dentro de seis meses existe aunque todavía no se escribe).

───────────────────

*🌎 Sobre idiomas, orígenes y barrios (declarado sin romantismo)*

Miyorare es un proyecto que se presenta en *indonesio* en su portada y su material de marca («Manga, novel, dan koleksimu…» —manga, novela y tus colecciones), con Source Packs ID y EN. Esto, lejos de ser un detalle exótico, es un hecho de ecosistema que conviene adultar: *el software libre no tiene capital*, y los barrios lectores del mundo no leen todos en inglés. 

La traducción útil para tu barrio: existe un taller asiático-serio, con oficio y disciplina documentada, que hoy lee contigo en inglés y mañana —si su comunidad madura— podría leer contigo en español. Nada de eso se debe pintar «ya en español»: no lo está al 22-sep-2026, se fichó aquí así por honra al método. Pero tampoco se debe pintar «ajeno»: su licencia GPL-3.0 significa que el taller no tiene dueño de una sola bandera: cualquier comunidad —la tuya— puede verlo, aprenderlo, y si quiere, aportar su paquete el día que se abra la puerta.

> *Regla emocional del barrio lector:* no te enamores de ninguna app al punto que te duela si para; enamórate del método con que la verificas. Las apps van y vienen; la vara se queda. Con la vara, el barrio descansa, los vecinos nuevos se miran con calma, y el español —tu español— no necesita mendigar espacio: se lo gana con fecha cuando su paquete exista.

───────────────────

*❓ Segunda ronda de preguntas pequeñas (las que sobraron del pasillo)*

*¿Cuánto pesa la app?*
No consta en su ficha el peso exacto del APK de v1.4.3 (por eso no se escribe aquí: la ficha honesta no adivina tamaños). Se verifica en el propio post de Releases antes de bajar, como paso 1 de la vara.

*¿Pide cuenta o registro?*
Su ficha declara biblioteca/gestión local, sin mención a cuenta obligatoria en la documentación pública leída el 22-sep. Si apareciera una puerta de registro que no consta en la ficha, la ficha se actualiza con fecha y esa novedad pasa a la vara como temperamento nuevo.

*¿Tiene modo oscuro?*
Declara UI moderna con tema claro/oscuro (light/dark en su documentación). Trivial, pero consta: con ficha pasada por dueño, todo dato —hasta el del modo oscuro— va con su fuente.

*¿Sirve para novelas visuales o audiolibros?*
No consta en su ficha. Se anota como incertidumbre, no como «probablemente sí». En esta casa «no consta» es una respuesta completa, no media respuesta.

*¿Por qué no recomienda la beta para darme «ventaja»?*
Porque la beta es para _el proyecto_ ayudarse a sí mismo, no para _ti_ leer primero. La lectura de diario duerme en la estable. Quien te vende la beta como atajo, no te quiere a ti: quiere un conejito con pantalla.

*¿Las notas de la biblioteca viajan si mañana salta otra app?*
Las notas que solo viven en la app vieja, viajan mal (ficha de mudanza). Las notas que además hiciste a mano, en un mensaje o papelado tuyo, viajan eternamente. La vara de los respaldos no es penitencia: es el hábito del que ya perdió una biblioteca una vez y no repite.

───────────────────

*🤝 Guía de convivencia con la familia lectora (quién hace qué, sin rivalidad inventada)*

*Semilla de la mesa familiar:* la familia lectora no es un campeonato: es una mesa donde cada cual tiene su habichuela. La pregunta útil no es «¿cuál es la mejor app lectora?» — pregunta de concurso barato — sino «¿para qué tarea exacta pongo cada app delante de mí?». Dicho así, la mesa queda repartida sin pelea.

───────────────────

*El reparto de bañquitos (con ficha, sin noviazgos)*

• *Para manga/cómics con las extensiones clásicas ya probadas del mundo:* las casas maduras del ecosistema (Mihon y su rama, las guías de forks lectores de esta serie). Años de uso comunitario, respaldos hechos, canal vecinal amplio. Eso pesa y se respeta.
• *Para novelas + manga juntos*, con el convenio de una sola mesa y quizás con el gusto de taller nuevo: Miyorare se postula con ficha honesta (léctora de ambas cosas declarado, Source Packs oficiales, dos puertas convivientes). No «mejor que las maduras»: distinto reparto de bañquito.
• *Para lectura en español hoy:* las vías documentadas en español de esta serie siguen al frente — dicho aquí por segunda vez sin poderse evitar la repetición honrada. Miyorare fichó su incertidumbre ES el mismo día de la verificación; cuando el paquete ES exista con fecha, el reparto se rehace con fecha, y no antes.
• *Para archivos que ya son tuyos (CBZ/ZIP/EPUB/PDF):* cualquiera de la mesa con puerta honesta lo sirve; el archivo local no depende del lector sino de tu baúl con respaldo. La app cambia, el baúl queda.

───────────────────

*Lo que la mesa NO tolera nunca*

• La app que se presenta como «sucesora oficial de___ muerta» sin descendencia declarada en la casa vieja: chaqueta.
• La «versión sin límites» de cualquier lector conocido: chaqueta con palabra clave.
• El «pack de proyectos populares» empaqueta-do-al-lado, todo en un solo APK: el cesto donde nadie audita cada huevo por separado.
• La puerta que exige apagar la verificación del teléfono para «garantizar la mejor experiencia»: esa frase, en cualquier idioma, es la señal del comedor ajeno; no hay mesa que repartir, hay puerta que cerrar.

───────────────────

*🗣️ La gramática del cebo (cómo habla el anzuelo cuando vende lectores)*

*Semilla de la oreja:* el anzuelo no miente con datos — miente con ritmo. Aprende su gramática una vez y cualquier APK nuevo, de lectura o de lo que sea, te llegará ya traducido antes de instalarlo. Cinco frases, cinco lecturas.

1. *«Versión Premium/PRO gratuita de [app famosa]».* La palabra cobra con nombre de casa ajena. Lectura: si fuera de la casa, estaría en la casa; chaqueta rechazada.
2. *«Todo el contenido del mundo en un solo toque».* El mundo cabe en nada. Lectura: nadie cura «todo»; «todo» es el nombre del cesto donde no se revisa nada.
3. *«Sin anuncios, sin permisos, sin límites».* Triple sin = nunca es gratis la escondida; algo pasa por detrás (el APK toca algo, alguien cobra algo, nada sale del aire). Lectura: mejor déjalo donde está — no se instala, no se comparte — y bloquea el canal que lo manda.
4. *«Solo por hoy, cupos agotados».* La prisa es coartada, no promoción: se usa para que instales antes de mirar. Lectura: lo bueno sigue mañana, con fecha; lo que solo existe hoy no existe mañana por voluntad del anzuelo, y mañana se te caerá encima.
5. *«Pásale esto a cinco amigos para desbloquear la biblioteca».* Tu círculo se convierte en la entrada gratis. Lectura: NUNCA. La gramática del cebo siempre te pide que sirvas de casa para el próximo atrapado; la vara corta hoy el eslabón en tu nombre de vecino.

> *Ejercicio de mesa:* repasa con la vara algún enlace de «lector premium» que te mandaran antes. Nómbrenle en voz alta sus cinco frases gramaticales cada una. Cuando hayas hecho dos o tres, el cebo dejará de aparecerte mágico: aparecerá gramática conocida. Y el enemigo gramatico-conocido ya no da miedo: da risa — y la risa es la mejor vacuna del barrio.

───────────────────

*🌅 El día a día con el lector nuevo (primeras dos semanas, dicho por experiencia de ecosistema)*

*Semana 1 — La cura del mostrador.* Lees lo urgente en tu lector viejo, lees el taller nuevo, experimentas dos o tres categorías, haces un respaldo de prueba en la estable. No mudes, no desinstales, no digas «nunca más» — ni a la vieja ni a la nueva. La semana 1 es para darse cuenta de verdad, no para declarar amor ni divorcio.

*Semana 2 — El equilibrio medido.* Empiezas a notar dónde la compatibilidad variable se manifiesta (declarado por la casa y por esta guía: constato). Mides el ritmo de tu lectura en cada puerta. El respaldo semanal del nuevo se hace el mismo día cada semana — el hábito lo fija el día, no la memoria.

*El día que algo falle.* Falla una fuente → la fuente es, la app no: se espera el Source Pack siguiente y se sigue leyendo por puertos de paso. Falla la beta → se reporta con datos (versión, nombre de obra, qué hiciste) y se vuelve a la estable sin drama. Falla la estable → el respaldo de la semana pasada te devuelve la biblioteca en media hora. Todo fallo se lee como información; ningún fallo se lee como traición personal del taller.

*El hábito final, el que queda para siempre.* Abrir la libreta de vez en cuando: la ficha de la app con su fecha de verificación, una nota cuando cambia algo importante (versión grande, cambio en SECURITY.md, paquete ES si algún día existe). La libreta no cuesta nada y te da lo que ningún canal: tu verdad con fecha.

───────────────────

*🚫 Qué esta guía NO receta (declarado por adelantado)*

Esta guía ficha, no prescribe. Queda por escrito, para que nadie la malinterprete mañana:

• *No receta «usa Miyorare ya».* La ficha dice: mostrador en período de prueba + vuelta con fecha. Quien quiera esperar seis meses a que el vecino siga con libreta al día, está tomando la decisión correcta de su barrio — no exagerando.
• *No receta «bota a Mihon/Kotatsu».* La mesa familiar arriba demuestra el reparto: no hay choque entre bañquitos, hay tareas distintas. El barrio lector necesita sus casas maduras tanto como necesita mirar talleres nuevos.
• *No receta fuentes concretas de contenido.* La vara mide empacadores, no anuncia estantería: cada fuente específica se mide aparte, y quien te dice «esta es la buena, confía» sin cartelera pública está hablando gramática de cebo, aunque le caiga bien.
• *No receta desactivar nada del teléfono.* Ni Play Protect ni gastos de actualización ni aviso alguno. La documentación del proyecto explica el aviso; nadie debe explicarte apagarlo. Nunca. En ningún idioma.
• *No receta entrar por enlaces externos.* Puntero único de esta guía: repo oficial + Source Packs + SECURITY.md. Lo demás, por bueno que suene, queda fuera de la ficha hasta que tenga su puerta fechada.

───────────────────

*❓ Tercera ronda corta (para dejar ficha cerrada)*

*¿Sirve en tablet y en teléfono?*
Su ficha declara app Android sin distinguir formato; la experiencia de lector con UI moderna suele escalar, pero como no consta fichado específico para tablet, se anota como incertidumbre y no como promesa. Tu tablet se prueba misma (puerta estable, contenido tuyo, sin prisa).

*¿Si ya tengo Mihon, para qué tener dos lectores?*
No necesitas dos para nada — el baúl de archivos locales cualquiera de la mesa lo carga. La razón de mirar al vecino nuevo no es necesidad inmediata, es _conocimiento del barrio_: el día que tu lector maduro tenga contratiempos o su ecosistema cambie, ya sabrás a qué puerta tocarle con ficha pasada por fecha — no por rumor de grupo.

*¿Los Source Packs oficiales son «seguros» al 100%?*
Nada es «100% seguro», y la primera casa que te lo diga así es la primera casa de la que hay que desconfiar de inmediato. Lo que consta: el modelo de seguridad escrito, la curaduría y compilación por el proyecto, la distribución aparte. Eso multiplica la visibilidad; no elimina la vara — jamás —.

*¿Esta ficha vence?*
Sí, y es lo más sano que le pasa. Toda ficha lleva su fecha: hoy 22-sep-2026. Todo lo dicho aquí de Miyorare es hoy; en tres meses se vuelve a abrir su casa y se rehace con fecha — y si pasaron cosas (familia nueva de Source Packs, paquete ES, ritmo nuevo), esta guía se actualizará como cualquier mapa honesto del barrio.

───────────────────

*🗺️ Libería de la colección: dónde encaja esta pieza (mapa ancho)*

Esta ficha es hermana de la familia completa — no una isla nueva —. Mapa rápido para ubicarte al terminar:

• *La pieza madre de tiendas* dejó la vara con su nombre: la tienda legal regala siempre algo que el mod no puede — un dueño al que exigirle. En lectores pasa igual: el lector con repo tiene dueño al que exigirle; el APK del grupo no.
• *Las guías de lectura* de la serie (la cadena de los forks lectores, las casas maduras y sus bifurcaciones) mapearon los bañquitos grandes. La ficha de hoy busca solo una tarea: que el vecino nuevo más joven ya quede en el mapa con su ubicación correcta — esperando su historial, no robando el de nadie.
• *Las familias de verificación* (la de Exodus, VirusTotal, piezas de revisión de archivos) mantienen su oficio al lado: la ficha de una app nueva les abre la puerta cuando es la hora de medir por afuera, no solo por el README de la casa.

*La regla del mapa ancho:* ninguna pieza de la serie funciona sola. Los vecinos se miran entre sí, las fichas se heredan las fechas y el barrio queda descrito por todas a la vez. Esa es la promesa de fondo de La Bandita: no son piezas sueltas con marketing de pieza — familia entera con método.

───────────────────

*🧊 Mitos que caen con la vara*

*Mito 1: «Pocas estrellas en GitHub = app mala o peligrosa.»*
Las estrellas de GitHub miden *fama*, no *salud*. Al día de verificación: ★11 y 3.561 commits con empuje de ayer. La vara mira el taller en marcha, la licencia visible y los límites escritos; la fama ya vendrá o no vendrá — eso es el vecino el que va ganando clientela, no el código. Al contrario también es verdad: miles de estrellas en un archivo muerto (el caso ViMusic, ya contado en esta serie) no salvan a una app que dejó de respirar. Estrellas ≠ salud, en ambas direcciones.

*Mito 2: «El aviso de Play Protect quiere decir virus.»*
Dicho por el propio proyecto y corroborado por lo que declara hacer (permisos avanzados: instalar extensiones, almacenamiento, apps instaladas, Shizuku): el aviso puede aparecer por *permisos sensibles*, no por malicia. La calibración es: ¿el proyecto explicó por escrito por qué pide lo que pide? Miyorare lo explica en su SECURITY.md. Eso cambia el aviso de alarma a aviso acompañado.

*Mito 3: «Un Source Pack oficial quiere decir que el contenido de la fuente es legal y de la app.»*
Dicho con franqueza inusual por el mismo proyecto: oficial Miyorare = *curado, compilado y distribuido por el proyecto*; *no* significa que Miyorare sea dueño de los sitios, servicios ni contenidos. La custodia es de la *llave*; la *casa* a la que entra la llave es otro tema. La vara mide ambas por separado — y esta guía dejó su propia vara para eso en la pieza de tiendas.

*Mito 4: «Compatibilidad declarada con Mihon/Kotatsu = fork haciéndose pasar por nuevo.»*
Su casa no declara ser fork: declara *compatibilidad* con cinco ecosistemas, con niveles variables y terceros independientes. Un fork es un hijo con apellido; la compatibilidad declarada es un vecino que aprendió el idioma de todos. Son cosas distinguibles, y garantía de barrio es decirlas aparte: se dice «compatibilidad declarada» porque lo que consta con fecha es eso, no una genealogía que no consta.

*Mito 5: «La beta es para gente pro.»*
La beta es el taller a cielo abierto: entras para mirar, reportar y aprender cómo se arma. Lo «pro» no es usar beta; es saber que estable (`org.noirero.miyorare`) y beta (`…beta`) *conviven* sin pelear y que la lectura de diario va mejor en la casa ya pintada.

*Mito 6: «Si una app lee manga y novelas a la vez es ilegal.»*
La app es un *lector*: muestra lo que tú le conectas. Legal o no lo es el *contenido* y su licencia, no el mueble. La misma vara de siempre: fuente con dueño declarado, sitio visible, contenido con permiso — o no se entra. Esa pregunta se la haces a la fuente, no al mueble.

*Mito 7: «Sin muchos usuarios no sirve el respaldo. Se pierde todo igual.»*
El respaldo local es costumbre, no comunidad: exportar/ restaurar es función declarada por el proyecto y no depende de cuánta gente la use. La costumbre que te salva es hacerla estando el teléfono sano, y solo se aprende haciéndola una vez.

───────────────────

*❓ Preguntas frecuentes (las que de verdad se hacen en el barrio)*

*¿Miyorare reemplaza a Mihon o Kotatsu?*
Hoy, 22-sep-2026, no hay base para decirlo: son trayectorias distintas (las casas de la familia lectora tienen años de uso amplio; Miyorare tiene 11 estrellas contadas). Lo sí hay base: si lees en inglés o indonesio, sus dos Source Packs oficiales + la compatibilidad declarada lo hacen candidato con ficha honesta. En español, las vías ya documentadas de esta serie siguen al frente *hasta que exista paquete ES con fecha*. Decisión de semilla: el nieto se mira con cariño, pero al colmado del barrio se le da clientela cuando tiene estantería en tu idioma.

*¿Los Source Packs ID/EN me sirven si leo en español?*
Su nombre lo indica con franqueza: ID = contenido en indonesio, EN = contenido en inglés. Su cobertura exacta, sitio por sitio, la dice cada paquete al instalarse (verifícala tú dentro de la app). Lo que *no* consta al 22-sep: paquete oficial en español declarado. Incertidumbre explícita, sin inventar: la pregunta «¿y el ES?» queda abierta con fecha, como corresponde.

*Con 11 estrellas, ¿puedo confiarle mi biblioteca?*
La biblioteca la guardas con respaldo, no con esperanza. La confianza en el software se apoya en otra cosa: casa pública visible, historial en marcha (empuje de ayer), límites por escrito y modelo de seguridad documentado. Con eso a la vista + tu respaldo hecho, una biblioteca dentro de Miyorare puede dormir tranquila; sin respaldo, ninguna app — ni la más famosa — te promete nada.

*¿Puedo usar extensiones de Mihon directamente?*
La propia casa declara compatibilidad con ecosistema Mihon *con nivel variable* según fuente, extensión, plugin, sitio y versión. Traducción: intenta, pero por los canales curados primero (los Source Packs de la casa), y mide cada puente con la vara. Lo que la casa declara con humildad hay que leérselo con humildad: compatibilidad ≠ promesa cerrada.

*¿Para novelas largas me conviene EPUB?*
Sí, y eso es por el formato, no por Miyorare en particular: el EPUB reflows (el texto se acomoda a tu tamaño de letra y pantalla) y es liviano. Para PDF de hoja fija en pantalla chiquita: funciona, pero se pelea; no le eches la culpa al lector, es la hoja la que va en foto.

*¿Qué pasa si Noirero para el proyecto mañana?*
Lo mismo que le pasa a cualquier casa nueva: la licencia GPL-3.0 deja el plano a la vista (comunidad puede tomarlo), y tus respaldos te dejan migrar con calma a otra puerta de la familia (la piensa del ecosistema lector ya está contada en la serie). Lo que duele del adiós no es el adiós: es la biblioteca sin respaldo. Por eso el respaldo va antes que la nostalgia.

*¿Debo instalar la beta «para apoyar»?*
No. La beta se instala si tienes ganas de taller y canal de reporte a mano. El apoyo real a un proyecto chiquito se da así: verificas, usas con medida, reportas con datos y dices su nombre con su enlace — no con entusiasmo sin fecha. Al vecino nuevo se le apoya comprándole con desconfianza sana y regresando con queja concreta, no con fe ciega.

*¿Esto funciona sin internet, con la señal floja de mi barrio?*
La app declara lectura offline para lo descargado donde la fuente lo permite, más tus archivos locales que no necesitan señal de ningún lado. Traducción práctica al barrio: descarga bajo WiFi fuerte, lee en el guagua sin señal. La nube te alcanza solo para traer más, no para leer lo que ya es tuyo.

*¿Los 3.561 commits son señal de estabilidad o de caos?*
Depende del ritmo: el historial constatado muestra trabajo continuo y temas serios recientes (sincronización de fuentes 18-sep, modelo de seguridad 13-sep, reorganización segura de settings 13-sep), no empuje desordenado ni abandonos largos. Eso se lee como taller disciplinado. También se lee el otro lado con honestidad: 204 ramas y 40 tags en proyecto chiquito se lee como _muchas vías de una casa sola_, y se seguirá mirando si el canal se estrecha. Ficha con fecha, ojo también con fecha.

───────────────────

*📚 Glosario de esta guía*

• *Source Pack:* paquete de fuentes (conectores de lectura) armado por alguien con nombre; en Miyorare: curado, compilado, verificado y distribuido por el propio proyecto, aparte del APK.
• *Fuente/parser:* el conector que le dice a la app dónde y cómo leer una obra; es la llave, no el cuarto.
• *Compatibilidad declarada:* cuando un proyecto dice por escrito «hablo el formato de X»; Miyorare declara cinco: Kotatsu, Mihon, Keiyoushi, UMA, Gekkoushi — con niveles variables dichos también por escrito.
• *Application ID:* la cédula interna del APK; los canales stable y beta de Miyorare usan IDs distintas y por eso conviven sin pelear.
• *CBZ/ZIP:* empaques de imágenes (páginas escaneadas); el formato del manga/comic de imagen.
• *EPUB:* formato de texto fluido (reflow): la novela se acomoda a tu letra.
• *Fork:* hijo con apellido de otra casa de código; Miyorare *no* lo declara: se trata como proyecto nuevo que declara compatibilidad, no linaje (ficha dicho así).
• *Play Protect (aviso):* cartel del sistema por permisos sensibles; su significado lo cambia la documentación del proyecto detrás, no el cartel solo.
• *Modelo de seguridad (SECURITY.md):* donde la casa explica qué revisa, qué responsabiliza y qué límites tiene; leer lo que el proyecto escribió de sí mismo es la primera verificación.
• *Commits / tags / ramas:* pasos del taller / versiones puestas / vías de trabajo. Se miden con fecha; una foto de «repo con mucho verde de hoy» es evidencia, no admiración.
• *Vara:* el metro de esta casa: dueño visible + firma que cuadra + permisos con razón + límites escritos + cero prisa. Viene de la pieza madre de tiendas y no afloja por barrio.

───────────────────

*🔗 Enlaces comprobados (abiertos 22-sep-2026)*

• Repo oficial: https://github.com/Noirero/Miyorare
• Source Packs oficiales (ID y EN): https://github.com/Noirero/Miyorare-Source-Packs (constatado desde su documentación)
• Releases (vía oficial del APK, dicho por el proyecto): dentro del repo oficial
• Seguridad y modelo de Source Packs: SECURITY.md del repo oficial
• Ecosistemas declarados compatibles (cada cual su casa): Mihon · Kotatsu · Keiyoushi · UMA · Gekkoushi (fichado por documentación del propio proyecto; terceros independientes)

───────────────────

*🗒️ Nota de verificación de La Bandita (22-sep-2026)*

Todo número de esta ficha se contó hoy en la casa pública del proyecto: versión *v1.4.3*, licencia *GPL-3.0* (LICENCIA con guía ampliada retocada abril-2026), ★11 · 1 fork · *3.561 commits* · *40 tags* · *204 ramas* · último commit *21-sep-2026*; canales stable/beta con IDs distintas; Source Packs oficiales *ID y EN* curados y distribuidos aparte; compatibilidad declarada con Kotatsu, Mihon, Keiyoushi, UMA y Gekkoushi; archivos locales *CBZ/ZIP/EPUB/PDF*; biblioteca con favoritos/categorías/marcadores/notas/historial; respaldo/restauración; soporte Shizuku; explicación propia del aviso de Play Protect; y la propia franqueza del proyecto sobre «oficial ≠ dueño del contenido». 

*Incertidumbres marcadas al fuego:* (1) su documentación no declara linaje de fork — se trate como trata, así se fichó; (2) no consta paquete de fuentes en español al 22-sep — se dijo sin adornarlo; (3) compatibilidad declarada ≠ promesa cerrada, dicho por la propia casa y dicho otra vez aquí. Lo que no consta no se pinta; se anota y se visita el día exacto que conste.

───────────────────

*Nota de formato (D-011, Tratado V.0.04):* esta pieza fue reformateada la noche del 22-sep-2026 al formato nativo de su plataforma — negritas de un asterisco, citas, cajas monoespaciadas y separadores, sin un solo símbolo Markdown impreso. El contenido no cambió; la ropa sí.

> *Firma de la casa:* La Bandita informa a partir de fuentes fechadas. Lo no constado se anota con su incertidumbre. El mapa se mueve; la vara no.

───────────────────

*😄 Remate de esta pieza (meme original, consentido, del tema)*

> Don Ramón llega al colmado nuevo de Miyorare y le dice: «Mi hijo, vi que tienes sobres de semillas ID y EN… ¿y en dominicano no trajiste?». Miyorare, que ya sabe de qué va el barrio, le responde sin inmutarse: «Don, las semillas en español todavía no salen de la siembra — pero ya mismo le anoto la fecha en la libreta del mostrador». Don Ramón se queda un rato mirando la libreta, asiente despacio y le deja el mejor elogio que da un barrio: «Bueno… al menos este no me pinta las semillas. Vuelvo la semana que viene a ver cómo va la siembra». Y se fue tranquilo, porque en este barrio nadie le tiene miedo a esperar lo que está anotado con fecha.

_(Moraleja aplicada al tema: la fuente honesta con su fecha vale más que el arrastre de contenido sin dueño. Y el que espera verificando, espera seguro.)_

───────────────────

*🌅 Cierre — el nieto que habla todos los idiomas*

Esta pieza no preguntó «¿instalo Miyorare sí o no?»; preguntó algo más útil: *¿cómo se le mira el pulso a un lector nuevo del barrio?* Y la respuesta quedó en cinco miradas que te llevas para siempre: casa visible, taller en marcha, empacador con nombre, límites escritos, cero prisa. Miyorare pasó la ficha con honestidad propia (11 estrellas dichas sin tapujos, paquete ES no consta dicho sin suavizarlo), y la otra mitad la puso su documentación, que explica su Play Protect, su modelo de Source Packs y su propio límite. 

Y una última cosa queda dicha con calma: la mirada honesta a un proyecto joven también deja abierta la despedida honesta. Si mañana el taller se calla, la ficha de hoy no fue mentira — fue foto con fecha, y las fotos con fecha nunca mienten, solo se vuelven historia útil del barrio. Por eso el barrio apunta todo: porque la memoria del vecindario está hecha de apuntes, no de promesas. 

La familia lectora del barrio no se cierra con esta pieza: Mihon y Kotatsu siguen siendo las casas con clientela documentada en español, el nieto trae dos idiomas nuevos al mostrador y un aprendizaje de ecosistema que no se le había visto a ninguna app de su barrio. A la hermana siguiente de la serie le toca esa conversación: qué significa que las casas nuevas ya nazcan hablando todos los idiomas de las viejas. *Mapa se mueve; la vara no.*

───────────────────

*🌱 Semilla de despedida*

> Un vecino nuevo no se juzga por las estrellas de ayer ni por el letrero que cuelga hoy: se juzga por si tiene libreta con fecha, si pinta las semillas o las deja como son, y si abre el taller cuando tú no lo estás mirando. Miyorare abrió ayer 21 de septiembre con libreta al día y semillas sin pintar — y el barrio, ya curtido, le respondió con lo único que responde un barrio seguro de su vara: «Vuelvo la próxima semana. La libreta dirá». Eso es confianza madura: no la fe que se regala, sino la verificación que regresa.

───────────────────

#LaBandita #Miyorare #LectorAndroid #MangaYNovelas #SourcePacks #GPL3 #VerificaAntesDeInstalar #EcosistemaLibre #Shizuku #FuenteFechada #LecturaEnEspañol #OpenSource
