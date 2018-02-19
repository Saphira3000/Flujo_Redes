from random import random, randint
nodos = []
n = 25 # nodos
p = 0.05
p1 = 0.1
p2 = 0.3
p3 = 0.5
i = 1 # etiqueta para la arista
with open("nodos.dat", 'w') as archivo1:
    for nodo in range(n):
        x = random()
        y = random()
        #r = randint(2,7) # radio y color
        nodos.append((x,y))
        print(x,y, file = archivo1)
        #print(x,y,r, file = archivo1)
with open("grafo_rc.plot", 'w') as archivo3:
    print('set term png', file = archivo3)
    print('set output "prueba005.png"', file = archivo3)
    print('set size square', file = archivo3)
    print('set key off', file = archivo3)
    print('set xrange [-0.1:1.1]', file = archivo3)
    print('set yrange [-0.1:1.1]', file = archivo3)
    for (x1, y1) in nodos:
        for (x2, y2) in nodos:
            if random() < p:
                print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2,'nohead', file = archivo3)
                i += 1
    print('plot "nodos.dat" using 1:2 with points pt 7 ps 3 lc "blue"', file = archivo3)
    print('reset', file = archivo3)
    
    print('set term png', file = archivo3)
    print('set output "prueba01.png"', file = archivo3)
    print('set size square', file = archivo3)
    print('set key off', file = archivo3)
    print('set xrange [-0.1:1.1]', file = archivo3)
    print('set yrange [-0.1:1.1]', file = archivo3)
    for (x1, y1) in nodos:
        for (x2, y2) in nodos:
            if random() < p1:
                print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2,'nohead', file = archivo3)
                i += 1
    print('plot "nodos.dat" using 1:2 with points pt 7 ps 3 lc "blue"', file = archivo3)
    print('reset', file = archivo3)
    
    print('set term png', file = archivo3)
    print('set output "prueba03.png"', file = archivo3)
    print('set size square', file = archivo3)
    print('set key off', file = archivo3)
    print('set xrange [-0.1:1.1]', file = archivo3)
    print('set yrange [-0.1:1.1]', file = archivo3)
    for (x1, y1) in nodos:
        for (x2, y2) in nodos:
            if random() < p2:
                print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2,'nohead', file = archivo3)
                i += 1
    print('plot "nodos.dat" using 1:2 with points pt 7 ps 3 lc "blue"', file = archivo3)
    print('reset', file = archivo3)
    
    print('set term png', file = archivo3)
    print('set output "prueba05.png"', file = archivo3)
    print('set size square', file = archivo3)
    print('set key off', file = archivo3)
    print('set xrange [-0.1:1.1]', file = archivo3)
    print('set yrange [-0.1:1.1]', file = archivo3)
    for (x1, y1) in nodos:
        for (x2, y2) in nodos:
            if random() < p3:
                print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2,'nohead', file = archivo3)
                i += 1
    print('plot "nodos.dat" using 1:2 with points pt 7 ps 3 lc "blue"', file = archivo3)
    print('quit()', file = archivo3)
    
