import numpy as np
import matplotlib.pyplot as plt

w0 = np.pi
t = np.linspace(-2, 2, 1000)

def fourier_series(t, N):
    f_t = np.full_like(t, 1.0)  # b0 = 1
    for n in range(1, N + 1):
        coef = (4 / (n * np.pi)) * np.sin(n * np.pi / 2)
        f_t += coef * np.cos(n * w0 * t)
    return f_t

#Gráficos

plt.figure(figsize=(12, 5))
for i, N in enumerate([10, 50], 1):
    plt.subplot(1, 2, i)
    f = fourier_series(t, N)
    plt.plot(t, f)
    plt.title(f'Série de Fourier com n = {N}')
    plt.grid(True)
plt.tight_layout()
plt.show()