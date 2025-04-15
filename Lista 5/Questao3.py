import numpy as np
import matplotlib.pyplot as plt

n = np.array([0, 1, 2, 3])
amplitudes = np.array([2, 5, 3, 2])
fases_deg = np.array([0, -53.1, -48.2, -60])  # em graus

# Gráfico
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.stem(n, amplitudes)
plt.title("Espectro de Amplitude")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(n, fases_deg)
plt.title("Espectro de Fase (graus)")
plt.grid(True)

plt.tight_layout()
plt.show()
