#coding: utf-8
import os
import numpy as np
import matplotlib.pyplot as plt
import random


# # # # # 作図 # # # # #
def plot(y, x_label):
    n = len(y)
    bityousei = 1.0
    x = np.arange(n)*bityousei

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.barh(x, y, align="center", edgecolor='grey', color='c')
    ax.vlines(0, -1.0*bityousei, np.max(x)+bityousei, color = '0.3')
    ax.hlines([0.5, 2.5, 3.5, 7.5, 11.5, 15.5, 19.5, 23.5, 27.5], -1.2, 1.2, color = 'grey', linestyles='--', linewidth=0.4)

    for x, y, i in zip(x, y, range(n)):
        if y >= 0.0:
            ax.text(-0.01, x, x_label[i], ha='right', va= 'center', fontsize=7.0)
        else:
            ax.text(y-0.01, x, x_label[i], ha='right', va= 'center', fontsize=7.0)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.0*bityousei, np.max(x)+bityousei)
    ax.set_yticks(())
    ax.set_xticklabels([r'$-1.0$', r'$-0.5$', r'$0$', r'$0.5$', r'$1.0$'])
    ax.set_xticks([-1.0, -0.5, 0, 0.5, 1.0])


    fig.savefig("out_naiseki.eps")


class Graph():
    def __init__(self, name):
        self.name = name
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def to_tex(self, text):
        col = []
        for content in text:
            temp = '$' + content + '$'
            col.append(r'%s' % temp)

        return col

class GraphNorm(Graph):
    def __init__(self, name, norm, col_norm):
        Graph.__init__(self, name)
        self.norm = norm
        self.col_norm = col_norm

    def plot_norm_frame(self):
        ax = self.ax
        norm = self.norm
        x = range(len(self.norm))
        label = self.to_tex(self.col_norm)

        for i, content in enumerate(label):
            label[i] = content.replace('k=', '')

        ax.set_ylim(-0.08, 1.2)
        ax.set_xticks(x)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
        ax.set_xticklabels(label)
        ax.set_yticklabels([r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1.0$'])
        ax.set_xlabel(r'$(m, n)$')
        ax.set_ylabel(r'$norm_{m, n}$')

    def plot_norm(self):
        ax = self.ax
        norm = self.norm
        x = range(len(self.norm))

        self.plot_norm_frame()
        ax.plot(x, norm, color='c', marker ='o', markeredgecolor = 'None')

        self.fig.savefig("%s.eps" % self.name)

# # # # # 実行 # # # # #
'''y = range(36)
for i in range(36):
    y[i] = random.random()*2 - 1.0
x_label = range(36)
plot(y, x_label)'''
