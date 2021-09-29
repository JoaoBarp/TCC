from sklearn.ensemble import ExtraTreesClassifier
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
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import plot_confusion_matrix
import seaborn as sns

SEED =  19963
# load data
filename='C:\\Users\\joaor\\Desktop\\2classesFF.csv'
filesalve='C:\\Users\\joaor\\Desktop\\result.csv'
#filename='/media/Lun02_Raid0/joaob/'+sys.argv[1]
#filesalve='Result/'+sys.argv[2]
#perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
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

print('Começou ler...')
print(filename)
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...')
dataframe=dataframe.dropna()
'''
print(len(dataframe.index))
dataframe = dataframe[(np.abs(stats.zscore(dataframe)) < 3).all(axis=1)]
print(len(dataframe.index))
'''
print(dataframe.groupby(['Rotulo']).size())


#Realoca o dataframe pela ordem de features mais importantes
#--dataframe=dataframe[results]

dict={}
classes=[1,2]
#classes=['C1','C2','C3','C4','C5','C6','C7']


#total de features
#features = ['Tamanho Codigo','flesch','N frases corpo','Interogacao','Inicia com WH','N perguntas Feitas','N Palavras Titulo','Subjetividade','N respostas Feitas','Media Caracteres Frase','Polaridade','']
#---features = ['flesch','Tamanho Codigo','N perguntas Feitas','Media Caracteres Frase','N frases corpo','N de tags','Polaridade','N Palavras Titulo','Interogacao','Inicia com WH','N respostas Feitas','']
#Aux vai incrmentanto, começa com as 2 mais importantes features
#---aux= ['Subjetividade','N Palavras corpo']

'''
print('-------------------------------------------------')
print(x_train)
print(y_train)
'''

clf=ExtraTreesClassifier(n_estimators=120,criterion='gini',max_features=0.8,max_samples=0.6,min_samples_split=2,min_samples_leaf=4,random_state=SEED,n_jobs=-1,verbose=1)

x_train, x_test, y_train, y_test = train_test_split(dataframe.drop(columns=['Rotulo']),dataframe['Rotulo'],test_size=0.3,random_state=SEED)

#features estão ordenadas pela importancia
#começa com 2 principais e vai sendo adicionada as seguintes.

print('------------------------------------------------------------------------------------')
print('Começou o treino')
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)

#sns.heatmap(confusion_matrix(y_test, y_pred, normalize='all'), annot = True)
#plot_confusion_matrix(clf, X_test, y_test)
#plt.show()
#print(classification_report(y_test, y_pred, target_names=classes))
print('Executando o classification_report')
    #salva o numero de features com os resultados(Como sei a ordem o numero já serve)
x=classification_report(y_test, y_pred, labels=classes)
print(x)
print('\n\n\n')
with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Val", x])
