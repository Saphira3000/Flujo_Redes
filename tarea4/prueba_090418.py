# 09 Abril 2018
# Crea grafo circular de n nodos, cada nodo se conecta con
# los k siguientes y anteriores. Ademas se incluyen aristas
# con probabilidad prob

from grafo import Grafo
from random import random
import math

for t in range(1,11):
    print(t) 
    n = 80 # nodos
    k = 30
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

    p = 1
    for nodo in G.V:
        for j in range(k):
            if (nodo + j + 1) >= n:
                a = (nodo + j + 1) - n
            else:
                a = (nodo + j + 1)
            G.arista(nodo, a, False, p)

    prob = 2*(10**-t) # probabilidad aristas aleatorias
    for v in G.V:
        for w in G.V:
            if random() < prob:
                if (v, w, False, p) not in G.E and v != w:
                    G.arista(v, w, False, p)

    with open("cc_n80_k30.csv", "at") as archivo:
        print(prob, G.clust_coef(), file=archivo)
    
    with open("dist_n80_k30.csv", "at") as archivo:
        print(prob, G.arg_dist(n,k), file=archivo)
