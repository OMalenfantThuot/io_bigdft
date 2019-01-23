import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from PIL import Image

dataN = np.loadtxt('nebN.dat')
dataC = np.loadtxt('nebC.dat')
distancesC = np.loadtxt('out_data_C.txt') * 0.529177
distancesN = np.loadtxt('out_data_N.txt') * 0.529177

reactionN = dataN[:,1]
reactionC = dataC[:,1]

fig,ax = plt.subplots(figsize=[14,11])

#Set axis
ax.set_xlim(distancesN[0], distancesN[-1])
ax.set_ylim(np.min(reactionN), np.max(reactionN) + 0.1)
ax.set_xlabel('Atom Displacement($\AA$)',fontsize=30)
ax.set_ylabel('Energy (ev)',fontsize=30)

ax.xaxis.set_ticks(np.arange(distancesN[0], distancesN[-1], 0.1))
ax.tick_params(labelsize=20)

ax.plot(distancesN, reactionN,'-o',color='g')
ax.plot(distancesC, reactionC,'-o',color='k')
ax.grid(True)
ax.set_axisbelow(True)

maxC = np.argmax(reactionC)
maxN = np.argmax(reactionN)

ax.plot([distancesC[0], distancesC[maxC]], [reactionC[maxC], reactionC[maxC]], '--k')
ax.plot([distancesN[0], distancesN[maxN]], [reactionN[maxN], reactionN[maxN]], '--k')

ax.arrow(distancesC[maxC], reactionC[maxC]/2, 0, reactionC[maxC]/2-0.01, width=0.003, facecolor='k',
        length_includes_head=True, head_width=0.02, head_length = 0.08)
ax.arrow(distancesC[maxC], reactionC[maxC]/2, 0, -reactionC[maxC]/2+0.01, width=0.003, facecolor='k',
        length_includes_head=True, head_width=0.02, head_length = 0.08)

ax.arrow(distancesN[maxN], reactionN[maxN]/2, 0, reactionN[maxN]/2-0.01, width=0.003, facecolor='g',
        edgecolor = 'g', length_includes_head=True, head_width=0.02, head_length = 0.08)
ax.arrow(distancesN[maxN], reactionN[maxN]/2, 0, -reactionN[maxN]/2+0.01, width=0.003, facecolor='g',
        edgecolor = 'g', length_includes_head=True, head_width=0.02, head_length = 0.08)

plt.subplots_adjust(top=0.75)

C1 = Image.open('C1.jpg')
C2 = Image.open('C9.jpg')
C3 = Image.open('C17.jpg')

zoom = 0.16
imagebox1 = OffsetImage(C1, zoom = zoom)
imagebox2 = OffsetImage(C2, zoom = zoom)
imagebox3 = OffsetImage(C3, zoom = zoom)

imagebox1.image.axes = ax
imagebox2.image.axes = ax
imagebox3.image.axes = ax

ab1 = AnnotationBbox(imagebox1, [distancesC[0], reactionC[0]],
                    xybox = [0.17 * distancesC[-1], 1.22],
                    arrowprops=dict(arrowstyle = "->"))
ab2 = AnnotationBbox(imagebox2, [distancesC[maxC], reactionC[maxC]],
                    xybox = [0.5 * distancesC[-1], 1.22],
                    arrowprops=dict(arrowstyle = "->"))
ab3 = AnnotationBbox(imagebox3, [distancesC[-1], reactionC[-1]],
                    xybox = [0.83 * distancesC[-1], 1.22],
                    arrowprops=dict(arrowstyle = "->"))

ax.add_artist(ab1)
ax.add_artist(ab2)
ax.add_artist(ab3)

#fig.tight_layout()

#Show or save figure
#plt.show()
plt.savefig('diffusion_C', dpi = 300)
