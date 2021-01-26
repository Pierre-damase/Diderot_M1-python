def nb_mystere(nb):
    if len(str(nb)) != 3: return None
    if nb > 300: return None
    if nb % 2 != 0: return None
    if str(nb).count(str(nb)[0]) != 2 and str(nb).count(str(nb)[1]) != 2 : return None
    tmp_nb = map(int, str(nb))
    if sum(list(tmp_nb)) != 7: return None
    else: return 1


def traitement(nb):
    if nb_mystere(nb) != None:
        print("{} est le nombre mystere".format(nb))

for i in range(300):
    traitement(i)
