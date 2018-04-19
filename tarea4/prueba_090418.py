# 09 Marzo 2018
# Crea grafo circular de n nodos, cada nodo se conecta con
# los k siguientes y anteriores

from grafo import Grafo
from random import random
import math

n = 8 # nodos
k = 2
i = 0 
G = Grafo()
ang = math.radians(360/n) # angulo en radianes de separacion entre nodos
r1 = 0.45
xc = 0.5
yc = 0.5

for i in range(n):
    x = r1*math.cos(i*ang) + xc
    y = r1*math.sin(i*ang) + yc
    r = 0.02  
    G.nodo(i,x,y,r)
    i += 1

p = 0
for nodo in G.V:
    for j in range(k):
        if (nodo + j + 1) >= n:
            a = (nodo + j + 1) - n
        else:
            a = (nodo + j + 1)
        G.arista(nodo, a, False, p)

prob = 0.2
for v in G.V:
    for w in G.V:
        if random() < prob:
            if (v, w, False, 1) not in G.E:
                G.arista(v, w, False, p)


print(G.E)
# falta conectar aristas con cierta probabilidad
print(G.clust_coef())
G.grafica('ejem.eps')


