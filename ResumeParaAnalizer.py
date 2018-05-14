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
res1 = resdfInit['RESUME_TEXT'].head(10000)[202]
print(res1)

def GetHeadingsSets():
  from itertools import chain
  HeadingDFJson = pd.read_json(xpath + "HeadingsJSON.json", orient='records')
  list(HeadingDFJson.columns)
  HList =  [ htokl.split(",") for htokl in  list(HeadingDFJson['HEADINGS'])  ]
  HList =  [ Hitem.strip().lower() for Hitem in list(chain(*HList)) if Hitem.strip().lower() !="" ]
  return set( HList[:] )

#from nameparser.parser import HumanName

HeadSet = list(GetHeadingsSets())

def CreateHeadRegExp(HeadSet):
  HeadExtraxtRegStr = r"(" + r"|".join(HeadSet) +   r")[: ]*" + r"(.*?)" + r"(" + r"|".join(HeadSet) +   r")"
  HeadExtraxtRe = re.compile(HeadExtraxtRegStr, flags= re.I | re.DOTALL )
  return HeadExtraxtRe

HeadExtraxtRe = CreateHeadRegExp(HeadSet)
matchRes =  HeadExtraxtRe.search(res1)

print(matchRes.group(0))
print(matchRes.group(1))
print(matchRes.group(2))
print(matchRes.group(3))
print(matchRes.group(4))
print(matchRes.group(5))



def ExtraxtParas(HeadExtraxtRe):
  HeadExtraxtRegStr = "(" + "|".join(HeadSet) +   ")" + "(.*?)()" + "(" + "|".join(HeadSet) +   ")"
  HeadExtraxtRe = re.compile(HeadExtraxtRegStr, flags= re.I | re.DOTALL )
  return HeadExtraxtRe


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

