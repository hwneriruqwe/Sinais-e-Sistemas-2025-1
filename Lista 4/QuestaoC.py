import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 10, 1000)
x = np.where(t >= -1, 1, 0)
h = np.where(t >= 0, np.exp(-t), 0)
dt = t[1] - t[0]
y = np.convolve(x, h) * dt
t_conv = np.linspace(2*t[0], 2*t[-1], len(y))

# Gráficos
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Função x(t)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, h)
plt.title('Função h(t)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_conv, y)
plt.title('Convolução y(t) = x(t) * h(t)')
plt.grid(True)
plt.show()