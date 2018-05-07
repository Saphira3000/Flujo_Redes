from random import random, normalvariate, expovariate
from math import floor
import shutil

class Grafo:

    def __init__(self):
        self.V = dict() # conjunto de nodos
        self.E = dict() # conjunto de aristas
        self.vecinos = dict() # un mapeo
        open("nodos.dat",'w')

    def nodo(self,v,x,y,r,c):
        self.V[v] = (x,y,c)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set()
        with open("nodos.dat", 'a') as archivo:
            print(x,y,r,c,v, file = archivo)
    
    def arista(self, u, v, d, p):
        self.E[(u,v)] = (d,p) 
        if d == False:
           self.E[(v, u)] = self.E[(u, v)]
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)

    def grafica(self, file_name, datos, k):
        i = 1
        with open(str(file_name)+".plot", 'w') as archivo:
            print('set term postscript eps enhanced color', file = archivo)
            print('set output "', file_name + ".eps", '" ', file = archivo)
            print('set size square', file = archivo)
            print('set key off', file = archivo)
            print('set xrange [-1:{:f}]'.format(k), file = archivo)
            print('set yrange [-1:{:f}]'.format(k), file = archivo)
            print('unset tics', file = archivo)
            print('unset border', file = archivo)
            for a in self.E:
                u = a[0]
                w = a[1]
                (diri,pond) = self.E[a]
                (x1, y1, c1) = self.V[u]
                (x2, y2, c2) = self.V[w]
                if pond != 0 and diri == False: # ponderado
                    print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'nohead', file = archivo)
                    i += 1
                elif pond != 0 and diri == True: # ponderado y dirigido       
                    print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'head filled size screen 0.03,15', file = archivo)
                    i += 1
                elif diri == True: # dirigido
                    print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'head filled size screen 0.03,15', file = archivo)
                    i += 1
                else: # simple
                    print('set arrow',i,'from', x1 , ',', y1, 'to', x2,',', y2,'nohead', file = archivo)
                    i += 1
            print('plot "' + datos + '" u 1:2:3:4 with circles lc var fs solid 0.5, "' + datos + '" using 1:2:(sprintf("%d", $5)) with labels offset char 0,0 notitle', file = archivo)
            print('reset', file = archivo)

    def camino(self, s, t, f): # construcción de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for arista in self.E:
                (w, v) = arista
                (direc, pond) = self.E[arista]
                if w == u and v not in cola and v not in usados:
                    actual = f.get((u, v), 0)
                    dif = pond - actual 
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if t in usados:
            return camino
        else: # no se alcanzó
            return None
  
    def ford_fulkerson(self, s, t): # algoritmo de Ford-Fulkerson
        if s == t:
            return 0
        maximo = 0
        f = dict()
        while True:
            aum = self.camino(s, t, f)
            if aum is None:
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = t
            while u in aum:
                v = aum[u][0]
                actual = f.get((v, u), 0) # cero si no hay
                inverso = f.get((u, v), 0)
                f[(v, u)] = actual + incr
                f[(u, v)] = inverso - incr
                u = v
            maximo += incr
        return maximo


    def rejilla(self, k, l, p, mu, sigma, lamb):
        et = 0 # etiqueta nodo
        for i in range(k):
            for j in range(k):
                x = j
                y = i
                r = 0.1 # radio del nodo
                if et == (k**2 - k):
                    self.nodo(et, x, y, r, 7)            
                elif et == k-1:
                    self.nodo(et, x, y, r, 6)
                else:
                    self.nodo(et, x, y, r, 0)
                et += 1
        for v in self.V: # aristas simetricas
            for w in self.V:
                d = self.man(v, w)
                if d <= l and (v, w) not in self.E and v != w:
                    pond = floor(normalvariate(mu, sigma))
                    if pond > 0:            
                        self.arista(v, w, False, pond)
                    else:
                        self.arista(v, w, False, -pond)
        for v in self.V: # aristas de largo alcance
            for w in self.V:
                if random() < p and (v, w) not in self.E:
                    pond = floor(expovariate(lamb))
                    self.arista(v, w, True, pond)

    def man(self,a,b): # distancia del taxista (Manhattan)
        (x1, y1, c1) = self.V[a]
        (x2, y2, c2) = self.V[b]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        d = dx + dy
        return(d)

    def per_aris(self,cual): # percolacion aristas
        (u,v) = cual[0]
        (diri, pond) = self.E[(u,v)]
        if diri:
            self.E.pop((u,v))
        else: # si es arista simple
            self.E.pop((u,v))
            otro = (v, u)
            self.E.pop(otro)
        print(self.E)

    def per_nodo(self,cual): # percolacion nodos    
        cual = cual[0]
        vec = self.vecinos[cual]
        for a in vec:
            quien = [(cual,a)]
            if (cual,a) in self.E:
                self.per_aris(quien)
        self.V.pop(cual)

