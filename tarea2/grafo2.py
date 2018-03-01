class Grafo:

    def __init__(self):
        self.V = dict() # conjunto de nodos
        self.E = list() # conjunto de aristas
        open("nodos.dat",'w')

    def nodo(self,v,x,y):
        self.V[v] = (x,y)
        with open("nodos.dat", 'a') as archivo:
            print(x,y, file = archivo)

    def arista(self, u, v, d, p):
        self.E.append((u,v,d,p)) 
        #if d == 0:
         #   self.E[(v, u)] = self.E[(u, v)] = p
        #else:
         #   self.E[(v, u)] = p

    def grafica(self):
        i = 1
        with open("grafo.plot", 'w') as archivo:
            print('set term postscript', file = archivo)
            print('set output "grafo.eps"', file = archivo)
            print('set size square', file = archivo)
            print('set key off', file = archivo)
            #print('set xrange [-0.1:1.1]', file = archivo3)
            #print('set yrange [-0.1:1.1]', file = archivo3)
            for v in self.E:
                print(v)
                u = v[0]
                w = v[1]
                #print(u)
                #print(w)
                (x1, y1) = self.V[u]
                (x2, y2) = self.V[w]
                print('set arrow',i,'from', x1 , ',', y1, 'to', x2,',', y2,'nohead', file = archivo)
                i += 1
            print('plot "nodos.dat" using 1:2 with points pt 7 ps 3 lc "blue"', file = archivo)
		



