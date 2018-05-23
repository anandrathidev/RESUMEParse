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

resumeJSONMapper = LoadResMapper(xpath)

def GetEmptyRes():
    resumeJSONMapper=None
    try:
        with open(xpath + "/RESUME_JSON_EMPTY.json") as RM:
            mapper = RM.read().lower()
            resumeJSONMapper =  json.loads( mapper )
    except Exception as e:        
        print("FillResume : {}".format(e))
    return resumeJSONMapper

ORes = GetEmptyRes() 

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
                yield (x,local_path)
                
        else:    
            yield (dic,path)

def ReverseMapRes(resumeJSONMapper, kpath=None):
    rev = {}
    if resumeJSONMapper==None:
        return rev 
    for k,v in resumeJSONMapper.items():
        kpath=[]
        #print("type({})=={}".format(v, type(v)))
        if isinstance(v, str):
            if not v=="":
                 rev[v] = kpath.append(k)
        if type(v)==type(1):
            rev[v] = kpath.append(k)
        if type(v)==type(1.1):
            rev[v] = kpath.append(k)
        if type(v)==type(["list"]):
            for i in v:
                if not i=="":
                    rev[i] = kpath.append(k)
        if type(v)==type({"dict":"dict"}):
            srev = ReverseMapRes(resumeJSONMapper=v,kpath=kpath)
            rev.update(srev)
        print("rev({})=={}".format(k, kpath ))
    return rev

import pandas as pd
rev = [ { "Key": k[0], "jpath":str(k[1])} for k in traverse(resumeJSONMapper, None)]
pd.DataFrame(rev).to_csv(xpath + "/RevrseMap.csv")


