def gen_pyramide(nb):
    for index in range(1,nb*2,2):
        print("{:{align}{width}s}".format("*" * index, align="^", width=nb*2))


while(True):
    reponse = input("Entrez un nb de lignes (entier positif): ")
    try:
        nombre = int(reponse)
        break
    except ValueError: 
        print("Veuillez renseigner un int !!")
print("",end="\n\n")
gen_pyramide(nombre)
