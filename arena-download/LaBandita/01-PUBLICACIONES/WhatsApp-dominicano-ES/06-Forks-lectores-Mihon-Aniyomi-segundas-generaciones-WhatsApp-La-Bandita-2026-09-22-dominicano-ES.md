FORKS DE LECTORES: EL MAPA VIVO DE MIHON, ANIYOMI Y SUS SEGUNDAS GENERACIONES

Cuándo un fork es proyecto y cuándo solo es una foto del padre — el censo de hoy, con estrellas contadas esta misma mañana repo por repo.

*Edición de La Bandita del 22 de septiembre de 2026. Sustituye a la edición del 15-sep: todas las placas principales re-contadas hoy sobre las casas oficiales. Sin afiliación con ningún proyecto vinculado; no recomendamos instalar nada desde fuera de sus propios repos.*

───────────────────

🌱 LA SEMILLA

Dominicana manija, de esas que criaron a los hijos de todo el barrio, cuidao. En mi esquina había una floristería de toda la vida — doña Carmen, que en paz descanse, le puso «La Azucena» y era el punto de referencia: ahí se hacían los ramos de las quinceañeras, las coronas y los domingos de ramos. Cuando doña Carmen enfermó y cerró el local, todo el barrio dijo «ya la floristería se acabó».

¿Y qué pasó? Que sus hijos crecieron viéndola atar ramos. El hijo mayor abrió su propia tienda a dos cuadras — con su propio nombre, oye bien, no «La Azucena 2» — y la gente fue porque él SABÍA atar, no porque era hijo de. La hija del medio montó un puestecito frente al cementerio, solo vendiendo coronas, y le va mejor concentrada en lo suyo que a la madre con todo el surtido. Y el menor estudió computación y en vez de flores hace la página web donde todos los floreros del barrio publican sus fotos — que es su manera de seguir en el negocio de siempre sin vender una sola rosa.

Ahora escucha la otra cara: al mes de cerrar doña Carmen, apareció UN SEÑOR QUE NADIE CONOCE con un letrero «La Azucena — ¡estamos de vuelta!», vendiendo ramos de plástico. Ese no era hijo ni de la flor, mi amor. El barrio entero aprendió la lección: que te digan «somos los de antes» no te dice nada. Que el muchacho sepa atar, SÍ te dice.

Así es el ecosistema de lectores libres, cliente. Tachiyomi era doña Carmen. Cerró su núcleo en enero de 2024, y lo que tienes hoy frente a ti no es «Tachiyomi con otro nombre»: es la familia entera — hijos, hijas, el que hace página web, y un reguero de señores con letrero copiado vendiendo ramo de plástico. Esta guía existe para que tú sepas atar con el ojo: quién empuja código esta semana, quién solo tiene la foto del padre en el mostrador.

Dessy, la voz principal. Hoy el censo salió con persiana arriba en tres repos — te lo cuento con horas.

───────────────────

🗺️ EL MAPA DE LA PIEZA

Primero la regla que ordena todo lo demás: fork no es criterio — cuatro puertas que sí cuentan. Después la herencia explicada sin drama: qué cerró exactamente en enero de 2024 y qué significa «rehijo». Luego el árbol completo con el censo de hoy, ficha por ficha, tronco manga y rama anime.

Después lo que pocos cuentan: la infraestructura que nadie ve (SyncYomi y el servidor), la taxonomía honesta de quién es fork declarado y quién solo heredó el código, la lectura de un repo en diez minutos, licencias dicho sin bufete, y las mudanzas de biblioteca con su liturgia de respaldo. Cierran los mitos del apellido, los problemas típicos de quien cambia de lector, preguntas frecuentes, glosario, el meme de la pieza, el método con sus fechas, los enlaces vivos y la nota de verificación.

───────────────────

⚡ LA PIEZA EN UNA PÁGINA

• Tachiyomi — el lector de manga libre que marcó una época — cerró su núcleo en enero de 2024. Lo que quedó NO es «Tachiyomi con otro nombre»: es una familia de proyectos distintos, con dueños, ritmos y licencias propias. Ninguna estrella instala nada; ningún parentesco garantiza nada.

• Censo manga contado HOY, 22-sep-2026: Mihon ★23.8 mil con commit de hace 14 horas, 8.020 commits acumulados — el sucesor de hecho. TachiyomiSY ★4.2 mil, master al 21-jul, versión 1.13.2 del 13-jul; su grafo Ya declara el bisabuelo (TachiyomiAZ) a la vista. Komikku ★4.8 mil, master al 17-jul, 10.617 commits. Neko ★2.8 mil, commit de hace 7 horas — el especialista MangaDex en plena migración de su lector a Compose (fase 1 integrada el 25-ago).

• Censo anime contado HOY: Aniyomi ★7.7 mil, commit del 14-sep añadiendo soporte a extensions-lib v17 — la rama madre cavando la versión siguiente, aún sin release estable pero viva. Anikku ★1.0 mil, release r8944 del 16-sep — la rama anime más movida del mes. Tadami ★266, con v0.63.0 del 16-sep y 2.062 commits por delante de su madre — manga, anime y ranobe. Animetail queda a su fecha del 15-sep (★579), marcado como no re-contado hoy.

• La infraestructura invisible también respira: SyncYomi ★718, commit de hace 3 horas probando bibliotecas gigantes, versión v1.5.6 del 18-sep. Y su propia portada regala la blunt más honesta del mapa: declara que el cliente Mihon dedicado probablemente nunca se implementará — los límites del dueño, escritos por el dueño.

• La regla ante todo: ser fork, variante o rebautizo NO es razón para usarlo. Las cuatro puertas que sí cuentan: uso real, unicidad, madurez pública y propósito propio. Y la única vía de instalación sana: Releases de la casa oficial, con tag y fecha — jamás «el paquete más actualizado» distribuido por grupos.

───────────────────

🧠 MAPA MENTAL: LA PERSIANA

LA PERSIANA — cómo elijo taller sin preguntar de quién es hijo.

LA REGLA — «fork» no es criterio; «es hijo de» no es función. Pregunto quién levanta la persiana, qué empujó esta semana, si responde issues, y qué hace que el taller de al lado no haga.

EL CENSO — un lector por materia, no tres para lo mismo. Manga general: el tronco con comunidad. MangaDex: el especialista. Anime más manga: la rama madre o sus hijos activos. Cada uno instalado desde su casa — Releases con fecha, nunca el archivo del grupo.

EL RESPALDO — exportar antes de mudar, con fecha en el nombre del archivo. La importación se ensaya con muestra de tres títulos; el viejo no se borra hasta la semana del nuevo.

LA LECTURA — diez minutos por taller nuevo: ¿archivado?, licencia, última versión firmada, último push real, autor respondiendo, badges de CI encendidos.

LO QUE NO INSTALO — «más actualizado que GitHub», mods premium de tienda ajena, previews para el día a día, forks de proyectos archivados sin parentesco declarado, y todo APK que me pida un índice de extensiones en el primer pantallazo.

───────────────────

📜 LA HERENCIA, SIN DRAMA (qué cerró y qué no)

Enero de 2024: el proyecto Tachiyomi anunció el fin de su desarrollo activo y archivó su repositorio. Esa fecha importa por dos cosas distintas que el barrio mezcla siempre. Primera: cerró EL PROYECTO — el taller del maestro, con su almacén oficial de extensiones incluido (archivado el mismo mes). Segunda: NO cerró el código — la licencia libre que siempre tuvo hizo que cualquier equipo con oficio pudiera continuar la obra bajo su propio nombre, y eso es exactamente lo que pasó.

Mihon nació como la continuidad organizada del tronco manga — repo nuevo, casa nueva, comunidad heredada. No es un fork en el grafo: es un rehijo (la taxonomía va en su sección, con los grados leídos hoy). Aniyomi ya existía como rama de manga y anime y siguió su propio camino con su propio árbol de almacenes. Y los forks que llevaban AÑOS como talleres paralelos — TachiyomiSY es el veterano de todos — descubrieron que de pronto eran referencias y no variantes.

Lo que la herencia NO produjo: un «Tachiyomi oficial 2», un «sucesor autorizado», un «Tachiyomi Pro». Todo letrero con ese sazón pertenece al señor del ramo de plástico. El lector libre no se sucede por decreto: se sucede empujando código — y hoy se empuja, en tres repos contados esta mañana con horas de diferencia.

