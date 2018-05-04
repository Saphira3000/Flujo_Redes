# Crea grafo rejilla

from grafo2 import Grafo
from random import random, randint, sample, choice
import math

k = 3
n = k*k
G = Grafo()
G.rejilla(k)
l = 2

# capacidades aristas simetricas
mu = 0
sigma = 0.02

# ----- Aristas simetricas (distancia manhattan) -----
for v in G.V:
    for w in G.V:
        #if G.arista(v,w,False,0) not in G.E and v != w:
        d = G.man(v,w)
        if d <= l and (v, w) not in G.E and v != w:
            G.arista(v,w,False,0)

# ----- Aristas aleatorias (prob p) -----
prob = 0.02
for v in G.V:
    for w in G.V:
        if random() < prob and (v,w) not in G.E:
            G.arista(v,w,True,0)

G.grafica("rejilla", "nodos.dat", k)

#flujo = G.ford_fulkerson(n-1, k-1)
#print(flujo)

# incluir en el reporte que, en el caso en que la arista ya este incluida, no se considera

# s = n-1 nodo
# t = k-1 nodo

quien = sample(G.V.keys(), 1)
#c = choice(G.E.keys())
for i in range(1,3):
    cual = sample(G.E.keys(), 1)
    print(cual)
    G.per_aris(cual)

print(quien)
G.per_nodo(quien)
G.grafica("rejilla_per", "nodos2.dat", k)
