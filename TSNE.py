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

sns.scatterplot(x="comp-1", y="comp-2", hue=df.y.tolist(),
                palette=sns.color_palette("hls", 10),
                data=df).set(title="MNIST data T-SNE projection")

plt.scatter(df[:,0],df[:,1], c=y_new)
plt.title('Horse Colic - PCA')
#plt.title('Horse Colic - TSNE')
plt.xlabel('Column 0')
plt.ylabel('Column 1')
plt.legend()
plt.show()