Esta pieza no romantiza el cierre tampoco: un proyecto archivado con su comunidad intacta es el mejor final posible para una era — dejó la puerta abierta y la receta escrita. Lo que vino después, a dos años y medio, es más maduro que el local original en varias cosas (interoperabilidad entre casas, especialización real, sincronización propia), y más desordenado en otras (demasiados apellidos compitiendo por la misma fachada). El mapa existe para que el desorden no te cueste a ti.

───────────────────

⚖️ LA REGLA QUE ORDENA EL MAPA: FORK NO ES CRITERIO

Que algo sea fork, variante o rebautizo de un proyecto querido no es, por sí solo, razón para instalarlo. Las cuatro puertas que sí cuentan — cada ficha de esta guía las cruzó antes de entrar al mapa:

*Puerta uno: uso real.* Alguien de carne y hueso lo usa y puede contar qué tal en grupos serios. Los testimonios con detalle tardan años en falsificarse; las estrellas se compran en una tarde.

*Puerta dos: unicidad.* ¿Hace algo que lo que ya tienes no cubre? «Es fork de X» no es una función. Especializarse en una fuente gigante (Neko), juntar manga, anime y novela ligera (Tadami), sostener el estilo clásico con extras (TachiyomiSY) — eso sí son funciones. Un ícono nuevo, no.

*Puerta tres: madurez pública.* Documentación, versiones firmadas en Releases con tag y fecha, un autor que responde issues. Un último push de hace dos años no cruza esta puerta — y todas las fichas del censo de hoy la cruzan con holgura.

*Puerta cuatro: propósito propio.* El proyecto existe para hacer algo concreto, no para existir como copia. «Más actualizado que el original» es marketing, no propósito; y cuando el original es un proyecto vivo que empuja a diario, la frase se desmonta sola leyendo el historial.

Con esas cuatro puertas, el mapa se reduce solo: decenas de forks se quedan fuera sin necesidad de insultarlos — simplemente no hay proyecto que listar. Y las casas que entran, entran con su persiana medida: estrellas contadas hoy y última señal con su fecha u hora exacta.

───────────────────

🌳 EL ÁRBOL COMPLETO DE HOY (censo del 22-sep)

EL TRONCO MANGA (linaje Tachiyomi → Mihon)
• Mihon — ★23.8 mil · commit HOY (14 h) · 8.020 commits · Apache-2.0 — el sucesor de hecho
• TachiyomiSY — ★4.2 mil · master al 21-jul · v1.13.2 (13-jul) · Apache-2.0 — el clásico con nombre viejo
• TachiyomiSYPreview — ★492 (a su fecha) · r6332 (14-ago) · host de pruebas
• Komikku — ★4.8 mil · master al 17-jul · 10.617 commits · Apache-2.0 — el rehijo con casa propia
• Neko — ★2.8 mil · commit HOY (7 h) · 351 tags · lector Compose en migración — especialista MangaDex
• (Decenas de forks sin proyecto propio: no se listan — la regla)

LA RAMA ANIME (manga + anime + primos)
• Aniyomi — ★7.7 mil · commit 14-sep (extensions-lib v17) · 8.135 commits · Apache-2.0 — la rama madre
• Aniyomi-preview — host de pruebas (a su fecha de la edición vieja)
• Anikku — ★1.0 mil · release r8944 (16-sep) · 8.935 commits · Apache-2.0 — anime, org Komikku
• Tadami — ★266 · v0.63.0 (16-sep) · 2.062 commits adelante de su madre · Apache-2.0 — manga+anime+ranobe
• Animetail — ★579 (a su fecha del 15-sep; no re-contado hoy) — fork declarado

LA INFRAESTRUCTURA
• SyncYomi — ★718 · commit HOY (3 h) · v1.5.6 (18-sep) · sincronización entre dispositivos
• Suwayomi — servidor de escritorio (su ficha vive fechada en la pieza 04 de esta serie)

EL ÁRBOL VECINO — Kotatsu/Usagi (GPL, parsers propios): otra gramática, otra guía de esta familia. No se mezclan extensiones entre árboles — la confusión número uno del barrio, señalada aquí otra vez a propósito.

───────────────────

📱 FICHA POR FICHA: LOS VIVOS DEL CENSO (contadas hoy)

*Mihon — el tronco.* https://github.com/mihonapp/mihon — ★23.8 mil contadas esta mañana (la edición anterior contaba 23.601: el tronco sigue creciendo) · forks 1.5 mil · 8,020 commits · etiquetas 105 · ÚLTIMO COMMIT HOY, hace 14 horas: PR #4002 arreglando la búsqueda de la biblioteca al tocar el nombre de la fuente · licencia Apache-2.0. Su comunidad de traducciones empuja a diario; su versión estable vigente marcaba el 5 de agosto en nuestra edición anterior, y hoy consta que la rama sigue barriendo sin anunciar APK nueva — el oficio hecho rutina. Keiyoushi lo nombra primero entre sus apps soportadas, y en este ecosistema esa mención es la recomendación que vale.

*Un apunte de la ficha que enseña a leer:* el push de hoy NO significa versión nueva. Mihon lleva semanas siendo el ejemplo vivo de «pushed_at ≠ release» — taller barriendo todos los días, vitrina cambiando cuando sale tag. Aprende la diferencia aquí y la tendrás para todos los repos de tu vida.

*TachiyomiSY — el vivo con el nombre viejo.* https://github.com/jobobby04/TachiyomiSY — ★4.2 mil contadas hoy · 9.935 commits · master con último empuje del 21 de julio (PR #1629, migración asíncrona del ordenamiento) · versión vigente 1.13.2 del 13 de julio · Apache-2.0. La portada de hoy deja legible un dato que antes pedía excavar: el grafo lo declara fork de TachiyomiAZ — el linaje con bisabuelo visible, para alegría de la taxonomía. Su julio incluyó subida del SDK mínimo y release firmada; desde entonces, silencio de taller pausado — no muerto: la regla de la casa marca la diferencia, y los dos años de historial sólido mandan más que dos meses de calma.

*Su host de pruebas:* TachiyomiSYPreview (★492 a su fecha, r6332 del 14 de agosto). Las preview-app: para probadores que reportan — no para tu lectura diaria.

*Komikku — el rehijo con taller propio.* https://github.com/komikku-app/komikku — ★4.8 mil contadas hoy (era 4.721) · 10.617 commits, los más numerosos de la familia manga del censo · master con último empuje del 17 de julio (PR #1800: migración de preferencias chapter-hash PARA USUARIOS EXISTENTES — los rehijos también cuidan a los ya-casados, no solo a los recién llegados) · Apache-2.0. La API de GitHub no lo declara fork: repo nuevo, linaje contado en el README. Su organización — con su botón de sponsor a la vista — mantiene además Anikku y el almacén independiente de la pieza 04: una familia de talleres con el mismo plomero.

*Neko — el especialista.* https://github.com/nekomangaorg/Neko — ★2.8 mil contadas hoy · 8.476 commits · 351 tags · COMMIT DE HOY hace 7 horas (PR #3425: el motor de precarga del nuevo lector corrigiendo su propio test) · «Unofficial MangaDex Reader for Android 8+». Su temporada es la obra gruesa de la familia: el 25 de agosto integró la FASE 1 de la migración de todo su lector a Jetpack Compose — actividad, visores y capas reescritos a la vista — y el 14-sep actualizó su CI a JDK 21. Es del linaje de los forks de Tachiyomi, pero su propósito propio no se discute: una sola fuente, hecha mejor que nadie. Para quien vive en MangaDex es ficha aparte; para el resto, un martillo con forma de destornillador — la frase de la edición vieja sigue sirviendo.

*Aniyomi — la rama madre del manga+anime.* https://github.com/aniyomiorg/aniyomi — ★7.7 mil contadas hoy · 8.135 commits · empuje del 14-sep que dice la frase del mes en estas ramas: «feat: Add support for extensions-lib v17». Léela otra vez: la convención que la pieza 04 documentó como la era siguiente YA vive en la rama madre de los lectores. Casi un año sin release estable y cavando sin pausa — madura y trabajando, no cadáver; su propio README ha llevado meses diciendo justamente eso a quien pregunta. Su host Aniyomi-preview sigue para quien prueba y reporta.

*Anikku — el anime-client activo.* https://github.com/komikku-app/anikku — ★1.0 mil contadas hoy · 8.935 commits · 18 tags · release r8944 del 16-sep, con un detalle que este mapa premia por encima de cualquier campaña: compatibilidad con los enlaces «añadir repo» de Aniyomi (PR #245). Antes de eso, la lib 16 integrada con paciencia (release candidates cherry-picados uno a uno) más el sistema de temporadas heredado de la rama madre. La más movida de la rama anime en septiembre — igual que en la edición anterior; algunos récords se repiten solos.

