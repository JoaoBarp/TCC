import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

filename = 'C:\\Users\\joaor\\Desktop\\Databases\\Data7classFULL.csv'

scaler = MinMaxScaler()

perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']

print('Começou...')
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou...')
dataframe=dataframe.dropna()

print(dataframe.head())

dataframe[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']] = scaler.fit_transform(dataframe[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas']])

print(dataframe.head())

dataframe.to_csv('C:\\Users\\joaor\\Desktop\\Databases\\Data7classFULL.csv', sep='\t', encoding='utf-8')
