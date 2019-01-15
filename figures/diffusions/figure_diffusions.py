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

fig,ax = plt.subplots(figsize=[16,11])

#Set axis
ax.set_xlim(distancesN[0], distancesN[-1])
ax.set_ylim(np.min(reactionN), np.max(reactionN) + 0.3)
ax.set_xlabel('Atom Displacement($\AA$)',fontsize=30)
ax.set_ylabel('Energy (ev)',fontsize=30)

ax.xaxis.set_ticks(np.arange(distancesN[0], distancesN[-1], 0.1))

ax.plot(distancesN, reactionN,'-o',color='g')
ax.plot(distancesC, reactionC,'-o',color='k')
ax.grid(True)

maxC = np.argmax(reactionC)
maxN = np.argmax(reactionN)

ax.plot([distancesC[0], distancesC[maxC]], [reactionC[maxC], reactionC[maxC]], '--k')
ax.plot([distancesN[0], distancesN[maxN]], [reactionN[maxN], reactionN[maxN]], '--k')

ax.arrow(distancesC[maxC], reactionC[maxC]/2, 0, reactionC[maxC]/2-0.01, width=0.005, facecolor='k',
        length_includes_head=True, head_width=0.025, head_length = 0.1)
ax.arrow(distancesC[maxC], reactionC[maxC]/2, 0, -reactionC[maxC]/2+0.01, width=0.005, facecolor='k',
        length_includes_head=True, head_width=0.025, head_length = 0.1)

#image1 = Image.open('posinp1.jpg')
#image2 = Image.open('posinp9.jpg')
#image3 = Image.open('posinp17.jpg')
#
#zoom = 0.18
#imagebox1 = OffsetImage(image1, zoom = zoom)
#imagebox2 = OffsetImage(image2, zoom = zoom)
#imagebox3 = OffsetImage(image3, zoom = zoom)
#
#imagebox1.image.axes = ax
#imagebox2.image.axes = ax
#imagebox3.image.axes = ax
#
#ab1 = AnnotationBbox(imagebox1, [distances[0], reaction[0]],
#                    xybox = [0.17 * distances[-1], 0.62],
#                    arrowprops=dict(arrowstyle = "->"))
#ab2 = AnnotationBbox(imagebox2, [distances[mid_i], reaction[mid_i]],
#                    xybox = [0.5 * distances[-1], 0.20],
#                    arrowprops=dict(arrowstyle = "->"))
#ab3 = AnnotationBbox(imagebox3, [distances[-1], reaction[-1]],
#                    xybox = [0.83 * distances[-1],0.62],
#                    arrowprops=dict(arrowstyle = "->"))
#
#ax.add_artist(ab1)
#ax.add_artist(ab2)
#ax.add_artist(ab3)

fig.tight_layout()

#Show or save figure
plt.show()
#plt.savefig('diffusion_C', dpi = 300)
