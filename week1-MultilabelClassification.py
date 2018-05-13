# -*- coding: utf-8 -*-
"""
Created on Sat May 12 19:13:12 2018

@author: anandrathi
"""
import os
import inspect
from inspect import currentframe, getframeinfo

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno


path="C:/Users/anandrathi/Documents/DataScieince/Coursera/NLP/natural-language-processing-master/week1"
os.chdir(path)

import sys
sys.path.append("..")
from common.download_utils import download_week1_resources

download_week1_resources()


from grader import Grader
grader = Grader()

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from ast import literal_eval
import pandas as pd
import numpy as np

def read_data(filename):
    data = pd.read_csv(filename,  sep="\t")
    data['tags'] = data['tags'].apply(literal_eval)
    return data

train = read_data('data/train.tsv')
validation = read_data('data/validation.tsv')
test = pd.read_csv('data/test.tsv', sep='\t')

X_train, y_train = train['title'].values, train['tags'].values
X_val, y_val = validation['title'].values, validation['tags'].values
X_test = test['title'].values

print("X_train {}".format( len(X_train)))
print("y_train  {}".format( len(y_train )))

import re

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def text_prepare(text):
    """
        text: a string

        return: modified initial string
    """
    text = text.lower() # lowercase text
    #print("lowercase text {}".format(text) )
    text = REPLACE_BY_SPACE_RE.sub(" ", str(text)) # replace REPLACE_BY_SPACE_RE symbols by space in text
    #print("REPLACE_BY_SPACE_RE {}".format(text) )
    text = BAD_SYMBOLS_RE.sub("", text) # delete symbols which are in BAD_SYMBOLS_RE from text
    #print("BAD_SYMBOLS_RE {}".format(text) )
    text = text.strip()
    #print("strip {}".format(text) )
    text = " ".join( [ w for w in  text.split() if not w in STOPWORDS] )  # delete stopwords from text
    #print("STOPWORDS {}".format(text) )
    return text



def test_text_prepare():
    examples = ["SQL Server - any equivalent of Excel's CHOOSE function?",
                "How to free c++ memory vector<int> * arr?"]
    answers = ["sql server equivalent excels choose function",
               "free c++ memory vectorint arr"]
    for ex, ans in zip(examples, answers):
        if text_prepare(ex) != ans:
            return "Wrong answer for the case: '%s'" % ex
    return 'Basic tests are passed.'


print(test_text_prepare())


prepared_questions = []
for line in open('data/text_prepare_tests.tsv', encoding='utf-8'):
    line = text_prepare(line.strip())
    prepared_questions.append(line)
text_prepare_results = '\n'.join(prepared_questions)

grader.submit_tag('TextPrepare', text_prepare_results)

X_train = [text_prepare(x) for x in X_train]
X_val = [text_prepare(x) for x in X_val]
X_test = [text_prepare(x) for x in X_test]


message = 'Code location {0.filename}@{0.lineno}:'.format(inspect.getframeinfo(inspect.currentframe()))
print(" X_train {}".format( len(X_train) ))
print("y_train  {}".format( len(y_train )))


len(X_train)

X_train[:3]

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from ast import literal_eval
import pandas as pd
import numpy as np



# Dictionary of all tags from train corpus with their counts.
tags_counts = {}
# Dictionary of all words from train corpus with their counts.
words_counts = {}

######################################
######### YOUR CODE HERE #############
######################################

######################################
######### YOUR CODE HERE #############
######################################
from collections import Counter
text = " ".join(X_train)
words_counts = dict(Counter( text.split()))
text = " ".join([" ".join(tags) for tags in y_train][:])
tags_counts = dict(Counter( text.split()))


mctags = ",".join([ tag[0] for tag in list(Counter(words_counts).most_common(3)) ] )
mcwprds = ",".join([ word[0] for word in list(Counter(tags_counts).most_common(3)) ] )
print(mctags)
print(mcwprds)


most_common_tags = sorted(tags_counts.items(), key=lambda x: x[1], reverse=True)[:3]
most_common_words = sorted(words_counts.items(), key=lambda x: x[1], reverse=True)[:3]

grader.submit_tag('WordsTagsCount', '%s\n%s' % (','.join(tag for tag, _ in most_common_tags),
                                                ','.join(word for word, _ in most_common_words)))

DICT_SIZE = 50000
from sklearn.feature_extraction.text import CountVectorizer

WORDS_TO_INDEX = { word:index for index, word in enumerate( dict(Counter(words_counts).most_common(DICT_SIZE)).keys() ) }
INDEX_TO_WORDS = {v: k for k, v in WORDS_TO_INDEX.items()}

import numpy as np
result_vector = np.zeros(10)

