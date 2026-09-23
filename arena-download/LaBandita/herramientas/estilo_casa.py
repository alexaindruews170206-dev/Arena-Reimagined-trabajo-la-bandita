#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
estilo_casa.py — taller de La Bandita (herramienta, no canon — Art. D-011)

Convierte una pieza Markdown crudas a texto NATIVO de plataforma:
  wa  : gramática que WhatsApp sí formatea (*negrita* con 1 asterisco,
        _cursiva_, ```monoespaciado```, > cita, listas, separador ─)
  fb  : Facebook no formatea NADA → texto plano prosódico al 100 %
        (━ separadores, • ✔ → listas, «énfasis», ❝citas❞, sin un solo
        símbolo Markdown).

Uso:
    python3 estilo_casa.py wa entrada.md salida.md
    python3 estilo_casa.py fb entrada.md salida.md

El conversor es tonto por diseño: la vara humana revisa la salida
(D-011.6). No toca: URLs, contenido de cajas, tags, fecha, firma.
"""
import re
import sys

SEP_WA = '─' * 19
SEP_FB = '━' * 15


def _split_fences(texto):
    """Devuelve lista de (es_caja, contenido) alternando prosa/cajas ```."""
    partes, actual = [], []
    es_caja = False
    for linea in texto.split('\n'):
        if linea.strip().startswith('```'):
            partes.append((es_caja, '\n'.join(actual)))
            actual = []
            es_caja = not es_caja
            continue
        actual.append(linea)
    partes.append((es_caja, '\n'.join(actual)))
    return partes


def _tabla_a_caja_wa(lineas_tabla):
    """Tabla |a|b| → caja monoespaciada alineada (WhatsApp)."""
    filas = []
    for li in lineas_tabla:
        celdas = [c.strip() for c in li.strip().strip('|').split('|')]
        filas.append(celdas)
    filas = [f for f in filas if not all(re.fullmatch(r':?-{2,}:?', c or '---') for c in f)]
    filas = [[c.replace('**', '') for c in f] for f in filas]
    if not filas:
        return ''
    ncols = max(len(f) for f in filas)
    anchos = [0] * ncols
    for f in filas:
        f += [''] * (ncols - len(f))
        for i, c in enumerate(f):
            anchos[i] = max(anchos[i], _ancho(c))
    salida = []
    for k, f in enumerate(filas):
        celdas = [c + ' ' * (anchos[i] - _ancho(c)) for i, c in enumerate(f)]
        salida.append(' · '.join(celdas).rstrip())
        if k == 0 and len(filas) > 1:
            salida.append('─' * min(28, sum(anchos) + 3 * (ncols - 1)))
    return '```\n' + '\n'.join(salida) + '\n```'


def _tabla_a_bullets_fb(lineas_tabla):
    salida = []
    for k, li in enumerate(lineas_tabla):
        celdas = [c.strip() for c in li.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-{2,}:?', c or '---') for c in celdas):
            continue
        limpias = [c.replace('**', '') for c in celdas if c]
        if k == 0:
            salida.append('▸ ' + ' / '.join(limpias))
        else:
            salida.append('• ' + ' → '.join(limpias) if len(limpias) > 2
                          else '• ' + ' — '.join(limpias))
    return '\n'.join(salida)


def _ancho(s):
    return len(s)


def _ultimo_separador(res, sep):
    for li in reversed(res):
        if not li.strip():
            continue
        return li.strip() == sep
    return False


def _negritas_a_mayus_fb(match):
    interior = match.group(1)
    palabras = interior.split()
    if len(palabras) <= 3 and len(interior) <= 30 and not re.search(r'[.]', interior):
        return interior.upper()
    return '«' + interior + '»'


def convertir_wa(texto):
    partes = _split_fences(texto)
    salida = []
    for es_caja, bloque in partes:
        if es_caja:
            salida.append('```\n' + bloque.strip('\n') + '\n```')
            continue
        lineas = bloque.split('\n')
        res, i = [], 0
        while i < len(lineas):
            li = lineas[i]
            if li.strip().startswith('|') and '|' in li.strip()[1:]:
                j = i
                while j < len(lineas) and lineas[j].strip().startswith('|'):
                    j += 1
                res.append(_tabla_a_caja_wa(lineas[i:j]))
                i = j
                continue
            m = re.match(r'^(#{1,6})\s+(.*)$', li)
            if m:
                titulo = re.sub(r'\*\*(.+?)\*\*', r'\1', m.group(2))
                cabeza = ([] if _ultimo_separador(res, SEP_WA) else ['', SEP_WA, ''])
                res.extend(cabeza + ['*' + titulo.strip() + '*'])
                i += 1
                continue
            if re.match(r'^\s*-{3,}\s*$', li):
                if not _ultimo_separador(res, SEP_WA):
                    res.append(SEP_WA)
                i += 1
                continue
            li = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'_\1_', li)
            li = re.sub(r'\*\*(.+?)\*\*', r'*\1*', li)
            li = re.sub(r'^(\s*)- ', r'\1• ', li)
            res.append(li)
            i += 1
        bloque = '\n'.join(res)
        bloque = re.sub(r'\n{3,}', '\n\n', bloque)
        salida.append(bloque)
    texto = '\n'.join(salida)
    texto = re.sub(r'\n{3,}', '\n\n', texto).strip() + '\n'
    return texto


