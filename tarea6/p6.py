# Algoritmo aproximado de contraccion
from random import random, randint, sample
from grafo2 import Grafo
import time

k = 30 # nodos por lado en rejilla
n = k**2 # total nodos
l = 1
G = Grafo() 
G1 = Grafo()

G.rejilla(k, l) # crea rejilla
G.grafica("grafica", "nodos.dat", k)
#print(G.E)

with open("aristas.dat", 'w') as archivo:
    for arista in G.E:
        (u,v) = arista
        p = G.E[arista]
        print(u, v, p, file = archivo)           

s = str(n-k) # nodo fuente
t = str(k-1) # nodo destino

ti_f = time.time()
ff = G.ford_fulkerson(s, t)
tf_f = time.time() - ti_f
#open("flujo_k10.dat", "w")

aprox_antes = 100000
i = 0
#open("resultados_k10.dat", "w")

ti_a = time.time()
while (aprox_antes) > (ff+3) and i < (n/2):
    i += 1
    j = 1
    #print("iteracion", i)
    #print("---------------- NUEVO --------------")
    G1.copia("nodos.dat", "aristas.dat")
    while len(G1.E) > 2:
        if j == 1:
            cual = sample(G.E.keys(), 1)    
            (u,v) = cual[0]
            n1 = u.split('-')
            n2 = v.split('-')
            while (s in n1 and t in n2) or (s in n2 and t in n1):
                cual = sample(G1.E.keys(), 1)    
                (u,v) = cual[0]
                n1 = u.split('-')
                n2 = v.split('-')
            #print(cual)       
        else:
            max_key = max(G1.E, key=lambda k: G1.E[k])
            (u,v) = max_key
            n1 = u.split('-')
            n2 = v.split('-')
            while (s in n1 and t in n2) or (s in n2 and t in n1):
                cual = sample(G1.E.keys(), 1)    
                (u,v) = cual[0]
                n1 = u.split('-')
                n2 = v.split('-')
        uaux = u + "-" + v
        if (s in n2) or (t in n2):
            temp = u
            u = v
            v = temp
        G1.per_aris((u,v))
        G1.vecinos[u].remove(v)
        vec = G1.vecinos[v]  
        G1.V.pop(v)
        G1.V[uaux] = G1.V[u] 
        G1.vecinos[uaux] = G1.vecinos[u]
        vec2 = G1.vecinos[u]       
        for b in vec2:
            pond = G1.E[(u,b)]
            G1.per_aris((u,b))
            G1.arista(uaux, b, pond)
        for a in vec:
            pond = G1.E[(v,a)]
            G1.per_aris((v,a))
            if (uaux, a) in G1.E:
                pond2 = G1.E[(uaux,a)]
                G1.E[(uaux,a)] = pond + pond2
                G1.E[(a,uaux)] = pond + pond2
            else:
                G1.arista(uaux, a, pond)
        G1.V.pop(u)
        j += 1

    #print(G1.E)
    r = sample(G1.E.keys(),1)[0]
    result = G1.E[r]
    #print(ff, aprox_antes, result)

    for u in G.V:
        G1.vecinos[u].clear()
    G1.V = {}
    G1.E = {}
    
    if result <= aprox_antes:
        aprox_antes = result 
        #with open("resultados_k10.dat", 'a') as archivo:       
        #    print(i, aprox_antes, file = archivo)
    
    #with open("flujo_k10.dat", 'a') as archivo:       
    #    print(i, ff, file = archivo)

    if ff == result:
        break
tf_a = time.time() - ti_a

with open("tiempos_p6.dat", "at") as archivo:
    print(k, tf_f - tf_a, file=archivo)
