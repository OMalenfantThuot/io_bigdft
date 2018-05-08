#Script pour créer un graphique pour les barrières de réaction pour les calculs NEB
# à partir des fichiers .dat de BigDFT

import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.signal import argrelextrema

filename = str(sys.argv[1])
data_reac = []
data_ener = []

f = open(filename)
for line in f:
    l = line.split()
    data_reac.append(float(l[0]))
    data_ener.append(float(l[1]))
data_reac = np.array(data_reac)
data_ener = np.array(data_ener)

data_reac = data_reac/max(data_reac)
maximums = argrelextrema(data_ener,np.greater)[0]

plt.figure(1)
plt.plot(data_reac,data_ener,'b')
for m in maximums:
    plt.plot([0,data_reac[m]],[data_ener[m],data_ener[m]],'--k')
    plt.text(0,data_ener[m]*0.95,'%2.2f'%(data_ener[m]))
plt.xlabel('Coordonnée de réaction')
plt.ylabel('Énergie relative (eV)')
plt.show()
