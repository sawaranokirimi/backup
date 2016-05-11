#coding:utf-8
import pandas as pd
from making_map import Ploting
from set_to_grid import Lines 
from parallelogram import Parallel
import sakuzu
import os


def main1():
   file_name = 'usa_canada-pop-2014/usa_canada-pop-2014.csv'
   file_name2 = 'czech-pop-2014/czech-pop-2014.csv'
   file_name3 = 'south_germany-pop-2011/south_germany-pop-2011.csv'
   memo = 'data_memo.txt'
   ploting = Ploting(file_name3)
   ploting.convert()
   ploting.make_fig()
   if os.path.isfile('/home/kdaichi/Workspace/Pywork/data_lt_rb.csv') == True:
       ploting.callback_parallel(toumeido=0.25, grid=False, face=False, rireki=True)
   ploting.scatter(teisuu=4000.)

   data = pd.read_csv('data_projected.csv').values
   print 'lt', ploting.lt
   print 'rb', ploting.rb

   # BostonからPhiladelphiaまでの試し
#   ploting.lt = [1.07548*10**7, 1.90071*10**7]
#   ploting.rb = [1.1386*10**7, 1.94851*10**7]
   # 南ドイツの試し
   #ploting.lt = [20202313., 21429402.]
   #ploting.rb = [20102759., 20231413.]

   lt_input= [19443701.725, 20818665.35]  
   rb_input= [20283251.275, 20164668.65]

   #ploting.lt = lt_input
   #ploting.rb = rb_input

   lines = Lines(data, ploting.lt, ploting.rb)
   print 'included points are ', lines.include_point()
   lines.gather().to_csv('data_gathered.csv', index=False)
   
   f = open(memo, 'w')
   l = lines.lattice_size()/1000.
   f.write('size %d km\n' % l)
   f.write('lt= (%d, %d)\nrb= (%d, %d)' %(ploting.lt[0], ploting.lt[1], \
                                         ploting.rb[0], ploting.rb[1]))
   lt_rb = pd.DataFrame([[ploting.lt[0], ploting.lt[1]],\
                         [ploting.rb[0], ploting.rb[1]]],\
                          columns=['x','y'], index = ['lt', 'rb'])
   lt_rb.to_csv('data_lt_rb.csv')
   f.close()
   
   draw = sakuzu.Drawing(lines.gather()).draw_all(teisuu=2000)

def max_of_rooped():
   file_name = 'usa_canada-pop-2014/usa_canada-pop-2014.csv'
   file_name2 = 'czech-pop-2014/czech-pop-2014.csv'
   file_name3 = 'south_germany-pop-2011/south_germany-pop-2011.csv'
   memo = 'data_memo.txt'

   ploting = Ploting(file_name3)
   ploting.convert()
   ploting.make_fig()
   ploting.scatter(teisuu=4000.)

   data = pd.read_csv('data_projected.csv').values

   df = pd.read_csv('data_rooped.csv', index_col=0)
   lt= [df.ix[0,0], df.ix[0,1]]
   rb= [df.ix[0,2], df.ix[0,3]]

   ploting.lt = lt
   ploting.rb = rb

   lines = Lines(data, ploting.lt, ploting.rb)
   lines.gather().to_csv('data_gathered.csv', index=False)
   
   f = open(memo, 'w')
   l = lines.lattice_size()/1000.
   f.write('size %d km\n' % l)
   f.write('lt= (%d, %d)\nrb= (%d, %d)' %(ploting.lt[0], ploting.lt[1], \
                                         ploting.rb[0], ploting.rb[1]))
   lt_rb = pd.DataFrame([[ploting.lt[0], ploting.lt[1]],\
                         [ploting.rb[0], ploting.rb[1]]],\
                          columns=['x','y'], index = ['lt', 'rb'])
   lt_rb.to_csv('data_lt_rb.csv')
   f.close()

   draw = sakuzu.Drawing(lines.gather()).draw_all(teisuu=2000)


if __name__ == '__main__':
   main1()      
   #max_of_rooped()
