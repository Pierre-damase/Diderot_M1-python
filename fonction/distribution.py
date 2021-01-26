import random as rand
import sys


def nb_argument():
    if len(sys.argv) != 4:
        sys.exit("Veuillez renseigner 3 arguments : n, debut et fin")
    try:
        n_floats, debut, fin = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    except:
        sys.exit("Veuillez renseigner 3 integer!")
    return n_floats, debut, fin


def traitement():
    n_floats, debut, fin = nb_argument()
    for i in range(20):
        list_float = []
        for j in range(n_floats):
            list_float.append(rand.uniform(debut,fin))
        print("Liste {} : min = {:.2f}, max = {:.2f}, moyenne = {:.2f}"\
              .format(i+1,\
                      min(list_float),\
                      max(list_float),\
                      sum(list_float)/len(list_float)))


traitement()
