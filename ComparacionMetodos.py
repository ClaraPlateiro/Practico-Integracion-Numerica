import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

PI = math.pi

def f(x):
    return 2 * math.sqrt(1 - x**2)

def metodo_rectangulos(N, a=-1, b=1):
    dx = (b - a) / N
    return sum(f(a + i * dx) * dx for i in range(N))

def metodo_trapecio(N, a=-1, b=1):
    dx = (b - a) / N
    total = 0.0
    for i in range(N):
        xi  = a + i * dx
        xi1 = a + (i + 1) * dx
        total += (f(xi) + f(xi1)) / 2 * dx
    return total

def metodo_punto_medio(N, a=-1, b=1):
    dx = (b - a) / N
    return sum(f(a + (i + 0.5) * dx) * dx for i in range(N))

def tabla_metodos(N_values):
    header = f"{'N':>6} | {'Rect.':>10} | {'Res. rect':>11} | {'Trap.':>10} | {'Res. trap':>11} | {'Pto.med.':>10} | {'Res. med.':>11}"
    print(header)
    print("-" * len(header))
    for N in N_values:
        r = metodo_rectangulos(N)
        t = metodo_trapecio(N)
        m = metodo_punto_medio(N)
        print(f"{N:>6} | {r:>10.6f} | {r-PI:>11.6f} | {t:>10.6f} | {t-PI:>11.6f} | {m:>10.6f} | {m-PI:>11.6f}")

def figura_metodos():
    N_vals = (list(range(10, 101, 10))
              + list(range(100, 1001, 100))
              + list(range(1000, 10001, 1000)))
    rect_v = [metodo_rectangulos(n) for n in N_vals]
    trap_v = [metodo_trapecio(n)    for n in N_vals]
    mid_v  = [metodo_punto_medio(n) for n in N_vals]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(N_vals, rect_v, label='Rectángulos', color='steelblue')
    ax.plot(N_vals, trap_v, label='Trapecio',    color='orange', linestyle='--', lw=1.5)
    ax.plot(N_vals, mid_v,  label='Punto medio', color='green')
    ax.axhline(PI, color='red', linestyle='--', label='π teórico', lw=1.2)
    ax.set_xlabel('Cantidad de subintervalos (N)')
    ax.set_ylabel('Valor aproximado de la integral')
    ax.set_title('Comparación de métodos de integración numérica')
    ax.legend()
    ax.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig('figura6_metodos.png', dpi=150)
    plt.show()

def figura_punto_medio(N=100):
    a, b = -1, 1
    dx   = (b - a) / N
    xs   = np.linspace(a, b, 600)
    colors = plt.cm.tab20(np.linspace(0, 1, N))

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(xs, [f(x) for x in xs], 'b-', lw=2, label='f(x)', zorder=3)
    for i in range(N):
        xi = a + i * dx
        xm = xi + dx / 2
        rect = patches.Rectangle((xi, 0), dx, f(xm),
                                  lw=0.3, edgecolor='gray',
                                  facecolor=colors[i], alpha=0.6)
        ax.add_patch(rect)
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(0, 2.15)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'Método del punto medio (N = {N})')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('figura7_puntomedio.png', dpi=150)
    plt.show()


if __name__ == '__main__':
    print("=" * 70)
    print("Tabla 7: N de 10 a 100")
    print("=" * 70)
    tabla_metodos(range(10, 101, 10))

    print("\n" + "=" * 70)
    print("Tabla 8: N de 100 a 1000")
    print("=" * 70)
    tabla_metodos(range(100, 1001, 100))

    print("\n" + "=" * 70)
    print("Tabla 9: N de 1000 a 10000")
    print("=" * 70)
    tabla_metodos(range(1000, 10001, 1000))

    figura_metodos()
    figura_punto_medio(N=100)