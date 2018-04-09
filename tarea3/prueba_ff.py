from random import random, randint
from grafo import Grafo

n = 6 # nodos 
G = Grafo()
r = 0.025  
G.nodo(0,0.1,0.5,r)
G.nodo(1,0.3,0.8,r)
G.nodo(2,0.6,0.8,r)
G.nodo(3,0.3,0.2,r)
G.nodo(4,0.6,0.2,r)
G.nodo(5,0.9,0.5,r)

G.arista(0, 1, True, 10)
G.arista(0, 3, True, 10)

G.arista(1, 2, True, 4)
G.arista(1, 3, True, 2)
G.arista(1, 4, True, 8)

G.arista(2, 5, True, 10)

G.arista(3, 4, True, 9)

G.arista(4, 2, True, 6)
G.arista(4, 5, True, 10)

G.grafica("ejem_grafo2.eps")
d = G.ford_fulkerson(0,5)
print(d)


