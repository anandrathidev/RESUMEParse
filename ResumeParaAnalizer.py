# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:14:40 2018

@author: anandrathi
"""
import pandas as pd
import re
import numpy as np
import json

xpath = "C:/Users/anand.rathi/Documents/tmp/ALEEP/"
xpath = "D:/Users/anandrathi/Documents/personal/Bussiness/Aleep/"


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


list(HeadingDFJson)[1]

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

HeadSet

"project" in HeadSet

avgHeaderLen = np.mean([ len(head) for  head in HeadSet if len(head.strip())>0 ])
stdHeaderLen = np.std([ len(head) for  head in HeadSet if len(head.strip())>0 ])
avgHeaderWords = np.mean([ len(head.split()) for  head in HeadSet if len(head.strip())>0 ])
stdHeaderWords = np.std([ len(head.split()) for  head in HeadSet if len(head.strip())>0 ])

textSer = resdfInit['RESUME_TEXT']

def GetAvgLineDetails(textSer=textSer, avgHeaderWords=avgHeaderWords,  avgHeaderLen=stdHeaderLen):
  rlines=[]
  for item in textSer.iteritems():
    rlines.extend(item[1].splitlines() )

  avgWordLen = np.mean([ len(rline) for rline in rlines if len(rline.strip())>avgHeaderWords ])
  stdWordLen = np.std([ len(rline) for  rline in rlines if len(rline.strip())>avgHeaderWords ])
  avgWordCount = np.mean([ len(rline.split()) for  rline in rlines if len(rline.strip())>avgHeaderLen ])
  stdWordCount = np.std([ len(rline.split()) for  rline in rlines if len(rline.strip())>avgHeaderLen ])
  return avgWordLen,stdWordLen ,avgWordCount, stdWordCount

avgWordLen,stdWordLen ,avgWordCount, stdWordCount = GetAvgLineDetails(textSer=textSer, avgHeaderWords=avgHeaderWords, avgHeaderLen=stdHeaderLen)

def CreateAllHeadRegExp(HeadSet):
  regList = []
  for h in HeadSet:
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


from scipy import stats
np.random.seed(7654567)


HeaderStack=[]
Para=[]
ParaLines=[]
rlines = res1.splitlines()
lastHeader=""


rvsWord = stats.norm.rvs(loc=avgWordCount, scale=stdWordCount, size=(50))
rvsHeader = stats.norm.rvs(loc=avgHeaderWords, scale=stdHeaderWords, size=(50))
rvsWordLen = stats.norm.rvs(loc=avgWordLen, scale=stdWordLen, size=(50))
rvsHeaderLen = stats.norm.rvs(loc=avgHeaderLen, scale=stdHeaderLen, size=(50))

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
     print("is in header list :{}   {}".format(line, isHeader))
   pval = stats.ttest_1samp(rvsWord, wcnt)
   if abs(pval.pvalue) < 0.05:
     if wcnt< avgWordCount:
       isHeader+=1
       print("This is header rvsWord test :{} pval={} wcnt={}".format(isHeader,
             abs(pval.pvalue), wcnt))
   wpval = stats.ttest_1samp(rvsHeader, wcnt)
   if abs(wpval.pvalue) > 0.05:
     isHeader+=1
     print("This is header rvsHeader test :{} pval={} wcnt={}".format(isHeader,
           abs(wpval.pvalue), wcnt))

   pval = stats.ttest_1samp(rvsWordLen, len(line))
   if abs(pval.pvalue) < 0.05 :
     if(len(line)< avgWordLen):
       isHeader+=1
       print("This is header rvsWordLen test :{} pval={}  len(line)={}".format(isHeader,
           abs(pval.pvalue), len(line) ) )
   wpval = stats.ttest_1samp(rvsHeaderLen, len(line))
   if abs(wpval.pvalue) > 0.05:
     isHeader+=1
     print("This is header rvsHeaderLen test :{} pval={}  len(line)={}".format(isHeader, abs(wpval.pvalue), len(line) ) )

   if isHeader>=3 and isMatch:
     print("This is header :{}".format(line))
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
   elif isHeader>2:
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

#print(Para)

