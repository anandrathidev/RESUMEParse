# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 18:54:01 2018

@author: anandrathi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:31:29 2018
@author: Anand.RATHI
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
#import enchant
from nltk.corpus import stopwords
STOP_WORDS=set(stopwords.words('english'))

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
NO_NAME.update(set( """
                   skype
tech communication
downloaded
analysis implementation net platform asp net mvc related
objective leader strong client relationship
male dd mm yyyy
dedicated working
enclave lane word
working tech
linkedin https ae linkedin ajirin
tech info edge limited noida months
objective seeking leverage hone skills working across various tech stacks

phone  phone  no  name   bachelor
                    no    block  jaitpur extension  badarpur
                   curriculam
                   curriculum
                   resume
village tobra office ateli mandi
extension
 network ccna ccnp
mba nmims e nit jamshedpur
 planning
 big
 practical
 informatica
 carriculum
 think
 due restriction
 enclosing
 citrix administrator source solutions
 sap basis  consultant
 performance banking insurance health domain
 competent communicator
 sap abap consultant
 results customer focused articulate analytical
                   room svr executive men hostel patrika nagar st madhapur hyderabad
                   first floor sector rohini delhi th june usa b visa
                   snapshot cid total years cid conceptualized designed
                   developed deployed optimized scaled web applications
                   cid provided oversight mentorship team developers cid
                   wrote technical specification streamlined development
                   process reduce time market multiple projects cid microsoft
                   coding contest rank india selected internship live project
                   professional sde tolexo india pvt ltd july present tolexo high
                   availability golang redis vagrant git mysql rest api gorm
                   cid planned designed implemented backend following scratch
                   order management system shipping provider management system
                   serviceability management access control list returns
                   refunds cid implemented message queues using redis
                   list cid lead team create scalable optimized microservices
                   cid caching api level well db level cid solution design
                   db design review new development optimizing existing backend
                   apis cid taking care scalability micro services architecture
                   cid troubleshooting live issues cid drive code hygiene ensure
                   industry best standard followed cid mentored new joiners took
                   care scrum project lead computer scientist belzabar software
                   design delhi jan july infor backend mongo db mongoose node js
                   git rest api cid conceptualized designed developed deployed web
                   app cid created apis asset management tool manage different
                   types asset different types collections cid implemented version
                   control status transformation content management tool along
                   respective apis cid designed mongoose schema implement inheritance
                   integrated cmt amt cid redesigned workflow storing images
                   different presets physical location expertly java spring
                   postgre mybatis cid architecture design review cid implemented
                   guideless activities cid developed functionality yet created
                   guide nyc comptroller backend php wordpress ajax jquery json
                   svn mysql cid created multiple plugins filling post meta data
                   plugins converting data mysql db excel sheets vice versa cid
                   wrote scripts google analytics filling form addresses using
                   google map apis ajax calls cid handled team create theme url
                   post based architecture request manager java servlets jsp mysql
                   ajax xslt svn cid implemented request hierarchy model fetches
                   data dynamically create represents tree format cid implemented
                   work order management inside request manager cid developed rich
                   text notes creation multiple request creation performed bug fixes
                   ixquick search engine c perl json regex cid implemented pdf ppt
                   docx search support proxy hide tracking details ua ip
                   previous searches user
                   objectives mind synergistic excellence
                   senior associate infrastructure
                    senior scm build release change
                     accomplished integrity driven
                     pmp csm safe agilist icp acc itil
                      master agile coach   mobile
                      license current employer tata consultancy
                       house gardens  street road
                       android rit indore batch  business
                       technologies
                        address block near motor garadge
                        tal dist thane
                        enthusiastic realistic year real
                        add megapolis splendour hinzewadi phase pune maharastra
                        personal highly efficient enthusiastic comprehensive
                        understanding processes driven sr year r led lighting integration
                        embedded programming testing verification led drivers topology
                        special application products keento find engineering good
                        organization bring expertise also solve difficult task
                        areas power electronics led lighting integration embedded
                        testing production sr r august solving service
                        quantum dots technology chennai embedded programming adc
                        timing voltage sensing dimming pwm tools comfort switch solar
                        combo pir sensor solar home light lantern switch hydrophonis electric
                        detector etc ccs led driver mikroc dc dc led drivers w boost buck buck boost
                        flyback sepic circuit maker ac dc led drivers buck flyback
                        isolated non isolated led lighting integration higher end
                        technology autocad led light integration w w bay led light
                        sketchup special application comfort switch electric detector
                        solar hybrid led lights dual light calling bell porch light
                        dc dc mobile charger etc duties personal embedded programming
                        bit microcontroller responsible concept circuit senbagavalli g
                        product codification test procedure bom preparation parasuram
                        product validation product layout maintain products karungalpalayam
                        delivering products budgets getting erode charge lab instruments
                        inventory tamil  communicating customers suppliers resolve
                        dob component sourcing pcb layout verification academic
                        qualifications married female ece university kcet
                        nationality indian
                       id contact number current preferred gender current annual
                       salary current job title current functional current current
                       company current job notice period education education stream education
                       institute year passing education course type
                       last modified date last active date note
                         national institute technology
                   rational clearcase certifieddevops certified financial markets foundation
                   telecommunication
implementing lan wan connections switches routers
around installation configuration migration
websphere
machine learning turning
box problem expert html html css css bootstrap
cann take call hours please drop immediately reply
hi step exploring possibilities employment
ui applicaton
http www
cross north city  bangalore
pagenote iamlookingonlyforpermanentandoncompanypayrolljobs
iamnotinterestedinc handthirdpartypayroll
goodunderstandingofoperatingsysteminfrastructure
yearsofexperienceinmicrosoftexchange activedirectory backupsolutionsandmicrosofttechnologies
provenknowledgeofmicrosoftexchange dagadministration workingknowledgeofcitrixxenapp
xendeskop knowledgeofbackupproductsveritasnetbackup backupexec
dlo commvaultbackup workingknowledgeofxenapp xendesktop
workingknowledgeofcitrixprovisioningserver abilitytoworkunderpressureandremaindecisive
professionalexperiencepresentemployer continuummanagedsolutionsprivateltd nocsupportengineer
l techproducts activedirectory microsoftactivedirectory microsoftexchange windowsservers dhcp
rmmportal responsibilities windowsservers exchange backupsolution
widowsserverbackup handlingticketsrelatedwindowsbackup activedirectory
dhcp dns emails
teams currently playing role
cell
 sas programmer parexel international
 candidate
 oracle dba
 aspects administering
 cypress semiconductor  wireless
 warehousing  comfortable warehousing
 hospitality sales degree international
 possess jobs ibm infosphere datastage
 equipped result oriented seeks ambitious
  soft azure cloud
   correspondence petroleum
    oracle dba
	 sql server dba
	 comforts gents pg main mob
     possessing erp full ites corporation use
     efficiently effectively global competitive environment
 cobol jcl
 indeed
                   """.split()))
