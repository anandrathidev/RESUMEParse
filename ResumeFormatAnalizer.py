# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:31:29 2018

@author: Anand.RATHI
"""

import pandas as pd
from nltk.corpus import wordnet
import re
import enchant

EMAIL_PATTERN = r'[\w\.-]+@[\w\.-]+'
STOP_WORDS = ["resume", "vitae" , "of", "curriculum", "curriculum-vitae", 
              "profile", "email", "gmail", "com", "yahoo" , "vitae", 
               "electronics",   "tele munication", "engineer" , "with",
               "yrs", "experience", "exp"]
PAT = re.compile(EMAIL_PATTERN)

xpath = "C:/Users/anand.rathi/Documents/tmp/ALEEP/"
resdfInit = pd.read_json(xpath + "ALLRES.json", orient='records')

list(resdfInit.columns)

resdfInit.head(1).index

res1 = resdfInit['RESUME_TEXT'].head(1)[0]

def ReplaceEmail(emails, x):
  if len(emails)>0:
    for email in emails:
      x.replace(email,'')
  return pd.Series( {"TEXT":x}) 

def ExtractEmail(x):
  emails = PAT.findall(x)
  return  { "emailsCount": len(emails) , "emails":emails}

def removeStopWords(x):
  for sw in STOP_WORDS:
    x=x.replace(sw," ")
    pass
  #for xw in x.split():
  #  if wordnet.synsets(xw):
       #English Word
  #    x=x.strip().replace(xw," ")  
  return x 

def ExtractFirstLine(x):
  newx=""
  for name in x.lstrip().splitlines()[0:4]:
    emails = ExtractEmail(name)["emails"]
    for email in emails:
      name=name.replace(email,' ')
    
    newx1 = re.sub(r'[0-9]+', ' ', name)
    newx1 = newx1.strip().lower()
    newx1=re.sub(r'[^\s\w_]+',' ',newx1).strip()
    newx1=removeStopWords(newx1).strip()
    if len(newx1) >2:
      newx = newx + " " + newx1
      break
  return pd.Series( { "Firstline": newx } ) 

  
def ExtractName(x):
  newx=""
  for name in x.lstrip().splitlines()[0:4]:
    newx1 = re.sub(r'[0-9]+', '', name)
    newx1 = newx1.strip().lower()
    newx1=re.sub(r'[^\s\w_]+',' ',newx1).strip()
    newx1=removeStopWords(newx1).strip()
    if len(newx1) >2:
      newx = newx + " " + newx1
      break
  nameline = " ".join(x.lstrip().splitlines()[0:3])
  emails = ExtractEmail(nameline)["emails"]
  for email in emails:
    print("replace email {} ".format(email))
    nameline=nameline.replace(email,'')
  return pd.Series( { "nameline": nameline} ) 

## Extract Email   
emailsDF = pd.DataFrame(resdfInit.apply(lambda x: pd.Series(ExtractEmail(x['RESUME_TEXT'])) , axis=1))

resdf = pd.merge(resdfInit, emailsDF, left_index=True, right_index=True)

firstLineDF = pd.DataFrame(resdf.apply(lambda x: ExtractFirstLine(x['RESUME_TEXT']) , axis=1))

#namesDF = pd.DataFrame(resdf.apply(lambda x: ExtractName(x['RESUME_TEXT']) , axis=1))

from collections import Counter
words = []
for morewords in firstLineDF['Firstline'].str.split() :
  #print(type(morewords))
  words.extend(morewords)
wordcount = Counter(words)

resdf.head(1)['RESUME_TEXT'][0].splitlines(True)

"anand\n\n\n\n\nrathi anand@anand.com\n\n".splitlines(True)
"anand\n\n\n\n\nrathi anand@anand.com\n\n".splitlines(False)

## Extract Name 

import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

import nltk
from nameparser.parser import HumanName

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)
        
        
get_human_names(res1)