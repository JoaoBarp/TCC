from pandas import read_csv
import pandas as pd
import numpy as np
import csv
import datetime
from datetime import datetime
import holidays
from scipy.stats import norm
import seaborn as sns, numpy as np
from matplotlib import pyplot

from scipy import stats

SEED =  19963
# load data
perg = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']

print('Começou...')
Perguntas=pd.read_csv('C:\\Users\\joaor\\Desktop\\2classesFF.csv',sep='\t',usecols=perg)
print('Acabou...')


perg = ['N Palavras corpo','N Palavras Titulo','N frases corpo','flesch','Media Caracteres Frase','Tamanho Codigo','Interogacao','Inicia com WH','Subjetividade','Polaridade','N de tags','N perguntas Feitas','N respostas Feitas','Rotulo']
Feature = 'N de tags'

#Perguntas = Perguntas.loc[Perguntas[Feature]< 500]
#cats, binss = pd.cut(Perguntas[Feature],50, retbins=True)
binss = [1,2,3,5,Perguntas[Feature].max()]
x1 = Perguntas.loc[Perguntas.Rotulo==1, Feature]
x2 = Perguntas.loc[Perguntas.Rotulo==2, Feature]
'''
print('Média por classe: ', Feature)
print('C0 média : ' , x1.mean())
print('C1 média : ' , x2.mean())
print('C2 média : ' , x3.mean())

'''
#=================//=========================================================//===================================================//=================================
g = sns.kdeplot(Perguntas[Feature][(Perguntas['Rotulo'] == 1) & (Perguntas[Feature])], color="Red", shade = False)
g = sns.kdeplot(Perguntas[Feature][(Perguntas['Rotulo'] == 2) & (Perguntas[Feature])], ax =g, color="Blue", shade= False)

g.set_xlabel('Número de tags')
g.set_ylabel("Frequencia")
g = g.legend(['1','2'])
pyplot.show()
#=================//=========================================================//===================================================//=================================

fig,ax = pyplot.subplots(ncols=2)

hist, bin_edges = np.histogram(x1,binss,density=1)
ax[0].bar(range(len(hist)),hist,width=1,align='center',tick_label=
        ['{}-{}'.format(binss[i],binss[i+1]) for i,j in enumerate(hist)])
ax[0].tick_params(axis='x', rotation=30)
ax[0].set_title("Classe 0")
ax[0].set_xlabel(Feature)
ax[0].set_ylabel('Probabilidade')

hist, bin_edges = np.histogram(x2,binss,density=1)
ax[1].bar(range(len(hist)),hist,width=1,align='center',tick_label=
        ['{} - {}'.format(binss[i],binss[i+1]) for i,j in enumerate(hist)])
ax[1].tick_params(axis='x', rotation=30)
ax[1].set_title("Classe 1")
ax[1].set_xlabel(Feature)
ax[1].set_ylabel('Probabilidade')


pyplot.show()

ax= sns.boxplot(x="Rotulo", y=Feature, data=Perguntas)
pyplot.show()


print(Perguntas[Feature].describe().apply(lambda x: format(x, 'f')))

'''
kwargs = dict(alpha=0.5, bins=binss, density=True, stacked=True)
pyplot.hist(x1, **kwargs,width=10, color='g', label='0')
pyplot.hist(x2, **kwargs,width=10, color='b', label='1')
pyplot.hist(x3, **kwargs,width=10, color='r', label='2')
pyplot.gca().set(title=Feature, ylabel='Probabilidade')
pyplot.legend();
pyplot.xticks(binss)
pyplot.show()



facet = sns.FacetGrid(Perguntas, hue='Rotulo',aspect=4)
facet.map(sns.kdeplot,Feature,shade= True)
facet.set(xlim=(0, Perguntas[Feature].max()))
facet.add_legend()
pyplot.show()

'''

'''
kwargs = dict(alpha=0.5, bins=5)
x1 = Perguntas.loc[Perguntas.Rotulo==1,'Tamanho Codigo']
x2 = Perguntas.loc[Perguntas.Rotulo==2,'Tamanho Codigo']
x3 = Perguntas.loc[Perguntas.Rotulo==3, 'Tamanho Codigo']
pyplot.hist(x1, **kwargs, color='b', label='1')
pyplot.hist(x2, **kwargs, color='r', label='2')
pyplot.hist(x3, **kwargs, color='g', label='3')
pyplot.show()
'''


'''
pyplot.hist(Perguntas[Feature],
         bins=binss.tolist(),
         density=False,
         histtype='bar',
         color='b',
         edgecolor='k',
         alpha=0.5)

pyplot.xlabel('Commute time (min)')
pyplot.xticks(binss.tolist())
pyplot.ylabel('Number of commuters')
pyplot.title('Histogram of commute times')

pyplot.show()
'''
