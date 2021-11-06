# Feature Selection with Univariate Statistical Tests
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
import pandas as pd
import numpy as np
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report
import csv
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import sys
from sklearn.tree import DecisionTreeClassifier

SEED =  19963
# load data
filename='C:\\Users\\joaor\\Desktop\\Databases\\' + sys.argv[1]
#filename='/media/Lun02_Raid0/joaob/'+sys.argv[1]
#filesalve='Result/'+sys.argv[2]
#perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']


print('Começou ler...')
print(filename)
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...')
dataframe=dataframe.dropna()

print(dataframe.groupby(['Rotulo']).size())

x=dataframe.loc[:,['N Palavras corpo','Rotulo','N Palavras Titulo']]
'''
print(x.sort_values(by=['N Palavras corpo']))
x.plot(kind='scatter',x='Rotulo',y='N Palavras corpo',color='red')
pyplot.show()
'''

pyplot.scatter(x['N Palavras corpo'],x['N Palavras Titulo'] ,c=x['Rotulo'])
#plt.ylim(0, 1)
#plt.xlim(0,1)
pyplot.xlabel('Column 0')
pyplot.ylabel('Column 1')
pyplot.show()
