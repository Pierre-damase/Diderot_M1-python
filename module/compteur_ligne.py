# VIII.
import sys
import os

if len(sys.argv) != 2:
    sys.exit("Veuillez renseigner un argument!")

if os.path.exists(sys.argv[1]):
    nb_lignes = 0
    with open(sys.argv[1], "r") as filin:
        nb_lignes = len(filin.readlines())
        print("{} contient {} lignes!".format(sys.argv[1], nb_lignes))
else:
    sys.exit("{} n'existe pas dans le répertoire courant!".format(sys.argv[1]))
