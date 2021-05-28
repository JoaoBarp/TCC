# -*- coding: utf-8 -*-
from sklearn.manifold import TSNE
from collections import defaultdict
from matplotlib import pyplot as plt
import xml.etree.ElementTree
import pandas as pd
from datetime import datetime, timedelta
import time
import re, cgi, os, pickle, logging, time
from textblob import TextBlob
import textstat
from collections import Counter
import sys
import csv
import json
from collections import Counter
import numpy as np
from xml.etree.ElementTree import iterparse
from lxml import etree
import psutil
import statistics
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report

SEED =  19963
perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']

filename='C:\\Users\\joaor\\Desktop\\Databases\\' + sys.argv[1]
print('Começou ler...')
print(filename)
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...')



X=dataframe.drop(columns=['Rotulo'])
y=dataframe['Rotulo']

tsne = TSNE(n_components=2, verbose=1,n_jobs=-1, random_state=SEED)
z = tsne.fit_transform(X)


plt.scatter(z[:,0],z[:,1], c=y)
plt.title('TSNE')
plt.xlabel('Column 0')
plt.ylabel('Column 1')
plt.legend()
plt.show()
