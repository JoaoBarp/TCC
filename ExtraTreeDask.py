from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
#from pandas import read_csv
from sklearn.model_selection import train_test_split
#import pandas as pd
from datetime import datetime
import sys
import dask.dataframe as ddf

filename='/media/Lun02_Raid0/joaob/'+sys.argv[1]

perg2 = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']

print('Começou ler...')
print(filename)
start_t=datetime.now()
dataframe=ddf.read_csv(filename,sep='\t',usecols=perg2, encoding='utf-8')
print('Acabou ler ...',datetime.now()-start_t)
dataframe=dataframe.dropna()

print(dataframe.groupby(['Rotulo']).size())

y = dataframe['Rotulo']
X = dataframe.drop(columns=['Rotulo'])

#X=X[:1000]
#y=y[:1000]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=777)

n_est=[100,120,150,200,250]
crit=['entropy','gini']
mxfeat=[0.1,0.4,0.6,0.8,1]
mxsam=[0.6, 0.8,0.9]
mnsamsp=[2, 4, 10, 20]
mnsamle=[1, 4, 8, 10, 16]
for ne in n_est:
	for c in crit:
		for mf in mxfeat:
			for ms in mxsam:
				for mss in mnsamsp:
					for msl in mnsamle:
						print('Combination:\n','\tn_estimator:',ne,'\n\tcriterion: ',c,'\n\tmax_features: ',mf)
						print('\tmax_samples:',ms,'\n\tmin_samples_split:',mss,'\n\tmin_samples_leaf:',msl)
						print('Training ...')
						start_t=datetime.now()
						ExT = ExtraTreesClassifier(n_estimators=ne,
                                     criterion= c,
                                     max_features=mf, 
                                     max_samples = ms,
                                     min_samples_split= mss,
                                     min_samples_leaf= msl,
                                     class_weight='balanced_subsample',
                                     random_state=1,
                                     n_jobs=10,
                                     verbose=1)
						ExT.fit(X_train, y_train)
						print('Testing ...')
						start_t=datetime.now()
						y_hat=ExT.predict(X_test)
						print('Time elapsed:',datetime.now()-start_t)
						print('Report:\n',classification_report(y_test,y_hat))
