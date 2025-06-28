import numpy as np
import matplotlib.pyplot as plt

# Vetor de tempo
t = np.linspace(0, 1, 1000)
u = (t >= 0).astype(float)  # Degrau unitário

# Entrada
x = u  # x(t) = u(t)

# Saída
y = (1 - np.exp(-10*t) - 10*t*np.exp(-10*t)) * u

# Plotar
plt.figure(figsize=(8, 4))
plt.plot(t, x, label='x(t) = u(t)', color='black', linewidth=2)
plt.plot(t, y, label='y(t) = (1 - e^(-10t) - 10t·e^(-10t))·u(t)', color='tab:blue')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Entrada x(t) e saída y(t)')
plt.legend()
plt.grid(True)
plt.xlim(0, 1)
plt.ylim(-0.2, 1.2)
plt.show()