*Tadami — el joven de las tres materias.* https://github.com/andarcanum/Tadami-Aniyomi-fork — ★266 contadas hoy (era 260) · 10.181 commits · fork declarado por grafo con padre visible y 2.062 commits POR DELANTE de su madre (solo 16 por detrás) · merge del 13-sep de la rama «ranobe-novel» y versión v0.63.0 del 16-sep según su Releases · Apache-2.0. Manga más anime más novela ligera en una sola app — el que más rápido evoluciona entre los forks declarados. Tres versiones en un mes: ese ritmo en septiembre se repite desde la ficha anterior.

*Animetail — el «official fork» declarado.* Se marca a su fecha del 15-sep sin reconteo de hoy: ★579, v0.20.4.0, empuje del 7-sep. Su lección permanente se escribió en la pieza 04: él mismo se cuelga la etiqueta «Official fork of Aniyomi» en la descripción — del lado de la org madre no se vio sello ratificándolo — y su caso histórico (el PR del cargador de extensiones que devolvió la entrada cuando llegó tarde a la convención nueva) sigue siendo el ejemplo vivo de por qué migrar la cadena a tiempo no es detalle técnico sino supervivencia del taller.

───────────────────

🏗️ LA INFRAESTRUCTURA QUE NADIE VE

*SyncYomi* — https://github.com/syncyomi/syncyomi — ★718 contadas hoy (era 710) · rama develop con 356 commits · etiquetas 52 · versión v1.5.6 del 18-sep · COMMIT DE HOY hace 3 horas: dos PRs consecutivos ensayando bibliotecas gigantes — la #261 con transmisión continua y primera subida de un dispositivo, la #262 contra un servidor Suwayomi con montón de memoria pequeño. Traducción al barrio: alguien está probando, AHORA MISMO, si tu biblioteca de miles de títulos aguanta la sincronización contra el servidor — con pruebas escritas, no con promesas. Y su portada regala la blunt más refrescante del mapa entero: declara que el cliente Mihon dedicado NO está implementado (el flujo funciona igual por el estándar del árbol) y que — texto literal de su README — probablemente nunca se implementará. Límites escritos por el dueño, no descubiertos por ti: así se ve una casa honesta.

*Suwayomi* — el servidor de escritorio del ecosistema: tu biblioteca corriendo en la PC, leída desde el navegador. Su estado vigente vive fechado en la pieza 04 de esta serie (verificada esta misma jornada). Nombrar la infraestructura aquí cumple su propósito clásico: evitar el error de confundir la app con la capa que la acompaña — el taller con el depósito.

*Hosts de preview* — SYPreview y aniyomi-preview no son aplicaciones de lectura diaria: son aparatos de lanzamiento de compilaciones de prueba del proyecto madre. Se instalan para probar y reportar fallos; quien los usa de diario acepta, sin saberlo, ser piloto de pruebas sin sueldo.

───────────────────

🧬 LA TAXONOMÍA HONESTA: QUIÉN ES FORK Y QUIÉN SOLO HEREDÓ

El grafo de GitHub y la realidad no siempre coinciden — cuatro formas de nacer, leídas hoy con nombres propios:

*Fork declarado.* La plataforma lo dice: campo fork verdadero, padre visible. Hoy lo constatan dos fichas perfectas: Tadami — hijo de aniyomiorg/aniyomi con la cuenta exacta de distancia (2.062 empujes adelante, 16 atrás) — y TachiyomiSY — cuya portada muestra ahora su abuelo declarado (TachiyomiAZ) sin que nadie se lo pregunte. No se discute; se lee.

*Rehijo.* Repositorio NUEVO que hereda el código y declara el linaje en el README sin ser fork en el grafo. Mihon es el caso famoso; Komikku y Anikku completan la muestra. El grafo dice «no es fork»; la historia dice de dónde vienen. Ambos son verdad — por eso a los repos se les leen las dos caras: la del grafo y la del README.

*Host de builds.* No es aplicación: es el aparato que lanza versiones de prueba del proyecto madre. SYPreview, aniyomi-preview. Sirven para probar y reportar — y dejar de servir el día que alguien les confunde con la app diaria.

*Fork de fork.* Copia de una copia sin taller propio. Suele morir sin avisar, y esta guía no los lista ni cuando tienen logo bonito — la señal reconocible: su rama no empuja nada propio, solo persiste el apellido.

La pregunta útil cuando alguien te recomiende «un fork» nunca es ¿de quién es hijo? Es ¿quién empujó código esta semana? Hoy el mapa te lo responde con horas: Mihon 14, Neko 7, SyncYomi 3.

───────────────────

🔍 CÓMO LEER UN REPO EN DIEZ MINUTOS (el ritual del lunes)

```
1. Abre la página del repo desde SU casa — no el
   recorte que te pasaron por el grupo.
2. ¿Dice ARCHIVED? Listo: los muertos se diagnostican
   rápido; se cierra y se anota en el museo.
3. Licencia: el campo de la página o el archivo
   LICENSE. Anótala siempre.
4. Releases: tag y fecha de la última versión
   firmada. Esa es TU puerta de instalación.
5. Separa empuje de versión: pushed_at no es APK —
   Mihon hoy mismo (commit hace 14 h, versión de
   agosto) es el ejemplo de libro.
6. ¿Es fork? El grafo lo dice con padre a la vista;
   si es rehijo, el README lo cuenta. Las dos caras.
7. Autor con cara: abre dos issues al azar — ¿responde
   con soluciones o con silencio?
8. CI vivo: badges verdes y workflows de este mes
   (Neko actualizó el suyo a JDK 21 el 14-sep: se
   ve sin preguntar).
9. Regla de cierre: si el repo la pasa entera, su
   Releases es tu única puerta. Ningún grupo de
   chat es «la casa».
```

───────────────────

📜 LICENCIAS, DICHO SIN BUFETE

Lo que el campo de licencia de cada página declara (contado hoy en las fichas grandes; lo demás, a su fecha):

*Apache-2.0* — Mihon, TachiyomiSY, Komikku, Anikku, Aniyomi, Neko, Tadami; Animetail a su fecha. En términos generales: puedes usar, modificar y redistribuir conservando avisos y nota de cambios. Es la licencia de la familia manga-anime de este mapa.

*GPL-3.0* — el árbol vecino Kotatsu y sus parientes, con la regla de compartir igual: quien redistribuye modificaciones las redistribuye con la misma licencia. Su guía vecina vive en esta serie.

Dos cláusulas de sobremesa, sin cobrar consulta: esto no es asesoría legal — es el campo de licencia de cada página leído con fecha. Si un día redistribuyes un APK modificado, abre el texto completo de la licencia ESE día. Y el aviso de oro que se repite pieza a pieza: un «SY mod premium» comprado o bajado de una tienda de mods NO hereda la confianza del repo Apache — hereda la de su empaque. La licencia no viaja en paquetes de terceros: viaja en el repositorio.

───────────────────

🔄 RESPALDOS Y MUDANZAS DE BIBLIOTECA (la liturgia completa)

• Cada lector de la familia tiene su formato de respaldo; los formatos entre primos SE PARECEN, pero nadie garantiza igualdad ni entre versiones ni entre casas. Mudarte no es arrastrar el archivo: es exportar en casa A e importar en casa B — con ensayo antes de borrar nada.

• Un respaldo creado en 2024 no está verificado contra las versiones de 2026 de NINGÚN lector del censo. La costumbre de la casa: respaldo nuevo cada trimestre, con la fecha en el propio nombre del archivo.

• «Exportas y listo» es promesa de anuncio: las migraciones se ensayan en copia, nunca sobre tu única biblioteca. El episodio documentado en la pieza de Kototoro — donde cambiar de formato de respaldo rompía la mudanza entre versiones de su serie 1.4–1.7 — sigue siendo el memorándum del barrio: los formatos cambian sin avisarte en la cara.

• Si tu progreso vive entre dispositivos, SyncYomi existe exactamente para eso — y su ficha de hoy (ensayos de biblioteca gigante contra Suwayomi, versión del 18-sep, límite de cliente declarado) es la demostración de que la infraestructura maduró también. Aun así, la exportación manual periódica no se cancela: las dos cosas viven juntas, en ese orden.

