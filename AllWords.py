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
print("Data frame Size : {}".format(resdfInit.size))
sentenses=[]
for r in  list(resdfInit['RESUME_TEXT']):
    r = r.encode().decode("ascii", "ignore").lower()
    r=r.replace(r"'","").replace(r"`","").replace(r"-"," ").replace(r""," ").replace(r"..."," ").replace(r"-.com","").replace("•", " ").replace('"', "").replace('(', " ").replace(')', " ").replace('/', " ")
    r=r.replace(r"c++","cpp")
    sentenses.extend( [ l for l in r.splitlines() if len(l)>1 ] )

sentensesOrig = sentenses
print("Number of sentenses: {}".format(len(sentenses)))

ostrlen = sum([ len(s) for s in sentenses] )
print("Full text Length ={}".format(ostrlen))

################## REMOVE number non alpha words ################## 
#textSer = re.sub(r'[^a-zA-Z\-\.\s\+#]+', ' ', textSer)
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_short

sentenses = [ strip_short(strip_punctuation(strip_numeric(s)),minsize=2) for s in sentenses]
sentensesOrig1 = sentenses


#from gensim.parsing.preprocessing import stem_text
#stem_text("logs")

strlenAfterNumbers = sum([ len(s) for s in sentenses] )
print("strlenAfter strip numbers  ={}".format(strlenAfterNumbers))
print("% change  ={}".format((ostrlen- strlenAfterNumbers)*100/ostrlen))
print("Number of sentenses: {}".format(len(sentenses)))

################## REMOVE  -AAA ################## 

firstDashExpstr = r'\s+([-]+)([a-zA-Z]+)' 
#finddash = re.findall(firstDashExpstr, textSer)
finddash = [ re.findall(firstDashExpstr, s) for s in sentenses]
sentenses = [ re.sub(firstDashExpstr, '\2' , s) for s in sentenses]
finddash = [ re.findall(firstDashExpstr, s) for s in sentenses]


strlenAfterDashExpstr = sum([ len(s) for s in sentenses] )
print("strlenAfterDashExpstr ={}".format(strlenAfterDashExpstr))
print("% change  ={}".format((strlenAfterDashExpstr- strlenAfterNumbers)*100/strlenAfterNumbers))
print("Number of sentenses: {}".format(len(sentenses)))



################## REMOVE  .AAA ################## 

sample = " aaa ignoreme .blabla fasdfdsa .net .com .hello hello hi  bbb .ignoreme .com ad bbb ignoreyou .ad"
firstDotExpstr = r'\s+([\.]+)(?!net|csv|txt|xls|com|in|doc|rtf|pdf|msi)([a-zA-Z]+?)' 

finddot = [ re.findall(firstDotExpstr, s) for s in sentenses]
sentenses = [ re.sub(firstDotExpstr, '\2' , s) for s in sentenses]
finddot = [ re.findall(firstDotExpstr, s) for s in sentenses]

strlenAfterDotExpstr = sum([ len(s) for s in sentenses] )
print("strlenAfterDotExpstr ={}".format(strlenAfterDotExpstr))
print("% change  ={}".format((strlenAfterDotExpstr - strlenAfterDashExpstr )*100/strlenAfterDashExpstr))



def cleanData(data):
    textSerTok =  word_tokenize(data)
    cdata=[]
    firstDotExpstr = r'\s+([\.]+)(?!net|csv|txt|xls|com|in|doc|rtf|pdf|msi)([a-zA-Z]+?)' 
    firstDotExpstr = r'([\.-]+)(?!net|csv|txt|xls|com|in|doc|docx|exe|dll|rtf|pdf|msi)([a-zA-Z0-9-]+)' 
    for w in textSerTok:
        w=w.replace(r"|"," ")
        w=w.replace(r"-"," ")
        w=w.replace(r"","")
        w=w.replace(r"...","")
        w=w.replace(r"-.com","")
        w=w.lower().strip()
        w = re.sub(firstDotExpstr, r'\2' , w, re.I|re.M)
        w = re.sub(firstDashExpstr, '\2' , w, re.I|re.M)
        w=w.strip()
        if len(w)<2:
            continue
        cdata.append(w)
    return cdata
  
print("Number of sentenses: {}".format(len(sentenses)))
len(sentenses)
#sentenses = [cleanData(s) for s in sentenses]
#sentenses = [s for s in sentenses if len(s)>0]

print("after cleanData Number of sentenses: {}".format(len(sentenses)))
print(sentenses[100:200])

sentenses = [word_tokenize(s) for s in sentenses]
print("After tokens Number of sentenses: {}".format(len(sentenses)))

import gensim
from gensim import models
from gensim.models import KeyedVectors
phrases = gensim.models.Phrases(sentenses)
bigram = gensim.models.phrases.Phraser(phrases)
model = models.Word2Vec(bigram[sentenses], size=351, window=5, min_count=1,
                        max_vocab_size=None, workers=4,
                        compute_loss=True)
print("vocab size {}".format(len(model.wv.vocab)))
vocab = list(model.wv.vocab)
print("vocab size {}".format( vocab[0:300]))


fname = "/w2vec.bin"
model.save(xpath + fname)

"science" in vocab


print("similarity 'script', 'java' {}".format(model.wv.similarity('script', 'java')))
print("similarity  'script', 'python' {}".format(model.wv.similarity('script', 'python')))

print("similarity 'programming', 'java' {}".format(model.wv.similarity('programming', 'java')))
print("similarity  'programming', 'python' {}".format(model.wv.similarity('programming', 'python')))

print("similarity 'programming', 'R' {}".format(model.wv.similarity('programming', 'java')))
print("similarity  'programming', 'python' {}".format(model.wv.similarity('programming', 'python')))

print("similarity 'science', 'java' {}".format(model.wv.similarity('science', 'java')))
print("similarity  'science', 'python' {}".format(model.wv.similarity('science', 'python')))
print("similarity  'science', 'scala' {}".format(model.wv.similarity('science', 'scala')))

print("similarity 'datascience', 'java' {}".format(model.wv.similarity('datascience', 'java')))
print("similarity  'datascience', 'python' {}".format(model.wv.similarity('datascience', 'python')))
print("similarity  'datascience', 'scala' {}".format(model.wv.similarity('datascience', 'scala')))


print("similarity 'bigdata', 'java' {}".format(model.wv.similarity('bigdata', 'java')))
print("similarity  'bigdata', 'python' {}".format(model.wv.similarity('bigdata', 'python')))
print("similarity  'bigdata', 'scala' {}".format(model.wv.similarity('bigdata', 'scala')))

print("similarity 'bigdata', 'datascience' {}".format(model.wv.similarity('bigdata', 'datascience')))





#model = Word2Vec.load(fname)
