#coding:utf-8

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np



class Ploting():
    def __init__(self, in_data):
        self.data = pd.read_csv(in_data, index_col=0)
        self.fig = plt.figure()        
        self.ax = self.fig.add_subplot(111) 
        self.m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
                            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')

    def make_fig(self):

        self.m.drawcoastlines()
        # self.m.fillcontinents(color='coral',lake_color='aqua')
        # --- draw parallels and meridians.---
        # self.m.drawparallels(np.arange(-90.,91.,30.))
        # self.m.drawmeridians(np.arange(-180.,181.,60.))
        # self.m.drawmapboundary(fill_color='aqua')
        plt.title("Mercator Projection")
       
    def convert(self):

        def pop_wo_float(aaa):
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

        return pd.DataFrame({'x':x, 'y':y, 'pop':pop})
       
    def scatter(self):
        data = self.convert()
        plt.scatter(data['x'], data['y'], 0.0001*data['pop'], alpha=0.5)
       
        plt.show()




def main1():
    file_name = 'data.csv'
    ploting = Ploting(file_name)
    ploting.convert()
    ploting.make_fig()
    ploting.scatter()
   
if __name__ == '__main__':
                          
    main1()               
