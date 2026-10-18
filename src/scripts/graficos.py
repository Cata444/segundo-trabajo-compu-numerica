#Importaciones de librerias
import numpy as np
import iteraciones as ite
import matplotlib.pyplot as plt
from pathlib import Path
import datos as dt

# Zona de Variables Globales
TITULOS = ["x^3 - x - 2", "(x - 2)^2", "ln(x) + x - 4", "e^(-x) - x", "cos(x) - x", "sqrt(x) - cos(x)"]
DIRECCIOND = dt.DIRECCION
DIRECCIONG = Path("src/assets")
DIRECCIONG.mkdir(parents= True, exist_ok= True)

def grafico_converguencia_per_metodos():
    """Generador de graficos de error vs iteracion por metodos en cada funcion."""
    for i in range(len(dt.NOMBRES)):
        # Obtenemos los datos necesarios para poder graficar.
        nombre = dt.NOMBRES[i]
        datos = np.loadtxt(DIRECCIOND / f"iteraciones_{nombre.replace(' ', '_')}.csv", delimiter=",", skiprows=1, dtype=str)
        datos = np.atleast_2d(datos)
        metodos = datos[:, 0]
        iteracion = datos[:, 1].astype(float)
        x = datos[:, 2].astype(float)
        plt.figure()

        hubo_ceros = False # Esta variable me entrega si el error fue cero y de ser asi, entonces se activa una nota especifica
        # debido a que ya que se modela por el eje de un logaritmo, y log(0) tiende al infinito, basicamente no se veria el punto.
        raiz = 2.0 if nombre == "Raiz doble" else ite.newton_raphson_modificado(dt.FUNCIONES[i], dt.FUNCIONES_DERIVADA[i], dt.FUNCIONES_SEGUNDA_DERIVADA[i], dt.X0[i], tol = 1e-15, max_iter = 400)["raiz"]
        for metodo in dict.fromkeys(metodos):
            m = metodos == metodo
            error = np.abs(x[m] - raiz)
            if np.any(error == 0):
                hubo_ceros = True
            error = np.where(error == 0, 1e-17, error)   # el log no admite 0 asi que lo reemplazamos con un valor muy pequeño para que sea visible.
            plt.semilogy(iteracion[m], error, marker="o", label=metodo)

        plt.axhline(ite.TOLERANCIA, color="gray", linestyle="-", linewidth=1.0, label="tol = 1e-6")
        plt.xlabel("iteración")
        plt.ylabel("|error| = |x_k - raíz|")
        nota = " (error 0 se dibuja en 1e-17)" if hubo_ceros else ""
        plt.title(f"Convergencia: f(x) = {TITULOS[i]}{nota}")
        plt.grid(True, which="both", alpha=0.3)
        plt.legend(fontsize=8)

        salida = DIRECCIONG / f"convergencia_{nombre.replace(' ', '_')}.png"
        plt.savefig(salida, dpi=150)
        print(f"convergencia_{nombre.replace(' ', '_')}.png generado con exito en src / assets.")
        plt.close()

def grafico_curva_funciones():
    """Generacion de las curvas de las funciones junto a su raiz aproximada, usando un csv con los puntos desde un intervalo a hasta b,
      y la raiz aproximada entregada por newton raphson modificado."""
    plt.figure()
    for i in range(len(dt.NOMBRES)):
        nombre = dt.NOMBRES[i]

        # Cargamos los datos desde los archivos .csv generados anteriormente
        datos = np.loadtxt(DIRECCIOND / f"funcion_{nombre.replace(' ', '_')}.csv", delimiter=',', skiprows=1)

        # Calculamos la raiz aproximada para colocar el punto aproximado donde se encuentra con el eje x para ello usaremos
        # newton raphton mejorado.
        raiz_aproximada = ite.newton_raphson_modificado(dt.FUNCIONES[i], dt.FUNCIONES_DERIVADA[i], dt.FUNCIONES_SEGUNDA_DERIVADA[i], dt.X0[i], tol = 1e-15, max_iter = 400)
        
        # De los datos sacados al ser solo dos columnas las separaremos en x e y.
        x = datos[:, 0]
        y = datos[:, 1]

        # Primero dibujaremos la funcion gracias a los valores del csv.
        plt.plot(x, y, color="blue", linewidth=0.8, label = f"Funcion {TITULOS[i]}")
        # luego dibujamos el punto donde se encuentra la raiz aproximada.
        plt.plot(raiz_aproximada["raiz"], 0, 'ro', label = f"Raiz Aproximada: {raiz_aproximada["raiz"]:.6f}")

        #Dibujamos de manera mas clara el eje x e y.
        plt.axhline(0, color="black", linewidth=0.8) 
        plt.axvline(0, color="black", linewidth=0.8) 

        # Nombramos los ejes y el titulo del grafico
        plt.title(f'Gráfico de la función: {nombre}')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')

        # Activamos que se vea la cuadrilla y la legenda.
        plt.grid(True)
        plt.legend()
        # Guardamos la figura en la ruta donde se encuentra la carpeta assets
        plt.savefig(DIRECCIONG / f"Curva_{nombre.replace(' ', '_')}.png", dpi=150)
        print(f"Archivo {f"Curva_{nombre.replace(' ', '_')}.png"} generado con exito en src/assets.")
        plt.close()

