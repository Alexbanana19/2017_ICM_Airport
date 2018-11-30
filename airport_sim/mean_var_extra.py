# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:46:19 2017

@author: Alex
"""


import airport_sim5_extra_precheck as sim
import numpy as np
import matplotlib.pyplot as plt

mean_list = []
var_list = []
M = 50

for p in range(M): 
    tmp1, tmp2 = sim.main()
    mean_list.append(tmp1)
    var_list.append(tmp2)
    print("Episode: ", p)
plt.figure(1)
plt.scatter(range(M), mean_list)
plt.ylabel("Average Waiting Time")
plt.xlabel("#Expeiment")
plt.title("Passenger Mean Waiting Time")
plt.show()
plt.figure(2)
plt.scatter(range(M), var_list)
plt.ylabel("Waiting Time Variance")
plt.xlabel("#Expeiment")
plt.title("Passenger Waiting Time Variance")
plt.show()

print(mean_list)
print(var_list)