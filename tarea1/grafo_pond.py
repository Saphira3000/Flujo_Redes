from random import random, randint
nodos = []
rad = []
n = 25 # nodos
#p = 0.1
i = 1 # etiqueta para la arista
j = 0
with open("nodos.dat", 'w') as archivo1:
    for nodo in range(n):
        x = random()
        y = random()
        r = randint(2,6)
        nodos.append((x,y))
        rad.append(r)
        print(x,y,r, file = archivo1)
with open("grafo_ponderado.plot", 'w') as archivo3:
    print('set term png', file = archivo3)
    print('set output "grafo_pond.png"', file = archivo3)
    print('set size square', file = archivo3)
    print('set key off', file = archivo3)
    print('set xrange [-0.1:1.1]', file = archivo3)
    print('set yrange [-0.1:1.1]', file = archivo3)
    for (x1, y1) in nodos:
        r = rad[j]
        for (x2, y2) in nodos:
            if random() < r*0.007:
                #print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'head filled size screen 0.03,15', file = archivo3)
                pond = r/2.0
                print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2, 'nohead lw {:f} lc {:f}'.format(pond, r), file = archivo3)
                i += 1
        j += 1
    print('plot "nodos.dat" using 1:2:3:3 with points pt 7 ps var lc var', file = archivo3)
    print('quit()', file = archivo3)