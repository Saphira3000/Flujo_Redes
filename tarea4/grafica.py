with open("grafica.plot", 'w') as archivo:
    print('set term postscript eps enhanced color', file = archivo)
    print('set output "cc.eps"', file = archivo) 
    print('set datafile separator ","', file = archivo)
    print('set logscale y', file = archivo)
    print('set logscale x', file = archivo)
    #print('plot "dist_n80_k30.csv" u 0:1 with lines lc "red"', file = archivo)
    print('plot "cc_n80_k30.csv" u 0:1 with lines lc "blue"', file = archivo)
    print('reset', file = archivo)
