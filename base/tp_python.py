## Exo 5.4.12

ligne = 4
colonne = 4

nb_case_parcourues = 0
print("ligne colonne")
for index in range(ligne-1):
    for i in range(index+1,colonne):
       print("{} {}".format(index+1, i+1));
       nb_case_parcourues += 1

print("Matrice de taille N = {} et nb case parcourues est {}".format(i+1, nb_case_parcourues))


## Exo 5.4.14
x_zero = 0
x_un = 1
suite = 0

for index in range(0,10):
    if index == 0:
        suite = x_zero # 0
    elif index == 1:
        suite = x_un # 1
    else:
        suite = x_zero + x_un # x(n-2) + x(n-1)
        x_zero = x_un # x(n-1)
        x_un = suite # x
    print("{}".format(suite), end =" ")

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


## Exo 5.4.14 avec la question du rapport
x_zero = 0
x_un = 1
suite = 0


for index in range(0,15):
    if index == 0:
        suite = x_zero # 0
    elif index == 1:
        suite = x_un # 1
    else:
        suite = x_zero + x_un # x(n-2) + x(n-1)
        x_zero = x_un # x(n-1)
        x_un = suite # x
        print("{}".format(suite/x_zero), end=" ") # tend vers 1.6666666


## Exo 6.7.7
nombre = 10

for index in range(20):
    print("{}".format(nombre), end=" ")
    if nombre % 2 == 0:
        nombre = int(nombre / 2)
    else:
        nombre = (nombre * 3) + 1


# Le motif qui se répette est 4 2 1


## Exo 6.7.8
ITFE = [[48.6, 53.4], [-124.9, 156.7], [-66.2, -30.8], [-58.8, -43.1], \
         [-73.9, -40.6], [-53.7, -37.5], [-80.6, -26.0], [-68.5, 135.0], \
         [-64.9, -23.5], [-66.9, -45.5], [-69.6, -41.0], [-62.7, -37.5], \
         [-68.2, -38.3], [-61.2, -49.1], [-59.7, -41.1]]
phi = -57
psi = -47

for index, angles in enumerate(ITFE):
    if phi - 30 <= angles[0] <= phi + 30 and \
       psi - 30 <= angles[1] <= psi +30:
        print("{} est en hélice".format(angles))
    else:
        print("{} n'est pas en hélice".format(angles))



## Exo 6.7.9
n1 = 0
n2 = 101
suite = list(range(n1,n2))
liste_premier = []

for index, nombre in enumerate(suite):
    if nombre == 0 or nombre == 1:
        continue
    premier = True
    for i in range(1, nombre+1): # Calcul du reste de la division entière du nombre jusqu'à lui-même
        if nombre % i == 0:
            if i != 1 and i != nombre:
                premier = False
                break
            else:
                continue
    if premier:
        liste_premier += [nombre]

print("Les nombres premier de {} à {} sont : {}".format(n1,n2-1,liste_premier))



## Version 2 améliorée

liste_premier = [2]
for index, nombre in enumerate(suite):
    if nombre == 0 or nombre == 1:
        continue
    premier = True
    for i, prem in enumerate(liste_premier):
        if nombre % prem == 0:
            premier = False
            break
        else:
            continue
    if premier:
        liste_premier += [nombre]

print("Les nombres premier de {} à {} sont : {}".format(n1,n2-1,liste_premier))



## Exo 6.7.10

nb_question = 0
print("Pensez à un nombre entre 1 et 100 inclus")

nombre = 50
max = 101
min = 0
while min < max-1 or max > min + 1: # condition d'arrêt
    print("Est-ce que votre nombre est plus grand, plus petit ou égal à {} ? [+/-/=]".format(nombre))
    lettre = input("Entrez une lettre : ")
    nb_question += 1
    if lettre == "=":
        print("J'ai trouvé en {} question(s)".format(nb_question))
        break
    elif lettre == "+":
        min = nombre
        nombre = int(nombre + (max-nombre)/2)
    else:
        max = nombre
        nombre = int(nombre + (min-nombre)/2)


