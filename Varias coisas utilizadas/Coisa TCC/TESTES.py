from pandas import read_csv
import pandas as pd
import numpy as np
import csv
import datetime
from datetime import datetime
import holidays
'''
weekno = datetime.datetime.today().weekday()

if weekno < 5:
    print "Weekday"
else:  # 5 Sat, 6 Sun
    print "Weekend"
'''
def is_weekend(d = datetime.today()):
    if (d.weekday() in (5, 6)) or (d in us_holidays):
        return 1
    else:
        return 0

us_holidays = holidays.UnitedStates()


SEED =  19963
# load data
perg = ['OwnerUserId','CreationDate','Ntags','TemCodigo','CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Minutos']

print('Começou...')
Perguntas=pd.read_csv('C:\\Users\\joaor\\Desktop\\Databases\\DataFramePerg.csv',sep='\t',usecols=perg)
Perguntas=Perguntas.loc[(Perguntas.Minutos >= -1)]
Perguntas=Perguntas.dropna()
print('Acabou...')

i=0
result=[]
for x in Perguntas['CreationDate']:
    #if (x.CreationDate, format="%Y-%m-%d %H:%M:%S") in us_holidays:
    #print(Perguntas['CreationDate'][x])
    #if pd.to_datetime(Perguntas['CreationDate'][x], format="%Y-%m-%d %H:%M:%S") in us_holidays:
    #    print('------------------------------------------------------Feriado')
    #if is_weekend(pd.to_datetime(Perguntas['CreationDate'][x], format="%Y-%m-%d %H:%M:%S")):
    #    print('Feriado----------------------------------------Final de semana')
    result.append(is_weekend(pd.to_datetime(x, format="%Y-%m-%d %H:%M:%S")))
    #Perguntas.loc[5,'FeriadoFinSem'] = is_weekend(pd.to_datetime(Perguntas['CreationDate'][x], format="%Y-%m-%d %H:%M:%S"))
    if i%500 == 0:
        print('Post: ',i,end='')
    i+=1

    print('\r\r\r',end='')

Perguntas['Feriado'] = result

print(Perguntas.head())

'''
Perguntas=Perguntas.loc[pd.to_datetime(Perguntas.CreationDate, format="%Y-%m-%d %H:%M:%S") > datetime.strptime('2015-12-31 23:59:59', "%Y-%m-%d %H:%M:%S")]
dataframe.to_csv('C:\\Users\\joaor\\Desktop\\Databases\\XX.csv', sep='\t', encoding='utf-8')
'''
#Lê o arquivo seque, que
