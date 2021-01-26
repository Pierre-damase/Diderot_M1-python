import numpy as np

def trouve_calpha(file):
    calpha = []
    with open(file, "r") as filin:
        lines = filin.readlines()
        for line in lines:
            if line.startswith("ATOM"):
                if "CA" in line[12:16]:
                    calpha.append(line)
    print("Res 1 : {}\nRes 2 : {}".format(calpha[0], calpha[1]))
    return calpha

def calcule_distance(calpha):
    dist = []
    for index in range(len(calpha)-1):
        xA, xB = float(calpha[index][30:38].strip()), float(calpha[index+1][30:38].strip())
        yA, yB = float(calpha[index][38:46].strip()), float(calpha[index+1][38:46].strip())
        zA, zB = float(calpha[index][46:54].strip()), float(calpha[index+1][46:54].strip())

        dist.append(np.sqrt(np.power(xB-xA,2) + np.power(yB-yA,2) + np.power(zB-zA,2)))
    for i in range(4):
        print("{} {} : {:.2f}".format(i+1, i+2,dist[i]))
    return dist

file1 = "1bta.pdb"
calpha = trouve_calpha(file1)
dist = calcule_distance(calpha)
print("La dist moyenne de {} est {:.5f}".format(file1, np.mean(dist)))