• La mudanza limpia en seis pasos vive en su taller dedicado más abajo — porque el respaldo sin liturgia es una foto del respaldo, no el respaldo.

───────────────────

🔧 PROBLEMAS TÍPICOS DE QUIEN CAMBIA DE LECTOR (cuatro trancas de mudanza)

*Tranca 1 — «Instalé el nuevo lector y no veo ninguna extensión».* La más común de todas. Cada lector trae su propia lista de extensiones VACÍA: los almacenes se añaden por casa (la pieza 04 cubre ese ritual entero), y ningún respaldo de biblioteca incluye las extensiones — respaldo es biblioteca, no instalación. Solución: abre las guías del almacén oficial del árbol correspondiente y añade desde ahí; si la lista aparece con el aviso de app desactualizada, el problema es tu versión del lector, no el almacén.

*Tranca 2 — «Importé mi respaldo y falta la mitad».* Casi siempre es una de tres causas: el respaldo venía de una versión muy vieja del primo (los formatos migran), la importación se cortó a medias por espacio libre insuficiente, o los títulos faltantes venían de fuentes que el nuevo lector no tiene instaladas (el respaldo guarda referencias; la fuente va por su lado). Solución en orden: libera espacio, re-intenta la importación completa, instala los almacenes correspondientes primero, y compara muestras de tres títulos antes de declarar desastre.

*Tranca 3 — «Tengo dos lectores y las notificaciones me llegan dobles».* No es fallo: es convivencia mal administrada. Si probás dos talleres en paralelo (el paso 5 de la mudanza limpia lo manda), desactiva las actualizaciones automáticas y notificaciones del VIEJO durante la semana de prueba — o vivirás con dos campaneros anunciando el mismo capítulo. Al cerrar la mudanza, el viejo se desinstala con su respaldo ya exportado y fechado.

*Tranca 4 — «El seguimiento de mi progreso (tracker) se desincronizó al cambiar de lector».* El tracker vive atado a tu cuenta del servicio (MAL, AniList, etc.) y cada lector guarda sus propios vínculos título-a-ficha. Al mudarte, los vínculos hay que rehacerlos o verificar uno por uno en muestra — meter el respaldo no migra magia. Solución preventiva: un solo servicio de tracker, credenciales a mano, y SyncYomi para el progreso interno mientras tanto (su limitación de cliente declarada no impide el flujo por el estándar del árbol).

───────────────────

🛠️ TALLER EN SEIS PASOS: LA MUDANZA LIMPIA DE LECTOR

```
PASO 1    RESPALDAR EN EL VIEJO: ajustes → copia de
          seguridad → crear. Nombra el archivo con
          la fecha de hoy y guárdalo FUERA del
          teléfono (nube o PC).

PASO 2    INSTALAR EL NUEVO solo desde su casa:
          pestaña Releases del repo, tag y fecha
          firmados. Jamás el «paquete ya listo» de
          ningún grupo.

PASO 3    ABRIR EL NUEVO SIN IMPORTAR TODAVÍA:
          recórrerlo, añadir los almacenes oficiales
          de tu árbol, confirmar que la versión
          entiende tu convención (nada de avisos
          rojos de app desactualizada).

PASO 4    IMPORTAR Y VERIFICAR MUESTRA: tres
          títulos al azar — capítulo actual,
          progreso, marcadores. Si falla uno, NO
          sigas: se investiga antes de cargar más.

PASO 5    VIVIR UNA SEMANA EN PARALELO: nuevo en
          uso diario, viejo quieto pero instalado
          (notificaciones apagadas en el viejo).
          La semana decide — no la primera hora.

PASO 6    CERRAR: respaldo NUEVO creado desde el
          nuevo (su formato ya no es el del viejo),
          y solo entonces desinstalar el viejo.
          Mudanza terminada, casa ordenada.
```

La liturgia parece excesiva hasta la primera vez que pierdes una biblioteca de mil títulos a un «no pasa nada». Después se te queda para siempre.

───────────────────

🧯 MITOS DEL APELLIDO (cuatro cuentos de barrio)

*Cuento 1 — «Mihon es Tachiyomi».* No. Tachiyomi cerró su núcleo en enero de 2024; Mihon es OTRO repo, vivo hoy, que heredó el modelo — rehijo con casa propia, no sucesor nombrado. El apellido de la historia no viaja en el nombre: viaja en el código y la comunidad. Quien diga «es el Tachiyomi oficial nuevo» está vendiendo apellido, no herramienta.

*Cuento 2 — «El fork con más estrellas es el mejor».* Las estrellas cuentan congregación, no oficio. Hoy el orden manga del censo es Mihon, Komikku, SY, Neko; y Neko — la de menos del cuarteto — hace UNA cosa mejor que todos: si tu vida es MangaDex, «el mejor del mapa» es ella para ti y el tronco es el martillo equivocado. La única lista que elige por ti es tu lista de lectura.

*Cuento 3 — «El que mantiene el nombre viejo es el que manda».* Al contrario: el nombre viejo es exactamente donde parquean los impostores SEO y los mods premium. TachiyomiSY se identifica por su dueño (jobobby04), su grafo (hoy con abuelo a la vista) y su historial — no por tener el rótulo más nostálgico. «SY» sin su casa no es SY: es disfraz.

*Cuento 4 — «Un rehijo sin grafo de fork es sospechoso».* La taxonomía no es jerarquía de confianza: es forma de nacer. Mihon es rehijo — y es el tronco más sólido del mapa con commit de hace catorce horas. La confianza se mide siempre igual: taller abierto, versión firmada con fecha, autor que responde, CI encendido. Da igual el certificado de nacimiento.

───────────────────

🧪 CASOS PRÁCTICOS DEL BARRIO (cuatro mudanzas contadas)

*Caso 1 — Yeraldy, la que probó sin borrar.* Tenía años en el tronco y le picaba el estilo clásico del SY. Instaló desde la casa (Release 1.13.2), exportó su respaldo con fecha en el tronco, importó en SY, verificó tres títulos en muestra — y leyó una semana en paralelo con el viejo en silencio. Al octavo día eligió el clásico por sus fuentes extra, creó respaldo nuevo desde SY, y recién entonces desinstaló el tronco — que se quedó archivado en su nube como respaldo histórico. Mudanza ejemplar: ensayo primero, borrado al final — nunca al revés.

*Caso 2 — Najwa, la del APK bonito.* Recibió por un grupo el «SY PREMIUM sin anuncios, más actualizado que GitHub». Sin casa, sin tag, sin Release — solo el nombre viejo en un paquete. Leyó la regla de esta pieza — «más actualizado que GitHub» no existe: la definición de actualizado ES el repo — y borró el archivo antes de probarlo. Después instaló el SY de su casa y le enseñó al grupo el dato de la licencia: el mod no hereda la confianza del código; hereda la del empaque. El grupo le quitó el silencio y le puso un admin menos.

*Caso 3 — Pedro, el de los dos aparatos.* Tablet de noche, teléfono en la guagua, dos bibliotecas eternamente desincronizadas: capítulo 303 en una, 287 en la otra. Su arreglo de esta temporada: SyncYomi — mismo día en que sus desarrolladores ensayaban bibliotecas gigantes con memoria mínima (los commits de esta mañana, ya citados). Se sincronizó sin que esa función fuera nativa de ninguno de sus lectores, y mantuvo su respaldo manual trimestral — porque el servidor sincroniza, no sustituye el hábito: así lo manda la casa también.

*Caso 4 — Grismely, la que casi cae en el fork del fork.* Se topó con un «MihonTurbo» de cinco estrellas y logo vistoso. Aplicó el ritual de diez minutos: último empuje hacía dos años, README prometiendo desarrollo activo, padre declarado de un fork OLVIDADO — ni siquiera del tronco. Cerró la pestaña y se quedó con la frase del barrio: el fork de un olvidado es un olvidado con retraso — se muere sin avisar y te deja la biblioteca de ceniza.

Los cuatro comparten oficio: mirar taller, no parentesco; ensayar antes de mudar; y tratar cada APK sin casa como lo que es — basura con envoltorio bonito.

───────────────────

📖 HISTORIA CORTA: EL BAR SIN MAESTRO

Cuando el taller del maestro cerró en enero de 2024, el barrio se hizo la pregunta de siempre: ¿ahora qué? La respuesta no fue una herencia — fue una temporada de aprendices. Nadie peleó por el letrero: levantaron talleres con nombre propio y aprendieron a compartir plomería entre casas que ni siquiera se llaman igual.

