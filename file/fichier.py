## I. ##
with open("notes.txt", "r") as filin:
    notes = filin.readlines()

moyenne = 0.0
for index in range(len(notes)):
    moyenne = moyenne + float(notes[index])

moyenne /= len(notes)

print("Moyenne {:.2f}".format(moyenne))


## II. ##
with open("notes2.txt", "w") as filout:
    for note in notes:
        if abs(float(note)) >= 10.000000001 :
            filout.write("{} admis\n".format(float(note)))
        else:
            filout.write("{} recalé\n".format(float(note)))
