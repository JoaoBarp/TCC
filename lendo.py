from pandas import read_csv
import pandas as pd
import numpy as np
import csv



mydict={}
with open('valores.csv','r') as csv_file:
    for line in csv.reader(csv_file):
        if line:
            #print(line[0])
            mydict[line[0]] = line[1]

for key, value in mydict.items():
    print('-------------------------------------------------------')
    print(key)
    print('-------------------------------------------------------')
    print(value)
    print('-------------------------------------------------------')
    print('.')
    print('.')
    print('.')