Dos años y medio después — y constado esta mañana con horas —, el barrio tiene dos señales que el maestro no vio en su época. La primera, la INTEROPERABILIDAD entre las casas: el 16 de septiembre un anime-client de una organización aprendió a entender los enlaces de añadir repo de la otra, y nadie lo anunció — simplemente quedó en el historial, como se deja todo lo que es oficio y no promoción. La segunda, el ESPECIALISTA re-inventando su taller entero a la vista: la fase 1 del lector nuevo, integrada en agosto, con los tests de septiembre corrigiendo los detalles en público.

La moraleja la regala la pieza anterior de esta serie: el ecosistema que sobrevive no es el que encuentra «al nuevo Tachiyomi» — es el que acepta que no lo hay. El tronco maduró como tronco; las ramas maduraron como ramas; los arbustos tienen su propia función. Tu lector ideal no existe en abstracto: existe en la combinación de lo que TÚ lees con el taller que esta mañana levantó la persiana. Y quien aprende a leer un repo en diez minutos ya no pregunta en los grupos «¿cuál es el bueno?» — lo ve desde la acera.

───────────────────

🎙️ SEÑALES DE LA SEMANA (ocho hechos reales, con su hora)

*Mihon, hace 14 horas, PR #4002:* arreglo de la búsqueda en biblioteca al tocar el nombre de la fuente. Nadie lo publicitó; la salud del tronco se mide en silencios así.

*Neko, hace 7 horas, PR #3425:* el motor de precarga del lector Compose corrigiendo su propio test. La migración grande no se hace de golpe; se hace test a test, en público.

*SyncYomi, hace 3 horas, PRs #261 y #262:* bibliotecas gigantes ensayadas contra servidor con memoria mínima. Si te preguntas «¿aguantará mis cinco mil títulos?» — alguien lo está midiendo ahora, con datos.

*Anikku, 16-sep, PR #245:* la casa de un árbol entendiendo el add-repo de la otra. Interoperabilidad sin comunicado — la noticia estructural del mes.

*Tadami, 13-sep, merge «ranobe-novel» y v0.63.0 del 16:* las tres materias ya no como promesa sino como integración.

*Aniyomi, 14-sep:* soporte a extensions-lib v17 en la rama madre — la convención nueva de los almacenes llegando a los lectores. La lección técnica del trimestre en un commit.

*Komikku, 17-jul, PR #1800:* migración de preferencias pensada en usuarios EXISTENTES — la señal de madurez que siempre busca esta casa: cuidar a los ya-casados.

*TachiyomiSY, 21-jul:* el último empuje visible de su master, en verano tranquilo tras su release firmada del 13-jul. El clásico no corre: ordeña su rama — y su grafo enseña hoy su abuelo declarado.

───────────────────

📋 RADIOGRAFÍA DEL CENSO (lo medido hoy, con su hora)

```
CASO / TALLER      PLACA HOY     SEÑAL VIVA                NOTA
Mihon              ★23.8 mil     commit HOY 14 h           tronco al día
TachiyomiSY        ★4.2 mil      master al 21-jul          clásico, verano
Komikku            ★4.8 mil      master al 17-jul          rehijo, verano
Neko               ★2.8 mil      commit HOY 7 h            obra gruesa
Aniyomi            ★7.7 mil      commit 14-sep (v17)       rama madre, cava
Anikku             ★1.0 mil      release r8944 (16-sep)    la más movida
Tadami             ★266          v0.63.0 (16-sep)          el joven, corre
Animetail          ★579 (15-sep) push 7-sep (fecha)        a su fecha
SyncYomi           ★718          commit HOY 3 h            infra, mide duro
```

La radiografía en una línea: tres talleres con persiana subida ESTA MAÑANA, el resto trabajando esta misma semana o en su verano — y ninguna ficha viva por debajo de la puerta de madurez. El barrio no está en decadencia: está en reorganización, con las horas a la vista.

───────────────────

🈁 LA CAPA DE INMERSIÓN (la nota de paso, a su fecha)

El censo vecino de la pieza 17 de esta serie cuenta el territorio japonés del ecosistema: lectores para estudiar leyendo (diccionario nativo, minado a Anki), el triple joven anime-manga-novela compatible con las extensiones de esta rama, y el cliente del servidor Komga. Se nombran aquí para que el mapa no tenga esquinas oscuras; sus fichas completas — con placas y fechas propias — viven en su pieza vecina, verificada en su día. La regla cruzada se repite porque es la confusión número uno del barrio: la capa de inmersión usa EXTENSIONES DE ESTE ÁRBOL; el árbol vecino Kotatsu/Usagi, NO — y confundir capas te deja el teléfono instalado y la lectura vacía.

───────────────────

📌 LÍMITES HONESTOS DE ESTA PIEZA

*Este mapa no elige por ti.* Las fichas comparan placas y señales; la elección pertenece a tu lectura. La pregunta «¿cuál es el mejor?» no se responde aquí: se responde en tu casa, con tu lista.

*No cubre el árbol vecino.* Los árboles Kotatsu/Usagi (GPL, otros parsers) viven otra gramática: su guía es vecina en esta serie, y mezclar protocolos es la trampa primera.

*No presume continuidad de placa.* Las estrellas de hoy son de hoy: el tronco subió casi doscientas en una semana. Si lees esta pieza en un mes, re-cuenta — la vara de siempre: este tema envejece por semanas.

*No recontó hoy dos fichas.* Animetail queda marcado a su fecha del 15-sep; Suwayomi a su fecha de la pieza 04. Lo no re-verificado lleva su recibo al lado, siempre.

*No receta índices ni fuentes.* Esta pieza habla de lectores (las lámparas). Lo que leas con ellas es decisión tuya con tus leyes — la disciplina es una: criterio primero, herramienta después.

───────────────────

🆕 QUÉ TRAE NUEVA ESTA EDICIÓN (contra la del 15-sep)

*Uno — placas re-contadas con hora:* las ocho fichas principales tienen estrellas de esta mañana (Mihon 23.8 mil, Komikku 4.8, SY 4.2, Neko 2.8, Aniyomi 7.7, Anikku 1.0, Tadami 266, SyncYomi 718) — y dos fichas marcadas honestamente a su fecha anterior.

*Dos — tres talleres con señal del mismo día:* Mihon 14 horas, Neko 7, SyncYomi 3 — la edición anterior celebraba empujes de la semana; esta tiene la mañana entera trabajando.

*Tres — la v17 en la rama madre:* el commit del 14-sep en Aniyomi: la convención de los almacenes llegando a los lectores — el hilo que liga esta pieza con la de almacenes.

*Cuatro — la obra gruesa de Neko:* fase 1 del lector Compose integrada el 25-ago y tests vivos esta misma mañana — la noticia gorda del especialista, ausente en la edición anterior.

*Cinco — taxonomía comprobada en vivo:* Tadami con su distancia exacta a la madre (2.062 adelante) y SY con su abuelo ya declarado (TachiyomiAZ) — el grafo hoy confirma las dos categorías enseñando.

*Seis — secciones nuevas de oficio:* problemas de mudanza (cuatro trancas), radio del censo con horas, señales de la semana (ocho hechos), la nota de paso de la capa de inmersión, y la historia corta del bar sin maestro. La edición anterior era el mapa; esta es el taller visitado — midiendo con sus propias herramientas.

───────────────────

❓ PREGUNTAS FRECUENTES (doce, contadas hoy)

*¿Cuál instalo?* El que uses y verifiques. Manga general: el tronco, con comunidad y empuje diario. Estilo clásico con extras: el SY de jobobby04. MangaDex por entero: Neko. Anime además del manga: la rama madre o sus hijos activos — Anikku es la más movida del mes, Tadami suma ranobe. Abre la Release el día que instales: esa es la única fecha que manda.

*¿Mihon es Tachiyomi?* No. Tachiyomi cerró; Mihon es otro repo, vivo hoy, que heredó el modelo. La ficha arriba lo cuenta con placa y hora.

*¿Komikku o TachiyomiSY?* Dos vivos con estilo distinto: 4.8 mil contra 4.2 mil de placa hoy; ambos en ritmo de verano tras release firmada cada una. Tu lectura decide — clásico con extras o la casa que además cría Anikku.

*¿Anikku es AniZen?* No — pero es familia declarada: AniZen se declara rebrand de «Anikku Mod» (tiene guía propia en esta serie). Parentela escrita, repos distintos: el caso de escuela del «declarado se ve».

