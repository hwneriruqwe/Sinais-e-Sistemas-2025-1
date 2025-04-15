import math
import numpy as np
import matplotlib.pyplot as plt

def magnitudeA(w):
    return 3/math.sqrt(9+math.pow(w,2))

def faseA(w):
    return math.degrees(-math.atan(w/3))

w_valuesA = np.linspace(-10, 10, 100)

mag_valuesA = [magnitudeA(w) for w in w_valuesA]
fase_valuesA = [faseA(w) for w in w_valuesA]

def magnitudeB(w):
    return 5*abs(w)/math.sqrt(9+math.pow(w,2))

def faseB(w):
    if w > 0:
        return 90-math.degrees((math.atan(w/3))) 
    elif w < 0:
        return -90-math.degrees((math.atan(w/3))) 
    else:
        return None

w_valuesB = np.linspace(-10, 10, 100)

mag_valuesB = [magnitudeB(w) for w in w_valuesB]
fase_valuesB = [faseB(w) for w in w_valuesB]

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(w_valuesA, mag_valuesA, label='Magnitude A')
plt.xlabel('w')
plt.ylabel('Magnitude A')
plt.title('Gráfico da Magnitude - A')
plt.grid()
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(w_valuesA, fase_valuesA, label='Fase A', color='r')
plt.xlabel('w')
plt.ylabel('Fase A')
plt.title('Gráfico da Fase - A')
plt.grid()
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(w_valuesB, mag_valuesB, label='Magnitude B')
plt.xlabel('w')
plt.ylabel('Magnitude B')
plt.title('Gráfico da Magnitude - B')
plt.grid()
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(w_valuesB, fase_valuesB, label='Fase B', color='r')
plt.xlabel('w')
plt.ylabel('Fase B')
plt.title('Gráfico da Fase - B')
plt.grid()
plt.legend()
 
plt.tight_layout()
plt.show()