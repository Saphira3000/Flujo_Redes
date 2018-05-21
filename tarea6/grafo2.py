from random import random, randint, normalvariate
from math import floor

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
            print(v,x,y,r,c, file = archivo)
    
    def arista(self, u, v, p):
        self.E[(u,v)] = p 
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
                pond = self.E[a]
                (x1, y1, c1) = self.V[u]
                (x2, y2, c2) = self.V[w]
                if pond != 0: # ponderado
                    print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'nohead', file = archivo)
                    print('set label "', int(pond),'" at', (x1+x2)/2, ',', (y1+y2)/2, file = archivo)         
                    i += 1
            print('plot "' + datos + '" u 2:3:4:5 with circles lc var fs solid 0.5, "' + datos + '" using 2:3:(sprintf("%d", $1)) with labels offset char 0,0 notitle', file = archivo)
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
                pond = self.E[arista]
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


    def rejilla(self, k, l):
        et = 0 # etiqueta nodo
        for i in range(k):
            for j in range(k):
                x = j
                y = i
                r = 0.1 # radio del nodo
                self.nodo(str(et), x, y, r, 0)
                et += 1
        for v in self.V: # aristas simetricas
            for w in self.V:
                d = self.man(v, w)
                if d <= l and (v, w) not in self.E and v != w:
                    pond = floor(normalvariate(10, 2))          
                    self.arista(v, w, pond)
                    
    def man(self,a,b): # distancia del taxista (Manhattan)
        (x1, y1, c1) = self.V[a]
        (x2, y2, c2) = self.V[b]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        d = dx + dy
        return(d)

    def per_aris(self,cual): # percolacion aristas
        (u,v) = cual
        #pond = self.E[(u,v)]
        self.E.pop((u,v))
        otro = (v, u)
        self.E.pop(otro)
        self.vecinos[v].remove(u)
        #self.vecinos[u].remove(v)

    def copia(self, nodos, aristas):
        with open(nodos, 'r') as archivo:
            for linea in archivo.readlines():
                algo = linea.split('\n')
                algo = str(algo[0])
                (v,x,y,r,c) = algo.split(' ')
                self.V[v] = (int(x), int(y), int(c))
                if not v in self.vecinos: # vecindad de v
                    self.vecinos[v] = set()
        with open(aristas, 'r') as archivo:
            for linea in archivo.readlines():
                algo = linea.split('\n')                
                algo = str(algo[0])
                (u, v, p) = algo.split(' ')
                self.E[(u,v)] = int(p)
                self.vecinos[v].add(u)
                self.vecinos[u].add(v)