*¿Neko sirve para todo?* Para MangaDex, de maravilla — y ahora con su lector migra a Compose. Para el resto del universo manga, un lector general — una bombilla para un cuarto.

*¿Las apps de «preview» son para instalar?* Para probar y reportar — con la obligación implícita de devolver buenos reportes. Tu día a día pide la versión estable firmada.

*¿Y los doscientos forks que no listaste?* Ser fork no puntúa (la regla del principio). Los que tienen proyecto propio están arriba; los que no, son copias con reloj.

*¿Dónde descargo Mihon?* En su casa: el repo citado, pestaña Releases. No está en Play Store ni tiendas; cualquier «Mihon oficial» en canal ajeno es falso por definición de su propia distribución.

*¿Tadami sirve si solo leo manga?* Funciona, pero es triple materia en una app — para manga sola el tronco es más sencillo. Si las tres te llaman, este es el joven con 2.062 commits de ventaja medidos hoy.

*¿Los respaldos entre primos son compatibles?* A veces se parecen mucho y engañan. Exporta en casa A, importa en casa B, verifica muestra de tres — jamás confíes el archivo solo.

*¿Aniyomi sigue viva sin versiones nuevas?* Constado hoy: commit del 14-sep integrando la v17. Una rama madre puede cavar un año sin lanzar estable y estar vivísima — el cemento no se ve hasta que agarra.

*¿Puedo donar?* Varias casas muestran su botón (Patreon del tronco, GitHub Sponsors y Ko-fi de la rama madre, Sponsors y Liberapay de la infra). Donar no compra soporte: compra continuidad del taller. Esta familia no recibe de ninguna casa — y lo declara cada pieza.

───────────────────

📖 GLOSARIO DEL TEMA (dieciséis términos del taller)

*Fork.* Proyecto hijo de otro, declarado en el grafo de GitHub con su padre visible. Dato de nacimiento — no certificado de calidad.

*Rehijo.* Repo nuevo que hereda el código de un antecesor y lo declara en el README sin ser fork en el grafo. Mihon, Komikku, Anikku: la segunda generación típica de este mapa.

*Fork de fork.* Copia de una copia sin taller propio. Suele morir sin aviso; se reconoce porque su rama no empuja nada propio, solo persiste el apellido.

*Host de previews.* El aparato de lanzamiento de compilaciones de prueba del proyecto madre. Para probar y reportar — no para tu lectura diaria.

*Tronco.* El lector con mayor comunidad y actividad del linaje manga (hoy: Mihon). No es título oficial que alguien otorgó: es medida del presente.

*Rama madre.* La que sostiene una familia entera de vivos (Aniyomi para el anime). Puede cavar sin lanzar versiones — se mide por commits, no por anuncios.

*Especialista.* El taller de una sola materia (Neko con MangaDex). Hace una cosa mejor que todos; si esa cosa no es tu asunto, no es tu taller.

*Commit.* Cada empuje de código al repositorio, con autor, hora y razón públicos. La placa de vida más difícil de falsificar — y la que esta casa siempre lee primero.

*Release (versión firmada).* El paquete instalable con tag y fecha en la pestaña de versiones del repo. Tu única puerta sana de instalación.

*pushed_at no es release.* La verdad gemela de la anterior: un empuje de hoy no es la APK de hoy. El taller barre a diario; la vitrina se renueva con la etiqueta.

*CI (integración continua).* Los workflows que compilan y prueban cada empuje — los badges verdes y acciones de la portada. Taller con CI vivo es fábrica con calidad encendida; el «nightly sin CI» del impostor no aguanta esta lectura.

*minSDK.* La versión mínima de Android que la app exige (el clásico la subió en julio). Tu lámpara vieja marca el límite — no el programa.

*extensions-lib (v16, v17).* La librería-convención con que lectores y almacenes se entienden. La rama madre ya integra la v17 (14-sep); la pieza 04 de esta serie cuenta el otro lado del puente.

*Sincronización (SyncYomi).* El servicio que lleva tu progreso entre dispositivos del linaje — servidor ligero más cliente en el teléfono, con la limitación de cliente dedicado declarada de frente por su propio dueño.

*Apache-2.0 / GPL-3.0.* Las dos familias de licencia de este mapa: la permisiva con avisos y la de compartir igual. Se lee el campo de cada repo, con fecha — y jamás se hereda por paquete ajeno.

*Respaldo (backup).* El archivo que tu lector genera con tu biblioteca entera. Se exporta con fecha, se ensaya en copia, se guarda fuera del teléfono — y no se confía de memoria jamás.

───────────────────

🔬 ANATOMÍA DE UN FORK SALUDABLE (ocho órganos, todos visibles)

Un fork sano no se siente: se examina. Ocho órganos que cualquiera puede abrir desde la acera, con ejemplos de hoy:

```
1. MERGE VIVO CON LA MADRE
   El hijo sigue cogiendo empujes del padre
   (Tadami: solo 16 commits detrás de Aniyomi;
   SY: merges regulares del tronco; Anikku:
   cherry-picks de la rama anime uno a uno).
   El que dejó de absorber, dejó de heredar.

2. TRABAJO PROPIO ENCADENADO
   Commits que NO vienen de la madre (Tadami:
   2.062 propios; Neko: toda una migración).
   El hijo que solo copia compila viejo.

3. RELEASES FIRMADAS CON FECHA
   Tag + fecha + binario coherente con el código.
   La puerta de instalación: no hay otra.

4. CHANGELOG O EQUIVALENTE
   El taller cuenta qué cambió (los PRs son el
   diario público). Silencio total = taller
   que no documenta.

5. README QUE CUENTA EL LINAJE
   De dónde viene, para qué existe, qué NO
   hace todavía (SyncYomi declarando sus
   límites: el modelo de la casa).

6. ISSUES CON RESPUESTA
   Dos hilos al azar: ¿hay humano del lado del
   mantenedor? El cementerio de issues sin
   respuesta es la foto del porvenir.

7. CI ENCENDIDO
   Badges verdes, workflows de este mes. La
   fábrica con calidad encendida, no a oscuras.

8. PROPÓSITO DECLARADO
   «Especialista en X», «triple materia», «el
   estilo clásico»: una frase que sobrevive al
   contacto con el uso. «Más actualizado que
   el original» no sobrevive un mes.
```

Con los ocho a la vista, la decisión de instalar o no instalar deja de ser fe: es ficha técnica. Y con los ocho a la vista, los doscientos forks que esta guía no lista se descartan solos — sin ensañamiento, sin drama: les faltan órganos.

───────────────────

⚖️ EL CASO ANIMETAIL, LEÍDO COMPLETO (la lección que sigue cobrando)

Su resumen aparece en la pieza 04; su lectura completa va aquí porque es la biblia práctica de esta pieza:

Los lectores de esta familia no «poseen» sus fuentes: las cargan desde almacenes. Cuando el ecosistema de almacenes migró su convención (la era contada en la guía anterior), los lectores tenían dos caminos: migrar su cargador a tiempo, o quedarse hablando un idioma que los almacenes ya no hablaban. El caso de Animetail — documentado por su propio PR #448, «resolve 1.6+ extension loading» — es el retrato del segundo camino: los almacenes cambiaron, el lector se quedó, y los usuarios despertaron un día con un lector VIVO pero sin extensiones cargables — como tener taller pintado de nuevo sin entrada de aire.

La moraleja triple, que ninguna pieza de esta serie deja pasar: uno, «estar vivo» (commits, versión nueva) no basta si la cadena técnica se quedó atrás — el cargador es parte del lector, no decoración. Dos, el arreglo llegó por la casa: PR público, revisión, versión firmada — y la comunidad rastreando el hilo, como se arregla todo en el barrio serio. Tres, la vacuna del usuario es la de siempre: lector al día desde su casa, y las extensiones se actualizan solas en la ronda semanal — y quien te ofrece un «parche de compatibilidad» por fuera de la casa te está vendiendo el problema con otro nombre.

Hoy, septiembre de 2026, el ciclo corre de nuevo (la rama madre ya integra la generación siguiente de la librería): la lección no caduca. Lo que migró a tiempo, sobrevivió; lo que se quedó, apagó. Cuando leas dentro de un año «el cargador migró otra vez», que no te coja de sorpresa: será la misma puerta de siempre — entrar por la casa, a tiempo.

───────────────────

🧭 LA BRÚJULA DE 48 HORAS (cómo elegir entre los dos o tres finalistas)

Cuando ya filtraste el mapa con las cuatro puertas y te quedan dos o tres talleres que todo el barrio celebra, la elección se hace así — con cronómetro de barrio, no con encuesta:

