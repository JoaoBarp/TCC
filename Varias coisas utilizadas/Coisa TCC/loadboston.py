from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import ExtraTreesClassifier
# Feature Selection with Univariate Statistical Tests
from pandas import read_csv
import matplotlib.pyplot as plt
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

from collections import Counter

from sklearn.datasets import make_classification

from imblearn.under_sampling import RandomUnderSampler

SEED =  19963

filename='C:\\Users\\joaor\\Desktop\\Databases\\Data3class20%.csv'
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']

print('Começou ler...')
print(filename)
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...')
dataframe=dataframe.dropna()

print(dataframe.groupby(['Rotulo']).size())


boston = pd.DataFrame(dataframe.drop(columns='Rotulo'), columns= ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas'])

plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(boston.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12);# save heatmap as .png file
# dpi - sets the resolution of the saved image in dots/inches
# bbox_inches - when set to 'tight' - does not allow the labels to be croppedplt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
