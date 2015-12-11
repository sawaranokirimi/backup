#coding: utf-8
import subprocess


def main1(folder):
    data = ['data_gathered.csv', 'data_memo.txt', 'data_projected.csv', \
            'distribution.csv', 'naiseki.csv', 'norm.csv', \
            'graph_norm*', 'figure*', 'm=*']

    for aaa in data:
        subprocess.call('mv %s %s' %(aaa, folder), shell=True)



if __name__ == '__main__':
    #folder_name = raw_input()
    #print '%s is written' % folder_name
    folder_name = 'idea_nominus'
    main1(folder_name)
