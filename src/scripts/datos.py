import iteraciones as ite
import funciones as fn
import numpy as np
from typing import Callable
from pathlib import Path

def crear_csv(nombre_archivo, lista_iteraciones):
    """
    Crea un archivo CSV con los resultados de las iteraciones.
    """
    ruta_carpeta_resultados = Path("src/data")
    ruta_carpeta_resultados.mkdir(parents=True, exist_ok=True)
    nombre_archivo = ruta_carpeta_resultados / nombre_archivo
    print(f"Ruta de la carpeta de resultados: {ruta_carpeta_resultados.resolve()}")
    np.savetxt(nombre_archivo, lista_iteraciones, delimiter=',', header='Iteracion,a,b,f(a),p_n,f(p_n),err_abs,err_rel_%', comments='', fmt='%s')

def ejecutar_metodo(metodo: Callable, f: Callable, intervalo, tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER, function_number=1):
    """
    Ejecuta un metodo de iteracion y guarda los resultados en un archivo CSV.
    """
    resultado = metodo(f, intervalo, tol, max_iter)
    if resultado["aplicable"]:
        nombre_archivo = f"resultados_{metodo.__name__}_{function_number}.csv"
        crear_csv(nombre_archivo, resultado["lista_iteraciones"])
        print(f"Resultados guardados en {nombre_archivo}")
    else:
        print("El metodo no es aplicable al intervalo dado.")

def crear_todos_los_archivos():
    lista_funciones = [fn.fun_1, fn.fun_2, fn.fun_3, fn.fun_4, fn.fun_5]
    lista_funciones_punto_fijo = [fn.puntofijo_1, fn.puntofijo_2, fn.puntofijo_3, fn.puntofijo_4, fn.puntofijo_5]
    lista_intervalos = [[fn.a_1, fn.b_1], [fn.a_2, fn.b_2], [fn.a_3, fn.b_3], [fn.a_4, fn.b_4], [fn.a_5, fn.b_5]]
    lista_intervalos_punto_fijo = [fn.x0_1, fn.x0_2, fn.x0_3, fn.x0_4, fn.x0_5]
    # Ejecutar el metodo de biseccion para todas las funciones
    for i in range(1, 6):
        print("\n")
        ejecutar_metodo(ite.biseccion, lista_funciones[i-1], lista_intervalos[i-1], tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER, function_number=i)
        print("---------------------------------------------------------------------\n")
    # Ejecutar el metodo de falsa posicion para todas las funciones
    for i in range(1, 6):
        ejecutar_metodo(ite.falsa_posicion, lista_funciones[i-1], lista_intervalos[i-1], tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER, function_number=i)
        print("\n")
        print("---------------------------------------------------------------------\n")
    # Ejecutar el metodo de punto fijo para todas las funciones
    for i in range(1, 6):
        ejecutar_metodo(ite.punto_fijo, lista_funciones_punto_fijo[i-1], lista_intervalos_punto_fijo[i-1], tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER, function_number=i)
        print("\n")
        print("---------------------------------------------------------------------\n")
    return "Todos los archivos CSV han sido creados exitosamente."

if __name__ == "__main__":
    #crear_todos_los_archivos()
    pass