*Horas 0–8, el banco de pruebas.* Instala los dos (o tres) finalistas desde sus casas. No importes nada todavía: solo recórrerlos. Carga el mismo título de muestra en cada uno, del mismo almacén, y lee diez minutos por taller — el mismo capítulo si puedes.

*Horas 8–24, las tres preguntas del dedo.* ¿El gesto que más usas (siguiente capítulo, volver a la biblioteca, buscar) le cuesta menos al dedo en cuál? ¿Dónde encuentras sin manual el ajuste que más tocas? ¿Cuál te pide menos permisos raros en primer arranque? Anota sin teorizar: punta y papel, tres renglones por taller.

*Horas 24–48, la noche de importar muestra.* En el favorito, importa un respaldo parcial o añade cinco títulos — y vive con él un día completo: celular acostado, guagua, cama. El taller se mide en las cuatro posturas de tu vida real, no en su captura de portada.

*Hora 48, decide — y cierra.* Te quedas con uno; el otro se desinstala con su respaldo exportado. Dos lectores «en prueba» más de una semana no es prudencia: es biblioteca duplicada con notificaciones dobles (ya lo dicta el taller de mudanza). La decisión del barrio no es «el mejor del mapa»: es EL MÍO, DOCUMENTADO.

───────────────────

📊 LO QUE CADA PRIMO DA QUE EL TRONCO NO (la diferencia real, sin floritura)

```
TachiyomiSY    el estilo clásico con EXTRAS:
               más opciones de fuente y ajustes
               finos heredados de la era AZ —
               el sabor de siempre, sostenido.
Komikku        la familia organizada: una org
               que cría lector manga + anime +
               almacén con el mismo plomero,
               y migraciones pensadas para sus
               usuarios existentes.
Neko           MangaDex como nadie: seguimiento,
               sincronización con la fuente y
               ahora lector reescrito — para su
               nicho, no tiene rival del mapa.
Aniyomi        dos materias (manga+anime) en la
               casa madre de la rama, con la
               convención nueva llegando primero.
Anikku         anime puro contemporary: temporadas,
               lib 16 paciente, add-repo de la
               vecina — la rama anime más ágil.
Tadami         tres materias (manga+anime+ranobe)
               en una sola app, al ritmo más
               joven del censo.
Animetail      se declara «official fork» y
               sostiene su línea propia — con la
               lección histórica ya contada.
SyncYomi       no es lector: es el andamio que
               une tus dispositivos — la pieza
               que completa al resto.
```

No es una tabla para decantar: es para desterrar la idea de que estos talleres compiten por lo mismo. Cada uno cultiva la esquina que el tronco deja libre — eso es un ecosistema, no un campeonato.

───────────────────
🪜 LA ESCALERA DE CONFIANZA DEL LECTOR PRIMERIZO (cuatro peldaños, en orden)

Si llegas hoy a este ecosistema desde cero — o regresas después de años —, la escalera sana es esta. No se brincan peldaños:

*Peldaño 1 — un solo lector, desde su casa.* Para manga general, el tronco; para MangaDex, la especialista; para anime+manga, la rama madre o su anime-client activo. UNO. Instalado desde su Releases, con tag y fecha apuntados en una nota tuya (parece exagerado; no lo es: es tu ficha de instalación).

*Peldaño 2 — los almacenes sugeridos por esa casa.* La pieza 04 de esta serie es el ritual: índices desde la casa oficial del almacén, nunca desde mensajes. Tres a cinco extensiones bastan para el 95% de la lectura del barrio — no necesitas el catálogo entero.

*Peldaño 3 — el respaldo primero que la pasión.* Cuando tu biblioteca llegue a veinte títulos, crea tu primer respaldo con fecha y sácalo del teléfono. El hábito nace antes de que duela; quien aprende el respaldo tras perder 500 títulos lo aprende llorando.

*Peldaño 4 — un primo, solo si una puerta exigió.* Cuando NOTES una necesidad real que tu lector no cubre («quiero esta fuente específica», «quiero anime también», «quiero novela ligera»), vuelves a las cuatro puertas de esta guía y eliges el primo que la cubre — mudanza limpia en seis pasos, semana de convivencia, respaldo nuevo. La mayoría del barrio vive feliz en dos peldaños toda la vida; el tercero y cuarto llegan cuando la lectura los pide, no cuando el aburrimiento los inventa.

La escalera tiene un único enemigo: «me instalo los ocho de una vez para probar». Con ocho talladas no pruebas nada — administras ocho, actualizas ocho, respaldas ninguno. El ecosistema no premia al coleccionista de apps: premia al lector con casa ordenada.

───────────────────

🗄️ LA SEMANA EN DELTA (15-sep contra 22-sep, en números)

El movimiento de siete días, medido con la misma vara en ambas orillas:

```
MIHON      23.601 → 23.8 mil        sube; commit HOY 14 h
KOMIKKU    4.721  → 4.8 mil         sube; master al 17-jul
SY         4.146  → 4.2 mil         sube; master al 21-jul
NEKO       2.792  → 2.8 mil         sube; commit HOY 7 h
ANIYOMI    7.683  → 7.7 mil         sube; v17 integrada 14-sep
ANIKKU     1.032  → 1.0 mil (=)     plana; r8944 del 16-sep
TADAMI     260    → 266             sube; v0.63.0 del 16-sep
SYNYOMI    710    → 718             sube; v1.5.6 del 18-sep
ANIMETAIL  579 (a su fecha)         sin reconteo — marcado
```

La lectura del delta es tan importante como cada fila: una semana normalísima del ecosistema — ninguna explosión, ninguna caída, dos lanzamientos, una integración grande y tres talleres barriendo en la mañana del día del conteo. La salud no es el número alto: es el número que se MUEVE despacio hacia arriba, con código detrás. La próxima pieza contará de nuevo — eso es la vara.

───────────────────

🧾 LA FICHA RESUMEN (para guardar en la nota del teléfono)

```
¿CUÁL INSTALO?   Uno por materia; desde su casa;
                 versión firmada con fecha.
¿MIHON QUÉ ES?   El tronco vivo del manga libre;
                 NO es Tachiyomi (cerró ene-2024).
¿ANIYOMI ESTÁ    Sí: commit del 14-sep, sin
MUERTA?          estable nueva — cavando, no
                 archivada.
¿FORKS MALOS?    Fork no es juicio: NiKO/Komikku/
                 Tadami/SY responden las 4 puertas;
                 el fork-de-fork olvidado no.
¿RESPALDO?       Exportado con fecha, ensayado,
                 fuera del teléfono, trimestral.
¿PREVIEWS?       Probar y reportar: nunca diario.
¿TELEGRAM-APK?   No existe «más actualizado que
                 GitHub»: es la trampa del empaque.
¿DOS LECTORES?   Solo en semana de mudanza, con
                 el viejo en silencio.
¿CON EL ÁRBOL    No se mezclan extensiones:
VECINO?          otro protocolo, otra guía.
¿REGLA MADRE?    ¿Quién levantó la persiana esta
                 semana? — eso es el criterio.
```

───────────────────

🗝️ UNA PALABRA SOBRE LA PAZ DEL ECOSISTEMA (porque esta guía también educa)

Cerrando el mapa, una nota que no es técnica pero sostiene todo lo técnico. Cada ficha de esta pieza está mantenida por gente que trabaja gratis y a la vista: mientras tú leías la radiografía, alguien empujaba un fix del buscador de biblioteca a las diez de la noche, otro corregía un test del nuevo lector, otro ensayaba bibliotecas de extraños contra servidores de extraños. La moneda con que se paga todo eso no es solo la donación — es el comportamiento del barrio: reportes de fallo con pasos y capturas, preguntas ya leídas antes de abrir issue, paciencia con el ritmo de cada taller, y la regla suprema de nunca regar APKs por fuera de la casa (cada paquete re-distribuido sin permiso es un pedacito del taller que alguien tiene que ir a recoger después).

La paz del ecosistema también se mantiene con omisiones deliberadas: esta guía no lista los forks que no superan las puertas, y tú tampoco tienes por qué señalarlos en los grupos con nombre y burla. Se les deja morir silencio — el algoritmo del buscador ya hace el resto; el barrio solo tiene que no regar su nombre. El criterio también es una forma de jardinería: no se arranca la mala hierba con escándalo; se deja de regarla.

───────────────────

🕯️ EL MINUTO DE LOS QUE YA NO EMPUJAN

