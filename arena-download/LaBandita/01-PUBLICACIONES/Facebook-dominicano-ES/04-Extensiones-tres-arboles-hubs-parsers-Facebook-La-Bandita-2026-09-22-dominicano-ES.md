DÓNDE VIVEN LAS FUENTES DE TU LECTOR: EL MAPA COMPLETO DE LOS ALMACENES DE EXTENSIONES

Guía profunda de La Bandita sobre los árboles de parsers por fuentes abiertas, los almacenes vivos que los reparten, la feria de impostores que los imita y la regla que protege tu teléfono — todo verificado esta mañana sobre las propias casas.

🌱 LA SEMILLA

Dominicana practicona, otra vez. Yo tengo una lámpara que lee cualquier idioma y oyeme, tres bodegas me pelean por ser la única que venda las bombillas. Una me ofrece la «bombilla universal que sirve pa' todo», otra me enseña un almacén que abrió la semana pasada pero pule con mil estrellas, y la tercera… la tercera es la misma de siempre, la que lleva años en la misma esquina, con el mismo camión repartiendo a la misma hora y el mismo tendero que se queja de que ya nadie lee el inventario.

Yo soy de las que compran donde es desde siempre — no porque el de siempre sea bueno, sino porque lo veo trabajar. Lo veo abrir a la misma hora, el mismo camión descargando, las mismas facturas pegadas en la reja. El de la «bombilla universal» me mira como si le estuviera haciendo un desaire al no comprarle. El del almacén nuevo tiene el traje reluciente, sí… pero su estantería estaba vacía el martes pasado, y eso se lo preguntó mi vecina que fue a curiosear.

Le paso la misma pregunta a todas: «¿Y si una bombilla me explota, tú me la cambias?» Dos se ríen. La vieja de la esquina me enseña el libro de reclamaciones y me dice que lleva ahí cinco años. Eso me basta. Las lámparas se compran por luz; las bombillas, por recibo.

Cliente, es lo mismo con tu lector de manga y anime. Las extensiones son las bombillas; los almacenes, las bodegas; y tu teléfono, el mueble que las recibe. Hoy te dibujo el mapa completo del barrio: qué árbol de parsers tiene tu lector, qué almacenes viven de él, cuáles mudaron de dirección este verano, y por qué la camada de impostores se viste igual todas las semanas.

Dessy, la voz principal. Este tema nos tocó verificarlo de cerca — y el mapa tiene sorpresas de agosto.

┄┄┄

🗺️ EL MAPA DE LA PIEZA

Primero se entiende la regla de oro: lámpara (tu app), bombilla (la extensión), y bodega (el almacén). Tres capas, ninguna sirve sin la otra — pero todas las confusiones del barrio nacen de cruzarlas.

Después los árboles: tu lector no es «de extensiones» en general — es de UN árbol de parsers (Mihon/Keiyoushi, Usagi/Kotatsu, servidores), y cada árbol tiene almacenes propios que no hablan entre sí. La pieza 03 de esta serie explica por dónde llegar al lector mismo; esta explica qué llega después.

Luego el censo de hoy: hub central empujando esta madrugada, casa anime con commit de hace tres horas, independiente con empuje de ayer, y un directorio que declara su servicio y sus límites. Y al final, el catálogo de impostores y las cinco preguntas que cierran la feria sin que te des cuenta.

┄┄┄

🧩 LA PIEZA EN UNA PÁGINA

• Tu lector es una LÁMPARA: trae motor, no contenido. Las extensiones son las BOMBILLAS: se instalan por almacén, y se actualizan como las apps. Los ALMACENES son las BODEGAS: viven en repos con mantenedor, historial y código a la vista.

• Tres árboles de parsers dominan el barrio: MIHON (el primogénito vivo del ecosistema madre, con su almacén de referencia Keiyoushi), el árbol USAGI/KOTATSU (su propio protocolo, su casa aparte, pieza futura de esta serie), y la capa SERVIDOR (Suwayomi y el recién llegado uchiyomi: tu biblioteca corriendo en PC o web, comiendo las mismas bombillas de Mihon).

• El hub del árbol Mihon se reinició el 13 de agosto de 2026 como un almacén basado en RELEASES — maquinaria nueva, mismo nombre, mismo bot repartiendo índices a diario (empuje de hoy, 19 horas). La convención citada en papeles como «KeiSource 1.6» vive hoy en los commits como la «lib 16», con el PR #448 de Animetail como el caso que enseña por qué migrar la cadena no es opción sino urgencia.

