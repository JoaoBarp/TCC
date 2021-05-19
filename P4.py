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

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report

scaler = MinMaxScaler()

SEED =  19963
perg = ['OwnerUserId','CreationDate','Ntags','TemCodigo','CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Minutos']

print('Começou...')
Perguntas=pd.read_csv('C:\\Users\\joaor\\Desktop\\Databases\\DataFramePerg.csv',sep='\t',usecols=perg)
Perguntas=Perguntas.loc[(Perguntas.Minutos >= -1)]
print('Acabou...')


'''
Perguntas.loc[(Perguntas.Minutos >= 0) & (Perguntas.Minutos <= 480),'Rotulo'] = 'C1'
Perguntas.loc[(Perguntas.Minutos > 480) & (Perguntas.Minutos <= 960),'Rotulo'] = 'C2'
Perguntas.loc[(Perguntas.Minutos > 960) & (Perguntas.Minutos <= 1440),'Rotulo'] = 'C3'
Perguntas.loc[(Perguntas.Minutos > 1440) & (Perguntas.Minutos < 2280),'Rotulo'] = 'C4'
Perguntas.loc[(Perguntas.Minutos > 2280) & (Perguntas.Minutos <= 5790),'Rotulo'] = 'C5'
Perguntas.loc[(Perguntas.Minutos > 5790),'Rotulo'] = 'C6'
Perguntas.loc[(Perguntas.Minutos == -1) ,'Rotulo'] = 'C7'
'''

Perguntas.loc[(Perguntas.Minutos >= 0) & (Perguntas.Minutos <= 960),'Rotulo'] = 1
Perguntas.loc[(Perguntas.Minutos > 960) & (Perguntas.Minutos <= 2280),'Rotulo'] = 2
Perguntas.loc[(Perguntas.Minutos > 2280) & (Perguntas.Minutos <= 5790),'Rotulo'] = 3
Perguntas.loc[(Perguntas.Minutos > 5790),'Rotulo'] = 4
Perguntas.loc[(Perguntas.Minutos == -1) ,'Rotulo'] = 5





Perguntas = Perguntas.drop(columns=['OwnerUserId'])
Perguntas = Perguntas.drop(columns=['CreationDate'])
Perguntas = Perguntas.drop(columns=['Ntags'])
Perguntas = Perguntas.drop(columns=['TemCodigo'])
Perguntas = Perguntas.drop(columns=['Minutos'])

x_train, x_test, y_train, y_test = train_test_split(Perguntas.drop(columns=['Rotulo']),Perguntas['Rotulo'],test_size=0.3,random_state=SEED)

x_test['Rotulo'] =  y_test

perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']
x_test.columns=perg2

print(x_test.head())


x_test[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']] = scaler.fit_transform(x_test[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']])

x_test['N de tags'] = x_test['N de tags']*2
x_test['N Palavras corpo'] = x_test['N Palavras corpo']*2

print(x_test.head())



x_test.to_csv('C:\\Users\\joaor\\Desktop\\Databases\\Data5class.csv', sep='\t', encoding='utf-8')
