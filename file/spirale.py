import math
import matplotlib.pyplot as plt

teta = 0
rayon = 0.5

filout = open("spirale.dat", "w")

while(abs(teta) < 4*math.pi):
    xA = math.cos(teta) * rayon
    yA = math.sin(teta) * rayon
    filout.write("{:.5f} {:.5f}\n".format(xA, yA))
    teta += 0.1
    rayon += float(0.1)

filout.close()

x = []
y = []
with open("spirale.dat", "r") as filin:
    for line in filin:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))

plt.figure(figsize=(8,8))
mini = min(x + y) * 1.2
maxi = max(x + y) * 1.2
plt.xlim(mini, maxi)
plt.ylim(mini, maxi)
plt.plot(x,y)
plt.savefig("spirale.png")
