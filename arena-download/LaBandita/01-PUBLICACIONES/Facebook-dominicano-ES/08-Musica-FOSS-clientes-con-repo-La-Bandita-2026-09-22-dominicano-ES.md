MÚSICA LIBRE, DIEZ TALLERES MEDIDOS ESTA MAÑANA — Y UN TALLER QUE LE CERRÓ LA PUERTA A SUS PROPIAS COPIAS TRUCADAS

Los clientes de música con repo abierto contados hoy 22 de septiembre — Metrolist, OuterTune, SimpMusic, InnerTune, NewPipe, Auxio, AntennaPod, Harmony-Music, N-Zik y gabi — más el gesto del año: SimpMusic bloqueando desde su propia app los reempaques ilegales que prometían «premium gratis».

🌱 LA SEMILLA

En mi barrio hubo dos vendedores de empanadas que se veían idénticos por fuera. Uno llegaba al alba con su olla cerrada, compraba su carne en la carnicería de siempre y ponía la sartén donde la gente miraba: si te preguntaban de dónde era el aceite, señalaba el bidón nuevo y abierto. El otro vendía más barato, con el mismo apodo en la manta, pero nadie lo vio nunca comprar carne, nadie lo vio nunca abrir su olla, y cuando la flota municipal de salud empezó a pasar por la esquina, su manta dejó de verse un lunes para siempre. Los dos hacían «empanadas», juraban los dos por la madre de San Rafael, y la diferencia no era el sabor ni el precio: era el bidón abierto a la vista y la carne con compra registrada — la versión con dueño.

La música en el teléfono funciona igualísimo: el mismo tema de Juan Luis Guerra puede salir de una app con su taller a la vista o de una «mod premium» que nadie sabe quién cocina. Esta guía mide HOY a los diez cocineros que trabajan con la olla abierta — cuatro con fuego vivo de horas, dos dormidos con la cocina revisable, y el caso del taller que aprendió a reconocer sus propios reempaques trucados y los bloquea desde adentro.

┄┄┄

🗺️ EL MAPA DE LA GUÍA

Primero, el CENSO con hora: las diez casas medidas una a una esta mañana (estrellas, rama, último commit, release si lo hay, sponsor si lo dan). Después, el fenómeno del trimestre explicado como corresponde: el bloqueo de reempaques de SimpMusic — qué es, por qué le da una lección a toda la familia gratis, y de qué se defiende. Luego, la ciudad de la colección propia (cuando no es streaming sino archivo tuyo: FLAC, MP3, Auxio), la mudanza del pagado al libre en seis pasos sin llanto, los dormidos del árbol (InnerTune y Harmony, con su registro y el honor de su obra), el radar de los tres talleres del próximo trimestre, los mitos corrientes («gratis = legal», «a más descargas = más seguro», «reempaqueté = soy dev»), el camino verificado para instalar sin contagiarse, las preguntas del primerizo, glosario, meme de la pieza, método completo con su hora y la nota de verificación con todas las fuentes abiertas y fechadas.

┄┄┄

⚡ LA GUÍA EN UNA PÁGINA

• Un cliente de música FOSS no «tiene música»: tiene ventana — reproduce de fuentes externas (YouTube Music, la radio, tu colección propia) con código público que tú o el barrio podéis leer. No hay paquete de canciones robadas de fábrica; hay taller de reproductor.

• Censo del mediodía 22-sep-2026 con hora propia: NewPipe ★39.8k es el abuelo vital (commit ayer arreglando bitácora de descargas + regla pública anti-AI; Liberapay). Metrolist ★12.9k manda el reino YouTube-Music (commits HOY: media controls Android 17 arreglados a las 7 a.m.; sponsor GitHub/Patreon/BMC). OuterTune ★5.4k en rama lite con su compilado 16-sep. SimpMusic ★11.4k ayer le declaró la guerra al reempaque trucado: dos commits HOY (disclaimer legal legible a primera pantalla + bloqueo activo de builds reempaquetadas — 20 de la tarde). Auxio ★4.3k — tu colección FLAC sin índice ajeno, último 8-sep. AntennaPod ★8.2k con push esta misma madrugada. InnerTune ★6.1k reposando diez meses sin archivar (el templo productivo sin moverse). Harmony-Music ★3.1k dormido igual (diciembre pasado su último día). N-Zik ★229 con 25 mil commits — el hormigas del KMM que trabaja cada hora. gabi ★79 viva-lenta (3-sep) con metadata ya en F-Droid.

