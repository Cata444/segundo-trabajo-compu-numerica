#Importaciones de librerias
import numpy as np
from typing import Callable

#Zonas de Variables Globales.
TOLERANCIA = 1e-6
MAX_ITER = 100

#------------------------------------------------Metodos Cerrados-----------------------------------------------------------------#

def biseccion(f: Callable, intervalo: list, tol=TOLERANCIA, max_iter=MAX_ITER):
    """Funcion que recrea el metodo cerrado de biseccion."""
    a = intervalo[0]
    b = intervalo[1]
    if not(bolzano(f, a, b)):
        return {"metodo": "Biseccion",
                "aplicable": False, 
                "convergencia": False, 
                "raiz": None, 
                "iteraciones": 0, 
                "lista_iteraciones": [], 
                "columnas": ["iteracion", "a", "b", "f_a", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                "motivo": "No hay un cambio de signo en el intervalo [a, b], no se puede aplicar el metodo de biseccion."}
    f_a = f(a)
    p_previo = None
    lista_iteraciones = []
    for i in range(1, max_iter + 1):
        p_n = (a + b) / 2
        f_p = f(p_n)

        if p_previo is None:
            err_abs, err_rel = np.nan, np.nan
        else:
            err_abs = error_absoluto(p_n, p_previo)
            err_rel = error_relativo_porcentual(p_n, p_previo)
        lista_iteraciones.append([i, a, b, f_a, p_n, f_p, err_abs, err_rel])
        
        if np.abs(f_p) < tol or err_abs < tol:
            return {"metodo": "Biseccion",
                    "aplicable": True, 
                    "convergencia": True, 
                    "raiz": p_n, 
                    "iteraciones": i, 
                    "lista_iteraciones": lista_iteraciones, 
                    "columnas": ["iteracion", "a", "b", "f_a", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                    "motivo": f"Se encontro una raiz en el intervalo [a, b] con una tolerancia de {tol}"}
        
        if f_a * f_p < 0:
            b = p_n
        elif f_a * f_p > 0:
            a = p_n
            f_a = f_p
        else:
            return {"metodo": "Biseccion",
                    "aplicable": True, 
                    "convergencia": True, 
                    "raiz": p_n, 
                    "iteraciones": i, 
                    "lista_iteraciones": lista_iteraciones, 
                    "columnas": ["iteracion", "a", "b", "f_a", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                    "motivo": "Se encontro una raiz exacta en el intervalo [a, b]"}
        p_previo = p_n
        
    return {"metodo": "Biseccion",
            "aplicable": True, 
            "convergencia": False,
            "raiz": p_n,
            "iteraciones": max_iter,
            "lista_iteraciones": lista_iteraciones,
            "columnas": ["iteracion", "a", "b", "f_a", "p_n", "f_p", "err_abs", "err_rel_pct"], 
            "motivo": f"Se alcanzo el maximo de iteraciones sin encontrar una raiz con una tolerancia de {tol}"}
 
def falsa_posicion(f: Callable, intervalo: list, tol=TOLERANCIA, max_iter=MAX_ITER):
    """Funcion que implementa el metodo cerrado de falsa posicion."""
    a = intervalo[0]
    b = intervalo[1]
    if not(bolzano(f, a, b)):
        return {"metodo": "Falsa Posicion",
                "aplicable": False, 
                "convergencia": False, 
                "raiz": None, 
                "iteraciones": 0, 
                "lista_iteraciones": [], 
                "columnas": ["iteracion", "a", "b", "f_a", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                "motivo": "No hay un cambio de signo en el intervalo [a, b], no se puede aplicar el metodo de falsa posicion."}
    f_a = f(a)
    p_previo = None
    lista_iteraciones = []
    for i in range(1, max_iter + 1):
        p_n = b - ((f(b) * (a - b)) / (f(a) - f(b)))
        f_p = f(p_n)
        
        if p_previo is None:
            err_abs, err_rel = np.nan, np.nan
        else:
            err_abs = error_absoluto(p_n, p_previo)
            err_rel = error_relativo_porcentual(p_n, p_previo)
        lista_iteraciones.append([i, a, b, f_a, p_n, f_p, err_abs, err_rel])
        
        if np.abs(f_p) < tol or err_abs < tol:
            return {"metodo": "Falsa Posicion",
                    "aplicable": True, 
                    "convergencia": True, 
                    "raiz": p_n, 
                    "iteraciones": i, 
                    "lista_iteraciones": lista_iteraciones, 
                    "columnas": ["iteracion", "a", "b", "f_a", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                    "motivo": f"Se encontro una raiz en el intervalo [a, b] con una tolerancia de {tol}"}
        
        if f_a * f_p < 0:
                    b = p_n
        elif f_a * f_p > 0:
            a = p_n
            f_a = f_p
        else:
            return {"metodo": "Falsa Posicion",
                    "aplicable": True, 
                    "convergencia": True, 
                    "raiz": p_n, 
                    "iteraciones": i, 
                    "lista_iteraciones": lista_iteraciones, 
                    "columnas": ["iteracion", "a", "b", "f_a", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                    "motivo": "Se encontro una raiz exacta en el intervalo [a, b]"}
        p_previo = p_n
    return {"metodo": "Falsa Posicion",
            "aplicable": True, 
            "convergencia": False,
            "raiz": p_n,
            "iteraciones": max_iter,
            "lista_iteraciones": lista_iteraciones, 
            "columnas": ["iteracion", "a", "b", "f_a", "p_n", "f_p", "err_abs", "err_rel_pct"], 
            "motivo": f"Se alcanzo el maximo de iteraciones sin encontrar una raiz con una tolerancia de {tol}"}

#------------------------------------------------Metodos Abiertos-----------------------------------------------------------------#

def punto_fijo(g: Callable, p0, f: Callable = None, tol=TOLERANCIA, max_iter=MAX_ITER):
    """Funcion que implementa el metodo abierto de punto fijo."""
    lista_iteraciones = []
    p_previo = p0
    f_pn = 0
    
    for n in range(1, max_iter + 1):
        p_n = g(p_previo)
        if not np.isfinite(p_n):
                    return {"metodo": "Punto Fijo",
                            "aplicable": True, 
                            "convergencia": False, 
                            "raiz": None,
                            "iteraciones": n, 
                            "lista_iteraciones": lista_iteraciones, 
                            "columnas": ["iteracion", "p_previo", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                            "motivo": "El metodo diverge (valor no finito)."}
        
        if f != None:
            f_pn =f(p_n)
        else:
            f_pn = np.nan
        
        err_abs = error_absoluto(p_n, p_previo)
        err_rel = error_relativo_porcentual(p_n, p_previo)
        lista_iteraciones.append([n, p_previo, p_n, f_pn, err_abs, err_rel])
        if err_abs < tol or np.abs(f_pn) < tol:
            return {"metodo": "Punto Fijo",
                    "aplicable": True, 
                    "convergencia": True, 
                    "raiz": p_n,
                    "iteraciones": n, 
                    "lista_iteraciones": lista_iteraciones, 
                    "columnas": ["iteracion", "p_previo", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                    "motivo": f"Convergio con tolerancia {tol}"}

        p_previo = p_n

    return {"metodo": "Punto Fijo",
            "aplicable": True, 
            "convergencia": False, 
            "raiz": p_n,
            "iteraciones": max_iter, 
            "lista_iteraciones": lista_iteraciones, 
            "columnas": ["iteracion", "p_previo", "p_n", "f_p", "err_abs", "err_rel_pct"], 
            "motivo": f"Se alcanzo el maximo de iteraciones sin cumplir tol={tol}"}


def newton_raphson(funcion, mi_derivada, punto_inicio, tol=TOLERANCIA, max_iter=MAX_ITER):
    """Funcion que implementa el metodo abierto de newton raphson."""
    x = punto_inicio
    lista_iteraciones = []
    i = 0

    while abs(funcion(x)) >= tol and i < max_iter:
        i = i + 1
        x_nuevo = x - funcion(x) / mi_derivada(x)
        lista_iteraciones.append([i, x, x_nuevo, funcion(x_nuevo), abs(x_nuevo - x), error_relativo_porcentual(x_nuevo, x)])
        x = x_nuevo

    encontramos_raiz = abs(funcion(x)) < tol

    return {"metodo": "Newton-Raphson",
            "aplicable": True,
            "convergencia": encontramos_raiz,
            "raiz": x,
            "iteraciones": i,
            "lista_iteraciones": lista_iteraciones,
            "columnas": ["iteracion", "p_previo", "p_n", "f_p", "err_abs", "err_rel_pct"],
            "motivo": "Se encontro la raiz" if encontramos_raiz else "Se alcanzo el maximo de iteraciones"}


def newton_raphson_modificado(funcion, mi_derivada, mi_segunda_derivada, punto_inicio, tol=TOLERANCIA, max_iter=MAX_ITER):
    """Funcion que implementa el metodo abierto de newton raphston mejorado."""
    x = punto_inicio
    lista_iteraciones = []
    i = 0

    while abs(funcion(x)) >= tol and i < max_iter:
        i = i + 1
        arriba = funcion(x) * mi_derivada(x)
        abajo = mi_derivada(x)**2 - funcion(x) * mi_segunda_derivada(x)
        x_nuevo = x - arriba / abajo
        lista_iteraciones.append([i, x, x_nuevo, funcion(x_nuevo), abs(x_nuevo - x), error_relativo_porcentual(x_nuevo, x)])
        x = x_nuevo

    encontramos_raiz = abs(funcion(x)) < tol

    return {"metodo": "Newton-Raphson modificado",
            "aplicable": True,
            "convergencia": encontramos_raiz,
            "raiz": x,
            "iteraciones": i,
            "lista_iteraciones": lista_iteraciones,
            "columnas": ["iteracion", "p_previo", "p_n", "f_p", "err_abs", "err_rel_pct"],
            "motivo": "Se encontro la raiz" if encontramos_raiz else "Se alcanzo el maximo de iteraciones"}

def secante(funcion, punto_inicio, punto_dos, tol=TOLERANCIA, max_iter=MAX_ITER):
    """Funcion que implementa el metodo abierto de la secante."""
    x_antes = punto_inicio
    x = punto_dos
    lista_iteraciones = []
    i = 0

    while abs(funcion(x)) >= tol and i < max_iter:
        i = i + 1
        arriba = funcion(x) * (x - x_antes)
        abajo = funcion(x) - funcion(x_antes)
        x_nuevo = x - arriba / abajo
        lista_iteraciones.append([i, x, x_nuevo, funcion(x_nuevo), abs(x_nuevo - x), error_relativo_porcentual(x_nuevo, x)])
        x_antes = x
        x = x_nuevo

    encontramos_raiz = abs(funcion(x)) < tol

    return {"metodo": "Secante",
            "aplicable": True,
            "convergencia": encontramos_raiz,
            "raiz": x,
            "iteraciones": i,
            "lista_iteraciones": lista_iteraciones,
            "columnas": ["iteracion", "p_previo", "p_n", "f_p", "err_abs", "err_rel_pct"],
            "motivo": "Se encontro la raiz" if encontramos_raiz else "Se alcanzo el maximo de iteraciones"}
    

def bolzano(f: Callable, a, b):
    """Teorema de Bolzano para saber si hay una raiz en el intervalo [a, b]."""
    if f(a) * f(b) < 0:
        return True
    else:
        return False

def tangencia_raiz_doble(f: Callable, f_1: Callable, f_2: Callable, x):
    """Tangencia a la al eje, Con esto podemos determinar la convergencia de la raiz doble."""
    # f(x) = 0
    f_cero  = np.isclose(f(x), 0, atol=TOLERANCIA)
    # f'(x) = 0
    f1_cero = np.isclose(f_1(x), 0, atol=TOLERANCIA)
    # f''(x) ≠ 0
    f2_cero = np.isclose(f_2(x), 0, atol=TOLERANCIA)
    # f(x) = 0 ^ f'(x) = 0 ^ f''(x) ≠ 0 -> True, si no False
    return bool(f_cero and f1_cero and not f2_cero)

def estimador_iteraciones(tol, a, b):
    """Estimador de iteraciones por tolerancia para el metodo de biseccion"""
    return np.ceil(np.log((b - a) / tol) / np.log(2))

## Errores
def error_absoluto(x_n, x_n_1):
    return np.abs(x_n - x_n_1)

def error_relativo_porcentual(p_n, p_n1):
    if p_n == 0:
        return np.nan
    return np.abs((p_n - p_n1) / p_n) * 100

if __name__ == "__main__":
    # Llamada a las funciones de iteraciones para cada función
    # print("Te encuentras en el archivo 'iteraciones.py'.")
    pass