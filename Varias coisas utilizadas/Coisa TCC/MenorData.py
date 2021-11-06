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
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.under_sampling import NearMiss

SEED =  19963
# load data
filename = 'C:\\Users\\joaor\\Desktop\\Data2class20%.csv'
#perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']

'''
mydict={}
with open('valores.csv','r') as csv_file:
    for line in csv.reader(csv_file):
        if line:
            print(line[0])
            mydict[line[0]] = line[1]

print(mydict)
'''
print('Começou...')
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou...')
dataframe=dataframe.dropna()

y_test=dataframe['Rotulo']
x_test=dataframe.drop(columns=['Rotulo'])

counter = Counter(y_test)
print(counter)
undersample = NearMiss(n_jobs=6)
X, y = undersample.fit_resample(x_test, y_test)
counter = Counter(y)
print(counter)

X['Rotulo'] = y

print(X)

#df['Rótulo']= y_test
#df['N Palavras corpo','N Palavras Título','N frases corpo','flesch_reading_ease','Média Caracteres Frase','Tamanho Código','Interogacão','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas'] = x_test
X.to_csv('C:\\Users\\joaor\\Desktop\\Databases\\Data2classNEAR.csv', sep='\t', encoding='utf-8')
