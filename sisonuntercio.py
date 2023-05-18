import numpy as np

a=2
b=6
n=10

def f(x):
    return(np.cos(np.sqrt(x)))

def simpson(f, a, b, n):
    h = (b - a) / n
    sumaimpar = 0
    sumapar = 0

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sumapar += f(x)
        else:
            sumaimpar += f(x)

    resultado = (h / 3) * (f(a) + 4 * sumaimpar + 2 * sumapar + f(b))
    return resultado

for n in range(10,100,10):  
    resultadosimpson=simpson(f,a,b,n)
    print(n, resultadosimpson)