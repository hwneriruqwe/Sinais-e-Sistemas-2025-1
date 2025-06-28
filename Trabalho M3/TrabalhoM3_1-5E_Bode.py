import numpy as np
import matplotlib.pyplot as plt

# Frequência w
w = np.logspace(0, 5, 1000)

systems = [
    {
        'mag': 20*np.log10(1/10) + 20*np.log10(w) - 20*np.log10((w/10)+1),
        'fase': 90 - np.degrees(np.arctan(w/10)),
        'title': 'Bode 1.1'
    },
    {
        'mag': 20*np.log10(1/100) + 20*np.log10(w) - 20*np.log10((w/100)+1),
        'fase': 90 - np.degrees(np.arctan(w/100)),
        'title': 'Bode 1.2'
    },
    {
        'mag': -80 - 10*np.log10((w**4/1e12) - (1.99*w**2/1e6) + 1),
        'fase': 90 - np.degrees(np.arctan((1e4*w)/(1e6 - w**2))),
        'title': 'Bode 2'
    },
    {
        'mag': 100 - 10*np.log10(w**2+1354896) - 10*np.log10(w**2+7378.81),
        'fase': -np.degrees(np.arctan(w**2/1354896)) - np.degrees(np.arctan(w**2/7378.81)),
        'title': 'Bode 3'
    },
    {
        'mag': 10*np.log10((w**4/1e12)+1) - 10*np.log10((w**4/1e12) - (1.99*w**2/1e6) + 1),
        'fase': np.degrees(np.arctan(-w**2/1e6)) - np.degrees(np.arctan((1e4*w)/(1e6 - w**2))),
        'title': 'Bode 4'
    },
    {
        'mag': 10*np.log10(5e6+(w**2)*(50**2)) - 10*np.log10(w**2+435.08**2) - 10*np.log10(w**2+144.92**2),
        'fase': np.degrees(np.arctan(w/100)) - np.degrees(np.arctan(w/435.08)) - np.degrees(np.arctan(w/144.92)),
        'title': 'Bode 5'
    }
]

fig, axs = plt.subplots(len(systems), 2, figsize=(12, 18), sharex=True)

for i, sys in enumerate(systems):
    # Magnitude no eixo da esquerda
    axs[i, 0].semilogx(w, sys['mag'], label='Magnitude')
    axs[i, 0].set_ylabel('Magnitude (dB)')
    axs[i, 0].grid(True, which='both')
    axs[i, 0].legend()
    axs[i, 0].set_title(sys['title'])

    # Fase no eixo da direita
    axs[i, 1].semilogx(w, sys['fase'], color='orange', label='Fase')
    axs[i, 1].set_ylabel('Fase (graus)')
    axs[i, 1].grid(True, which='both')
    axs[i, 1].legend()

# Label comum do eixo x (frequência)
for ax in axs[-1, :]:
    ax.set_xlabel('Frequência (rad/s)')

plt.tight_layout()
plt.show()
