# -*- coding: utf-8 -*-
from collections import defaultdict
from matplotlib import pyplot as plt
import xml.etree.ElementTree
import pandas as pd
from datetime import datetime, timedelta
import time
import re, cgi, os, pickle, logging, time
from textblob import TextBlob
#import language_check
import textstat
from collections import Counter
import sys
import csv
import json
from collections import Counter
import numpy as np
from xml.etree.ElementTree import iterparse
from lxml import etree
import psutil
import statistics
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
import holidays
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report
from scipy import stats

scaler = MinMaxScaler()


def is_weekend(d = datetime.today()):
    if (d.weekday() in (5, 6)) or (d in us_holidays):
        return 1
    else:
        return 0

us_holidays = holidays.UnitedStates()


SEED =  19963
perg = ['OwnerUserId','CreationDate','Ntags','TemCodigo','CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Minutos']

print('Começou...')
Perguntas=pd.read_csv('C:\\Users\\joaor\\Desktop\\Databases\\DataFramePerg.csv',sep='\t',usecols=perg)
Perguntas=Perguntas.loc[(Perguntas.Minutos >= -1)]
#print(type(datetime.strptime(Perguntas.CreationDate, "%Y-%m-%d %H:%M:%S")))
#Perguntas=Perguntas.loc[pd.to_datetime(Perguntas.CreationDate, format="%Y-%m-%d %H:%M:%S") > datetime.strptime('2015-12-31 23:59:59', "%Y-%m-%d %H:%M:%S")]
Perguntas=Perguntas.dropna()
print('Acabou...')
#datetime.strptime('2015-12-31 23:59:59', "%Y-%m-%d %H:%M:%S")
#print(Perguntas.head())

'''
Perguntas.loc[(Perguntas.Minutos >= 0) & (Perguntas.Minutos <= 480),'Rotulo'] = 1
Perguntas.loc[(Perguntas.Minutos > 480) & (Perguntas.Minutos <= 960),'Rotulo'] = 2
Perguntas.loc[(Perguntas.Minutos > 960) & (Perguntas.Minutos <= 1440),'Rotulo'] = 3
Perguntas.loc[(Perguntas.Minutos > 1440) & (Perguntas.Minutos < 2280),'Rotulo'] = 4
Perguntas.loc[(Perguntas.Minutos > 2280) & (Perguntas.Minutos <= 5790),'Rotulo'] = 5
Perguntas.loc[(Perguntas.Minutos > 5790),'Rotulo'] = 6
Perguntas.loc[(Perguntas.Minutos == -1) ,'Rotulo'] = 7
'''


Perguntas.loc[(Perguntas.Minutos >= 0) & (Perguntas.Minutos <= 1440),'Rotulo'] = 1
Perguntas.loc[(Perguntas.Minutos >1440) | (Perguntas.Minutos == -1),'Rotulo'] = 2


#Perguntas=Perguntas[(Perguntas.Minutos > 1440) | (Perguntas.Minutos == -1)]
#Perguntas.loc[(Perguntas.Minutos >= 0) & (Perguntas.Minutos <= 1440),'Rotulo'] = 0
#Perguntas.loc[(Perguntas.Minutos > 1440) | (Perguntas.Minutos == -1),'Rotulo'] = 1
#Perguntas.loc[(Perguntas.Minutos == -1) ,'Rotulo'] = 2


Perguntas = Perguntas.drop(columns=['OwnerUserId'])
Perguntas = Perguntas.drop(columns=['Ntags'])
Perguntas = Perguntas.drop(columns=['TemCodigo'])
Perguntas = Perguntas.drop(columns=['Minutos'])
Perguntas = Perguntas.drop(columns=['CreationDate'])

x_train, x_test, y_train, y_test = train_test_split(Perguntas.drop(columns=['Rotulo']),Perguntas['Rotulo'],test_size=0.999,random_state=SEED)

x_test['Rotulo'] =  y_test

perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']
x_test.columns=perg2
'''
result=[]
i=0
for x in x_test['CreationDate']:
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

x_test['Feriado/FimSem'] = result'''
#x_test = x_test.drop(columns=['CreationDate'])

'''
print(len(x_test.index))
x_test = x_test[(np.abs(stats.zscore(x_test)) < 3).all(axis=1)]
print(len(x_test.index))
'''

#x_test[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']] = scaler.fit_transform(x_test[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']])
df1 = x_test.groupby(['Rotulo']).size()/ len(x_test)
df1 = df1.reset_index(name = 'Porcentagem')
print('\n\n Distribuição')
print(df1.to_string(index=False))
#df.groupby(['Fruit','Name'])['Number'].sum().reset_index()

df2 = x_test.groupby(['Rotulo']).size()
df2 = df2.reset_index(name = 'Soma')

print('\n\n Distribuição')
print(df2.to_string(index=False))

x_test = x_test[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']]
print(x_test.head())
x_test.to_csv('C:\\Users\\joaor\\Desktop\\2classesFF.csv', sep='\t', encoding='utf-8')
