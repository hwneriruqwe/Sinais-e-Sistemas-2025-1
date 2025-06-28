import numpy as np
import matplotlib.pyplot as plt

# Coeficientes dos polinômios de zeros e polos
sistemas = {
    "1.1": {
        "zeros": [1, 0],
        "polos": [1, 10]
    },
    "1.2": {
        "zeros": [1, 0],
        "polos": [1, 100]
    },
    "2": {
        "zeros": [100, 0],
        "polos": [1, 100, 1e6]
    },
    "3": {
        "zeros": [1e5],
        "polos": [1, 1250, 1e5]
    },
    "4": {
        "zeros": [1, 0, 1e6],
        "polos": [1, 100, 1e6]
    },
    "5": {
        "zeros": [50, 5e4],
        "polos": [1, 550, 5e4]
    }
}

# Criar figura e eixos com subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
axs = axs.flatten()

# Loop para calcular raízes e plotar
for idx, (key, dados) in enumerate(sistemas.items()):
    zeros = np.roots(dados["zeros"])
    polos = np.roots(dados["polos"])

    ax = axs[idx]

    # Plotar zeros e polos
    if len(zeros) > 0:
        ax.scatter([z.real for z in zeros], [z.imag for z in zeros],
                   color='blue', marker='o', label='Zeros')
    if len(polos) > 0:
        ax.scatter([p.real for p in polos], [p.imag for p in polos],
                   color='red', marker='x', label='Polos')

    # Eixos e grade
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
    ax.grid(True)
    ax.set_title(f'Sistema {key}')
    
    # Ajuste automático de limites com margem
    todos = np.concatenate((zeros, polos)) if len(zeros) > 0 else polos
    if len(todos) > 0:
        real_vals = [p.real for p in todos]
        imag_vals = [p.imag for p in todos]
        margem = 0.2

        real_min, real_max = min(real_vals), max(real_vals)
        imag_min, imag_max = min(imag_vals), max(imag_vals)

        real_range = real_max - real_min if real_max != real_min else 1
        imag_range = imag_max - imag_min if imag_max != imag_min else 1

        ax.set_xlim(real_min - margem * real_range, real_max + margem * real_range)
        ax.set_ylim(imag_min - margem * imag_range, imag_max + margem * imag_range)
    else:
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)

# Título geral
fig.suptitle('Diagramas de Polos e Zeros dos Sistemas', fontsize=16)
fig.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
