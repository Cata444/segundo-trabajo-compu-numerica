import numpy as np
import funciones as fn
from typing import Callable
#Zonas de Variables Globales.
TOLERANCIA = 1e-6
MAX_ITER = 100
# Zona de Metodos
## Metodos Cerrados

def biseccion(f: Callable, intervalo: list, tol=TOLERANCIA, max_iter=MAX_ITER):
    #   Biseccion requiere de dos valores iniciales a y b que se encuentran dentro de un intervalo donde se encontraria una raiz
    #   para ello primero revisamos con el teorema de Bolzano si hay un cambio de signo en el intervalo [a, b] si es asi,
    #   entonces podemos aplicar el metodo de biseccion, si no hay un cambio de signo entonces no podemos aplicar el metodo de biseccion.

    #   Primero verificaremos usando el teorema de Bolzano si hay un cambio de signo en el intervalo [a, b]
    a = intervalo[0]
    b = intervalo[1]
    if not(bolzano(f, a, b)):
        print("No hay un cambio de signo en el intervalo [a, b], no se puede aplicar el metodo de biseccion.")
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
    #   Ahora aplicamos el metodo de biseccion
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
    a = intervalo[0]
    b = intervalo[1]
    if not(bolzano(f, a, b)):
        print("No hay un cambio de signo en el intervalo [a, b], no se puede aplicar el metodo de falsa posicion.")
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

## Metodos Abiertos
def punto_fijo(g: Callable, p0, f: Callable = None, tol=TOLERANCIA, max_iter=MAX_ITER):
    lista_iteraciones = []
    p_previo = p0
    f_pn = 0
    for n in range(1, max_iter + 1):
        p_n = g(p_previo)
        if f != None:
            f_pn =f(p_n)
        else:
            f_pn = "NA"
        if not np.isfinite(p_n):
            return {"metodo": "Punto Fijo",
                    "aplicable": True, 
                    "convergencia": False, 
                    "raiz": None,
                    "iteraciones": n, 
                    "lista_iteraciones": lista_iteraciones, 
                    "columnas": ["iteracion", "p_previo", "p_n", "f_p", "err_abs", "err_rel_pct"], 
                    "motivo": "El metodo diverge (valor no finito)."}

        err_abs = error_absoluto(p_n, p_previo)
        err_rel = error_relativo_porcentual(p_n, p_previo)
        lista_iteraciones.append([n, p_previo, p_n, f_pn, err_abs, err_rel])
        if err_abs < tol or np.abs(f_pn):
            return {"metodo": "Punto Fijo",
                    "aplicable": True, 
                    "convergencia": True, 
                    "raiz": p_n,
                    "iteraciones": n, 
                    "lista_iteraciones": lista_iteraciones, 
                    "columnas": ["iteracion", "p_previo", "p_n", "err_abs", "err_rel_pct"], 
                    "motivo": f"Convergio con tolerancia {tol}"}

        p_previo = p_n

    return {"metodo": "Punto Fijo",
            "aplicable": True, 
            "convergencia": False, 
            "raiz": p_n,
            "iteraciones": max_iter, 
            "lista_iteraciones": lista_iteraciones, 
            "columnas": ["iteracion", "p_previo", "p_n", "err_abs", "err_rel_pct"], 
            "motivo": f"Se alcanzo el maximo de iteraciones sin cumplir tol={tol}"}

def newton_raphson():
    pass
def secante():
    pass
def newton_raphson_modificado():
    pass

## Teorema de Bolzano para saber si hay una raiz en el intervalo [a, b]
def bolzano(f: Callable, a, b):
    if f(a) * f(b) < 0:
        return True
    else:
        return False

def tangencia_raiz_doble(f: Callable, f_1: Callable, f_2: Callable, x):
    if ((f(x) == 0 and f_1(x) == 0) and f_2(x) != 0):
        return True
    else:
        return False

## Estimador de iteraciones por tolerancia para el metodo de biseccion y falsa posicion
def estimador_iteraciones(tol, a, b):
    return np.ceil(np.log((b - a) / tol) / np.log(2))

## Errores
def error_absoluto(x_n, x_n_1):
    return np.abs(x_n - x_n_1)

def error_relativo_porcentual(a, b):
    if b == 0:
        return np.nan
    return np.abs((b - a) / b) * 100

if __name__ == "__main__":
    # Llamada a las funciones de iteraciones para cada función

    #print("\n")
    # #print(biseccion(fn.fun_1, [fn.a_1, fn.b_1])["raiz"] - 1.5213797068)
    #print("---------------------------------------------------------------------\n")
    #print(falsa_posicion(fn.fun_4, [fn.a_4, fn.b_4]))
    #print("\n")
    #print("---------------------------------------------------------------------\n")
    #print(punto_fijo(fn.puntofijo_5, fn.x0_5))
    pass