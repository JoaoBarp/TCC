from pandas import read_csv
import pandas as pd
import numpy as np
import csv


SEED =  19963
# load data
filename = 'C:\\Users\\joaor\\Desktop\\Databases\\DataMENOR.csv'
perg2 = ['N Palavras corpo','N Palavras Título','N frases corpo','flesch_reading_ease','Média Caracteres Frase','Tamanho Código','Interogacão','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rótulo']


print('Começou ler...')
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...')
dataframe=dataframe.dropna()

dataframe.loc[(dataframe.Rótulo == 'C2') ,'Rótulo'] = 'C1'
dataframe.loc[(dataframe.Rótulo == 'C7') ,'Rótulo'] = 'C6'

dataframe.to_csv('C:\\Users\\joaor\\Desktop\\Databases\\5Class.csv', sep='\t', encoding='utf-8')

#Lê o arquivo seque, que
