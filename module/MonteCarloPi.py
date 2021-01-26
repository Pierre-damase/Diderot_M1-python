# IX.
import sys
import os
import random as rand
import numpy as np
import time

tps_debut = time.time()

if len(sys.argv) != 2:
    sys.exit("Veuillez renseigner un argument!")

try: # Tester si l'argument rentré est bien un int 
    nb_point_rand = int(sys.argv[1]) # Convertible => est un int
except ValueError:
    sys.exit("Veuillez renseigner un int!")

nb_point_ds_cercle = 0

for index in range(nb_point_rand):
    # pass Définir un bloc de code qui ne fait rien
    abs_x = rand.uniform(-1,1)
    ord_y = rand.uniform(-1,1)

    distance = np.sqrt(np.power(0-abs_x,2) + np.power(0-ord_y,2))

    if distance <= 1:
        nb_point_ds_cercle += 1

pi = 4 * (nb_point_ds_cercle / nb_point_rand)

tps_fin = time.time()

print("Pour {} itérations, l'estimation de pi est {:.6f} avec un temps d'éxécution de {} s ".format(nb_point_rand,pi,tps_fin-tps_debut))
