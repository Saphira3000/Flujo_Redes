from random import random, randint
from grafo import Grafo
n = 5 # nodos
G = Grafo()

for nodo in range(n):
    x = random()
    y = random()
    G.nodo(x,y)

for v in G.V:
    for w in G.V:
        if random() < 0.5:
            G.arista(v, w)

print(G.V)
print(G.E)
G.grafica()
    
