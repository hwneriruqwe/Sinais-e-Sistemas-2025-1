import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 5))

plt.subplot(1, 3, 1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Gráfico de $f(t) = u(t) - e^{-t}u(t)$', fontsize=14)
plt.xlabel('t', fontsize=12)
plt.ylabel('f(t)', fontsize=12)
plt.xlim(-1, 5)
plt.ylim(-0.1, 1.1)
def f(t):
    return np.where(t >= 0, 1 - np.exp(-t), 0)
t = np.linspace(-1, 5, 1000)
plt.plot(t, f(t), 'b', linewidth=2)
plt.axhline(y=1, color='gray', linestyle=':', alpha=0.5)
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.5)

plt.subplot(1, 3, 2)
w = np.linspace(-10, 10, 1000)
w_nonzero = w.copy()
w_nonzero[w == 0] = np.nan
magnitude = 1 / (np.abs(w_nonzero) * np.sqrt(1 + w_nonzero**2))
plt.plot(w, magnitude, 'b', linewidth=2)
plt.title('Magnitude')
plt.xlabel('$\\omega$')
plt.ylabel('|F($\\omega$)|')
plt.grid(True)
plt.xlim(-10, 10)
plt.ylim(0, 5)

plt.subplot(1, 3, 3)
phase = -np.pi/2 - np.arctan(w)
plt.plot(w, phase, 'b', linewidth=2)
plt.title('Fase')
plt.xlabel('$\\omega$')
plt.ylabel('∠F($\\omega$)')
plt.grid(True)
plt.xlim(-10, 10)
plt.ylim(-np.pi, np.pi)

plt.tight_layout()
plt.show()