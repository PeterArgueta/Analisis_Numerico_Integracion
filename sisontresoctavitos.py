import numpy as np

a=2  
b=6  
n=9

h = (b-a)/n

def f(x):
    return(np.cos(np.sqrt(x)))

def simpson(f, a, b, n):

    terminosmultiplosdetres = 0
    losdemas = 0

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            terminosmultiplosdetres += f(x)
        else:
            losdemas += f(x)

    resultado = (3 * h / 8) * (f(a) + 3 * losdemas + 2 * terminosmultiplosdetres + f(b))
    return resultado


resultadosimpson = simpson(f, a, b, n)
print(n, resultadosimpson)

""" for n in range(10, 100, 10):
    resultadosimpson = simpson(f, a, b, n)
    print(n, resultadosimpson)
 """