# 23 abril 2018
# Crear grafo rejilla

from grafo import Grafo
from random import random
import math
import scipy.stats as ss

k = 5
n = k*k
G = Grafo()
G.rejilla(k)
l = 1

# capacidades aristas simetricas
#mu = 0
#sigma = 0.02
#normal = ss.norm(mu,sigma)
#print(normal)

# capacidades aristas dirigidas
# lambda = 2
#normal = ss.norm(mu,sigma)
#print(normal)

for v in G.V:
    for w in G.V:
        d = G.man(v,w)
        if d <= l:
            G.arista(v,w,False,0)

prob = 0.002
for v in G.V:
    for w in G.V:
        if random() < prob:
            G.arista(v,w,False,0)

G.grafica("rejilla.eps", k)

flujo = G.ford_fulkerson(n-1, k-1)
print(flujo)

# incluir en el reporte que, en el caso en que la arista ya este incluida, no se considera

# s = n-1 nodo
# t = k-1 nodo
