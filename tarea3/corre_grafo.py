from random import random, randint
from grafo import Grafo
n = 5 # nodos
G = Grafo()
i = 1 # etiqueta nodo
d = {}
p = {}

for nodo in range(n):
    x = random()
    y = random()
    r = 2  
    G.nodo(i,x,y,r)
    i += 1

for v in G.V:
    for w in G.V:
        if random() < 0.5:
            pond = randint(1,5)
            G.arista(v, w, False, pond)

#d = G.floyd_warshall()
#print(d)
#print(p)

#print(G.V)
print(G.E)
a = G.ford_fulkerson(1, 5)
print(a)

	#nodo = G.V[i]
	#r = randint(i + 1, n - 1)
	#G.arista(nodo, r, False, pond)
