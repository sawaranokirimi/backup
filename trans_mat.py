#coding: utf-8

import pandas as pd
import numpy as np


class Default():
    def __init__(self, n, k=None, l=None, slide=[9, 9]):
        self.n = float(n)
        self.k = k
        self.l = l
        self.slide = slide

    def vector(self, q):              
        # slide[0]がx方向の平行移動、slide[1]がy方向の平行移動
        data = []                     
        for n2 in range(int(self.n)):      
            n2 += -self.slide[1]
            for n1 in range(int(self.n)):  
                n1 += -self.slide[0]
                data.append(q(n1, n2))
                                      
        return pd.DataFrame(data)     

class Q1flat(Default):
    def __init__(self, n):
        Default.__init__(self, n)

    def q_1(self, n1, n2):                                 
        return 1.0/self.n
                                                           
    def get_Q(self):                                       
        df = pd.DataFrame()                                
        for func in [self.q_1]:                  
            df = pd.concat([df, self.vector(func)], axis=1)
                                                           
        df.columns = range(1)                              
        return df                                          



class Q2even(Default):
    def __init__(self, n):
        Default.__init__(self, n)
        
    def q_1(self, n1, n2):
        return np.cos(2.*np.pi*(n1 - 2.*n2)/3.)
    def q_2(self, n1, n2):
        return np.sin(2.*np.pi*(n1 - 2.*n2)/3.)

    def get_Q(self):
        df = pd.DataFrame()
        for func in [self.q_1, self.q_2]:
            df = pd.concat([df, self.vector(func)], axis=1)
            
        df.columns = range(2)
        return df

class Q3even(Default):
    def __init__(self, n):
       Default.__init__(self, n)
        
    def q_1(self, n1, n2):
        return np.cos(np.pi*n1)
    def q_2(self, n1, n2):
        return np.cos(np.pi*n2)
    def q_3(self, n1, n2):
        return np.cos(np.pi*(n1-n2))

    def get_Q(self):
        df = pd.DataFrame()
        for func in [self.q_1, self.q_2, self.q_3]:
            df = pd.concat([df, self.vector(func)], axis=1)
            
        df.columns = range(3)
        return df

class Q6k0(Default):
    def __init__(self, n, k):
       Default.__init__(self, n, k)
        
    def q_1(self, n1, n2):
        return np.cos(2.*np.pi*self.k*n1/self.n)
    def q_2(self, n1, n2):
        return np.sin(2.*np.pi*self.k*n1/self.n)
    def q_3(self, n1, n2):
        return np.cos(2.*np.pi*self.k*(-n2)/self.n)
    def q_4(self, n1, n2):                          
        return np.sin(2.*np.pi*self.k*(-n2)/self.n) 
    def q_5(self, n1, n2):                           
        return np.cos(2.*np.pi*self.k*(-n1+n2)/self.n)  
    def q_6(self, n1, n2):                           
        return np.sin(2.*np.pi*self.k*(-n1+n2)/self.n)  

    def get_Q(self):
        df = pd.DataFrame()
        for func in [self.q_1, self.q_2, self.q_3, self.q_4, self.q_5, self.q_6]:
            df = pd.concat([df, self.vector(func)], axis=1)
            
        df.columns = range(6)
        return df

class Q6kk(Default):
    def __init__(self, n, k):
       Default.__init__(self, n, k)
        
    def q_1(self, n1, n2):
        return np.cos(2.*np.pi*self.k*(n1+n2)/self.n)
    def q_2(self, n1, n2):
        return np.sin(2.*np.pi*self.k*(n1+n2)/self.n)
    def q_3(self, n1, n2):
        return np.cos(2.*np.pi*self.k*(n1-2.*n2)/self.n)
    def q_4(self, n1, n2):                          
        return np.sin(2.*np.pi*self.k*(n1-2.*n2)/self.n) 
    def q_5(self, n1, n2):                           
        return np.cos(2.*np.pi*self.k*(-2.*n1+n2)/self.n)  
    def q_6(self, n1, n2):                           
        return np.sin(2.*np.pi*self.k*(-2.*n1+n2)/self.n)  

    def get_Q(self):
        df = pd.DataFrame()
        for func in [self.q_1, self.q_2, self.q_3, self.q_4, self.q_5, self.q_6]:
            df = pd.concat([df, self.vector(func)], axis=1)
            
        df.columns = range(6)
        return df

