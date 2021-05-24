# TCC

**Link databases**:https://drive.google.com/drive/folders/1xdFhtToRCFQTtnQGJomsqn1QZPGPEEUv?usp=sharing  
## Data4classFULL.csv: Database completo com 4 classes.
### Classes  
- (Minutos >= 0 & Minutos <= 1440) = 1  
- (Minutos >1440) & (Minutos <= 10080) = 2  
- (Minutos > 10080) = 3  
- (Minutos == -1) = 4 (Sem resposta)
### Número de amostras em cada classe:
1 = 13171169  
2 = 1067850  
3 = 1205715   
4 = 2418457  

## Data4classNearmiss.csv : Database reduzido após processo utilizando Near-Miss  
O que é o algoritmo Near-Miss?  

Near-miss é um algoritmo que pode ajudar a equilibrar um conjunto de dados desequilibrado. Ele pode ser agrupado em algoritmos de subamostragem e é uma maneira eficiente de equilibrar os dados. O algoritmo faz isso observando a distribuição da classe e eliminando aleatoriamente as amostras da classe maior. Quando dois pontos pertencentes a classes diferentes estão muito próximos um do outro na distribuição, este algoritmo elimina o ponto de dados da classe maior, tentando equilibrar a distribuição.  
### Classes  
- (Minutos >= 0 & Minutos <= 1440) = 1  
- (Minutos >1440) & (Minutos <= 10080) = 2  
- (Minutos > 10080) = 3  
- (Minutos == -1) = 4 (Sem resposta)
### Número de amostras em cada classe:
1 = 1067850  
2 = 1067850  
3 = 1067850   
4 = 1067850  


