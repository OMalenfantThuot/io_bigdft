import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from PIL import Image

data = np.loadtxt('neb.it0012.dat')
distances = np.loadtxt('out_data.txt') * 0.529177

reaction = data[:,1]

fig,ax = plt.subplots(figsize=[16,11])

#Set axis
ax.set_xlim(distances[0], distances[-1])
ax.set_ylim(0, np.max(reaction) + 0.6)
ax.set_xlabel('Nitrogen Displacement($\AA$)',fontsize=30)
ax.set_ylabel('Energy (ev)',fontsize=30)

ax.xaxis.set_ticks(np.arange(distances[0], distances[-1], 0.1))

ax.plot(distances, reaction,'-o')
ax.grid(True)

max_i = np.argmax(reaction)

ax.plot([distances[0], distances[max_i]], [reaction[max_i], reaction[max_i]], '--k')
ax.plot([distances[max_i], distances[-1]], [reaction[-1], reaction[-1]], '--k')
ax.arrow(distances[max_i], reaction[-1], 0, reaction[max_i]-reaction[-1]-0.01, width=0.005, facecolor='k',
        length_includes_head=True, head_width=0.025, head_length = 0.1)
ax.arrow(distances[max_i], reaction[-1], 0, -reaction[-1]+0.01, width=0.005, facecolor='k',
        length_includes_head=True, head_width=0.025, head_length = 0.1)


#ax.text(distances[max_i] + 0.12, reaction[max_i]-0.008 , '{:4.2f} eV'.format(reaction[max_i]), fontsize = 20)

#image1 = Image.open('posinp1.jpg')
#image2 = Image.open('posinp9.jpg')
#image3 = Image.open('posinp17.jpg')
#
#zoom = 0.38
#imagebox1 = OffsetImage(image1, zoom = zoom)
#imagebox2 = OffsetImage(image2, zoom = zoom)
#imagebox3 = OffsetImage(image3, zoom = zoom)
#
#imagebox1.image.axes = ax
#imagebox2.image.axes = ax
#imagebox3.image.axes = ax
#
#ab1 = AnnotationBbox(imagebox1, [distances[0], reaction[0]],
#                    xybox = [0.13 * distances[-1], 0.9],
#                    arrowprops=dict(arrowstyle = "->"))
#ab2 = AnnotationBbox(imagebox2, [distances[8], reaction[9]],
#                    xybox = [0.5 * distances[-1], 0.4],
#                    arrowprops=dict(arrowstyle = "->"))
#ab3 = AnnotationBbox(imagebox3, [distances[-1], reaction[-1]],
#                    xybox = [0.87 * distances[-1],0.9],
#                    arrowprops=dict(arrowstyle = "->"))
#
#ax.add_artist(ab1)
#ax.add_artist(ab2)
#ax.add_artist(ab3)

fig.tight_layout()

#Show or save figure
plt.show()
#plt.savefig('diffusion_N', dpi = 300)
