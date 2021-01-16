import numpy as np
import matplotlib.pyplot as plt



#calculates whether point c diverges after maxiter iterations
def mandel (c, maxiter):
    iterations = 0
    z = complex(0,0)
    for iteration in range(maxiter):
        if abs(z) > 4:
            break
        iterations += 1
        z = (z*z) + c
    return iterations

#def main():
#    print(mandel(complex(0.5,0.5),40))

#set the location and size of the complex plane rectangle
xvalues = np.linspace(0.1, 0.5, 2000)
yvalues = np.linspace(-0.4, 1.0, 2000)

#size of these lists of x and y values
xlen = len(xvalues)
ylen = len(yvalues)

atlas = np.empty((xlen,ylen))
for ix in range(xlen):
    for iy in range(ylen):

        cx = xvalues[ix]
        cy = yvalues[iy]
        c = complex(cx, cy)

        atlas[ix,iy] = mandel(c,300)

#-------------------------------
#main()
plt.figure(figsize=(18,18))
plt.imshow(atlas.T, interpolation="nearest")

plt.show()

        
