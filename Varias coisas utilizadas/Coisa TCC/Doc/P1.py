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


#tool = language_check.LanguageTool('en-US')
DTags = {}
DUsers = {}

dictRESP = {}
dictPERG = {}
dictDataRespsPERG = {}

def ErroLing(Texto):
    Texto = limpaTexto(Texto)
    matches = tool.check(Texto)
    return len(matches)

def Ntags(Texto):
  Texto = Texto.replace('<',' ').replace('>',' ')
  Texto = Texto.split()
  return len(Texto)

def SomaCount(Texto):
    Texto = Texto.replace('<',' ').replace('>',' ')
    #Texto = limpaTexto(Texto)
    #Texto = Texto.replace('&amp;lt;',' ').replace('&amp;gt;',' ')
    Texto = Texto.split()
    y=0
    for x in Texto:
        try:
            y=y+int(DTags[x])
        except:
            y=y+0

    if not Texto:
        return 0
    else:
        return y


def temCod(Texto):
  y = re.findall('<code>[^>]+</code>',Texto)
  if len(y)>0:
    return 1
  else:
    return 0

def limpaTexto(Texto):
  tagremove = re.compile(r'(<!--.*?-->|<[^>]*>)')
  Texto = cgi.escape(tagremove.sub('', re.sub('<code>[^>]+</code>', '', Texto)))
  Texto = Texto.replace('\r\n','').replace('\n','')
  Texto = Texto.replace('?','')
  #print(Texto)
  return Texto

def contaPalavras(Texto):
  Texto = limpaTexto(Texto)
  #print(len(re.split(r'[:;.]+',Texto)),' ',re.split(r'[:;.]+',Texto))
  #print(re.split('\W+',Texto))
  print(Texto)
  return len(re.split('\W',Texto))

def contaFrases(Texto):
  Texto = limpaTexto(Texto)
  return len(re.split(r'[:;.?]+',Texto))

def legibilidade(Texto):
  Texto = limpaTexto(Texto)
  x = textstat.flesch_reading_ease(Texto)
  return x

def mediaCaracteresFrase(Texto):
  Texto = limpaTexto(Texto)
  Texto = re.split(r'[:;.]+',Texto)
  x = [len(i) for i in Texto]
  return format(sum(x)/len(Texto), '.4f')

def tamCod(Texto):
  exp = re.compile('<.*?>')
  cod = re.findall('<code>[^>]+</code>',Texto)
  if len(cod)>0:
    aux = [re.sub(exp, '', i) for i in cod]
    b = [len(i) for i in aux]
    b = sum(b)
    return b
  else:
    return 0

def interogacao(Texto):
  if '?' in Texto:
    return 1
  else:
    return 0;

def iniciaWH(Texto):
  Texto = Texto.split()
  x = Texto[0].lower()
  if x.startswith('wh') or x == 'how':
    return 1
  else:
    return 0;

def subjectivity(Texto):
  Texto = limpaTexto(Texto)
  testimonial = TextBlob(Texto)
  #print('Subje: ',testimonial.sentiment)
  return format(testimonial.sentiment.subjectivity, '.4f')

def polaridade(Texto):
    Texto = limpaTexto(Texto)
    testimonial = TextBlob(Texto)
    #print('Subje: ',testimonial.sentiment)

    return format(testimonial.sentiment.polarity, '.4f')


def attPerg(key,val):
    if key not in dictPERG:
        dictPERG[key] = [val]
    else:
        dictPERG[key].append(val)



def attResp(key,val):
    if key not in dictRESP:
        dictRESP[key] = [val]
    else:
        dictRESP[key].append(val)


def attdictDataRespsPERG(key,val):
    if key not in dictDataRespsPERG:
        dictDataRespsPERG[key] = [val]
    else:
        dictDataRespsPERG[key].append(val)




#--------MAIN--------------

#===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//

def parseUser():
    i=0
    context = etree.iterparse("Users.xml", events=('end',))

    for action, elem in context:
        if elem.tag=='row':
            if i%500 == 0:
                print('User: ',i, end='')
            #if i == 500000:
            #    break

            Id = elem.attrib['Id']
            DUsers[int(Id)]=Id
            i+=1
            print('\r\r\r',end='')
            pass

        elem.clear()

        while elem.getprevious() is not None:
            del elem.getparent()[0]

#TAGS
#===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//
i=0
print('\n')
#print('\nComecou Tags')
with open('Tags.xml') as Tags:
    for _, elem in iterparse('Tags.xml', events=("end",)):
        if elem.tag == "row":
            if i%10 == 0:
                print('Tags: ',i, end='')
            #doc = xml.etree.ElementTree.fromstring(Tag)
            TagName = elem.attrib['TagName']
            Count = elem.attrib['Count']
            DTags[TagName] = Count
            i+=1
            print('\r\r\r',end='')

