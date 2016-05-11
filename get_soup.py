# coding: utf-8
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import pandas as pd
import sys
import codecs

#soup = BeautifulSoup(open('USA-Cities.html'))
#b = soup.find(id='citysection').find_all('tr', itemtype="http://schema.org/City")  
#data = []

#for bi in b:
   # print bi.find(itemprop='name').string, bi.find('td', 'rpop prio1').string
#    data.append(bi.find(itemprop='name').string)



#cityname = str(data[0])
#geolocator = Nominatim()
#print cityname, geolocator.geocode(cityname).longitude


class CityData():
    def __init__(self, htmlfile):
        self.soup = BeautifulSoup(open(htmlfile))

    def get_namepop(self):
        data_name = []
        data_pop = []
        extracted_soup = self.soup.find(id='citysection').find_all('tr', itemtype="http://schema.org/City") 

        for ai in extracted_soup:
            data_name.append(ai.find(itemprop='name').string + ' ' + ai.find_all('a')[1].string +' US')
            data_pop.append(ai.find('td', 'rpop prio1').string)
        return pd.DataFrame({'name':data_name, 'pop':data_pop})

    def get_namepop2(self):
        data_name = []
        data_pop = []
        extracted_state = self.soup.find_all('tbody', 'admin1') 
        extracted_city = self.soup.find_all('tbody', 'admin2')
        for cities, states in zip(extracted_city, extracted_state):
            x = cities.find_all('span')
            y = cities.find_all('td', 'rpop prio1') 
            z = states.find('span').string
            for city, pop in zip(x, y):
               # data_name.append(city.string +' '+ z + ' GERMANY')
                data_name.append(city.string) 
                data_pop.append(pop.string)
                
        df = pd.DataFrame({'name':data_name, 'pop':data_pop})
        return df


    def get_latlon(self):
        lat=[]
        lon=[]
        geolocator = Nominatim()
        name_seq = self.get_namepop()['name']
        
        for i, name in enumerate(name_seq):
            name = str(name)
            lat.append(geolocator.geocode(name).latitude)
            lon.append(geolocator.geocode(name).longitude)
            print i, name, lat[i], lon[i]
        return pd.DataFrame({'lat':lat, 'lon':lon})

    def get_latlon2(self):
        lat=[]
        lon=[]
        missed_point=[]
        geolocator = Nominatim()
        name_seq = self.get_namepop2()['name']
        
        Tokorozawa = geolocator.geocode('Tokorozawa')
        for i, name in enumerate(name_seq):
            #name = str(name)
            geocoded = geolocator.geocode(name)
            if type(geocoded) != type(Tokorozawa):
                lat.append('missed to get data')
                lon.append('missed to get data')
                print i, name, 'missed to get data'
                missed_point.append(i)
                continue
            #lat.append(geolocator.geocode(name).latitude)
            #lon.append(geolocator.geocode(name).longitude)
            lat.append(geocoded.latitude)
            lon.append(geocoded.longitude)

            print i, name, lat[i], lon[i]
        print 'missed points are ', missed_point
        return pd.DataFrame({'lat':lat, 'lon':lon})

    def concatenate(self):
         data = pd.concat([self.get_namepop(), self.get_latlon()], axis=1)
         data.to_csv('data.csv')
         
    def concatenate2(self):
         data_init = self.get_namepop2().to_csv('data_init.csv', encoding='utf-8')
         data = pd.concat([self.get_namepop2(), self.get_latlon2()], axis=1)
         data.to_csv('data_germany.csv', encoding='utf-8')

class GetLatLon():
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_csv(self.filename, index_col=0, encoding='utf-8')
        self.data_num = len(self.df.values[:, 1])

    def get_csv(self):
        geolocator = Nominatim(format_string='%s,France')
        name_list=[]
        pop_list=[]
        i_list=[]
        lat=[]         
        lon=[]         
        start = 231 #はじめは 0 スタート
        for i in range(start, self.data_num):
            name = self.df.iloc[i, 0]
            pop = self.df.iloc[i, 1]
            geocoded = geolocator.geocode(name)

            name_list.append(name)
            pop_list.append(pop)
            lat.append(geocoded.latitude)
            lon.append(geocoded.longitude)
            i_list.append(i)
            print i, name, pop, geocoded.latitude, geocoded.longitude
            df = pd.DataFrame({'':i_list, 'name':name_list, 'pop':pop_list, 'lat':lat, 'lon':lon},\
                                columns = ['', 'name', 'pop', 'lat', 'lon'],\
                                index = None)
            
            df.to_csv('hogehoge-%d.csv' %start, encoding='utf-8', index=None)
            

def main1():
    source = 'USA-Cities.html'
    citydata = CityData(source)
#    print citydata.get_namepop().values[0, 0]
#    print citydata.get_latlon()
    citydata.concatenate()

def main2():
    source = 'germany-admin.html'
    citydata = CityData(source)
    
    citydata.concatenate2()

def main3():
    filename = 'data_prim.csv'
    getlatlon = GetLatLon(filename)
    getlatlon.get_csv()

def main4():
    geolocator = Nominatim(format_string='%s,Czech Republic')
    name='Börde'
    name2='Oldenburg'
    name3='Altenkirchen'
    name4='Kitzbühel'
    name5='Salzburg'
    name6='Thomas, Nebraska'
    name7='Leeds and Grenville'
    name8='Jindřichův Hradec, Jihočeský kraj' 

    NAME = name8
    geocoded = geolocator.geocode(NAME, exactly_one=False)        
    geocoded_one = geolocator.geocode(NAME)        
    
    print geocoded_one.latitude, geocoded_one.longitude, '\n'
    for place in geocoded:
        print place.latitude, place.longitude, place.address

    

def stdout_utf():
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

if __name__ == '__main__':
    stdout_utf()
    main3()  





