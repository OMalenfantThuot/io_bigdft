import matplotlib.pyplot as plt
import numpy as np

# Load data
dftresO = np.loadtxt("dft_results_O2.txt")
dftresN = np.loadtxt("dft_results_N2.txt")
mlresO = np.loadtxt("ml_results_O2.txt")
mlresN = np.loadtxt("ml_results_N2.txt")
datalist = [dftresO, mlresO, dftresN, mlresN]

# Set a 0 energy
for d in datalist:
    d[:, 1] = d[:, 1] - np.min(d[:, 1])

# Forces processing
O_i, O_j = np.where(np.abs(dftresO[:,2:]) > 0.01)
N_i, N_j = np.where(np.abs(dftresN[:,2:]) > 0.01)

dftforcesO, mlforcesO = dftresO[:,2:][O_i,O_j], mlresO[:,2:][O_i,O_j]
dftforcesN, mlforcesN = dftresN[:,2:][N_i,N_j], mlresN[:,2:][N_i,N_j]

comparisonO = (dftforcesO-mlforcesO)/dftforcesO
comparisonN = (dftforcesN-mlforcesN)/dftforcesN

# Generate graphs
fig, ax = plt.subplots(nrows=2, ncols=2)
ax1, ax2, ax3, ax4 = ax.flatten()

ax1.set_title("O_2 molecule - energy")
ax1.plot(dftresO[:, 0], dftresO[:, 1], label="dft")
ax1.plot(dftresO[:, 0], mlresO[:, 1], label="ml")
ax1.legend()

ax2.set_title("O_2 molecule - forces")
ax2.plot(dftforcesO, comparisonO, 'o')
ax2.axhline(y=0, color='k')
ax2.axhline(y=1, color='k')

ax3.set_title("N_2 molecule - energy")
ax3.plot(dftresN[:, 0], dftresN[:, 1], label="dft")
ax3.plot(dftresN[:, 0], mlresN[:, 1], label="ml")
ax3.legend()

ax4.set_title("N_2 molecule - forces")
ax4.plot(dftforcesN, comparisonN, 'o')
ax4.axhline(y=0, color='k')

fig.tight_layout()

#plt.show()
plt.savefig('graph.jpg', dpi=350)
