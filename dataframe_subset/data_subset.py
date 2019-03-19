#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def subset():
    list=[]
    for data2_idx in data2.index:
        flag = 1
        for data1_idx in data1.index:
            if (data2.iloc[data2_idx]==data1.iloc[data1_idx]).all():
                flag = 0
                break
        if flag == 1:
            list.append(data2_idx)
    
    return list


if __name__=='__main__':

    data1=pd.read_csv('data/test1.csv')
    data2=pd.read_csv('data/test2.csv')

    # data2-data1
    data_subset=data2.iloc[subset()]

    print('             < Data1>')
    print(data1)
    print()
    print('             < Data2>')
    print(data2)
    print()
    print('         <Data2 - Data1>')
    print(data_subset)

