import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from PIL import Image

data = np.loadtxt("neb.it0004.dat")
distances = np.loadtxt("out_data.txt") * 0.529177

reaction = data[:, 1]

fig, ax = plt.subplots(figsize=[14, 11])

# Set axis
ax.set_xlim(distances[0], distances[-1])
ax.set_ylim(np.min(reaction), np.max(reaction) + 2)
ax.set_xlabel("Nitrogen Displacement($\AA$)", fontsize=35)
ax.set_ylabel("Energy (ev)", fontsize=35)

ax.xaxis.set_ticks(np.arange(distances[0], distances[-1], 0.4))
ax.tick_params(labelsize=30)

ax.plot(distances, reaction, "k-o", linewidth=4, clip_on=False, markersize=8)
ax.grid(True)
ax.set_axisbelow(True)

min_i = 5
max_i = 14
h = (reaction[min_i] + reaction[max_i]) / 2

ax.plot([distances[min_i], distances[max_i]], [reaction[min_i], reaction[min_i]], "--k", linewidth=3)
ax.plot([distances[max_i], distances[-1]], [reaction[-1], reaction[-1]], "--k", linewidth=3)
ax.arrow(
    distances[max_i],
    h,
    0,
    (reaction[max_i] - h - 0.01),
    width=0.015,
    facecolor="k",
    length_includes_head=True,
    head_width=0.04,
    head_length=0.1,
)
ax.arrow(
    distances[max_i],
    h,
    0,
    -(reaction[max_i] - h - 0.01),
    width=0.015,
    facecolor="k",
    length_includes_head=True,
    head_width=0.04,
    head_length=0.1,
)

plt.subplots_adjust(top=0.95)

ax.text(
    distances[max_i] - 0.33,
    reaction[min_i] - 0.55,
    "{:4.2f} eV".format(reaction[max_i] - reaction[min_i]),
    fontsize=30,
)

image1 = Image.open("posinp1.jpg")
image2 = Image.open("posinp6.jpg")
image3 = Image.open("posinp10.jpg")
image4 = Image.open("posinp17.jpg")

zoom = 0.255
imagebox1 = OffsetImage(image1, zoom=zoom)
imagebox2 = OffsetImage(image2, zoom=zoom)
imagebox3 = OffsetImage(image3, zoom=zoom)
imagebox4 = OffsetImage(image4, zoom=zoom)

imagebox1.image.axes = ax
imagebox2.image.axes = ax
imagebox3.image.axes = ax
imagebox4.image.axes = ax

ab1 = AnnotationBbox(
    imagebox1,
    [distances[0] + 0.02, reaction[0] - 0.03],
    xybox=[0.16 * distances[-1], -4.5],
    arrowprops=dict(arrowstyle="->", linewidth=4),
)
ab2 = AnnotationBbox(
    imagebox2,
    [distances[5] + 0.02, reaction[5] - 0.03],
    xybox=[0.47 * distances[-1], -4.5],
    arrowprops=dict(arrowstyle="->", linewidth=4),
)
ab3 = AnnotationBbox(
    imagebox3,
    [distances[max_i] + 0.02, reaction[max_i] + 0.02],
    xybox=[0.75 * distances[-1], 0.6],
    arrowprops=dict(arrowstyle="->", linewidth=4),
)
ab4 = AnnotationBbox(
    imagebox4,
    [distances[-1] - 0.01, reaction[-1] + 0.03],
    xybox=[0.87 * distances[-1], -3.2],
    arrowprops=dict(arrowstyle="->", linewidth=4),
)

ax.add_artist(ab1)
ax.add_artist(ab2)
ax.add_artist(ab3)
ax.add_artist(ab4)

# Show or save figure
#plt.show()
plt.savefig("scenario_1.eps")
