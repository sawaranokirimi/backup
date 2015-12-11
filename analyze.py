#coding:utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ptick
import sakuzu
from matplotlib.font_manager import FontProperties



class DoubleFourier():
    def __init__(self, data, Q):
        self.data = data
        self.Q = Q
        self.n = int(np.sqrt(data.shape[0]))

    def normalize(self):
        Z = np.zeros([self.n**2, self.n**2])
        for i in range(self.n**2):
            Z[:, i] = self.Q[:, i] / np.linalg.norm(self.Q[:, i])
            
        return Z

    def analize(self):
        Q = self.normalize()
        #return np.linalg.solve(Q, self.data/np.linalg.norm(self.data))
        return np.linalg.solve(Q, self.data)

    def save_data(self):
        p = pd.DataFrame({'naiseki':self.analize()})
        p.to_csv('naiseki.csv')


class Norm(DoubleFourier):
    def __init__(self, data, Q):
        DoubleFourier.__init__(self, data, Q)

    def distribution(self):
        x = np.zeros([self.n**2, self.n**2])
        Q = self.normalize()
        p = self.analize()
        for i in range(self.n**2):
            x[:, i] = p[i] * Q[:, i]
        return x
        
    def get_norm_18(self):
        df = pd.read_csv('hexagon_18.csv')
        colname = pd.concat([pd.Series([1, 3, 4]), df['D']])

        norm = np.zeros(len(colname))
        dist = np.zeros([self.n**2, len(colname)])
        P = self.analize()**2
        D = self.distribution()
        
        def sumation(X, begin, end):
            temp = 0.0
            for i in range(begin, end + 1):
                temp += X[i]
            return temp

        def sumation_vector(X, begin, end):
            temp = np.zeros(self.n**2)
            for i in range(begin, end + 1):
                temp += X[:, i]
            return temp
             
        #ノルムの重ねあわせ
        norm[0] = P[0]
        norm[1] = P[1] + P[2]
        norm[2] = P[3] + P[4] + P[5]
        dist[:, 0] = D[:, 0]
        dist[:, 1] = D[:, 1]+D[:, 2]
        dist[:, 2] = D[:, 3]+D[:, 4]+D[:, 5]

        num1 = 6        
        K = df['k'].values
        L = df['l'].values
        for i in range(3, len(colname)):
            k = K[i-3]
            l = L[i-3]

            if l == 0:                       
                num2 = num1+5
            elif k == l:                     
                num2 = num1+5
            else :                           
                num2 = num1+11

            norm[i] = sumation(P, num1, num2)
            dist[:, i] = sumation_vector(D, num1, num2)
            num1 = num2 + 1

        dist_df = pd.DataFrame(dist)
        dist_df.columns = colname.values
        dist_df.to_csv('distribution.csv', index=None)
        
        return norm

    def save_data(self):
        colname = pd.concat([pd.Series([1, 3, 4]), 
                             pd.read_csv('hexagon_18.csv')['D']])
        colname = pd.DataFrame({'D':colname.values})
        norm = pd.DataFrame({'norm':self.get_norm_18()})
        df = pd.concat([colname, norm], axis=1)

        df.to_csv('norm.csv')


class PlotNorm():
    def __init__(self, columns, norm):
        self.norm = norm
        self.columns = columns
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def plot(self):
        self.ax.plot(self.norm)
        plt.show()

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
    def __init__(self, name, col_norm, norm):
        Graph.__init__(self, name)
        self.norm = norm
        self.col_norm = col_norm
        print norm

    def plot_norm_frame(self):
        ax = self.ax
        # 軸の指数表記を10^nにする
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax.yaxis.set_major_formatter(ptick.ScalarFormatter(useMathText=True))
        norm = self.norm
        x = range(len(self.norm))
        fp = FontProperties(fname=r'/usr/share/fonts/truetype/vlgothic/VL-PGothic-Regular.ttf', size=14)
        #label = self.to_tex(self.col_norm)
        #for i, content in enumerate(label):
        #    label[i] = content.replace('k=', '')

        #ax.set_ylim(0, 1400000)
        ax.set_xticks(x)
        #ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
        label = self.col_norm
        ax.set_xticklabels(label, rotation='vertical', fontproperties=fp)
        #ax.set_yticklabels([r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1.0$'])
        ax.set_xlabel(r'$\rm{k}$')
        ax.set_ylabel(r'$\rm{power\,  spectra}$')

    def plot_norm(self):
        ax = self.ax
        norm = self.norm
        x = range(len(self.norm))

        self.plot_norm_frame()
        ax.plot(x, norm, color='black', marker ='o', markeredgecolor = 'None')

        # 追加のPlot
        #norm2 = pd.read_csv('norm2.csv', encoding='utf-8')['norm']
        #ax.plot(x, norm2, color='m', marker ='o', markeredgecolor = 'None')

        self.fig.subplots_adjust(bottom = 0.2)
        self.fig.savefig("%s.eps" % self.name)
        self.fig.savefig("%s.png" % self.name)


def main1():
    data = pd.read_csv('data_gathered.csv').values[:, 2]
    Q = pd.read_csv('transformation_matrix_18.csv').values
    #Q = pd.read_csv('moved_transformation_matrix_18.csv').values


    double_fourier = DoubleFourier(data, Q)
    norm = Norm(data, Q)

    double_fourier.save_data()
    norm.save_data()
    
    data_norm = pd.read_csv('norm.csv', encoding='utf-8')
    graphnorm = GraphNorm('graph_norm', data_norm['D'], data_norm['norm'])
    graphnorm.plot_norm()
    print norm.distribution()
#    plotnorm.plot()

if __name__ == '__main__':
    main1()      
    plt.show()
