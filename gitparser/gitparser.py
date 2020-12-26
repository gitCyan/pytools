#!/usr/bin/python
# encoding = utf-8

__author__ = 'cuiyue'

import os
from datetime import datetime
import re
import sys
from matplotlib import pyplot as plt

def tstr2tstamp(strin, i):
    try:
        dt = datetime.strptime(strin.strip(' '), '%Y-%m-%d %H:%M:%S').date()
        return dt
    except:
        return None

def gitparser():
    #get commit log.
    cmd = 'git lg ./'
    strf = os.popen(cmd)
    stro = strf.read()
    strf.close()
    listo = stro.split('\n')
    #convert log to dict.
    logdict = {'hash':[], 'time':[], 'name':[], 'log':[], 'ts':[]}
    pat = '.*?34m([0-9a-z]+) .*?32m([^\+]+)\+0800.*?31m([a-z]+)[^ ]* (.*)'
    for i in range(len(listo)):
        mat = re.match(pat, listo[i])
        if mat != None:
            dt = tstr2tstamp(mat.group(2), i)
            if dt == None: 
                print('null date!(%s)' % listo[i])
                continue
            logdict['ts'  ].append(dt)
            logdict['hash'].append(mat.group(1))
            logdict['time'].append(mat.group(2))
            logdict['name'].append(mat.group(3))
            logdict['log' ].append(mat.group(4))
        else:
            print('null match!(%s)' % listo[i])
    #stats each day commits:
    list1 = list(set(logdict['ts']))
    list1.sort()
    list2, list3, sname = [], [], ''
    if len(sys.argv) > 1: sname = sys.argv[1]
    for i in list1:
        list2.append(logdict['ts'].count(i))
        cnt = 0
        for j in range(len(logdict['ts'])):
            if logdict['ts'][j] == i and logdict['name'][j] == sname: cnt += 1
        list3.append(cnt)
    print(list2)
    print(list3)
    #Draw:
    plt.figure(1)
    plt.title('show')
    plt.plot(list1, list2, 'o-', label='team')
    plt.legend(loc='best')
    plt.xlabel('Time')
    plt.ylabel('Commits')
    if len(sys.argv) > 1: plt.plot(list1, list3, 'ro--', label=sname)
    plt.legend(loc='best')
    plt.gcf().autofmt_xdate()
    plt.show()

def main():
    gitparser()

if __name__ == '__main__':
    main()
