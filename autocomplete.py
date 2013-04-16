import pdb
from keypress import setup, use_letter,clean_up
import os
import sys
import time
import string
import unittest
from trie import Node
import pprint

def get_files(directory='corpus/shakespeare/',subfolders=['comedies/','histories/','tragedies/','poetry/']):
	files = (directory+folder+text for folder in subfolders for text in os.listdir(directory+folder))
	return files

def autocomplete(prefix,corpus=None,pretty=True):
	colorprefix = '\t\033[35m{prefix}\033[0m'
	node = corpus.find(nodify(prefix))
	if node:
		found_words =  [str(leaf) for leaf in node.endnodes()]
		if pretty:
			for word in found_words:
				print word.replace(prefix, colorprefix.format(prefix=prefix),1)
		return found_words
	else:
		return None

def tokenize(open_file):
	words = (word for line in open_file for word in line.split())
	return (token(word) for word in words)

def token(st):
	"""Returns tokenized form of the input st"""
	return st.strip(string.punctuation).lower()

def prefix(li):
	return [li[:i] for i in range(1,len(li)+1)]

def nodify(word):
	return map(Node,prefix(word))

def make_corpus(files,name=None):
	corp = Node(None)
	for file_name in files:
		with open(file_name) as f:
			for token in tokenize(f):
				corp.insert(nodify(token))
	return corp

def wordcount(iterator):
	wc = 0
	for line in iterator:
		wc+=len(line.split())
	return wc

def linecount(iterator):
	lc = 0
	for line in iterator:
		lc+=1
	return lc

def frequencies(iterator,tokenfn=token):
	words = {}
	for line in iterator:
		for word in [tokenfn(st) for st in line.split()]:
			entry = words.setdefault(word,0)
	return words

def cachedproperty(fn):
	cache = []
	def cached(self):
		pdb.set_trace()
		try:
			return cache[0]
		except IndexError:
			val = fn(self)
			cache.append(val)
			return val
	return cached


class Corpus(Node):	

	def __init__(self,source):
		self.value = None
		self.children = []
		self.isEnd = False
		self.source = source
		words = set(word for line in self.text for word in line.split())
		self.words = set(token(word) for word in words)
		if '' in self.words:
			self.words.remove('')
		for word in self.words:
			self.insert(nodify(word))

	@property
	def text(self):
		"""Return a generator that allows for 'for line in text'"""
		if os.path.exists(self.source): # checks if the file can be read as a file
			return open(self.source)
		return (line for line in self.source.splitlines())

	@property
	@cachedproperty
	def source_wordcount(self):
		"""Return wordcount of the file"""
		return wordcount(self.text)

	@property
	@cachedproperty
	def lines(self):
		return linecount(self.text)

	@property
	@cachedproperty
	def frequencies(self,tokenfn=lambda st: st.strip(string.punctuation).lower()):
		return frequencies(self.text, tokenfn)

	@property
	def unique(self):
		return len(self.frequencies)

if __name__ == '__main__':
	f1 = '/Users/margoK/Dropbox/autocomplete/shakespeare.txt'
	f2 = '/Users/margoK/Dropbox/autocomplete/corpus/whitmanpoem.txt'
	corp1 = Corpus(f2)
	corp2 = Corpus(f1)
	print corp.pprint()
	print corp.wordcount,corp.lines,corp.frequencies




