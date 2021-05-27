from sklearn.manifold import TSNE
import pandas as pd
import numpy as np
from matplotlib import pyplot
from sklearn.feature_selection import SelectKBest
import seaborn as sns
import sys
import csv
import json

SEED =  19963
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']

filename='C:\\Users\\joaor\\Desktop\\Databases\\' + sys.argv[1]
print('Começou ler...')
print(filename)
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...')


X=dataframe.drop(columns=['Rotulo'])
y=dataframe['Rotulo']

tsne = TSNE(n_components=2, verbose=1, random_state=SEED)
z = tsne.fit_transform(X)

df = pd.DataFrame()
df["y"] = y
df["comp-1"] = z[:,0]
df["comp-2"] = z[:,1]




'''


# carrega dataset e elimina as linhas com mais de 60% de valores faltantes
fpath='/content/drive/MyDrive/Aulas/Pós/'
dfhorse=loaddf(fpath+'horse-colic.csv')
# elimina as colunas com mais de 60% de valores faltantes
#getMissingValues(dfhorse)
dfhorse=deleteRows(60,dfhorse)
# elimina as colunas com mais de 50% de valores faltantes
dfhorse=deleteColumns(50,dfhorse)

###
X=dfhorse  # cria o dataset
y=dfhorse[22] # cria o conjunto de rótulos
y=np.array(y) # y é do tipo Series do pandas
# y que era um vetor passar ser uma matriz vetor para fit do SimpleImputer
y=y.reshape(-1,1)
X=X.drop(columns=[22]) # exclui o rótulo do dataset
# objeto do SimpleImputer para imputar o rótulo faltante (valor mais frequente)
imp_y=SimpleImputer(strategy='most_frequent')
imp_y.fit(y)
y_new=imp_y.transform(y) # cria y_new
# transform y_new em um vetor (era uma matriz de 1 coluna)
y_new=y_new.reshape(y_new.shape[0])
## objeto do tipo IterativeImputer
hor_imp=IterativeImputer(estimator=BayesianRidge(),max_iter=100,random_state=0)
hor_imp.fit(X)
X_new=hor_imp.transform(X) # cria X_new sem valores faltantes

#
#X_new=transform01(X_new)
X_new=transformAvg(X_new)

K=2
skBest=SelectKBest(k=K).fit(X_new,y_new)
features = skBest.get_support(indices=True)
print('Melhores',K,' atributos',features)
#
#X_2d=getPCA(X_new,K)
X_2d=getTSNE(X_new,K)
#####
print(X_2d[:4,:])


plt.scatter(X_2d[:,0],X_2d[:,1], c=y_new)
plt.title('Horse Colic - PCA')
#plt.title('Horse Colic - TSNE')
plt.xlabel('Column 0')
plt.ylabel('Column 1')
plt.legend()
plt.show()
'''
