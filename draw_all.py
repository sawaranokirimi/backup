#coding: utf-8
import pandas as pd
import numpy as np
import sys
import sakuzu
import sys
import codecs


def main1():
    df = pd.read_csv('distribution.csv', encoding='utf-8')
    column_num = df.values.shape[1]
    city_num =  df.values.shape[0]

    xy = np.zeros([city_num, 2])
    file_names = ['1', '3', '4', '9', '12', '27-1', '27-2', '27-3', \
                  '36-1', '36-2', '81-1', '81-2', '81-3', '81-4', '81-5', '81-6', \
                  '108-1', '108-2', '108-3', '108-4', '108-5', '108-6', \
                  '324-1', '324-2', '324-3', '324-4', '324-5', '324-6', \
                  '324-7', '324-8', '324-9', '324-10', '324-11', '324-12', \
                  '324-13', '324-14', '324-15']  

    number = 0
    for i in range(int(np.sqrt(city_num))):
        for j in range(int(np.sqrt(city_num))):
            xy[number, 0] = j
            xy[number, 1] = i
            number += 1

    for i in range(column_num):
        #name = 'm=' + df.columns[i] 
        #name = (u'%s' % name)
        name = 'm=' + file_names[i]
        pop = pd.concat([pd.DataFrame(xy), df.iloc[:, i]], axis=1)  
        #sakuzu.Drawing(pop, name, n=18).draw_all()
        sakuzu.Drawing(pop, name, n=18).draw_all_BY(teisuu=1.0)


if __name__ == '__main__':
    main1()
