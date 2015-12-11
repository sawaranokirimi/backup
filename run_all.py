#coding:utf-8
import pandas as pd
from making_map import Ploting
from set_to_grid import Lines 
from parallelogram import Parallel
import sakuzu


def main1():
   file_name = 'usa-pop-2014(1)/usa-pop-2014.csv'
   memo = 'data_memo.txt'
   ploting = Ploting(file_name)
   ploting.convert()
   ploting.make_fig()
   ploting.scatter(teisuu=1000.)

   data = pd.read_csv('data_projected.csv').values
   print 'lt', ploting.lt
   print 'rb', ploting.rb

   # BostonからPhiladelphiaまでの試し
#   ploting.lt = [1.07548*10**7, 1.90071*10**7]
#   ploting.rb = [1.1386*10**7, 1.94851*10**7]
   # 南ドイツの試し
   #ploting.lt = [20202313., 21429402.]
   #ploting.rb = [20102759., 20231413.]

   lt_input = [19619687, 20778206] 
   rb_input = [20161100, 20178900]
   #ploting.lt = lt_input_obli
   #ploting.rb = rb_input_obli

   lines = Lines(data, ploting.lt, ploting.rb)
   print 'included points are ', lines.include_point()
   lines.gather().to_csv('data_gathered.csv', index=False)
   
   f = open(memo, 'w')
   l = lines.lattice_size()/1000.
   f.write('size %d km\n' % l)
   f.write('lt= (%d, %d)\nrb= (%d, %d)' %(ploting.lt[0], ploting.lt[1], \
                                         ploting.rb[0], ploting.rb[1]))
   f.close()
   
   draw = sakuzu.Drawing(lines.gather()).draw_all(teisuu=2000)

if __name__ == '__main__':
    main1()      
