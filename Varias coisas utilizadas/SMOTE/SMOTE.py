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
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE


sm = SMOTE(random_state=42,n_jobs=6)

scaler = MinMaxScaler()


SEED =  19963
perg = ['OwnerUserId','CreationDate','Ntags','TemCodigo','CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Minutos']

print('Começou...')
Perguntas=pd.read_csv('C:\\Users\\joaor\\Desktop\\Databases\\DataFramePerg.csv',sep='\t',usecols=perg, encoding='utf-8')
Perguntas=Perguntas.loc[(Perguntas.Minutos >= -1)]
print('Acabou...')



Perguntas.loc[(Perguntas.Minutos >= 0) & (Perguntas.Minutos <= 1440),'Rotulo'] = 1
Perguntas.loc[(Perguntas.Minutos >1440) | (Perguntas.Minutos == -1),'Rotulo'] = 2

Perguntas=Perguntas.dropna()

Perguntas = Perguntas.drop(columns=['OwnerUserId'])
Perguntas = Perguntas.drop(columns=['Ntags'])
Perguntas = Perguntas.drop(columns=['TemCodigo'])
Perguntas = Perguntas.drop(columns=['Minutos'])
Perguntas = Perguntas.drop(columns=['CreationDate'])

#x_train, x_test, y_train, y_test = train_test_split(Perguntas.drop(columns=['Rotulo']),Perguntas['Rotulo'],test_size=0.999,random_state=SEED)

#x_test['Rotulo'] =  y_test

perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']
Perguntas.columns=perg2

print(Perguntas.isnull().sum())
check_for_nan = Perguntas.isnull().values.any()
print (check_for_nan)

total_nan_values = Perguntas.isnull().sum().sum()
print (total_nan_values)

X=Perguntas.drop(columns=['Rotulo'])
y=Perguntas['Rotulo']


X_res, y_res = sm.fit_resample(X,y)
X_res['Rotulo'] =  y_res

#x_test[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']] = scaler.fit_transform(x_test[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']])
df1 = X_res.groupby(['Rotulo']).size()/ len(X_res)
df1 = df1.reset_index(name = 'Porcentagem')
print('\n\n Distribuição')
print(df1.to_string(index=False))
#df.groupby(['Fruit','Name'])['Number'].sum().reset_index()

df2 = X_res.groupby(['Rotulo']).size()
df2 = df2.reset_index(name = 'Soma')

print('\n\n Distribuição')
print(df2.to_string(index=False))

X_res = X_res[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']]
print(X_res.head())
X_res.to_csv('C:\\Users\\joaor\\Desktop\\SMOTE.csv', sep='\t', encoding='utf-8')
