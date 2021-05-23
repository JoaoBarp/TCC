from pandas import read_csv
import pandas as pd
import numpy as np
import csv


SEED =  19963
# load data
filename = 'C:\\Users\\joaor\\Desktop\\Databases\\XX.csv'
#perg2 = ['N Palavras corpo','N Palavras Título','N frases corpo','flesch_reading_ease','Média Caracteres Frase','Tamanho Código','Interogacão','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rótulo']
perg = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rótulo']
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']


print('Começou ler...')
dataframe=pd.read_csv(filename,sep='\t',usecols=perg, encoding='utf-8')
print('Acabou ler ...')
dataframe=dataframe.dropna()
dataframe.columns=perg2



dataframe.to_csv('C:\\Users\\joaor\\Desktop\\Databases\\XX.csv', sep='\t', encoding='utf-8')

#Lê o arquivo seque, que
