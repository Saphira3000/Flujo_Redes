from grafo import Grafo
from random import sample
import time

k = 5 # nodos por lado en rejilla
n = k*k # total nodos
l = 2 # para aristas simetricas
p = 0.002 # prob para aristas de largo alcance
mu = 10
sigma = 2
lamb = 5

G = Grafo()
G.rejilla(k, l, p, mu, sigma, lamb) # crea rejilla
G.grafica("rejilla", "nodos.dat", k)

s = n-k # nodo fuente
t = k-1 # nodo destino

# ----- Percolacion de aristas -----
#G.rejilla(k, l, p, mu, sigma, lamb)
#flujo = G.ford_fulkerson(s, t)
#cuantos = 0
#while flujo != 0:
#    G.per_aris(sample(G.E.keys(), 1))
#    cuantos += 1
#    flujo = G.ford_fulkerson(s,t)
#    with open("pa_1.dat", "at") as archivo:
#        print(cuantos, flujo, file=archivo)


# ----- Percolacion de nodos -----
nodos = G.V.copy()
nodos.pop(s)
nodos.pop(t)
flujo = G.ford_fulkerson(s, t)
cuantos = 0
while flujo != 0:
    cual = sample(nodos.keys(), 1)        
    nodos.pop(cual[0])
    G.per_nodo(cual) 
    cuantos += 1
    ti = time.time()
    flujo = G.ford_fulkerson(s,t)
    print(flujo, cual)
    t = t + (time.time() - ti)
    with open("perNod.dat", "at") as archivo:
        print(cuantos, flujo, t, file=archivo)