len(NO_NAME)

NO_NAME.update(STOP_WORDS)
len(NO_NAME)
"telecommunication" in NO_NAME
"luke" in NO_NAME
"richmnan"  in NO_NAME
"resume"  in NO_NAME
"phone"  in NO_NAME

PAT = re.compile(EMAIL_PATTERN)

xpath = "C:/Users/anand.rathi/Documents/tmp/ALEEP/"
xpath = "D:/Users/anandrathi/Documents/personal/Bussiness/Aleep/"
resdfInit = pd.read_json(xpath + "ALLRES.json", orient='records')


list(resdfInit.columns)

resdfInit.head(1).index

res1 = resdfInit['RESUME_TEXT'].head(1)[0]


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

def ReplaceEmail(emails, x):
  if len(emails)>0:
    for email in emails:
      x.replace(email,'')
  return pd.Series( {"TEXT":x})

def ExtractEmail(x):
  emails = PAT.findall(x)
  return  { "emailsCount": len(emails) , "emails":emails}

def removeStopWords(x):
  word_list=x.split()
  filtered_words = " ".join([word.strip() for word in word_list if word.strip() not in  NO_NAME])
  #for xw in x.split():
  #  if wordnet.synsets(xw):
       #English Word
  #    x=x.strip().replace(xw," ")
  return filtered_words

def ExtractFirstLine(x):
  newx=""
  for line in x.lstrip().splitlines()[0:4]:
    newx1=line.lower()
    #log.write("bef StopWords  {}\n".format(newx1).encode('ascii', errors='ignore').decode('ascii', errors='ignore') )
    newx1=removeStopWords(newx1).strip()
    if len(newx1.split()) >10:
      newx1= " ".join(newx1.split()[0:4])
      #log.write("10 {} \n".format(newx1).encode('ascii', errors='ignore').decode('ascii', errors='ignore') )
    emails = ExtractEmail(newx1)["emails"]
    for email in emails:
      newx1=newx1.replace(email,' ')
    newx1 = re.sub(r'[0-9]+', ' ', newx1)
    newx1 = re.sub(r'_+', ' ', newx1)
    newx1 = newx1.strip().lower()
    newx1=re.sub(r'[^\s\w_]+',' ',newx1).strip()
    newx1=removeStopWords(newx1).strip()
    #log.write("after removeStopWords  {}\n".format(newx1).encode('ascii', errors='ignore').decode('ascii', errors='ignore') )
    #newx1=removeStopWords(newx1).strip()
    newx = str(newx + " " + newx1).strip()
    if len(newx.split())>1:
      break
  return pd.Series( { "Firstline": newx } )


def ExtractParas(x):
  paraList =[]
  #Parainfo={}
  for para in x.lstrip().split("\n\n") :
    paraList.append(para)
    summ = re.search('summary', para.lower())
    if(summ is not None):
      summ=para
    exp = re.search('exp', para.lower())
    if(exp is not None):
      exp=para
    skill = re.search('skill', para.lower())
    if(skill is not None):
      skill=para
    edu = re.search('edu', para.lower())
    if(edu is not None):
      edu=para
  return pd.Series( { "paraList ": paraList ,
                     "paraCount": len(paraList),
    "summ" :summ  ,
    "exp" : exp,
    "skill" : skill,
    "edu" : edu

                     } )


## Extract Email
emailsDF = pd.DataFrame(resdfInit.apply(lambda x: pd.Series(ExtractEmail(x['RESUME_TEXT'])) , axis=1))

resdf = pd.merge(resdfInit, emailsDF, left_index=True, right_index=True)

log = open(xpath+ "/clog.log", "w")
firstLineDF = pd.DataFrame(resdf.apply(lambda x: ExtractFirstLine(x['RESUME_TEXT']) , axis=1))
namesDF = pd.DataFrame(firstLineDF.apply(lambda x: extract_entities(x['Firstline']) , axis=1))
ParasDF = pd.DataFrame(resdf.apply(lambda x: ExtractParas(x['RESUME_TEXT']) , axis=1))

ParasDF100 = ParasDF.head(100)

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


name = get_human_names(res1.splitlines()[0])
extract_entities(res1.splitlines()[0])
