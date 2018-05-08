# Script pour générer les fichiers contenant les positions
# des grilles de points k pour le script grille_bigdft.py

import numpy as np

filename = input('Nom du fichier de sortie:\n')
gridx = int(input('Taille de la grille en x:\n'))
gridz = int(input('Taille de la grille en z:\n'))

if gridx%2 == 0:
	coordx = np.linspace(-0.5 + 1./gridx, 0.5, num = gridx)
	coordz = np.linspace(-0.5 + 1./gridz, 0.5, num = gridz)
else:
	coordx = np.linspace(-0.5 + 1./(2*gridx), 0.5 - 1./(2*gridx), num = gridx)
	coordz = np.linspace(-0.5 + 1./(2*gridz), 0.5 - 1./(2*gridz), num = gridz)


f = open(filename,'w')
for i in range(len(coordx)):
	for j in range(len(coordz)):
		f.write('%11.8f'%(coordx[i]) + '\t' + '%11.8f'%(0) + '\t' + '%11.8f'%(coordz[j]) + '\n')
f.close()
