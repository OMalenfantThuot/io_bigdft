# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:44:11 2017

@author: oliviermt
"""

#Script pour convertir les tailles de cellules

import io_bigdft as io
import numpy as np
import sys

data_pos, data_at = io.read_ascii(sys.argv[1])
#data_pos = np.where(1-data_pos < 0.5,data_pos,data_pos)

Nat = len(data_at)

if Nat == 0:
    x_init = 0
    y_init = 0
elif Nat >= 29 and Nat <= 34:
    x_init = 4
    z_init = 2
elif Nat >= 94 and Nat <= 98:
    x_init = 6
    z_init = 4
elif Nat >= 110 and Nat <= 114:
    x_init = 7
    z_init = 4
elif Nat >= 177 and Nat <= 183:
    x_init = 9
    z_init = 5
else:
    print("Format de cellule d'entrée non reconnu")
    exit()

Nat_fin = int(sys.argv[2])

if Nat_fin == 180:
    x_fin = 9
    z_fin = 5
    x_cell = 41.9649
    z_cell = 40.38075
elif Nat_fin == 96:
    x_fin = 6
    z_fin = 4
    x_cell = 27.9766
    z_cell = 32.3046
elif Nat_fin == 288:
    x_fin = 12
    z_fin = 6
    x_cell = 55.9532
    z_cell = 48.4569
elif Nat_fin == 60:
    x_fin = 5
    z_fin = 3
    x_cell = 23.31383
    z_cell = 24.22845
elif Nat_fin == 336:
    x_fin = 12
    z_fin = 7
    x_cell = 55.9531
    z_cell = 56.53305
else:
    print("Format de cellule de sortie non reconnu")
    exit()

deltax_r = int(np.ceil((x_fin-x_init)/2))
deltax_l = int(np.floor((x_fin-x_init)/2))
deltaz_u = int(np.ceil((z_fin-z_init)/2))
deltaz_d = int(np.floor((z_fin-z_init)/2))

Nat_fin = Nat + ((x_fin-x_init)*z_fin + (z_fin-z_init)*x_init)*4
pos_fin = np.zeros([Nat_fin,3])
pos_fin[0:Nat,0] = (data_pos[0:Nat,0]+deltax_r/x_fin*x_cell)
pos_fin[0:Nat,1] = data_pos[0:Nat,1]
pos_fin[0:Nat,2] = (data_pos[0:Nat,2]+deltaz_d/z_fin*z_cell)

x1 = np.arange(0.,2.*x_fin,2)/(2*x_fin)
x2 = np.arange(1.,2.*x_fin,2)/(2*x_fin)
z1 = np.arange(0,4.*z_fin,2)
z2 = np.arange(1,4.*z_fin,2)

for i in range(len(z1)):
    if i%2 == 0:
        z2[i] = z2[i]+1
    if i%2 == 1:
        z1[i] = z1[i]-1

for i in range(2*z_fin):
    if i%2 == 0:
        z1[i] = z1[i]/(4*z_fin)
        z2[i] = z2[i]/(4*z_fin)
    if i%2 == 1:
        z1[i] = z1[i]/(4*z_fin)+1./(12*z_fin)
        z2[i] = z2[i]/(4*z_fin)+1./(12*z_fin)

tempx = []
tempz = []

for i in range(deltaz_d*4):
    for j in range(x_fin):
        if i%4 == 0:
            tempx.append(x1[j])
            tempz.append(z1[int(i/2)])
        if i%4 == 1:
            tempx.append(x1[j])
            tempz.append(z1[int((i-1)/2+1)])
        if i%4 == 2:
            tempx.append(x2[j])
            tempz.append(z2[int((i-2)/2)])
        if i%4 == 3:
            tempx.append(x2[j])
            tempz.append(z2[int((i-3)/2+1)])
            
for i in range(z_init*4):
    for j in range(deltax_r):
        if i%4 == 0:
            tempx.append(x1[j])
            tempz.append(z1[int(i/2+2*deltaz_d)])
        if i%4 == 1:
            tempx.append(x1[j])
            tempz.append(z1[int((i-1)/2+1+2*deltaz_d)])
        if i%4 == 2:
            tempx.append(x2[j])
            tempz.append(z2[int((i-2)/2+2*deltaz_d)])
        if i%4 == 3:
            tempx.append(x2[j])
            tempz.append(z2[int((i-3)/2+1+2*deltaz_d)])
    for j in range(deltax_l):
        if i%4 == 0:
            tempx.append(x1[j+deltax_r+x_init])
            tempz.append(z1[int(i/2+2*deltaz_d)])
        if i%4 == 1:
            tempx.append(x1[j+deltax_r+x_init])
            tempz.append(z1[int((i-1)/2+1+2*deltaz_d)])
        if i%4 == 2:
            tempx.append(x2[j+deltax_r+x_init])
            tempz.append(z2[int((i-2)/2+2*deltaz_d)])
        if i%4 == 3:
            tempx.append(x2[j+deltax_r+x_init])
            tempz.append(z2[int((i-3)/2+1+2*deltaz_d)])

for i in range(deltaz_u*4):
    for j in range(x_fin):
        if i%4 == 0:
            tempx.append(x1[j])
            tempz.append(z1[int(i/2+2*deltaz_d+2*z_init)])
        if i%4 == 1:
            tempx.append(x1[j])
            tempz.append(z1[int((i-1)/2+1+2*deltaz_d+2*z_init)])
        if i%4 == 2:
            tempx.append(x2[j])
            tempz.append(z2[int((i-2)/2+2*deltaz_d+2*z_init)])
        if i%4 == 3:
            tempx.append(x2[j])
            tempz.append(z2[int((i-3)/2+1+2*deltaz_d+2*z_init)])

tempx = np.array(tempx)
tempz = np.array(tempz)

pos_fin[Nat:Nat+len(tempx),0] = tempx*x_cell
pos_fin[Nat:Nat+len(tempz),2] = tempz*z_cell
pos_fin[Nat:Nat+len(tempz),1] = 20

output_file = "out_posinp.ascii"

g = open(output_file,'w')
g.write("#Fichier de positions à "+str(Nat_fin)+" atomes.\n")
g.write(str(x_cell)+" 0 40\n")
g.write("0 0 "+str(z_cell)+"\n")
g.write("#keyword: atomicd0\n")
g.write("#keyword: surface\n")
for i in range(Nat):
    g.write('%.15f'%(pos_fin[i,0])+"\t"+'%.15f'%(pos_fin[i,1])+"\t"+'%.15f'%(pos_fin[i,2])+"\t"+str(data_at[i])+"\n")
g.write('#Nouveaux atomes\n')
for i in range(Nat,max(pos_fin.shape)):
    g.write('%.15f'%(pos_fin[i,0])+"\t"+'%.15f'%(pos_fin[i,1])+"\t"+'%.15f'%(pos_fin[i,2])+"\tC\n")
