# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:09:16 2018

@author: he159490
"""

##################################################################
###################### Resume Mapper  ############################
##################################################################
import json

def LoadResMapper(xpath):
  resumeJSONMapper=None
  try:
    with open(xpath + "/ResumeMapper.json") as RM:
      mapper = RM.read().lower()
      resumeJSONMapper =  json.loads( mapper )
  except Exception as e:
    print("LoadResMapper : {}".format(e))
  return resumeJSONMapper


def GetEmptyRes():
  resumeJSONMapper=None
  try:
    with open(xpath + "/RESUME_JSON_EMPTY.json") as RM:
      mapper = RM.read().lower()
      resumeJSONMapper =  json.loads( mapper )
  except Exception as e:
      print("FillResume : {}".format(e))
  return resumeJSONMapper


import re
def replaceWithRegExp(s):
  s = s.strip()
  s = re.sub(r"(&|and)+", r"(&|and)", s)
  s = re.sub(r"[\s\t]+", r" ", s)
  #s = re.sub(r" ", r"[\s\t]*", s)
  s=s.replace(" ","[ \t]*")
  #s = re.sub("\\\\", r"\\", s)
  return s

s = replaceWithRegExp(" a quick & brown fox")
re.search(s," a quick & brown fox")

def traverse(dic, path=None):
  if not path:
    path=[]
  if isinstance(dic,dict):
    for x in dic.keys():
      local_path = path[:]
      local_path.append(x)
      for b in traverse(dic[x], local_path):
        yield b
  else:
    if isinstance(dic,list):
      local_path = path[:]
      #local_path.append(x)
      for x in dic:
        x = replaceWithRegExp(x)
        yield (x,local_path)
    else:
      dic = replaceWithRegExp(dic)
      yield (dic,path)


def getRevKeyHash(xpath):
  resumeJSONMapper = LoadResMapper(xpath)
  revHash = { k[0] : str(k[1])  for k in traverse(resumeJSONMapper, None) }
  return revHash




#import pandas as pd
#rev = [ { "Key": k[0], "jpath":str(k[1])} for k in traverse(resumeJSONMapper, None)]
#revHash = { k[0] : str(k[1])  for k in traverse(resumeJSONMapper, None) }

#pd.DataFrame(rev).to_csv(xpath + "/RevrseMap.csv")


