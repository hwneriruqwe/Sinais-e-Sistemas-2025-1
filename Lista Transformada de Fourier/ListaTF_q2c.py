import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4, 1000)

delta = np.zeros_like(t)

index_2 = np.argmin(np.abs(t - 2))

delta[index_2] = 1 / (t[1] - t[0])  # Área ≈ 1

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(t, delta, label=r'$\delta(t - 2)$', color='blue')
plt.title("Aproximação Discreta de δ(t - 2)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

omega = np.linspace(-10, 10, 1000)

F_omega = np.exp(-1j * 2 * omega)

magnitude = np.abs(F_omega)
phase = np.angle(F_omega)


plt.subplot(1, 3, 2)
plt.plot(omega, magnitude, 'b', linewidth=2)
plt.title(r'Magnitude')
plt.xlabel(r'$\omega$')
plt.ylabel('Magnitude')
plt.ylim(0, 1.5)
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(omega, phase, 'r', linewidth=2)
plt.title(r'Fase')
plt.xlabel(r'$\omega$ ')
plt.ylabel('Fase')
plt.grid(True)

plt.tight_layout()
plt.show()