• El árbol anime vive en la familia YŪZŌNŌ: almacén al día (commit de hace 3 horas), y desde el 1 de septiembre una capa LEGACY publicada por la propia casa para que las fuentes viejas respiren en la convención nueva. La noticia del mes ese tipo: el 17 de septiembre el almacén Yūzōnō injertó el CORE del hub Keiyoushi en su rama (PR #952): dos casas grandes compartiendo plomero.

• Los independientes siguen con su oficio: manga-repo con empuje de ayer, y una mudanza de dirección declarada en su propio README — la receta convencional queda bajo el nombre de la familia Yūzōnō aunque el repo viva con otro dueno. El segundo estante adulto de referencia sigue vivo a su ritmo (empuje del 3 de agosto). Los ecosistemas chinos (copymanga y su rama comunitaria, la megacolección ZGQ) viven su propio ciclo. Miyomi es el cartel del mercado — ahora con organización propia y licencia AGPL-3.0 — pero dice claramente que no audita: cartel, no sello.

• Y la feria de impostores: camada documentada esta semana con estrellas gemelas compradas por lote, fecha de nacimiento del mismo día, títulos de anuncio («Best Manga Reader App 2026»), y nombres que se cuelgan de los proyectos buenos. La vacuna son las cinco preguntas de la sección 🧭 y la regla no-traficable: tu almacén se instala desde su casa oficial, jamás desde un post — ni desde este.

┄┄┄

🧠 MAPA MENTAL: LA LISTA

LA LISTA (cómo vivo yo con este tema)

LA LÁMPARA — mi lector, con versión y casa propia. Solo se descarga desde su fuente oficial. Lo primero que se cuida, antes de tocar ninguna bodega.

LAS BODEGAS — uno o dos almacenes oficiales de mi árbol, añadidos desde la guía oficial de cada casa. El hub del árbol Mihon (con su bot de cada día), la casa Yūzōnō para anime. La feria, ni de vitrina.

LA RONDA — cada fin de semana: aceptar las actualizaciones de extensiones que ofrece la app. Dos minutos que previenen todos los dramas de esta guía.

EL RECIBO — saber responder: ¿quién mantiene mi almacén, desde cuándo, dónde está su código, qué límites me confiesa y cómo lo instalé? Si una respuesta me falta, no he terminado la compra.

EL RESPALDO — el catálogo de mi biblioteca guardado fuera del teléfono. Las bombillas se cambian; la biblioteca no se repite.

┄┄┄

📐 LAS TRES CAPAS, CONTADAS DESPACIO

La mejor forma de no perderse en este tema es jurarse que nunca se cruzarán estas tres capas. La PRIMERA es la lámpara: tu app. No trae contenido, trae motor. Se mantiene viva actualizándose desde su propia casa — y sola. Cuando el almacén te muestra el cartel «Outdated app», no es que la bodega se haya ganado enemigos tuyos: es que tu lámpara envejeció y ya no entiende el idioma de la convención nueva.

La SEGUNDA es la bombilla: cada extensión. Una por fuente. Se instalan desde el almacén de tu árbol, y se actualizan como cualquier app: la ronda semanal del mapa mental las mantiene al día. La bombilla es lo más frágil del barrio — la fuente que lee cambia de dirección, cambia de cartel, desaparece. Por eso los almacenes vivos las arreglan casi a diario; por eso el bot reparte a cada rato; y por eso la extensión rota no suele ser culpa del almacén entero, sino de UNA avería concreta que se reporta y se arregla (la semana actual lo vio tres veces).

Y la TERCERA es la bodega: el almacén donde viven las bombillas. Un repositorio con mantenedor, historial visible, código a la vista, y el famoso ÍNDICE — una lista técnica que la app lee para saber qué hay en la bodega y dónde está. Esa lista es la única puerta de entrada que debes conocer… precisamente para saber que nunca debes copiarla de un post: se lee desde la casa oficial, o no se lee.

La regla del índice de esta familia de guías la dice de corrido: te enseñamos a leer el mapa, no te escribimos la receta. La receta se aprende para el tema general y para ninguno en concreto; las direcciones buenas se confirman desde la casa; y cualquier almacén que llegue por cadena se queda esperando hasta que tú mismo verifiques su casa. Es la misma paciencia dominicana con la que se mira el aceite antes de encender el fogón.

┄┄┄

📅 LA LÍNEA DE TIEMPO DEL ECOSISTEMA (de la caída de la madre al bot de hoy)

Enero de 2024 — invierno. El almacén oficial del árbol madre archiva, y su historia queda como lección mayor: la comunidad que aprendió a mantener la plaza después de que cerró la casa original. De esa fecha en adelante, ninguna bodega del ecosistema vuelve a presentarse como «oficial» — y esa palabra es ya señal de alerta dondequiera que aparezca.

Agosto de 2024 — el almacén oficial del árbol anime archiva, y la familia Yūzōnō empieza a levantar su propia casa (su historia de origen queda escrita en los repos de la familia).

Enero de 2026 — el hub Keiyoushi anuncia cambios en su forma de distribuir (el anuncio queda en el historial del repositorio de código); la comunidad empieza a hablar de «release-based» como la vía nueva.

13 de agosto de 2026 — la mudanza se hace: el hub se reinicia con la maquinaria nueva. La raíz del repositorio de hoy lo muestra sin misterio: siete archivos, fechas de agosto, y el bot empujando cada día desde entonces.

1 de septiembre — la casa Yūzōnō publica su capa LegacySource para el tránsito a la convención «lib 16». El conducto entre la era vieja y la nueva queda oficialmente abierto.

13 de septiembre — la búsqueda de esa semana documenta la camada de impostores: varios repos nacidos el mismo día, con estrellas gemelas y títulos de venta. El catálogo de la feria queda escrito.

17 de septiembre — el mes firma su entrada fuera de lo común: el almacén Yūzōnō injerta el core de Keiyoushi en su rama (PR #952). Dos casas grandes comparten plomero por decisión — es la noticia estructural del otoño.

Y esta mañana, 22 de septiembre — el estado del barrio: hub con el bot empujando a las 19 horas de hoy, casa anime con commit de hace 3 horas, independiente de ayer, y el directorio del mercado en su ritmo de siempre. El ecosistema que quedó viudo en 2024 vive hoy más barrio que nunca — con mudanzas técnicas completadas y plomería compartida.

┄┄┄

📗 KEIYOUSHI, EL HUB PRINCIPAL, Y SU MUDANZA DE AGOSTO

El nombre largo que repite todo el barrio — Keiyoushi — es hoy el mercado central de las bombillas del árbol Mihon. Sus números de hoy lo respaldan: alrededor de 15.0 mil estrellas contadas esta mañana, y — mejor dato— el bot repartiendo el índice con un empuje de hace apenas 19 horas. Una bodega viva no se define por su placa: se define por su camión.

Lo interesante de esta casa, y lo que la madre vieja de esta pieza aún no conocía, es su mudanza técnica del 13 de agosto de 2026. En esa fecha el repositorio del almacén se reinició completo como «almacén basado en releases»: maquinaria nueva, historia nueva del repositorio, mismo nombre y mismo barrio. La raíz del repo de hoy lo cuenta sin adornos: un archivero llamado index.json (la lista completa de extensiones, en texto legible), su hermana comprimida index.min.json, la factura operativa index.pb, el carnet de identidad repo.json, el inventario de activos release-assets.json, la carpeta de logos, y el README de siempre. Todo eso junto es «el almacén» para tu lector: una lista viva que la app re-lee cada vez que abre.

La mudanza cambia una arruga práctica: la edad del repo ya no se deduce de la fecha de creación que muestra GitHub — ese reloj se reinició en agosto — sino del proyecto y su historial. Y añadirlo sigue siendo igual de simple: la guía oficial de la casa, con su instalación en pocos toques — desde esa página, no desde cadenas.

Keiyoushi además declara sus límites donde duele, y eso es buena señal: su sitio avisa qué aplicaciones ya no soporta (las del árbol madre original, las viejas del árbol) y pone la solución al lado (actualizar a las apps vivas del árbol: Mihon, TachiyomiSY, Komikku). En el barrio, el tendero que te dice «esto ya no lo sirvo» vale doble que el que dice «esto lo tenemos todito».

┄┄┄

⚪ YŪZŌNŌ, LA CASA DEL ANIME, Y EL INJERTO DEL MES

Si el hub es el mercado central, la familia Yūzōnō es hoy la casa donde vive el anime del ecosistema. Sus números de esta mañana: almacén de anime con 439 estrellas contadas hoy y 5.548 commits a sus espaldas — un historial de trabajo serio, no de semana. Su último commit llegó hace apenas tres horas: una fuente nueva entrando al almacén (PR #984). El periferia sigue mandando mercancía y la casa sigue despachando a diario.

Tres hechos de su historial reciente cuentan el mes entero. El más importante, y el que este punto titula de «injerto»: el 17 de septiembre la casa integró en su rama el módulo PRINCIPAL del hub Keiyoushi — un commit titulado «Keiyoushi Network Import (Core)» con su número #952. Traducido al barrio: dos bodegas grandes dejaron de mantener cada una su plomería por separado y empezaron a compartirla. El efecto práctico para ti: menos averías duplicadas, y los arreglos que salen de un lado sirven al otro. Es el tipo de integración que no sale en titulares y que define la salud de un ecosistema.

El segundo hecho: la casa vive la transición entre convenciones. Sus commits recientes incluyen los títulos «Bump to Lib 16» varias veces en las últimas semanas — la mudanza de patrón que la guía cita en su sección de convención. Y, lo más elegante del mes, su solución a la transición misma: el primer día de septiembre publicaron un componente llamado LegacySource «para compatibilidad con lib-16». En criollo: construyeron el ADAPTADOR para que las fuentes viejas siguieran respirando mientras el barrio migra, antes de que la mudanza doliera. Eso es mantener con tiempo, no con drama.

Y el tercero, casi un detalle fino que habla claro: el repo exige SDK mínimo 24 — es decir, las lámparas viejas de verdad (Android 6 para atrás) ya no reciben mercancía de esta casa. No es curios: es coherencia técnica declarada en el frente, sin que tengas que descubrirla a la mala.

Una nota más de la casa: su estante «cursed» para contenido adulto sigue vivo en su rango (la regla de siempre: se nombra que existe, no se pega el índice), como segundo dato del mapa de cada uno y su jurisdicción.

┄┄┄

🗂️ LOS DEMÁS ALMACENES DEL BARRIO (con su fecha)

El barrio no vive solo de las dos casas grandes. El censo de hoy reparte así el resto del mapa — todos numerados, todos con su fecha.

MANGA-REPO, EL INDEPENDIENTE ACTIVO. Su propio dueño mantiene una bodega de manga multi-idioma con 451 estrellas contadas esta mañana y empuje del día de ayer, 21 de septiembre (recuento de volúmenes añadido a sus fuentes). Lo más didáctico de esta casa es su MUDANZA DECLARADA: el README de su front avisa que la receta convencional del almacén queda bajo la dirección de la familia Yūzōnō (yuzono/manga-repo) AUNQUE EL REPO VIVA CON OTRO NOMBRE — la dirección se mantiene como alias para no romper a los viejos asiduos. Es la lección viva de por qué tu receta copiada de hace dos años puede ser letra muerta hoy: las direcciones migran y solo la casa avisa.

LOS SEGUNDOS ESTANTES ADULTOS. Aparte de la familia Yūzōnō, la referencia independiente documentada sigue su ciclo propio, con su último empuje del 3 de agosto a su fecha de constancia. Se nombra como marco del mapa (existe, vive, tiene mantenedor), y jamás su índice — cada quien decide su jurisdicción, como manda la casa.

EL ECOSISTEMA CHINO. Vive su propio ciclo con sus propios tiempos: la rama comunitaria de copymanga sigue con versiones activas (la última vista, v1.4.85, consta del 8 de septiembre), y la megacolección de ZGQ mantiene su agregador histórico de fuentes. Es un barrio hermano con su propia lógica de mantenimiento — y con las mismas reglas de verificación: casa oficial, historial, reporte bueno.

LA CAPA SERVIDOR. Para el que quiere su biblioteca manga en PC o en web, el almacén de la familia Suwayomi sigue activo (empuje de mediados de septiembre a su fecha), y el recién llegado del semestre, uchiyomi, ofrece la biblioteca como aplicación web auto-hospedada comiendo las mismas extensiones del árbol Mihon (versión v0.33.0 constada al 14 de septiembre). Otra habitación, mismas bombillas — la lámpara de escritorio del barrio.

Y EL MUSEO, siempre con su placa: el almacén oficial original del árbol madre (archivado enero de 2024), la gran fuente copymanga original (archivada febrero de 2024), el almacén oficial del árbol Aniyomi (archivado agosto de 2024), y Kohi-den — la primera casa de código del árbol Yūzōnō — archivada en mayo de 2026 con la obra terminada. Cada uno se cita para no esperar en su puerta y para recordar que todo lo vivo de hoy también tendrá su placa un día.

┄┄┄

📐 LA CONVENCIÓN, DE KEISOURCE 1.6 A LIB 16 (el detalle fino, dicho fino)

Aquí va el trozo más técnico de la pieza, y va despacio porque los números de versión de este barrio se prestan confusión. En los papeles históricos — guías, discusiones, repos viejos — la convención con la que se construyen las extensiones del árbol aparece como «KeiSource 1.6»: el patrón con el que se cocinan las bombillas modernas tras la gran mudanza de 2024. Quietecito y lejos del drama, en los commits de la temporada la misma convención se llama hoy «lib 16»: la librería número dieciséis, cuyo rastro aparece en los títulos de empuje («Bump to Lib 16», «LegacySource for lib-16 compatibility»).

¿Son dos cosas distintas? La lectura honesta: no existe un papel central que declare el cambio de nombre — la comunidad documenta en la marcha. Lo que sí existe es la evidencia de la semana: los repos vivos empujan esa numeración en cadena, y el caso clásico sigue citándose — el PR #448 de Animetail, el fork que tardó en migrar su cadena y cuyos usuarios perdieron el acceso a los almacenes de golpe, hasta que su ajuste «resolving 1.6+ extension loading» les devolvió la entrada. La moraleja de aquel PR es exactamente la de hoy: quien no migra la cadena, pierde los almacenes; y quien espera a que duela, migra de prisa.

Lo que sí cambió con el nombre: el papel. En la era 1.6 la convención era una cita histórica del ecosistema; en la era lib 16 vive dentro de los commits, los módulos compartidos y el core injertado — ya no es solo patrón, es plomería compartida entre casas. Para ti, usuario, se reduce otra vez a lo simple: mantén tu lector al día desde su casa, acepta las actualizaciones de bombillas los fines de semana, y no le pidas a una convención vieja que abra la puerta de la nueva.

┄┄┄

🗂️ MIYOMI, EL CARTEL DEL MERCADO (y su verano legal)

Miyomi ocupa una esquina rara y preciosa de este mapa: no es app (no es lámpara), no es almacén (no es bodega). Es el cartel del mercado: la guía curada donde el ecosistema entero — lectores, almacenes, herramientas, servidores — desfila ordenado por categorías con una breve nota de cada uno. Este verano también vivió su mudanza: desde junio vive en su organización propia (miyomiorg), y sus números de esta mañana — 188 estrellas contadas hoy, último empuje del 31 de agosto — muestran una comunidad de curadores con pulso propio.

Lo más didáctico de su temporada es legal: entre junio y julio el proyecto cambió de licencia, pasando de la permisiva Apache-2.0 a la compartida AGPL-3.0, y publicó en el mismo gesto una política de marca separada que regula el uso de su nombre, su logo y sus activos. Traducido al barrio: el cartel aclaró quién puede pintar encima de él y quién no, y ustedes mismos pueden leer la orden — está firmada en el repositorio, sin abogado necesario.

Y su propia confesión de límites, que esta familia de guías cita siempre: Miyomi no aloja las apps que lista, no garantiza su seguridad, no las audita. El cartel del mercado no es el tendero. Usarlo como mapa sí; usarlo como sello de seguridad, no — para eso están las cinco preguntas que vienen a continuación.

┄┄┄

🎭 LA FERIA DE LOS IMPOSTORES, EN PROSA DE BARRIO

Todo mercado próspero levanta su feria frente a la puerta. La búsqueda de la semana pasada documentó una camada entera de repos con el mismo traje, y el patrón se repite tanto que ya merece su propia clasificación. Cuatro botones delatan la funda: las ESTRELLAS GEMELAS — varios repos «distintos» con números idénticos entre sí, porque se compraron por lote; el HISTORIAL DE AYER — nacieron el mismo día, sin meses de empujes detrás (la camada documentada abrió sus toldos en conjunto el trece de septiembre); el TÍTULO DE ANUNCIO — frases de televisión de madrugada donde el proyecto debería tener nombre propio; y el NOMBRE PRESTADO — toman el de una casa buena y le cuelgan la palabra de venta.

Lo que venden esos toldos no es mercancía: es el clic — y en el peor caso de su ramo, la instalación envenenada bajo disfraz de extensión. El refrán del barrio se repite en todas las puertas de esta serie: si el título suena a anuncio de canal nocturno y las estrellas no cuadran con la historia, no se abre, no se enlaza, no se instala. Hay una forma más barata de perder el teléfono que comprando en la feria: no la hay.

Y la práctica que termina de cerrar la casa: la dirección oficial de cada almacén se confirma en la guía oficial del proyecto — la casa Keiyoushi publica la suya; la casa Yūzōnō, la suya; manga-repo, la suya en su propio front. De cualquier otra acera — de este post incluido — se toma nada pegable: solo el mapa y las casas. La regla no se negocia: si alguien te manda «el índice del almacén bueno», ese alguien está actuando como la feria, aunque sea tu primo.

┄┄┄

🧭 LAS CINCO PREGUNTAS ANTES DE ABRIR UN ALMACÉN

El filtro de la casa, en prosa, para memorizar antes de cualquier instalación nueva.

Primero: ¿quién lo mantiene? Un bot de una organización con historial público pesa más que una cuenta sin cara nacida este mes. Segundo: ¿desde cuándo empuja? Meses o años de empujes visibles valen infinitamente más que una semana de actividad; la fecha del último commit es el carnet de la bodega. Tercero: ¿el código está a la vista? Código publicado pasa la vara (o se registra como es); «solo binarios» no la pasa — se apunta como pregunta, no como confianza. Cuarto: ¿su sitio confiesa sus límites? La casa que avisa qué ya no sirve vende más verdad que la que promete infinito. Y quinto, el sello: ¿la instalación se lee en la casa? En la guía oficial del proyecto, jamás en un post ajeno — ni en este.

Dos minutos para responderlas, y la feria cierra sola. Sus anexos obvios: «está en Miyomi» no es respuesta a ninguna de las cinco — es el cartel del mercado, no el examen del tendero; y «me lo mandó el técnico del grupo» tampoco — el técnico del grupo no reemplaza a la casa, por bueno que sea.

┄┄┄

📚 LAS CUATRO TRANCAS DEL ALMACÉN, CONTADAS COMO DUEÑAS

La primera tranca es la clásica del ecosistema: «mi lista de extensiones amaneció vacía, todo sale obsoleto». Diagnóstico exacto: la app envejeció para la convención del almacén. Medicina en orden: leer el aviso de compatibilidad del sitio oficial (Keiyoushi declara a día de hoy su soporte a Mihon, TachiyomiSY y Komikku); actualizar tu app desde SU casa (su repositorio oficial o su canal libre, nunca un paquete «compatible» de la feria); re-añadir la fuente del almacén por la guía oficial. Si tras actualizar sigue vacío, ahí sí, te toca escribir al mantenedor — con pasos reproducibles, no con queja.

La segunda tranca es una bombilla sola apagada: «una fuente concreta dejó de funcionar, las demás corren bien». El almacén está sano; una extensión murió. La evidencia de esta semana (credenciales expiradas corregidas, recuento de volúmenes añadido) muestra el ritmo de reparación real: días. Medicina: actualizar la extensión cuando salga (llegan como actualizaciones de extensiones dentro de la app), y reportar bien en el repo del código: versión de la app, nombre de la fuente, pasos exactos, captura. El caso de Ambiorix abajo lo muestra con detalle — un reporte bueno arregla para todo el barrio.

La tercera tranca: «añadí la bodega y no aparece nada». Orden de revisión: receta intacta (un espacio la rompe), red viva (los almacenes se leen en tiempo real), app al día, y paciencia con el primer censo del índice. Todo en verde y sigue: limpiar caché o rehacer el procedimiento desde la guía oficial — rara vez el fallo es del almacén.

Y la cuarta tranca no es técnica: «me llegó por grupo un almacén nuevo y mejor». Corre las cinco preguntas antes de tocar nada — y si el remitente no puede nombrar el repo del código, su mantenedor o su casa oficial, la respuesta fina es «gracias, ya tengo bodega». La lámpara requiere bombillas con recibo.

┄┄┄

🧪 CASOS PRÁCTICOS DEL BARRIO

Carlitos, la que actualizó tarde. Usa su lector desde 2025 y esta semana su lista apareció vacía con el cartelito de obsoleto. Lloró al grupo pidiendo «el almacén nuevo que sirva», y tres vecinos le mandaron tres enlaces distintos — uno de ellos de la feria. El arreglo real no vino de ninguno: vino de la página oficial del almacén, que dice sin rodeos qué apps soporta. Carlitos actualizó desde la casa, re-añadió la fuente oficial y volvió todo. Lección que repartió al grupo entero: el almacén casi nunca se rompe; la lámpara es la que envejece.

Joandry, el curioso de la feria. Encontró un repo con título de «Ultimate Multilanguage Hub», ciento y pico de estrellas, y la palabra «gratis» dos veces en el banner. Abrió, miró: nació hace dos días, sin una línea de código publicado y con una dirección de receta que no cuadra con ninguna casa. Cerró la pestaña y avisó a su primo antes de que su primo instalara. No hubo historia porque no hubo clic — la sabiduría barrial más económica que existe.

Milka, la que quiso servidor. Quería la biblioteca en la PC de la casa, no solo en el teléfono. Descubrió la capa servidor: el almacén de la familia Suwayomi para escritorio, y el recién llegado uchiyomi corriendo como aplicación web comiendo las mismas extensiones del árbol. No cambió de almacén ni de convención: cambió de mueble. La lámpara grande del cuarto de cómputo usa las mismas bombillas que la del bolsillo.

Ambiorix, el que reportó bien. Una fuente suya no cargaba desde el lunes; en vez de abandonar la bodega, abrió un issue en el repo del código: versión de app, fuente, pasos, captura. A los tres días, commit con el arreglo integrado. No cambió de bodega: hizo la bodega mejor para todos — el barrio libre vive de esos reportes.

Los cuatro casos comparten espina: la herramienta libre premia al que mira la casa y después reporta; la feria, solo al que no compra.

┄┄┄

🧯 MITOS DE LA BOMBILLA (cuatro apagones, dichos sin rodeos)

Apagón uno: «Keiyoushi es el almacén oficial de Tachiyomi». No. El oficial original archivó con su árbol madre en enero de 2024, y desde entonces ninguna bodega del ecosistema tiene esa etiqueta — palabra que hoy solo usa la feria. Keiyoushi es el almacén DE REFERENCIA del árbol vivo: una comunidad organizada, sin empresa detrás. La diferencia práctica es enorme: nadie te garantiza nada; un colectivo te muestra su trabajo todos los días — y esa exhibición diaria es tu garantía.

Apagón dos: «más estrellas, más seguro». La camada de esta semana compró sus estrellas por lote — por eso las repite idénticas. Las estrellas cuentan congregación, no higiene. La vara de verdad ya la tienes: mantenedor con cara, historial con meses, código a la vista, límites confesados.

Apagón tres: «las extensiones del árbol Mihon sirven en todo lector de la lista». No. Los árboles viven protocolos distintos de parsers: las bombillas de Keiyoushi/Yūzōnō no entran en los lectores del árbol Usagi/Kotatsu (cuya guía será pieza propia de esta serie), y solo la capa servidor del mismo árbol las comparte. La bombilla del árbol equivocado no quema ni ilumina: simplemente no entra.

Apagón cuatro: «si figura en Miyomi, está verificado». Miyomi se declara a sí mismo: no aloja, no audita, no garantiza. Catalogar es mostrar vitrinas; verificar es otra profesión. El cartel del mercado es el mejor punto de entrada del barrio — y el peor sustituto imaginable de la vara.

┄┄┄

❓ PREGUNTAS FRECUENTES, EN PROSA

¿Qué almacén uso con Mihon? Keiyoushi — lo dice su propio sitio al declarar sus soportes. Si tu lista sale vacía con el aviso de app obsoleta, el problema es tu versión, no la bodega: actualiza desde la casa y re-añade por la guía oficial.

¿Y para anime? La casa Yūzōnō, al día de hoy con commit de hace tres horas. Las direcciones viejas del árbol anime son ya museo: el oficial original archivó en agosto de 2024 y su primera casa de código en mayo de 2026.

¿Los estantes adultos son peligrosos? El mecanismo es el mismo de cualquier bodega; el riesgo vive en el contenido y en tu jurisdicción. Se nombran para completar el mapa; los índices de ningún almacén se pegan en esta familia de guías.

¿Puedo tener varios almacenes? Sí, la app convive con varios. La regla de la casa: cada bodega extra aumenta la superficie que vigilar — dos bien miradas valen más que cinco sin recibo.

¿Cada cuánto se actualizan las extensiones? Las bodegas vivas publican varias veces por semana, y el bot del hub a diario. Tu app las ofrece como actualizaciones de extensiones — aceptarlas en la ronda del fin de semana es todo el mantenimiento.

¿Por qué dejó de funcionar mi receta vieja? Tres causas usuales: la casa migró de dirección (caso documentado hoy con manga-repo), el almacén cambió de maquinaria (el hub en agosto), o tu app envejeció para la convención nueva. Se mira la casa antes de re-copiar nada.

¿Pasan mis extensiones al teléfono nuevo? Sí, migrando la biblioteca con la herramienta de respaldo de tu lector. Los almacenes no se migran: se vuelven a añadir desde sus casas — ocasión sana de borrar los que ya no usas.

¿Dónde reporto una extensión rota? En el repositorio del código del ecosistema, con versión, fuente, pasos y captura. Ya se vio esta misma semana: reporte bueno igual a arreglo rápido.

¿Y si mañana cae el almacén grande? El ecosistema ya ensayó eso en 2024: la comunidad se re-organiza alrededor del código, que vive en forks. Tu plan: respaldo encendido, las cinco preguntas de memoria, y calma.

┄┄┄

📖 GLOSARIO DEL TEMA, EN PROSA

App: tu lector, la lámpara — motor sin contenido. Extensión: la bombilla adaptadora, una por fuente. Almacén: la bodega con dueño e historial donde viven las bombillas. Índice: la lista técnica que la app lee para descubrir el almacén; en esta casa se señala la puerta, jamás la receta. Fuente: el contenido que una bombilla lee. Hub: el almacén de referencia del árbol Mihon — hoy, Keiyoushi. Bot del almacén: el camión automático que reparte el índice a diario. Repositorio del código: el taller hermano donde se arreglan las bombillas. Convención (lib): el patrón técnico de construcción — en papeles «KeiSource 1.6», en commits «lib 16». LegacySource: el adaptador para que las fuentes del patrón viejo respiren en la convención nueva. «Outdated app»: el cartel de que tu lector ya no entiende la convención vigente — se cura actualizando la app. Release-based: la maquinaria nueva del hub desde agosto. Fork: proyecto hijo de otro. Estante adulto: el rincón de contenido de algunas bodegas; se nombra, no se enlaza. Capa servidor (Suwayomi, uchiyomi): tu biblioteca en PC o web comiendo las mismas bombillas. Directorio (Miyomi): el cartel del mercado — usar como mapa, nunca como sello.

┄┄┄

📖 HISTORIA CORTA: EL AÑO QUE EL ECOSISTEMA APRENDIÓ A VIVIR SIN MADRE

Enero de 2024 enseñó al barrio su lección fundacional: cuando la casa madre archivó su almacén oficial, quedó claro que nada de esto era infraestructura «de alguien» — era el trabajo de muchos esperando a que otro lo levantara. Lo que vino fue manual de supervivencia de libro: el árbol más fuerte encontró su almacén de referencia en una comunidad nueva, nacida como tarea compartida, con un bot repartiendo índices todos los días desde entonces; la casa anime se mudó a la familia de su propio árbol; y cada fork aprendió su manera de convivir con las bombillas.

Año y medio después, la semana de hoy enseña que el ecosistema no solo sobrevivió: se volvió más barrio. Dos señales nuevas lo demuestran: la INTEGRACIÓN de los herederos, dos casas grandes compartiendo plomero desde el diecisiete de septiembre, y la MADUREZ declarada — maquinaria de releases, capa puente para las fuentes viejas, museo cerrado con la obra terminada. Pasos de quien cuida legado, no de quien corre detrás del día.

La moraleja para el usuario común no es heroica: es doméstica. Tu lector y tus bombillas viven del trabajo de gente organizada en su tiempo libre. Cuidar el barrio no es donar estrellas: es reportar bien, actualizar tranquilo, no repartir calles ajenas, y acordarte de que el tendero voluntario también cansa. Quien aprende eso ya pagó la mitad del mapa con la moneda que no se gasta: el respeto al mantenedor.

┄┄┄

🧪 EL TALLER EN SEIS PASOS, CON CENTAVO DOMINICANO

Paso uno: identifica tu lámpara. Anota nombre y versión exactos desde sus ajustes — cuesta diez segundos y es tu primera defensa.

Paso dos: abre la casa, no el buscador. Escribe la dirección oficial del almacén y lee qué apps declara soportar y cuándo fue su último aviso.

Paso tres: añade por la guía oficial, con el atajo de instalación de la propia casa. Nada que pegar a ciegas desde sitios ajenos.

Paso cuatro: espera el primer censo. Si llega vacío con el aviso de app vieja, ya tienes diagnóstico. Si llega lleno, deja el botón quieto.

Paso cinco: instala poco, mira mucho. Solo las bombillas de las fuentes que realmente leerás; cada una extra es superficie que actualizar.

Y paso seis, el que sostiene todo: la ronda semanal. Dos minutos por fin de semana aceptando las actualizaciones que la app ofrece.

┄┄┄

🏛️ UNA NOTA DEL MUSEO, PARA CERRAR EL MAPA

Se llega al museo con respeto y se sale sin equipaje. El archivo del árbol madre (enero de 2024) apagó una semana y encendió un barrio; la gran fuente china original (febrero de 2024) donó su protocolo a todos los sucesores; el del árbol anime (agosto de 2024) fue la partida de nacimiento de la casa que hoy empuja hace tres horas; y Kohi-den (mayo de 2026) enseña lo más fino: archivar también puede ser madurez — cerrar con la obra terminada.

El museo se recorre para no esperar en la puerta equivocada, y para recordar que el hub vivo de hoy también tendrá su placa un día. La pregunta del barrio no es cuánto dura la bodega: es si tú estarás mirando mientras dure.

┄┄┄

😄 EL MEME DE LA PIEZA

Original de la casa, del tema, sin atacar a nadie.

LA BOMBILLA DE LA FERIA

— Tengo la bombilla UNIVERSAL que sirve pa' todos los enchufes, joven. Nueva en caja, recién llegada.
— ¿Y eso que la caja no tiene marca?
— Es que es tan buena que no necesita.
— ¿Y tiene año de fabricación?
— No pregunte tanto, que se espanta el descuento.
— Gracias, hermano, es que con mi lámpara se espantan hasta los que venden sin recibo.
— ¡Oye! ¿Y pa' quién tú me tomas?
— Pa' un vendedor sin recibo. Eso fue lo primero que me enseñaron en el mercado.

El chiste defiende su tema: el impostor no teme tus preguntas técnicas — teme las cuatro de siempre: quién eres, desde cuándo, a ver tu taller, y por qué no das recibo. La lámpara se enciende sola cuando la bombilla llega con papeles.

┄┄┄

🛠️ MÉTODO DE LA CASA (con los pasos fechados de hoy)

Primero, la madre re-leída: la guía del quince de septiembre (once mil caracteres) se leyó entera y se marcó su lista de caducables — nueve almacenes con placa, cuatro archivos de museo, la convención citada, la camada de impostores, las reglas de lectura. Lo mundano fue a re-contarse hoy; lo estructural, a confirmarse en su historial.

Segundo, la verificación viva de esta mañana, veintidós de septiembre: abierto el hub Keiyoushi (bot con empuje de hace 19 horas, raíz de siete archivos, reinicio de agosto a la vista, quince mil estrellas contadas hoy); abierto el almacén anime de la familia Yūzōnō (commit de hace 3 horas, 439 estrellas contadas hoy, 5.548 commits, el injerto del core documentado con su número del diecisiete, la capa puente del primero de septiembre, los empujes de la lib 16 de la semana); abierto manga-repo (451 estrellas contadas hoy, empuje del 21 de septiembre, y su propio README mandando mantener la receta bajo la dirección de la familia Yūzōnō); y abierto Miyomi (188 estrellas contadas hoy, organización propia desde junio, licencia AGPL-3.0 con política de marca publicada entre junio y julio, último empuje del 31 de agosto). Las cifras no re-contadas hoy llevan su fecha al lado, a la vista: el repositorio del código del hub (cuatro mil setecientas estrellas al quince del mes), la rama china (versión uno punto cuatro punto ochentaicinco al ocho de septiembre), la web-app de servidor (versión cero punto treinta y tres al catorce), el servidor clásico (empuje del doce), el segundo estante adulto (empuje del tres de agosto) y la megacolección ZGQ (mil doscientas al catorce). Los datos del museo son fechas históricas constadas en su día.

Tercero, lo no comprobado se dice tal cual: la transición de nombre de la convención se describe desde commits y mensajes de PR públicos — no existe papel oficial que la anuncie, y así se declara en su sección; el recuento exacto de fuentes del hub vive en su índice y no se re-contó hoy; los canales chinos no se re-abrieron esta mañana (actividad de días pasados basta para el mapa, marcada como tal).

Cuarto, la vara: conteo con longitud directa sobre este texto nativo de Facebook, anatomía completa verificada (semilla, mapa, página única, mapa mental, meme original, método, enlaces, nota, versión compacta y tags), y banda de la casa (treinta y nueve mil a cuarenta y un mil) confirmada antes de sellar. Número exacto en el registro vivo del día.

Y quinto, la humildad del tema: este mapa envejece por semanas — bots empujan a diario, convenciones migran por meses, bodegas mudan por sorpresa. Toda cifra aquí se re-cuenta antes de repetirse. La pieza dice la verdad de hoy; mañana, la de mañana.

┄┄┄

🔗 ENLACES, ABIERTOS HOY

El almacén del árbol Mihon: dos puntos barra barra github.com/keiyoushi/extensions — su código hermano: github.com/keiyoushi/extensions-source — la guía oficial de la casa: keiyoushi.github.io.
La casa del anime: github.com/yuzono/anime-extensions — su sitio: yuzono.github.io — su estante adulto (se nombra, no se enlaza índice): el que su propia organización lista.
El independiente: github.com/cuong-tran/manga-repo — leer su README sobre la dirección de la receta.
El segundo estante adulto independiente: el que su autor mantiene en su perfil (misma política: nombre sí, índice no).
El ecosistema chino: la rama comunitaria de copymanga y la megacolección ZGQ, accesibles desde sus propias casas públicas.
La capa servidor: el almacén de Suwayomi (github.com/Suwayomi) y la web-app nueva del semestre en su casa del catorce.
El cartel del mercado: miyomi.app — su código, en la organización que este verano abrió con su nombre.

┄┄┄

📝 NOTA DE VERIFICACIÓN — 22 DE SEPTIEMBRE DE 2026

Abiertos hoy y leídos en su propia página: el repositorio del almacén del árbol Mihon, el almacén de anime de la familia Yūzōnō, el repositorio del independiente manga-repo y el directorio del mercado. De ellos salen: el empuje del bot de esta madrugada, la re-inicialización basada en lanzamientos del trece de agosto, el commit de hace tres horas, el injerto del core del diecisiete con su número, la capa puente del primero de septiembre, los empujes de convención de la semana, la migración declarada del independiente y la mudanza legal del directorio. Placas re-contadas hoy: quince mil, cuatrocientas treinta y nueve, cuatrocientas cincuenta y una, ciento ochenta y ocho. Placas citadas a su fecha: las del código, la rama china, la web-app, el servidor, el segundo estante, la megacolección — todas marcadas en su punto. Fechas del museo constadas históricamente. Ningún número sale de memoria; todo lleva fuente y fecha.

┄┄┄

✍️ CIERRE

Pieza cuarta de La Bandita, edición dominicano-español, verificada esta mañana con la vara de la casa. El mapa del barrio no tiene alcalde: tiene bodegas con camión puntual y una feria que siempre intentará parecerse al mercado. Tu criterio es el recibo. Actualiza tranquilo, reporta bien, y jamás instales lo que venga sin casa.

Busca más, y que la bombilla te llegue con papeles.

Versión compacta: tu lector y sus extensiones viven de tres capas — lámpara, bombilla, bodega — y de tres árboles que no se mezclan. El hub del árbol principal mudó de maquinaria en agosto y reparte cada día; la casa del anime injertó la plomería del grande este mes; el independiente mudó de dirección declarándolo en su puerta; y la feria de imitaciones se reconoce por sus estrellas gemelas y sus títulos de venta. Todo almacén se instala desde su casa oficial, dos se miran bien y las demás no existen, y la ronda del fin de semana acepta las actualizaciones de la bombilla como quien riega el patio.

La Bandita informa a partir de fuentes fechadas. Las bodegas abren cada día; la vara también.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#LaBandita #ExtensionesMihon #Keiyoushi #MangaYAnime #LectorAndroid #KeiSourceLib16 #GitHubDeConfianza #VerificaAntesDeInstalar #EcosistemaLibre #FuenteFechada #SoftwareLibre #RepublicaDominicana
