def pascale(nb):
    new_nb = []
    for index in range(len(nb)):
        if not new_nb:
            new_nb.append(1)
        else:
            tmp = nb[index-1] + nb[index]
            new_nb.append(tmp)
    new_nb.append(1)
    return(new_nb)

def aff_list(l):
    for nombre in l:
        print("{:^3d}".format(nombre), end=" ")
    print("\n")

def traitement():
    nb = [1]
    aff_list(nb)
    for i in range(10):
        nb = pascale(nb)
        aff_list(nb)


traitement()
