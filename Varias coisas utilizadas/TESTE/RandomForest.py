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

SEED =  19963
# load data
filename = 'C:\\Users\\joaor\\Desktop\\XX.csv'
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

print('Começou ler...')
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...')
dataframe=dataframe.dropna()



#Lê o arquivo seque, que contem o seguencia de features mais importantes
with open('seque.txt', 'r') as f:
    line=f.readlines()
    results=line[0].split(',')
    del results[-1]

results.append('Rótulo')
#Realoca o dataframe pela ordem de features mais importantes
dataframe=dataframe[results]

dict={}
classes=['C1','C2','C3','C4','C5','C6','C7']

print('-------------------------------------------------')
print('Começou o treino')

#total de features
features = ['Tamanho Código','flesch_reading_ease','N frases corpo','Interogacão','Inicia com WH','N perguntas Feitas','N Palavras Título','Subjetividade','N respostas Feitas','Média Caracteres Frase','Polaridade','']
#Aux vai incrmentanto, começa com as 2 mais importantes features
aux= ['N Palavras corpo','N de tags']

'''
print('-------------------------------------------------')
print(x_train)
print(y_train)
'''

clf=RandomForestClassifier(random_state=SEED,n_jobs=-1,verbose=1)


#features estão ordenadas pela importancia
#começa com 2 principais e vai sendo adicionada as seguintes.
for x in features:

    #separa os dados em treino e teste utilizando dataframe[aux]
    x_train, x_test, y_train, y_test = train_test_split(dataframe[aux],dataframe['Rótulo'],test_size=0.3,random_state=SEED)



    clf.fit(x_train,y_train)
    y_pred=clf.predict(x_test)

    #print dos resultados e valores
    print('------------------------------------------------------------------------------------')
    print(aux)
    print('------------------------------------------------------------------------------------')
    print(classification_report(y_test, y_pred, target_names=classes))
    print('------------------------------------------------------------------------------------')
    #salva o numero de features com os resultados(Como sei a ordem o numero já serve)
    dict[len(aux)]=classification_report(y_test, y_pred, target_names=classes)
    aux.append(x)


#-------------------------------------Salvando-------------------------------------------------------------
with open('C:\\Users\\joaor\\Desktop\\valoresDatamenorRandon.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])