def grafico_resumen_iteraciones():
    """En esta funcion se genera el grafico que resume las convergencias entregando """
    # Cargamos los datos desde los archivos .csv generados anteriormente.
    datos = np.loadtxt(DIRECCIOND / "resumen_convergencias.csv", delimiter=",", skiprows=1, dtype=str, encoding="utf-8")

    # Sacamos los datos de las columnas que tenemos en el archivo csv.
    metodos_fila = datos[:, 0]
    funciones_fila = datos[:, 1]

    # Pasamos los textos de "True" o "False" a booleanos usando comparacion ya que si "True" == "True" -> True(Booleano)
    # caso contrario "False" == "True" -> False(Booleano)
    aplicable = datos[:, 2] == "True"
    convergio = datos[:, 3] == "True"
    
    # Pasamos los datos de la columna de iteraciones a enteros.
    iteraciones = datos[:, 5].astype(int)

    # Los datos que recogimos de las columnas de metodos y funciones las pasamos a listas sin repeticiones conservando el orden en que aparecen.
    metodos = list(dict.fromkeys(metodos_fila))
    funciones = list(dict.fromkeys(funciones_fila))

    n = len(metodos) # 6 barras por grupo
    ancho = 0.8 / n # cada barra usa 1/6 del 80% del espacio del grupo
    x = np.arange(len(funciones)) # centro de cada grupo

    fig, ax = plt.subplots(figsize=(12, 5.5))

    # definimos los colores que usaremos dentro del grafico.
    colores = plt.cm.tab10(np.arange(n))

    for j, metodo in enumerate(metodos):
        pos = x + (j - (n - 1) / 2) * ancho
        for k, funcion in enumerate(funciones):
            fila = np.where((metodos_fila == metodo) & (funciones_fila == funcion))[0] # Para determinar que existe el par necesario
            if len(fila) == 0:
                continue
            i = fila[0]
            if not aplicable[i]:
                # si no aplica se pone sin barra y solo la marca N/A
                ax.text(pos[k], 0.3, "N/A", rotation=90, ha="center", va="bottom", fontsize=8)
                continue
            ax.bar(pos[k], iteraciones[i], width=ancho, color=colores[j], hatch="//" if not convergio[i] else None,
                   edgecolor="white" if convergio[i] else "black")
        # Entrada de leyenda (una por método)
        ax.bar(0, 0, color=colores[j], label=metodo)

    # Entrada de leyenda para los que no convergieron
    ax.bar(0, 0, color="white", hatch="//", edgecolor="black", label="No convergió (tope)")

    # pone los nombres de las funciones por grupo en el eje x.
    ax.set_xticks(x)
    ax.set_xticklabels([f.lower() for f in funciones])

    ax.set_xlabel("función")
    ax.set_ylabel("iteraciones (tol = 1e-6)")
    ax.set_title("Resumen de iteraciones por método y función (N/A = no aplica)")
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(ncol=3, fontsize=8, loc="upper left")

    salida = DIRECCIONG / "resumen_iteraciones.png"
    fig.savefig(salida, dpi=150)
    print(f"resumen_iteraciones.png generado con exito en src / assets.")
    plt.close(fig)

if __name__ == "__main__":
    # Ejecucion del programa principal si este es el Ejecutado.
    grafico_curva_funciones()
    grafico_converguencia_per_metodos()
    grafico_resumen_iteraciones()
    pass