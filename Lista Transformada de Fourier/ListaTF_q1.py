import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

plt.style.use('default')
plt.rcParams.update({
    'figure.figsize': [14, 5],
    'axes.grid': True,
    'grid.linestyle': '--',
    'grid.alpha': 0.7,
    'font.size': 12
})

fig = plt.figure(constrained_layout=True)
gs = GridSpec(1, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
t = np.linspace(-0.2, 1, 1000)
f = 2 * np.exp(-5*t) * (t >= 0)

ax1.plot(t, f, 'b', linewidth=2)
ax1.set_title('Função no Tempo', pad=15)
ax1.set_xlabel('Tempo')
ax1.set_ylabel('Amplitude')
ax1.set_xlim([-0.2, 1])
ax1.set_ylim([-0.1, 2.1])
ax1.axhline(0, color='k', linestyle='-', linewidth=0.5)
ax1.axvline(0, color='k', linestyle='-', linewidth=0.5)

ax2 = fig.add_subplot(gs[0, 1])
w = np.linspace(-20, 20, 1000)
magnitude = 2 / np.sqrt(25 + w**2)

ax2.plot(w, magnitude, 'b', linewidth=2)
ax2.set_title('Mag', pad=15)
ax2.set_xlabel('Freq (ω)')
ax2.set_ylabel('Mag')
ax2.set_xlim([-20, 20])
ax2.set_ylim([0, 0.5])
ax2.axvline(0, color='k', linestyle='-', linewidth=0.5)

ax3 = fig.add_subplot(gs[0, 2])
phase = -np.arctan(w/5)

ax3.plot(w, phase, 'b', linewidth=2)
ax3.set_title('Fase', pad=15)
ax3.set_xlabel('Freq (ω)')
ax3.set_ylabel('Fase')
ax3.set_xlim([-20, 20])
ax3.set_ylim([-np.pi/2, np.pi/2])
ax3.axhline(0, color='k', linestyle='-', linewidth=0.5)
ax3.axvline(0, color='k', linestyle='-', linewidth=0.5)

ax3.set_yticks([-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2])
ax3.set_yticklabels(['$-\\pi/2$', '$-\\pi/4$', '0', '$\\pi/4$', '$\\pi/2$'])

plt.show()