import math
import random
import matplotlib.pyplot as plt
import numpy as np

PI = math.pi

def f(x):
    return 2 * math.sqrt(1 - x**2)

def monte_carlo(N, seed=None):
    rng = random.Random(seed)
    hits = 0
    for _ in range(N):
        r1 = rng.random()
        r2 = rng.random()
        x = 2 * r1 - 1
        y = 2 * r2
        if y <= f(x):
            hits += 1
    return 4 * hits / N

def tabla_montecarlo(N_values, seed=42):
    rng = random.Random(seed)
    print(f"{'N':>6} | {'Monte Carlo':>12} | {'Residuo':>12}")
    print("-" * 38)
    for N in N_values:
        val = monte_carlo(N, seed=rng.randint(0, 10**9))
        print(f"{N:>6} | {val:>12.6f} | {val - PI:>12.6f}")

def figura_montecarlo():
    N_vals = (list(range(10, 101, 10))
              + list(range(100, 1001, 100))
              + list(range(1000, 10001, 1000)))
    mc_vals = [monte_carlo(n, seed=n * 7) for n in N_vals]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(N_vals, mc_vals, color='purple', alpha=0.75, lw=1, label='Monte Carlo')
    ax.axhline(PI, color='red', linestyle='--', lw=1.2, label='π teórico')
    ax.set_xlabel('Cantidad de puntos (N)')
    ax.set_ylabel('Valor aproximado de π')
    ax.set_title('Estimación de π mediante el método de Monte Carlo')
    ax.legend()
    ax.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig('figura8_montecarlo.png', dpi=150)
    plt.show()

def metodo_rectangulos(N, a=-1, b=1):
    dx = (b - a) / N
    return sum(f(a + i * dx) * dx for i in range(N))

def metodo_punto_medio(N, a=-1, b=1):
    dx = (b - a) / N
    return sum(f(a + (i + 0.5) * dx) * dx for i in range(N))

def figura_errores_log():
    Ns = (list(range(10, 101, 10))
          + list(range(200, 1001, 100))
          + list(range(2000, 10001, 1000)))
    err_rect = [abs(metodo_rectangulos(n) - PI) for n in Ns]
    err_mid  = [abs(metodo_punto_medio(n)  - PI) for n in Ns]
    err_mc   = [abs(monte_carlo(n, seed=n * 3) - PI) for n in Ns]

    ref = np.array([100, 10000])
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.loglog(Ns, err_rect, 'b-',           lw=1.5, label='Rectángulos / Trapecio')
    ax.loglog(Ns, err_mid,  'g-',           lw=1.5, label='Punto medio')
    ax.loglog(Ns, err_mc,   color='purple', lw=1, alpha=0.8, label='Monte Carlo')
    ax.loglog(ref, 0.1  * (ref / 100) ** -1.5, 'b--', alpha=0.5, label='O(N⁻¹·⁵) ref')
    ax.loglog(ref, 0.35 * (ref / 100) ** -0.5, 'm--', alpha=0.5, label='O(N⁻⁰·⁵) ref')
    ax.set_xlabel('N (escala logarítmica)')
    ax.set_ylabel('|error| (escala logarítmica)')
    ax.set_title('Comparación de errores por método (escala log-log)')
    ax.legend(fontsize=9)
    ax.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig('figura9_errores.png', dpi=150)
    plt.show()

if __name__ == '__main__':
    print("=" * 70)
    print("Tabla 10: Monte Carlo, N de 10 a 100")
    print("=" * 70)
    tabla_montecarlo(range(10, 101, 10))

    print("\n" + "=" * 70)
    print("Tabla 11: Monte Carlo, N de 100 a 1000")
    print("=" * 70)
    tabla_montecarlo(range(100, 1001, 100))

    print("\n" + "=" * 70)
    print("Tabla 12: Monte Carlo, N de 1000 a 10000")
    print("=" * 70)
    tabla_montecarlo(range(1000, 10001, 1000))

    figura_montecarlo()
    figura_errores_log()