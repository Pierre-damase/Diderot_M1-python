seq = "TCTGTTAACCATCCACTTCG"
dico_complementaire = {"A" : 'T', "T" : 'A', "C" : 'G', "G" : 'C'}

def comp_inv(seq, dico):
    new_seq = []
    for i in range(len(seq)):
        new_seq.append(dico[seq[i]])
    new_seq.reverse()
    return new_seq

adn = comp_inv(seq, dico_complementaire)
print(adn)
