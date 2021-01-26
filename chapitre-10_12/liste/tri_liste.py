l = [8, 3, 12.5, 45, 25.5, 52, 1]

def tri_liste(l):
    new_l = []
    for i in range(len(l)):
        new_l.append(min(l))
        l.remove(min(l))
    return new_l

print(tri_liste(l))
