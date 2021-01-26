import numpy as np
import os
import time
import random as rand

# I.
for nb in range(10,21):
    print("{} {:.3f}".format(nb, np.sqrt(nb)))


# II.
print(np.cos((np.pi / 2)))


# III.
print("Vous êtes dans le répertoire {} et il contient {} élément.s".format(os.getcwd(), len(os.listdir()) ))


# IV.
for nb in range(1,11):
    print(nb)
    time.sleep(0.1) # 0.1 s


# V.
seq = []
for i in range(1,7):
    seq += [rand.randint(1,4)]
print(seq)


# VI.
seq = []
for i in range(1,21):
    seq += [rand.choice(["A","G","T","C"])]
print(seq)

seq = []
while(len(seq) < 20):
    seq += [rand.choice(["A","G","T","C"])]
print(seq)