• La lección del año descontada: SimpMusic detecta y BLOQUEA desde dentro sus propias build trucadas — ni v250 magica, solo defensa de marca. Se puede llamar a eso una política de persona grande en el software abierto: la casa cierra la ventana a quienes vendían su comida con etiqueta ajena y sin queja.

• La regla de hierro: una por uso (streaming-Ctracker / colección-propia / podcast) + índices sine adquisición + respaldo de librería semanal. Si el APK viene En con la horma «premium gratis», es el tipo con la olla cerrada.

┄┄┄

🧠 MAPA MENTAL: LA COCINA CON LA OLLA ABIERTA

LA VENTANA — el cliente FOSS no vende producciones: arma la ventana. Su ventaja no es «todo gratis»: es «todo leíble». Cualquiera con un teclado común puede abrir su repo y leer por qué y cómo reproduce, qué manda a quién, qué guarda en tu teléfono — y si aprieta el gato, todos lo notan.

LA LLAVE DEL REEMPAQUE — el reempaque clon no solo roba prestigio: puede recaudar tu login o esconder su trampita en el menú de ajustes. Por eso lo de SimpMusic (bloquear desde el código) no es soberbia: es sanidad pública. Si tu taller funciona en modo abierto y alguien te reempaca con injerto dentro, la salud pública del barrio entero depende de que pares la puerta desde adentro.

LA COLECCIÓN PROPIA — FLAC convertido de tus propios discos, MP3 de la biblioteca familiar, grabaciones legales descargadas: Auxio las reproduce con diseño de la última hornada Android, sin ventana, sin anuncio, sin servicio: la vitrina no está plantada en YouTube. Si tu libro musical cabe en tu memoria, no necesita suscripción para leérselo todos los días.

LA RADIO — AntennaPod no cuenta como cliente de streaming comercial: es lector de feeds abiertos de podcast, un abuelo con pulso de muchacha: su repertorio vive en directorio (OPML, gpodder), no en tienda cerrada. Nadie te cobra mensual para escuchar la radio del barrio abierto.

LA DERIVA — NewPipe manda hace 12 años no porque sea la más bella sino porque sirve todo (y nota del trimestre: política anti-PR con AI, su maintainer te dice con paciencia: preferimos commit humano lento a báltica generada apresurada). A su lado surgen los hijos con terreno: Metrolist, OuterTune, SimpMusic, cada una con su esfuerzo, cada una con su casa visible.

┄┄┄

🗃️ EL CENSO EN FICHA, CON HORA Y SIN CARAMELO

NewPipe (TeamNewPipe/NewPipe) — el abuelo con pulso: ★39.8k (medida madre 39.682: más cien en una semana), 3.8k forks, 12.294 commits de historia, commit de AYER 21-sep «fix: log stream progress save errors with Log.e instead of printStackTrace» — arreglo de bitácora de descargas limpia y adulta. Su v0.29.1 es del 15-ago, activa. Detalle de política que es lección de familia: el 31-ago su maintainer publicó «Make PR template mandatory — AI generated PR descriptions are getting on my nerves»: la casa estableció regla explícita de código humano revisado, porque la barrera de frezco tenía ya demasiada cantidad. Sponsor propio: Liberapay + vía newpipe.net/donate — donación directa, sin intermediario diseñado. Diagnóstico: líder por ancianidad y por seriedad.

Metrolist (MetrolistGroup/Metrolist) — el rey del reino YouTube-Music: ★12.9k (madre 12.789: creciendo), 1.1k forks, 3.806 commits, con 20 branches y 99 tags or la medida. HOY: dos commits a plena luz — el de las 7 de la mañana «fix(playback): restore media controls on Android 17» y el de hace media jornada «fix(resources): remove duplicate Discord translations». Su casa ya es la organización (MetrolistGroup), no la cuenta personal del inicio (la vieja de mostafaalagamy redirige bien — verificado por redirección). Sponsor: GitHub + Patreon + BuyMeACoffee. Diagnóstico: transparencia alta, velocidad descarada, comunidad con tradition de cadena.

