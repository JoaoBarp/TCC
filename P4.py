# -*- coding: utf-8 -*-
from collections import defaultdict
from matplotlib import pyplot as plt
import xml.etree.ElementTree
import pandas as pd
from datetime import datetime, timedelta
import time
import re, cgi, os, pickle, logging, time
from textblob import TextBlob
#import language_check
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


perg = ['OwnerUserId','CreationDate','Ntags','TemCodigo','CountPalavrasBody','CountPalavrasTitle','Nfrasesbody','flesch_reading_ease','mediaCaracteresFrase','tamCod','interogacao','iniciaWH','subjectivity','polaridade','sumT','NpergFei','NresFei','Minutos']

print('Começou...')
Perguntas=pd.read_csv('DataFramePerg.csv',sep='\t',usecols=perg)
Perguntas=Perguntas.loc[(Perguntas.Minutos >= -1)]
print('Acabou...')



Perguntas.loc[(Perguntas.Minutos >= 0) & (Perguntas.Minutos <= 480),'Rotulo'] = 'C1'
Perguntas.loc[(Perguntas.Minutos > 480) & (Perguntas.Minutos <= 960),'Rotulo'] = 'C2'
Perguntas.loc[(Perguntas.Minutos > 960) & (Perguntas.Minutos <= 1440),'Rotulo'] = 'C3'
Perguntas.loc[(Perguntas.Minutos > 1440) & (Perguntas.Minutos < 2280),'Rotulo'] = 'C4'
Perguntas.loc[(Perguntas.Minutos > 2280) & (Perguntas.Minutos <= 5790),'Rotulo'] = 'C5'
Perguntas.loc[(Perguntas.Minutos > 5790),'Rotulo'] = 'C6'
Perguntas.loc[(Perguntas.Minutos == -1) ,'Rotulo'] = 'C7'

Perguntas = Perguntas.drop(columns=['OwnerUserId'])
Perguntas = Perguntas.drop(columns=['CreationDate'])
Perguntas = Perguntas.drop(columns=['Ntags'])
Perguntas = Perguntas.drop(columns=['TemCodigo'])
Perguntas = Perguntas.drop(columns=['Minutos'])


print(Perguntas.head())



Perguntas.to_csv('DataParaTreino.csv', sep='\t', encoding='utf-8')