def getResumeMapper():
    ret = """
    {
    "basics": {
      "Personal":["Personal Glipse","Personal Details", "ADDITIONAL INFORMATION","About Me","SYNOPSIS","Personal Strength", "PERSONAL", "PERSONAL STRENGTH", "PERSONAL INFORMATION", "PERSONAL SUMMARY", "Personal Information","PERSONAL DOSSIER","PERSONNAL DETAILS","PERSONAL PROFILE","PERSONAL INFO", "PERSONAL TRAITS", "Personal Detail", "Personal information","Personal Interests","PERSONAL ATTRIBUTES","PERSONAL VITAE", "Personal Background", "PERSONAL STRENGTHS", "LinkedIn Profile", "PERSONAL SKILLS", "Personal Attributes","PASSPORT DETAILS","Profile","Academic Profile","PERSONEL INFORMATION", "Personal Info", "Personals Details", "PERSONAL INFORMATIONS", "Personal Profile", "Personal Dossier", "PERSONAL DETAILS", "Personal Details","PERSONAL QUALITIES", "Personality Traits", "Personal Skills", "Personal Traits", "PERSONAL DETAIL", "PERSONNAL DETAILS", "PERSONAL VITAE", "PERSONAL  QUALITIES"],
      "name": "",
      "label": "POSITION",
      "image": "",
      "email": ["email", "emails" ],
      "phone": ["phone", "contact details","contact"],
      "url": "",
      "summary": ["About Me","Summary","JOB OBJECTIVE","SUMMARY","[A] Summary","JOB OBJECTIVE","CO-CURRICULAR ACTIVITIES","EX-CURRICULAR ACTIVITIES","ABILITIES","Career Vision","vision","Objective","Brief Overview","PROFILE SUMMARY","CAREER CONTOUR","Job Objective","Career Vision","OBJECTIVE","OVERVIEW","Profile Summary","Synopsis","Profile summary","CAREER OBJECTIVE","CARRIER OBJECTIVES","Career objective", "CAREER OBJECTIVE & SUMMARY", "Career Objectives","Objectives","OBJECTIVES"],
      "location": {
        "address": "",
        "postalCode": "",
        "city": "",
        "countryCode": "",
        "region": ""
      },
      "profiles":  {  "network": "",  "username": "",  "url": ""  }
      
    },
    "work experience": 
      {
        "experience": ["EMPLOYMENT DETAILS","WORK & EXPERIANCE","ORGANISATIONAL EXPERIENCE","HARDWARE & NETWORKING EXPERIENCE","PROJECT RESPOSIBILITIES","Professional Qualification","Overall Experience","Total Professional Experience","Project and Work Responsibilities", "SOFTWARE PROJECTS", "Past Work History &  Experience", "KEY PROJECTS","PROFESSIONAL SYNOPSIS","Professional Attainments", "Organizational Experience", "ORGANIZATIONAL EXPERIENCE", "ORGANISATIONAL EXPERIENCE", "Organisational Experience", "Employment Chronicle", "KEY PROJECTS HANDLED", "Onsite Exposure", "TECHNICAL PROFILE", "Professional Experience & Details", "Areas of Expertise","PROJECT WORK","KEY PROJECTS UNDERTAKEN","ORGANISATIONAL SCAN","EMPLOYMENT HISTORY","ORGANIZATIONAL SCAN","Professional Digest","Employment History","PROFESSIONAL HISTORY","Project Experience","CAREER HISTORY","Last Experience","Profile & Experience Summary","HANDLED PROJECTS","PROJECT WORKED","Experience chronology","Current Projects","PROJECTS UNDERTAKEN","Executive Profile","Current Employer","Projects", "Projects Handled", "PROJECTS", "PROJECTS DETAILS","PROJECT DETAILS", "Projects Details", "Projects Worked On", "PROJECTS HANDLED", "Projects Undertaken","ONSITE EXPERIENCE","PROJECTS PROFILE","EXPERIENCE SUMMARY", "EXPERIENCE DETAILS", "EXPERIENCE", "Experience", "Experiences", "Experience Summary", "Experience SUMMARY", "Experience Snapshot","WORKING EXPERIENCE", "Working Experience","Job Experience","WORK EXPERINCE", "WORKING EXPERIENCE WITH",  "WORK AREAS", "WORK HISTORY", "WORK & EXPERIANCE", "WORK PROFILE","EMPLOYMENT EXPERIENCE", "Work Experience & Professional Experience","PROFESSIONAL EXPERIENCE", "Work history", "WORK EXPERIENCE", "Work History", "Work Experience", "Work Experience Details","Total Work Experience", "TOTAL WORK EXPERIENCE"],
        "name":"",
        "location": "",
        "description": "",
        "position": "",
        "url": "",
        "startDate": "",
        "endDate": "",
        "summary": ["SUMMARY OF EXPERIENCE","Executive Summary","Professional Summary","PROFESSIONAL SUMMARY","PROJECT SUMMARY","CAREER SUMMARY","PROJECT HIGHLIGHTS","Career Summary", "Career summary"],
        "highlights": ""
          
      },
    "volunteer": 
      {
        "organization": "",
        "position": "",
        "url": "",
        "startDate": "",
        "endDate": "",
        "summary": "",
        "highlights": ""
      },
    "education": 
      {
        "education":["Education / Professional Development","SUMMARY OF QUALIFICATION"],
        "institution": "",
        "area": "",
        "studyType": "",
        "startDate": "",
        "endDate": "",
        "gpa": "",
        "courses": []
      },
    "awards": 
      {
        "title": ["AWARD & ACHIEVEMENTS","Training& Certifications","ACHIEVEMENT HIGHLIGHTS","EXTRA-CURRICULAR ACTIVITIES","TRAINING EXPERIENCE"],
        "date": "",
        "awarder": "",
        "summary": ""
      } ,
    "publications": {
        "name": ["Research and Publications","Published Titles"],
        "publisher": "",
        "releaseDate": "",
        "url": "",
        "summary": ""
      } ,
    "skills": {
        "name": "",
        "level": "",
        "keywords": ["Technical skills","WORKING SKILL","BEHAVIOR SKILLS","SOFTWARE SKILLS",
		"Key Domain and Technical Knowledge","CO-CURRICULAR ACTIVITIES/ ACHIEVEMENTS","ACCOMPLISHMENTS","ACHIEVEMENT", 
		"Extra Curriculum", "EXTRA-CURRICULAR ACTIVITY", "ACHIVEMENTS & EXTRA CURRICULAR ACTIVITY", 
		"PROFESSIONAL TRAININGS","INDUSTRIAL TRAINING",  "Co-curricularactivities", "Career Interests", 
		"Other Notable Qualifications", "EXTRA  CURRICULLAR  ACTIVITIES", "HIGHLIGHTS", "Declarations",
		"SIGNIFICANT HIGHLIGHT","Training Programs", "AREAS OF INTEREST", "Declaration","Interest & Hobbies",  
		"Reward & Recognition", "REWARD & RECOGNITIONS","SummerTraining","Rewards&Achievements","Extra-CurricularActivities",
		"Characteristic Strengths","KNOWLEDGE BASE/TECHNICAL SKILLS","PROFICIENT IN",
		"SKILLS AND KNOWLEDGE ACQUIRED THROUGH EDUCATION AND EXPERIENCE",
		"FUNCTIONAL SKILLS","Technical Expertise", "COMPUTER SKILL SET", "Professional Strengths", 
		"Database Technologies & Skill Sets", "TECHNOLOGY TOOLSETS",
		"CORE COMPETENCY", "IT SKILLS", "IT Skills", "CORE COMPETENCIES", "Core Competencies", 
		"INTERPERSONAL SKILLS", "Computer Certification", "TECHNICAL PROFICIENCIES", "TECHNICAL EXPERTISE", 
		"TECHNICAL KNOWLEDGE","Technical Proficiency", "Technical Knowledge","Technical Skills","TECHNICAL SKILLS", 
		"KEY STRENGTHS","Key Strength","TECHNICAL SKILLS","OTHER SKILLS", "Other Skills","Technical Cognizance", 
		"Technical Skill Set","INFORMATION TECHNLOGY SKILLS","Technical Skills and knowledge","Key Skill Sets", 
		"CAREER SKILLS / KNOWLEDGE","EXCELLENCE SPHERE","EXCELLENCE","Technical skills","TECHNICAL QUALIFICATIONS", 
		"KEY SKILLS", "TECHNICAL QUALIFICATION","ADDITIONAL PROFESSIONAL SKILLS","COMPUTER KNOWLEDGE", "Personal Skills", 
		"STRENGTH", "STRENGTHS","Software Proficiency", "SOFTWARE PROFICIENCY", "EXCELLENCE", "LEADERSHIP SKILLS" , 
		"SKILL SETS", "Skills and Strengths", "Skill Summary", "Skill Sets", "Skills", "SKILLSET", "Skills Set", 
		"SKILLS AND KNOWLEDGE ACQUIRED THROUGH EDUCATION AND EXPERIENCE", "SKILLS", "Skills set", "SKILLS & PROFICIENCIES", 
		"SKILLS SUMMARY", "SKILLS AND KNOWLEDGE ACQUIRED THROUGH EXPERIENCE & TRAINING", "SKILLS & ABILITIES", "SKILL SET", 
		"Skills Profile", "SKILL/STRENTH", "Skills & Strenghts", "Skills Summary", "Skills SUMMARY", "Skill Set","Strength",
		"STRENGTH AND SKILLS", "Strengths & Weakness", "STRENGTH", "strengths"]
      },
    "languages":  {
        "language": "",
        "fluency": ""
      },
    "interests": 
      {
        "name": ["Participation and Achievements","Hobbies / Interests","TRAININGS","Other Certification","Training/Certification Details","Trainings & Achievements","Certifications","Award Details","TRAINING AND CERTIFICATION","EXTRACURRICULAR ACTIVITIES","Certified Courses","COURSE AND CERTIFICATION","ACHIEVEMENTS", "ACHIEVEMENTS/EXTRA-CURRICULAR", "Achievements","Technical Certification","INTERNSHIP EXPERIENCE", "Internship", "INTERNSHIP", "Internships", "INTERNSHIP/TRAINING","CERTIFICATION", "CERTIFICATIONS", "Certifications and Accomplishments", "Certification", "CERTIFICATIONS/LICENSES", "Certifications", "Certification & Education", "CERTIFICATION DETAILS", "Certification/s", "Certification/Professional Awards","Awards", "AWARDS", "Awards & Achievements", "Awards and Accomplishments", "Extra Curricular Activities","TECHNICAL FORTE","AWARDS AND RECOGNITIONS", "AWARDS & CERTIFICATE","AWARDS & EXTRA CURRICULAR ACTIVITIES", "AWARDS AND ACHIEVEMENTS", "AWARDS & RECOGNITIONS","EXTRA CURRICULAR ACTIVTIES","INTERESTS", "HOBBIES","INTERESTS AND HOBBIES", "Interests", "INTERESTS", "Interests and Hobbies", "Hobbies", "Hobbies&Interests", "HOBBIES", "HOBBIES AND INTEREST","CO-CURRICULAR ACTIVITIES", "Hobbies / Interests", "Hobbies and interest", "Achievements & Accomplishments", "ACHIEVEMENTS & EXTRA CURRICULAR ACTIVITIES", "Achievements & Awards"],
        "keywords": ""
      } ,
    "references": 
      {
        "name": "",
        "reference": ""
      } ,
    "projects": 
      {
        "name": ["Projects","PRECEEDING ASSIGNMENTS","Key Project Handled","PROJECT EXPERIENCE HIGHLIGHTS","PROJECT PROFILE", "Project Profile"],
        "description": "",
        "highlights": [ ],
        "keywords": [ "" ],
        "startDate": "",
        "endDate":["CURRENTLY WORKING","Currently Working"], 
        "url": "",
        "roles": [ "" ],
        "entity": "",
        "type": ""
      } ,
    "others":["DECLARATION","CAREER SNAPSHOT","Document Types and other Deliverables"]
  } """
    return ret    