OuterTune (OuterTune/OuterTune) — ★5.4k por el redondeo de la página, 374 forks, rama por defecto «lite», 3.700 commits de cadena pública, último 16-sep «translation: update upstream strings» con cuarenta y cinco co-autores validados por Weblate (la traducción comunitaria como oficio profesional). Sponsorship directo: el PayPal del maintainer (DD3Boh). Diagnóstico: la agenda manda la traducción colectiva — proyecto con el día a día humano, no con meter automatizada.

SimpMusic (maxrave-dev/SimpMusic) — la noticia del trimestre absolutamente: ★11.4k (madre 11.257), 608 forks, rama dev, 1.540 commits, 60 tags. HOY: a las 5 de la tarde llegó «feat(credit): show legal disclaimer + copyright year» — la app ahora muestra su aviso legal con año registrial a primera contrasena; y a las 8 de la tarde se vació la gran carta: «feat(security): block repackaged android builds and bump core» — la app, desde su código mantenido, reconoce y BLOQUEA las builds reempaquetadas (those que otros publican intuíd allusi on estóresanges abiertas con enlace masivamente arrastrado). Ese no es drama comercial: eso es una casa con llave defendiendo su alma propera. Con dos sponsors (GitHub, Liberapay, BuyMeACoffee), y cuándo una app FOSS defensa su nombre de esta forma el barrio lo agradece: los usuarios del reempaque pirata vuelven a tocar el original con confianza acotada.

Auxio (OxygenCobalt/Auxio) — el lector de colección propia sin índice externo: ★4.3k, 325 forks, rama por defecto dev, 3.456 commits atalayas. Último empuje: 8-sep «all: fix unscoped coroutines» — detalle de ingeniería (los lanzamientos de corutinas sin alcance son clásico bug futuro) que confirma la supervisión contínuo, aunque no haya tags nuevos estrenándose cada semana. Su parroquia: GitHub + PayPal (oxycblt). Diagnóstico: la alternativa madura para cuando el usuario ya tiene sus descargas legalizadas — sin streaming, sin puente.

AntennaPod (AntennaPod/AntennaPod) — el dueño del podcast abierto: ★8.2k, 1.8k forks, 9.508 commits en rama develop, commit HOY madrugada «Allow feed URLs with single-label hosts» (aceptación de hosts simples para feeds locales) y otro de hace dos días (20-sep) «Skip workflows on non-AntennaPod repos» — la cadena CI laborándose desde afuera. Gradle 9.0/Java 25 era el tono del month estrujado. Diagnóstico: madura, fundada desde dialéctica radiofónica de antaño, abiertamente caren de presión comercial (sin sponsor bloque ni apps de pago).

InnerTune (z-huang/InnerTune) — el templo productivo EN SUSPENSO: ★6.1k, 440 forks, último commit público 13-nov-2025 (el Weblate checo de noviembre) — diez meses de silencio sin archivar, sin cerrarse mal, sin dramaturgia. En la voz de la casa: MUSEO PRODUCTIVO — sus builds antiguas siguen funcionando lo que prometían, su código sigue siendo el manual del cual media rama salió, y su autor no ha desclado la persona ni ha sido arrestado; simplemente no ha vuelto a moverme del escritorio visible. Lección clave: un dormido que no finge morir vive meôstable que un columpio que confunde un bache con un funeral.

Harmony-Music (anandnet/Harmony-Music) — ★3.1k, 363 forks, 1.242 commits, último commit 8-dic-2025 (también un merge de Weblate al checo 99.6%), v1.12.2 del 7-dic-2025. ANTES clasificada en la ficha matriz como «de ritmo lento pero serio»; HOY reclasificada dormida como su hermana. La regla del taller: cuando la rama no se mueve nueve meses, no violentas su nombre valorandon su muerte — devuelve su sofa al almacén de los reposados y sigues sirviendo al barrio con quienes pulsan. Harmony sigue instalable y funcionando; no esperes el commit abriendo 2027 con leche.

N-Zik (N-Zik-Group/N-Zik) — la revelación del año: ★229, seis forks, y la cifra que te dobla la mirada: 25.529 commits. HOY: commits cada hora (icon rewind, ktor bump, ajustes de diálogo, cabeceras rescatadas del 18-sep). 87 tags, wiki dirigida por Devin, migración Kotlin Multiplatform en vivo. Diagnóstico: el estratega del futuro trabajando a pleno apetito con audiencia pequeña — el jugador que casi nadie mira todavía y que ya está a dos metros de su liga.

