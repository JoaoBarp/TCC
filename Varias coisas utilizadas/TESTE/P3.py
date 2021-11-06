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


perg = ['OwnerUserId','CreationDate','Ntags','TemCodigo','CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Minutos']

print('Começou...')
Perguntas=pd.read_csv('DataFramePerg.csv',sep='\t',usecols=perg)
Perguntas=Perguntas.loc[(Perguntas.Minutos >= -1)]
print('Acabou...')
#Perguntas = Perguntas.transpose()
#Perguntas.columns = perg
#print(Perguntas.head())

count_row = Perguntas.shape[0]  # Gives number of rows
count_col = Perguntas.shape[1]  # Gives number of columns
print('Rows',count_row)
#print('Columns',count_col)
#print(Perguntas['Minutos'])
#print(Perguntas['Minutos'].loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos < 1024)])
#print(Perguntas['Minutos'].loc[Perguntas.Minutos < 0])


#y=np.delete(np.array(Perguntas['Minutos']), -1)
#print(pd.cut(Perguntas['Minutos'].loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos <= 1024)],3))

#Perguntas.loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos <= 1024),'Rotulo']=pd.cut(Perguntas['Minutos'].loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos <= 1024)],3,labels=["Super Rapido", "Muito Rapido", "Rapido"])
#Perguntas.loc[Perguntas.Minutos > 1024,'Rotulo']=pd.cut(Perguntas['Minutos'].loc[Perguntas.Minutos > 1024],3,labels=["Medio", "Lento", "Mt Lento"])
#Perguntas.loc[Perguntas.Minutos == -1,'Rotulo']="Sem Resp"
#Perguntas['Rotulo']=pd.qcut(Perguntas['Minutos'].loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos <= 1024)],3)
#print(Perguntas)

z=Perguntas['Minutos'].loc[(Perguntas.Minutos >= 0) & (Perguntas.Minutos < 1440)].count()
#print('Rows z',z)

x=Perguntas['Minutos'].loc[(Perguntas.Minutos >= 1440) & (Perguntas.Minutos < 10080)].count()
#print('Rows x',x)

y=Perguntas['Minutos'].loc[(Perguntas.Minutos >= 10080) & (Perguntas.Minutos < 40320)].count()
#print('Rows y',y)

j=Perguntas['Minutos'].loc[(Perguntas.Minutos >= 40320)].count()
#print('Rows j',j)

t=Perguntas['Minutos'].loc[(Perguntas.Minutos == -1)].count()
#print('Sem respostas',t)

#print('Soma: ',z+x+y+j+t)


print('Maior tempo: ',round(Perguntas['Minutos'].max(), 2),'  -  ','Menor tempo: ',Perguntas['Minutos'].loc[(Perguntas.Minutos >= 0)].min())
print('Data de: ',Perguntas['CreationDate'].min(),'Até: ',Perguntas['CreationDate'].max())
print('Média minutos: ',round(Perguntas['Minutos'].loc[(Perguntas.Minutos >= 0)].mean(), 2))
print('Desvio padrão: ',round(Perguntas['Minutos'].loc[(Perguntas.Minutos >= 0)].std(), 2))
print('Variancia: ',round(Perguntas['Minutos'].loc[(Perguntas.Minutos >= 0)].var(), 2))
print('Mediana: ',Perguntas['Minutos'].loc[(Perguntas.Minutos >= 0)].median())
print('Moda: ',statistics.mode(Perguntas['Minutos'].loc[(Perguntas.Minutos >= -1)]),' - Numero de ocorrencias: ',Perguntas.loc[(Perguntas.Minutos == -1)].shape[0])

#x=Perguntas.loc[(Perguntas.Minutos == 0.0)]
#print(x)


#numeros_ordenados = sorted(Perguntas['Minutos'].loc[(Perguntas.Minutos >= 0)])
#x=len(numeros_ordenados)
#i=x/2
#print(numeros_ordenados[int(i)])

'''
vendas = [z,x,y,j,t]
labels = ['Até 1 dia', '1 dia até  semana','1 semana até 1 mês','+ 1 mês','Sem resp']
plt.pie(vendas, labels=labels,autopct='%1.1f%%',shadow=True)
plt.legend(labels, loc=3)
# define que o gráfico será plotado em circulo
plt.axis('equal')
plt.show()
'''



#x = pd.Series(Perguntas['Minutos'])
#z = pd.to_numeric(x ,downcast='float')

#Perguntas.to_csv('DataFramePerg.csv', sep='\t', encoding='utf-8')
