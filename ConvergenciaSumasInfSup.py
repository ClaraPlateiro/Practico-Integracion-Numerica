import math
import pandas as pd
import matplotlib.pyplot as plt

# Función del ejercicio
def f(x):
    return 2 * math.sqrt(1 - x**2)

# Suma inferior
def suma_inferior(N):
    a = -1
    b = 1
    dx = (b - a) / N
    suma = 0

    for i in range(N):
        x_izq = a + i * dx
        x_der = a + (i + 1) * dx

        minimo = min(f(x_izq), f(x_der))
        suma += minimo * dx

    return suma

# Suma superior
def suma_superior(N):
    a = -1
    b = 1
    dx = (b - a) / N
    suma = 0

    for i in range(N):
        x_izq = a + i * dx
        x_der = a + (i + 1) * dx

        maximo = max(f(x_izq), f(x_der))
        suma += maximo * dx

    return suma

# Generar tabla
def generar_tabla(valores_N):
    datos = []

    for N in valores_N:
        inf = suma_inferior(N)
        sup = suma_superior(N)

        datos.append({
            "N": N,
            "Suma inferior": inf,
            "Residuo inferior": inf - math.pi,
            "Suma superior": sup,
            "Residuo superior": sup - math.pi
        })

    return pd.DataFrame(datos)