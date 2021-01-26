import random as rand

def seq_comp(seq):
    sequence = []
    for index, base in enumerate(seq):
        if base == 'A':
            sequence.append('T')
        elif base == 'G':
            sequence.append('C')
        elif base == 'T':
            sequence.append('A')
        else:
            sequence.append('G')
    return sequence


sequence = []
for index in range(25):
    sequence += [rand.choice(["A", "G", "C", "T"])]

seqC = seq_comp(sequence)

print("{}".format(sequence))
print("{}".format(seqC))

