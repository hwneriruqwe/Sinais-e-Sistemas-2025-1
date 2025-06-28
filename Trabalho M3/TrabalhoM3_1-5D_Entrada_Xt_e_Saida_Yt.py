import numpy as np
import matplotlib.pyplot as plt

# Vetor de tempo
t = np.linspace(0, 0.5, 1000)  # 0 a 0.5 segundos
u = (t >= 0).astype(float)     # Degrau unitário
x = 2 * u                      # Entrada x(t)

# Cada saída y(t)
y_1_1 = 2 * np.exp(-10*t) * u
y_1_2 = 2 * np.exp(-100*t) * u
y_2   = 0.2 * np.exp(-50*t) * np.cos(998.75*t + np.deg2rad(90)) * u
y_3   = (2 + 0.16*np.exp(-1164*t) - 2.16*np.exp(-85.9*t)) * u
y_4   = (2 + 2.04*np.exp(-50*t)*np.cos(998.75*t + np.deg2rad(2.8))) * u
y_5   = (2 + 0.4*np.exp(-435*t) - 2.4*np.exp(-114*t)) * u

# Agrupar todas as saídas num dicionário
respostas = {
    "1.1": y_1_1,
    "1.2": y_1_2,
    "2": y_2,
    "3": y_3,
    "4": y_4,
    "5": y_5,
}

# Criar figura com subplots: 3 linhas x 2 colunas
fig, axs = plt.subplots(3, 2, figsize=(12, 10))
axs = axs.flatten()

for i, (nome, y) in enumerate(respostas.items()):
    axs[i].plot(t, x, label='x(t)', color='black', linewidth=2)
    axs[i].plot(t, y, label=f'y(t) {nome}')
    axs[i].set_xlabel('Tempo (s)')
    axs[i].set_ylabel('Amplitude')
    axs[i].set_title(f'Resposta y(t) {nome} e a entrada x(t)')
    axs[i].legend()
    axs[i].grid(True)
    axs[i].set_xlim(0, 0.5)

plt.tight_layout()
plt.show()
