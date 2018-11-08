import functions_briaree as fbr
import numpy as np
import os
import re
import shutil

images = [filename for filename in os.listdir() if ('posinp' or 'posout') in filename]
nimages = len(images)
pos = fbr.Posinp()
pos.def_from_file(images[0])
natoms = len(pos.atompos)

with open('out_data.txt', 'w') as out:
    total_pos = np.zeros((nimages, natoms, 3))
    for file in os.listdir():
        if 'posinp' in file:
            image_num = int(re.findall('\d+',file)[0])
            pos = fbr.Posinp()
            pos.def_from_file(file)
            total_pos[image_num-1] = pos.atompos
    total_displacement = np.sqrt(np.sum((total_pos[-1]-total_pos[0])**2, axis=1))
    displaced_atom = np.argmax(total_displacement)
    for i in range(nimages):
        displacement = np.sqrt(np.sum((total_pos[i][displaced_atom,:] - total_pos[0][displaced_atom,:])**2))
        out.write('{:> 20.17E}\n'.format(displacement))
shutil.move('out_data.txt', '../')