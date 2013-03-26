import matplotlib.pyplot as pyplot
import mpl_toolkits.mplot3d as p3d
import math

c = 1
a = 1

def x_func(u, v):
    return (1 + .5 * v * math.cos(u / 2)) * math.cos(u)
    
def y_func(u, v):
    return (1 + .5 * v * math.cos(u / 2)) * math.sin(u)
    
def z_func(u, v):
    return .5 * v * math.sin(u / 2)
    
def transform(u1, u2, v1, v2):
    
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    xs = []
    ys = []
    zs = []
    for u in range(100):
        u = u * (u2 - u1) / 100.0 + u1
        for v in range(100):
            v = v * (v2 - v1) / 100.0 + v1
            print u, v
            xs.append(x_func(u, v))
            ys.append(y_func(u, v))
            zs.append(z_func(u, v))
    
    ax.scatter(xs, ys, zs)
    pyplot.xlabel('X Value')
    pyplot.ylabel('Y Value')
    #pyplot.zlabel('Z Value')
    pyplot.title('Mobius Strip')
    pyplot.show()
    
transform(0, 2*math.pi, -1, 1)