El mapa también se honra mirando los bancos vacíos. De este linaje han cerrado talleres buenos: la primera casa de código de la rama anime archivó en mayo con la obra terminada — no con drama sino con relevo completo —, y decenas de forks sinceros se apagaron cuando su único mantenedor consiguió trabajo, se casó o simplemente se cansó de leer «crasha mi teléfono» a las tres de la mañana. Se les recuerda aquí con la misma vara con que se miden los vivos: cumplieron mientras estuvieron, y dejaron el código a la vista para quien quiera tomar la llave.

Por eso la frase más importante del ecosistema no es «larga vida al tronco»: es «gracias por cada empuje». La abierta disponibilidad de todo este código — cansancio incluido — es lo que permite que un jueves cualquiera como el de hoy exista un mapa que verificar. La próxima vez que tu ronda de actualizaciones corra sin fallos, ya sabes a quién agradecer en silencio: a los nombres de los commits.

───────────────────

😄 EL MEME DE LA PIEZA

Original de la casa — del tema, con el lector, sin atacar a nadie:

```
EL TALLER DEL APELLIDO

— Buenas, ¿aquí componen corollas como en
  La Azucena?
— ¡Cómo no! Somos La Azucena — ¡estamos de vuelta!
— ¿Y el olor a flor fresca, que no lo huelo?
— Estamos redecorando.
— ¿Y los ramos de novia de antes?
— Los estamos digitalizando.
— ¿Y doña Carmen, que me debe el cambio
  desde diciembre?
— …doña Carmen está en un retiro espiritual
  indefinido.
— Mijo, doña Carmen descansa en paz desde
  febrero; ese velorio lo lloré yo. Así que
  te pregunto otra vez: ¿sabes atar tú,
  o solo sabes el nombre?
— …tengo un primo que sabe.
— Pues trae al primo y quítate del mostrador,
  que el mostrador no ata.
```

El chiste defiende su tema: el apellido no ata ramos ni compone carros ni mantiene lectores — lo hace la grasa fresca de cada mañana. Quien te venda «el sucesor oficial» sin respaldo de commits está vendiendo mostrador, no oficio.

───────────────────

🛠️ MÉTODO DE LA CASA (cómo se horneó esta pieza, fechado)

*Paso uno — la madre re-leída.* Se leyó entera la edición del 15-sep (14.263 c) y se marcó su inventario de caducables: nueve fichas con placa y empuje, las dos piezas de infraestructura, los hosts de prueba, las versiones firmadas. Todo lo mundano fue a re-contarse hoy; lo no re-verificado quedó marcado con su fecha a la vista (Animetail; Suwayomi por la pieza 04).

*Paso dos — la verificación viva de hoy, 22-sep.* Ocho repositorios abiertos y leídos en su propia página esta misma mañana: Mihon (★23.8 mil, commit hace 14 horas, PR #4002; 8.020 commits), Aniyomi (★7.7 mil; commit del 14-sep «extensions-lib v17»; 8.135), TachiyomiSY (★4.2 mil; grafo con padre TachiyomiAZ a la vista; master al 21-jul), TachiyomiSYPreview (★492 y r6332, de la hornada de agosto constada), Komikku (★4.8 mil; 10.617 commits; master al 17-jul, PR #1800), Neko (★2.8 mil; commit hace 7 horas, PR #3425; CI a JDK 21 del 14-sep; fase 1 Compose integrada el 25-ago), Anikku (★1.0 mil; release r8944 del 16-sep; 8.935), Tadami (★266; 10.181 commits; 2.062 por delante; merge ranobe-novel del 13-sep y v0.63.0 del 16-sep) y SyncYomi (★718; commit hace 3 horas — PRs #261 y #262; v1.5.6 del 18-sep; la blunt de su README sobre el cliente dedicado citada textualmente). La búsqueda de prensa del tema no trajo novedad firme que no estuviera ya en los repos — se declara así, sin inventarla.

*Paso tres — lo no comprobado, dicho tal cual.* Animetail quedó a su fecha; las versiones firmadas viejas (1.13.2 del clásico, v0.20.4 del tronco) se describieron como vigentes según su día; la compatibilidad futura de la v17 se describe SOLO por el commit de hoy — sin promesas de roadmap; y la cercanía de los formatos de respaldo entre primos se mantiene como «a veces se parecen», sin garantía — igual que en la edición anterior, porque el oficio no ha cambiado su verdad.

*Paso cuatro — la vara.* Conteo con len() sobre este texto nativo, orillas limpias (cero dobles estrellas, cero pipes, ningún encabezado Markdown), anatomía completa (semilla, mapa, página única, mapa mental, talleres, meme original, método, enlaces, nota, firma, tags) y registro del número exacto en el acta viva del día.

*Paso cinco — la humildad del tema.* Este ecosistema empuja a diario: tres talleres lo hicieron esta misma mañana. Verifica tú la placa antes de repetirla — la costumbre de esta familia es la vara, no la confianza ciega.

───────────────────

🔗 ENLACES (señalados con su fecha de verificación)

*El tronco manga — verificados hoy:*
• Mihon — https://github.com/mihonapp/mihon
• TachiyomiSY — https://github.com/jobobby04/TachiyomiSY
• Sus pruebas — https://github.com/jobobby04/TachiyomiSYPreview (placa de agosto constada)
• Komikku — https://github.com/komikku-app/komikku
• Neko — https://github.com/nekomangaorg/Neko

*La rama anime — verificados hoy:*
• Aniyomi — https://github.com/aniyomiorg/aniyomi
• Anikku — https://github.com/komikku-app/anikku
• Tadami — https://github.com/andarcanum/Tadami-Aniyomi-fork
• Animetail — https://github.com/Animetailapp/Animetail (ficha a su fecha 15-sep)

*La infraestructura — verificada hoy:*
• SyncYomi — https://github.com/syncyomi/syncyomi
• Suwayomi — citado a su fecha en la pieza 04 de esta serie

*Los puentes de esta familia:* pieza 04 (almacenes de extensiones, de esta misma jornada) · pieza 03 (verificación e hito del censo) · la guía vecina del árbol Kotatsu/Usagi y la guía 17 de la capa de inmersión — en su carpeta, en sus fechas.

───────────────────

📝 NOTA DE VERIFICACIÓN (22-sep-2026)

Abiertos hoy y medidos en su propia página: Mihon, Aniyomi, TachiyomiSY, TachiyomiSYPreview (placa de agosto), Komikku, Neko, Anikku, Tadami y SyncYomi — de ellos salen todas las placas y horas marcadas como «hoy» o «esta semana» en el texto: los commits matinales de Mihon (14 h), Neko (7 h) y SyncYomi (3 h), la v17 integrada en la rama madre (14-sep), la fase 1 del lector Compose (25-ago) con su test de hoy (7 h), el release r8944 (16-sep) y la compatibilidad add-repo, el merge ranobe-novel (13-sep) con la v0.63.0 (16-sep), la sync v1.5.6 (18-sep) y los ensayos de biblioteca gigante. Citados a su fecha, sin reconteo de hoy: Animetail (★579 del 15-sep) y Suwayomi (empuje del 12-sep, por su pieza). La búsqueda fresca de prensa/web sobre el tema no añadió hechos firmes fuera de los repos — se declara aquí como vacío honesto. Datos históricos (cierre de enero de 2024, linajes) constados a su día. Cada placa lleva recibo; nada viene de memoria.

───────────────────

✍️ FIRMA Y DESPEDIDA

Pieza 06 de La Bandita, edición dominicano-español, verificada con la vara de la casa el 22 de septiembre de 2026. Cerró dentro de su banda (WhatsApp, 62 000–64 000 caracteres): el número exacto quedó en el acta viva del día.

El maestro cerró su taller hace casi tres años, y los aprendices levantaron los suyos — unos con la persiana subida esta misma mañana, otros con el martillo todavía en la mano del verano. No compres apellidos: mira quién barre. Instala desde Releases con tag y fecha, respalda con liturgia y elige el taller por la materia que lees — no por el nombre que supiste.

Busca más, y que tu taller levante la persiana contigo.

> «La Bandita informa a partir de fuentes fechadas. Un fork no es una razón; el repo vivo sí. Y el dueño, más.»

───────────────────

#LaBandita #LectoresLibres #Mihon #Aniyomi #NekoMangaDex #Komikku #ForksSaludables #GitHubDeConfianza #VerificaAntesDeInstalar #FuenteFechada #EcosistemaLibre #RepublicaDominicana
