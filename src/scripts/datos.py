import iteraciones as ite
import funciones as fn
import numpy as np
from pathlib import Path
NOMBRES = ["Polinomica", "Raiz doble", "Logaritmica", "Exponencial", "Trigonometrica", "Mixta"]
FUNCIONES = [fn.fun_1, fn.fun_2, fn.fun_3, fn.fun_4, fn.fun_5, fn.fun_6]
FUNCIONES_DERIVADA = [fn.derivada_1, fn.derivada_2, fn.derivada_3, fn.derivada_4, fn.derivada_5, fn.derivada_6 ]
FUNCIONES_SEGUNDA_DERIVADA = [fn.segunda_derivada_1, fn.segunda_derivada_2, fn.segunda_derivada_3, fn.segunda_derivada_4, fn.segunda_derivada_5, fn.segunda_derivada_6]
PUNTO_FIJO = [fn.puntofijo_1, fn.puntofijo_2, fn.puntofijo_3, fn.puntofijo_4, fn.puntofijo_5, fn.puntofijo_6]
INTERVALOS = [[fn.a_1, fn.b_1], [fn.a_2, fn.b_2], [fn.a_3, fn.b_3],[fn.a_4, fn.b_4], [fn.a_5, fn.b_5], [fn.a_6, fn.b_6]]
X0 = [fn.x0_1, fn.x0_2, fn.x0_3, fn.x0_4, fn.x0_5, fn.x0_6]
X1 = [fn.x1_1, fn.x1_2, fn.x1_3, fn.x1_4, fn.x1_5, fn.x1_6]
DIRECCION = Path("src/data")
DIRECCION.mkdir(parents= True, exist_ok= True)

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
    np.savetxt( DIRECCION / "resumen_convergencias.csv", filas, delimiter=",", fmt="%s", header=",".join(columnas), comments="")
    print(f"Archivo resumen_convergencias.csv generado con exito en src/data.")

def genera_curva_funciones():
    for nombre, f, (a, b) in zip(NOMBRES, FUNCIONES, INTERVALOS):
        x = np.linspace(a, b, 400)
        datos = np.column_stack((x, f(x)))
        archivo = DIRECCION / f"funcion_{nombre.replace(' ', '_')}.csv"
        np.savetxt(archivo, datos, delimiter=",", header="x,f(x)", comments="")
        print(f"Archivo {archivo.name} generado con exito en data.")

def generar_csv_funciones(lista_diccionarios):
    # Lo que hizo cada método: una fila por iteración
    columnas = ["Metodo", "Iteracion", "x", "f(x)", "Error"]
    for nombre, diccionarios in zip(NOMBRES, lista_diccionarios):
        datos = []
        for d in diccionarios:
            for fila in d["lista_iteraciones"]:
                # fila[0] = iteración, fila[-4] = x, fila[-3] = f(x), fila[-2] = err_abs
                datos.append([d["metodo"], fila[0], fila[-4], fila[-3], fila[-2]])
        filas = np.array(datos, dtype=object)
        archivo = DIRECCION / f"iteraciones_{nombre.replace(' ', '_')}.csv"
        np.savetxt(archivo, filas, delimiter=",", fmt="%s",
                   header=",".join(columnas), comments="")
        print(f"Archivo {archivo.name} generado con exito en src/data.")

def crear_archivos_per_funcion():
    lista_diccionarios = []
    for i in range(len(NOMBRES)):
        f = FUNCIONES[i]
        g = PUNTO_FIJO[i]
        f_p = FUNCIONES_DERIVADA[i]
        f_s = FUNCIONES_SEGUNDA_DERIVADA[i]
        intervalo = INTERVALOS[i]
        x0 = X0[i]
        x1 = X1[i]

        # Biseccion
        dic_biseccion = ite.biseccion(f, intervalo, tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER)

        # Falsa posicion
        dic_falsa_posicion = ite.falsa_posicion(f, intervalo, tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER)

        # Punto fijo
        dic_punto_fijo = ite.punto_fijo(g, x0, f, tol=ite.TOLERANCIA, max_iter=ite.MAX_ITER)

        #Newton Raphton
        dic_newton_raphton = ite.newton_raphson(f, f_p, x0, ite.TOLERANCIA, ite.MAX_ITER)

        #Newton Raphton Modificado
        dic_newton_raphton_mod = ite.newton_raphson_modificado(f, f_p, f_s, x0, ite.TOLERANCIA, ite.MAX_ITER)

        #Secante
        dic_secante = ite.secante(f, x0, x1, ite.TOLERANCIA, ite.MAX_ITER)

        lista_diccionarios.append([dic_biseccion, dic_falsa_posicion, dic_punto_fijo, dic_newton_raphton, dic_newton_raphton_mod, dic_secante])
    generar_csv_resumen(lista_diccionarios)
    generar_csv_funciones(lista_diccionarios)
    genera_curva_funciones()
    


if __name__ == "__main__":
    crear_archivos_per_funcion()