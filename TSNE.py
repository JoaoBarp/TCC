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
