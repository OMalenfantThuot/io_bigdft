import matplotlib.pyplot as plt
import numpy as np

#Valeurs calculées
N_graphitic = 0.89
N_adsorbe = 4.37
C_adsorbe = 6.52
N_in = 7.22

reaction = [N_adsorbe, N_in +3, N_in, C_adsorbe + N_graphitic]

#intervalles de la réaction
time = np.linspace(1.,4.,4)
delta1 = np.linspace(1.,2.,100)

plt.figure(1)
plt.plot(time, reaction,'o')
plt.plot(delta1, (reaction[0]+reaction[1])/2 + (reaction[0]-reaction[1])/2*np.sin((delta1-0.5)*(np.pi)))
plt.show(block='True')
