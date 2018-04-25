import os
import sys
from os import chdir, getcwd, listdir, path
from pathlib import Path
#Importing PYPDF2 for extracting Pdf text
import PyPDF2
#Importing docx for extracting text from word file
import docx
from docx import *
import string
from time import strftime
#Importing NLTK for stopword removal and tokenizing
import tokenize
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO
import nltk.data
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import subprocess
import string
import json
import re
import pickle
import os.path
#from _ _future_ _ import generators

#Extract text from DOCX
def getText(filename):
    print(filename)
    for filenames in files: 
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            re.split('\s{4,}',para.text)
        return '\n'.join(fullText)


def make_json(file):
    chapter = []
    out_path = 'C:/Users/Lenovo/Desktop/resumesParse/'

    op=''
    start=0
    cntr = 1
    filename='Ritu'
    
    for para in file.read().split('\n'):
       if(para==""):
            if(start==1): 
              with open(str(out_path)+str(filename) +'.json','a')as opf:
                     op= {"word": op}
                     print(json.dumps(op))
                     opf.write(str(json.dumps(op)) +"\n")
                     opf.close()
                     op=''
                     cntr+=1
                     
                     
                   
            else:
                start=1
       else:
             if(op==''):
                op = para
                
             else:
                 op= op +'\n' + para
                 #print(op)
   
    file.close()
    return op
with open("C:/Users/Lenovo/Desktop/resumesParse/Resume.txt") as file:
     make_json(file) 
   

def tokenFile(content):
    #Tokenizing/ Filtering the resume off stopwords and punctuations 
             print ("tokenizing the given file ......")
             tokens = word_tokenize(content)
             punctuations = ['(',')',';',':','[',']',',']

             stop_words = stopwords.words('english')
       
#clening the text
             filtered = [w for w in tokens if not w in stop_words and  not w in string.punctuation]

            
             print ("removing the stop words....\nCleaning the resumes....\nExtracting Text .......")
def file_exist(filename):
 list=[]

 for root,dirs,files in os.walk('C:/Users/Lenovo/Desktop/resumesParse/output/'):
  print(files)

  for filenames in files:
  #path='C:/Users/Lenovo/Desktop/resumesParse/output/'

         if os.path.exists(filename.endswith('.txt'))==False:
             print("end")
    
             print(filename)
             print("The File is already created :",filename)
         else :
             print ("file not created")
             #resume=getPdf(filename)

#extract text from pdf
def getPdf(filename):
 for file in list:
     filename=file
     #print(item)
     head,tail=os.path.split(filename)

     var="\\"

     tail=tail.replace(".pdf",".txt")

     name="C:/Users/Lenovo/Desktop/resumesParse/output/"+var+tail
     basename = '.'.join(os.path.basename(filename).split('.')[:1])


     content = ""

     pdf = PyPDF2.PdfFileReader(filename, "a+")

     for i in range(0, pdf.getNumPages()):
         for char in ',;-_+=#$^&!~()*':
            content=content.replace(char,'')
         content += pdf.getPage(i).extractText() + "\n"
         

     print (strftime("%H:%M:%S"), " pdf  -> txt ")
     
     with open(name,'w+') as out:
          out.write(content)

def check_path(prompt): 

    ''' (str) -> str

    Verifies if the provided absolute path does exist.

    '''

    abs_path = input(prompt)

    while path.exists(abs_path) != True:

        print ("\nThe specified path does not exist.\n")

        abs_path = input(prompt)

    return abs_path   

print ("\n")

folder = check_path("Provide absolute path for the folder: ")
#folder = 'C:/Users/Lenovo/Desktop/demo/resume/Java'

list=[]
out_path = 'C:/Users/Lenovo/Desktop/resumesParse/output/'
directory=folder
#check whether a file is pdf or doc
for root,dirs,files in os.walk(directory):

     for filename in files:

        if filename.endswith('.pdf'):
             print('works')
             print(filename)
             file_exist(filename)
             t=os.path.join(directory,filename)
             
             list.append(t)
             resume=getPdf(filename)
            # getParsedFiles(folder)
             print(folder)
             #file_exist(folder)
        elif filename.endswith('.docx'):
             print(filename)
             resume = getText(filename).encode("ascii", "ignore")
             str(resume, 'utf-8')
             basename = '.'.join(os.path.basename(filename).split('.')[:1])
             with open(str(out_path) + str(basename)+'.txt','wb') as out:
                  out.write(resume)
                  print("doc->txt")
    
        

                      
        else:
            print ("File format is currently not supported")
print ("processing..... \nplease wait....")




