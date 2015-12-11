#coding:utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


class Drawing():
    def __init__(self, data, figname='figure', n=18):
        self.data =data
        self.n = n
        self.figname = figname
        #self.n = int(round(np.sqrt(len(data))))
        self.fig = plt.figure()                           
        self.ax = self.fig.add_subplot(111, aspect='1.0') 

    def xy_label(self):
        number = 0
        xy = np.zeros([self.n**2, 2])
        for i in range(self.n):
            for j in range(self.n):
                xy[number, 0] = j
                xy[number, 1] = i
                number += 1

        return pd.DataFrame({'x':xy[:, 0], 'y':xy[:, 1]})
        
    # 基底ベクトル
    def obli_vectors(self):
        return np.array([[1., 0.],
                         [-1/2., np.sqrt(3)/2.]])

    # 左下、左上、右上、右下の座標
    def set_points(self):
        lb = [0, 0]
        lt = self.obli_vectors()[1] * (self.n - 1)
        rb = self.obli_vectors()[0] * (self.n - 1)
        rt = lt + rb

        # 最後のlbはpathを閉じるため
        return [lb, lt, rt, rb, lb]


    def outline_patch(self):
        codes = [Path.MOVETO,         
                Path.LINETO,          
                Path.LINETO,          
                Path.LINETO,          
                Path.CLOSEPOLY]                     

        path = Path(self.set_points(), codes)
        return patches.PathPatch(path, lw=1, facecolor='None', alpha=1.0)   

    def grid_patch(self):
        points = []
        codes = []
        haba =  1.
        theta = 0.
        lb = self.set_points()[0]
        lt = self.set_points()[1]
        rt = self.set_points()[2]
        rb = self.set_points()[3]

        #　斜線のpath
        for i in range(1, self.n - 1):
            # x方向
            points.append((lb[0] + i*haba*np.cos(theta), 
                           lb[1] + i*haba*np.sin(theta)))
            points.append((lt[0] + i*haba*np.cos(theta), 
                           lt[1] + i*haba*np.sin(theta)))
            codes.append(Path.MOVETO)
            codes.append(Path.LINETO)
            # y方向
            points.append((lb[0] - i*haba*np.cos(np.pi/3.-theta),
                           lb[1] + i*haba*np.sin(np.pi/3.-theta)))
            points.append((rb[0] - i*haba*np.cos(np.pi/3.-theta),
                           rb[1] + i*haba*np.sin(np.pi/3.-theta)))
            codes.append(Path.MOVETO)
            codes.append(Path.LINETO)
            
        path = Path(points, codes)
        return patches.PathPatch(path, lw=1, facecolor='None', alpha=1.0)   

    def combine(self):
        self.ax.add_patch(self.outline_patch())                                                    
        self.ax.add_patch(self.grid_patch())                                                    


    # 作図の基本設定       
    def draw_setting(self):
        plt.axis('off')                                   
        self.ax.set_xlim(self.set_points()[1][0]-2, self.set_points()[3][0]+2)
        self.ax.set_ylim(-2, self.set_points()[1][1]+2)

    # 円を作図(scatter)
    def scatter(self, teisuu=140):
        pop_max = max(self.data.values[:, 2])
        for x_obli, y_obli, z in self.data.values:
            xy = np.dot(self.obli_vectors().T, [x_obli, y_obli])
            if z >= 0:
                self.ax.scatter(xy[0], xy[1], z/pop_max*teisuu, facecolor='b', edgecolor='midnightblue', alpha=.6)
            else :
                self.ax.scatter(xy[0], xy[1], -z/pop_max*teisuu, color='y', alpha=.6)

    # 円を作図2(patchを使ってcircleを描く)
    def circle(self, teisuu=1.0):
        radius = map(np.sqrt, map(np.abs, self.data.values[:, 2]))
        norm = np.linalg.norm(radius)
        radius = radius / norm
        pop_max = max(radius)
        pop_min = min(radius)
  
        for x_obli, y_obli, z in self.data.values:
            xy = np.dot(self.obli_vectors().T, [x_obli, y_obli])
            r = np.sqrt(np.abs(z)) / norm / pop_max *( 0.3 + 1.4*(pop_max - pop_min) )
            r = r * teisuu
            if z >= 0:
                circle = patches.Circle(xy, r, color=(0.15,0.15,0.55), ec='0.0', alpha=1.0)
            else :
                circle = patches.Circle(xy, r, color=(1,1,0.5), ec='0.0', alpha=1.0)
            self.ax.add_patch(circle)                                                    


    # まとめて作図(scatter)
    def draw_all(self, teisuu=140):
        self.draw_setting()
        self.scatter(teisuu)
        self.combine()
        self.fig.savefig('%s.eps' % self.figname) 
        self.fig.savefig('%s.pdf' % self.figname)
        self.fig.savefig('%s.png' % self.figname)

   # Blue と Yellow で scatterを用いず作図
    def draw_all_BY(self, teisuu=140):
        self.draw_setting()
        self.combine()
        self.circle(teisuu)
        self.fig.savefig('%s.eps' % self.figname) 
        self.fig.savefig('%s.pdf' % self.figname)
        self.fig.savefig('%s.png' % self.figname)

   # ｘｙのラベルがないデータの作図
    def draw_all_noxy(self, teisuu=140):
        xy = self.xy_label()
        df = pd.concat([xy, self.data], axis=1) 
        #print df
        drawing = Drawing(df, self.figname)
        print drawing.data
        drawing.draw_all_BY(teisuu=1.0)

        #self.draw_setting()
        #self.combine()
        #self.circle(teisuu)
        #self.fig.savefig('%s.eps' % self.figname) 
        #self.fig.savefig('%s.pdf' % self.figname)
        #self.fig.savefig('%s.png' % self.figname)


def main1():
    pop = pd.read_csv('data_gathered.csv')
    drawing = Drawing(pop)
    drawing.set_points()
    drawing.draw_setting()
    drawing.combine()
    drawing.scatter()
    plt.show()

def main2():
    pop = pd.read_csv('usa-pop-2014(3)/data_gathered.csv')
    drawing = Drawing(pop).draw_all(teisuu=1000)
    plt.show()


def main3():
    pop = pd.read_csv('data_gathered.csv')
    drawing = Drawing(pop)
    drawing.set_points()
    drawing.draw_setting()
    drawing.combine()
    #drawing.scatter()
    drawing.circle(teisuu=1.0)
    plt.show()


def main_heikou():
    dist_theo = pd.read_csv('moved_transformation_matrix_18.csv')['4_1']
    Drawing(dist_theo, 'figureA').draw_all_noxy()



if __name__ == '__main__':
    main3()




