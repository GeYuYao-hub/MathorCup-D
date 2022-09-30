import numpy as np
import math
import matplotlib.pylab as pylab

X = []
Y = []
path = 'out.txt'
g = np.zeros([61, 61]).astype('int')
for i in range(0, 61):
    for j in range(0, 61):
        dis = math.sqrt(math.pow(i - 30, 2) + math.pow(j - 30, 2))
        if dis <= 30:
            X.append(i - 30)
            Y.append(j - 30)
            g[i][j] = 1
    print()

print(X)
print(Y)
print(g)
pylab.imshow(g)
pylab.show()
