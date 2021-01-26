seq = "ATATACGGATCGGCTGTTGCCTGCGTAGTAGCGT"

def calc_composition(seq):
    freq = {"A" : seq.count("A"),\
            "G" : seq.count("G"),\
            "T" : seq.count("T"),\
            "C" : seq.count("C")}
    print(freq)

calc_composition(seq)
