def est_premier(nb):
    suite = list(range(2,nb))
    for nombre in suite:
        if nb % nombre == 0:
            return False
    return True

for nombre in range(2,101):
    if est_premier(nombre):
        print("{} est premier".format(nombre))
    else:
        print("{} n'est pas premier".format(nombre))
