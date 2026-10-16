import numpy as np

# Teniamos que definirla tolerancia TOL y el numero maximo de iteraciones
TOL = 1e-6
MAX_ITER = 100


# Polinomica  x^3 - x - 2  con rango [1, 2] x lower 1, x upper 2

def fun_1(x):
    return x**3 - x - 2

def derivada_1(x):
    return 3*x**2 - 1

def segunda_derivada_1(x):
    return 6*x

def puntofijo_1(x):
    return np.cbrt(x + 2)

a_1 = 1.0      
b_1 = 2.0      
x0_1 = 1.5     
x1_1 = 2.0     


# Raiz doble  (x - 2)^2,  x0 = 1,2 -> en este no hay un cambio de signo

def fun_2(x):
    return (x - 2)**2

def derivada_2(x):
    return 2*(x - 2)

def segunda_derivada_2(x):
    return 2

def puntofijo_2(x):
    return (x**2 + 4) / 4

a_2 = 1.0     
b_2 = 3.0
x0_2 = 1.2
x1_2 = 1.5


# logaritmo  ln(x) + x - 4,  rango [2, 3] x lower 2 x upper 3

def fun_3(x):
    return np.log(x) + x - 4

def derivada_3(x):
    return 1/x + 1

def segunda_derivada_3(x):
    return -1/x**2

def puntofijo_3(x):
    return 4 - np.log(x)

a_3 = 2.0
b_3 = 3.0
x0_3 = 2.5
x1_3 = 3.0


# exponencial  e^(-x) - x   rango [0, 1]

def fun_4(x):
    return np.exp(-x) - x

def derivada_4(x):
    return -np.exp(-x) - 1

def segunda_derivada_4(x):
    return np.exp(-x)

def puntofijo_4(x):
    return np.exp(-x)

a_4 = 0.0
b_4 = 1.0
x0_4 = 0.5
x1_4 = 1.0


# trigonometrica  cos(x) - x,  rango [0, 1]

def fun_5(x):
    return np.cos(x) - x

def derivada_5(x):
    return -np.sin(x) - 1

def segunda_derivada_5(x):
    return -np.cos(x)

def puntofijo_5(x):
    return np.cos(x)

a_5 = 0.0
b_5 = 1.0
x0_5 = 0.5
x1_5 = 1.0


# mixta  raiz(x) - cos(x),  rango [0.1, 1]

def fun_6(x):
    return np.sqrt(x) - np.cos(x)

def derivada_6(x):
    return 1/(2*np.sqrt(x)) + np.sin(x)

def segunda_derivada_6(x):
    return -1/(4*x**1.5) + np.cos(x)

def puntofijo_6(x):
    return np.cos(x)**2

a_6 = 0.1
b_6 = 1.0
x0_6 = 0.5
x1_6 = 1.0


# usamos la funcion de bolzano que es f(1) por f(2) < 0 para ver si existen raices como tal

if __name__ == "__main__":
    print("Polinomica =", fun_1(a_1) * fun_1(b_1))
    print("raiz doble =", fun_2(a_2) * fun_2(b_2))
    print("logaritmica =", fun_3(a_3) * fun_3(b_3))
    print("exponencial =", fun_4(a_4) * fun_4(b_4))
    print("trigonometrica =", fun_5(a_5) * fun_5(b_5))
    print("mixta =", fun_6(a_6) * fun_6(b_6))