# Guía de versionado multiplataforma y multiidioma — La Bandita
**Documento de método · 15 de septiembre de 2026 · madrugada XXXV · fuente del proyecto 04-VERSIONES-MULTIIDIOMA/**

## ⚡ El contexto que manda

La casa creció: **el grupo de 40 personas es ahora una comunidad de 4.198 y subiendo**, repartida en canal de **Discord**, grupo de **WhatsApp**, **Facebook**, **Reddit**, **Telegram** y el foro de la comunidad (**Rethubs**). En Discord existe un subcanal de recomendaciones de código abierto (creado por un amigo de la casa, junto a otro colaborador, para un proyecto pequeño entre panas — **nada profesional, y así se declara en cada pieza: sin soporte oficial, sin promesas**). Con mucha gente encima, la regla es una: **no descarrilar**. Esta guía existe para eso: que cada versión —en cualquier plataforma y cualquier idioma— suene a la misma casa.

**Regla P10 extendida:** nombres de terceros (colaboradores, amigos, receptores) y datos personales NO entran en piezas públicas. El contexto interno vive solo en Handoff y Registro.

## 🏛️ Plataformas: qué cambia en cada una (investigación de cultura)

| Plataforma | Cultura y formato | Qué cambia vs. Facebook/WhatsApp | Prohibiciones de la casa |
|---|---|---|---|
| **Discord** | Canal en vivo; mensajes cortos; hilos (threads) para profundidad; fijados (pins) para lo permanente; emoji natural | Pieza = 2–3 bloques cortos, no ensayo; lista top-10, no top-20 (el resto va a hilo fijado); tono conversación, no manifiesto | Muros de texto >30 líneas; @everyone sin permiso; firmas largas |
| **Reddit** | Subreddits con reglas propias; Reddiquette; TL;DR obligatorio en posts largos; cultura de «Edit:»; el voto decide; anti-autopromoción descarada | Título honesto y concreto sin clickbait; TL;DR arriba; divulgación transparente («somos un proyecto pequeño, no comercial»); «Edit» fechado si cambia algo | Hashtags (no existen en Reddit); pedir votos; cross-postear el mismo texto a 10 subs el mismo día |
| **XDA Developers** | Foro técnico; hilo único por tema (OP); plantillas reconocibles: [APP], [GUIDE], [REFERENCE]; secciones esperadas: intro, requisitos, enlaces, changelog, créditos | Estructura de OP completa; el MÉTODO de verificación se explica (a XDA le importa el cómo); changelog fechado; tono técnico-seco con cortesía | Presentar una lista de terceros como si fuera [APP] propia; enlaces acortados; sin fuente de datos |
| **Telegram** (reservada, hornada 4) | Post de canal: primeras 2 líneas = preview; enlaces con embed; reacciones | Brevedad tipo Discord + archivo adjunto o enlace fijo | Muros de texto; spam de canales |
| **Rethubs** (reservada, hornada 4) | Foro de comunidad propia: tema fijo (pin), respuestas ordenadas | Formato hilo introductorio + FAQ; se actualiza por edición, no por posts nuevos | Duplicar temas; actualizar sin nota de edición |

## 🌍 Idiomas: adaptación de contexto, no traducción (7 normas)

| Carpeta | Idioma | Decisiones de adaptación |
|---|---|---|
| `dominicano-ES` | Español dominicano (casa madre) | El original. «Pana», «fino», «tas claro» con mesura: calidez sin caricatura. Números 319.420 |
| `ingles-US` | Inglés (EE. UU.) | Llano y directo; nada de «spanglish» de marketing; open source sin guion es lo normal en EE. UU.; números 319,420; TL;DR real |
| `frances-FR` | Francés | Espacio fino antes de «:» y «!»; «logiciel libre» y «open source» ambos válidos (se usa open source en contexto GitHub); vouvoiement comunitario, no solemne; números 319 420 |
| `portugues-BR` | Portugués (Brasil) | «código aberto», trato «você», calidez brasileña natural; NO portugués de Portugal; números 319.420 |
| `hindi-IN` | Hindi | Devanagari con **términos técnicos en inglés** (star, open source, GitHub) — así escribe la comunidad técnica india real; traducirlos sería señal de traducción automática; números 319,420 |
| `chino-CN` | Chino mandarín (simplificado) | 开源 (código abierto), 星标 (estrella); **números grandes en 万** (31.9万 = 319.420) — formato real de las comunidades técnicas chinas; puntuación china (，。「») |
| `ruso-RU` | Ruso | «опенсорс» coloquial aceptado, «открытый код» formal; tono directo sin adornos; números 319 420 |

**Glosario de la casa (se mantiene igual en todos los idiomas):** el nombre **La Bandita** no se traduce ni se declina. «Gemelas» (copias byte a byte) = *twins* / *jumelles* / *gêmeas* / *जुड़वाँ* / *双胞胎* / *близнецы*. La firma ritual se adapta una sola vez por idioma y queda fija: «La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan».

## 🛡️ Protocolo anti-descarrile (para 4.198 personas)

1. **Nada se publica sin fecha y fuente** — el antídoto del descarrile es el número constado.
2. **Una pieza por plataforma por turno** — el fuego masivo parece spam y provoca baneos (Reddit/XDA son estrictos).
3. **«No es profesional» se dice con orgullo** — proyecto entre amigos, sin soporte oficial: se aclara en cada pieza para que nadie espere garantías.
4. **Ante trolls o dudas: el acta manda** — se responde con la fecha y el método, una sola vez; a la segunda, silencio. La casa no se pelea en los comentarios.
5. **Sin nombres de terceros, sin claves, sin datos crudos** — igual que siempre.
6. **Cada idioma es ciudadano de primera** — si una versión no está bien redactada, no sale. Mejor una hornada buena que cinco apuradas.
7. **El meme se adapta, no se pega** — el humor que no suena natural delata a la máquina.

## 🗂️ Estructura y plan por hornadas

Árbol: `04-VERSIONES-MULTIIDIOMA/<plataforma>/<idioma>/` — plataformas: discord, reddit, xda, facebook, whatsapp (+ telegram, rethubs reservadas). Idiomas: ingles-US, dominicano-ES, frances-FR, portugues-BR, hindi-IN, chino-CN, ruso-RU.

- **Hornada 1 (HOY, 15-sep):** pieza 75 «El podio de la mina» — recomendaciones de código abierto, justo para el subcanal base-AI — en **Discord ×7, Reddit ×7, XDA ×7** + **Facebook/WhatsApp en ingles-US y portugues-BR** (25 piezas). Mejora fechada sobre el original ES: **top-20 deduplicado** (ente ×2 = espejo; T8RIN/ImageResizer+ImageToolbox = mismo proyecto renombrado; entran Operit ★7.836 y NewsBlur ★7.620).
- **Hornada 2:** pieza 79 «La octogésima» (la presentación de la casa) en la misma matriz.
- **Hornada 3:** Facebook/WhatsApp en francés, hindi, chino y ruso.
- **Hornada 4:** Telegram y Rethubs (formatos propios).
- **Hornada 5+:** series a pedido del dueño (el Mapa manda: lo que él pida, no lo que a la casa se le ocurra).

## ✍️ Convención de archivos

`<número>-<slug>-<PLATAFORMA>-La-Bandita-2026-09-15-<idioma>.md` — ejemplo: `75-El-podio-de-la-mina-Discord-La-Bandita-2026-09-15-es-DO.md`. Cada pieza declara en su cabeza: plataforma, idioma, fuente (pieza ES madre) y fecha de verificación.

> La Bandita verifica antes de recomendar — en los siete idiomas y en todas las plazas. Las estrellas adornan; las fechas mandan; y con 4.198 mirando, cada palabra sale con fecha, fuente y calma.


---

## 📌 Estado de continuación (17-sep, cierre de sesión — se termina en otra sesión)

| Lengua | discord | reddit | xda | telegram | rethubs | facebook | whatsapp |
|---|---|---|---|---|---|---|---|
| ingles-US | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| dominicano-ES | ✓ (madre, read-only) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| frances-FR | 78/78 ✓ | 78/78 ✓ | 78/78 ✓ | 79/79 ✓ | 79/79 ✓ | **30/79** | **30/79** |
| portugues-BR | sonda 75 | sonda 75 | sonda 75 | — | — | — | — |
| hindi-IN / chino-CN / ruso-RU | sonda 75 | sonda 75 | sonda 75 | — | — | — | — |

- **Sigue así:** FB+WA·FR 31→74 y 76→79 (gemelas byte-a-byte, verify por bloque, molde `archivo/molde-fb-en.md`, meta copiada de la sonda 75) → PT-BR → HI → zh-CN → RU. Sondas 75/79 NO tocar. Pieza WebView v154 AL FINAL. MCP de GitHub del dueño: usarlo para barridos vivos cuando esté; si no, REST anónima racionada.
- Registro del día y método: `archivo/verificacion-recursos-2026-09-17.md` · contador de la orden: `archivo/estado-mega-orden-multiidioma.md`.