def my_bag_of_words(text, words_to_index, dict_size):
    """
        text: a string
        dict_size: size of the dictionary

        return a vector which is a bag-of-words representation of 'text'
    """
    result_vector = np.zeros(dict_size)
    ######################################
    ######### YOUR CODE HERE #############
    ######################################
    index=0
    for word in text.split():
      if word in words_to_index:
        index=words_to_index[word]
        result_vector[index]+=1
    return result_vector

def test_my_bag_of_words():
    words_to_index = {'hi': 0, 'you': 1, 'me': 2, 'are': 3}
    examples = ['hi how are you']
    answers = [[1, 1, 0, 1]]
    for ex, ans in zip(examples, answers):
        if (my_bag_of_words(ex, words_to_index, 4) != ans).any():
            return "Wrong answer for the case: '%s'" % ex
    return 'Basic tests are passed.'

print(test_my_bag_of_words())

from scipy import sparse as sp_sparse

X_train_mybag = sp_sparse.vstack([sp_sparse.csr_matrix(my_bag_of_words(text, WORDS_TO_INDEX, DICT_SIZE)) for text in X_train])
X_val_mybag = sp_sparse.vstack([sp_sparse.csr_matrix(my_bag_of_words(text, WORDS_TO_INDEX, DICT_SIZE)) for text in X_val])
X_test_mybag = sp_sparse.vstack([sp_sparse.csr_matrix(my_bag_of_words(text, WORDS_TO_INDEX, DICT_SIZE)) for text in X_test])

print( "This is line {} ".format( get_linenumber()))
print('X_train shape ', X_train_mybag.shape)
print('X_val shape ', X_val_mybag.shape)
print('X_test shape ', X_test_mybag.shape)

#message = 'Code location {0.filename}@{0.lineno}:'.format(inspect.getframeinfo(inspect.currentframe()))
print( "This is line {} ".format( get_linenumber()))
print(" X_train {}".format( len(X_train)) )
print("y_train  {}".format( len(y_train )))


#Task 3 (BagOfWords)
row = X_train_mybag[10].toarray()[0]
non_zero_elements_count = np.count_nonzero(row ) ####### YOUR CODE HERE #######
grader.submit_tag('BagOfWords', str(non_zero_elements_count))


from sklearn.feature_extraction.text import TfidfVectorizer


print( "This is line {} ".format( get_linenumber()))
print(" X_train {}".format( len(X_train)))
print("y_train  {}".format( len(y_train )))
def tfidf_features(X_train, X_val, X_test):
    """
        X_train, X_val, X_test — samples
        return TF-IDF vectorized representation of each sample and vocabulary
    """
    # Create TF-IDF vectorizer with a proper parameters choice
    # Fit the vectorizer on the train set
    # Transform the train, test, and val sets and return the result


    ######################################
    ######### YOUR CODE HERE #############
    ######################################
    #tfidf_vectorizer = TfidfVectorizer()####### YOUR CODE HERE #######
    tfidf_vectorizer = TfidfVectorizer(token_pattern='(\S+)', analyzer='word')
    xall=X_train.copy()
    xall.extend(X_val)
    xall.extend(X_test)
    #xall.extend(X_val)
    #xall.extend(X_test)
    tfidf_vectorizer =  tfidf_vectorizer.fit(xall)
    return tfidf_vectorizer.transform(X_train), tfidf_vectorizer.transform(X_val), tfidf_vectorizer.transform(X_test), tfidf_vectorizer.vocabulary_

len(X_train)
len(train['tags'].values)

print( "This is line {} ".format( get_linenumber()))


X_train_tfidf, X_val_tfidf, X_test_tfidf, tfidf_vocab = tfidf_features(X_train, X_val, X_test)
tfidf_reversed_vocab = {i:word for word,i in tfidf_vocab.items()}
print( "This is line {} ".format( get_linenumber()))
print(" X_train {}".format( len(X_train)))
print("y_train  {}".format( len(y_train )))

tfidf_vocab["c++"]
tfidf_vocab["c#"]
tfidf_vocab["java"]

y_train = train['tags'].values
y_val = validation['tags'].values

from sklearn.preprocessing import MultiLabelBinarizer
mlb = MultiLabelBinarizer(classes=sorted(tags_counts.keys()))
y_train = mlb.fit_transform(y_train)
y_val = mlb.fit_transform(y_val)

from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier

def train_classifier(X_train, y_train):
    """
      X_train, y_train — training data

      return: trained classifier
    """

    # Create and fit LogisticRegression wraped into OneVsRestClassifier.
    ######################################
    ######### YOUR CODE HERE #############
    ######################################
    cls = OneVsRestClassifier(LogisticRegression())
    cls.fit(X_train, y_train)
    return cls

classifier_mybag = train_classifier(X_train_mybag, y_train)

classifier_tfidf = train_classifier(X_train_tfidf, y_train)

X_train_tfidf.shape
y_train.shape

print( "This is line {} ".format( get_linenumber()))
print(" X_train {}".format( len(X_train)))
print(" y_train  {}".format( len(y_train )))

