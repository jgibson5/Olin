import matplotlib.pyplot as pyplot
import mpl_toolkits.mplot3d as p3d
import math

def roh(t, vals):
    r = vals[0]
    l = vals[1]
    rDot = vals[2]
    rohMin = vals[3]
    rohMax = vals[4]
    m = vals[5]
    k1 = vals[6]
    k2 = vals[7]
    num = vals[8]
    return (rohMax - rohMin) / (2 * math.pi * r * num) * t + rohMin

def xFunc(t, vals):
    r = vals[0]
    l = vals[1]
    rDot = vals[2]
    rohMin = vals[3]
    rohMax = vals[4]
    m = vals[5]
    k1 = vals[6]
    k2 = vals[7]
    num = vals[8]
    return r * math.cos(float(t))
    
def yFunc(t, vals):
    r = vals[0]
    l = vals[1]
    rDot = vals[2]
    rohMin = vals[3]
    rohMax = vals[4]
    m = vals[5]
    k1 = vals[6]
    k2 = vals[7]
    num = vals[8]
    return r * math.sin(float(t))

def zFunc(t, vals):
    r = vals[0]
    l = vals[1]
    rDot = vals[2]
    rohMin = vals[3]
    rohMax = vals[4]
    m = vals[5]
    k1 = vals[6]
    k2 = vals[7]
    num = vals[8]
    return t * math.sqrt(l**2 - (2 * math.pi * r * num)**2) / (2 * math.pi * num)

def findCOM(xs, ys, zs, vals):
    r = vals[0]
    l = vals[1]
    rDot = vals[2]
    rohMin = vals[3]
    rohMax = vals[4]
    m = vals[5]
    k1 = vals[6]
    k2 = vals[7]
    num = vals[8]
    pi2n = 2 * math.pi * num
    comX = k1 * (pi2n * math.sin(pi2n) + math.cos(pi2n) - 1)
    comX += k2 * math.sin(pi2n)
    
    comY = k1 * (-pi2n * math.cos(pi2n) + math.sin(pi2n))
    comY += k2 * (-math.cos(pi2n) + 1)
    
    comZ = k1 * zFunc(1, vals) * (1.0 / 3) * (pi2n)**3 / r
    comZ += k2 * zFunc(1, vals) * .5 * (pi2n)**2 / r
    
    return comX, comY, comZ 
	    
def makeVectorField(x, y, z, t, vals, n = 100):
    r = vals[0]
    l = vals[1]
    rDot = vals[2]
    rohMin = vals[3]
    rohMax = vals[4]
    m = vals[5]
    k1 = vals[6]
    k2 = vals[7]
    num = vals[8]
    
    timeSteps = []
    for i in range(n):
        timeSteps.append(t[0] + (t[1] - t[0]) * (float(i) / n) * 2 * math.pi)
    
    points = []
    for time in timeSteps:
        if time != 0: points.append((x(time, vals), y(time, vals), z(time, vals)))
    return points
	
def main():
	
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    
    for i in range(0,20):
        for j in range(1,20):
            num = j / 10.0
            rohMin = 500
            r = 10.0
            l = 2* math.pi * r * num + 100
            rDot = l / (2 * math.pi * num)
            rohMax = 15000.0
            m = (rohMax + rohMin) / 2.0 * l

            k1 = (l * r * (rohMax - rohMin)) / (m * (2 * math.pi * num)**2)
            k2 = (rohMin * l * r) / (2 * math.pi * num * m)
            
            vals = [r, l, rDot, rohMin, rohMax, m, k1, k2, num]
          
            points = makeVectorField(xFunc, yFunc, zFunc, [0,num], vals)
    
            xs, ys, zs = zip(*points)
    
            comX, comY, comZ = findCOM(xs, ys, zs, vals)
            
            print num, rohMin, rohMax, comX, comY, comZ
            
            ax.scatter([comX], [comY], [comZ])
            ax.plot(xs, ys, zs)
    
    pyplot.xlabel('X')
    pyplot.ylabel('Y')
    pyplot.title('Impact of Changing the Density on Center of Mass')
    pyplot.show()
if __name__ == '__main__':
    main()
