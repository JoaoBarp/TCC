import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

filename = 'C:\\Users\\joaor\\Desktop\\Databases\\Data5class.csv'

scaler = MinMaxScaler()

perg = ['CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Rotulo']
perg2 = ['N Palavras corpo','N Palavras Título','N frases corpo','flesch_reading_ease','Média Caracteres Frase','Tamanho Código','Interogacão','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rótulo']

print('Começou...')
dataframe=pd.read_csv(filename,sep='\t',usecols=perg, encoding='utf-8')
dataframe.columns=perg2
print('Acabou...')
dataframe=dataframe.dropna()

print(dataframe.head())

dataframe[['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']])

print(dataframe.head())

dataframe.to_csv('C:\\Users\\joaor\\Desktop\\Databases\\Data5class.csv', sep='\t', encoding='utf-8')
