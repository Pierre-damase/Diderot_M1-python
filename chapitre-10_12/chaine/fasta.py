import sys
import os


def argument():
    if len(sys.argv) != 2:
        sys.exit("Veuillez renseigner 1 argument : le fichier fasta a lire")
    if sys.argv[1] not in os.listdir():
        sys.exit("Le fichier renseigner n'existe pas")
    return sys.argv[1]

def lire_fasta(file_fasta):
    with open(file_fasta, "r") as filin:
        fasta = filin.read()
    l = fasta.strip().split("\n")
    seq = fasta.split("sequence")[1].strip()

    print('''
La sequence contient {} bases
La sequence possede  {} codons
Les dix 1ere bases sont {}
Les dix derniere sont {}
    '''.format(len(seq), len(seq)/3, seq[0:10], seq[-10:]))

    if len(seq) % 3 == 0:
        print("La longueur de la seq est un multiple de 3 nucleotides")
    else:
        print("La longueur de la seq n'est pas un multiple de 3 nucleotides")

lire_fasta(argument())
