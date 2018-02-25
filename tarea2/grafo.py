class Grafo:

    def __init__(self):
        self.V = dict() # conjunto de nodos
        self.E = list() # conjunto de aristas

    def nodo(self,v, x,y):
        self.V[v] = (x,y)
        with open("nodos.dat", 'w') as archivo:
            print(x,y, file = archivo)

    def arista(self, v, u):
        self.E.append((u,v))

    def grafica(self):
        i = 1
        with open("grafo.plot", 'w') as archivo:
            print('set term png', file = archivo)
            print('set output "grafo.png"', file = archivo)
            print('set size square', file = archivo)
            print('set key off', file = archivo)
            #print('set xrange [-0.1:1.1]', file = archivo3)
            #print('set yrange [-0.1:1.1]', file = archivo3)
            for (u, v) in self.E:
                (x1, y1) = self.V[u]
                (x2, y2) = self.V[v]

                print('set arrow',i,'from', x1 , ',', y1, 'to', x2,',', y2,'nohead', file = archivo)
                i += 1
    	    #print('plot "nodos.dat" using 1:2 with points pt 7 ps 3 lc "blue"', file = archivo)
		



