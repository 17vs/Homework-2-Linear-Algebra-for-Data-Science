# plot here
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
# create n by 2 matrix
n = 1000000
p = np.random.rand(n,2) # some random points (n points in 2D ([0,1)x[0,1)))
center = np.array([0.5, 0.5]) # define center as (0.5, 0.5)


distance = np.linalg.norm(p-center,axis=1) # lecture
inside = distance<.5 # if less than 0.5, means point is within circle as distance from center is less than radius


count = np.sum(inside) # count number of true, meaning number of points within circle
total = inside.size # count total number of points
pi = (count/total)*4 # pi approximation
print(pi)


plt.axis('equal');
# select true for inside and false for outside (use not operator)
plt.scatter(p[inside, 0], p[inside, 1], color='green')
plt.scatter(p[~inside, 0], p[~inside, 1], color='red') # ~inside means outside

