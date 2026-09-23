# Publicación 12 — FMHY es una wiki de pistas, no un catálogo: discovery ≠ verificación

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🌐 Qué es FMHY y cómo funciona
├── 🧩 Lo que su navegación revela hoy
├── 🔒 El interstitial Base64 (qué es y qué no es)
├── 📦 El repo detrás de la wiki
├── 🧭 Discovery ≠ verificación: el embudo completo
├── 🔬 Un ejemplo real, de punta a punta
├── 📌 La corrección a la «gran ola» de abril
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

FMHY — «freemediaheckyeah» — se presenta como «la mayor colección de cosas gratis de internet». Es una wiki comunitaria enorme, viva hoy, y con un papel preciso en el mapa del conocimiento: **es un descubridor de primer nivel y un verificador de nada.**

La diferencia importa porque abril lo demostró con daño: alguien vació una porción de la wiki en un hilo de 340 mil caracteres y lo vendió como catálogo verificado. No lo era. Cada pista de FMHY es un primer eslabón — abrir la casa del proyecto, leer su licencia, comprobar su versión y su dueño es el trabajo que nadie puede hacer por ti, ni esta wiki ni esta guía.

Estado de hoy, 14 de septiembre: el sitio responde con su post mensual de septiembre activo, su guía de principiantes carga, y el repo que la genera suma ★14.592 — con la particularidad de que su código git no empuja desde mayo, y la wiki no por eso está muerta. Ambas cosas, contadas abajo.

## 🌐 Qué es FMHY y cómo funciona

https://fmhy.net

FMHY es una wiki mantenida por su comunidad: miles de entradas de herramientas, sitios y recursos organizados por categorías — privacy, AI, video, audio, gaming, reading, downloading, torrenting, educational, mobile, linux-macos, non-english, misc, entre otras. Su mecánica:

- La comunidad propone y curada entradas continuamente.
- Un changelog registra qué cambió — y su ritmo es visible: la wiki publica **posts mensuales de novedades** (el de septiembre de 2026 está en línea hoy).
- Hay variante SFW (sin contenido adulto) para quien la prefiera.
- La cultura del proyecto es la de un índice: describe, enlaza, no garantiza.

Su tamaño es su virtud y su límite: cubre todo, no audita nada. Es la biblioteca más grande del mundo en su género — y como toda biblioteca grande, el valor no está en tenerla toda: está en saber usar el catálogo.

## 🧩 Lo que su navegación revela hoy

La barra del sitio, abierta hoy, es una lección de lo que la wiki piensa de sí misma:

```
📑 Changelog    qué cambió y cuándo
📖 Glossary     el diccionario de sus términos
💾 Backups      cómo obtener la wiki entera
🌱 Ecosystem    las variantes y proyectos hermanos
❓ FAQs          las preguntas del proyecto
✅ SafeGuard    su capítulo de seguridad
🚀 Startpage    su propuesta de página de inicio
🔎 SearXNG      búsqueda propia
😇 SFW FMHY     la versión sin adulto
🏠 Selfhosting  cómone la montas en tu servidor
```

Fíjate en lo que esa barra dice sin decirlo: un proyecto que publica su changelog, mantiene glosario, ofrece backups de sí misma y tiene capítulo de seguridad se toma en serio como infraestructura. Sigue siendo un índice de pistas — pero de los organizados.

## 🔒 El interstitial Base64 (qué es y qué no es)

Al entrar, FMHY a veces muestra un aviso sobre enlaces codificados en Base64. Qué hay detrás, sin vueltas:

```
Es:    una medida de diseño. Algunos enlaces de la
       wiki se publican codificados para que los
       rastreadores automáticos no los indexen.
       El propio sitio ofrece un decodificador en página.

No es: un sistema de seguridad, ni un rito obligatorio,
       ni una instrucción de esta guía. El usuario
       decide si usa esa vía; el decodificador es
       del sitio y corre en tu navegador.

Y no es: motivo para copiar enlaces codificados en
       un post. Aquí van enlaces en claro o no van.
```

La wiki hace su ingeniería para sobrevivir a los indexadores; esta familia de guías hace la suya para no pegar recetas. Cada cual protege lo suyo.

## 📦 El repo detrás de la wiki

https://github.com/fmhy/FMHY

★14.592 · último push del 13 de mayo de 2026 · licencia: sin clasificar en su página (se dice tal cual — la wiki define su propia política de contenido en su sitio).

La curiosidad que enseña algo: el git lleva meses quieto y la wiki está viva — re-verificado HOY, 15-sep: carga con su post de septiembre. ¿Cómo? La wiki se sirve por vías propias (su web y sus despliegues) y el repo público no refleja cada movimiento. La lección general que ya viste en esta familia: **git quieto ≠ proyecto muerto; proyecto vivo ≠ todo verificado.** Un repo es una capa, no el proyecto entero.

## 🧭 Discovery ≠ verificación: el embudo completo

La regla de la casa cabe en una línea — encontrar no es verificar. Desplegado, el embudo que convierte una pista en algo citable:

