import sys

seq_aa = "ALA GLY ARG TRP TYR SER GLY ALA TRP"

dico_aa = {
    "ASP" : 'D', "GLU" : 'E', "HIS" : 'H', "ARG" : 'R', "TYR" : 'Y',
    "CYS" : 'C', "LYS" : 'K', "ALA" : 'A', "VAL" : 'V', "ILE" : 'I',
    "LEU" : 'L', "MET" : 'M', "PHE" : 'F', "TRP" : 'W', "ASN" : 'A',
    "GLN" : 'Q', "SER" : 'S', "THR" : 'T', "PRO" : 'P', "GLY" : 'G'
}

def convert_3_lettres_1_lettre(seq_3_lettres, dico_aa):
    seq_1_lettre = []

    for aa in seq_3_lettres.split(" "):
        if len(aa) != 3:
            sys.exit("Veuillez renseigner une seq proteique code 3 lettre")
        seq_1_lettre.append(dico_aa[aa])
    return seq_1_lettre


seq_1_lettre = convert_3_lettres_1_lettre(seq_aa, dico_aa)
print(" ".join(seq_1_lettre))
