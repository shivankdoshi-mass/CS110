# Author: Shivank Doshi
# Email: sbdoshi@umass.edu
# Spire ID: 29860515
# Task 1

#import functions
import urllib.request
import re
import string 
import sys

url = 'https://bityl.co/Fm50'

# Task 2
def read_article_file(url):
  req = urllib.request.urlopen(url)
  text = req.read()
  text = text.decode('UTF-8')
  return text


# Task 3
def text_to_article_list(text):
  article = re.split('<NEW ARTICLE>', text)
  article.remove('')
  return article
  
# Task 4
# Function 1
def split_words(article):
  splitwords = article.split()
  return splitwords


# Function 2
def scrub_word(word):
  stripword = word.strip(string.punctuation)
  return stripword

# Function 3


def scrub_words(words):
    output = []
    for word in words:
        scrubword = scrub_word(word)
        if scrubword != '':
          output.append(scrubword)
    return output

articles = text_to_article_list(read_article_file(url))
print(scrub_words(split_words(articles[0])))

def build_article_index(articles):
  output = {}
  for index in range(len(articles)):
    articles[index] = scrub_words(split_words(articles[index]))
    for word in articles[index]:
      if word.lower() in output:
        output[word.lower()] = output[word.lower()].union({index})
      else:
        output[word.lower()] = {index}
  return output

print(build_article_index(articles))

def find_words(keywords, index):
  firstWord = True
  intersect_docs = set()
  for word in keywords:
    if word in index:
      if firstWord:
        firstWord = False
        intersect_docs = intersect_docs.union(index[word])
        continue
      intersect_docs = intersect_docs.intersection(index[word])
    else:
      return set()
  return intersect_docs

text = read_article_file('https://bityl.co/Fm50')
articles = text_to_article_list(text)
index = build_article_index(articles)
print(find_words(['life', 'moon'], index))