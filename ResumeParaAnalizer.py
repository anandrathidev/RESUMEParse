# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:14:40 2018

@author: anandrathi
"""

from nltk.corpus import wordnet
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

import pandas as pd
import re
import numpy as np


#import enchant
from nltk.corpus import stopwords
STOP_WORDS=set(stopwords.words('english'))

xpath = "C:/Users/anand.rathi/Documents/tmp/ALEEP/"
xpath = "D:/Users/anandrathi/Documents/personal/Bussiness/Aleep/"

HEADINGS=set()
with open(xpath+"/Headings.txt","r") as HeadFile:
  for line in HeadFile.readlines():
    line=line.replace(":","").strip()
    HEADINGS.add(line)

HEADINGS=list(HEADINGS)

EMAIL_PATTERN = r'[\w\.-]+@[\w\.-]+'
NO_NAME = set(["phone","resume", "vitae" , "of", "curriculum", "curriculam"," carriculum", "curriculum-vitae",
              "profile", "email", "gmail", "com", "yahoo" , "vitae", "mail", "area", "experties", "telecommunication"
               "electronics",   "tele munication", "engineer" , "with",
               "yrs", "experience", "exp", "_", "engineer", "name", "career",
               "vision", "btech", "apartment", "analyst",
                'databae', 'developer',  'adminisrator', "release" "years" "contact", "details"
                 "objectives", "achieving", "challenging", "position", "field",
                 "database", "best", "knowledge", "creative", ",mind", ",synergistic", "whole", "strive",
                 ",excellence" ,"highest", "echelons", "technical", "level",
                  "professional", "summary","pic", "b tech"
               ,"\t"])
len(NO_NAME)

PAT = re.compile(EMAIL_PATTERN)

resdfInit = pd.read_json(xpath + "ALLRES.json", orient='records')
list(resdfInit.columns)
resdfInit.head(1).index
res1 = resdfInit['RESUME_TEXT'].head(1)[0]

HeadingDFJson = pd.read_json(xpath + "HeadingsJSON.json", orient='records')
list(HeadingDFJson.columns)
HeadingDFJson['HEADINGS']




#from nameparser.parser import HumanName

def extract_entities(text):
  allnames=""
  for sent in nltk.sent_tokenize(text):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
      #print("chunk {}".format(chunk))
      #print("chunk {}".format(chunk))
      if (chunk[1] == 'VBN' or
          chunk[1] == 'VBP' or
          chunk[1] == 'VBG' or
          chunk[1] == 'VBD' or
          chunk[1] == 'IN' or
          chunk[1] == 'CC' or
          chunk[1] == 'VB' ):
        pass
      else:
        if hasattr(chunk, 'label'):
          names=' '.join(c[0] for c in chunk.leaves())
          allnames = allnames + " " + names
        else :
          #log.write( str("chunk {}".format(chunk) + "\n").encode('ascii', errors='ignore').decode('ascii', errors='ignore') )
          if(chunk[1] == 'JJ' and len(chunk[0])>2 ):
            pass
          allnames = allnames + " " + chunk[0]
  #return(allnames.strip())
  return(pd.Series( { "nameline": allnames} ))

def get_human_names(text):
  tokens = nltk.tokenize.word_tokenize(text)
  pos = nltk.pos_tag(tokens)
  sentt = nltk.ne_chunk(pos, binary = False)
  print("sentt {}".format(sentt))
  person_list = []
  person = []
  name = ""
  def Filterlambda( t):
    #print("t {}".format(t));
    label=t.label()
    print("label {}".format(t.label));
    return label == 'PERSON'

  subtreeList = list(sentt.subtrees(filter=lambda t: Filterlambda(t) ))
  #subtreeList = list(sentt.subtrees(filter=lambda t: t.label() == 'PERSON'))
  print("subtreeList {}".format(subtreeList))
  for subtree in subtreeList:
    print("subtree={}".format(subtree))
    for leaf in subtree.leaves():
      print("leaf={}".format(leaf[0]))
      person.append(leaf[0])
      print("person={}".format(person))
      if len(person) > 1: #avoid grabbing lone surnames
        for part in person:
          name += part + ' '
          print("name[:-1]={}".format(name[:-1]))
          if name[:-1] not in person_list:
            person_list.append(name[:-1])
        #name = ''
      #person = []
  print(name)
  return pd.Series( { "nameline": name} )


headings=[]
def ExtractHeading(x):
  #Parainfo={}
  paraList = x.lstrip().split("\n\n")
  total = sum([len(para) for para in  paraList])
  avgwords = np.average([len(para.split()) for para in  paraList])
  headingsSet = set(headings)
  headingsSet.update(set([ para for para in  paraList  if len(para.split()) < 4 ]))
  headings.clear()
  headings.extend(list(headingsSet))

def getHeadingSet():
  nonedf = pd.DataFrame(resdfInit.apply(lambda x: ExtractHeading(x=x['RESUME_TEXT']) , axis=1))
  Heading = HeadingDFJson['HEADINGS'].tolist()
  HeadingTxt = ",".join(Heading)
  HeadingSet = set([  h.strip() for h in HeadingTxt.split(",")])
  return (HeadingSet)


from collections import Counter
words = []
for morewords in firstLineDF['Firstline'].str.split() :
  #print(type(morewords))
  words.extend(morewords)
wordcount = Counter(words)

