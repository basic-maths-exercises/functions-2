import matplotlib.pyplot as plt
import numpy as np

xspacing = 20 / 499
xvalues = np.zeros(500)
for i in range(500) : xvalues[i] = -10 + i*xspacing

def quadratic( a, b, c ) :
  yvalues = np.zeros(500)
  for i in range(500) : yvalues[i] = a*xvalues[i]*xvalues[i] + b*xvalues[i] + c
  return yvalues
  
# Now plot all the curves
aa, bb, cc = -2, 4, 8
plt.plot( xvalues, quadratic(aa,bb,cc), "b-")
plt.plot( xvalues, quadratic(1,4,8), "r-")
plt.savefig("quadratics.png")
