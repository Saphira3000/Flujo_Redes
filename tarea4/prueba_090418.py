# 09 Marzo 2018
# Crea grafo circular de n nodos, cada nodo se conecta con
# los k siguientes y anteriores. Ademas se incluyen aristas
# con probabilidad prob

from grafo import Grafo
from random import random
import math

n = 20 # nodos
k = 2
i = 0 
G = Grafo()
ang = math.radians(360/n) # angulo en radianes de separacion entre nodos
r1 = 0.5
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

prob = 0.1 # probabilidad aristas aleatorias
for v in G.V:
    for w in G.V:
        if random() < prob:
            if (v, w, False, p) not in G.E and v != w:
                G.arista(v, w, False, p)

#print(G.E)
#print(G.clust_coef())
G.grafica('ejem.eps')


