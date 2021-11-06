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
import gc
from imblearn.over_sampling import SMOTE

SEED =  19963
#sm = SMOTE(random_state=42,n_jobs=-1)
# load data
filename1='C:\\Users\\joaor\\Desktop\\TESTE.csv'
filename2='C:\\Users\\joaor\\Desktop\\Smote_bordeline.csv'

filesalve='C:\\Users\\joaor\\Desktop\\SMOTE\\Smote_bordeline.csv'
#filename='/media/Lun02_Raid0/joaob/'+sys.argv[1]
#filesalve='Result/'+sys.argv[2]
#perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','hora','Feriado/FimSem','Rotulo']
perg = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']


print('Começou ler...')
TREINO=pd.read_csv(filename2,sep='\t',usecols=perg, encoding='utf-8')
print('Acabou ler ...')
TREINO=TREINO.dropna()

'''
print('Começou ler...')
TESTE=pd.read_csv(filename1,sep='\t',usecols=perg, encoding='utf-8')
print('Acabou ler ...')
TESTE=TESTE.dropna()
'''
'''
pdList = [TESTE, TREINO,]  # List of your dataframes
Perguntas = pd.concat(pdList)'''
print(TREINO.groupby(['Rotulo']).size())
print('\n\n\n')
#print(TESTE.groupby(['Rotulo']).size())

#Realoca o dataframe pela ordem de features mais importantes
#--dataframe=dataframe[results]

dict={}
classes=[0,1]

clf=ExtraTreesClassifier(n_estimators=120,criterion='gini',max_features=0.8,max_samples=0.6,min_samples_split=2,min_samples_leaf=4,random_state=SEED,n_jobs=-1,verbose=1)


'''
with open('C:\\Users\\joaor\\Desktop\\SMOTE\\tx.txt', 'r') as f:
    line=f.readlines()
    results=line[0].split(',')
    del results[-1]

#results.append('Rotulo')
results.append('')
print(results)
print('------------------------------------------------------------------------------------')

aux=[]
aux.append(results[0])
aux.append(results[1])
print(aux)
print('------------------------------------------------------------------------------------')
del(results[0])
del(results[0])
print(results)
print('------------------------------------------------------------------------------------')



x_TRAINO, x_TESTE, y_TRAINO, y_TESTE = train_test_split(TREINO.drop(columns=['Rotulo']),TREINO['Rotulo'],test_size=0.50,random_state=SEED)
x_TESTE['Rotulo'] = y_TESTE
print(x_TESTE.groupby(['Rotulo']).size())
X_tr, X_te, y_train, y_test = train_test_split(x_TESTE.drop(columns=['Rotulo']),x_TESTE['Rotulo'],test_size=0.3,random_state=SEED)


print('\n\n\n')
print('\n\n\n')
print('\n\n\n')
for i,x in enumerate(results):

    #separa os dados em treino e teste utilizando dataframe[aux]
    x_train=X_tr[aux]
    x_test=X_te[aux]
    print('------------------------------------------------------------------------------------')
    print('Começou o treino')
    clf.fit(x_train,y_train)
    y_pred=clf.predict(x_test)

    #print dos resultados e valores
    print(i,'> ---------------------------------------------------------------------------------')
    print(aux)
    print('------------------------------------------------------------------------------------')
    #print(classification_report(y_test, y_pred, target_names=classes))
    print('Executando o classification_report')
    #salva o numero de features com os resultados(Como sei a ordem o numero já serve)
    dict[len(aux)]=classification_report(y_test, y_pred, labels=classes)
    print(dict[len(aux)])
    print('\n\n\n')
    aux.append(x)


#-------------------------------------Salvando-------------------------------------------------------------

with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])


'''
x_TRAINO, x_TESTE, y_TRAINO, y_TESTE = train_test_split(TREINO.drop(columns=['Rotulo']),TREINO['Rotulo'],test_size=0.50,random_state=SEED)
x_TESTE['Rotulo'] = y_TESTE
x_train, x_test, y_train, y_test = train_test_split(x_TESTE.drop(columns=['Rotulo']),x_TESTE['Rotulo'],test_size=0.3,random_state=SEED)

clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)

#print dos resultados e valores
print('> ---------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------')
#print(classification_report(y_test, y_pred, target_names=classes))
print('Executando o classification_report')
#salva o numero de features com os resultados(Como sei a ordem o numero já serve)
x=classification_report(y_test, y_pred, labels=classes)
print(x)
print('\n\n\n')
with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Val", x])
'''

k_values = [1, 3, 7, 10]
for i,x in enumerate(results):

    print('K: ',k)
    sm = SMOTE(random_state=42,n_jobs=-1,k_neighbors=k)
    X_res, y_res = sm.fit_resample(TREINO.drop(columns=['Rotulo']),TREINO['Rotulo'])

    #x_TRAINO, x_TESTE, y_TRAINO, y_TESTE = train_test_split(X_res, y_res,test_size=0.50,random_state=SEED)

    x_TRAINO, x_TESTE, y_TRAINO, y_TESTE = train_test_split(X_res, y_res,test_size=0.50,random_state=SEED)
    x_TESTE['Rotulo'] = y_TESTE
    x_train, x_test, y_train, y_test = train_test_split(x_TESTE.drop(columns=['Rotulo']),x_TESTE['Rotulo'],test_size=0.3,random_state=SEED)


    #X_res['Rotulo'] =  y_res
    #X_res.to_csv('C:\\Users\\joaor\\Desktop\\SMOTE_TREINO.csv', sep='\t', encoding='utf-8')




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
    dict[k]=classification_report(y_test, y_pred, labels=classes)
    print(dict[k])
    print('\n\n\n')

    del x_train
    del x_test
    del y_train
    del y_test
    del x_TRAINO
    del x_TESTE
    del y_TRAINO
    del y_TESTE
    del X_res
    del y_res

    gc.collect()



with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])
'''
'''
with open(filesalve, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Val", x])
'''


'''
X_res['Rotulo'] =  y_res
X_res.to_csv('C:\\Users\\joaor\\Desktop\\SMOTE_TREINO_SEM_FERIADO.csv', sep='\t', encoding='utf-8')
'''
