# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Luca Maddaleni, 330001030
# Section:      273
# Assignment:   Lab 13b Assignment 2
# Date:         12/6/2020

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