from random import random, randint
from grafo import Grafo

nom = ['a','b','c','d','e','f','g']

n = 3 # nodos 
i = 0 
G = Grafo()
for nodo in range(n):
    x = random()
    y = random()
    r = 0.025  
    G.nodo(nom[i],x,y,r)
    i += 1

G.arista('a', 'b', True, randint(1,5))
G.arista('a', 'c', True, randint(1,5))

G.arista('b', 'a', True, randint(1,5))
G.arista('b', 'c', True, randint(1,5))

G.arista('c', 'a', True, randint(1,5))
G.arista('c', 'b', True, randint(1,5))

G.grafica('ejem_grafo1.eps')
print(G.E)
d = G.floyd_warshall()
print(d)