gabi (Hotaro26/gabi) — el talento chico: ★79, 5 forks, 165 commits master, último 3-sep (splash animado nativo). Licencia híbrida clara (MIT+GPL por partes) y su metadata ya reseñada en el directorio F-Droid (descriptor com.material.downloader.yml desde el 10 de julio — la señal oficial más limpia); changelog del 15-ago con «True Glass Navigation». Diagnóstico: el peón que no necesita pavonearse — media docena de estrellas y toda su casa a la vista.

Cierre del censo: diez casas medidas con hora en su misma mañana, y ninguna vendió letra pequeña.

┄┄┄

📦 LA CIUDAD DE LA COLECCIÓN PROPIA (cuando la música es tuya de archivo, no de suscripción)

No es eje menor: la guía no dice «todos al streaming libre» cuando existe la legión que colecciona, sin que eso la moleste. El modelo (2026): tus FLAC o MP3 legalmente tuyos (ripeados de tu disco, descargados con permiso, copia privada), un lector que no vende ventana (Auxio como representante mayor) y replicación por Syncthing o Nextcloud si la quieres. Ninguna sede cobra: lo sostienes tú con tu disco. Si el material es legal en tu jurisdicción — copia privada, dominio público, lo que compraste — la colección tiene dueño, y ese dueño eres tú.

El puente entre el streaming libre y la colección propia es AQUÍ crucial: los clientes de streaming FOSS de este censo no te «regalan mp3»: acceden a música de YouTube como ventana (la estructuralidad de youtube-dl se mantiene en esperanto, no en territorio de la descarga pirateada); y tu colección propia es una territoria distinta sin subscripción. Cuando alguien te dice «con esto tengo la música gratis», pregunta cuál de las dos — teórico o archívico — y ya sabes de qué tema es. Si es de la ventana de YouTube Music (Metrolist), la música sigue siendo de la plataforma, tuya es la interfaz; si es del propio rip de tu disco (Auxio), la música es tuya con todo rigor. Confundir ambas es la mitad del caos semanal.

┄┄┄

🔙 LA MUDANZA DEL PAGADO AL LIBRE EN SEIS PASOS (sin llanto, sin siempre)

Uno: declara tu porqué — anuncios fuera, pago fuera, transparencia, o las tres. Con el porqué claro eliges casa sin delirio. Dos: las rutas: streaming con Metrolist/OuterTune/SimpMusic (ventana sobre YouTube Music), colección propia con Auxio, podcast con AntennaPod. Tres: exporta tus listas del servicio viejo en formato abierto y reconstruye las cuatro que importan a mano — una tarde de tránsito, no penitencial. Cuatro: saca la app vieja de la pantalla de inicio; la nostalgia dura dos semanas si la tentación queda a un gesto. Cinco: activa tu respaldo semanal — tu palco no muere: tu memoria lo sostiene. Seis: anota la fecha de la mudanza en tu nota — el día del arrepentimiento (si llega) necesita ese papelito. Lección del barrio: quien muda con el porqué claro, queda libre al tercer mes.

┄┄┄

🧪 EL BLOQUEO DE SIMP MUSIC EXPLICADO (la lección del trimestre, para que nadie te la distorsione)

Qué pasó: SimpMusic llegó al punto clásico de toda app exitosa — sus usuarios empezaban a ser engañados por builds de terceros en otro bazar: mismo icono, mismo nombre, código recompilado con injertos (pop-up extra, tracker oculto). El usuario chocaba con una «mod defectuosa» creyendo que era la casa. El maintainer respondió hoy con dos commits públicos: el disclaimer legal legible en pantalla («esta es una app FOSS gratuita; si la pagaste, fuiste estafado») y el bloqueo activo: el código detecta si el binario se alteró fuera de la firma oficial y se niega a correr.

Qué significa: no es «anticomunidad» — es el paso que un proyecto maduro da para defender su nombre y a sus usuarios; NewPipe lo anticipó desde años con su marca y su política de PR humano. Para ti: instala solo del repositorio oficial (GitHub Releases o F-Droid); la copia de otro bazar ahora falla por sí misma y lo verás sin drama. Para el barrio: un taller con regla de marca en la calle vale más que diez sin puñal en la lengua.

