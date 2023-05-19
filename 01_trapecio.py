import numpy as np
import pandas as pd
a=2
b=6
#n=10

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


lista=[]
for n in range(10,100,10):   
    resultadotrapecio=trapecio(f,a,b,n)
    print(n,resultadotrapecio)
    lista.append([n,resultadotrapecio])
df=pd.DataFrame(lista, columns=['n', 'metododeltrapecio'])
print(df.to_latex())