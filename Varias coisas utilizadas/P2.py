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


def getNper(User,data):
    if User in dictPERG.keys():
        lista = dictPERG[User]
        lista.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
        splice = [x for x in lista if  datetime.strptime(x, "%Y-%m-%d %H:%M:%S") < datetime.strptime(data, "%Y-%m-%d %H:%M:%S")]
        return len(splice)
    else:
        return 0

def getNres(User,data):
    if User in dictRESP.keys():
        lista = dictRESP[User]
        lista.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
        splice = [x for x in lista if  datetime.strptime(x, "%Y-%m-%d %H:%M:%S") < datetime.strptime(data, "%Y-%m-%d %H:%M:%S")]
        return len(splice)
    else:
        return 0

#remover a parte .%f aí n da mais erro
#"%Y-%m-%d %H:%M:%S.%f"
def minutos(k,d):
    try:
        if k in dictDataRespsPERG.keys():
            x = dictDataRespsPERG[k]
            x.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
            d1 = datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
            d2 = datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S")
            #print(((d2 - d1).total_seconds() / 60.0))
            return ((d2 - d1).total_seconds() / 60.0)
        else:
            return -1
    except:
        return -2


#DUsers.clear()
PerG={}
dictRESP = {}
dictPERG = {}
dictDataRespsPERG = {}


nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Dict\\dictDataRespsPERG.json"
with open(nArq) as json_file:
    dictDataRespsPERG = json.load(json_file)
dictDataRespsPERG= {int(k):v for k,v in dictDataRespsPERG.items()}

with open('countARQ.txt') as f:
    countARQ = f.read()

for x in range(int(countARQ)):
    nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Arq-" + str(x)+'.json'
    with open(nArq) as json_file:
        data = json.load(json_file)
        PerG.update(data)


nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Dict\\dictPERG.json"
with open(nArq) as json_file:
    dictPERG = json.load(json_file)

dictPERG= {int(k):v for k,v in dictPERG.items()}

nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Dict\\dictRESP.json"
with open(nArq) as json_file:
    dictRESP = json.load(json_file)

dictRESP = {int(k):v for k,v in dictRESP.items()}

print("Valor PerG:",sys.getsizeof(PerG)/(1024*1024))

i=0
for k,v in PerG.items():
    if i%500 == 0:
        print('Fim: ',i, end='')

    pe=getNper(v[0],v[1])
    re=getNres(v[0],v[1])
    #print(v[0],re,pe)
    #print(dictRESP[v[0]])
    min = minutos(int(k),v[1])
    PerG[k].append(pe)
    PerG[k].append(re)
    PerG[k].append(float(min))
    i+=1
    print('\r\r\r',end='')

nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Dict\\PerG.json"
with open(nArq, "w") as outfile:
    json.dump(PerG, outfile)




perg = ['OwnerUserId','CreationDate','Ntags','TemCodigo','CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Minutos']

#Perguntas = pd.DataFrame(dict([ (k,pd.Series(v)) for k, v in PerG.items()]))
Perguntas = pd.DataFrame()
inicio = time.time()
for k, v in PerG.items():
    Perguntas[k]=pd.Series(v)

fim = time.time()
print('\n\nTEMPO : ',(fim - inicio)/60)

Perguntas = Perguntas.transpose()
Perguntas.columns = perg
print(Perguntas.head())

#print(Perguntas['Minutos'])
#print(Perguntas['Minutos'].loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos < 1024)])
#print(Perguntas['Minutos'].loc[Perguntas.Minutos < 0])


#y=np.delete(np.array(Perguntas['Minutos']), -1)
#print(pd.cut(Perguntas['Minutos'].loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos <= 1024)],3))

Perguntas.loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos <= 1024),'Rotulo']=pd.cut(Perguntas['Minutos'].loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos <= 1024)],3,labels=["Super Rapido", "Muito Rapido", "Rapido"])
Perguntas.loc[Perguntas.Minutos > 1024,'Rotulo']=pd.cut(Perguntas['Minutos'].loc[Perguntas.Minutos > 1024],3,labels=["Medio", "Lento", "Mt Lento"])
Perguntas.loc[Perguntas.Minutos == -1,'Rotulo']="Sem Resp"
#Perguntas['Rotulo']=pd.qcut(Perguntas['Minutos'].loc[(Perguntas.Minutos > 0) & (Perguntas.Minutos <= 1024)],3)
#print(Perguntas)

x=Perguntas['Minutos'][(Perguntas['Minutos'] <= 1440) & (Perguntas['Minutos'] >720)].count()
y=Perguntas['Minutos'][Perguntas['Minutos'] > 1440].count()
z=Perguntas['Minutos'][(Perguntas['Minutos'] <= 720) & (Perguntas['Minutos'] >0)].count()
t=Perguntas['Minutos'][Perguntas['Minutos'] == -1].count()

vendas = [z,x,y,t]
labels = ['Até 6H', '6H até 1 dia','Após 1 dia','Sem resp']

plt.pie(vendas, labels=labels,autopct='%1.1f%%',shadow=True)
plt.legend(labels, loc=3)
# define que o gráfico será plotado em circulo
plt.axis('equal')
plt.show()

#x = pd.Series(Perguntas['Minutos'])
#z = pd.to_numeric(x ,downcast='float')

Perguntas.to_csv('DataFramePerg.csv', sep='\t', encoding='utf-8')
