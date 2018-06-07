# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:20:41 2018

@author: he159490
"""

import pandas as pd
import re
import numpy as np
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words
from nltk.corpus import wordnet 

#xpath = "D:/Users/anandrathi/Documents/personal/Bussiness/Aleep/"
xpath = "C:/temp/DataScience/Aleep/GIT/RESUMEParse/"

nltk.download('punkt')
nltk.download('words')
nltk.download('wordnet')

resdfInit = pd.read_json(xpath + "ALLRES.json", orient='records')
list(resdfInit.columns)
textSer = r"\n\n\n".join(list(resdfInit['RESUME_TEXT']))
sentenses = textSer.splitlines()
print(resdfInit.size)
print("Number of sentenses: {}".format(len(sentenses)))

ostrlen = len(textSer)

print("Full text Length ={}".format(ostrlen))

################## REMOVE number non alpha words ################## 
textSer = re.sub(r'[^a-zA-Z\-\.\s]+', ' ', textSer)
strlenAfterNumbers = len(textSer)
print("strlenAfterNumbers ={}".format(strlenAfterNumbers))
print("% change  ={}".format((ostrlen- strlenAfterNumbers)/ostrlen))

sentenses = textSer.splitlines()
print("Number of sentenses: {}".format(len(sentenses)))

################## REMOVE  -AAA ################## 

firstDashExpstr = r'\s+([-]+)([a-zA-Z]+)' 
finddash = re.findall(firstDashExpstr, textSer)
textSer2 = re.sub(firstDashExpstr, '\2' , textSer)
finddash = re.findall(firstDashExpstr, textSer2)
textSer=textSer2
strlenAfterDashExpstr = len(textSer)
print("strlenAfterDashExpstr ={}".format(strlenAfterDashExpstr))
print("% change  ={}".format((strlenAfterDashExpstr- strlenAfterNumbers)/strlenAfterNumbers))
sentenses = textSer.splitlines()
print("Number of sentenses: {}".format(len(sentenses)))

################## REMOVE  .AAA ################## 

sample = " aaa ignoreme .blabla fasdfdsa .net .com .hello hello hi  bbb .ignoreme .com ad bbb ignoreyou .ad"
firstDotExpstr = r'\s+([\.]+)(?!net|csv|txt|xls|com|in|doc|rtf|pdf|msi)([a-zA-Z]+?)' 
finddot = re.findall(firstDotExpstr, sample, re.I|re.M)
sample = re.sub(firstDotExpstr, r' \2' , sample, re.I|re.M)
finddot = re.findall(firstDotExpstr, sample, re.I|re.M)

finddot = re.findall(firstDotExpstr, textSer, re.I|re.M)
textSer3 = re.sub(firstDotExpstr, r' \2' , textSer, re.I|re.M)
finddot = re.findall(firstDotExpstr, textSer3, re.I|re.M)
textSer = textSer3 
strlenAfterDotExpstr = len(textSer)
print("strlenAfterDotExpstr ={}".format(strlenAfterDotExpstr))
print("% change  ={}".format((strlenAfterDotExpstr - strlenAfterDashExpstr )/strlenAfterDashExpstr))

print("strlenAfterDashExpstr ={}".format(strlenAfterDashExpstr))
print("% change  ={}".format((strlenAfterDashExpstr- strlenAfterNumbers)/strlenAfterNumbers))
sentenses = textSer.splitlines()
print("Number of sentenses: {}".format(len(sentenses)))

if False:
    ################## Tokenize ################## 
    textSerTok =  word_tokenize(textSer)
    
    ################## Unique ################## 
    textSerTokSet = set(textSerTok)
    
    ################## filter non english  ################## 
    
    type(words.words())
    type(wordnet.words() )
    manywords = set([ w.lower() for w in words.words() + list(wordnet.words())])
    len(manywords)
    
    NonEngWords = set()
    EngWords = set()
    for w in textSerTokSet:
        w=w.replace(r"-"," ")
        w=w.replace(r"","")
        w=w.replace(r"...","")
        w=w.replace(r"-.com","")
        w=w.lower().strip()
        firstDotExpstr = r'\s+([\.]+)(?!net|csv|txt|xls|com|in|doc|rtf|pdf|msi)([a-zA-Z]+?)' 
        firstDotExpstr = r'([\.-]+)(?!net|csv|txt|xls|com|in|doc|docx|exe|dll|rtf|pdf|msi)([a-zA-Z0-9-]+)' 
        finddot = re.match(firstDotExpstr, textSer, re.I|re.M)
        w = re.sub(firstDotExpstr, r'\2' , w, re.I|re.M)
        w = re.sub(firstDashExpstr, '\2' , w, re.I|re.M)
        w=w.strip()
        if w=="":
            continue
        if w in manywords:
            EngWords.add(w)
        else:
            NonEngWords.add(w)
    
    NonEngWords = list(NonEngWords)
    EngWords = list(EngWords)

def cleanData(data):
    textSerTok =  word_tokenize(data)
    cdata=[]
    firstDotExpstr = r'\s+([\.]+)(?!net|csv|txt|xls|com|in|doc|rtf|pdf|msi)([a-zA-Z]+?)' 
    firstDotExpstr = r'([\.-]+)(?!net|csv|txt|xls|com|in|doc|docx|exe|dll|rtf|pdf|msi)([a-zA-Z0-9-]+)' 
    for w in textSerTok:
        w=w.replace(r"-"," ")
        w=w.replace(r"","")
        w=w.replace(r"...","")
        w=w.replace(r"-.com","")
        w=w.lower().strip()
        w = re.sub(firstDotExpstr, r'\2' , w, re.I|re.M)
        w = re.sub(firstDashExpstr, '\2' , w, re.I|re.M)
        w=w.strip()
        if w=="":
            continue
        cdata.append(w)
    return " ".join(cdata)
  
sentenses = textSer.splitlines()
print("Number of sentenses: {}".format(len(sentenses)))
sentenses = [cleanData(s) for s in sentenses]
print("Number of sentenses: {}".format(len(sentenses)))


import gensim
from gensim import models
from gensim.models import KeyedVectors
bigram_transformer = gensim.models.Phrases(sentenses)
model = models.Word2Vec(bigram_transformer[sentenses], size=311, window=5, min_count=3, workers=4)
fname = "/w2vec.bin"
model.save(xpath + fname)
#model = Word2Vec.load(fname)
