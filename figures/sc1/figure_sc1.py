import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from PIL import Image

data = np.loadtxt('neb.it0005.dat')
distances = np.loadtxt('out_data.txt') * 0.529177

reaction = data[:,1]

fig,ax = plt.subplots(figsize=[16,11])

#Set axis
ax.set_xlim(distances[0], distances[-1])
ax.set_ylim(np.min(reaction), np.max(reaction) + 2)
ax.set_xlabel('Nitrogen Displacement($\AA$)',fontsize=30)
ax.set_ylabel('Energy (ev)',fontsize=30)

ax.xaxis.set_ticks(np.arange(distances[0], distances[-1], 0.2))
ax.tick_params(labelsize=20)

ax.plot(distances, reaction,'k-o', clip_on=False)
ax.grid(True)
ax.set_axisbelow(True)

min_i = 5
max_i = 9
h = (reaction[min_i]+reaction[max_i])/2

ax.plot([distances[min_i], distances[max_i]], [reaction[min_i], reaction[min_i]], '--k')
ax.plot([distances[max_i], distances[-1]], [reaction[-1], reaction[-1]], '--k')
ax.arrow(distances[max_i], h, 0, (reaction[max_i]-h-0.01), width=0.005, facecolor='k',
        length_includes_head=True, head_width=0.025, head_length = 0.1)
ax.arrow(distances[max_i], h, 0, -(reaction[max_i]-h-0.01), width=0.005, facecolor='k',
        length_includes_head=True, head_width=0.025, head_length = 0.1)

plt.subplots_adjust(top=0.95)

#ax.text(distances[max_i] + 0.12, reaction[max_i]-0.008 , '{:4.2f} eV'.format(reaction[max_i]), fontsize = 20)

image1 = Image.open('posinp1.jpg')
image2 = Image.open('posinp5.jpg')
image3 = Image.open('posinp12.jpg')
image4 = Image.open('posinp17.jpg')

zoom = 0.26
imagebox1 = OffsetImage(image1, zoom = zoom)
imagebox2 = OffsetImage(image2, zoom = zoom)
imagebox3 = OffsetImage(image3, zoom = zoom)
imagebox4 = OffsetImage(image4, zoom = zoom)

imagebox1.image.axes = ax
imagebox2.image.axes = ax
imagebox3.image.axes = ax
imagebox4.image.axes = ax

ab1 = AnnotationBbox(imagebox1, [distances[0], reaction[0]],
                    xybox = [0.15 * distances[-1], -4],
                    arrowprops=dict(arrowstyle = "->"))
ab2 = AnnotationBbox(imagebox2, [distances[4], reaction[4]],
                    xybox = [0.5 * distances[-1], -4],
                    arrowprops=dict(arrowstyle = "->"))
ab3 = AnnotationBbox(imagebox3, [distances[11], reaction[11]],
                    xybox = [0.87 * distances[-1], 0.2],
                    arrowprops=dict(arrowstyle = "->"))
ab4 = AnnotationBbox(imagebox4, [distances[-1], reaction[-1]],
                    xybox = [0.87 * distances[-1], -3.3],
                    arrowprops=dict(arrowstyle = "->"))

ax.add_artist(ab1)
ax.add_artist(ab2)
ax.add_artist(ab3)
ax.add_artist(ab4)

#fig.tight_layout()

#Show or save figure
plt.show()
#plt.savefig('scenario_1', dpi = 300)
