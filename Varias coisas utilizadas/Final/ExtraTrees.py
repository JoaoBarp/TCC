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
from scipy import stats

SEED =  19963
# load data
filename='C:\\Users\\joaor\\Desktop\\Final\\2classesFF.csv'
filesalve='C:\\Users\\joaor\\Desktop\\Final\\' + sys.argv[1]
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



#Lê o arquivo seque, que contem o seguencia de features mais importantes
with open('C:\\Users\\joaor\\Desktop\\Final\\2classesFF.txt', 'r') as f:
    line=f.readlines()
    results=line[0].split(',')
    del results[-1]

#results.append('Rotulo')
results.append('')
print(results)

aux=[]
aux.append(results[0])
aux.append(results[1])
print(aux)


dict={}
classes=[1,2]


clf=ExtraTreesClassifier(n_estimators=120,criterion='gini',max_features=0.8,max_samples=0.6,min_samples_split=2,min_samples_leaf=4,random_state=SEED,n_jobs=-1,verbose=1)

X_tr, X_te, y_train, y_test = train_test_split(dataframe.drop(columns=['Rotulo']),dataframe['Rotulo'],test_size=0.3,random_state=SEED)


for i,x in enumerate(results):

    x_train=X_tr[aux]
    x_test=X_te[aux]
    print('------------------------------------------------------------------------------------')
    print('Começou o treino')
    clf.fit(x_train,y_train)
    y_pred=clf.predict(x_test)


    print(i,'> ---------------------------------------------------------------------------------')
    print(aux)
    print('------------------------------------------------------------------------------------')

    print('Executando o classification_report')

    dict[len(aux)]=classification_report(y_test, y_pred, labels=classes)
    print(dict[len(aux)])
    print('\n\n\n')
    aux.append(x)


#-------------------------------------Salvando-------------------------------------------------------------

with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])
