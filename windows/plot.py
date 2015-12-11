#coding: utf-8
import os
import numpy as np
import matplotlib.pyplot as plt
import random


# # # # # 作図 # # # # #
def plot(y, x_label):
    n = len(y)
    bityousei = 9.5
    x = np.arange(n)*bityousei

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.bar(x, y, width=7.5, align="center", edgecolor='white')
    ax.plot([-1.0*bityousei, max(x)+bityousei], [0, 0], color = 'grey')

    for x, y, i in zip(x, y, range(n)):
        if y >= 0.0:
            ax.text(x, y, x_label[i], ha='center', va= 'bottom', fontsize=7.0)
        else:
            ax.text(x, y, x_label[i], ha='center', va= 'top', fontsize=7.0)

    ax.set_xlim(-1.0*bityousei, np.max(x)+bityousei)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks(())
    ax.set_yticks([-1.0, -0.5, 0, 0.5, 1.0])


    fig.savefig("aa.eps")


# # # # # 実行 # # # # #
'''y = range(36)
for i in range(36):
    y[i] = random.random()*2 - 1.0
x_label = range(36)
plot(y, x_label)'''
