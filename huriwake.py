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
"""index = np.argwhere(np.arange(n**2).reshape(n, n))
num = a.shape[0]
pop_on_lattice = np.zeros(n, n)
for i,j in index:
    for num_i in num:
        print i, j """


pop_on_lattice = np.zeros([n, n]) 
for i, j, pop in a:
    print i, j, pop
    pop_on_lattice[i, j] += pop
    
print pop_on_lattice

