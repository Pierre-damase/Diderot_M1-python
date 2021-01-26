import random as rand
import numpy as np

dico_freq = {"A" : 0.1, "T" : 0.3, "G" : 0.5, "C" : 0.1}

def seq_rand(taille):
    seq = []
    for i in range(taille):
        seq.append(rand.choice(["A", "G", "T", "C"]))
    return seq

def seq_rand_2(taille, dico_freq):
    new_seq = []
    pb = list(dico_freq.values())
    bases = list(dico_freq.keys())
    choix = list(np.random.choice(len(pb), taille, pb))

    for i in choix:
        new_seq.append(bases[i])
    return new_seq

adn = seq_rand(15)
print(adn)

adn2 = seq_rand_2(50, dico_freq)
print(adn2)
