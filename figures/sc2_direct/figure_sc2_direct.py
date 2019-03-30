import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from PIL import Image

data1 = np.loadtxt("neb.it0006.dat")
data2 = np.loadtxt("neb.it0007.dat")
distances1 = np.loadtxt("out_data1.txt") * 0.529177
distances2 = np.loadtxt("out_data2.txt") * 0.529177 + distances1[-1]

reaction1 = data1[:, 1] - data1[0, 1]
reaction2 = data2[:, 1] + reaction1[-1]

fig, ax = plt.subplots(figsize=[23, 10])

# Set axis
ax.set_xlim(distances1[0], distances2[-1])
ax.set_ylim(0, np.max(reaction1) + 0.6)
ax.set_xlabel("Nitrogen Displacement($\AA$)", fontsize=30)
ax.set_ylabel("Energy (ev)", fontsize=30)

ax.xaxis.set_ticks(np.arange(distances1[0], distances2[-1], 0.3))
ax.tick_params(labelsize=25)

ax.plot(distances1, reaction1, "-ok", linewidth=4, clip_on=False, markersize=8)
ax.plot(distances2, reaction2, "-ok", linewidth=4, clip_on=False, markersize=8)
ax.grid(True)
ax.set_axisbelow(True)

plt.subplots_adjust(top=0.78)

max1 = np.argmax(reaction1)
min1 = 3
max2 = np.argmax(reaction2)

h = (reaction2[0] + reaction2[max2]) / 2

ax.plot([distances1[0], distances1[max1]], [reaction1[max1], reaction1[max1]], "--k", linewidth=3)
ax.plot([distances1[-1], distances2[max2]], [reaction1[-1], reaction1[-1]], "--k", linewidth=3)
ax.arrow(
    distances1[max1],
    reaction1[max1] / 2,
    0,
    reaction1[max1] / 2 - 0.01,
    width=0.015,
    facecolor="k",
    length_includes_head=True,
    head_width=0.04,
    head_length=0.1,
)
ax.arrow(
    distances1[max1],
    reaction1[max1] / 2,
    0,
    -reaction1[max1] / 2 + 0.01,
    width=0.015,
    facecolor="k",
    length_includes_head=True,
    head_width=0.04,
    head_length=0.1,
)
ax.arrow(
    distances2[max2],
    h,
    0,
    reaction2[max2] - h - 0.01,
    width=0.015,
    facecolor="k",
    length_includes_head=True,
    head_width=0.04,
    head_length=0.1,
)
ax.arrow(
    distances2[max2],
    h,
    0,
    -(reaction2[max2] - h - 0.01),
    width=0.015,
    facecolor="k",
    length_includes_head=True,
    head_width=0.04,
    head_length=0.1,
)

ax.text(
    distances1[max1] + 0.05,
    reaction1[max1] / 2,
    "{:4.2f} eV".format(reaction1[max1]),
    fontsize=25,
)
ax.text(
    distances2[max2] - 0.08,
    reaction2[0] - 0.25,
    "{:4.2f} eV".format(reaction2[max2] - reaction2[0]),
    fontsize=25,
)

image1 = Image.open("posinp1.jpg")
image2 = Image.open("posinp10.jpg")
image3 = Image.open("posinp17.jpg")
image5 = Image.open("posinp33.jpg")

zoom = 0.3
imagebox1 = OffsetImage(image1, zoom=zoom)
imagebox2 = OffsetImage(image2, zoom=zoom)
imagebox3 = OffsetImage(image3, zoom=zoom)
imagebox5 = OffsetImage(image5, zoom=zoom)

imagebox1.image.axes = ax
imagebox2.image.axes = ax
imagebox3.image.axes = ax
imagebox5.image.axes = ax

ab1 = AnnotationBbox(
    imagebox1,
    [distances1[0] + 0.01, reaction1[0] + 0.02],
    xybox=[0.14 * distances2[-1], 5.4],
    arrowprops=dict(arrowstyle="->", linewidth=4),
)
ab2 = AnnotationBbox(
    imagebox2,
    [distances1[max1] + 0.02, reaction1[max1] + 0.01],
    xybox=[0.48 * distances2[-1], 5.4],
    arrowprops=dict(arrowstyle="->", linewidth=4),
)
ab3 = AnnotationBbox(
    imagebox3,
    [distances1[-1] + 0.02, reaction1[-1] + 0.03],
    xybox=[0.80 * distances2[-1], 5.4],
    arrowprops=dict(arrowstyle="->", linewidth=4),
)
ab5 = AnnotationBbox(
    imagebox5,
    [distances2[-1] - 0.02, reaction2[-1] - 0.02],
    xybox=[0.80 * distances2[-1], 1.2],
    arrowprops=dict(arrowstyle="->", linewidth=4),
)

ax.add_artist(ab1)
ax.add_artist(ab2)
ax.add_artist(ab3)
ax.add_artist(ab5)

# Show or save figure
#plt.show()
plt.savefig("sc2_direct", dpi=200)
