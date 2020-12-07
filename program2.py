from numpy import *
from matplotlib.pyplot import *

v = array((1, 0))

M = array([(1.00583, -0.087156), (0.087156, 1.00583)])

x = []
y = []

new_point = v @ M

for i in range(169):
    new_point = new_point @ M
    x.append(new_point[0])
    y.append(new_point[1])

plot(x, y)
show()