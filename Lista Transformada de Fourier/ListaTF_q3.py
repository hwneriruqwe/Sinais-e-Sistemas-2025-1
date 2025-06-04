import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 4))

plt.subplot(1, 2, 1)
t1 = np.linspace(-3, 3, 1000)
f1 = np.where((t1 >= -2) & (t1 <= 2), 1, 0)
plt.plot(t1, f1, 'b', linewidth=2)
plt.title('Pulso retangular')
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.xlim(-3, 3)
plt.ylim(-0.1, 1.5)
plt.axvline(0, color='k', linestyle='-', linewidth=0.5)
plt.axhline(0, color='k', linestyle='-', linewidth=0.5)

plt.subplot(1, 2, 2)
t2 = np.linspace(-2, 2, 1000)
f2 = np.where((t2 >= -1) & (t2 <= 1), 1, 0)
plt.plot(t2, f2, 'b', linewidth=2)
plt.title('Pulso escalonado')
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.xlim(-2, 2)
plt.ylim(-0.1, 1.5)
plt.axvline(0, color='k', linestyle='-', linewidth=0.5)
plt.axhline(0, color='k', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.show()