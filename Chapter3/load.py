from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
print(type(raw))
print(len(raw))
print(raw[:75])

tokens = nltk.word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])