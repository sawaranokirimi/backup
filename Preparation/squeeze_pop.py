#coding: utf-8
import pandas as pd
import sys
import codecs
import re

# []を置き換える
def replace(sentence):
    pattern = re.compile('\[.*\]')
    x = ''
    return pattern.sub(x, sentence) 


def main1():
    filename = 'population.csv'
    column_num = 5 #年数のcolumn
    
    pop = pd.read_csv(filename, encoding='utf-8')
    print '===columns===\n', pd.Series(pop.columns), '\n'
    df = pop.iloc[:, [1, 2, column_num]]
    
    data_name = []
    data_pop = []
    for name, status, population in df.values:
        name = replace(name)
        status = replace(status)
        if status == 'Province (Oblast)':
            state_temp = name
            print '===== %s, %s ===== ' %(status, name)
        else :
            name = '%s, %s' %(name, state_temp)
            data_name.append(name)
            data_pop.append(population)
            print name
    
    df = pd.DataFrame({'name':data_name, 'pop':data_pop}, \
                       columns=['name', 'pop'])
    df.index = range(len(data_name))
    df.to_csv('data_prim.csv', encoding='utf-8')
    #name = df.iloc[:, 0]
    #pop = df.iloc[:, 5]
    #df = pd.DataFrame({'name':name, 'pop':pop}, columns=['name', 'pop'])
    #df.index = range(len(name))
    #df.to_csv('data.csv', encoding='utf-8')

def stdout_utf():
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)


if __name__ == '__main__':
    stdout_utf()
    main1()





