import numpy as np

a=2
b=6
n=10

def f(x):
    return(np.cos(np.sqrt(x)))

def trapecio(f, a, b, n):
    h = (b - a) / n
    suma = 0

    for i in range(1, n):
        x = a + i * h
        suma += f(x)

    resultado = (h / 2) * (f(a) + 2 * suma + f(b))
    return resultado
    
resultadotrapecio=trapecio(f,a,b,n)

print(resultadotrapecio)