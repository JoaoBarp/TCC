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
filename = 'DataNorm.csv'
perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
perg2 = ['N Palavras corpo','N Palavras Título','N frases corpo','flesch_reading_ease','Média Caracteres Frase','Tamanho Código','Interogacão','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rótulo']

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



with open('seque.txt', 'r') as f:
    line=f.readlines()
    results=line[0].split(',')
    del results[-1]

results.append('Rótulo')
#print(results)
#print(dataframe.head())
dataframe=dataframe[results]
#print(dataframe.head())
dict={}
classes=['C1','C2','C3','C4','C5','C6','C7']
print('-------------------------------------------------')
print('Começou o treino')

features = ['N frases corpo','flesch_reading_ease','Média Caracteres Frase','Tamanho Código','Interogacão','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','']
aux= ['N Palavras corpo','N Palavras Título']



'''
print('-------------------------------------------------')
print(x_train)
print(y_train)
'''

#clf=RandomForestClassifier(random_state=19889,n_jobs=-1)
clf=LinearSVC(random_state=SEED,verbose=1)

#features estão ordenadas pela importancia
#começa com 2 principais e vai sendo adicionada as seguintes.
for x in features:

    x_train, x_test, y_train, y_test = train_test_split(dataframe[aux],dataframe['Rótulo'],test_size=0.3,random_state=SEED)



    clf.fit(x_train,y_train)

    print('------------------------------------------------------------------------------------')
    print(aux)
    y_pred=clf.predict(x_test)
    print('------------------------------------------------------------------------------------')
    print(classification_report(y_test, y_pred, target_names=classes))
    print('------------------------------------------------------------------------------------')
    dict[len(aux)]=classification_report(y_test, y_pred, target_names=classes)
    aux.append(x)


#-------------------------------------Salvando-------------------------------------------------------------
with open('valores.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])
