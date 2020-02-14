# -*- coding: utf-8 -*-
# Resolucion del problema de tres caballos en un tablero 3x3

import Caballos as C
import sys
sys.setrecursionlimit(10000) # Para incrementar el limite de la recursion
import visualizacion as V

# Solicita condicion inicial
print(u'Introduzca el número de la casilla (1,...,9) en la que')
print(u'desea un caballo como condición inicial.')
print(u'Deje vacío si no desea condición inicial.')
cInicial = input(u'Condición inicial? (1,...,9):')

if len(cInicial) > 0:
    assert(int(cInicial)>0 and int(cInicial)<10)
    print(u'Resolviendo el problema con condición inicial', cInicial)
    cInicial = chr(int(cInicial) + 96)
    # print(cInicial)
else:
    print(u"El problema se resolverá sin condiciones iniciales.")

print("Creando reglas...")
reglas = C.crear_reglas()
if len(cInicial) > 0:
    reglas += cInicial + "Y"

A = C.String2Tree(reglas)

print('Encontrando soluciones (paciencia, por favor!)...')
listaSoluciones = C.Encuentra_Interpretaciones(A)

print('Hay', str(len(listaSoluciones)), ' interpretaciones que resuelven el problema.')
# print('Las interpretaciones son:\n', listaSoluciones)

for x in range(len(listaSoluciones)):
    f = listaSoluciones[x]
    V.dibujar_tablero(f,x + 1)

print('Visualizaciones guardadas en /Soluciones')
print('Terminado!')
