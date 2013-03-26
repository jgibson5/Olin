import matplotlib.pyplot as pyplot
import mpl_toolkits.mplot3d as p3d
import math

def xFunc(t):
    return -math.exp(-t) + 1
    
def yFunc(t):
    return (2.0 / 3) * math.sin(3.0 * t) + 2

def zFunc(t):
    return (-2.0 / 3) * math.cos(3.0 * t) - 1
    
def makeVectorField(x, y, z, t, n = 100):
    timeSteps = []
    for i in range(n):
        timeSteps.append(t[0] + (t[1] - t[0]) * (float(i)/n))
    
    points = []
    for time in timeSteps:
        points.append((xFunc(time), yFunc(time), zFunc(time)))
    return points
	
def main():
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    points = makeVectorField(xFunc, yFunc, zFunc, [1,2])
    
    xs, ys, zs = zip(*points)
    
    ax.scatter(xs, ys, zs)
    pyplot.show()
if __name__ == '__main__':
    main()