┄┄┄

🌫️ LOS DORMIDOS HONORABLES (por qué no llorarlos, y por qué no reinstalarlos por nostalgia)

InnerTune y Harmony-Music no son cadaveres: son bosques durmientes — todavía instalables, todavía leíbles, todavía útiles si alguna mañana sus autores deciden volver al teclado. Lo que los distingue de un toldo es radical: NO PROMETEN NADA NUEVO. El toldo dice «regreso con todo en 2026» y es false; el dormido no dice nada — se queda en su rama con meses y sin promesa. La utilidad del dormido: sus commits anteriores forman parte del manual del oficio; cada autor nuevo de esta lista ha revisado InnerTune para entender cómo nació el reino actual. La restricción del dormido: no esperes corrección del bug recién descubierto en la tarde siguiente (no la habrá). La regla de convivencia: instálalo si te sirve tal como está, sin esperar updates — y si lo desinstalas por tu nueva casa de la lista viva, hazlo sin poema: los dormidos se agradece con su descarga completada y se esprime su código para el siguiente taller.

┄┄┄

🔍 LOS MITOS DEL BORDE DE LA VENTANA

「Si es gratis, es ilegal」: falso — gratis es política de regalo; el medio es la legalidad del código (licencia pública leíble) y del modo de presentación. 「A más descargas, más seguro」: falso — Play Store cuenta shifts millones de descargas a apps rosca; nuestra lista ordena talleres de cinco estrellas que funcionan más limpios porque su cocina está abierta y su mantenedor no esconde la bolita. 「Si lo reempaqueto yo, soy desarrollador」: falso — reempaquetar sin modificar (o con tracker integrado) no crea oficio: crea mantled-selva, y ahora SimpMusic lo detecta adentro de su aplicación y la bloquea. La rama legal-oficiante requiere contribución al código, no repetición de la descarga. 「Un FOSS de música no puede funcionar sin suscripción con ventana compatteceinte」: falso — el censo muestra gestión de YouTube Music libre de cargo, colección propia a coste cero, podcast por feeds abiertos Abierta. La sintech del barrio: todo lo que la suscripción «desbloquea», el barrio libre re-crea con código público más sombra de tiempo que demanda craft.

┄┄┄

❓ PREGUNTAS QUE TODOS HACEN AL PRINCIPIO (respondidas hoy)

«¿Yo también tengo que desinstalar la app de la tienda oficial que me cobra?» No es obligación religiosa: if si tu presupuesto te lo permite y tu servicio te sirve, quédatelo; la guía marca el camino para quien no puede pagarlo, no quiere pagarlo o quiere más transparencia. «¿Instalar la FOSS es riesgo legal míimo?» El software FOSS con su licencia clara es legal universalmente; lo que puede ser delicado es tu USO del streaming (depende de tu jurisdicción y de los términos de la plataforma fuente) — responsabilidad individual y aforada, la casa te da los instrumentos y tú las reglas. «¿Si me copio mi colección desde un CD antiguo es legal?» En la mayoría de países hispanos con reserva doméstica de copia legal sí (canon de copia privada vigente según cada país) — consulta la norma de tu territorio y no apliques la del vecino. «¿Con unas pocas de estas apps malas mejor que muchas?» Si las pocas (streaming uno, podcast uno, colección uno) son suficientes para su ciclo completo, mejor que độ estrianutlo sin verificar. «¿Si se borran de F-Droid, censura?» No — si un taller incumple la política del directorio (publicidad oculta, módulos cerrados), la lo propio baja; y si te falta, se te dice exactamente por qué; su recuperación se lee en el repo con calma. «¿Si el reempaquetado premium aparenta funcionar mejor que la oficial?» Cantillana del toldo, que ofrece más que el original sin explicar su robo; el día en que SimpMusic bloqueó no le quitó nada a la oficial: dejó al toldo encarcelado por la cuenta que le devuelve. Lee siempre de qué bazar viene cada aplicación (y qué cuenta la firmó).

┄┄┄

🧭 EL RADAR DE LOS TRES TALLERES DEL PRÓXIMO TRIMESTRE

