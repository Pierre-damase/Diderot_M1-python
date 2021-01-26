## I. ##
jour = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

for index, n in enumerate(jour):
    print("{}".format(n), end = " ")
    if index <= 3:
        print("Get back to work feignasse!")
    elif index == 4:
        print("Party time!")
    else:
        print("Auchan time!")



## II. ##
import random

sequence = []
for index in range(10):
    sequence += [random.choice(["A", "G", "C", "T"])]

print(sequence)
for index, n in enumerate(sequence):
    if n == "A":
        sequence[index] = "T"
    elif n == "T":
        sequence[index] = "A"
    elif n == "C":
        sequence[index] = "G"
    else:
        sequence[index] = "C"
print("{}".format(sequence))



## III. ##
liste = [6, 4, 2, 1, 5, 0]

for index, n in enumerate(liste):
    if index == 0:
        min = liste[index]
    else:
        if n < min:
            min = n
print("Le minimum de la liste est {}".format(min))



## IV. ##
aa = []
for index in range(100): # de 0 à 9 par défaut
    aa += [random.choice(["A", "R", "W", "G"])]

nb_A = nb_R = nb_W = nb_G = 0
for index, n in enumerate(aa):
    if n == "A":
        nb_A += 1
    elif n == "R":
        nb_R += 1
    elif n == "W":
        nb_W += 1
    else:
        nb_G += 1

print("Il y a {:.2f}% d'alanine (A)".format((nb_A/len(aa))*100), end="")
print(", {:.2f}% d'arginine (R)".format((nb_R/len(aa))*100), end="")
print(", {:.2f}% de tryptophane (W)".format((nb_W/len(aa))*100), end="")
print(" et {:.2f}% de glycine (G)".format((nb_G/len(aa))*100))



## V. ##
notes = [14, 9, 13, 15, 12]
moyenne = 0
for index, n in enumerate(notes):
    moyenne += n
moyenne = moyenne / len(notes)

del min

print("La note max est {}".format(max(notes)), end="")
print(", la note min est {}".format(min(notes)), end="")
print(" et la moyenne est {:.2f}".format(moyenne))
if moyenne < 10:
    print("L'étudiant n'a pas de mention!")
elif moyenne >= 10 and moyenne < 12:
    print("L'étudiant a la mention passable!")
elif moyenne >= 12 and moyenne < 14:
    print("L'étudiant a la mention assez bien!")
else:
    print("L'étudiant a la mention bien!")



## VI. ##
nombre = list(range(21)) # liste de 0 inclus à 21 exlu par pas de 1

for index, n in enumerate(nombre):
    if n <= 10 and n % 2 == 0:
        print("{}".format(n))
    elif n > 10 and n % 2 != 0:
        print("{}".format(n))



## VII. ##
nombre = 10

for index in range(20):
    print("{}".format(nombre), end=" ")
    if nombre % 2 == 0:
        nombre = int(nombre / 2)
    else:
        nombre = (nombre * 3) + 1

# Pour n = 10 ou 20 => 1 4 2
nombre = 10
nb_tour = 0

print("Pour le nombre {}".format(nombre), end=" ")
while True:
    if nombre % 2 == 0:
        nombre = int(nombre / 2)
    else:
        nombre = (nombre * 3) + 1
    nb_tour += 1
    print("{}".format(nombre))
    if nombre == 1: break;

print("il y a {} opérations avant d'atteindre 1".format(nb_tour))



## VIII. ##
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
# hélice alpha principallement pour ITFE



## IX. ##
n1 = 0
n2 = 101
suite = list(range(n1,n2))
liste_premier = []

for nombre in suite:
    if nombre == 0 or nombre == 1: continue
    premier = True
    for i in range(1, nombre+1):
        if nombre % i == 0:
            if i != 1 and i != nombre:
                premier = False
                break
            else:
                continue
    if premier:
        liste_premier.append(nombre) # liste_premier += [nombre]

print("Les nombres premier de {} à {} sont : {}".format(n1,n2-1,liste_premier))


n1 , n2 = 2 , 101
suite = list(range(n1,n2)) # 0 et 1 non premier => commencer à 2
liste_premier = []

for nombre in suite:
    premier = True
    for i in range(2, nombre): # de 2 à nombre - 1
        if nombre % i == 0:
            premier = False
    if premier:
        liste_premier.append(nombre)

print("Les nombres premier de {} à {} sont : {}".format(n1,n2-1,liste_premier))


# METHODE 2
n1 , n2 = 3 , 101
suite = list(range(n1,n2)) # 0 et 1 non premier
liste_premier = [2]
for nombre in suite:
    premier = True
    for nb_premier in liste_premier:
        if nombre % nb_premier == 0:
            premier = False
            break
    if premier:
        liste_premier += [nombre]

print("Les nombres premier de {} à {} sont : {}".format(n1-3,n2-1,liste_premier))



## X. ##
nb_question = 0
print("Pensez à un nombre entre 1 et 100 inclus")

nombre = 50
max = 101
min = 0
while min < max-1 or max > min + 1:
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
