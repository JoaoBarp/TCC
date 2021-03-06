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
import _pickle as pickle
import json
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import GridSearchCV

SEED =  19963
# load data
filename='C:\\Users\\joaor\\Desktop\\Databases\\' + sys.argv[1]
filesalve='C:\\Users\\joaor\\Desktop\\TCC\\Result\\' + sys.argv[2]
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
with open('seque4class.txt', 'r') as f:
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
#features = ['Tamanho Codigo','flesch','N frases corpo','Interogacao','Inicia com WH','N perguntas Feitas','N Palavras Titulo','Subjetividade','N respostas Feitas','Media Caracteres Frase','Polaridade','']
features = ['N Palavras corpo','N de tags','Tamanho Codigo','N frases corpo','Interogacao','flesch','Inicia com WH','N perguntas Feitas','N Palavras Titulo','N respostas Feitas','Subjetividade','Polaridade','Media Caracteres Frase']
#Aux vai incrmentanto, começa com as 2 mais importantes features
aux= ['N Palavras corpo','N de tags','Tamanho Codigo','N frases corpo','Interogacao']

'''
print('-------------------------------------------------')
print(x_train)
print(y_train)
'''

y = dataframe['Rotulo']
X = dataframe.drop(columns=['Rotulo'])
X = X[aux]

clf=ExtraTreesClassifier(random_state=SEED,n_jobs=4)


param = {
    'n_estimators': [200, 100, 50, 30],
    'min_samples_split': [2, 3 ,4, 10],
    'max_depth': [10, None, 2, 5],
    'min_samples_leaf':[1, 2, 3, 10],
}




#scorer = {'precision micro' : make_scorer(precision_score, average = 'micro'),'precision macro' : make_scorer(precision_score, average = 'macro'),
#'recall micro' : make_scorer(recall_score, average = 'micro'),'recall macro' : make_scorer(recall_score, average = 'macro')}

scorer = {'precision' : make_scorer(precision_score,average = 'macro',zero_division=0),'recall' : make_scorer(recall_score,average = 'macro',zero_division=0)}


grid = GridSearchCV(estimator=clf, param_grid=param, scoring = scorer, verbose=2, cv=5, n_jobs=1,refit='precision')

print('------------------------------------------------------------------------------------')
print('TREINANDO')
print('------------------------------------------------------------------------------------')
grid.fit(X, y)


print('------------------------------------------------------------------------------------')
print(grid.best_estimator_)
print('------------------------------------------------------------------------------------')
print(grid.best_score_)
print('------------------------------------------------------------------------------------')
print(grid.best_params_)
print('------------------------------------------------------------------------------------')

a = {'cv_results': grid.cv_results_}
b = {'best_estimator': grid.best_estimator_}
c = {'best_score_':grid.best_score_}
d = {'best_params_': grid.best_params_}

with open('C:\\Users\\joaor\\Desktop\\TCC\\Grid\\ExtraTrees\\cv_results.txt', 'w') as json_a:
    json_a.write(str(grid.cv_results_))

with open('C:\\Users\\joaor\\Desktop\\TCC\\Grid\\ExtraTrees\\best_estimator.txt', 'w') as json_b:
    json_b.write(str(grid.best_estimator_))

with open('C:\\Users\\joaor\\Desktop\\TCC\\Grid\\ExtraTrees\\best_score_.txt', 'w') as json_c:
    json_c.write(str(grid.best_score_))

with open('C:\\Users\\joaor\\Desktop\\TCC\\Grid\\ExtraTrees\\best_params_.txt', 'w') as json_d:
     json_d.write(str(grid.best_params_))

























'''
#X_tr, X_te, y_train, y_test = train_test_split(dataframe.drop(columns=['Rotulo']),dataframe['Rotulo'],test_size=0.3,random_state=SEED)

#features estão ordenadas pela importancia
#começa com 2 principais e vai sendo adicionada as seguintes.
for i,x in enumerate(features):

    #separa os dados em treino e teste utilizando dataframe[aux]
    x_train=X_tr[aux]
    x_test=X_te[aux]

    clf.fit(x_train,y_train)
    y_pred=clf.predict(x_train)

    #print dos resultados e valores
    print(i,'> ---------------------------------------------------------------------------------')
    print(aux)
    print('------------------------------------------------------------------------------------')
    #print(classification_report(y_test, y_pred, target_names=classes))
    print('Executando o classification_report')
    #salva o numero de features com os resultados(Como sei a ordem o numero já serve)
    dict[len(aux)]=classification_report(y_train, y_pred, labels=classes)
    print(dict[len(aux)])
    aux.append(x)



#-------------------------------------Salvando-------------------------------------------------------------
with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])
'''
