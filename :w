from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import pandas as pd

soup = BeautifulSoup(open('USA-Cities.html'))
b = soup.find(id='citysection').find_all('tr', itemtype="http://schema.org/City")  
data = []

for bi in b:
   # print bi.find(itemprop='name').string, bi.find('td', 'rpop prio1').string
    data.append(bi.find(itemprop='name').string)



cityname = str(data[0])
geolocator = Nominatim()
print cityname, geolocator.geocode(cityname).longitude


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

    def concatenate(self):
         data = pd.concat([self.get_namepop(), self.get_latlon()], axis=1)
         data.to_csv('data.csv')

def main1():
    source = 'USA-Cities.html'
    citydata = CityData(source)
#    print citydata.get_namepop().values[0, 0]
#    print citydata.get_latlon()
    citydata.concatenate()
if __name__ == '__main__':

    main1()
