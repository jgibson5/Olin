import matplotlib.pyplot as pyplot
import mpl_toolkits.mplot3d as p3d
import numpy as np
import math

def c_func(l, w):
    a = .9 * l * w
    b = 1.4 * (1 / w + 1 / l)
    c = .36 * (l + w)
    d = .72 / (l * w)
    print a + b + c + d
    return a + b + c + d

def lspace(a, b, n):
    r = b - a
    res = []
    for i in range(n):
        res.append(i * (b - a) / n + a)
    return res
    
def plotFunc(func, aMin, aMax, bMin, bMax, n):
    results = np.zeros((n, n))
    a = np.linspace(aMin, aMax, n)
    b = np.linspace(bMin, bMax, n)
    for i in range(n):
        #results.append([])
        for j in range(n):
            #results[i].append(func(a[i+1], b[j+1]))
            #results.append(func(a[i+1], b[j+1]))
            results[i, j] = func(a[i], b[j])
    a, b = np.meshgrid(a, b)
    print np.size(a)
    print np.size(b)
    print np.size(results)
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([a], [b], [results])
    fig.add_axes(ax)
    
    pyplot.show()
    
plotFunc(c_func, 1.1, 1.3, 1.1, 1.3, 10)
    

#Plot .9(LW)+1.4(1/W+1/L)+.36(L+W)+.72/(LW)  from L = 1.1 to 1.3 and W = 1.1 to 1.3