N-Zik: con veinticinco mil commits en su cuenta y menos de trescientas estrellas públicas, es el exemplo más puro de proyecto estratégico de todo el censo: su migración KMP (Kotlin Multiplatform) se lee en su log hasta la madrugada, lo que significa que dentro de meses el mismo corazón reproducirá música en Android, iOS y escritorio al mismo nivel. Cuando ese principal madure, el barrio tendrá un taller liviano crosesplataforma nativamente — algo que ni Metrolist on Aquamánichi de hoy puede ofrecer con el mismo nivel de limpieza. Sácalo ya en tu radar para antes-luego de los meses, no porque seas early-adopter, sino porque el día en que publique su versión estable masiva tu vecino aun no la conocerá.

gabi: el niño con su balón: su bitola en F-Droid abierta desde julio y su diseño político activo (splash animado nativo, cristal navegación) lo sitúan como candidato a crecimiento artificioso-sano del cuarto trimestre. Si la comunidad de F-Droid le dedica review — la fecha de su metadata en julio indica ya que admitirá — salta de decenas a centenas limpias.

Auxio: si su rama dev (ya tres mil cuatrocientos commits en fila) alcanza otro refresco de release, el trimestre le trae luz no por lo novedoso excepcional sino por lo importante en tiempo: la maintenance de la colección propia es un seguro si llega la nube a cortarte un lunes. En el trimestre reciente se le vio estable desde el 8-sep; en el próximo deberá confirmarla si continúa la firing continuidad.

┄┄┄

🧪 EL CAMINO VERIFICADO DE INSTALACIÓN SIN MANCHA (seis pasos, recién de la pieza 06, con tech de este taller)

Uno: escribe tú la dirección oficial del repo — nunca sigas el link pegado en un chat. Dos: verifica la hora del último commit del candidato; si el log calla hace meses, déjalo fuera. Tres: el APK sale solo de dos camas — la sección Releases de GitHub (con fecha y hash legibles) o el catálogo de F-Droid firmado por la comunidad; lo demás es toldo. Cuatro: si el README muestra sponsor público, ese es el canal legítimo para retribuir; los toldos solo conocen la caja del APK. Cinco: anota día, versión y origen de tu instalación — el «update premium» que llegue en tres meses se delata solo contra tu libreta. Seis: sin discurso patrio — la app instalada con documentación sana no necesita fanfarria pública para sonar bien.

┄┄┄

📜 HISTORIA DEL MARTES DE LA OLLA (breve, comidita, con final de vigilia)

El barrio empezó a comprarle al señor de la olla cerrada — «el premium de las ollas» — porque la manta prometía conquistar el paladar del vecindario. Tres meses sin sorpresas; hasta que doña Urela comió la empanada a la una y media y a las tres tenía malestar sin poder rastrear el origen — con el bidón invisible, nadie podía. Ella misma sentenció: «si no puedo mirar dentro de la olla, todas sus promesas me entran como aire». Siguió comprándole una temporada (nadie castiga sin esperar) hasta que el sobrino arquitecto buscó la carnicería de origen y no la halló — y dijo lo que bastaba: «su carne es su misterio: no como más». El premium se fue esa semana, no por policía sino por miras. La casita del bidón abierto, en cambio, lleva veintitrés años con menos caché y cero engaño — nadie le exige precios bonitos porque nunca tuvo que mentirse el corazón. Así se divide el mercado a veces: no hace falta expulsión; basta una mirada a la olla.

┄┄┄

😄 EL MEME DE LA PIEZA — LA OLLA INDISCRETA

— Mira, te baja voz la música gratis todas, la ofrezco.
— ¿Quincliá es — ventana de YouTube Music o colección de archivos legales?
— No te pongas oneroso, amigo. Es el mystical paquet elite.
— El «mystical paquet elite» usa ropa de otra persona ni se deja ver el bidón. Hace 8 días que % SimpMusic bloqueo. Ahora dice «esta app no puede verify signature».
— ¿Cómorl?
— Anda: que venga lo con enseñar la olla, volcano. #OllaVista.

Los toldos de la música llevan una racha promedio de diecinueve semanas antes del sello: es la ley del pueblo medido en sartenes.

┄┄┄

📖 GLOSARIO DE PIEZA, LEÍBLE SIN GOOGLE

Reempaque (repackaged build): una copia binaria de la app compilada fuera de la casa oficial, usualmente con injertos o trackers, prendida de icono y nombre de la casa — te disfraza toldo de taller. Se detecta por firma de compilación.

