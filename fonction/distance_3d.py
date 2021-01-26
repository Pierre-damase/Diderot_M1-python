import numpy as np

def calc_distance_3D(a, b):
    return np.sqrt(np.power(b[0]-a[0],2) + np.power(b[1]-a[1],2) + np.power(b[2]-a[2],2))

atomA, atomsB = (0,0,0), (1,1,1)
dist = calc_distance_3D(atomA, atomB)

print("La distance entre les deux atomes vaut {:.2f}".format(dist))
