#Importaciones de librerias
import datos as dt
import graficos as gf
import iteraciones as ite

def salto_linea():
    """Funcion para imprimir un salto de linea."""
    print("\n")

def main():
    """Ejecucion principal del programa."""
    print("Iniciando Programa.")
    #Desde este archivo se llama la funcion para generar todos los datos usados en los graficos.
    salto_linea()
    print("Generando archivos CSV. Espere por favor...")
    dt.crear_archivos_per_funcion()
    
    # LLamando generadores de graficos despues de tener los .csv .
    salto_linea()
    print("Generando Graficos de funciones con su raiz aprox...")
    gf.grafico_curva_funciones()
    salto_linea()
    print("Generando Graficos de |Error| vs Iteracion...")
    gf.grafico_converguencia_per_metodos()
    salto_linea()
    print("Generando Grafico de iteraciones versus metodos y funcion....")
    gf.grafico_resumen_iteraciones()
    salto_linea()
    #Prints de las convergencias por Bolzano y tangencia para raiz doble.
    print("Generando tipo de convergencias por funcion.")
    salto_linea()
    for i, nombre in enumerate(dt.NOMBRES):

        converge = "No tiene raices"
        metodo_convergencia = "Teorema de Bolzano"

        # Si la funcion es la de raiz doble usamos tangencia al eje, porque de lo contrario no convergeria por Bolzano.
        if nombre == "Raiz doble":
            if (ite.tangencia_raiz_doble(dt.FUNCIONES[1], dt.FUNCIONES_DERIVADA[1], dt.FUNCIONES_SEGUNDA_DERIVADA[1], dt.X0[1])): 
                converge = "Existe una raiz"     
            metodo_convergencia = "Tangencia al eje"

        if (ite.bolzano(dt.FUNCIONES[i], dt.INTERVALOS[i][0], dt.INTERVALOS[i][1])): 
            converge = "Existe una raiz" 

        print(f"{nombre}: {converge} por {metodo_convergencia}.")
    salto_linea()
    #Finalizacion
    print("Ha finalizado la ejecucion del archivo.")

if __name__ == "__main__":
    # Ejecucion del programa principal si este es el Ejecutado.
    main()
