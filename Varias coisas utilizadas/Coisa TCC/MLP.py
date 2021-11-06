# Feature Selection with Univariate Statistical Tests
from sklearn.neural_network import MLPClassifier
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
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import classification_report
import csv
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import sys
from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


SEED =  19963
# load data
filename='C:\\Users\\joaor\\Desktop\\Databases\\' + sys.argv[1]
filesalve='C:\\Users\\joaor\\Desktop\\' + sys.argv[2]
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

print(dataframe.groupby(['Rotulo']).size())



#Lê o arquivo seque, que contem o seguencia de features mais importantes
with open('seque.txt', 'r') as f:
    line=f.readlines()
    results=line[0].split(',')
    del results[-1]

results.append('Rotulo')
#Realoca o dataframe pela ordem de features mais importantes
dataframe=dataframe[results]

dict={}
classes=[1,2,3,4]
#classes=['C1','C2','C3','C4','C5','C6','C7']

print('-------------------------------------------------')
print('Começou o treino')

#total de features
#features = ['N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','']
features = ['Tamanho Codigo','flesch','N frases corpo','Interogacao','Inicia com WH','N perguntas Feitas','N Palavras Titulo','Subjetividade','N respostas Feitas','Media Caracteres Frase','Polaridade','']

#Aux vai incrmentanto, começa com as 2 mais importantes features
aux= ['N Palavras corpo','N de tags']

'''
print('-------------------------------------------------')
print(x_train)
print(y_train)
'''

clf=LinearDiscriminantAnalysis()
X=dataframe.drop(columns=['Rotulo'])
y=dataframe['Rotulo']

#features estão ordenadas pela importancia
#começa com 2 principais e vai sendo adicionada as seguintes.
for i,x in enumerate(features):

    #separa os dados em treino e teste utilizando dataframe[aux]
    x_train=X[aux]



    #print dos resultados e valores
    print(i,'> ---------------------------------------------------------------------------------')
    print(aux)
    print('------------------------------------------------------------------------------------')
    #print(classification_report(y_test, y_pred, target_names=classes))
    print('Executando o classification_report')
    #salva o numero de features com os resultados(Como sei a ordem o numero já serve)
    dict[len(aux)]=cross_validate(clf, X, y,
               scoring = {'precision micro' : make_scorer(precision_score, average = 'micro'),'precision macro' : make_scorer(precision_score, average = 'macro'),
       'recall micro' : make_scorer(recall_score, average = 'micro'),'recall macro' : make_scorer(recall_score, average = 'macro')},n_jobs=-1,cv=10,return_train_score=True)
    print(dict[len(aux)])
    aux.append(x)


#-------------------------------------Salvando-------------------------------------------------------------
with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])