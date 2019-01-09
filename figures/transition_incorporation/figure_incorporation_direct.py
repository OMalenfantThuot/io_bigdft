import functions_briaree as fbr
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#Valeurs calculées
E_start = 6
E_N_adsorbe = 4.5
E_N_diffusion = 5.6
E_reac = 8.3
E_doped_init = 6.5
E_doped_diffusion = 7.3
E_final = 6.2

reaction = [E_start, E_N_adsorbe, E_N_diffusion, E_N_adsorbe, E_reac, E_doped_init,
            E_doped_diffusion, E_final]

#intervalles de la réaction
time = np.linspace(1.,len(reaction), len(reaction))


fig,ax = plt.subplots(figsize=[16,11])

ax.set_facecolor('xkcd:silver')
ax.plot(time, reaction,'o')
color = ['k','r','k','r','k','r','k']
for i in range(len(reaction)-1):
    delta = np.linspace(i+1, i+2, 100)
    ax.plot(delta, fbr.sin_interpolate(reaction[i], reaction[i+1], delta), color=color[i])


#Set axis
ax.set_xlim(0.5, len(reaction)+0.5)
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

xoffset = [-0.4, -0.4, -0.55, -0.4, -0.7, -0.4, -0.55, -0.4]
yoffset = [0.1,-0.24,0.1,-0.24,0.1,-0.24,0.1,-0.24]
texts = ['Initial state', 'Adsorbed N', 'N diffusion TS', 'Adsorbed N',
         'Functionalisation TS', 'Adsorbed C', 'C diffusion TS', 'Final state']

for i,ener in enumerate(reaction):
    ax.plot([time[i] - 0.25, time[i] + 0.25], [ener, ener], 'k')
    ax.text(time[i] + xoffset[i] , ener + yoffset[i] , texts[i], fontsize = 20)

fig.tight_layout()
plt.savefig('reaction.png')
#plt.show()
