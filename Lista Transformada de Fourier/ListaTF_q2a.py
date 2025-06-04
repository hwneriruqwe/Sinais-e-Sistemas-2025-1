import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 1000)

u = np.where(t >= 0, 1, 0)

# Plotagem
plt.figure(figsize=(12, 4))


plt.subplot(1, 3, 1)
plt.plot(t, u, label='u(t)', color='blue')
plt.title("Função")
plt.xlabel("t")
plt.ylabel("u(t)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

omega = np.linspace(-10, 10, 1000)
epsilon = 1e-12
omega_safe = np.where(omega == 0, epsilon, omega)

delta = np.zeros_like(omega)
delta[np.abs(omega) < 0.05] = 1e3

F_omega = np.pi * delta + 1 / (1j * omega_safe)

magnitude = np.abs(F_omega)
phase = np.angle(F_omega)

plt.subplot(1, 3, 2)
plt.plot(omega, magnitude, 'b', linewidth=2)
plt.title(r'Magnitude')
plt.xlabel(r'$\omega$')
plt.ylabel('Magnitude')
plt.yscale('log')
plt.grid(True)

# Gráfico da Fase
plt.subplot(1, 3, 3)
plt.plot(omega, np.degrees(phase), 'b', linewidth=2)
plt.title(r'Fase$')
plt.xlabel(r'$\omega$')
plt.ylabel('Ângulo')
plt.yticks([-90, 0, 90], [r'$-90^\circ$', r'$0^\circ$', r'$90^\circ$'])
plt.grid(True)

plt.tight_layout()
plt.show()