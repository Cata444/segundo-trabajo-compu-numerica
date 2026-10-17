import numpy as np
import iteraciones as ite
import matplotlib.pyplot as plt
from pathlib import Path
import datos as dt

DIRECCIONG = dt.DIRECCION
TITULOS = ["x^3 - x - 2", "(x - 2)^2", "ln(x) + x - 4", "e^(-x) - x", "cos(x) - x", "sqrt(x) - cos(x)"]

def grafico_converguencia_per_metodos():
    for i in range(len(dt.NOMBRES)):
        nombre = dt.NOMBRES[i]
        datos = np.genfromtxt(DIRECCIONG / f"iteraciones_{nombre.replace(' ', '_')}.csv", delimiter=",", skip_header=1, dtype=str)
        datos = np.atleast_2d(datos)
        metodos = datos[:, 0]
        iteracion = datos[:, 1].astype(float)
        x = datos[:, 2].astype(float)
        plt.figure(figsize=(8, 4.8))
        hubo_ceros = False
        raiz = 0
        if nombre == "Raiz doble": 
            raiz = 2.0 
        else: 
            raiz = ite.newton_raphson_modificado(dt.FUNCIONES[i], dt.FUNCIONES_DERIVADA[i], dt.FUNCIONES_SEGUNDA_DERIVADA[i], dt.X0[i])["raiz"]
        for metodo in dict.fromkeys(metodos):
            m = metodos == metodo
            error = np.abs(x[m] - raiz)
            if np.any(error == 0):
                hubo_ceros = True
            error = np.where(error == 0, 1e-17, error)   # el log no admite 0
            plt.semilogy(iteracion[m], error, marker="o", label=metodo)

        plt.axhline(ite.TOLERANCIA, color="gray", linestyle="--", linewidth=1, label="tol = 1e-6")
        plt.xlabel("iteración")
        plt.ylabel("|error| = |x_k - raíz|")
        nota = "  (error 0 se dibuja en 1e-17)" if hubo_ceros else ""
        plt.title(f"Convergencia: f(x) = {TITULOS[i]}{nota}")
        plt.grid(True, which="both", alpha=0.3)
        plt.legend(fontsize=8)
        plt.tight_layout()

        salida = Path("src/assets") / f"convergencia_{nombre.replace(' ', '_')}.png"
        plt.savefig(salida, dpi=150)
        plt.close()

def grafico_curva_funciones():
    """Generacion de las curvas de las funciones junto a su raiz aproximada, usando un csv con los puntos desde un intervalo a hasta b,
      y la raiz aproximada entregada por newton raphson modificado."""
    plt.figure()
    for i in range(len(dt.NOMBRES)):
        nombre = dt.NOMBRES[i]
        datos = np.loadtxt(DIRECCIONG / f"funcion_{nombre.replace(' ', '_')}.csv", delimiter=',', skiprows=1)
        raiz_aproximada = ite.newton_raphson_modificado(dt.FUNCIONES[i], dt.FUNCIONES_DERIVADA[i], dt.FUNCIONES_SEGUNDA_DERIVADA[i], dt.X0[i])
        x = datos[:, 0]
        y = datos[:, 1]
        plt.plot(x, y, color="blue", linewidth=0.8, label = f"Funcion {nombre}")
        plt.plot(raiz_aproximada["raiz"], 0, 'ro', label = f"Raiz Aproximada: {raiz_aproximada["raiz"]}")
        plt.axhline(0, color="black", linewidth=0.8) 
        plt.axvline(0, color="black", linewidth=0.8) 
        plt.title(f'Gráfico de la función: {nombre}')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        plt.legend()
        plt.savefig(Path("src/assets") / f"Curva_{nombre.replace(' ', '_')}.png", dpi=150)
        plt.close()

def grafico_resumen_iteraciones():
    datos = np.genfromtxt(DIRECCIONG / "resumen_convergencias.csv", delimiter=",",
                          skip_header=1, dtype=str, encoding="utf-8")
    metodos_fila = datos[:, 0]
    funciones_fila = datos[:, 1]
    aplicable = datos[:, 2] == "True"
    convergio = datos[:, 3] == "True"
    iteraciones = datos[:, 5].astype(int)

    metodos = list(dict.fromkeys(metodos_fila))
    funciones = list(dict.fromkeys(funciones_fila))

    n = len(metodos)
    ancho = 0.8 / n
    x = np.arange(len(funciones))

    fig, ax = plt.subplots(figsize=(12, 5.5))
    colores = plt.cm.tab10(np.arange(n))

    for j, metodo in enumerate(metodos):
        pos = x + (j - (n - 1) / 2) * ancho
        for k, funcion in enumerate(funciones):
            fila = np.where((metodos_fila == metodo) & (funciones_fila == funcion))[0]
            if len(fila) == 0:
                continue
            i = fila[0]
            if not aplicable[i]:
                # si no aplica se pone sin barra y solo la marca N/A
                ax.text(pos[k], 0.3, "N/A", rotation=90, ha="center", va="bottom", fontsize=8)
                continue
            ax.bar(pos[k], iteraciones[i], width=ancho, color=colores[j],
                   hatch="//" if not convergio[i] else None,
                   edgecolor="white" if convergio[i] else "black")
        # Entrada de leyenda (una por método)
        ax.bar(0, 0, color=colores[j], label=metodo)

    # Entrada de leyenda para los que no convergieron
    ax.bar(0, 0, color="white", hatch="//", edgecolor="black", label="No convergió (tope)")

    ax.set_xticks(x)
    ax.set_xticklabels([f.lower() for f in funciones])
    ax.set_xlabel("función")
    ax.set_ylabel("iteraciones (tol = 1e-6)")
    ax.set_title("Resumen de iteraciones por método y función (N/A = no aplica)")
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(ncol=3, fontsize=8, loc="upper left")
    fig.tight_layout()

    salida = Path("src/assets") / "resumen_iteraciones.png"
    fig.savefig(salida, dpi=150)
    plt.close(fig)

if __name__ == "__main__":
    # Ejemplo de uso
    grafico_curva_funciones()
    grafico_converguencia_per_metodos()
    grafico_resumen_iteraciones()
    pass