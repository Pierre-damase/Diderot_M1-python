mots = {"coucou" : 'uocuoceokzezh', "python" : 'aeiouyhpq', "fonction" : 'nhwfnitvkloco', "zzzz" : 'uocucekzezh', "coucouu" : 'ccuuceokzezh'}


def test_composable(mots):
    print(mots)
    for mot, seq in mots.items():
        list_tmp, tmp = [], 0
        for lettre in seq:
            list_tmp.append(lettre)
        for lettre in mot:
            if lettre not in list_tmp:
                tmp += 1
            else:
                if seq.count(lettre) < mot.count(lettre):
                    tmp += 1
        if tmp != 0:
            print("{} est non composable a partir de {}".format(mot,seq))
        else:
            print("{} est composable a partir de {}".format(mot,seq))

test_composable(mots)
