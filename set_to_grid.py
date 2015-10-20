#coding:utf-8
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Lines():
    def __init__(self, data, lt, rb, n=6):
        self.data = data
        self.lt = map(float,lt)
        self.rb = map(float,rb)
        self.n = n

    # latticeの一辺のサイズを求める
    def lattice_size(self):
        return np.linalg.norm([self.lt[0]-self.rb[0], 
                               self.lt[1]-self.rb[1]])/np.sqrt(3)
    # latticeの傾きを求める
    def lattice_angle(self):
        return np.pi/6.0 - np.arctan((self.lt[1]-self.rb[1])/(self.rb[0]-self.lt[0]))

    # latticeの原点を求める
    def lattice_genten(self):
        return [self.rb[0]-self.lattice_size()*np.cos(self.lattice_angle()),
                self.rb[1]-self.lattice_size()*np.sin(self.lattice_angle())]


    # 斜交座標上の座標を獲得
    def basement_vector(self):
        haba = self.lattice_size() / (self.n - 1)
        P = haba * np.array([[1.0, -1.0/2.0],        
                             [0.0, np.sqrt(3.0)/2.0]])
        rot = np.matrix(
                        ((np.cos(self.lattice_angle()), -np.sin(self.lattice_angle())),
                         (np.sin(self.lattice_angle()), np.cos(self.lattice_angle()) ))
                        )
                        
        P = np.dot(rot, P)
        xy = self.data[0:, 0:2].T           
        #print 'coordinate before\n', xy

        genten = self.lattice_genten()
        xy[0, :] = xy[0, :] - genten[0]
        xy[1, :] = xy[1, :] - genten[1]
        obli_xy = np.linalg.solve(P, xy)

        #print 'coordinate slide\n', xy         
        #print 'coordinate obli\n', obli_xy
        #print 'coordinate obli int\n', np.round(obli_xy)
        
        return np.round(obli_xy)

    # 分析範囲外の点のインデックスを取得
    def eliminate_point(self):
        data_num = self.data.shape[0]
        obli_xy = self.basement_vector()
        index = [] # 排除する点の行番号

        for i in range(data_num):
            if obli_xy[0, i] >= self.n or obli_xy[1, i] >= self.n :
                index.append(i)

        return index

    # 分析対象外の点を外す
    def eliminate(self):
        pass
            
    # グリッドの交点にデータを集める
    def gather(self):
        pass

def main1():
    data = pd.read_csv('in_data.csv').values 
    lt = [0, 500*np.sqrt(3.0)]
    rb = [1500, 0]
   # lt = [137, 514]
   # rb = [379, 320]

    X = Lines(data, lt, rb)
    print X.lattice_angle()
    print X.lattice_size() 
    print X.lattice_genten() 
    X.basement_vector()
    X.eliminate_point()



    

if __name__ == '__main__':
    print os.getcwd()
    main1()
