import numpy as np
import matplotlib.pyplot as plt

# Tempo
t = np.linspace(0, 1, 1000)
u = (t >= 0).astype(float)  # Degrau unitário
x = u  # Entrada x(t) = u(t)

# Saídas corrigidas com ângulos em radianos
y1 = (0.5 + 0.70 * np.exp(-10*t) * np.cos(10*t - np.deg2rad(225))) * u
y2 = (2/3 + 0.80 * np.exp(-10*t) * np.cos(14.14*t - np.deg2rad(215.3))) * u
y10 = (0.91 + 0.98 * np.exp(-10*t) * np.cos(31.62*t - np.deg2rad(197.78))) * u
y100 = (0.99 + 0.99 * np.exp(-10*t) * np.cos(99.99*t - np.deg2rad(185.71))) * u

# Organizar as saídas
respostas = {
    "K = 1": y1,
    "K = 2": y2,
    "K = 10": y10,
    "K = 100": y100,
}

# Cores para cada resposta
cores = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.flatten()

for i, (k, y) in enumerate(respostas.items()):
    axs[i].plot(t, x, label='x(t) = u(t)', color='black', linewidth=2)
    axs[i].plot(t, y, label=f'y(t) para {k}', color=cores[i], linewidth=1.5)
    axs[i].set_xlabel('Tempo (s)')
    axs[i].set_ylabel('Amplitude')
    axs[i].set_title(f'Resposta do sistema — {k}')
    axs[i].legend()
    axs[i].grid(True)
    axs[i].set_xlim(0, 1)
    axs[i].set_ylim(0, 1.6)

plt.tight_layout()
plt.show()