print(" X_train_tfidf.shape {}".format( X_train_tfidf.shape ))
print("y_train  {}".format( y_train.shape))

y_val_predicted_labels_mybag = classifier_mybag.predict(X_val_mybag)
y_val_predicted_scores_mybag = classifier_mybag.decision_function(X_val_mybag)

y_val_predicted_labels_tfidf = classifier_tfidf.predict(X_val_tfidf)
y_val_predicted_scores_tfidf = classifier_tfidf.decision_function(X_val_tfidf)


y_val_pred_inversed = mlb.inverse_transform(y_val_predicted_labels_tfidf)
y_val_inversed = mlb.inverse_transform(y_val)

for i in range(3):
    print('Title:\t{}\nTrue labels:\t{}\nPredicted labels:\t{}\n\n'.format(
        X_val[i],
        ','.join(y_val_inversed[i]),
        ','.join(y_val_pred_inversed[i])
    ))

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import recall_score

#sklearn.metrics  MultiLabelBinarizer
def print_evaluation_scores(y_val, predicted):
    ######################################
    ######### YOUR CODE HERE #############
    ######################################
    print( "accuracy={}".format( accuracy_score(y_val, predicted)))
    print( "")
    print( "roc_auc_score={}".format( roc_auc_score(y_val, predicted)))
    print( "")
    print( "average_precision_score={}".format( average_precision_score(y_val, predicted)))
    print( "")

    print( "macro average_precision_score={}".format( average_precision_score(y_val, predicted, average = "macro")))
    print( "micro average_precision_score={}".format( average_precision_score(y_val, predicted, average = "micro")))
    print( "weighted average_precision_score={}".format( average_precision_score(y_val, predicted, average = "weighted")))

    print( "")

    print( "macro recall_score={}".format( recall_score(y_val, predicted, average = "macro")))
    print( "micro recall_score={}".format( recall_score(y_val, predicted, average = "micro")))
    print( "weighted recall_score={}".format( recall_score(y_val, predicted, average = "weighted")))
    print( "")

    print( "macro f1_score={}".format( f1_score(y_val, predicted, average = "macro")))
    print( "micro f1_score={}".format( f1_score(y_val, predicted, average = "micro")))
    print( "weighted f1_score={}".format( f1_score(y_val, predicted, average = "weighted")))


    #print( "f1_score={}".format( f1_score(y_val, predicted)))



print( "This is line {} ".format( get_linenumber()))
print(" X_train {}".format( len(X_train)))
print("y_train  {}".format( len(y_train )))

print('\nBag-of-words')
print_evaluation_scores(y_val, y_val_predicted_labels_mybag)
print('\nTfidf')
print_evaluation_scores(y_val, y_val_predicted_labels_tfidf)


from metrics import roc_auc
##matplotlib inline
n_classes = len(tags_counts)
roc_auc(y_val, y_val_predicted_scores_mybag, n_classes)


n_classes = len(tags_counts)
roc_auc(y_val, y_val_predicted_scores_tfidf, n_classes)



##**Task 4 (MultilabelClassification).** Once we have the evaluation set up,
## we suggest that you experiment a bit with training

def train_classifier(X_train, y_train, c):
    """
      X_train, y_train — training data

      return: trained classifier
    """

    # Create and fit LogisticRegression wraped into OneVsRestClassifier.
    ######################################
    ######### YOUR CODE HERE #############
    ######################################
    cls = OneVsRestClassifier(LogisticRegression(C=c))
    cls.fit(X_train, y_train)
    return cls


for c in [0.1, 1, 10, 100]:
  classifier_mybag = train_classifier(X_train_mybag, y_train, c=c)
  classifier_tfidf = train_classifier(X_train_tfidf, y_train, c=c)


y_test_predicted_labels_mybag = classifier_mybag.predict( X_test_mybag )
y_test_predicted_scores_mybag = classifier_mybag.decision_function( X_test_mybag )

y_test_predicted_labels_tfidf = classifier_tfidf.predict(X_test_tfidf)
y_test_predicted_scores_tfidf = classifier_tfidf.decision_function(X_test_tfidf)

y_test_pred_inversed = mlb.inverse_transform(y_test_predicted_labels_tfidf)
y_test_inversed = mlb.inverse_transform(y_test)

print('\nBag-of-words')
print_evaluation_scores(y_test, y_test_predicted_labels_mybag)
print('\nTfidf')
print_evaluation_scores(y_test, y_test_predicted_labels_tfidf)

test_predictions = ######### YOUR CODE HERE #############
test_pred_inversed = mlb.inverse_transform(test_predictions)

test_predictions_for_submission = '\n'.join('%i\t%s' % (i, ','.join(row)) for i, row in enumerate(test_pred_inversed))
grader.submit_tag('MultilabelClassification', test_predictions_for_submission)