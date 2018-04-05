from random import random, randint
from grafo import Grafo
n = 5 # nodos
G1 = Grafo()
G2 = Grafo()
i = 1 # etiqueta nodo

for nodo in range(n):
    x = random()
    y = random()
    r = 2  
    G1.nodo(i,x,y,r)
    i += 1

G1.arista(1, 2, True, 4)
G1.arista(1, 3, True, 8)

G1.arista(2, 1, True, 4)
G1.arista(2, 3, True, 1)
G1.arista(2, 4, True, 2)

G1.arista(3, 1, True, 8)
G1.arista(3, 4, True, 4)
G1.arista(3, 5, True, 2)

G1.arista(4, 2, True, 2)
G1.arista(4, 3, True, 4)
G1.arista(4, 5, True, 7)

G1.arista(5, 3, True, 2)
G1.arista(5, 4, True, 7)

d = G1.floyd_warshall()
print(d)

G1.grafica()


