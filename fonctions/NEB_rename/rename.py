# Script pour renommer les fichiers posinpX.in.ascii
# à posinpX.ascii pour les calculs NEB
# Peut s'appeler comme un exécutable avec un alias

import os

names = os.listdir(os.getcwd())
#print(names)
#print(type(names))

for name in names:
    if name.endswith(".in.ascii"):
        os.rename(name,name.strip(".in.ascii")+".ascii")
