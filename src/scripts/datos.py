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

def generar_csv_resumen(lista_diccionarios):
    datos = []
    columnas = ["Metodo", "Funcion", "Aplicable?", "Convergencia?", "Raiz", "Iteraciones", "Error Absoluto Final", "Motivo"]
    for i in range(len(lista_diccionarios)):
        nombre = NOMBRES[i]
        for j in range(len(lista_diccionarios[i])):
            diccionario = lista_diccionarios[i][j]
            metodo = diccionario["metodo"]
            funcion = nombre
            aplicable = diccionario["aplicable"]
            convergencia = diccionario["convergencia"]
            raiz = diccionario["raiz"]
            iteraciones = diccionario["iteraciones"]
            error_absoluto_final = diccionario["lista_iteraciones"][-1][-2] if diccionario["lista_iteraciones"] else None
            motivo = diccionario["motivo"].replace(",", ";")
            datos.append([metodo, funcion, aplicable, convergencia, raiz, iteraciones, error_absoluto_final, motivo])
    filas = np.array(datos, dtype=object)
    np.savetxt(Path("src/data") / "resumen_convergencias.csv", filas, delimiter=",", fmt="%s", header=",".join(columnas), comments="")
    print(f"Archivo resumen_convergencias.csv generado con exito en src/data.")

def generar_csv_iteraciones(nombre, lista_diccionarios):
    pass

def crear_archivos_per_funcion():
    lista_diccionarios = []
    for i in range(len(NOMBRES)):
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

        lista_diccionarios.append([dic_biseccion, dic_falsa_posicion, dic_punto_fijo])

    generar_csv_resumen(lista_diccionarios)
    #generar_csv_iteraciones(nombre, [dic_biseccion, dic_falsa_posicion, dic_punto_fijo])


if __name__ == "__main__":
    crear_archivos_per_funcion()
    
    pass