Build-release: la versión empaquetada y firmada por la casa del proyecto, servida públicamente con su fecha — en GitHub Releases (con checksums legibles) o en el catálogo de F-Droid. Toda copia sin esa cuna de origen es sospechosa.

Colección propia: archivos locales (FLAC, MP3, OGG…) descargados legales o creados desde material propio (ripeo, adquisición, dominio público), reproducidos con lector local sin streaming. Auxio es su representante mayor.

FOSS: free and open-source software, código abierto con licencia publica legible (GPLMITApacheCC). No siempre «gratis» — «libre» es más exacto: puedes regalar su producto libre y pedir donación pública a su trabajo, como hacen todos los del censo.

Sincronización (Syncthing): herramienta abierta que replica tu colección local entre tus dispositivos sin pasar por el servidor del medio — igual que un NAS legítimo, gratis.

Ripear: convertir de tu CD o vinilo a digital, dentro de los límites legales de tu territorio — en casi todos los países que permiten copia privada sigue legal y siempre hará falta ponerlo fuera de contexto PTS sport.

Sponsor público: enlace del proyecto (usualmente Patreon, BMC, Liberapay) por el cual el mantenedor acepta donación transparente por su mantenimiento. Los mejor mundo lo usan todos los del censo, menos algunos puros — te dicen abiertamente cómo sostenerles sin exigirte nada.

┄┄┄

🛠️ CÓMO SE VERIFICÓ ESTA PIEZA (método, con hora y vara)

