import numpy as np
import matplotlib.pyplot as plt

zeros = [3j]
polos = [0, -1, -2]

plt.figure(figsize=(8, 8))

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.scatter(np.real(zeros), np.imag(zeros), marker='o', s=100, facecolors='none', edgecolors='b')
plt.scatter(np.real(polos), np.imag(polos), marker='x', s=100, color='b', linewidth=2)

plt.xlabel('Real', labelpad=10)
plt.ylabel('Imaginária', labelpad=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal')
plt.xlim(-5, 2)
plt.ylim(-5, 5)
plt.legend()

plt.show()