#coding:utf-8
import numpy as np

a = np.array([[1, 4, 500],
     [2, 3, 500],
     [5, 1, 600],
     [2, 3, 500]])

print a

b = np.argwhere(a[:, 0]==1)
print b


# 振り分け                              
n = 6


pop_on_lattice = np.zeros([n, n]) 
for i, j, pop in a:
    print i, j, pop
    pop_on_lattice[i, j] += pop
    
print pop_on_lattice

