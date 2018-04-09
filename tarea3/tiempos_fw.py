from random import random, randint
from grafo import Grafo
import time

for n in range(1,11):
    for j in range(1,11): # replicas
        i = 0
        G = Grafo()
        for nodo in range(n*10):
            x = random()
            y = random()
            r = 0.025  
            G.nodo(i,x,y,r)
            i += 1
        for v in G.V:
            for w in G.V:
                if random() < 0.2:
                    G.arista(v, w, True, randint(1,8))
        with open("tiempos_fw_dir.csv", "at") as archivo:
            ti = time.time()
            G.floyd_warshall()
            print(time.time() - ti, file=archivo)

