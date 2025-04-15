#Função original
import numpy as np
import matplotlib.pyplot as plt

#Definição dos pontos
arrayt = np.array([-2, -1, 0, 2, 2])  # Valores do eixo t
arrayx = np.array([0, -1, 2, 2, 0])  # Valores do eixo x(t)
tO = arrayt
xO = arrayx

tA = arrayt-2
xA = arrayx

tB = arrayt+2
xB = arrayx

tC = arrayt*2
xC = arrayx*3

tD = -arrayt
xD = arrayx

tE = arrayt/2
xE = -arrayx

tF = -arrayt+3
xF = arrayx

plt.figure(figsize=(10, 8))

#Original

plt.subplot(3, 3, 2)
plt.step(tO, xO, where='post', linestyle='-', linewidth=2, label='x(t)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('Gráfico Original')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.legend()

#A

plt.subplot(3, 3, 4)
plt.step(tA, xA, where='post', linestyle='-', linewidth=2, label='x(t)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('Gráfico A')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.legend()

#B

plt.subplot(3, 3, 5)
plt.step(tB, xB, where='post', linestyle='-', linewidth=2, label='x(t)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('Gráfico B')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.legend()

#C

plt.subplot(3, 3, 6)
plt.step(tC, xC, where='post', linestyle='-', linewidth=2, label='x(t)')
plt.axhline(0, color='black', linewidth=1)  # Linha horizontal
plt.axvline(0, color='black', linewidth=1)  # Linha vertical
plt.title('Gráfico C')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.legend()

#D

plt.subplot(3, 3, 7)
plt.step(tD, xD, where='post', linestyle='-', linewidth=2, label='x(t)')
plt.axhline(0, color='black', linewidth=1)  # Linha horizontal
plt.axvline(0, color='black', linewidth=1)  # Linha vertical
plt.title('Gráfico D')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.legend()

#E

plt.subplot(3, 3, 8)
plt.step(tE, xE, where='post', linestyle='-', linewidth=2, label='x(t)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('Gráfico E')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.legend()

#F

plt.subplot(3, 3, 9)
plt.step(tF, xF, where='post', linestyle='-', linewidth=2, label='x(t)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('Gráfico F')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.legend()

plt.show()