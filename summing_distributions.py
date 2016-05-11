#coding: utf-8
import numpy as np
import pandas as pd
import sys
import codecs
import sakuzu
import subprocess


class SummingDist():
    def __init__(self, filename):
        self.input_file = filename
        self.df = pd.read_csv(self.input_file, encoding='utf-8')

    def dist_name(self):
        for i, aaa in enumerate(pd.Series(self.df.columns)):
            print aaa,'==', i
        
    def get_summing_dist(self, dist_num=[None]):
        df_sum = pd.DataFrame(np.zeros(self.df.values.shape[0]))
        df_sum.columns = ['sum']
        for num in dist_num:
            df_sum.iloc[:, 0] += self.df.iloc[:, num]

        return df_sum

            

def stdout_utf():
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

# 任意の分布を選び、重ね合わせる
def main1():
    #filename = 'moved_transformation_matrix_18.csv'
    filename = 'usa-pop-2014(17)/distribution.csv'
    draw_list = [8, 16, 22, 25, 26]
    figname = 'figure_sumed'
    #draw_list = range(288, 311, 2)

    summingdist = SummingDist(filename)
    summingdist.dist_name()
    pop = summingdist.get_summing_dist(draw_list)

    sakuzu.Drawing(pop, figname=figname, n=18).draw_all_noxy(teisuu=1.0)
    subprocess.call('eog "%s.png"' % figname , shell=True)
    
# 最も負の値が大きい人口が０となるように一様分布をたす
def main2():
    filename = 'idea/distribution.csv'
    df = SummingDist(filename).df
    for aaa in df.columns:
        #pop = df[aaa]
        #pop_new = pop - min(pop)
        df[aaa] = df[aaa] - min(df[aaa])
    df.to_csv('distribution_nominus.csv', encoding='utf-8', index=None)
    
        





if __name__ == '__main__':
    stdout_utf()
    main1()
