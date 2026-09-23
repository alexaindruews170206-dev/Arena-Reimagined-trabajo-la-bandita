# Publicación — Música FOSS (La Bandita) · 2026-09-13
> BORRADOR · Facebook / La Bandita · no Discord. Perfil FACEBOOK (Manual 5.2).
> POST: copia desde la primera línea del título hasta hashtags. COMENTARIO FIJADO al final, no es el post.
> No publicar sin firma humana.

MÚSICA FOSS hasta hashtags.

MÚSICA FOSS · La Bandita · 2026-09-13 (BORRADOR · firma humana pendiente)
**Tiempo estimado de lectura: 24–34 min**
**Índice:** mapa + el mismo icono.

# Clientes de música con repo. Spotify crackeado no entra.

**Corte:** 2026-09-13. API GitHub. Sin instalar. Sin cuenta de YouTube Music.
**No es:** «alternativas pirata a Spotify», ni receta para saltarse ToS, ni el hilo de 340k de abril recalentado.

```
Mapa

├── ⚡  En una página
├── ⚖️  Qué no es esta guía
├── 📻  NewPipe
├── 🎵  InnerTune y OuterTune
├── 📦  RiMusic está archivado
├── 🎧  SimpMusic
├── 📂  Auxio (archivos locales)
├── 🎙️  AntennaPod (podcasts)
├── 🚫  Lo que no se pega
├── 📌  Correcciones al 340k de abril
├── ❓  FAQ
├── 🚧  Límites
├── 📚  Fuentes
└── 🏁  Cierre
```

---

## ⚡ En una página

Hoy, API:

```
TeamNewPipe/NewPipe
  39.668 ★  GPL-3.0  v0.29.1 (15-ago-2026)
  push 31-ago-2026  no archivado
  «libre lightweight streaming front-end for Android»

z-huang/InnerTune
  6.084 ★  GPL-3.0
  push 13-nov-2025  no archivado
  Material 3 YouTube Music client

OuterTune/OuterTune
  5.393 ★  GPL-3.0
  push 6-sep-2026  no archivado
  latest v0.10.1 (19-dic-2025)
  «Forked from» InnerTune, según su description

fast4x/RiMusic
  3.903 ★  GPL-3.0  ARCHIVADO
  último push 30-jul-2025

maxrave-dev/SimpMusic
  11.202 ★  GPL-3.0  v2.1.0 (7-sep-2026)
  push 11-sep-2026
  «cross-platform music app using YouTube Music for backend»

OxygenCobalt/Auxio
  4.267 ★  GPL-3.0
  push 8-sep-2026
  «simple, rational music player» — local

AntennaPod/AntennaPod
  8.148 ★  GPL-3.0  3.12.1 (5-sep-2026)
  push 12-sep-2026
  podcasts
```

---

## ⚖️ Qué no es esta guía

YouTube y YouTube Music tienen términos. Un cliente FOSS que habla con esos servidores puede chocar con esos términos. **Esta guía no es un bufete.** No dice «es legal». Dice: este repo existe, esta licencia, esta release, este push.

No se enlazan APK de mods «Spotify Premium». Misma regla que HappyMod (pub 01).

No se copia FMHY/audio. Eso es la pub 12: cómo leer una wiki, no cómo vaciarla aquí.

---

## 📻 NewPipe

https://github.com/TeamNewPipe/NewPipe

El más grande en ★ de esta lista. Front-end ligero de streaming, no un clon de YouTube Music con biblioteca de álbumes. v0.29.1 = 15-ago. Push 31-ago: el código se movió después del tag. No se afirma v0.29.2.

[Observación] F-Droid suele ser el canal histórico de NewPipe. **F-Droid no se reabrió para esta ficha.** No se recita la versión de F-Droid.

---

## 🎵 InnerTune y OuterTune

https://github.com/z-huang/InnerTune — 6.084 ★, último push **noviembre 2025**. Vivo en el sentido de no archivado. Lento en el sentido de diez meses sin push.

https://github.com/OuterTune/OuterTune — 5.393 ★, push **6-sep-2026**, description de API: player Material 3 con archivos locales y YouTube Music, fork de InnerTune. Latest **v0.10.1 es de diciembre 2025**. Otra vez: push ≠ tag. Hay código de septiembre y un APK de diciembre. Quien instale, que abra Releases ese día.

Malopieds/InnerTune (821 ★, push mar-2025) no es el canónico de esta ficha.

---

## 📦 RiMusic está archivado

