import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from PIL import Image

data = np.loadtxt('neb.it0035.dat')

reaction = data[:,1]
time = data[:,0]

fig,ax = plt.subplots(figsize=[16,11])

#Set axis
ax.set_xlim(time[0], time[-1])
ax.set_ylim(np.min(reaction), np.max(reaction) + 0.3)
ax.set_xlabel('Reaction Coordinate',fontsize=30)
ax.set_ylabel('Energy',fontsize=30)

ax.xaxis.set_ticks(time)

ax.plot(time, reaction,'-o')
ax.grid(True)

mid_i = int(np.floor(time.shape[0]/2))
ax.plot([time[0], time[mid_i] + 0.1], [reaction[mid_i], reaction[mid_i]], '--k')
ax.text(time[mid_i] + 0.12, reaction[mid_i]-0.008 , '{:4.2f} eV'.format(reaction[mid_i]), fontsize = 20)

image1 = Image.open('posinp1.jpg')
image2 = Image.open('posinp9.jpg')
image3 = Image.open('posinp17.jpg')

zoom = 0.17
imagebox1 = OffsetImage(image1, zoom = zoom)
imagebox2 = OffsetImage(image2, zoom = zoom)
imagebox3 = OffsetImage(image3, zoom = zoom)

imagebox1.image.axes = ax
imagebox2.image.axes = ax
imagebox3.image.axes = ax

ab1 = AnnotationBbox(imagebox1, [time[0], reaction[0]],
                    xybox = [0.15 * time[-1], 0.5])
ab2 = AnnotationBbox(imagebox2, [time[0], reaction[0]],
                    xybox = [0.5 * time[-1], 0.5])
ab3 = AnnotationBbox(imagebox3, [time[0], reaction[0]],
                    xybox = [0.85 * time[-1],0.5])

ax.add_artist(ab1)
ax.add_artist(ab2)
ax.add_artist(ab3)

#plt.show()
plt.savefig('diffusion_C', dpi = 300)
