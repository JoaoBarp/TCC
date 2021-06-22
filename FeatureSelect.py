from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest, SelectFwe, GenericUnivariateSelect, SelectFdr, SelectFpr
from sklearn.feature_selection import f_classif
import pandas as pd
import numpy as np
from matplotlib import pyplot

from sklearn.ensemble import RandomForestClassifier

# load data
filename = 'C:\\Users\\joaor\\Desktop\\Databases\\Data2classNEAR.csv'
#perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']


print('Começou...')
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
#dataframe.columns=perg2
print('Acabou...')

dataframe=dataframe.dropna()


X = dataframe.drop(columns=['Rotulo'])
y = dataframe['Rotulo']

'''
#-----------------------------------------------AQUI FOI f_classif ------------------------------------------------------------------------------------------------------
# feature extraction
model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)
RandomForestClassifier(criterion='giny')


print(model.feature_importances_)

fig = pyplot.figure()
ax = fig.add_subplot(111)

sampledata = {'genre': ['N Palavras corpo','N Palavras Título','N frases corpo','flesch_reading_ease','Média Caracteres Frase','Tamanho Código','Interogacão','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']
,
              'rating':model.feature_importances_ }

test = pd.DataFrame(sampledata,  index=sampledata['genre'])
test.sort_values(by = "rating").plot(kind = "barh", color = "blue", legend = False, grid = True, ax = ax)

pyplot.xlim(0, 0.5)
pyplot.xlabel('Score')
pyplot.ylabel('Features')
pyplot.title('Índice de GINI')
for i, v in enumerate(sorted(test.rating)):
    pyplot.text(v+0.02, i, str(round(v, 2)), color='blue', va="center")

pyplot.show()

#-----------------------------------------------AQUI FOI f_classif ------------------------------------------------------------------------------------------------------

'''


#-----------------------------------------------AQUI FOI f_classif ------------------------------------------------------------------------------------------------------

var=[]

fs = SelectKBest(score_func=f_classif, k='all')
#fs = SelectFpr(score_func=f_classif)
# learn relationship from training data
fs.fit(X,y)
# transform train input data
for i in range(len(fs.scores_)):
    print(perg2[i],':         ', fs.scores_[i])
    var.append(fs.scores_[i])

# plot the scores

#pyplot.barh([perg2[i] for i in range(len(fs.scores_))], fs.scores_)
#pyplot.show()


fig = pyplot.figure()
ax = fig.add_subplot(111)

sampledata = {'genre': ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']
,
              'rating':var }

test = pd.DataFrame(sampledata,  index=sampledata['genre'])
test.sort_values(by = "rating").plot(kind = "barh", color = "blue", legend = False, grid = True, ax = ax)

pyplot.xlim(0, 800000)
pyplot.xlabel('Score')
pyplot.ylabel('Features')
pyplot.title('SelectKBest')
for i, v in enumerate(sorted(test.rating)):
    pyplot.text(v+0.2, i, str(round(v, 2)), color='blue', va="center")

print('----------------------------------------')
z=test.sort_values(by = "rating")
list=z.index.tolist()
list=list[::-1]
print(list)
pyplot.show()
arquivo = open('C:\\Users\\joaor\\Desktop\\TCC\\Arq complementar\\Data3class20%.txt', 'w+')
for x in list:
    arquivo.writelines(x)
    arquivo.writelines(',')
arquivo.close()

#-----------------------------------------------AQUI FOI f_classif ------------------------------------------------------------------------------------------------------
