───────────────────

*Los almacenes de las bombillas: extensiones, hubs vivos y la feria donde venden funditas que no encienden*

*La Bandita · 22 de septiembre de 2026 · edición dominicano-español*

───────────────────

🌱 LA SEMILLA

Imagina que tu lector de manga es una lámpara buena, de las que duran. La lámpara no hace la luz sola: necesita una bombilla para cada cuarto, y cada cuarto tiene un enchufe distinto. La lámpara no sabe de cuartos: sabe de bombillas. Esas adaptadoras — bombillas que convierten cualquier enchufe en luz — se llaman extensiones.

Ahora bien: las bombillas no se fabrican en tu casa. Se guardan en bodegas del barrio — almacenes con dueño, con horario y con historia. Una bodega abre todos los días con su camión de mercancía; otra cerró el mes pasado y dejó el aviso en la puerta; y en la feria del fin de semana hay unos toldos nuevos que venden «bombillas universales originales» a precio de saldo: encajan en todo, dicen — y a veces lo que encienden no es tu lámpara, es otra cosa.

Esta guía recorre las bodegas del barrio de los lectores libres — cuál está viva hoy, cuál migró de dirección, qué convención técnica anda mandando, y cómo se le ve la funda al toldo falso antes de comprarle. Todo contado hoy, con fecha de hoy.

───────────────────

🗺️ MAPA DE ESTA GUÍA

├── 🌱 La semilla
├── 🗺️ Este mapa
├── ⚡ En una página
├── 🧠 Mapa mental de la casa
├── 🧩 Las tres capas (y la regla del índice)
├── 📜 Línea del tiempo del ecosistema
├── 📗 Keiyoushi: el hub principal — y su mudanza técnica de agosto
├── 📘 Yūzōnō: anime vivo y la era lib 16
├── 📙 Los demás almacenes vivos
├── 🧬 De KeiSource 1.6 a lib 16: la convención que manda
├── 🗂️ Miyomi: el directorio que ahora tiene org y marca propia
├── 🎭 La feria de los impostores
├── 🧭 Las cinco preguntas antes de abrir un almacén
├── 📚 Solución de problemas del almacén (cuatro trancas)
├── 🧪 Casos prácticos del barrio
├── 🧯 Mitos de la bombilla (cuatro apagones)
├── ❓ Preguntas frecuentes
├── 📖 Glosario del tema
├── 😄 El meme de la pieza
├── 🛠️ Método de la casa
├── 🔗 Enlaces
├── 📝 Nota de verificación
└── ✍️ Firma y despedida

───────────────────

⚡ EN UNA PÁGINA

Las extensiones son la capa que conecta un lector libre — Mihon, Komikku y sus parientes — con sus fuentes de contenido. No viven dentro de la app: viven en almacenes con dueño, y el estado de cada almacén cambia semana a semana. Ayer hubo una mudanza técnica grande; hoy hay un ecosistema vivo con cara nueva.

Los datos de esta mañana, abiertos hoy:

```
Keiyoushi extensions          ★15.0 mil  bot empujó HOY     el hub
  (su repositorio se re-inicializó el 13-ago-2026 como
   almacén basado en releases — ciclo nuevo)
Keiyoushi extensions-source   vivo (★4.7 mil al 15-sep)     el código
Yūzōnō anime-extensions       ★439       commit hace 3 h    anime
  (su core recibió el 17-sep el «Keiyoushi Network Import»:
   el árbol oficial se injerta en el árbol de la familia)
cuong-tran/manga-repo         ★451       empujó el 21-sep   el indepe
  (su receta de instalación vive hoy bajo la dirección de
   yuzono/manga-repo — la casa migró, la receta no)
Miyomi (el directorio)        ★188       en org propia      el índice
  (cambió de dueño a la organización «miyomiorg» y de
   licencia Apache-2.0 a AGPL-3.0 más política de marca)
```

La convención técnica que gobierna todo esto ya camina en la era «lib 16»: los commits de los dos árboles nombran esa librería esta semana, y el árbol de Yūzōnō acaba de añadir una capa «LegacySource» para que las fuentes viejas sigan respirando bajo ella. Traducción al barrio: la lámpara nueva trae adaptador para las bombillas de antes — pero la feria vende, cada vez más, solo bombillas del patrón nuevo.

¿Qué necesitas saber sin estudiar nada? Tres cosas. Una: si tu lista de extensiones sale vacía u «obsoleta» con el aviso «Outdated app», el problema casi nunca es el almacén — es tu app vieja para la convención. Dos: la instalación de cualquier almacén se lee en la casa del proyecto, nunca pegada en un post — ni en este. Tres: los toldos de la feria — repos nacidos esta semana con estrellas gemelas y títulos de anuncio clasificado — no son bodegas: son anzuelos. La guía enseña a distinguirlos por el traje.

───────────────────

🧠 MAPA MENTAL DE LA CASA

Esta pieza abre el zaguán técnico de LA LISTA: la habitación de las extensiones y sus almacenes. Así se ve la familia entera desde arriba:

```
LA LISTA — el vecindario libre (rama de las extensiones)
│
├── 🪪 PUERTA 03 — El censo de desarrolladores (de ayer)
│      Por qué la forma de DISTRIBUIR apps cambia el 30-sep-2026
│      y en 2027. Parentesco con esta pieza: la lámpara y las
│      bodegas viven dentro del censo — distribuir también es
│      documento.
│
├── 🧩 PUERTA 04 — ESTA PIEZA
│      Las extensiones y sus almacenes: la bombilla, la bodega
│      y la feria. Qué está vivo hoy, qué migró, qué manda.
│
├── 🕳️ PUERTA 05 — La caída de TMO y los clones
│      (la siguiente del horno)
│      Cuando la app espejo cae, los almacenes de impostores se
│      llenan. El parentesco es directo: esta pieza enseña a
│      oler el toldo falso; la 05 muestra la batalla real.
│
├── 📚 PUERTA 06 — Forks y segundas generaciones
│      Los lectores que nacen de lectores: cada uno trae su
│      propia relación con estos almacenes.
│
└── 🔗 HERMANAS YA PUBLICADAS
       01 — tiendas y el reloj · 02 — Kototoro · 81 — Miyorare
```

La brújula de hoy: si tu lector no encuentra fuentes, el problema vive en ESTA habitación — la de los almacenes — o en la versión de tu app, no en tu teléfono. Y si te llegó por cadena de WhatsApp un «nuevo almacén universal oficial», esa cadena empieza en la feria de la sección 🎭, no en ninguna bodega de verdad.

───────────────────

🧩 LAS TRES CAPAS (Y LA REGLA DEL ÍNDICE)

Antes de recorrer bodegas, el plano del edificio. Todo esto funciona en tres capas:

```
LA APP        tu lector: Mihon, Komikku, TachiyomiSY
              y los demás de la familia. Ella no trae
              contenido: trae el motor.

LA EXTENSIÓN  la adaptadora: una bombilla por fuente.
              Vive en un ALMACÉN (repo) con dueño,
              historial y fecha — esta guía.

EL ÍNDICE     la receta técnica (una dirección de archivo
              de recuento) con la que la app descubre
              el almacén.
```

La regla de esta familia de guías sobre la tercera capa es de piedra: el índice no se pega. No porque sea secreto — está en el README de cada proyecto, a la vista — sino porque pegar recetas de instalación en un post es el gesto exacto que convierte una guía en anzuelo: hoy pego la receta buena y mañana, por el mismo canal, te llega la envenenada, y tú ya aprendiste a pegar primero y mirar después. La costumbre sana es al revés: quien quiera el índice, que lo lea en la casa del proyecto, el día que lo use, con sus propios ojos. Esta pieza enlaza las casas; las llaves se leen adentro.

Una consecuencia honesta de la regla: esta guía tampoco le dice a nadie qué contenido leer ni con qué fuente. El catálogo de esta casa es de herramientas — lámparas y bombillas — ; la lectura es tuya y de tu jurisdicción.

───────────────────

📜 LÍNEA DEL TIEMPO DEL ECOSISTEMA

Los almacenes de extensiones tienen genealogía, y conocerla explica el porqué del mapa de hoy:

