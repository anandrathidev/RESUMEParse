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

HeadSet = GetHeadingsSets()
type(HeadSet)

"project" in HeadSet

avgHeaderLen = np.mean([ len(head) for  head in HeadSet if len(head.strip())>0 ])
avgHeaderWords = np.mean([ len(head.split()) for  head in HeadSet if len(head.strip())>0 ])
stdHeaderWords = np.std([ len(head.split()) for  head in HeadSet if len(head.strip())>0 ])

def CreateAllHeadRegExp(HeadSet):
  regList = []
  for h in HeadSet:
    HeadExtraxtRegStr = h
    HeadExtraxtRe = re.compile(h, flags= re.I)
    regList.append(HeadExtraxtRe)
  return regList

def MatchRegExp(text, cregs):
  matchcount = 0
  for hr in cregs:
    m = hr.match( text)
    if m:
      matchcount += 1
  return matchcount

def CreateHeadRegExp(HeadSet):
  HeadExtraxtRegStr = r"(" + r"|".join(HeadSet) +   r")[: ]*" + r"(.*?)" + r"(" + r"|".join(HeadSet) +   r")"
  HeadExtraxtRe = re.compile(HeadExtraxtRegStr, flags= re.I | re.DOTALL )
  return HeadExtraxtRe

hregall =  CreateAllHeadRegExp(HeadSet)

avgLen = np.mean([ len(rline) for  rline in rlines if len(rline.strip())>0 ])
avgWordCount = np.mean([ len(rline.split()) for  rline in rlines if len(rline.strip())>0 ])
stdWordCount = np.std([ len(rline.split()) for  rline in rlines if len(rline.strip())>0 ])

from scipy import stats
np.random.seed(7654567)

rvsWord = stats.norm.rvs(loc=avgWordCount, scale=stdWordCount, size=(50))
rvsHeader = stats.norm.rvs(loc=avgHeaderWords, scale=stdHeaderWords, size=(50))

HeaderStack=[]
Para=[]
ParaLines=[]
rlines = res1.splitlines()
lastHeader=""
for line in rlines:
   isHeader=0
   isMatch=0
   line=line.strip()
   words = line.split()
   wcnt = len(words)
   ##is this a heading ??
   if MatchRegExp(text=line, cregs=hregall)>0:
     #most probablity this is an header line
     isHeader+=1
     isMatch=1
     print("is in header list :{}".format(line))
   pval = stats.ttest_1samp(rvsWord, wcnt)
   if abs(pval.pvalue) < 0.05:
     isHeader+=1
   wpval = stats.ttest_1samp(rvsHeader, wcnt)
   if abs(wpval.pvalue) > 0.05:
     isHeader+=1
   if isHeader>2 and isMatch:
     if len(HeaderStack) >0:
       lastHeader=HeaderStack.pop()
     if len(ParaLines) >0:
       Para.append( { lastHeader: " ".join(ParaLines)} )
       lastHeader=""
       ParaLines=[]
     HeaderStack.append(line)
     print("")
     print("")
     print("==============isHeader={}".format(isHeader))
     print(line)
     print("============================")
   elif isHeader>2 :
     print("")
     print("")
     print("===== Sub Header==============isHeader={}".format(isHeader))
     print(line)
     print("============================")
     print("")
   else:
     if len(HeaderStack) >0:
       ParaLines.append(line)

if len(HeaderStack) >0:
  lastHeader=HeaderStack.pop()
if len(ParaLines) >0:
  Para.append( { lastHeader: " ".join(ParaLines)} )
  lastHeader=""
  ParaLines=[]

print(Para)

#ParaReg = re.compile(r"(\n|^)(.*?)(?=\n|$)")

ParaReg = re.compile(r"(\.\s)?(?[A-Z][^\.]+\.)")
i=0
for paras in re.finditer(ParaReg, res1):
  i=i+1
  print(i)
  if not paras is None:
    print("============== START")
    if not paras.group(0) == "":
      print("============== group 0")
      print( paras.group(0))
    if not paras.group(1) == "":
      print("============== group 1")
      print( paras.group(1))
    #if not paras.group(2) == "":
    #  print("============== group 2")
    #  print( paras.group(2))
    print("============== END")

print(matchRes.group(0))
print(matchRes.group(1))
print(matchRes.group(2))
print(matchRes.group(3))
print(matchRes.group(4))
print(matchRes.group(5))


HeadExtraxtRe = CreateHeadRegExp(list(HeadSet))
matchRes =  HeadExtraxtRe.search(res1)

for rline in res1.split("\n"):
  if

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

