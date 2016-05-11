#coding: utf-8
import subprocess
import re


def main1(folder):
    data = ['data_gathered.csv', 'data_memo.txt', 'data_projected.csv', \
            'distribution.csv', 'naiseki.csv', 'norm.csv', \
            'graph_norm*', 'figure*', 'm=*', 'data_rooped.csv', 'data_lt_rb.csv']

    for aaa in data:
        subprocess.call('mv %s %s' %(aaa, folder), shell=True)

class Boukennosyo():
    def __init__(self):
        self.f = open('.boukennosyo.txt', "r+")

    def ex_filename(self):
        fname_old = self.f.read()
        return fname_old.rstrip()

    def new_filename(self):
        f = self.ex_filename()
        pattern = re.compile('\(\d+\)')
        pattern2 = re.compile('\d+')
        name = pattern.findall(f)
        print name
        if len(name) == 0:
            return f
        else:
            number = pattern2.findall(name[0])
            f = f.replace(name[0], '('+str(int(number[0])+1)+')')
            return f.rstrip()

    def hozon(self, name):
        folder_name = name
        L = []
        for moji in folder_name:
            if moji == '(' or moji == ')':
                moji = '\\' + moji
            L.append(moji)
        for_shell_name = "".join(L)
        subprocess.call('mkdir %s' %for_shell_name, shell=True)
        main1(for_shell_name)
        self.f.close()
        f = open('.boukennosyo.txt', "w+")
        f.write(folder_name)
        f.close()


if __name__ == '__main__':
    #folder_name = raw_input()
    #print '%s is written' % folder_name

    folder_name = 'south_germany-pop-2011\(16\)'
    subprocess.call('mkdir %s' %folder_name, shell=True)
    main1(folder_name)
