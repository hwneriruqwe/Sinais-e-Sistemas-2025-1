import numpy as np
import matplotlib.pyplot as plt

# Dados dos zeros e polos para cada K
sistemas = {
    "K = 1": {
        "zeros": [100],          # zero constante (sem raiz finita)
        "polos": [1, 20, 200]
    },
    "K = 2": {
        "zeros": [200],
        "polos": [1, 20, 300]
    },
    "K = 10": {
        "zeros": [1000],
        "polos": [1, 20, 1100]
    },
    "K = 100": {
        "zeros": [10000],
        "polos": [1, 20, 10100]
    }
}

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()

for idx, (k, dados) in enumerate(sistemas.items()):
    zeros = np.roots(dados["zeros"])  # zeros vazios (sem raízes)
    polos = np.roots(dados["polos"])

    ax = axs[idx]

    # Plot zeros (não existem zeros finitos, então só legenda)
    if len(zeros) > 0:
        ax.plot(zeros.real, zeros.imag, 'bo', markersize=10, label='Zeros')
    else:
        ax.plot([], [], 'bo', label='Zeros')  # legenda sem pontos

    # Plot polos
    ax.plot(polos.real, polos.imag, 'rx', markersize=10, label='Polos')

    # Eixos
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_title(f'Diagrama de Polos e Zeros — {k}')
    ax.set_xlabel('Eixo Real')
    ax.set_ylabel('Eixo Imaginário')
    ax.grid(True)
    ax.legend()

    # Ajustar limites com margem
    real_parts = list(polos.real) + list(zeros.real)
    imag_parts = list(polos.imag) + list(zeros.imag)

    real_min, real_max = min(real_parts), max(real_parts)
    imag_max_abs = max(abs(im) for im in imag_parts)

    ax.set_xlim(real_min - 10, real_max + 10)
    ax.set_ylim(-imag_max_abs - 10, imag_max_abs + 10)

plt.tight_layout()
plt.suptitle('Diagramas de Polos e Zeros para diferentes valores de K', fontsize=16, y=1.02)
plt.show()
