from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import pandas as pd
from datetime import datetime
import sys

filename='/media/Lun02_Raid0/joaob/'+sys.argv[1]

perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']

print('Começou ler...')
print(filename)
start_t=datetime.now()
dataframe=pd.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...',datetime.now()-start_t)
dataframe=dataframe.dropna()

print(dataframe.groupby(['Rotulo']).size())

y = dataframe['Rotulo']
X = dataframe.drop(columns=['Rotulo'])

#X=X[:1000]
#y=y[:1000]

k=[2,4,6,8,10]
for K in k:
   print('Reduzindo a dimensão de',len(X.columns),' para',K)
   start_t=datetime.now()
   XKd=X #PCA(n_components=K).fit_transform(X)
   print('Time elapsed:',datetime.now()-start_t)

   X_train, X_test, y_train, y_test = train_test_split(XKd,y,test_size=0.3,random_state=777)

   n_estimators = 700
   min_samples_split= 10

   print('Training ...')
   start_t=datetime.now()
   ExT = ExtraTreesClassifier(n_estimators=n_estimators,
                                     criterion= 'entropy',
                                     min_samples_split= min_samples_split,
                                     min_samples_leaf= min_samples_split, 
                                     class_weight='balanced_subsample',
                                     random_state=1,
                                     n_jobs=10,
                                     verbose=1)
   ExT.fit(X_train, y_train)
   print('Time elapsed:',datetime.now()-start_t)

   y_hat=ExT.predict(X_test)
   print('SEM PCA',K,'\n',classification_report(y_test,y_hat))
   break

# PCA = 4
#            precision    recall  f1-score   support
#
#         1.0       0.77      0.44      0.56   3951792
#         2.0       0.07      0.20      0.10    320349
#         3.0       0.08      0.21      0.11    361730
#         4.0       0.16      0.26      0.19    725087
#
#    accuracy                           0.38   5358958
#   macro avg       0.27      0.28      0.24   5358958
#   weighted avg       0.60      0.38      0.45   5358958

