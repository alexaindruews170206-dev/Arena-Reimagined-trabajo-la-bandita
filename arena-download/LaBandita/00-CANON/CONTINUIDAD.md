# ENTREGA DE CONTINUIDAD — La Bandita, era dominicana — corte 2026-09-22

Documento puente para continuar la operación en **otro chat** sin perder nada. Sucede al documento del 20-sep (era multilengua), que queda como acta histórica en el respaldo. La operación se REABRIÓ por orden del dueño el 22-sep, tras la desconexión.

---

## 1. Cómo usar este documento

1. El canon normativo vive en `00-CANON/` — este documento solo es el mapa; la regla vive allá.
2. El estado vivo pieza por pieza está en `02-ARCHIVO/estado-expansion-ES-2026-09-22.md` (append-only). Ahí se mira la última pieza cerrada antes de hornear.
3. Si el dueño dice «arranca» o «sigue», se retoma desde ese acta sin nueva confirmación (Tratado V.0.05, Art. D-008).

---

## 2. Fuentes normativas vigentes (`00-CANON/`)

| Fichero | Rol | Versión |
|---|---|---|
| `TRATADO.md` | Tratado vigente | **V.0.05** Edición Dominicana Revisada — Libro D (modo monolingüe, clases 63k/40k, título limpio, anatomía con mapa mental y meme, Anexo Q mapa maestro, T10/T11 resueltas) + fe de erratas E01–E05 de la revisión integral de 154 puntos (22-sep noche) |
| `MANUAL-COMPLETO.md` | Manual vigente | **V2.1** — §6 (protocolo editorial: ciclo de pieza, taller del meme, #tags, recetario de nombres, anti-timeout) y §7 (registro, con la precisión V2.1: secciones 1–4 — errata «1–5» corregida y fichada el 22-sep noche) |
| `MANUAL-FICHAS-FALLOS.md` | Fichas de uso diario | sin cambio (las 75 fichas, deduplicadas) |
| `LECCIONES-ALEXIS.md` | Memoria entre sesiones | **V.22-sep** — cuatro entradas del 22-sep (foco ES, cuerpos por plataforma, semilla y meme, revisión del trío) |
| `AMPLIACION-ALMENDRA.md` | Ampliación: canciones | sin cambio (anexo doctrinal) |
| `LECCIONES-EXTRA-ARCHIVO.md` | Archivo, NO norma | sin cambio |
| `REGISTRO-VERIFICACION-14sep.md` | Acta histórica | sin cambio |
| `_versiones/` | Copias congeladas | Tratado V.0.03 y V.0.04 · Manual V1 · Lecciones 20-sep |

---

## 3. Decisiones de la era dominicana (resumen subordinado al Libro D)

- **Modo monolingüe:** solo español dominicano × (Facebook + WhatsApp). Lo demás fue eliminado del workspace por orden del dueño (22-sep): lenguas no ES, plataformas no FB/WA, cortes stale, ZIP anidado. **Respaldo íntegro:** `workspace.zip` en `/home/user/`, SHA-256 `adf1dfe2…` registrado en `02-ARCHIVO/RESPALDO-workspace-zip-SHA256.txt`. **No-reactivación sin orden expresa.**
- **Formato (D-002):** WhatsApp = completa, clase 63 000 ± 1 000 caracteres; Facebook = compacta, clase 40 000 ± 1 000; misma verdad, prosa distinta, **prohibido** el copiado byte a byte (la vieja regla de gemela octeto-a-octeto quedó derogada con acta: tensión T10 resuelta).
- **Título limpio (D-003):** el H1 no lleva «Publicación NN»; el número vive solo en nombre de archivo y ZIP; cero meta-comentarios de IA en lo publicado.
- **Anatomía obligatoria (D-004):** semilla de entrada → mapa de la guía → una página → **mapa mental** (no se omite) → fichas → meme textual ORIGINAL con humor y a tema → método → glosario → enlaces → nota de verificación fechada → firma → despedida → #tags al final.
- **Voz (D-005):** español dominicano; estilo semilla/infantil solo como recurso de claridad, jamás contra la precisión.
- **Plan (D-006/D-010 + acta §3):** piezas 01–79 existentes se expanden con novedad real; 80 (emulación) se amplía con los recursos ordenados (EmuHub-APP, Neo Geo Vault 87,9 MB pendiente de constatar, appteka 586r323266, axekin, FMHY, appteka); 81–110 nuevas por familias del banco de exploración; índices 00/20/78 al final.

---

## 4. Estado al corte 22-sep-2026

- Canon versionado y congelado (ver §2). Estructura limpia: `00-CANON/` · `01-PUBLICACIONES/Facebook-dominicano-ES/` · `01-PUBLICACIONES/WhatsApp-dominicano-ES/` · `01-PUBLICACIONES/_archivo-15sep/` · `02-ARCHIVO/`.
- **Pieza 01 cerrada y VERDE en ambas plataformas:** WA 63 810 c · FB 39 136 c (detalle en acta §2).
- Piezas 02–79 pendientes de expansión (trabajables desde sus madres del corte 15-sep, hoy archivadas en `01-PUBLICACIONES/_archivo-15sep/` a medida que se cierren; hasta entonces siguen en las carpetas activas).
- Pieza 80 por expandir; 81–110 por hornear.

## 5. Vara de verificación de pieza (resumen operativo)

Por pieza y plataforma: (1) caracteres en banda (WA 62 000–64 000 · FB 39 000–41 000, `len()` en Python); (2) H1 sin «Publicación NN»; (3) sin meta-comentarios de IA; (4) semilla, mapa mental, meme, nota de verificación, firma y #tags presentes; (5) ningún número de pieza en el cuerpo; (6) los recursos nuevos de la pieza abiertos con fecha en la apertura; (7) prosa WA ≠ FB (solo coinciden líneas de datos/enlaces). VERDE en las dos antes de registrar en el acta.

## 6. Errores a no repetir (los del 20-sep, vigentes, más los de hoy)

1–12. Los doce del documento anterior (globs de dos dígitos, tuplas para corpus, gemela última, `ls` antes de escribir, heredocs flush-left, auto-test de vara, etc.).
13. **No copiar WA a FB ni al revés** (T10 resuelta; quien lo haga rompe la orden del dueño y falsea la verificación).
14. **No poner «Publicación NN» en el H1** (T11 resuelta) ni meta-comentarios sobre el título; la nota de verificación al final SÍ vive (es contenido de confianza, no meta).
15. **Checker estricto pero no injusto:** la vara de meta-IA del 22-sep dio un falso positivo con «Aquí está, desarmada…» (frase de contenido) — la vara se afina, no se borra; anotado para que no vuelva a marcar inocentes.
16. **Editar siempre sobre archivo real:** un intento de edición cayó en ruta inexistente (desliz, sin efecto) — confirmar la ruta con `ls` antes de cada `edit_file` sobre fichas.

---

*Era dominicana iniciada el 22-sep-2026 por orden del dueño. La Bandita informa a partir de fuentes fechadas. Lento pero firme; la vara contigo.*
