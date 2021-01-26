# VIII.
import sys
import random as rand

if len(sys.argv) != 2:
    sys.exit("Veuillez renseigner un argument!")


try:
    int(sys.argv[1])
except ValueError:
    sys.exit("Veuillez renseigner un int!")


seq = []
for i in range(1,int(sys.argv[1]) + 1):
    seq += [rand.choice(["A","G","T","C"])]
print(seq)
