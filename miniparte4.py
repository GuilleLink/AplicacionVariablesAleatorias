#Universidad del Valle de Guatemala
#Juan Guillermo Sandoval LAcayo - 17577
#Hector Javier Carpio Garcia - 17077
#Modelacion y Simulacion
#
#Miniproyecto2

#Problema4
#Imports
import numpy
import random
import matplotlib.pyplot as plt

#Variables
it = 30
prob9, prob10, prob11 = 0.3, 0.4, 0.3
gananciaTotal9, gananciaTotal10, gananciaTotal11 = 0,0,0
y9, y10, y11 = [], [], []
x = []

for j in range (0,it):
    probDiaria = random.random()
    #Solo vendo 9 periodicos
    if (probDiaria<=prob9):
        gananciaTotal9 += 9
        gananciaTotal10 += 8
        gananciaTotal11 += 7
    #Solo vendo 10 periodicos
    elif(probDiaria>prob9 and probDiaria<=(prob9+prob10)):
        gananciaTotal9 += 9
        gananciaTotal10 += 10
        gananciaTotal11 += 9
    #Solo vendo 11 periodicos
    elif(probDiaria>(prob9+prob10)):
        gananciaTotal9 += 9
        gananciaTotal10 += 10
        gananciaTotal11 += 11
    
    x.append(j)
    y9.append(gananciaTotal9)
    y10.append(gananciaTotal10)
    y11.append(gananciaTotal11)

plt.scatter(x, y9, s=0.3, edgecolor = 'blue')
plt.scatter(x, y10, s=0.3, edgecolor = 'green')
plt.scatter(x, y11, s=0.3, edgecolor = 'yellow')
plt.plot(x, y9, 'b')
plt.plot(x, y10, 'g')
plt.plot(x, y11, 'y')
plt.show()