https://github.com/fast4x/RiMusic — 3.903 ★, **archived**, último push 30-jul-2025. El archivo viejo de 340k lo trataba como vivo. Art. 63: historia. nishant6342/RiMusic: 2 ★, push 2023. Craeckie/RiMusic: 0 ★, 2024. No se recomiendan como sucesores.

Si alguien te pasa «RiMusic actualizado» en Telegram: letrero. Pub 01.

---

## 🎧 SimpMusic

https://github.com/maxrave-dev/SimpMusic

11.202 ★, v2.1.0 el **7-sep-2026**, push 11-sep. GPL-3.0. Description: cross-platform, backend YouTube Music.

[Observación] Es el que, hoy, combina ★ altas + release de esta semana. Eso no es «el mejor». Es el más fácil de datar como activo en esta caja.

No se abrió la Play Store. No se afirma que esté ahí.

---

## 📂 Auxio (archivos locales)

https://github.com/OxygenCobalt/Auxio

4.267 ★, GPL-3.0, push 8-sep. Player de archivos que ya tienes. No es un cliente de YouTube Music. Si tu música está en el teléfono, esta ficha aplica. Si tu música está en la nube de Google, no.

---

## 🎙️ AntennaPod (podcasts)

https://github.com/AntennaPod/AntennaPod

8.148 ★, 3.12.1 el 5-sep-2026, push 12-sep. Gestor de podcasts. No es un reemplazo de Spotify. Es otra categoría. Se pone aquí porque el hilo viejo mezclaba «música y podcasts» en 340k caracteres.

---

## 🚫 Lo que no se pega

```
- APK de Spotify/YouTube Music «premium»
- Listas de FMHY/audio
- Discord
- Recetas de NewPipe para URLs de YouTube
  (cada quien abre el README el día que use)
```

---

## 📌 Correcciones al 340k de abril

```
ANTES                    AHORA
RiMusic vivo             Archivado (30-jul-2025)
InnerTune = el cliente   InnerTune lento (nov-2025);
                         OuterTune empuja (sep-2026)
                         con tag de dic-2025
Lista interminable       Seis repos abiertos hoy.
                         C05 no manda.
«340k de alternativas»   Inflar no verifica.
```

---

## ❓ FAQ

**¿Cuál instalo?**
El que uses. Local → Auxio. Podcasts → AntennaPod. YouTube front-end → NewPipe. YT Music clients → OuterTune / SimpMusic, con ToS a tu riesgo. RiMusic no.

**¿Es legal?**
No es un bufete.

**¿OuterTune v0.10.1 de diciembre con push de septiembre?**
Sí. Tag viejo, código más nuevo. Quien quiera el tag, tag. Quien quiera el commit, que compile.

**¿F-Droid?**
No se reabrió hoy para estas fichas.

**¿Discord?**
No hay envío.

---

## 🚧 Límites

```
CAMPO DE VERDAD — Música · 2026-09-13
API abierta para los siete repos de arriba.
No se instaló. No se hizo cuenta. No se midió
calidad de audio. No se abrió FMHY/audio.
```

---

## 📚 Fuentes

https://github.com/TeamNewPipe/NewPipe
https://github.com/z-huang/InnerTune
https://github.com/OuterTune/OuterTune
https://github.com/fast4x/RiMusic
https://github.com/maxrave-dev/SimpMusic
https://github.com/OxygenCobalt/Auxio
https://github.com/AntennaPod/AntennaPod

---

## 🏁 Cierre

El hilo de 340k se caducó. RiMusic está archivado. InnerTune empujó por última vez en 2025. OuterTune y SimpMusic se mueven. Auxio toca archivos. AntennaPod toca feeds. NewPipe es otra especie. Nada de esto es Spotify premium de Telegram.

> La Bandita informa a partir de fuentes fechadas.

#NewPipe #OuterTune #SimpMusic #Auxio #AntennaPod #FOSS #LaBandita #Septiembre2026

---
COMENTARIO FIJADO — no forma parte del post. Primer comentario, fijar.

Música FOSS — La Bandita
Fecha: 2026-09-13
Versión: BORRADOR 2026-09-13

Índice (el mismo icono abre cada bloque)

⚡ En una página
⚖️ Qué no es
📻 NewPipe
🎵 InnerTune / OuterTune
📦 RiMusic archivado
🎧 SimpMusic
📂 Auxio
🎙️ AntennaPod
🚫 No se pega
📌 Correcciones
❓ FAQ
🚧 Límites
📚 Fuentes
🏁 Cierre

Corrección: RiMusic archivado. InnerTune lento. OuterTune y SimpMusic se mueven.
