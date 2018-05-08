import numpy as np
import math
import matplotlib.pyplot as plt


def read_ascii(filename):
    data_pos = []
    data_at = []
    f = open(filename,'r')
    for line in f:
        l = line.split()
        if (not line[0]== '#') and (len(l) > 3):
            data_pos.append([float(l[0]),float(l[1]),float(l[2])])
            data_at.append(l[3])
    data_pos = np.array(data_pos)
    return data_pos,data_at
            
    
    

def first_BZ_rec(kx,ky,bx,by):
#kx,ky : coordonnées du point à  vérifier
#bx,by : norme des vecteurs bx et by
    if (-bx/2 < kx <= bx/2) & (-by/2 < ky <= by/2):
        return True
    else:
        return False
        

def first_BZ_hex(kx,ky,b):
#kx,ky : coordonnées du point à  vérifier
#b : norme des vecteurs b
    if (kx > 0) & (ky >= 0):
        theta = math.atan(ky/kx)
    elif (kx < 0):
        theta = math.pi + math.atan(ky/kx)
    elif (kx > 0) & (ky < 0):
        theta = 2*math.pi + math.atan(ky/kx)
    elif (kx == 0):
        if ky >= 0: theta = math.pi/2
        if ky < 0: theta = (3/2)*math.pi
    theta = (theta % (math.pi/3)) - math.pi/6
    l = np.sqrt(kx**2+ky**2)
    lim = b/(2.*math.cos(theta))+0.001
    if l <= lim:
        return True
    if l > lim:
        return False

def plot_hex(b,color='k',label=''):
    r = b/math.sqrt(3)
    hex1 = [-r/2,-r,-r/2, r/2,r,r/2,-r/2]
    hex2 = [ b/2, 0,-b/2,-b/2,0,b/2, b/2]
    plt.plot(hex1,hex2,color=color,label=label)
    plt.axis('equal')
    return

def plot_rec(x,y,color='g',label=''):
    rec1 = [x/2, x/2, -x/2, -x/2, x/2]
    rec2 = [y/2, -y/2, -y/2, y/2, y/2]
    plt.plot(rec1,rec2,color=color,label=label)
    plt.axis('equal')
    return
