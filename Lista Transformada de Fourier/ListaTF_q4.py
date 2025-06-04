import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
t = np.linspace(0, 0.02, 1000)

f1 = np.cos(2*np.pi*200*t) + np.cos(2*np.pi*400*t)
f2 = np.cos(2*np.pi*800*t) + np.cos(2*np.pi*1600*t)

plt.subplot(2, 2, 1)
plt.plot(t, f1, 'b')
plt.title('$f_1(t)')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, 0.02)

# Plot f2(t)
plt.subplot(2, 2, 2)
plt.plot(t, f2, 'b')
plt.title('$f_2(t)')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, 0.02)

w = np.linspace(-3000, 3000, 2000)

def delta(x, a):
    return np.where(np.abs(x - a) < 10, 1, 0)

F1 = (delta(w, 400*np.pi) + delta(w, -400*np.pi) + 
      delta(w, 800*np.pi) + delta(w, -800*np.pi)) * np.pi

F2 = (delta(w, 1600*np.pi) + delta(w, -1600*np.pi) + 
      delta(w, 3200*np.pi) + delta(w, -3200*np.pi)) * np.pi/4

plt.subplot(2, 2, 3)
plt.stem(w/np.pi, F1, 'b', markerfmt='bo', basefmt=" ")
plt.title('$F_1(\omega)$')
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid(True)
plt.xlim(-1000, 1000)
plt.ylim(0, 4)

plt.subplot(2, 2, 4)
plt.stem(w/np.pi, F2, 'b', markerfmt='bo', basefmt=" ")
plt.title('$F_2(\omega)$')
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid(True)
plt.xlim(-1000, 1000)
plt.ylim(0, 4)

plt.tight_layout()
plt.show()