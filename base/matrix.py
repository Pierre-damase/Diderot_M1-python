## XI. ##
import numpy as np

matrice = np.ones((2,2))

# print("ligne colonne")
# for index, nombre in enumerate(matrice):
#     for i, nb in enumerate(nombre):
#         print("{:{align}{width}d} {:{align}{width}}".format(index+1, i+1, align=">", width=4))

# Enumerate => long à executer | favoriser range


print("ligne colonne")
for index in range(len(matrice)):
    for i in range(len(matrice[index])):
        print("{:{align}{width}d} {:{align}{width}}".format(index+1, i+1, align=">", width=4))



print("ligne colonne")
index = 0
while index < len(matrice):
    i = 0
    while i < len(matrice[index]):
        print("{:{align}{width}} {:{align}{width}}".format(index+1, i+1, align=">", width=4))
        i += 1
    index += 1



## XII. ##
matrice = np.ones((4,4))

# nb_case_parcourues = 0
# for index,nombre in enumerate(matrice[:len(matrice)-1]):
#     for i in range(index+1,len(matrice)):
#         print("{} {}".format(index+1, i+1));
#         nb_case_parcourues += 1

# print("Matrice de taille N = {} et nb case parcourues est {}".format(i+1, nb_case_parcourues))

# Enumerate => long à executer | favoriser range

nb_case_parcourues = 0
print("ligne colonne")
for index in range(len(matrice[:len(matrice)-1])):
    for i in range(index+1,len(matrice)):
       print("{} {}".format(index+1, i+1));
       nb_case_parcourues += 1

print("Matrice de taille N = {} et nb case parcourues est {}".format(i+1, nb_case_parcourues))

## XIII. ##
import random

nombre = 0
nb_saut = 0

while nombre != 5:
    nb_saut += 1
    if(random.choice([-1,1]) == -1 and nombre != -1):
        nombre += -1
    else:
        nombre += 1

print("Nb saut puce : {}".format(nb_saut))



## XIV. ##
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
print("La suite vaut {}".format(suite))
