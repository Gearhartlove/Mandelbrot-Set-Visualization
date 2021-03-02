#Kristoff Finley
#I followed the excellent tutorial from Tariq Rashid's "Make Your Own Mandelbrot" book
import numpy as np
import matplotlib.pyplot as plt

#calculates whether point c diverges after maxiter iterations
#using the function z --> z^2 + c
def MandelbrotFunction (c, maxiter):
    iterations = 0
    z = complex(0,0)
    for iteration in range(maxiter):
        if abs(z) > 4:
            break
        iterations += 1
        z = (z*z) + c
    return iterations


def CreateComplexPlain (maxIterations):
    #set the location and size of the complex plane rectangle
    xvalues = np.linspace(0.1, 0.5, 2000)
    yvalues = np.linspace(-0.1, -0.5, 2000)

    #size of these lists of x and y values
    xlen = len(xvalues)
    ylen = len(yvalues)

    #creates a 2D array, then creates each point, based off the xlen and ylen lists
    atlas = np.empty((xlen,ylen))
    for ix in range(xlen): #iterating over each complex point (x,y)
        for iy in range(ylen):

            cx = xvalues[ix]
            cy = yvalues[iy]
            c = complex(cx, cy)

            #testing iterations per complex point c
            atlas[ix,iy] = MandelbrotFunction(c,maxIterations)
    return atlas

def Main():
    maxIterations = 40; #number of iterations until considered divergent
    plt.figure(figsize = (18,18))
    #myFractal = CreateComplexPlain(maxIterations)
    plt.imshow(CreateComplexPlain(maxIterations).T, interpolation = "nearest")
    print("finished")
    plt.show()

#--------------------------------------------------------------------    
Main()
        