def convertir_fb(texto):
    partes = _split_fences(texto)
    salida = []
    for es_caja, bloque in partes:
        if es_caja:
            cuerpo = '\n'.join('  ' + l if l.strip() else l
                               for l in bloque.strip('\n').split('\n'))
            salida.append(cuerpo)
            continue
        lineas = bloque.split('\n')
        res, i = [], 0
        while i < len(lineas):
            li = lineas[i]
            if li.strip().startswith('|') and '|' in li.strip()[1:]:
                j = i
                while j < len(lineas) and lineas[j].strip().startswith('|'):
                    j += 1
                res.append(_tabla_a_bullets_fb(lineas[i:j]))
                i = j
                continue
            if li.lstrip().startswith('> '):
                cita = li.lstrip()[2:]
                cita = re.sub(r'\*\*(.+?)\*\*', _negritas_a_mayus_fb, cita)
                res.append('❝ ' + cita + ' ❞' if cita.strip() else '')
                i += 1
                continue
            m = re.match(r'^(#{1,6})\s+(.*)$', li)
            if m:
                titulo = re.sub(r'\*\*(.+?)\*\*', r'\1', m.group(2)).strip()
                nivel = len(m.group(1))
                cabeza = ([] if _ultimo_separador(res, SEP_FB) else ['', SEP_FB, ''])
                if nivel == 1:
                    res.extend(cabeza + ['🟦 ' + titulo.upper()])
                elif nivel == 2:
                    res.extend(cabeza + [titulo.upper()])
                else:
                    res.append('\n▸ ' + titulo)
                i += 1
                continue
            if re.match(r'^\s*-{3,}\s*$', li):
                if not _ultimo_separador(res, SEP_FB):
                    res.append(SEP_FB)
                i += 1
                continue
            li = re.sub(r'\*\*(.+?)\*\*', _negritas_a_mayus_fb, li)
            li = re.sub(r'`([^`]+)`', r'«\1»', li)
            li = re.sub(r'^(\s*)- ', r'\1• ', li)
            res.append(li)
            i += 1
        bloque = '\n'.join(res)
        bloque = re.sub(r'\n{3,}', '\n\n', bloque)
        salida.append(bloque)
    texto = '\n\n'.join(salida)
    texto = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'«\1»', texto)
    while '««' in texto or '»»' in texto:
        texto = texto.replace('««', '«').replace('»»', '»')
    texto = re.sub(r'\n{3,}', '\n\n', texto).strip() + '\n'
    return texto


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ('wa', 'fb'):
        print(__doc__)
        sys.exit(2)
    modo, entrada, salida = sys.argv[1], sys.argv[2], sys.argv[3]
    texto = open(entrada, encoding='utf-8').read()
    convertido = convertir_wa(texto) if modo == 'wa' else convertir_fb(texto)
    antes, despues = len(texto), len(convertido)
    open(salida, 'w', encoding='utf-8').write(convertido)
    print(f'{modo}: {antes} → {despues} c  ({entrada} → {salida})')


if __name__ == '__main__':
    main()