#===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//


i=0
#PerG={}
ResP={}
d1    =   "2108-08-04 04:48:40.697"
countPerg = Counter()
countResp = Counter()
inicio = time.time()

def parsePost():
    PerG={}
    countARQ = 0
    i=0
    context = etree.iterparse("Post.xml", events=('end',))
   # process = psutil.Process(os.getpid())
    for action, elem in context:
        if elem.tag=='row':
            variavel=[]
            if i%500 == 0:
                print('Post: ',i,end='')
            i+=1
            if i == 50:
                break

            print('\r\r\r',end='')
            #doc = xml.etree.ElementTree.fromstring(Post)
            if 'Id' in elem.attrib and 'PostTypeId' in elem.attrib and 'CreationDate' in elem.attrib:
                Id                  =   elem.attrib['Id']
                PostTypeId          =   elem.attrib['PostTypeId']
                CreationDate  = datetime.strptime(elem.attrib['CreationDate'], "%Y-%m-%dT%H:%M:%S.%f")
                CreationDate = CreationDate.strftime("%Y-%m-%d %H:%M:%S")
            else:
                continue

            if PostTypeId == "1":
                if 'OwnerUserId' in elem.attrib:
                    OwnerUserId         =   elem.attrib['OwnerUserId']
                if OwnerUserId is not None  and int(OwnerUserId) in DUsers.keys():
                #variavel.append(-1)
                    variavel.append(int(OwnerUserId))
                    variavel.append(CreationDate)
                    if 'Body' in elem.attrib and 'Title' in elem.attrib and 'Tags' in elem.attrib:
                        Body        = elem.attrib['Body']
                        Title       = elem.attrib['Title']
                        Tags        = elem.attrib['Tags']

                    variavel.append(SomaCount(Tags))
                    variavel.append(temCod(Body))
                    variavel.append(contaPalavras(Body))
                    variavel.append(contaPalavras(Title))
                    variavel.append(contaFrases(Body))
                    variavel.append(legibilidade(Body))
                    variavel.append(mediaCaracteresFrase(Body))
                    variavel.append(tamCod(Body))
                    variavel.append(interogacao(Title))
                    variavel.append(iniciaWH(Title))
                    variavel.append(subjectivity(Body))
                    variavel.append(polaridade(Body))
                    variavel.append(Ntags(Tags))

                    PerG[int(Id)]=variavel

                    attPerg(int(OwnerUserId),CreationDate)

            elif PostTypeId == "2":
                if 'OwnerUserId' in elem.attrib:
                    OwnerUserId         =   elem.attrib['OwnerUserId']
                variavel.append(OwnerUserId)
                variavel.append(CreationDate)
                if 'ParentId' in elem.attrib:
                    ParentId            =   int(elem.attrib['ParentId'])
            #------print(OwnerUserId, ' ',CreationDate)
                variavel.append(int(ParentId))
                ResP[int(Id)]=variavel

                attdictDataRespsPERG(int(ParentId),CreationDate)

                if OwnerUserId is not None  and int(OwnerUserId) in DUsers.keys():
                    attResp(int(OwnerUserId),CreationDate)

                pass
            elem.clear()

            while elem.getprevious() is not None:
                del elem.getparent()[0]

            if (sys.getsizeof(PerG)/(1024*1024)) > 10000:
                nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Arq-" + str(countARQ)+'.json'
                with open(nArq, "w") as outfile:
                    json.dump(PerG, outfile)
                countARQ+=1
                PerG.clear()

    if (sys.getsizeof(PerG)/(1024*1024)) < 10000:
        nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Arq-" + str(countARQ)+'.json'
        with open(nArq, "w") as outfile:
            json.dump(PerG, outfile)
        countARQ+=1
        PerG.clear()

    return countARQ

#===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//===//
parseUser()

print("Valor dict users:",sys.getsizeof(DUsers))

countARQ = parsePost()

nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Dict\\dictPERG.json"
with open(nArq, "w") as outfile:
    json.dump(dictPERG, outfile)

nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Dict\\dictRESP.json"
with open(nArq, "w") as outfile:
    json.dump(dictRESP, outfile)

nArq = "C:\\Users\\joaor\\Desktop\\TCC\\Json\\Dict\\dictDataRespsPERG.json"
with open(nArq, "w") as outfile:
    json.dump(dictDataRespsPERG, outfile)

with open('countARQ.txt','w') as f:
    f.write(str(countARQ))
    f.close()
