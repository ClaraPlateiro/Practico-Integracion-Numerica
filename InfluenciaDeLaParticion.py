import math
import random
import matplotlib.pyplot as plt

def f(x):
    return 2 * math.sqrt(1 - x**2)

# -----------------------------
# Particiones
# -----------------------------

def particion_equi(N):
    a = -1
    b = 1
    dx = (b - a) / N

    puntos = []
    for i in range(N + 1):
        puntos.append(a + i * dx)

    return puntos


def particion_aleatoria(N):
    puntos = [-1, 1]

    for i in range(N - 1):
        puntos.append(random.uniform(-1, 1))

    puntos.sort()
    return puntos


def particion_coseno(N):
    puntos = []

    for i in range(N + 1):
        x = math.cos(i * math.pi / N)
        puntos.append(x)

    puntos.sort()
    return puntos


# -----------------------------
# Suma inferior para cualquier partición
# -----------------------------

def suma_inferior_particion(puntos):
    total = 0

    for i in range(len(puntos) - 1):
        x1 = puntos[i]
        x2 = puntos[i + 1]

        ancho = x2 - x1

        if f(x1) < f(x2):
            altura = f(x1)
        else:
            altura = f(x2)

        total += altura * ancho

    return total


# -----------------------------
# Mostrar tablas
# -----------------------------

def mostrar_tabla(Ns, titulo):
    print("\n" + titulo)
    print("N | Equiespaciada | Residuo equi | Aleatoria | Residuo aleatoria | Coseno | Residuo coseno")
    print("-" * 105)

    for N in Ns:
        equi = suma_inferior_particion(particion_equi(N))
        alea = suma_inferior_particion(particion_aleatoria(N))
        cos = suma_inferior_particion(particion_coseno(N))

        print(
            N, "|",
            round(equi, 6), "|",
            round(equi - math.pi, 6), "|",
            round(alea, 6), "|",
            round(alea - math.pi, 6), "|",
            round(cos, 6), "|",
            round(cos - math.pi, 6)
        )


# Para que la partición aleatoria sea reproducible
random.seed(10)

Ns_1 = list(range(10, 101, 10))
Ns_2 = list(range(100, 1001, 100))
Ns_3 = list(range(1000, 10001, 1000))

mostrar_tabla(Ns_1, "Tabla 1: N de 10 a 100")
mostrar_tabla(Ns_2, "Tabla 2: N de 100 a 1000")
mostrar_tabla(Ns_3, "Tabla 3: N de 1000 a 10000")


# -----------------------------
# Gráfico de las tres particiones
# -----------------------------

random.seed(10)

Ns_grafico = Ns_1 + Ns_2 + Ns_3

valores_equi = []
valores_alea = []
valores_cos = []

for N in Ns_grafico:
    valores_equi.append(suma_inferior_particion(particion_equi(N)))
    valores_alea.append(suma_inferior_particion(particion_aleatoria(N)))
    valores_cos.append(suma_inferior_particion(particion_coseno(N)))

plt.plot(Ns_grafico, valores_equi, label="Equiespaciada")
plt.plot(Ns_grafico, valores_alea, label="Aleatoria uniforme")
plt.plot(Ns_grafico, valores_cos, label="Coseno")
plt.axhline(y=math.pi, linestyle="--", label="π teórico")

plt.xlabel("Cantidad de subintervalos (N)")
plt.ylabel("Valor aproximado de la integral")
plt.title("Influencia de la partición en la aproximación")
plt.legend()
plt.grid()

plt.show()


# -----------------------------
# Gráficos con rectángulos para N = 100
# -----------------------------

def graficar_rectangulos(puntos, titulo):
    xs = []
    ys = []

    for i in range(300):
        x = -1 + 2 * i / 299
        xs.append(x)
        ys.append(f(x))

    plt.plot(xs, ys, label="f(x)")

    for i in range(len(puntos) - 1):
        x1 = puntos[i]
        x2 = puntos[i + 1]

        ancho = x2 - x1
        altura = min(f(x1), f(x2))

        plt.bar(
            x1,
            altura,
            width=ancho,
            align="edge",
            alpha=0.3,
            edgecolor="black"
        )

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(titulo)
    plt.legend()
    plt.grid()
    plt.show()


random.seed(10)

N = 100

graficar_rectangulos(particion_equi(N), "Rectángulos con partición equiespaciada (N = 100)")
graficar_rectangulos(particion_aleatoria(N), "Rectángulos con partición aleatoria uniforme (N = 100)")
graficar_rectangulos(particion_coseno(N), "Rectángulos con partición tipo coseno (N = 100)")