```
1. DESCUBRIMIENTO
   FMHY (o un grupo, o un amigo) dice:
   «esta app es buena».
   ── esto vale exactamente cero como verificación.

2. APERTURA
   Se abre la casa del proyecto — su repo o sitio —
   ESE DÍA. No el recorte del grupo: la casa.

3. LECTURA
   ¿Quién es el dueño? ¿Desde cuándo existe?
   ¿Qué licencia declara? ¿Cuándo fue su última
   versión y su último push? ¿Está archivado?

4. CONTRASTE
   ¿Lo nombran otras fuentes independientes?
   ¿Su comunidad responde issues?
   ¿Su firma/checksums son públicos?

5. USO REAL
   ¿Alguien de carne y hueso lo usa y puede
   contar cómo le va? El uso real es la última
   puerta — y la única que nadie puede abrir por ti.

6. FICHA
   Recién entonces: una ficha con fecha, en una
   guía como esta. Y con fecha de caducidad.
```

Cualquier atajo que se salte pasos — «está en FMHY, punto», «lo recomiendan en Telegram, punto» — es el gesto exacto que hizo del hilo de abril un estorbo de 340 mil caracteres.

## 🔬 Un ejemplo real, de punta a punta

Para que el embudo no quede en teoría, el recorrido que ya hizo esta familia con una entrada real:

```
1. La wiki (y medio internet) menciona «Mihon»
   como lector de manga.

2. Se abre la casa: github.com/mihonapp/mihon

3. Se lee: 23.575 estrellas · Apache-2.0 ·
   versión 0.20.4 de agosto · push de HOY ·
   organización mihonapp con historial desde 2024.

4. Se contrasta: Keiyoushi (el almacén de
   extensiones) lo lista primero entre las apps
   soportadas; sus issues tienen actividad; la
   comunidad del ecosistema lo nombra como el
   sucesor de hecho de Tachiyomi.

5. Uso real: la gente de la banda que lo usa,
   con su opinión.

6. Ficha: hoy Mihon tiene guía propia dentro de
   esta familia (la de forks de lectores), con su
   fecha de corte.
```

Seis pasos. Todo lo que hace falta para que «Mihon» pase de pista a información. Y todo lo que NO pasó el día que alguien pegó una wiki entera en un hilo.

## 📌 La corrección a la «gran ola» de abril

```
Lo que hizo abril                Lo que hace esta familia
Vaciar FMHY en un post           Abrir la casa de cada pista
Vender la wiki como verificación Presentar la wiki como descubrimiento
340 mil caracteres sin dueño     Fichas cortas, fechadas, con casa
Índices de instalación pegados   El índice se lee en la casa del
                                 proyecto, nunca en un post
«Todo gratis, todo seguro»       Cada ficha con su límite y su fecha
```

La wiki no era el problema. El problema era el gesto: presentar acumulación como verificación. Ese gesto es lo que esta familia de guías existe para no repetir.

## ❓ Preguntas frecuentes

**¿Puedo usar FMHY?**
Puedes leerla: es pública y su papel como índice es legítimo. Lo que esta guía no hace es mandarte a sus destinos ni vaciarla aquí. Cada clic dentro de ella es un descubrimiento — el verificación va aparte, con el embudo de arriba.

**¿Es más segura que googlear?**
No se afirma. Es otra lista, curada por otra gente, con otros incentivos. Los buscadores te mandan a anuncios pagados; las wikis, a lo que la comunidad anotó. Ninguna de las dos puertas verifica por ti.

**¿Su sección de Android reemplaza la guía de tiendas de esta familia?**
No. La guía de tiendas abrió cada proyecto el día del corte; una sección de wiki es una lista con otra fecha y otro criterio.

**¿Y su sección de música?**
Misma respuesta: la familia tiene guía de música con las fichas verificadas. La wiki puede apuntar a lo mismo — o a cosas que nadie abrió todavía.

**¿El repo dice mayo pero la wiki está viva, cuál es la verdad?**
Las dos: la wiki se sirve por despliegues propios y el repo no refleja cada cambio. Git quieto no es proyecto muerto — ya lo decía la lección del repo.

**¿Base64 es piratería?**
Es codificación de texto — la misma técnica que tu teléfono usa para mandar imágenes por correo. El uso que cada quien le dé a los enlaces es su asunto y su ley. Aquí no se decodifica nada para nadie.

**¿Entonces para qué sirve FMHY, al final?**
Para lo que dijo su definición: el índice más grande del ecosistema. Como mapa de qué EXISTE, no tiene rival. Como prueba de qué funciona y es seguro, no vale nada — y no pretende valerla.

## 🔗 Enlaces

- La wiki: https://fmhy.net
- Guía de principiantes: https://fmhy.net/beginners-guide
- Post de septiembre: https://fmhy.net/posts/sept-2026
- El repo: https://github.com/fmhy/FMHY

> La Bandita informa a partir de fuentes fechadas. La wiki de pistas no es un catálogo — y el que descubre, todavía no verificó.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: wiki re-verificada viva a HOY. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.
