# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:05:50 2018

@author: anandrathi
"""



def dictObjListChk(MT,ORes,wede):
  try:
    if not MT in ORes:
      ORes[MT]=[]
    if ORes[MT] is None:
      ORes[MT]=[]
    ORes[MT].append(wede)
    wed =  ORes[MT][-1]
  except Exception as e:
    print("{}".format(e))
    print("ORes = {}".format(ORes))
    print("wede = {}".format(wede))
  return wed


def dictObjChk(MT,ORes,wede):
  try:
    if not MT in ORes:
      ORes[MT]=wede
    if ORes[MT] is None:
      ORes[MT]=wede
    if not isinstance(ORes[MT],dict) :
      ORes[MT]=wede
  except Exception as e:
    print("{}".format(e))
    print("ORes = {}".format(ORes))
    print("wede = {}".format(wede))
  return ORes[MT]

def fillObjL1(v, wed , d):
  try:
    wed[v[1]] =  wed[v[1]] + " " + d
  except Exception as e:
    print("{}".format(e))
    print("wed = {}".format(wed))
    print("v[] = {}".format(v))
    print("v[1] = {}".format(v[1]))
    print("d = {}".format(d))


def fillObjL2(v, wed , d):
  try:
    wed[ v[1] ][ v[2] ] =   wed[ v[1] ][ v[2] ] + " "+ d
  except Exception as e:
    print("{}".format(e))
    print("wed = {}".format(wed))
    print("v[] = {}".format(v))
    print("v[1] = {}".format(v[1]))

def fillSkills(v, ORes, d):
  MT ="skills"
  wede = {
      "level": "",
      "keywords": ""
  }
  dictObjChk(MT=MT,ORes=ORes,wede=wede)
  wed =  ORes[MT]
  fillObjL1(v, wed , d)

def fillBasic(v, ORes, d):
  MT ="basics"
  wede = {
      "name": "",
      "personal":"",
      "other": "",
      "label": "",
      "dob": "",
      "email": "" ,
      "phone": "",
      "marital Status": "",
      "gender": "",
      "nationality": "",
      "summary": "",
      "location": {
        "address": "",
        "postalCode": "",
        "city": "",
        "countryCode": "",
        "region" : ""
        },
      "profiles" : ""
    }
  dictObjChk(MT=MT,ORes=ORes,wede=wede)
  wed =  ORes[MT]
  if v[1]=="location":
    fillObjL2(v, wed , d)
  else :
    fillObjL1(v, wed , d)

def fillEdu(v, ORes, d):
  MT ="education"
  wede = {
    "education":"",
    "institution": "",
    "area": "",
    "studyType": "",
    "startDate": "",
    "endDate": "",
    "gpa": "",
    "courses": ""
  }
  wed = dictObjListChk(MT=MT, ORes=ORes, wede=wede)
  fillObjL1(v, wed , d)


def fillWorkExp(v, ORes, d):
  MT ="work experience"
  wede = {
    "project":"",
    "experience":"",
    "organization":"",
    "location":"",
    "description":"",
    "roles":"",
    "highlights":"",
    "url":"",
    "duration":"",
    "startDate":"",
    "endDate":"",
    "teamsize":"",
    "summary":"",
    "roles":"",
    "highlights":""
  }

  wed =  dictObjListChk(MT=MT,ORes=ORes,wede=wede)
  fillObjL1(v, wed , d)
