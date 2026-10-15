import iteraciones as ite
import funciones as fn
import numpy as np
from typing import Callable
from pathlib import Path

NOMBRES = ["Polinomica", "Raiz doble", "Logaritmica", "Exponencial", "Trigonometrica", "Mixta"]
FUNCIONES = [fn.fun_1, fn.fun_2, fn.fun_3, fn.fun_4, fn.fun_5, fn.fun_6]
PUNTO_FIJO = [fn.puntofijo_1, fn.puntofijo_2, fn.puntofijo_3, fn.puntofijo_4, fn.puntofijo_5, fn.puntofijo_6]
INTERVALOS = [[fn.a_1, fn.b_1], [fn.a_2, fn.b_2], [fn.a_3, fn.b_3],
              [fn.a_4, fn.b_4], [fn.a_5, fn.b_5], [fn.a_6, fn.b_6]]
X0 = [fn.x0_1, fn.x0_2, fn.x0_3, fn.x0_4, fn.x0_5, fn.x0_6]

def generar_csv_resumen(nombre, lista_diccionarios):
    pass

def generar_csv_iteraciones(nombre, lista_diccionarios):
    pass

def crear_archivos_per_funcion():
    for i in range(len(NOMBRES)):
        nombre = NOMBRES[i]
        f = FUNCIONES[i]
        g = PUNTO_FIJO[i]
        intervalo = INTERVALOS[i]
        x0 = X0[i]

        # Biseccion
        dic_biseccion = ite.biseccion(f, intervalo, tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER)

        # Falsa posicion
        dic_falsa_posicion = ite.falsa_posicion(f, intervalo, tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER)

        # Punto fijo
        dic_punto_fijo = ite.punto_fijo(g, x0, tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER)

        generar_csv_resumen(nombre, [dic_biseccion, dic_falsa_posicion, dic_punto_fijo])
        generar_csv_iteraciones(nombre, [dic_biseccion, dic_falsa_posicion, dic_punto_fijo])


if __name__ == "__main__":
    #crear_todos_los_archivos()
    #csv_resumen()
    pass