class Q12kl(Default):
    def __init__(self, n, k, l):
        Default.__init__(self, n, k, l)

    def q_1(self, n1, n2):
        return np.cos(2.*np.pi*(self.k*n1 + self.l*n2)/self.n)
    def q_2(self, n1, n2):
        return np.sin(2.*np.pi*(self.k*n1 + self.l*n2)/self.n)
    def q_3(self, n1, n2):
        return np.cos(2.*np.pi*(self.l*n1 - (self.k+self.l)*n2)/self.n)
    def q_4(self, n1, n2):
        return np.sin(2.*np.pi*(self.l*n1 - (self.k+self.l)*n2)/self.n)
    def q_5(self, n1, n2):
        return np.cos(2.*np.pi*(-(self.k+self.l)*n1 + self.k*n2)/self.n)
    def q_6(self, n1, n2):
        return np.sin(2.*np.pi*(-(self.k+self.l)*n1 + self.k*n2)/self.n)
    def q_7(self, n1, n2):
        return np.cos(2.*np.pi*(self.k*n1 - (self.k+self.l)*n2)/self.n)
    def q_8(self, n1, n2):
        return np.sin(2.*np.pi*(self.k*n1 - (self.k+self.l)*n2)/self.n)
    def q_9(self, n1, n2):
        return np.cos(2.*np.pi*(self.l*n1 + self.k*n2)/self.n)
    def q_10(self, n1, n2):
        return np.sin(2.*np.pi*(self.l*n1 + self.k*n2)/self.n)
    def q_11(self, n1, n2):
        return np.cos(2.*np.pi*(-(self.k+self.l)*n1 + self.l*n2)/self.n)
    def q_12(self, n1, n2):
        return np.sin(2.*np.pi*(-(self.k+self.l)*n1 + self.l*n2)/self.n)

    def get_Q(self):
        df = pd.DataFrame()
        for func in [self.q_1, self.q_2, self.q_3, self.q_4, self.q_5, 
                     self.q_6, self.q_7, self.q_8, self.q_9, self.q_10, 
                     self.q_11, self.q_12]:

            df = pd.concat([df, self.vector(func)], axis=1)
            
        df.columns = range(12)
        return df
    
def connect_to_Q(n, k, l, slide=[None]):
    if l == 0:
        return Q6k0(n, k).get_Q()
    elif k == l:
        return Q6kk(n, k).get_Q()
    else :
        return Q12kl(n, k, l).get_Q()

def main1():
    n =18
    df = pd.DataFrame()
    df = pd.concat([df, Q1flat(n).get_Q(), 
                    Q2even(n).get_Q(), Q3even(n).get_Q()], axis=1)
    data_kl = pd.read_csv('hexagon_18.csv').values
    col = ['1_1', '3_1', '3_2', '4_1', '4_2', '4_3']

    for kl in data_kl:
        Q = connect_to_Q(n, kl[1], kl[2])
        df = pd.concat([df, Q], axis=1)
        for i in range(1, Q.values.shape[1] + 1):
            col.append(str(kl[0])+'_'+str(i))
    df.columns = col
    print df
    df.to_csv('transformation_matrix_18.csv', index=None)

    
def main_moved_tmat():
    n =18
    df = pd.DataFrame()
    df = pd.concat([df, Q1flat(n).get_Q(), 
                    Q2even(n).get_Q(), Q3even(n).get_Q()], axis=1)
    data_kl = pd.read_csv('hexagon_18.csv').values
    col = ['1_1', '3_1', '3_2', '4_1', '4_2', '4_3']

    for kl in data_kl:
        Q = connect_to_Q(n, kl[1], kl[2])
        df = pd.concat([df, Q], axis=1)
        for i in range(1, Q.values.shape[1] + 1):
            col.append(str(kl[0])+'_'+str(i))
    df.columns = col
    print df
    df.to_csv('moved_transformation_matrix_18.csv', index=None)



if __name__ == '__main__':
    main_moved_tmat()
    #main1()
