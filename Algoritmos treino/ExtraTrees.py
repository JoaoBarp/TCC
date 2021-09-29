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
filename='C:\\Users\\joaor\\Desktop\\4Clas.csv'
filesalve='C:\\Users\\joaor\\Desktop\\Result\\' + sys.argv[1]
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



#Lê o arquivo seque, que contem o seguencia de features mais importantes
with open('C:\\Users\\joaor\\Desktop\\TCC\\Arq complementar\\ultimotsts.txt', 'r') as f:
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

#Realoca o dataframe pela ordem de features mais importantes
#--dataframe=dataframe[results]

dict={}
classes=[1,2,3,4]
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

clf=ExtraTreesClassifier(random_state=SEED,n_jobs=-1,verbose=0)

X_tr, X_te, y_train, y_test = train_test_split(dataframe.drop(columns=['Rotulo']),dataframe['Rotulo'],test_size=0.3,random_state=SEED)

#features estão ordenadas pela importancia
#começa com 2 principais e vai sendo adicionada as seguintes.
for i,x in enumerate(results):

    #separa os dados em treino e teste utilizando dataframe[aux]
    x_train=X_tr[aux]
    x_test=X_te[aux]
    print('------------------------------------------------------------------------------------')
    print('Começou o treino')
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
    print('\n\n\n')
    aux.append(x)


#-------------------------------------Salvando-------------------------------------------------------------

with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])
