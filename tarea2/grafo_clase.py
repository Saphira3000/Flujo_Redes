from random import random, randint
from grafo import Grafo
n = 15 # nodos
G = Grafo()
i = 1 # etiqueta nodo

for nodo in range(n):
    x = random()
    y = random()
    r = 2 #randint(2,7) 
    G.nodo(i,x,y,r)
    i += 1

for v in G.V:
    for w in G.V:
        if random() < 0.1:
            if random() < 0.4:
                G.arista(v, w, True, randint(1,7)/2.0)
            else:
                G.arista(v, w, False, randint(0,2))

G.grafica()

