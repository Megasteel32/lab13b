# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do
#  I have not given or received any unauthorized aid on this assignment
#
# Name:         Luca Maddaleni, 330001030
# Section:      273
# Assignment:   Lab 13b Assignment 1
# Date:         12/6/2020

from numpy import *

req_array = array([(200, 975, 3, 2, 1), (225, 850, 8, 2, 1), (250, 850, 3, 3, 1), (100, 850, 3, 3, 2), (0, 500, 0, 5, 0), (0, 500, 0, 5, 1), (150, 595, 5, 8, 1), (175, 675, 20, 8, 3), (250, 1080, 9, 10, 1), (250, 800, 8, 10, 1), (800, 850, 0, 12, 2), (0, 725, 50, 12, 0)])
prices_array = array([(0.14, 0.22, 5.50, 8.95, 185), (0.09, 0.21, 5.75, 8.94, 195), (0.10, 0.22, 5.65, 7.00, 205)])

final_cost = []

for i in range(len(req_array)):
    temp_list = []
    for j in range(len(prices_array)):
        temp_list.append(req_array[i] @ prices_array[j])
    final_cost.append(temp_list)

final_array = array(final_cost)
print(final_array)

temp_sum = 0
for x in range(len(final_array)):
    temp_sum += final_array[x][0]

shop_a = temp_sum

temp_sum = 0
for x in range(len(final_array)):
    temp_sum += final_array[x][1]

shop_b = temp_sum

temp_sum = 0
for x in range(len(final_array)):
    temp_sum += final_array[x][2]

shop_c = temp_sum

print(f"Shop A's cost: ${round(shop_a, 2)}. Shop B's cost: ${round(shop_b, 2)}. Shop C's cost: ${round(shop_c, 2)}.")