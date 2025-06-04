import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 1000)

delta = np.zeros_like(t)

index_zero = len(t) // 2

delta[index_zero] = 2 / (t[1] - t[0])

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(t, delta, label='2·δ(t)', color='blue')
plt.title("Aproximação Discreta de 2·δ(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

omega = np.linspace(-10, 10, 1000)

F_omega = 2 * np.ones_like(omega)

magnitude = np.abs(F_omega)
phase = np.angle(F_omega)


plt.subplot(1, 3, 2)
plt.plot(omega, magnitude, 'b', linewidth=2)
plt.title(r'Magnitude')
plt.xlabel(r'$\omega$')
plt.ylabel('Magnitude')
plt.ylim(0, 3)
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(omega, np.degrees(phase), 'b', linewidth=2)
plt.title(r'Fase')
plt.xlabel(r'$\omega$')
plt.ylabel('Ângulo (graus)')
plt.yticks([0], [r'$0^\circ$'])
plt.grid(True)

plt.tight_layout()
plt.show()
