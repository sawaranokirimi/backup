#coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.patches as patches
import matplotlib.cm as cm
import matplotlib.lines as mlines
from geopy.distance import vincenty

import parallelogram 
import set_to_grid


class Ploting():
    def __init__(self, in_data, kaizoudo='c'):
        self.data = pd.read_csv(in_data, index_col=0)
        self.fig = plt.figure()        
        self.ax = self.fig.add_subplot(111) 
        self.m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
                            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution=kaizoudo)
        self.lt = [10, 10]
        self.rb = [0, 0]
    
    #basemapの作成
    def make_fig(self):

        self.m.drawcoastlines()
        self.m.drawcountries()
        # self.m.fillcontinents(color='coral',lake_color='aqua')
        # --- draw parallels and meridians.---
        # self.m.drawparallels(np.arange(-90.,91.,30.))
        # self.m.drawmeridians(np.arange(-180.,181.,60.))
        # self.m.drawmapboundary(fill_color='aqua')
        # plt.title("Mercator Projection")
    
    #lonをx, latをyに変換
    def convert(self):
        def pop_wo_float(aaa):
            aaa = str(aaa)
            if ',' in aaa:
                aaa = aaa.replace(',', '')
            return float(aaa)
        pop = map(pop_wo_float, self.data['pop'])
        lat = self.data['lat']
        lon = self.data['lon']
        x = []
        y = []
        
        for lat_i, lon_i in zip(lat, lon):
            x_i, y_i = self.m(lon_i, lat_i)
            x.append(x_i)
            y.append(y_i)

        df = pd.DataFrame({'x':x, 'y':y, 'pop':pop}, columns=['x', 'y', 'pop'])
        df.to_csv('data_projected.csv', index=False)
        return df

    #　平行四辺形の一辺の実距離
    def distance(self):
        lt_latlon = self.m(self.lt[0], self.lt[1], inverse=True)
        rb_latlon = self.m(self.rb[0], self.rb[1], inverse=True)
        taikaku = vincenty(lt_latlon, rb_latlon).km
        print lt_latlon
        print rb_latlon
        #l = taikaku / np.sqrt(3)
        return taikaku


    def callback_line(self):
        x = [self.lt[0], self.rb[0]]
        y = [self.lt[1], self.rb[1]]
        line = mlines.Line2D(x, y, color='green')
        taikaku_line = self.ax.add_line(line)

    def callback_parallel(self, toumeido=0.1, grid=True, face=True, rireki=False):
        lines = set_to_grid.Lines(self.data, self.lt, self.rb)
        if rireki == True:
            df = pd.read_csv('data_lt_rb.csv', index_col=0)
            lt= [df.ix[0,0], df.ix[0,1]]
            rb= [df.ix[1,0], df.ix[1,1]]
            lines = set_to_grid.Lines(self.data, lt, rb)

        lb = lines.lattice_genten()
        rt = lines.lattice_rt()
        
        parallel = parallelogram.Parallel(lb, self.lt, rt, self.rb)
        if rireki == True:
            parallel = parallelogram.Parallel(lb, lt, rt, rb)
        path = parallel.parallel_outline()
        path_grid = parallel.parallel_grid()
        if face==True:
            patch = patches.PathPatch(path, facecolor='green', lw=2, alpha=toumeido)   
        else :
            patch = patches.PathPatch(path, facecolor='none', edgecolor=(1, 0, 0), lw=3, alpha=0.8)   
        patch_grid = patches.PathPatch(path_grid, lw=1, alpha=0.3)             
        self.ax.add_patch(patch)                                                    
        if grid==True:
            self.ax.add_patch(patch_grid)                                               

    def heikou(self, lt, rb, toumeido=0.1, color=(1, 0, 0), lw=1):
        lines = set_to_grid.Lines(self.data, lt, rb)
        lb = lines.lattice_genten()
        rt = lines.lattice_rt()
        parallel = parallelogram.Parallel(lb, lt, rt, rb)

        path = parallel.parallel_outline()
        patch = patches.PathPatch(path, facecolor='none', edgecolor=color, lw=lw, alpha=toumeido)   
        return patch

    def draw_many(self, df, kaiseki=True):
        # 人口の散布図
        teisuu = 500
        data = self.convert()
        data['pop'] = data['pop'] / np.linalg.norm(data['pop']) 
        self.fig.canvas.draw() # キャンバスに描く
        sca = self.ax.scatter(data['x'], data['y'], teisuu*np.abs(data['pop']), \
                color='blue', edgecolors='grey', alpha=0.5)

        # 分析範囲の作図
        if kaiseki is True:
            df = df.sort('target', ascending=True)
            target_max = max(df.values[:, 4])
        for lt_rb in df.values:
            lt = (lt_rb[0], lt_rb[1]) 
            rb = (lt_rb[2], lt_rb[3])
            if kaiseki is True and lt_rb[4] == target_max:
                self.ax.add_patch(self.heikou(lt, rb, 0.8, (1, 0, 0), 2.5))
            else:
                self.ax.add_patch(self.heikou(lt, rb, 0.3, (1, 0.5, 0.0)))
        plt.show()
            

    # callbackして描いたものをOFFにする
    def callback_off(self):
        self.ax.patches.pop()
        self.ax.patches.pop()
        self.ax.lines.pop()
       
    def onclick(self, event):
        line = mlines.Line2D([0,0], [0,0])
        taikaku_line = self.ax.add_line(line)
        self.lt = [event.xdata, event.ydata]

    def onrelease(self, event):
        self.rb = [event.xdata, event.ydata]   
        self.callback_line()
        self.callback_parallel()
        self.fig.canvas.draw() # キャンバスに描く
        self.callback_off()


    def scatter(self, teisuu=1000):
        data = self.convert()
        data['pop'] = data['pop'] / np.linalg.norm(data['pop']) 
        '''sca = self.ax.scatter(data['x'], data['y'], teisuu*np.abs(data['pop']), \
                c=data['pop'], cmap=cm.bwr, edgecolors='grey', alpha=0.5)'''
        sca = self.ax.scatter(data['x'], data['y'], teisuu*np.abs(data['pop']), \
                color='blue', edgecolors='grey', alpha=0.5)
        #sca.set_clim(-1., 1.)

        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        cid = self.fig.canvas.mpl_connect('button_release_event', self.onrelease)

        lines = set_to_grid.Lines(self.data, self.lt, self.rb)
        lb = lines.lattice_genten()
        rt = lines.lattice_rt()
        
        parallel = parallelogram.Parallel(lb, self.lt, rt, self.rb)
        path = parallel.parallel_outline()
        patch = patches.PathPatch(path, facecolor='orange', lw=2, alpha=0.4)   
        #patch_grid = patches.PathPatch(path_grid, lw=1, alpha=0.4)             
        self.ax.add_patch(patch)                                                    
        #ax.add_patch(patch_grid)                                               
        plt.show()
        print lines.lattice_size()

    def analizing_area(self, lt, rb, teisuu=4000):
        self.lt = lt
        self.rb = rb
        data = self.convert()
        data['pop'] = data['pop'] / np.linalg.norm(data['pop']) 
        self.fig.canvas.draw() # キャンバスに描く
        sca = self.ax.scatter(data['x'], data['y'], teisuu*np.abs(data['pop']), \
                color='blue', edgecolors='grey', alpha=0.5)
        self.callback_parallel(toumeido=0.25, grid=False, face=False)
        plt.show()


