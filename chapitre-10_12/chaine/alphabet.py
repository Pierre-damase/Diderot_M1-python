def get_alphabet():
    alphabet = ""
    for i in range(97,123):
        alphabet += chr(i)
    return alphabet

def pangramme(chaine):
    chaine_original = chaine
    chaine = chaine.lower() # Code ASCII different entre a et A, b et B, etc.
    alphabet = get_alphabet()

    for lettre in alphabet:
        if chaine.count(lettre) == 0:
            print("\"{}\" n est pas un pangramme".format(chaine_original))
            return None
    print("\"{}\" est un pangramme".format(chaine_original))

pangramme("Portez ce vieux whisky au juge blond qui fume")
pangramme("Monsieur Jack vous dactylographiez bien mieux que votre ami Wolf")
pangramme("Buvez de ce whisky que le patron juge fameux")
pangramme("Je suis donc je pense")
pangramme("Que brule la galaxie")
pangramme("Du sang pour le Dieu du sang! Des cranes pour le trone de cranes!")
pangramme("J'ai du sang de pauvre sur les mains! AHHHHHHHHHHHHHHHH!")
