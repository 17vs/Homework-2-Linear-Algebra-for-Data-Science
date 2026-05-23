import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0) # for reproducibility

n = 50
path = np.zeros((n,2)) # lecture

angle = np.deg2rad(19) # constant angle
k = np.arange(n)
step = angle*k

xs = np.cos(step) # cos
ys = np.sin(step) # sin
csx = np.cumsum(xs) # increment x coordinates
csy = np.cumsum(ys) # increment y coordinates
# since coordinates are (cos, sin) we get a distance of 1

path[:,0] = csx # update all the x coordinates but leave the first coordinate zero
path[:,1] = csy # update all the y coordinates

plt.axis('equal')
plt.plot(path.T[0],path.T[1],lw=.5)
