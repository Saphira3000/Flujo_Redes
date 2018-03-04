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
		



