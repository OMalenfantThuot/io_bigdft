import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from PIL import Image

data = np.loadtxt('neb.it0001.dat')
distances = np.loadtxt('out_data.txt') * 0.529177

reaction = data[:,1]
time = data[:,0]

fig,ax = plt.subplots(figsize=[16,11])

#Set axis
ax.set_xlim(distances[0], distances[-1])
ax.set_ylim(np.min(reaction), np.max(reaction) + 0.3)
ax.set_xlabel('Carbon Displacement($\AA$)',fontsize=30)
ax.set_ylabel('Energy (ev)',fontsize=30)

ax.xaxis.set_ticks(np.arange(distances[0], distances[-1], 0.1))

ax.plot(distances, reaction,'-o')
ax.grid(True)

mid_i = int(np.floor(distances.shape[0]/2))
ax.plot([distances[0], distances[mid_i] + 0.1], [reaction[mid_i], reaction[mid_i]], '--k')
ax.text(distances[mid_i] + 0.12, reaction[mid_i]-0.008 , '{:4.2f} eV'.format(reaction[mid_i]), fontsize = 20)

image1 = Image.open('posinp1.jpg')
image2 = Image.open('posinp9.jpg')
image3 = Image.open('posinp17.jpg')

zoom = 0.18
imagebox1 = OffsetImage(image1, zoom = zoom)
imagebox2 = OffsetImage(image2, zoom = zoom)
imagebox3 = OffsetImage(image3, zoom = zoom)

imagebox1.image.axes = ax
imagebox2.image.axes = ax
imagebox3.image.axes = ax

ab1 = AnnotationBbox(imagebox1, [distances[0], reaction[0]],
                    xybox = [0.17 * distances[-1], 0.7],
                    arrowprops=dict(arrowstyle = "->"))
ab2 = AnnotationBbox(imagebox2, [distances[mid_i], reaction[mid_i]],
                    xybox = [0.5 * distances[-1], 0.7],
                    arrowprops=dict(arrowstyle = "->"))
ab3 = AnnotationBbox(imagebox3, [distances[-1], reaction[-1]],
                    xybox = [0.83 * distances[-1],0.7],
                    arrowprops=dict(arrowstyle = "->"))

ax.add_artist(ab1)
ax.add_artist(ab2)
ax.add_artist(ab3)

#Show or save figure
plt.show()
#plt.savefig('diffusion_C', dpi = 300)
