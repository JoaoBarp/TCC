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
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import seaborn as sns

SEED =  19963
# load data
filename='C:\\Users\\joaor\\Desktop\\Databases\\Test2.csv'
#filename='/media/Lun02_Raid0/joaob/'+sys.argv[1]
#filesalve='Result/'+sys.argv[2]
#perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
perg2 =  ['TemCodigo','N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']


print('Começou ler...')
print(filename)
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...')
dataframe=dataframe.dropna()

#print(dataframe.groupby(['Rotulo']).size())
#print(dataframe.head())
#print(dataframe.describe())
#x=dataframe.describe()

print(dataframe[["TemCodigo", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["N Palavras corpo", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["N perguntas Feitas", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["N respostas Feitas", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["N Palavras Titulo", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["flesch", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["Interogacao", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["Tamanho Codigo", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["Subjetividade", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["Polaridade", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))
print('\n')
print(dataframe[["N de tags", "Rotulo"]].groupby(['Rotulo'], as_index=False).mean().sort_values(by='Rotulo', ascending=False))

#print(pd.crosstab(dataframe['TemCodigo'],data1[Target[0]]))
''''
print(dataframe.groupby(['Rotulo'])['flesch'].mean())
print(dataframe.groupby(['Rotulo'])['N Palavras Titulo'].mean())
print(dataframe.groupby(['Rotulo'])['Tamanho Codigo'].mean())
print(dataframe.groupby(['Rotulo'])['N Palavras corpo'].mean())
print(dataframe.groupby(['Rotulo'])['N perguntas Feitas'].mean())
print(dataframe.groupby(['Rotulo'])['N respostas Feitas'].mean())
#x.to_csv ('C:\\Users\\joaor\\Desktop\desc.csv', index = False, header=True)

g = sns.FacetGrid(dataframe, col='Rotulo')
g.map(plt.hist, 'N Palavras corpo', bins=10)

plt.show()
'''
