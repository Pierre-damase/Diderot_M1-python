# Chapitre 5 Boucles et comparaisons
## I. ##
animals = ["vache", "souris", "levure", "bacterie"]
for index in animals:
    print(index, end=" ")
print("\n")
for index in range(len(animals)):
    print("{}".format(animals[index]), end=" ")

i = 0
print("\n")
while i != len(animals):
    print("{}".format(animals[i]), end=" ")
    i += 1
    if(i==len(animals)):print("\n")


## II. ##
jour = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for index in jour[0:5]:
    print(index)
i=0
while i != len(jour):
    if(i >= 5):print("{}".format(jour[i]))
    i+=1

# Ternary operator in python => 1 if true else 0
print("T") if jour[0]=="lundi" else print("F")


## III. ##
for index in range(1,11): # 1 inclus, 11 exlu
    print("{}".format(index), end=" ")
    if index==10: print("")


## IV. ##
impair = list(range(1,22,2))
pair = list()
print(impair)
#for index in range(len(impair)):
#    pair.append(impair[index]+1)
#print(pair)


for index, nombre in enumerate(impair):
    pair.append(nombre+1)
print(pair)


## V. ##
notes = [14, 9, 6, 8, 12]
moyenne = 0

#for index in range(len(notes)):
#    moyenne += notes[index]
#moyenne = moyenne/len(notes)
#print("Moyenne : {:.2f}".format(moyenne))


for index, note in enumerate(notes):
    moyenne += note
moyenne = moyenne/(index+1)
print("Moyenne : {:.2f}".format(moyenne))


## VI. ##
pair = list(range(2,21,2))
for index in range(len(pair)):
    if index < len(pair)-1:
        print("{:>2} * {:>2} = {:>3}".format(pair[index], pair[index+1], pair[index]*pair[index+1]))

for index, nombre in enumerate(pair):
    if index < len(pair)-1:
        print("{:>2} * {:>2} = {:>3}".format(nombre, pair[index+1], nombre*pair[index+1]))


## VII. ##
for index in range(11): # 0 inclus à 11 exclu avec pas de 1
    print("{}".format("*" * index))


## VIII. ##
print("")
for index in range(10,0,-1): # 10 inclus à 0 exclu avec pas de -1
    print("{}".format("*" * index))


## IX. ##
for index in range(11):
    print("{:>10}".format("*" * index))


## X. ##
for index in range(1,20,2):
    print("{:^20}".format("*" * index))


reponse = input("Entrez un nb de lignes (entier positif): ")
nb = int(reponse)
for index in range(1,nb*2,2):
    print("{:{align}{width}s}".format("*" * index, align="^", width=nb*2))



## QCM ##
legumes = ['Carotte', 'Betterave', 'Tomate', 'Poivron', 'Radis']

for index in legumes[0:]: # de l'index 0 jsuqu'à la fin
    print(index)

for index in legumes[0:-1]: # de l'index 0 jusqu'a la fin -1
    print(index)

for legume in legumes:
    if legume == 1:
        print(index) # jamais afficher car index stocke l'élément et non l'indice

print(legumes[-1]) # radis
print(legumes[-6]) # error out of range

i = 5
i*2 # = 10 means 5 times 2
i**2 # = 25 means 5 squared 2