def main1():
    file_name = 'usa-pop-2014(1)/usa-pop-2014.csv'
    ploting = Ploting(file_name)
    print ploting.convert()
    ploting.make_fig()
    ploting.scatter()
    print ploting.distance()

def main2():
    lat = 54.6360021
    lon = 13.3439199

    m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution=None)
    #plt.clf()
    #m.bluemarble()
    plt.show()
    print 'lat, lon', lat, lon
    print 'x, y', m(lon, lat)
    
# 分析範囲確認用
def main3():
    file_name = 'usa_canada-pop-2014/usa_canada-pop-2014.csv'
    file_name2 = 'south_germany-pop-2011/south_germany-pop-2011.csv'
    file_name4 = 'CityPopulation/china/population-china-2010.csv'
    file_name5 = 'CityPopulation/russia/russia_all-pop-2010.csv'
    df = pd.read_csv('data_lt_rb.csv', index_col=0)
    print df
    lt= [df.ix[0,0], df.ix[0,1]]
    rb= [df.ix[1,0], df.ix[1,1]]
    ploting = Ploting(file_name5, kaizoudo='i')
    ploting.make_fig()
    ploting.analizing_area(lt, rb, teisuu=2000)
    #ploting.analizing_area(lt2, rb2, teisuu=3000)

def for_auto(lt_rb, kaiseki=True):
    file_name = 'usa_canada-pop-2014/usa_canada-pop-2014.csv'
    file_name2 = 'south_germany-pop-2011/south_germany-pop-2011.csv'
    file_name4 = 'CityPopulation/china/population-china-2010.csv'
    file_name5 = 'CityPopulation/russia/russia_all-pop-2010.csv'
    ploting = Ploting(file_name5, kaizoudo='c')
    ploting.make_fig()

    #lt_rb = pd.read_csv('data_rooped.csv', index_col=0)

    ploting.draw_many(lt_rb, kaiseki)

    



   
if __name__ == '__main__':
    main3()               
    #for_auto()
