import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0) # for reproducibility

T = 60*60*24 # 60*60*24 = 1 day worth
path = np.zeros((T + 1,2)) # lecture
angle = np.random.uniform(0, 2*np.pi, size=(T,)) # lecture
step = np.random.randn(T)
xs = step* np.cos(angle)
ys = step* np.sin(angle)
# lecture
csx = np.cumsum(xs) # increment x coordinates
csy = np.cumsum(ys) # increment y coordinates

path[1:,0] = csx # update all the x coordinates but leave the first coordinate zero
path[1:,1] = csy # update all the y coordinates
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (20,8)) # two subplots for both graphs (looked up how to create two graphs in same plot, google ai)
ax1.axis('equal')
ax1.plot(path.T[0],path.T[1],lw=.5) # path after a day
# recall np.linalg.norm(path,?) (lecture)
distance = np.linalg.norm(path,axis=1)
ax2.plot(distance) # distance from origin over time
