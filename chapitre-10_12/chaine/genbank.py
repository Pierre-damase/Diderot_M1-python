# from Bio import SeqIO

def lit_genbank(file):
    # with open(file, "r") as filin:
    #     record = SeqIO.read(filin, "genbank")
    #     record.seq => obtenir la seq directement

    flag, seq = False, ""
    with open(file, "r") as filin:
        lines = filin.readlines()
        for line in lines:
            if "//" in line:
                flag = False
            if flag == True:
                line = "".join(line.strip().split(" ")[1:])
                seq += line

            if "ORIGIN" in line:
                flag = True
    return seq

file1 = "NC_001133.gbk"
seq = lit_genbank(file1)

print('''{}
La seq contient {} bases
Les 10 premieres bases : {}
les 10 dernieres bases : {}
'''.format(file1, len(seq), seq[0:10], seq[len(seq)-10:]))
