import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import datos as dt
def grafico_converguencia():
    plt.figure()
    direccion = dt.DIRECCION
    for nombre in dt.NOMBRES:
        datos = np.loadtxt(direccion / f"iteraciones_{nombre.replace(' ', '_')}.csv", delimiter=',', skiprows=1, dtype=object)
        iters = datos[:, 1]
        errores = datos[:, 4]
        plt.semilogy(iters, errores, marker="o", label="datos[:,0]")
        plt.xlabel("Iteración")
        plt.ylabel("|error| (escala log)")
        plt.title(f"Convergencia - {nombre}")
        plt.legend()
        plt.grid(True)
        plt.show()
        plt.savefig(Path("src/assets") /f"convergencia_{nombre}.png")
        plt.close()

def grafico_curva():
    plt.figure()
    direccion = dt.DIRECCION
    for nombre in dt.NOMBRES:
        datos = np.loadtxt(direccion / f"funcion_{nombre.replace(' ', '_')}.csv", delimiter=',', skiprows=1)
        x = datos[:, 0]
        y = datos[:, 1]
        plt.plot(x, y, color="blue", linewidth=0.8)
        plt.axhline(0, color="black", linewidth=0.8) 
        plt.axvline(0, color="black", linewidth=0.8) 
        plt.title(f'Gráfico de la funcion {nombre} con puntos')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        plt.savefig(Path("src/assets") / f"Curva{nombre}.png", dpi=150)
        plt.show()
        


if __name__ == "__main__":
    # Ejemplo de uso
    grafico_curva()
    #grafico_converguencia()
    pass