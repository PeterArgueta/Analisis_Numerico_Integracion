import numpy as np

a=2
b=6
n=4
h=(b-a)/n

def f(x):
    return (np.cos(np.sqrt(x)))

def boole(f, a, b, n):
    suma = 0

    for i in range(n):
        x0 =a 
        x1 =a+h
        x2 =a+2*h
        x3 =a+3*h
        x4 =b

        suma = (2*h / 45) * (7 * f(x0) + 32 * f(x1) + 12 * f(x2) + 32 * f(x3) + 7 * f(x4))
    return suma

resultado = boole(f, a, b, n)
print(n, resultado)
