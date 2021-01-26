# Chapitre 4 Listes
jour = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
jour[:5] # 0 inclus à 5 exlu

print("Jour de la semaine : {} \nJour du week-end : {}".format(jour[:5], jour[5:]))
print("Jour de la semaine : {} \nJour du week-end : {}".format(jour[4::-1], jour[6:4:-1]))
print("Dernier jour :  {} {} {}".format(jour[6:], jour[6:5:-1], jour[6::-7]))

jour_inverse = jour[6::-1]
print("Jour inverse : {}".format(jour_inverse))


hiver = ["decembre", "janvier", "fevrier"]
ete = ["juin", "juillet", "aout"]
automne = ["septembre", "octobre", "novembre"]
printemps = ["mars", "avril", "mai"]
saisons = [hiver, printemps, ete, automne]

#                                            mars                         accède à tous les éléments de la liste d'indice n
print("{} \n{} \n{} \n{}".format(saisons[2], saisons[1][0], saisons[1:2], saisons[:][0]))
#                                contenu ete                contenu printemps

table_9 = list(range(0,91,9))
print("Table de 9 {} ".format(table_9))

print("Il y a {} nombre paire dans l'intervalle [2,10000] inclus".format(len(list(range(2,10001,2)))))
