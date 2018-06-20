# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
import math as m
import numpy as np
import io_bigdft as io

#Taille de la supercellule entrée par l'utilisateur
x = int(input('Taille de la supercellule en x:\n'))
z = int(input('Taille de la supercellule en z:\n'))

#Définition des longueurs pour la cellule primitive
# et la supercellule
d = 1.42
a_uni = d*np.sqrt(3)
a_big_base_x = a_uni
a_big_base_z = d*3
b_uni = 4*np.pi/(np.sqrt(3)*a_uni)
b_big_base_x = 2*np.pi/a_big_base_x
b_big_base_z = 2*np.pi/a_big_base_z
bx = b_big_base_x/x
bz = b_big_base_z/z

b1k = []
b2k = []

#Nom du fichier contenant les coordonnées des points k
#À générer avec le script generate_grid.py
f = open(input('Nom du fichier contenant la grille de points k:\n'),'r')

#Lecture des points k et conversion en array
for line in f:
    l = line.split()
    b1k.append(float(l[0]))
    b2k.append(float(l[2]))
b1k = np.array(b1k)
b2k = np.array(b2k)

#Conversion en coordonnées cartésiennes
kx = b1k*bx
kz = b2k*bz

#Liste qui contiendra les points à l'intérieur de
#la première ZdB
final = [[] for i in range(len(kx))]
onlim = 0

#Translations possibles entre les points k
trans_x = [bx, 0, -bx, 0]
trans_z = [0, -bz, 0, bz]

#Trouver tous les points à l'intérieur et sur la limite
#de la première ZdB
for i in range(len(kx)):
    final[i].append([round(kx[i],10),round(kz[i],10)])
    j = 0
    while(j<len(final[i])):
        for k in range(len(trans_x)):
            point = [round(final[i][j][0]+trans_x[k],10),round(final[i][j][1]+trans_z[k],10)]
            if point not in final[i]:
                inside = io.first_BZ_hex(point[0],point[1],b_uni)
                if inside[0]:
                    final[i].append(point)
                    if inside[1]:
                        onlim += 1
        j += 1

total = 0

#Nombre de points par Zdb
for i in range(len(final)):
    total += len(final[i])
total = total - onlim/2

#Affichage du résultat
print('La ZdB primitive est discrétisée sur ',str(int(total)),' points.')

#Liste pour le graphique
pointx=[]
pointz=[]
for i in range(len(final)):
    for el in final[i]:
        pointx.append(el[0])
        pointz.append(el[1])

#Affichage du graphique
plt.figure(1,figsize=(9,9))       
io.plot_hex(b_uni,color='k',label='ZdB primitive')
io.plot_rec(bx,bz,color='g',label='ZdB pour cellule 9x5 (180 atomes)')
plt.plot(pointx,pointz,'ob',markersize=2)
plt.plot(0,0,'kx',markersize=10)
plt.plot(1/3*b_uni*np.cos(np.pi/6),1/3*b_uni+1/3*b_uni*np.sin(np.pi/6),'kx',markersize=10)
plt.text(-0.1,-0.1,'$\Gamma$',size='large')
plt.text(1/3*b_uni*np.cos(np.pi/6)-0.1,1/3*b_uni+1/3*b_uni*np.sin(np.pi/6)-0.1,'K',size='large')
#plt.legend(bbox_to_anchor=(1,1),prop={'size':20})
plt.xlabel('kx ($\mathrm{\AA{}}^{-1}$)')
plt.ylabel('kz ($\mathrm{\AA{}}^{-1}$)')
plt.show()
