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
textSer = " ".join(list(resdfInit['RESUME_TEXT']))
textSer = re.sub(r'[^a-zA-Z\-\.]+', ' ', textSer)

firstDashExpstr = r'\s+([-]+)([a-zA-Z]+)' 
finddash = re.findall(firstDashExpstr, textSer)
textSer2 = re.sub(firstDashExpstr, '\2' , textSer)
finddash = re.findall(firstDashExpstr, textSer2)


textSer = textSer2
sample = " aaa ignoreme .blabla fasdfdsa .net .com .hello hello hi  bbb .ignoreme .com ad bbb ignoreyou .ad"
firstDotExpstr = r'\s+([\.]+)(?!net|csv|txt|xls|com|in|doc|rtf|pdf|msi)([a-zA-Z]+?)' 
finddot = re.findall(firstDotExpstr, textSer, re.I|re.M)
textSer3 = re.sub(firstDotExpstr, r' \2' , textSer, re.I|re.M)
finddot = re.findall(firstDotExpstr, textSer3, re.I|re.M)


################## Tokenize ################## 
textSerTok =  word_tokenize(textSer3)

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
    cdata=[]
    firstDotExpstr = r'\s+([\.]+)(?!net|csv|txt|xls|com|in|doc|rtf|pdf|msi)([a-zA-Z]+?)' 
    firstDotExpstr = r'([\.-]+)(?!net|csv|txt|xls|com|in|doc|docx|exe|dll|rtf|pdf|msi)([a-zA-Z0-9-]+)' 
    for w in data:
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