```
Ene 2024      El árbol madre (Tachiyomi) archiva su
              almacén oficial de extensiones. La era
              «un solo hub» termina.

Feb-Ago 2024  Los hijos se reparten la herencia: nace
              Keiyoushi como almacén de referencia del
              árbol Mihon; la comunidad aprende a vivir
              con varios almacenes a la vez.

Ago 2024      El almacén oficial de anime del ecosistema
              Aniyomi archiva. La familia Yūzōnō hereda
              el anime en la práctica.

May 2026      Kohi-den, el otro código vivo de la casa
              Yūzōnō, archiva: la familia consolida
              su trabajo en los almacenes directos.

Jun-Jul 2026  Miyomi, el directorio de índices, cambia
              de dueño a una organización propia
              («miyomiorg») y de licencia a AGPL-3.0.

13-ago-2026   Keiyoushi re-inicializa su almacén como
              «release-based»: nueva maquinaria de
              distribución (se ve en su historial como
              «Reinitialize release-based repo»).

Sep 2026      La era «lib 16»: los commits de los
              grandes almacenes migran fuentes a esa
              librería, y Yūzōnō injerta el core de
              Keiyoushi en su propio árbol (#952).

HOY, 22-sep   Keiyoushi empujó hace 19 horas. Yūzōnō
              empujó hace 3 horas. manga-repo empujó
              ayer con su receta migrada. El mapa
              respira.
```

La moraleja del calendario: este ecosistema no tiene dueño único ni anuncio oficial central — tiene generaciones. Quien consulta la guía de hace un año encuentra las bodegas cerradas; quien consulta la de hoy las ve abiertas y moviendo cajas. Por eso cada guía de esta familia lleva su fecha en la meta.

───────────────────

📗 KEIYOUSHI: EL HUB PRINCIPAL — Y SU MUDANZA TÉCNICA DE AGOSTO

Keiyoushi es el almacén de referencia del árbol Mihon: el recuento de fuentes más grande del ecosistema, código abierto (Apache-2.0 en su repositorio hermano), y un bot propio — keiyoushi-bot — que actualiza el índice a diario. Hoy, la evidencia de vida más fresca que existe: el último «Update extensions repo» del bot es de hace 19 horas, con fecha 22-sep-2026 en la entrada del historial.

La novedad estructural que la madre de esta pieza no conocía: el 13-ago-2026 el almacén se re-inicializó como repositorio basado en releases. En la práctica, dos cosas cambiaron para el usuario avanzado. Primera, el almacén ahora distribuye con una maquinaria de releases — archivos de índice y de activos por lanzamiento (se ven en su raíz: índice en tres formatos y un archivo de activos de release) —, un ciclo de distribución nuevo que la propia casa describió en su commit como reinicio del repo. Segunda, junto con eso, la rama del almacén quedó con historial corto contado desde agosto: la «edad aparente» del repo bajó sin que el proyecto fuera nuevo — lección viva de por qué la vara mide el proyecto y no solo la página.

Para el lector diario nada cambia: el proceso de añadir el almacén sigue igual (su guía «Getting started» es la puerta, y su sitio ofrece añadirlo con un toque). Su sitio mantiene además el aviso más útil del ecosistema: si tu lista sale vacía o «obsoleta» con el «Outdated app», tu aplicación ya no es compatible con el almacén — soportan Mihon, TachiyomiSY y Komikku, y la solución no es buscar espejo: es actualizar la app desde su casa.

Detalle de transparencia que sigue igual y se dice igual: el repositorio de binarios no declara licencia en su página (el código sí: Apache-2.0). Sin licencia visible, no inventada — así queda fechado.

───────────────────

📘 YŪZŌNŌ: ANIME VIVO Y LA ERA LIB 16

