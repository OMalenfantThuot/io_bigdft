import functions_briaree as fbr
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#Valeurs calculées
N_graphitic = 0.89
N_adsorbe = 4.37
C_adsorbe = 6.52
N_in = 7.22

reaction = [N_adsorbe, N_in +3, N_in, C_adsorbe + N_graphitic]

#intervalles de la réaction
time = np.linspace(1.,4, 4)

fig,ax = plt.subplots(figsize=[16,11])

ax.plot(time, reaction,'o')
for i in range(3):
    delta = np.linspace(i+1, i+2, 100)
    ax.plot(delta, fbr.sin_interpolate(reaction[i], reaction[i+1], delta))


#Set axis
ax.set_xlim(0.5, 4.5)
ax.set_ylim(np.min(reaction) - 0.5, np.max(reaction) + 0.5)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Time',fontsize=30)
ax.set_ylabel('Energy',fontsize=30)

#Fig values
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()
dps = fig.dpi_scale_trans.inverted()
bbox = ax.get_window_extent().transformed(dps)
width, height = bbox.width, bbox.height

# manual arrowhead width and length
hw = 1./20.*(ymax-ymin)
hl = 1./20.*(xmax-xmin)
lw = 1. # axis line width
ohg = 0.3 # arrow overhang
yhw = hw/(ymax-ymin)*(xmax-xmin)* height/width
yhl = hl/(xmax-xmin)*(ymax-ymin)* width/height

#Draw arrows
ax.arrow(xmin, ymin, xmax-xmin, 0, fc='k', ec='k', lw = lw,
         head_width=hw, head_length=hl, overhang = ohg,
         length_includes_head= True, clip_on = False)
ax.arrow(xmin, ymin, 0, ymax-ymin, fc='k', ec='k', lw = lw,
         head_width=yhw, head_length=yhl, overhang = ohg,
         length_includes_head= True, clip_on = False)

for i,ener in enumerate(reaction):
    ax.plot([time[i] - 0.25, time[i] + 0.25], [ener, ener], 'k')
    ax.text(time[i] - 0.1 , ener-0.3 , '{:4.2f} eV'.format(ener), fontsize = 20)

#patch = patches.Ellipse((time[1], reaction[1]), 0.6, 2, transform=ax.transData)
#image = plt.imread('questionmark.png')
#im = ax.imshow(image)
#im.set_clip_path(patch)
#ax.add_artist(patch)

#fig.tight_layout()
plt.show()
