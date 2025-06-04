import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 1000)

f = np.full_like(t, -3)

plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
plt.plot(t, f, label='f(t) = -3', color='blue')
plt.title('Função Constante f(t) = -3')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.ylim(0, -5)

w = np.linspace(-10, 10, 1000)

magnitude = np.zeros_like(w)
magnitude[np.abs(w) < 0.01] = 6 * np.pi  # pico no zero

phase = np.zeros_like(w)

plt.subplot(1, 3, 2)
plt.plot(w, magnitude, label='|F(ω)|', color='blue')
plt.title('Magnitude')
plt.xlabel('ω')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(w, phase, label='∠F(ω)', color='blue')
plt.title('Fase')
plt.xlabel('ω')
plt.ylabel('Fase')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