El canal vivo de referencia para extensiones de anime en el árbol Tachiyomi/Mihon. La placa de hoy: 439 estrellas, 5.548 commits de historia, y el último empuje es de hace tres horas — una fuente nueva de anime en inglés integrada esta misma tarde (PR #984). El estante está tan vivo como se puede estar.

Pero la noticia de fondo no es la estrella: es la obra de plomería que se está haciendo dentro. Tres hechos visibles esta semana en sus commits:

*Uno — el injerto del core de Keiyoushi.* El 17-sep entró el «Keiyoushi Network Import (Core)» (PR #952): la capa de red del árbol oficial injertada en el árbol de la familia, con revisión y limpieza a dos manos de ambas casas. Traducción al barrio: las dos bodegas grandes ahora comparten el camión de reparto — menos duplicación, un mismo plomero para dos almacenes.

*Dos — la era «lib 16».* Los commits recientes migran fuentes a la librería 16 («Bump to Lib 16», visible en su historial de esta semana), y el 1-sep se añadió una capa pública llamada LegacySource «para compatibilidad con lib-16». Es decir: el patrón nuevo ya es el vigente, y la casa misma empacó el adaptador para las bombillas del patrón anterior. Cuando un ecosistema nombra su propio adaptador, ya nadie discute si la mudanza viene: llegó.

*Tres — el piso mínimo subió.* El mismo periodo marca el ajuste del minSDK a 24 en el núcleo común: las bombillas nuevas piden Android 7 o superior como piso. Coherente con el ciclo del sistema — y con la puerta 03 de esta lista, donde el mundo certificado también camina hacia pisos más altos.

Tercera pieza que pocos nombran y esta casa sí: el estante «cursed» (contenido adulto) de la misma familia sigue con actividad de este mes. Se nombra porque existe y se actualiza — con el mismo tratamiento de siempre: nombre sí, índice no, contenido de cada quien y de su jurisdicción.

───────────────────

📙 LOS DEMÁS ALMACENES VIVOS

*cuong-tran/manga-repo — el independiente más activo.* ★451, último empuje el 21-sep-2026 (hace un día): recuento de volúmenes añadido a una fuente multi-idioma. La semana pasada arregló un fallo de credenciales expiradas en otra fuente. Y un detalle fino que enseña cómo migran las casas en este ecosistema: su propio README avisa que la receta de instalación se mantiene siempre bajo la dirección de «yuzono/manga-repo», sin importar dónde viva el repositorio real. La bodega se movió de esquina, pero el anuncio de la calle no cambió — lección práctica: si tu receta deja de funcionar algún día, es probable que la esquina haya cambiado de nombre, no que la mercancía haya desaparecido.

*La segunda bodega de contenido adulto* — activa con empuje del 3-ago. Mismo tratamiento: nombre sí, índice no.

*El ecosistema chino, en dos piezas.* Una megacolección de fuentes centradas en el ecosistema copymanga (su rama comunitaria marcaba versión v1.4.85 al 8-sep, con su «vomic» paralelo del 4-sep), y una súper-colección general que junta libros, imágenes y reglas de varias familias. Se mapean como parte del mundo — lo que cada contenedor trae dentro no se receta; su comunidad se organiza por sus propios grupos y su propio idioma.

*La capa servidor, en dos casas.* Una: la extensión del ecosistema para Suwayomi — el servidor de escritorio donde tu biblioteca corre en la PC y se lee desde el navegador — con empuje del 12-sep. Dos: uchiyomi, el recién llegado self-hosted (MPL-2.0) que funciona como app web en el navegador, webtoon-first y pensado para OLED, comiendo las mismas extensiones de Mihon/Tachiyomi; publicó dos versiones el 14-sep (v0.32.0 y v0.33.0 — dato de su día). La biblioteca dejó de ser solo del bolsillo: también vive en el cuarto de cómputo.

*Los históricos que ya solo son historia.* El almacén archivado del árbol madre (ene-2024) y el repo archivado de una gran fuente copymanga (feb-2024) siguen en línea como museo: se pueden mirar, ya no se siembra. Su valor es de referencia histórica — y de lección: la página viva y el proyecto muerto a veces llevan el mismo disfraz; la fecha de último empuje es el carnet.

───────────────────

🧬 DE KEISOURCE 1.6 A LIB 16: LA CONVENCIÓN QUE MANDA

Las extensiones no son archivos sueltos: siguen una convención técnica de la casa de los parsers. Hasta hace poco la regla citada era KeiSource con librería 1.6 (la base antigua, HttpSource 1.4, ya era legado). Hoy los commits de los dos árboles grandes nombran otra cosa: lib 16 — y la familia Yūzōnō empacó encima su capa LegacySource para no ahogar a las fuentes viejas.

¿Qué cambia para quien solo lee? Dos cosas concretas:

*La falla típica se diagnostica sola.* Cuando una app «no ve» las extensiones nuevas, o las ve «obsoletas», casi siempre es esto: la app es vieja para la convención que el almacén ya adoptó. La lámpara no cambió de cuarto: cambió el patrón del enchufe — y el adaptador se consigue actualizando la app desde su casa, nunca instalando «el almacén compatible» de la feria.

*El caso histórico que selló la transición sigue enseñando.* El PR #448 de Animetail — «resolver carga de extensiones 1.6+» — mostró en su día el precio de no migrar a tiempo: un lector entero fuera de los almacenes nuevos hasta que su casa ajustó el enchufe. Hoy la lección se actualiza sola: los lectores que no migren a lib 16 vivirán la misma escena. Por eso esta serie de guías insiste en una costumbre simple: cuando el almacén dice «obsoleto», primero se actualiza la lámpara — y solo después, si sigue sin encender, se sospecha de la bodega.

Y una aclaración de honestidad técnica, porque la vara marca la diferencia: la conversación documental entre «KeiSource 1.6» y «lib 16» se lee en los commits y guías de contribución de los árboles, no en un papel de diseño central — este ecosistema documenta en la marcha. Lo que aquí se afirma es lo que el historial público muestra hoy, con nombre de commit y fecha.

───────────────────

🗂️ MIYOMI: EL DIRECTORIO QUE AHORA TIENE ORG Y MARCA PROPIA

El directorio comunitario que cataloga apps, almacenes y guías del ecosistema entero. Novedades de fondo desde la madre de esta pieza:

Primera — cambio de casa legal: el repositorio migró su titularidad a una organización propia, visible en el propio historial («changed repo owner», jun-2026) y hoy se lee bajo esa org. Segunda — cambio de licencia y de marca: pasó de Apache-2.0 a AGPL-3.0 con una cláusula de marca registrada añadida el 30-jun-2026, pidiendo que los forks y clones alojados no usen el nombre «Miyomi» para presentarse. Tercera — la placa de hoy: 188 estrellas, último empuje el 31-ago (moderación y estados limpios del panel de administración) — vivo, con ritmo más lento que los almacenes porque su trabajo es de vitrina y de catálogo, no de paquetería diaria.

Lo que no cambió y sigue mandando: el proyecto declara que no aloja contenido y que no garantiza la seguridad ni la legalidad de lo que cataloga. Esa frase es justamente lo que lo hace útil si se lee bien: Miyomi es el cartel del mercado, no el inspector del mercado. «Aprobado» en su vitrina significa «está en su catálogo hoy» — no significa aval de nadie, y la diferencia entre esas dos frases es toda la defensa que el usuario necesita contra la cadena de WhatsApp.

───────────────────

🎭 LA FERIA DE LOS IMPOSTORES

Toda bodega exitosa tiene su feria al frente. La búsqueda de la semana pasada dejó documentada una camada de repos con el mismo traje, y el patrón se repite tanto que ya merece catálogo propio:

```
EL TRAJE DEL IMPOSTOR — cuatro botones de la funda

1. Estrellas gemelas. Varios repos «distintos» con
   números idénticos entre sí (115–120 en la camada
   documentada): las estrellas se compran por lote.
2. Historial de ayer. Nacieron todos el mismo día
   (13-sep en aquella camada), sin meses de empujes
   detrás. Una bodega tiene raíces; el toldo, no.
3. Título de anuncio. «Best Manga Reader App 2026»,
   «Top Open Source Alternative», «Ultimate Hub».
   Los proyectos verdaderos tienen nombres de proyecto;
   la propaganda tiene promesas.
4. Hijo del nombre famoso. Toman el nombre de un
   almacén conocido y le cuelgan una palabra de venta —
   de ahí viene justamente la segunda defensa: las
   direcciones buenas se confirman desde la casa, no
   desde el buscador.
```

Lo que venden esos toldos no es mercancía: es el clic — y en el peor caso, la instalación envenenada bajo disfraz de extensión. El barrio ya tiene su refrán para esto, y esta familia de guías lo cuelga en la puerta: si el título suena a televisión de madrugada y las estrellas no cuadran con la historia, no se abre, no se enlaza, no se instala.

Una práctica que termina de sellar la casa: la dirección oficial de cada almacén se toma de la guía oficial del proyecto (la casa Keiyoushi publica la suya; la casa Yūzōnō, la suya), y de más nadie. Ni de este post, ni de ninguno — por eso aquí van enlaces a las casas y no pegamos recetas.

───────────────────

🧭 LAS CINCO PREGUNTAS ANTES DE ABRIR UN ALMACÉN

El filtro de la casa para mirar cualquier bodega nueva — cinco preguntas en orden, y en dos minutos:

```
1. ¿Quién lo mantiene?
   Un bot de una organización con historial público
   pesa más que una cuenta sin cara nacida este mes.

2. ¿Desde cuándo empuja?
   Meses o años de empujes visibles valen más que una
   semana de actividad. La fecha del último commit es
   el carnet: bodega viva = camión reciente.

3. ¿El código está a la vista?
   Código publicado (extensions-source y parientes)
   pasa la vara; «solo binarios», no la pasa — se
   registra como incógnita, no como confianza.

4. ¿Su sitio confiesa sus límites?
   Keiyoushi avisa qué apps ya no soporta y pone
   la solución al lado. Quien confiesa límites vende
   más verdad que quien promete infinito.

5. ¿La instalación sale de la casa?
   El índice se lee en el README del proyecto,
   nunca en posts de terceros. Ni en este. Si la
   receta vino por cadena, la cadena es el truco.
```

Anexo obvio pero necesario: «sale en el directorio Miyomi» no es respuesta a ninguna de las cinco — es la entrada al mercado, no el examen del tendero.

───────────────────

📚 SOLUCIÓN DE PROBLEMAS DEL ALMACÉN (CUATRO TRANCAS)

*Tranca 1 — «Mi lista de extensiones apareció vacía / todo obsoleto.»* El síntoma clásico del ecosistema nuevo: la app es vieja para la convención del almacén. Medicina en orden: (a) abre el aviso del sitio oficial del almacén — Keiyoushi avisa que soporta Mihon, TachiyomiSY y Komikku; (b) actualiza tu app desde su propia casa (su repo o su tienda legal, nunca un «paquete compatible» de la feria); (c) borra y vuelve a añadir la fuente del almacén desde la guía oficial. Si sigue vacío después de actualizar, entonces sí escribe al mantenedor.

*Tranca 2 — «Una fuente concreta dejó de funcionar, las demás bien.»* El almacén está sano; una bombilla se quemó. Periodistas del barrio (esta semana: credenciales expiradas corregidas en manga-repo, recuento añadido a otra fuente) muestran que estas averías se reparan en días — el mantenedor la arregla cuando alguien la reporta bien. Medicina: espera unos días y ACTUALIZA la extensión (se actualizan como las apps); si persiste, repórtala en el repo del código con versión de app, nombre de fuente, pasos para reproducir y captura — los mantenedores responden mejor a pasos que a quejas.

*Tranca 3 — «Añadí el almacén y no aparece nada para instalar.»* Orden de revisión: papel bien copiado (la receta es un texto largo que se rompe con un espacio); red funcionando (los almacenes se leen en vivo); versión de app al día; y una sola vez más — paciencia con el conteo, porque el índice se descarga completo la primera vez. Todo check y sigue: limpia caché de la app o empieza de cero el procedimiento desde la guía oficial — raras veces el fallo es del almacén.

*Tranca 4 — «Me llegó por grupo un almacén nuevo y mejor.»* No es tranca técnica: es tranca de barrio. Corre las cinco preguntas antes de tocar nada — y si el remitente no puede nombrar el repo del código, su Discord oficial o su mantenedor, la respuesta educada es «gracias, ya tengo bodega». La lámpara se compra donde se compra la luz.

───────────────────

🧪 CASOS PRÁCTICOS DEL BARRIO

*Caso 1 — La que actualizó tarde.* Carlitos usa un lector de la familia desde 2025 y esta semana se le vació la lista: todo «obsoleto». Lloró al grupo pidiendo «el nuevo almacén que sirva», y tres personas le pasaron tres enlaces distintos. El arreglo real no vino de ninguno: vino de la página oficial del almacén, que decía «Outdated app = tu app no es compatible; actualízala». Actualizó desde la casa, re-añadió la fuente oficial, y volvió todo. Lección contada al grupo entero: el almacén casi nunca se rompe — la lámpara envejece.

*Caso 2 — El curioso de la feria.* Joandry encontró un «Ultimate Multilanguage Hub» con ciento y pico de estrellas y abrió la página: nació hace dos días, cero código publicado, dirección de receta que no cuadra con ninguna casa conocida. Cerró la pestaña y se lo contó a su primo antes de que el primo instalara. No hubo daño porque no hubo clic. La feria vende miedo gratis; la cerrazón también es gratis.

*Caso 3 — La que quiso servidor de verdad.* Milka quería su biblioteca manga en la PC de la casa, no solo en el teléfono. Descubrió la capa servidor: el almacén de la familia Suwayomi para escritorio, y el recién llegado uchiyomi corriendo como app web comiendo las mismas extensiones de Mihon. No cambió de almacén ni de convención: cambió de mueble. La lámpara grande del cuarto de cómputo usa las mismas bombillas.

*Caso 4 — El que reportó bien.* Ambiorix encontró una fuente concreta que no cargaba desde el lunes. En vez de abandonar el almacén (la tranca 1 al revés), escribió al repo del código: versión de la app, nombre de la fuente, pasos exactos, captura. A los tres días el mantenedor respondió con el arreglo puesto en un commit. No cambió de bodega: hizo que la bodega mejorara para todos. El almacén libre vive de esos reportes — son su pila.

Los cuatro casos comparten la espina de esta puerta: la herramienta libre premia al que mira primero la casa y al que reporta después. La feria solo premia al que mira sin prisa — es decir, al que no compra.

───────────────────

🧯 MITOS DE LA BOMBILLA (CUATRO APAGONES)

*Apagón 1 — «Keiyoushi es el almacén oficial de Tachiyomi.»* No: el almacén oficial original archivó en enero de 2024 con su árbol madre. Keiyoushi es el almacén DE REFERENCIA del árbol Mihon — comunidad organizada, no «oficial» de ninguna empresa. La distinción importa: nadie te garantiza nada; un colectivo te muestra su trabajo — y esa es tu garantía.

*Apagón 2 — «Más estrellas = más seguro.»* La camada de impostores documentada esta semana compró sus estrellas en lote y por eso las replicaba en varios repos. Las estrellas cuentan congregación, no higiene. La vara de verdad: mantenedor, historial, código a la vista, límites confesados. Las cuatro, o ninguna.

*Apagón 3 — «Las extensiones de Mihon sirven en cualquier lector de la lista.»* No: cada árbol tiene su protocolo de parsers. Las extensiones del árbol Mihon/Keiyoushi no se instalan en los lectores de otros árboles (Usagi, Kotatsu y los suyos), que tienen sus propias casas — y su propia guía en esta serie. La bombilla de la bodega equivocada no quema: ni siquiera entra.

*Apagón 4 — «Si está en Miyomi está verificado.»* Miyomi se declara a sí mismo: no aloja, no garantiza, no audita. Catalogar es mostrar vitrinas; verificar es otra profesión. Usa el directorio como lo que es — el mejor cartel del mercado — y no como sello de seguridad.

───────────────────

❓ PREGUNTAS FRECUENTES

*¿Qué almacén uso con Mihon?* Keiyoushi: lo declara su propio sitio (Mihon, TachiyomiSY, Komikku). Si tu lista sale vacía con «Outdated app», el problema es la versión de tu app, no la bodega.

*¿Y para anime?* El canal vivo es Yūzōnō anime-extensions: su historial de hoy tiene apenas tres horas. El almacén oficial del ecosistema Aniyomi archivó en agosto de 2024 y su otra casa de código (Kohi-den) en mayo de 2026 — la dirección vieja ya solo es museo.

*¿Los estantes «cursed» son peligrosos?* El mecanismo es el mismo que cualquier otro almacén; el riesgo vive en el contenido y en tu jurisdicción. Se nombran para completar el mapa; el índice de instalación no se pega en esta familia de guías, para ninguno.

*¿Puedo usar varios almacenes a la vez?* Sí: la app convive con varios índices. La regla sana es la del presupuesto de confianza: cada almacén extra aumenta la superficie que vigilar. Dos bodegas bien miradas valen más que cinco sin mirar.

*¿Cada cuánto se actualizan las extensiones?* Los almacenes vivos publican varias veces por semana (el bot de Keiyoushi, a diario). La app las ofrece como actualizaciones de extensiones — aceptarlas es el mantenimiento del barrio entero.

*¿Por qué mi receta vieja dejó de funcionar?* Tres causas usuales: la casa migró de dirección (caso documentado hoy: manga-repo vive con la receta bajo el nombre de la familia Yūzōnō), el almacén cambió de maquinaria (Keiyoushi pasó a releases en agosto), o la app envejeció para la convención nueva. Siempre se mira en la casa antes de re-copiar nada.

*¿Sirven estas extensiones en Usagi o Kotatsu?* No: esos lectores tienen sus propios árboles de parsers; pieza aparte en esta serie. Mezclar árboles es la confusión número uno del barrio.

*¿Qué pasa si mi lector desaparece de la tienda?* Nada que afecte a los almacenes: viven en sus repos, no en tiendas. La puerta 03 de esta serie explica el censo por venir — pero tu biblioteca no depende de ninguna tienda para seguir siendo tuya.

*Las extensiones de mi teléfono viejo pasan al nuevo* — sí, si migras la biblioteca con la herramienta de respaldo del propio lector. Los almacenes no se migran: se vuelven a añadir desde sus casas (y es la ocasión sana de borrar los que ya no usas).

*¿Dónde reporto una extensión rota?* En el repo del código de la extensión, con versión de app, fuente, pasos y captura. Para Keiyoushi, su apartado de issues del repo hermano. Reportes buenos = arreglos rápidos; ya se vio esta semana.

*¿Qué es eso de «release-based» en Keiyoushi?* Su nueva maquinaria de distribución desde el 13-ago-2026: los índices y activos se publican como lanzamientos. Para ti: el add-repo de su sitio sigue siendo tu única puerta necesaria.

*¿Y si mañana cae el almacén grande?* El ecosistema ya demostró que sobrevive a eso (invierno de 2024): la comunidad se organiza en torno al código, y el código vive en forks. Tu plan personal: saber usar las cinco preguntas de esta guía, guardar tu respaldo de biblioteca y no traficar calma.

───────────────────

📖 GLOSARIO DEL TEMA (dieciséis términos)

*App.* Tu lector: la lámpara. No trae contenido, trae motor.

*Extensión.* La adaptadora: una bombilla por fuente. Se instala por almacén, se actualiza como app.

*Almacén (repo-de-extensiones).* La bodega con dueño e historial donde viven las extensiones. El mapa de esta guía.

*Índice.* La receta técnica — una dirección de archivo de recuento — con la que la app descubre un almacén. En esta familia de guías: se señala la casa, no se pega la receta.

*Fuente.* El contenido al que una extensión lee — el cuarto al que tu bombilla da luz. Cada fuente tiene su propia vida y sus averías.

*Hub.* El almacén de referencia del árbol Mihon (hoy, Keiyoushi): el mercado central de las bombillas.

*Bot del almacén.* El camión automático que actualiza el índice a diario (keiyoushi-bot, empuje de hoy). Su existencia es la mejor señal de vida que puede tener una bodega.

*extensions-source.* El repositorio hermano con el CÓDIGO de las extensiones. Donde se arreglan las bombillas — y donde se reporta.

*Convención / librería (lib).* El patrón técnico con que se construyen las extensiones. Era KeiSource 1.6 en su papel; hoy los commits nombran la «lib 16» como el patrón vigente.

*LegacySource.* El adaptador publicado por la casa Yūzōnō para que fuentes del patrón anterior sigan respirando en la era lib 16.

*«Outdated app».* El aviso de los almacenes cuando tu lector ya no entiende la convención nueva. Solución: actualizar la app, nunca buscar espejos.

*Repositorio basado en releases («release-based»).* La maquinaria nueva del hub desde el 13-ago-2026: publicación por lanzamientos con activos. Invisible para ti si no vas al sótano.

*Fork.* Proyecto hijo de otro. En extensiones: los lectores forkean a los lectores; los almacenes, casi siempre, se heredan.

*Estante «cursed».* El rincón de contenido adulto de algunas familias de almacenes. Existe; se nombra con la misma regla de siempre: índice no, jurisdicción de cada quien.

*Suwayomi / uchiyomi.* La capa servidor: tu biblioteca corriendo en PC o como web-app, comiendo las mismas bombillas del ecosistema. Otra habitación del mismo edificio.

*Directorio (Miyomi).* El cartel del mercado: catálogo de apps, almacenes y guías. Declara que no audita. Usar como cartel, no como sello.

───────────────────

📋 RADIOGRAFÍA DEL MAPA ACTUAL (lo medido hoy, con su hora)

Censo del barrio tomado esta mañana, leyendo cada casa en su propia página. Lo que no se contó hoy lleva su fecha anterior marcada — la regla de la casa sobre números:

```
ALMACÉN O CASA             SEÑAL VIVA HOY            PLACA
Keiyoushi (hub)            empuje del bot: 19 h      ★15.0 mil
└ Re-init release-based    hecho: 13-ago-2026        —
Keiyoushi (código)         vivo entre semana         ★4.7 mil (15-sep)
Yūzōnō anime               empuje: hace 3 h          ★439 · 5.548 commits
└ Core injertado Keiyoushi hecho: 17-sep (#952)      —
└ Capa LegacySource        hecho: 1-sep              —
manga-repo (indepe)        empuje: 21-sep            ★451
└ Receta bajo otra casa    migrada (su README)       —
2º estante «cursed»        vivo en su rango          empuje del 3-ago
Ecosistema CN copymanga    v1.4.85 (8-sep)           ★2.7 mil (14-sep)
Suwayomi (servidor)        vivo                      empuje 12-sep (14-sep)
uchiyomi (web self-host)   v0.33.0 (14-sep)          ★37 (14-sep)
Miyomi (directorio)        empuje: 31-ago            ★188 · AGPL-3.0
MUSEO (archivados)         sin empujes               —
├ oficial árbol madre      archivado ene-2024        —
├ gran fuente copymanga    archivado feb-2024        —
├ oficial Aniyomi          archivado ago-2024        —
└ Kohi-den (código Yūzōnō) archivado may-2026        —
```

Lectura de la radiografía en una frase: cuatro casas con camión de esta semana (una de hoy), dos aprendices con mudanza técnica terminada, y un museo que conviene saber dónde queda — para no esperar en su puerta con la mercancía en la mano.

───────────────────

📖 HISTORIA CORTA: EL AÑO QUE EL ECOSISTEMA APRENDIÓ A VIVIR SIN MADRE

En enero de 2024 pasó lo que las comunidades libres no se cansan de ensayar: la casa madre del ecosistema — el almacén oficial del árbol Tachiyomi — cerró la persiana y archivó. En ese invierno el barrio aprendió su lección grande: nada de esto era «la infraestructura de alguien» — era el trabajo coordinado de muchos, esperando a que alguien más se hiciera cargo.

Lo que siguió fue manual de supervivencia comunitaria. Primero, el reparto de la herencia: el árbol vivo más fuerte (Mihon) encontró su almacén de referencia en una comunidad nueva — Keiyoushi — que no nació como empresa ni como marca: nació como tarea compartida con un bot que reparte índices todos los días. Después, el segundo hijo (el anime) encontró su casa en la familia Yūzōnō. Después, los lectores mismos empezaron a forkar unos de otros, y cada fork aprendió su propio modo de comer extensiones.

Año y medio después — la semana de hoy la enseña bien — el ecosistema ya no solo sobrevivió a la madre: se volvió más barrio que antes. Hoy se ven dos señales que no existían cuando cayó la casa original. Una, la INTEGRACIÓN entre los herederos: el árbol Yūzōnō no compite con el core de Keiyoushi — lo INJERTA en su rama y comparte plomero (#952, 17-sep). Otra, la MADUREZ técnica declarada: la nueva maquinaria del hub (releases, agosto) y la capa LegacySource (septiembre) son pasos de quien piensa en cuidar legado, no de quien corre detrás del día.

La moraleja que esta historia deja al usuario común no es heroica: es doméstica. Tu lector y sus bombillas viven del trabajo de gente organizada en su tiempo libre. La forma de cuidar el barrio no es donar estrellas — es reportar bien, actualizar tranquilo, no repartir calles, y reconocer que una bodega de voluntarios también cansa. El que aprende eso ya tiene la mitad del mapa comprado con la moneda que no se gasta: el respeto al mantenedor.

───────────────────

🎒 LA MOCHILA MÍNIMA DEL LECTOR LIBRE (lo que tu lector debería llevar)

Si esta guía tuviera que caber en una mochila, iría así — cinco piezas:

```
1. Un lector AL DÍA, descargado de su casa.
   (El «Outdated app» se previene actualizando, no
   sufriendo.)

2. Los almacenes OFICIALES de tu árbol, añadidos desde
   la guía oficial de cada casa — jamás desde un post.
   Uno o dos bastan; cada bodega extra es una bodega
   más que vigilar.

3. El respaldo de biblioteca ENCENDIDO, con fecha
   reciente, guardado fuera del teléfono (nube o PC).
   Tu catálogo vale más que cualquier lámpara.

4. Las cinco preguntas de la sección 🧭, aprendidas —
   mantenedor, historial, código, límites, casa.
   La mochila más liviana es la memoria.

5. La costumbre de la fecha: cuando un consejo llegue
   por cadena, preguntar «¿cortado cuándo?» antes de
   seguirlo. El mapa de este tema envejece por semanas;
   tu criterio, si lo cuidas, no.
```

Extra opcional para el que quiera servidor: la capa Suwayomi o uchiyomi en el cuarto de cómputo — la misma mochila, ampliada a otra habitación. Nada de esto cuesta dinero: cuesta algo mucho más fino, la costumbre de leer en la casa antes de instalar.

───────────────────

🗺️ CÓMO LEER ESTAS FUENTES SIN PERDER EL PIE (mini-guía por sitio)

*GitHub de cada almacén.* Lo primero que se mira no es el título: es la fecha del último commit (debajo del botón verde) y la placa de estrellas. Después la pestaña de commits: una bodega sana tiene empujes con nombres de fuentes y fechas de ahora, no solo «archives». Si la rama se reinició (como la del hub en agosto), la edad real se mide en el proyecto, no en la página.

*Sitio oficial del almacén.* Donde viven las instrucciones de instalación y los avisos de compatibilidad («qué apps soporto»). Ahí se resuelven el noventa por ciento de las preguntas del barrio — antes de escribir a nadie, se lee esa página.

*Los issues del código.* El teclado del mantenedor. Leerlos antes de abrir uno nuevo enseña qué averías ya están siendo cuidadas — reportar duplicado es dejar otra caja en el pasillo del plomero.

*El directorio Miyomi.* Para descubrir alternativas cuando una bodega quede coja — leyendo su propia declaración (no audita, no garantiza), y nunca como atajo de confianza.

*Regla de sellado, como siempre:* cualquier recomendación de almacén que llegue por cadena se contrasta con la casa oficial esa misma tarde. Y los números de esta guía — estrellas, empujes, versiones — se re-cuentan antes de repetirse: el bot de hoy ya habrá empujado mañana otra vez.

───────────────────

🔎 ANATOMÍA DE UN ALMACÉN DE EXTENSIONES (qué significa cada archivo, visto hoy)

Abrir el hub hoy enseña una raíz con siete archivos. Pocas veces se explica qué hace cada uno; aquí va la placa de cada pieza, leída en la propia lista del repositorio de hoy:

```
index.json          El recuento completo en texto legible:
                    todas las extensiones, sus versiones,
                    fuentes y metadatos. La lista del tendero.

index.min.json      La misma lista, comprimida para viaje
                    rápido. Cuando la app descarga la lista,
                    suele tomar esta plaza.

index.pb            El índice en formato de máquina
                    (el de la receta que la app entiende
                    nativa). La «factura» operativa: hoy
                    trae el empuje de hace 19 horas.

repo.json           La cédula del almacén: quién es,
                    qué maquinaria usa, dónde vive. El
                    archivo que estrena identidad cada
                    vez que el almacén muda de ciclo.

release-assets.json El inventario de paquetes publicados
                    por lanzamiento (la prueba visible de
                    la era «release-based» de agosto).

icon/               La carpeta de los logos de cada
                    extensión (se actualizó por última vez
                    en la misma reinicialización).

README.md           La carta de bienvenida: cómo añadir
                    el almacén y dónde reportar. Siempre la
                    primera lectura — nunca la última.
```

Saber esta anatomía cambia un comportamiento: cuando la «receta» llega por cadena, identificas en segundos si apunta a uno de estos archivos EN LA CASA correcta — o a un archivo con nombre parecido en una casa ajena. El impostor de la feria rara vez imita la carpeta completa: imita solo el nombre.

───────────────────

🧩 LOS TRES ÁRBOLES Y SUS PROTOCOLOS (el mapa que evita la confusión número uno)

La confusión más repetida del barrio nace de no distinguir árboles. Tres familias de lectores, tres protocolos distintos de parsers, y ninguno habla con el otro:

```
ÁRBOL MIHON / KEIYOUSHI      Lengua de extensiones:
                             Android propia (la familia
                             Tachiyomi→Mihon→forks).
                             Almacenes de esta guía.

ÁRBOL USAGI / KOTATSU        Otro protocolo de parsers
                             (su propia casa de sources,
                             su propio cronograma, su
                             propia guía futura en esta
                             serie).

LA CAPA SERVIDOR             Suwayomi y uchiyomi comen
                             el PRIMER árbol (por eso
                             conviven en esta pieza),
                             pero el servidor es otra
                             habitación: PC o web-app,
                             no teléfono directo.
```

La bombilla no miente: si no entra, es de otro árbol. Descargar «cualquier APK de extensión» de cualquier bodega no da más fuentes: da riesgo — porque el archivo que no encaja en tu lámpara suele encajar otro propósito. Regla casera de una línea: identifica tu ÁRBOL primero (¿qué lector tengo?), su almacén oficial después, y todo lo demás nunca.

───────────────────

🎙️ SEÑALES DE LA SEMANA (lo que el historial contó hoy)

El barrio habla por sus commits. Aquí van seis mensajes reales leídos hoy esta misma mañana, con su hora o su fecha:

*«Update extensions repo» — keiyoushi-bot, hace 19 horas.* El camión del hub pasó esta madrugada. Nada extraordinario — y justamente por eso es noticia de fondo: la bodega más grande del ecosistema sigue abriendo todos los días sin anuncio.

*PR #984 integrado, hace 3 horas — Yūzōnō.* Una fuente de anime nueva entra al almacén vivo esta tarde. La periferia no para de mandar mercancía.

*«Keiyoushi Network Import (Core)» — 17-sep.* Las dos casas grandes comparten plomería desde esta semana: es el evento técnico del mes en estos árboles, y pasó sin un solo titular.

*«LegacySource para compatibilidad lib-16» — 1-sep.* La casa publicó el adaptador antes de que la mudanza doliera. Mantener así, enseña el barrio, se hace con tiempo y sin ruido.

*Recuento de volúmenes integrado — 21-sep, manga-repo.* El independiente activo sumando detalle a fuentes multi-idioma — trabajo silencioso que el lector solo nota porque un día su ficha lee más completa.

*PR #448 «resolve 1.6+ extension loading» — Animetail.* El caso histórico que sigue dando clases: quien no migra la cadena, pierde los almacenes. Se cita aquí porque la lección se repite con cada convención nueva.

───────────────────

🧠 «EL ÍNDICE NO SE PEGA» — LA REGLA EXPLICADA SIN MISTERIO

Esta familia de guías insiste tanto en no pegar recetas que merece una sección que explique el porqué con lógica de barrio. Cuatro razones:

*Uno — la versión envenenada llega por el mismo canal.* Si tú aprendiste a instalar almacenes pegando textos de posts, el impostor no necesita hackear nada: necesita un post bonito. La regla desactiva ese canal entero: si siempre instalas desde la casa, nadie puede colarte su casa falsa.

*Dos — la receta cambia de esquina.* La evidencia de hoy: manga-repo cambió la dirección de su receta sin cambiar de producto; el hub cambió de maquinaria en agosto. La receta de tu post del año pasado hoy puede ser letra muerta — o peor: re-usada por alguien más. La casa actualiza; el post no.

*Tres — pegar no enseña a pescar.* Cada instalación por receta ajena deja al usuario igual de dependiente; cada instalación desde la casa oficial lo deja un poco más dueño del barrio. Esta guía vende autonomía, no atajos.

*Cuatro — el escudo es barato.* Ir a la casa cuesta un clic extra frente a pegar. Comparado con el costo de una extensión envenenada — tu sesión de lectura, tus cuentas, tu teléfono — el clic es la ganga del siglo.

Por eso aquí van enlaces a las casas y jamás la receta. La casa dice: lee las llaves adentro, con la luz encendida.

───────────────────

🆕 QUÉ TRAE NUEVA ESTA EDICIÓN (contra la madre del 15-sep)

*Uno — el censo rehecho de hoy:* hub empujando hoy (bot, 19 h), Yūzōnō hace 3 horas, manga-repo ayer, con placas actualizadas (★15.0 mil · 439 · 451). La madre decía «push del 14-sep» como novedad; hoy la novedad es el pulso de las últimas tres horas.

*Dos — la mudanza de agosto documentada:* el hub pasó a almacén basado en releases el 13-ago-2026, con la anatomía completa de sus siete archivos explicada. La madre no conocía ese ciclo: se quedaba en el antes; esta guía nombra el después.

*Tres — la era lib 16:* la convención citada como «KeiSource 1.6» vive hoy en los commits como «lib 16», y la casa publicó su capa LegacySource el 1-sep. Vieja foto del papel, nueva foto del historial; el detalle fino se dice fino.

*Cuatro — las migraciones de los independientes:* manga-repo vive con su receta bajo la dirección de la familia Yūzōnō (dicho por su propio README), y Miyomi ya tiene org propia y licencia AGPL-3.0 con política de marca (junio-julio).

*Cinco — el injerto del mes:* el core de Keiyoushi dentro del árbol Yūzōnō (#952, 17-sep). Dos casas compartiendo plomero: la noticia estructural del otoño de este ecosistema, aquí explicada con calma dominicana.

*Seis — secciones nuevas de oficio:* radiografía medida, historia corta del año sin madre, la mochila del lector, el árbol de los tres protocolos, la anatomía del almacén, la regla del índice explicada de verdad, las señales de la semana y la camada de impostores convertida en catálogo de traje. La madre era noticia; esta es manual.

───────────────────

⏱️ UN DÍA CON EL BOT: CÓMO SE COCINA EL ÍNDICE (reconstrucción desde la evidencia pública)

¿Cómo llega una bombilla reparada desde el taller del mantenedor hasta tu teléfono? El proceso no está descrito en un manual central — este ecosistema documenta en la marcha —, pero las piezas públicas lo cuentan entero; aquí se reconstruye solo con lo que se ve hoy, y se marca como reconstrucción:

```
El taller   Alguien arregla una fuente en el repo del
            CÓDIGO (extensions-source o su hermano):
            un commit con nombre de fuente, fecha y
            razón («fix expired credentials», de esta
            misma semana).

La cocina   El sistema de construcción del proyecto
            (sus workflows públicos de CI, visibles en
            el badge de la portada del hub) compila
            esa fuente en su bombilla — el ejecutable
            de la extensión.

El reparto  El bot del almacén — keiyoushi-bot, con
            su empuje-de-cada-día— vuelca lo cocinado
            al índice y a los activos de release (la
            maquinaria nueva de agosto), con el nombre
            de commit de siempre: «Update extensions
            repo».

Tu casa     La app, al abrir, re-lee el índice vigente,
            detecta que tu bombilla habitual tiene
            número nuevo y te ofrece la actualización
            como una actualización más — sin anuncio,
            sin ruido.
```

La moraleja operativa de esta cocina: todo el trayecto — arreglo, compilación, reparto, entrega — se hace TODOS los días sin que nadie reciba aplauso. Por eso, cuando la bombilla se quema de nuevo (y todas se queman algún día), la respuesta del barrio no es irse a la feria: es caminar al taller y escribir el reporte como manda el caso 4.

───────────────────

🏪 DÓNDE INSTALAR TU LECTOR SIN SUSTOS (la lista legal corta)

Paradójicamente, la pregunta más repetida del barrio tiene la respuesta más corta: el lector se instala SOLO desde su casa. Con fecha de hoy, las casas de este árbol son:

```
LA LÁMPARA
Mihon       su repositorio oficial de GitHub, con sus
            releases firmadas por la casa. (La app no
            vive en tiendas de Google ni de nadie.)
Komikku     igual: su casa publica sus releases; F-Droid
            como canal libre adicional.
TachiyomiSY su casa propia de fork — con su propio
            nombre, su propia clave, su propio aviso
            de pariente.

LAS BODEGAS
Keiyoushi   solo desde su sitio oficial y su guía
            «Getting started». Un toque, sin receta
            manual si no quieres verla.
Yūzōnō      su propio sitio y su propio README.
manga-repo  su README, que te recuerda que la receta
            es la de la familia Yūzōnō aunque el repo
            lleve otro nombre.

EL DIRECTORIO
Miyomi      para mirar vitrinas, jamás para pegar
            instalaciones desde ahí.
```

Ninguno de estos pasos pasa por letreros luminosos, «APK Premium Mod Latest», ni canales de reenvío. La regla de oro del barrio, aplicable a todas las puertas de esta serie: tu teléfono se merece instalaciones de fábrica — y la fábrica siempre tiene nombre de proyecto, historial y releases firmadas.

───────────────────

🧪 UN TALLER EN SEIS PASOS: RECORRIDO PRÁCTICO POR EL HUB

Teoría sin oficio no cierra la casa. Este recorrido se hace en silencio, una vez, y queda de memoria para siempre — seis pasos contra el telón de la feria:

*Paso 1 — Identifica tu lámpara.* Abre tu lector y busca la versión exacta (en la sección de ajustes: nombre, número, fecha de instalación). Escríbela. Esa línea es tu primera defensa: sin ella no sabrás leer el aviso «qué apps soporto» de ninguna bodega.

*Paso 2 — Abre la casa, no el buscador.* Escribe la dirección del sitio oficial del almacén en el navegador — la de esta guía si quieres, o mejor: la que tú mismo anotaste la primera vez. Lo primero que miras: ¿dice qué apps soporta? ¿Cuándo fue su último aviso? Se lee la puerta antes de entrar — eso es barrio.

*Paso 3 — Añade desde la guía oficial.* Sigue el procedimiento propio del sitio (su atajo de instalación con un toque, o su sección de «añadir fuente» con la opción guiada). No pegues manualmente nada que no entiendas: la receta, si algún día hace falta, se copia DESDE la casa y se vuelve a verificar contra ella.

*Paso 4 — Espera al primer censo.* La app descarga el índice completo la primera vez; la lista puede tardar un minuto en llenarse. Si llega vacía con el cartel «Outdated app», ya tienes diagnóstico: actualiza tu lector por su casa y re-intenta. Si llega llena, instalaste bien — no toques más el botón por hoy.

*Paso 5 — Instala poco, mira mucho.* Instala solo las extensiones (bombillas) de las fuentes que realmente vas a usar — entre cinco y quince para un lector normal. Cada bombilla extra es superficie que actualizar. La bodega se queda en tu teléfono; su inventario no se muda entero.

*Paso 6 — Enciende la ronda semanal.* Una costumbre: cada fin de semana, abrir las actualizaciones de extensiones que ofrece la app, aceptarlas, y recordar el nombre de tu almacén oficial. Esa ronda de dos minutos sostiene todo el andamio del barrio — y a ti te ahorra cada drama que esta guía describe.

───────────────────

💬 FRASES QUE DELATAN AL IMPOSTOR (el catálogo rápido del toldo)

Doce frases escuchadas por el barrio esta temporada. Si dos se juntan en el mismo anuncio, no hace falta más examen — se guarda el dinero:

```
«Sirve con TODOS los lectores»          (las bombillas no son universales)
«Es el almacén OFICIAL nuevo»            (los oficiales viejos archivaron;
                                        el nuevo nació en comunidad y no se
                                        anuncia por cadena)
«Mismo código, más fuentes»              (traducción: mismo clon, otro logo)
«Premium unlocked / VIP gratis»          (no existe VIP en una bodega libre)
«Sin anuncios de por vida»               (los anuncios viven en la fuente,
                                        no en la extensión: gato por liebre)
«No necesitas registrarte aquí»          (tú nunca te registras en la bodega:
                                        la frase huele a capturar credenciales)
«Actualizado hoy»                        (¿cortado a qué hora? ¿dónde está
                                        el commit? Las estrellas gemelas mienten)
«La versión que los demás no quieren…»   (el miedo como argumento de venta:
                                        la cola es siempre la captura)
«100% seguro, verificado»                (nadie verifica así: la propia
                                        casa dice «lee el código»)
«Te envié el índice por interno»         (los índices se leen de la casa;
                                        el interno es el disfraz)
«Actívalo con este código»               (las bombillas no se activan, abren)
«Es como Keiyoushi pero mejor»           (la comparación es siempre con el
                                        grande; la bodega verdadera no se
                                        vende como «como otro, pero»)
```

Ninguna frase es delito suelta. Juntas — o en la boca de un toldo sin taller al lado — son la cotización exacta de lo que no vale tu teléfono.

───────────────────

🏛️ EL MUSEO CON SU PLACA (los archivos donde ninguna puerta abre)

Se llega al museo con respeto, porque cada archivo fue un mercado enorme en su año — y se sale sin esperar, porque ninguno abre más:

*Archivo del 16 de enero de 2024 — el almacén oficial del árbol madre.* El que enseñó a este ecosistema lo que es la consolidación comunitaria: cuando cerró, no cerró una app — apagó la plaza donde se repartían las bombillas de un continente entero de lectores. Su cierre echó al barrio a la calle por una semana; los vivos nacieron en esa semana.

*Febrero de 2024 — la gran fuente copymanga original.* El gigante del ecosistema chino que donó su protocolo a todos sus sucesores. Su archivo fue el más re-leído de la temporada en aquel lado del mundo; las ramas que hoy existen se cuentan descendientes directos.

*Agosto de 2024 — el almacén oficial del árbol Aniyomi.* El día que el anime se quedó sin casa propia — y el empuje definitivo para que la familia Yūzōnō levantara la suya. Su archivo hizo de partida de nacimiento del canal que hoy empuja hace tres horas.

*Mayo de 2026 — Kohi-den, la primera casa de código del árbol Yūzōnō.* Aquí la lección es más fina: archivar puede ser MADUREZ, no muerte. Kohi-den cerró cuando su familia terminó su mudanza a un lugar más grande — archivó con la obra terminada, como quien cuelga el uniforme después del turno.

El museo se recorre para dos cosas: para no repetir la espera delante de su puerta (nadie abre allí), y para recordar que todo lo vivo de esta guía también será archivo un día. La pregunta del barrio no es «¿cuánto durará mi almacén?» — es «¿estaré mirando bien mientras dure?».

───────────────────

📌 LO QUE ESTE MAPA NO DICE (límites honestos de la pieza)

Toda guía de la casa cierra declarando su techo, y esta no es excepción:

*Este mapa no nombra fuentes de contenido.* Las extensiones se cuentan como mecanismo; los sitios que cada bombilla lee son asunto de cada lector y de su jurisdicción. Esta familia de guías se queda en la lámpara, la bodega y la bombilla — nunca en el cuarto ajeno.

*No sustituye la casa oficial.* Todo procedimiento aquí descrito (añadir, actualizar, reportar) tiene su versión autorizada en el sitio del proyecto. Si una línea de esta guía algún día contradice la casa, la casa gana — y se re-verifica el mapa esa misma tarde.

*No aplica a todos los árboles.* El árbol Usagi/Kotatsu y los ecosistemas de Apple viven otra gramática de parsers (y otras reglas, y otros riesgos). Todo lo de esta pieza aplica al árbol Mihon y su capa servidor — lo dice el título y lo repite cada capítulo.

*No presume eternidad.* La placa del hub de hoy (★15.0 mil, bot con empuje a las 19 horas) tiene ya veinticuatro horas de vieja cuando tú la leas mañana. La vara está puesta: re-contar antes de repetir. Esa es toda la honestidad posible en un tema que empuja a diario.

Y lo que este mapa sí persigue: que instalado tu almacén como manda la guía oficial, nunca más en tu historia de lector vuelvas a depender de un post — ni siquiera de este.

───────────────────

😄 EL MEME DE LA PIEZA

Original de la casa, de este mismo horno — del tema, con el lector, contra nadie:

```
LA BOMBILLA DE LA FERIA

— Tengo la bombilla UNIVERSAL que sirve pa' todos
  los enchufes, joven. Nueva en caja, recién llegada.
— ¿Y eso que la caja no tiene marca?
— Es que es tan buena que no necesita.
— ¿Y tiene año de fabricación?
— No pregunte tanto, que se espanta el descuento.
— Gracias, hermano, es que con mi lámpara se
  espantan hasta los que venden sin recibo.
— ¡Oye! ¿Y pa' quién tú me tomas?
— Pa' un vendedor sin recibo. Eso fue lo primero
  que me enseñaron en el mercado.
```

El chiste defiende su tema: el impostor no teme tus preguntas técnicas — teme las cuatro de siempre: quién eres, desde cuándo, a ver tu taller, y por qué sin recibo. La lámpara se enciende sola cuando la bombilla llega con papeles.

───────────────────

🛠️ MÉTODO DE LA CASA (cómo se horneó esta pieza, fechado)

*Paso uno — la madre re-leída.* Se leyó completa la guía del 15-sep (11.257 c) y se marcó su inventario de caducables: nueve almacenes en placa, tres archivos de museo, la convención citada, la camada de impostores, las reglas de lectura. Todo lo mundano (estrellas, empujes) fue a re-contarse hoy; todo lo estructural (re-init, migraciones, licencia) fue a confirmarse en su historial.

*Paso dos — verificación viva de hoy.* Abiertos hoy, 22-sep-2026: el hub Keiyoushi (bot hace 19 h, raíz de siete archivos, re-init ago-13 visible, placa 15.0 mil), Yūzōnō anime (commit hace 3 h, placa 439, 5.548 commits, el injerto #952 del 17-sep, la capa Legacy del 1-sep, los bumps lib 16 recientes), manga-repo (☆451, empuje del 21-sep, y el README que instruye conservar la receta bajo la dirección yuzono/manga-repo), y Miyomi (☆188, org «miyomiorg», licencia AGPL-3.0 con cláusula de marca, último empuje 31-ago). Las placas no re-contadas hoy llevan su fecha al lado, a la vista: código Keiyoushi (★4,7 mil al 15-sep), Copymanga-CN (v1.4.85 al 8-sep), uchiyomi (v0.33.0 al 14-sep), segundo estante adulto (3-ago), Suwayomi (12-sep).

*Paso tres — lo no comprobado, dicho tal cual.* La conversación «KeiSource 1.6 → lib 16» se describe desde commits y mensajes de PR públicos; no existe papel de diseño central que la anuncie — y así se dijo en la sección de la convención. El recuento preciso de fuentes del hub no se re-contó (vive en el índice, se cita desde la madre como «más de mil», marcada a su fecha). Los canales CN no se re-abrieron hoy (actividad de hace unos días basta para el mapa; se marcan).

*Paso cuatro — la vara.* Conteo con len() sobre este texto nativo, revisión de orillas (cero dobles estrellas impresas, cero pipes), anatomía D-004 completa (semilla, mapa, mapa mental, meme original, nota, firma, tags), y registro del conteo en el acta viva del día.

*Paso cinco — la humildad del barrio.* Este tema envejece por semanas: bots empujan a diario, convenciones migran por meses, almacenes mudan por sorpresa. La vara de re-lectura queda fijada en la sección de lectura de fuentes: todo número aquí se re-cuenta antes de repetirse. La pieza dirá la verdad de hoy — mañana la de mañana.

───────────────────

🔗 ENLACES (abiertos hoy, 22-sep-2026)

*El hub y su código:*
• Almacén — https://github.com/keiyoushi/extensions
• Código — https://github.com/keiyoushi/extensions-source
• Sitio / añadir — https://keiyoushi.github.io

*Anime y familia Yūzōnō:*
• Anime extensions — https://github.com/yuzono/anime-extensions
• Sitio — https://yuzono.github.io
• Estante adulto de la familia (nombre sí, índice no) — https://github.com/yuzono/cursed-manga-extensions

*Independientes y segundas bodegas:*
• manga-repo — https://github.com/cuong-tran/manga-repo
• Segundo estante adulto (mismo tratamiento) — https://github.com/mojuru/cursed-manga-repo

*Ecosistema chino (mapa, sin receta):*
• Rama comunitaria copymanga — https://github.com/LittleSurvival/copymanga-copy20
• Megacolección — https://github.com/ZGQ-inc/source

*Capa servidor:*
• Suwayomi (extensión) — https://github.com/Suwayomi/tachiyomi-extension
• uchiyomi — su repo self-hosted (buscar en su casa del 14-sep; dato marcado a su fecha)

*Directorio del mercado:*
• Miyomi — https://miyomi.app · código: https://github.com/miyomiorg/Miyomi

───────────────────

📝 NOTA DE VERIFICACIÓN (22-sep-2026)

Abiertos hoy y leídos en su propia página: el almacén Keiyoushi, el repositorio de anime Yūzōnō, manga-repo y Miyomi. De ellos salen: el empuje del bot de hoy, la re-inicialización release-based del 13-ago-2026, el commit de hace 3 h de Yūzōnō, el injerto del core del 17-sep (#952), la capa LegacySource del 1-sep, los commits «lib 16» de la semana, la migración de la receta de manga-repo declarada en su README, y la mudanza de Miyomi a org + AGPL-3.0. Placas re-contadas hoy: ★15.0 mil, 439, 451, 188. Placas citadas a su fecha (no re-contadas hoy): código Keiyoushi ★4,7 mil (15-sep), Copymanga-CN v1.4.85 (8-sep), uchiyomi v0.33.0 (14-sep), Suwayomi (12-sep), segundo estante adulto (3-ago), ZGQ (★1,2 mil, 14-sep). Los datos de museo (ene/feb/ago-2024, may-2026) son fechas históricas constadas en sus días. Todo número sin fuente de hoy lleva su fecha al lado; nada sale de la memoria.

───────────────────

✍️ FIRMA Y DESPEDIDA

Pieza 04 de La Bandita, edición dominicano-español, verificada con la vara de la casa el 22 de septiembre de 2026. Esta completa cerró dentro de su banda (WhatsApp, 62 000–64 000 caracteres) — el número exacto, en el registro vivo del día.

El vecindario de las bombillas no tiene alcalde: tiene bodegas con camión puntuando cada mañana y una feria que siempre intentará parecerse al mercado. Tu criterio es el recibo. Actualiza tranquilo, reporta bien, y nunca instales lo que venga sin casa.

Busca más, y que la bombilla te llegue con papeles. 💡

> «La Bandita informa a partir de fuentes fechadas. Las bodegas abren cada día; la vara también.»

───────────────────

#LaBandita #ExtensionesMihon #Keiyoushi #MangaYAnime #LectorAndroid #KeiSourceLib16 #GitHubDeConfianza #VerificaAntesDeInstalar #EcosistemaLibre #FuenteFechada #SoftwareLibre #RepublicaDominicana
