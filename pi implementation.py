# plot here
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(2)
all_pi = []
correct = 0
for i in range (10): # repeat 10 times to get 10 pi approximations
  # create n by 2 matrix
  n = 1000000

  p = np.random.uniform(0, 1, size=(n,2)) # some random uniform points (n points in 2D ([0,1]x[0,1]))

  inside = p[:, 0]**2 + p[:,1]**2 <= 1 # x^2 + y^2 < 1, that is within circle
  # lecture
  k = np.arange(1,n+1,1) # steps
  b = np.cumsum(inside) # count of points inside


  pi = (b/k)*4 # pi approximation
  last = pi[-1] # pi[-1] is last pi of array
  if abs(last-np.pi) < 0.0005: # check if pi estimate is within 3 decimal places of actual
    correct += 1
  all_pi.append(round(float(last), 3)) # append last pi , round to three decimal places (fix formatting with float)

print(all_pi)
print("{}/10".format(correct))
