def dist_hamming(seq1, seq2):
    tmp = 0
    for index in range(len(seq1)):
        if seq1[index] != seq2[index]:
            tmp += 1
    return tmp

seq1 = "AGWPSGGASAGLAIL"
seq2 = "IGWPSAGASAGLWIL"
print("Dist entre {} et {} vaut\n{}".format(seq1, seq2, dist_hamming(seq1,seq2)))


seq1 = "ATTCATACGGTTACGATT"
seq2 = "ATACTTACGTAACCAATT"
print("Dist entre {} et {} vaut\n{}".format(seq1, seq2, dist_hamming(seq1,seq2)))
