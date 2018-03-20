from math import *
from numpy import *
from sympy import *
import matplotlib.pyplot as plt


def functionInDot(f, t):
    return eval(f, {'x': t, 'exp': math.exp, 'sqrt': math.sqrt})


def arrayOfDots(f, array):
    y = []
    for i in array:
        y.append(eval(f, {'x': i, 'exp': math.exp, 'sqrt': math.sqrt}))
    return y

def drawPlot(startOfXLabel, endOfXLabel, f):
    x = linspace(startOfXLabel, endOfXLabel, 40)
    y = arrayOfDots(f, x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def diffWithMinus(f):
    result = str(diff(f))
    result = result.replace('-exp', '(-1) * exp')
    result = str(result)
    result = result.replace('-sqrt', '(-1) * sqrt')
    return str(result)

def newtonMethod(f, start, end, epsilon):
    firstX = 0.001
    currentX = functionInDot(f, firstX)
    nextX = currentX - functionInDot(f, currentX) / functionInDot(diffWithMinus(f), currentX)
    while abs(nextX - currentX) > epsilon:
        print("currentX = %.8f\n" % currentX)
        print("f(x) = %.8f\n" % functionInDot(f, currentX))
        print("f`(x) = %.8f\n" % functionInDot(diffWithMinus(f), currentX))
        print("(nextX - currentX) = %.8f\n" % abs(nextX - currentX))
        currentX = nextX
        nextX = currentX - functionInDot(f, currentX) / functionInDot(diffWithMinus(f), currentX)
    print("currentX = %.8f\n" % currentX)
    print("f(x) = %.8f\n" % functionInDot(f, currentX))
    print("f`(x) = %.8f\n" % functionInDot(diffWithMinus(f), currentX))
    print("(nextX - currentX) = %.8f\n" % abs(nextX - currentX))
    return currentX


f = input('f(x):')
startOfXLabel = float(input('Start Of X Label'))
endOfXLabel = float(input('End Of X Label'))
drawPlot(startOfXLabel, endOfXLabel, f)
newtonMethod(f, startOfXLabel, endOfXLabel, 0.000001)

