import math
import matplotlib.pyplot as plt

def f(x):
    return 2 * math.sqrt(1 - x**2)

def suma_inf(N):
    a = -1
    b = 1
    dx = (b - a) / N
    total = 0

    for i in range(N):
        x1 = a + i * dx
        x2 = a + (i + 1) * dx

        if f(x1) < f(x2):
            minimo = f(x1)
        else:
            minimo = f(x2)

        total += minimo * dx

    return total

def suma_sup(N):
    a = -1
    b = 1
    dx = (b - a) / N
    total = 0

    for i in range(N):
        x1 = a + i * dx
        x2 = a + (i + 1) * dx

        if f(x1) > f(x2):
            maximo = f(x1)
        else:
            maximo = f(x2)

        total += maximo * dx

    return total

def mostrar_tabla(Ns, titulo):
    print("\n" + titulo)
    print("N | Suma inferior | Residuo inferior | Suma superior | Residuo superior")
    print("-" * 75)

    for N in Ns:
        inf = suma_inf(N)
        sup = suma_sup(N)

        print(
            N, "|",
            round(inf, 6), "|",
            round(inf - math.pi, 6), "|",
            round(sup, 6), "|",
            round(sup - math.pi, 6)
        )

# Tablas pedidas
Ns_1 = list(range(10, 101, 10))
Ns_2 = list(range(100, 1001, 100))
Ns_3 = list(range(1000, 10001, 1000))

mostrar_tabla(Ns_1, "Tabla 1: N de 10 a 100")
mostrar_tabla(Ns_2, "Tabla 2: N de 100 a 1000")
mostrar_tabla(Ns_3, "Tabla 3: N de 1000 a 10000")

# Datos para el gráfico
Ns_grafico = Ns_1 + Ns_2 + Ns_3

inf_vals = []
sup_vals = []

for N in Ns_grafico:
    inf_vals.append(suma_inf(N))
    sup_vals.append(suma_sup(N))

# Gráfico
plt.plot(Ns_grafico, inf_vals, label="Suma inferior")
plt.plot(Ns_grafico, sup_vals, label="Suma superior")
plt.axhline(y=math.pi, linestyle="--", label="π teórico")

plt.xlabel("Cantidad de subintervalos (N)")
plt.ylabel("Valor aproximado")
plt.title("Convergencia de suma inferior y suma superior")
plt.legend()
plt.grid()

plt.show()