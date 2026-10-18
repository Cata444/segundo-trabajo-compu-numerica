# Importacion de libreria
import numpy as np

#------------------------------Funcion Polinomica----------------------------------------------#

# f(x) = x^3 - x - 2  
# Intervalo: [1, 2] x lower 1, x upper 2
a_1 = 1.0
b_1 = 2.0

# x_0 y x_1 para el metodo de Secante, Punto Fijo, Newton Raphson y Newton Raphson modificado
x0_1 = 1.5
x1_1 = 2.0

# Funcion
def fun_1(x):
    return x**3 - x - 2

# Primera Derivada
def derivada_1(x):
    return 3*x**2 - 1

# Segunda Derivada
def segunda_derivada_1(x):
    return 6*x

# Funcion usada para el metodo del punto fijo g(x)
def puntofijo_1(x):
    return np.cbrt(x + 2)


#------------------------------Funcion Raiz doble----------------------------------------------#

# f(x) = (x - 2)^2 
# x0 = 1,2 -> (En este no hay un cambio de signo)

# (solo gráfico)
a_2 = 1.0     
b_2 = 3.0

# x_0 y x_1 para el metodo de Secante, Punto Fijo, Newton Raphson y Newton Raphson modificado
x0_2 = 1.2
x1_2 = 1.5

# Funcion
def fun_2(x):
    return (x - 2)**2

# Primera Derivada
def derivada_2(x):
    return 2*(x - 2)

# Segunda Derivada
def segunda_derivada_2(x):
    return 2

# Funcion usada para el metodo del punto fijo g(x)
def puntofijo_2(x):
    return (x**2 + 4) / 4


#------------------------------Funcion Logaritmo----------------------------------------------#

# f(x) = ln(x) + x - 4
# Intervalo: [2, 3] x lower 2 x upper 3
a_3 = 2.0
b_3 = 3.0

# x_0 y x_1 para el metodo de Secante, Punto Fijo, Newton Raphson y Newton Raphson modificado
x0_3 = 2.5
x1_3 = 3.0

# Funcion
def fun_3(x):
    return np.log(x) + x - 4

# Primera Derivada
def derivada_3(x):
    return 1/x + 1

# Segunda Derivada
def segunda_derivada_3(x):
    return -1/x**2

# Funcion usada para el metodo del punto fijo g(x)
def puntofijo_3(x):
    return 4 - np.log(x)


#------------------------------Funcion Exponencial----------------------------------------------#
# exponencial  e^(-x) - x   rango [0, 1]

# f(x) = e^(-x) - x
# Intervalo: [0, 1]
a_4 = 0.0
b_4 = 1.0

# x_0 y x_1 para el metodo de Secante, Punto Fijo, Newton Raphson y Newton Raphson modificado
x0_4 = 0.5
x1_4 = 1.0

# Funcion
def fun_4(x):
    return np.exp(-x) - x

# Primera Derivada
def derivada_4(x):
    return -np.exp(-x) - 1

# Segunda Derivada
def segunda_derivada_4(x):
    return np.exp(-x)

# Funcion usada para el metodo del punto fijo g(x)
def puntofijo_4(x):
    return np.exp(-x)


#------------------------------Funcion Trigonometrica----------------------------------------------#

# f(x) = cos(x) - x
# Intervalo: [0, 1]
a_5 = 0.0
b_5 = 1.0

# x_0 y x_1 para el metodo de Secante, Punto Fijo, Newton Raphson y Newton Raphson modificado
x0_5 = 0.5
x1_5 = 1.0

# Funcion
def fun_5(x):
    return np.cos(x) - x

# Primera Derivada
def derivada_5(x):
    return -np.sin(x) - 1

# Segunda Derivada
def segunda_derivada_5(x):
    return -np.cos(x)

# Funcion usada para el metodo del punto fijo g(x)
def puntofijo_5(x):
    return np.cos(x)


#------------------------------Funcion Trigonometrica----------------------------------------------#

# f(x) = raiz(x) - cos(x)
# Intervalo: [0.1, 1]
a_6 = 0.1
b_6 = 1.0

# x_0 y x_1 para el metodo de Secante, Punto Fijo, Newton Raphson y Newton Raphson modificado
x0_6 = 0.5
x1_6 = 1.0

# Funcion
def fun_6(x):
    return np.sqrt(x) - np.cos(x)

# Primera Derivada
def derivada_6(x):
    return 1/(2*np.sqrt(x)) + np.sin(x)

# Segunda Derivada
def segunda_derivada_6(x):
    return -1/(4*x**1.5) + np.cos(x)

# Funcion usada para el metodo del punto fijo g(x)
def puntofijo_6(x):
    return np.cos(x)**2


if __name__ == "__main__":
    # Usamos la funcion de bolzano que es f(1) por f(2) < 0 para ver si existen raices como tal.
    print("Polinomica =", fun_1(a_1) * fun_1(b_1))
    print("raiz doble =", fun_2(a_2) * fun_2(b_2))
    print("logaritmica =", fun_3(a_3) * fun_3(b_3))
    print("exponencial =", fun_4(a_4) * fun_4(b_4))
    print("trigonometrica =", fun_5(a_5) * fun_5(b_5))
    print("mixta =", fun_6(a_6) * fun_6(b_6))