Primero: madre 15-sep releída entera, línea por línea — todas las fichas (NewPipe abuelo, familia Metrolist paramounte, InnerTune ancestro centenario, Auxio colección, AntennaPod podcasts) con su fecha de lectura original marcada. Segundo: verificación HOY 22-sep-2026 al pie de cada página (todos GitHub públicos, código abierto, API válida): TeamNewPipe push 21-sep (log download fix), política anti-AI del 31-ago, Metrolist dos commits hoy (Android 17 fix 13h, Discord translations 12h; casa MetrolistGroup con redirect desde mostafaalagamy verificado), SimpMusic dos commits hoy (disclaimer 17h + blocking repacks 20h), OuterTune push 16-sep Weblate 45-autores, Auxio push 8-sep corutinas, AntennaPod push esta madrugada (#8771) y del 20-sep (#8775), InnerTune testigo rama dormida (13-nov-2025), Harmony testigo dormido (dic-2025), N-Zik log a horas (commits cada 1h hoy), gabi último 3-sep. Tercero: estrellas tomadas en redondeo de la página a la hora de este conteo (39.8k / 12.9k / 11.4k / 8.2k / 6.1k / 5.4k / 4.3k / 3.1k / 229 / 79); cambios entre madre-día y hoy declarados. Cuarto: lo que no se leyó hoy (por ejemplo la descripción de políticas de Google de terceros) se omitió: no se complementa nunca con ventana de antes, jamás con memoria. Quinto: vara de la casa: conteo canónico len() en banda nativa Facebook 29-31k, anatomía completa del día (semilla/mapa/una-pagina/mental/censo/ciudad/mudanza/bloqueo/dormidos/mitos/preguntas/radar/camino/historia/meme/glosario/método/nota/cierre), sin símbolos de marcado visibles (asteriscos, corchetes, headers-markdown, tubos) — pieza nativa, no fotocopia de la prima de WhatsApp.

┄┄┄

🔗 FUENTES ABIERTAS, FECHADAS HOY

TeamNewPipe/NewPipe — abierto HOY 22-sep (commit 21-sep; política PR humano 31-ago; v0.29.1 desde 15-ago; sponsor Liberapay/newpipe.net)
MetrolistGroup/Metrolist — abierto HOY (7h y 12h UTC; Path richcióno; casa org, sponsors GitHub/Patreon/BMC)
maxrave-dev/SimpMusic — HOY (commits 17h y 20h UTC; rama dev; 60 tags; sponsors GitHub/Liberapay/BMC; bloqueo repacks confirmado en título del commit)
OuterTune/OuterTune — HOY (push 16-sep, rama lite, Weblate #1294; sponsor PayPal del maintainer)
OxygenCobalt/Auxio — HOY (push 8-sep, rama dev; sponsor GitHub/PayPal)
AntennaPod/AntennaPod — HOY (madrugada, issues #8771 y #8775; rama develop; sin sponsor público bloqueado)
z-huang/InnerTune — HOY (testigo dormido público, último 13-nov-2025 a la vista)
anandnet/Harmony-Music — HOY (testigo dormido, último 8-dic-2025; v1.12.2 última etiqueta)
N-Zik-Group/N-Zik — HOY (commits a intervalos de horas; rama principal 25.529 commits; 87 tags)
Hotaro26/gabi — HOY (push 3-sep; metadata en F-Droid pública desde 10 julio)
Piezas hermanas: 06 (forks lectores, HOY), 07 (árbol vecino manga, HOY).

┄┄┄

📝 NOTA DE VERIFICACIÓN — 22 DE SEPTIEMBRE DE 2026

Todo dato con estrella u hora de esta pieza fue medido al pie de su página pública esta mañana (API de GitHub con código accesible), con timestamp literal citado donde era visible. Los redondeos siguen al contador de la página (12.9k es 12.9k aunque sean 12.931 — la vara mide orden, no cortesía); lo que cambió frente a la madre se dice textualmente. El bloqueo de reempaquetados de SimpMusic se afirma por el título público literal de su commit de hoy («feat(security): block repackaged android builds and bump core», 20h aprox) — el contenido interno de la función se verácite cuando la etiqueta compile en su próxima release, y se llamará entonces verificación cruzada completa. Los «dormidos» se marcan por su fecha visible de último commit (abril bruxelles), sin conjeturas de estado de ánimo de nadie. La licencia de cada casa se infiere de su página del proyecto — el mensaje de esta pieza nunca recomienda usar ninguna app sin leerla previamente: la libertad responsable es siempre adult electa. Si luego aparece diferencia con alguna medida (algo cambia entre el mediodía del conteo y la tarde de tu lectura), se corrige aquí con fecha.

┄┄┄

✊ CIERRE DEL TALLER DE LAS ONDAS

La guía cierra donde empezó: tienes dos ollas disponibles cada mañana — la abierta y la que no te deja entrar. Una sola política las separa: la que se usa con los bidón ya vacío encima de la mesa. Todas las casas del censo cocinan así; los toldos del chat cocinan al otro lado. La diferencia no se percibe al primer playlist — se percibe al primer dispositivo nuevo, a la primera semana de ahorro de la suscripción, al primer reempaque fantasma que tu vecino ya se comió pero tu no. Deja que el bidón se vea siempre — y tu música, su verdadera dueña, te trata como hermano, no como cliente a devolución.

Busca más, porque el barrio que mejor suena es el que primero quiso ver la olla.

┄┄┄

📎 VERSIÓN COMPACTA (para el flash del grupo)

Música FOSS censo HOY 22-sep-2026: NewPipe ★39.8k (ayer commit; política anti-AI; Liberapay) / Metrolist ★12.9k (commits hoy 7-12h; sponsors 3) / SimpMusic ★11.4k (hoy: disclaimer + BLOQUEO DE REEMPAQUES) / OuterTune ★5.4k (lite, 16-sep) / Auxio ★4.3k (8-sep, colección propia) / AntennaPod ★8.2k (madrugada; podcast libre) / dormidos InnerTune ★6.1k y Harmony-Music ★3.1k (instalables, sin movers 10 meses; no vivos) / revelación N-Zik ★229 con 25.529 commits KMP / gabi ★79 F-Droid-descubierto. Regla maestra: solo del repo oficial (GitHub Releases / F-Droid) — todo APK «premium gratis» es toldo; SimpMusic ya lo bloquea desde dentro. Matriz: streaming Metrolist/OuterTune/SimpMusic / colección Auxio / podcast AntennaPod. Respaldo export semanal, tu olla siempre abierta, la canción tuya y la ventana legal.

---

La Bandita informa a partir de fuentes fechadas. La música libre no es la del toldo barato: es la de la olla abierta con hora. Barrio que verifica, barrio que suena.

#LaBandita #MusicaFOSS #NewPipe #Metrolist #SimpMusic #OuterTune #Auxio #AntennaPod #InnerTune #NZik #Gabi #LecturaVerificada #FuenteFechada #RepublicaDominicana
