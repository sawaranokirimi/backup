#coding:utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from set_to_grid import Lines 
import analyze

                               
class Patterns():
    def __init__(self, lt, rb):
        self.lt = lt
        self.rb = rb

    
    #===移動距離l, 分割数n===
    def slide(self, l=10000, n=1):
        patterns = np.zeros(((2*n+1)**2, 4))
        d = float(l)/n
        
        index = 0
        for y in range(-n, n+1, 1):
            for x in range(-n, n+1, 1):
                lt = np.array(self.lt) + d*np.array([x, y])
                rb = np.array(self.rb) + d*np.array([x, y])
                patterns[index, 0] = lt[0]
                patterns[index, 1] = lt[1]
                patterns[index, 2] = rb[0]
                patterns[index, 3] = rb[1]
                index += 1

        return pd.DataFrame(patterns)

    #===回転角theta, 分割数n, 拡大率p(%), 拡大の分割数pn===
    def zoom_rotate(self, theta=0, n=0, p=100, pn=0):
        if n==0 or theta==0:
            kaku = 0
            n=0
        else:
            kaku = float(theta)/n  / 180.0 * np.pi
        if pn==0 or p==100:
            zoom = 0
            pn = 0
        else:    
            zoom = (float(p)-100)/pn/100 

        patterns = np.zeros(((2*n+1)*(2*pn+1), 4))
        center = [(self.rb[0] + self.lt[0])/2.,\
                  (self.rb[1] + self.lt[1])/2.] 
        lt_rb = np.array([[self.lt[0], self.rb[0]],\
                          [self.lt[1], self.rb[1]]])

        center = np.matrix([[center[0], center[0]],\
                           [center[1], center[1]]])

        index = 0
        for i in range(-n, n+1, 1):
            R = np.matrix([[np.cos(kaku*i), -np.sin(kaku*i)],\
                           [np.sin(kaku*i), np.cos(kaku*i)]])

            for j in range(-pn, pn+1, 1):
                zoomed = (zoom*j+1.0)*(lt_rb - center)
                rotated = np.dot(R, zoomed) + center
            
                patterns[index, 0] = rotated[0, 0]
                patterns[index, 1] = rotated[1, 0]
                patterns[index, 2] = rotated[0, 1]
                patterns[index, 3] = rotated[1, 1]

                index += 1

        return pd.DataFrame(patterns)
        
        

def kakunin(lt_rb):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    ax.set_aspect('equal')
    print lt_rb

    def sakuzu(lt, rb):
        line = plt.Polygon([lt, rb], lw=1.0, fc='red')
        ax.add_patch(line)
    
    for aaa in lt_rb.values:
        sakuzu([aaa[0], aaa[1]], [aaa[2], aaa[3]])

    plt.show()


def main1():
    lt = (7898455, 18031077) 
    rb = (11952121, 19776635)
    lt = (10, 0) 
    rb = (-5, 5*np.sqrt(3))
    lt = (-1.830127, -3.169873) 
    rb = (6.830127, 11.830127)

    patterns = Patterns(lt, rb)
    X1 = patterns.slide(l=10000, n=1)
    X2 = patterns.zoom_rotate(theta=90, n=3, p=100, pn=1)

    #kakunin(X2)

#回転、拡大、移動の選択範囲を作成
def automation(lt, rb, slide_l=10000, slide_n=1,\
                       rotate_theta=0, rotate_n=0,\
                       zoom_p=100, zoom_n=0):
    
    patterns = Patterns(lt, rb)
    if slide_l == 0:
        df = patterns.zoom_rotate(rotate_theta, rotate_n,\
                                       zoom_p, zoom_n)

    elif rotate_theta == 0 and zoom_p == 100:
        df = patterns.slide(slide_l, slide_n)

    else:
        in_data = patterns.slide(slide_l, slide_n)
        df = pd.DataFrame()
        
        for lt_rb in in_data.values:
            temp = Patterns(lt_rb[0:2], lt_rb[2:4])
            temp = temp.zoom_rotate(rotate_theta, rotate_n,\
                                       zoom_p, zoom_n)
            df = pd.concat([df, temp])

    return pd.DataFrame(df.values, \
                        columns = ['lt_x','lt_y','rb_x','rb_y'])

def roop(df):
    data = pd.read_csv('data_projected.csv').values
    lt_rb_norm = pd.DataFrame()
    
    for i, lt_rb in enumerate(df.values):
        lt = (lt_rb[0], lt_rb[1])
        rb = (lt_rb[2], lt_rb[3])
        lines = Lines(data, lt, rb)
        gathered = lines.gather().values[:, 2]

        Q = pd.read_csv('transformation_matrix_18.csv').values

        double_fourier = analyze.DoubleFourier(gathered, Q)
        norm = analyze.Norm(gathered, Q)
        # === 324(4)の割合を指定 ===
        target = norm.save_data().ix[25, 1] / norm.save_data().ix[:, 1].sum()
        # === === === === ====    
        temp = pd.DataFrame([lt[0],lt[1], rb[0], rb[1], target]).T
        lt_rb_norm = pd.concat([lt_rb_norm, temp])
        print '%d/%d' %(i+1, df.values.shape[0])
    
    lt_rb_norm = lt_rb_norm.sort(4, ascending=False)
    return pd.DataFrame(lt_rb_norm.values, \
                        columns=['lt_x','lt_y','rb_x','rb_y', 'target'])
                


def main2():
    #lt = (10, 0) 
    #rb = (-5, 5*np.sqrt(3))
    lt= (19463701, 20803099)
    rb= (20263272, 20180245)

    slide_l = 100*1000
    slide_n = 1
    rotate_theta = 15
    rotate_n = 1
    zoom_p = 120
    zoom_n = 1

    auto = automation(lt, rb, slide_l, slide_n,\
                              rotate_theta, rotate_n,\
                              zoom_p, zoom_n)
    #kakunin(auto)
    print auto
    roop(auto).to_csv('data_rooped.csv')



if __name__ == '__main__':
    #main1()
    main2()
