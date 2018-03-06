class Grafo:

    def __init__(self):
        self.V = dict() # conjunto de nodos
        self.E = list() # conjunto de aristas
        open("nodos.dat",'w')

    def nodo(self,v,x,y,r):
        self.V[v] = (x,y)
        with open("nodos.dat", 'a') as archivo:
            print(x,y,r, file = archivo)

    def arista(self,u,v,d,p):
        self.E.append((u,v,d,p))
      
    def grafica(self):
        i = 1
        with open("grafo.plot", 'w') as archivo:
            print('set term png', file = archivo)
            print('set output "grafo.png"', file = archivo)
            print('set size square', file = archivo)
            print('set key off', file = archivo)
            print('set xrange [-0.1:1.1]', file = archivo)
            print('set yrange [-0.1:1.1]', file = archivo)
            for v in self.E:
                u = v[0]
                w = v[1]
                (x1, y1) = self.V[u]
                (x2, y2) = self.V[w]
                if v[3] != 0 and v[2] == False: # ponderado
                    print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'nohead lw {:f}'.format(v[3]), file = archivo)
                    i += 1
                elif v[3] != 0 and v[2] == True: # ponderado y dirigido
                    print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'head filled size screen 0.03,15 lw {:f}'.format(v[3]), file = archivo)
                    i += 1
                elif v[2] == True: # dirigido
                    print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'head filled size screen 0.03,15', file = archivo)
                    i += 1
                else: # simple
                    print('set arrow',i,'from', x1 , ',', y1, 'to', x2,',', y2,'nohead', file = archivo)
                    i += 1
            print('plot "nodos.dat" using 1:2:3 with points pt 7 ps var lc "purple"', file = archivo)

    def floyd_warshall(self): 
        d = {}
        for v in self.V:
            d[(v, v)] = 0 # distancia reflexiva es cero
        for arista in self.E:
            (v, u, m, p) = arista
            if m:
                d[(v, u)] = p
            else:
                d[(v, u)] = p
                d[(u, v)] = p
        for intermedio in self.V:
            for desde in self.V:
                for hasta in self.V:
                    di = None
                    if (desde, intermedio) in d:
                        di = d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in d:
                        ih = d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c # mejora al camino actual
        return d

    def camino(self, s, t, f): # construcción de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for arista in self.E:
                (w, v, m, p) = arista
                if w == u and v not in cola and v not in usados:
                    actual = f.get((u, v), 0)
                    dif = p - actual 
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if t in usados:
            return camino
        else: # no se alcanzó
            return None
  
    def ford_fulkerson(self, s, t): # algoritmo de Ford y Fulkerson
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

