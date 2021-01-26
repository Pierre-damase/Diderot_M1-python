l = [5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2]

def doublons(l):
    new_l = []
    while l != []:
        ele = l[0]
        nb_occurrences = l.count(ele)
        for i in range(nb_occurrences):
            l.remove(ele)
        new_l.append(ele)
    new_l.sort()
    return new_l

new_l = doublons(l)
print(new_l)
