#!/usr/bin/env python3
"""Verifica una pieza de La Bandita: tamaño, formato NN, META, firma, y lista de cecina."""
import sys, re, io
target = int(sys.argv[2]) if len(sys.argv)>2 else None
path = sys.argv[1]
txt = io.open(path, encoding='utf-8').read()
chars = len(txt)
lines = txt.count('\n')+1
# NN en el nombre de archivo
m = re.search(r'/(\d{2})-', path)
nn = m.group(1) if m else '??'
# META (línea con La Bandita · fecha)
has_meta = bool(re.search(r'\*\*La Bandita\s+·', txt))
# firma
has_sign = 'La Bandita informa a partir de fuentes fechadas' in txt
# alarmismo / palabras vedadas (cecina de redacción)
banned = ['¡ALERTA','URGENTE','PELIGRO INMINENTE','te van a bloquear','ya no podrás','se acabó Android',
          'emergencia','catástrofe','borra esto ya','virus garantizado']
found = [b for b in banned if b.lower() in txt.lower()]
# H1 con número
h1 = re.search(r'^#\s+Publicación\s+(\d+)\b', txt, re.M)
h1nn = h1.group(1) if h1 else None
print(f"Archivo: {path}")
print(f"Caracteres: {chars:,}  | Líneas: {lines:,}")
print(f"NN(nombre)={nn}  H1.NN={h1nn}  META={'SÍ' if has_meta else 'NO'}  FIRMA={'SÍ' if has_sign else 'NO'}")
if target:
    diff = chars - target
    print(f"Objetivo: {target:,}  | Diferencia: {diff:+,}  | {'DENTRO' if abs(diff)<=int(target*0.05) else 'FUERA DE RANGO'}")
if found: print("PALABRAS-VEDADAS encontradas:", found)
else: print("Palabras-vedadas: ninguna ✓")
