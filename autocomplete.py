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
	node = corpus.find(nodify(pre))
	if node:
		found_words =  [str(leaf) for leaf in node.endnodes()]
		if pretty:
			for word in found_words:
				print word.replace(prefix,color.prefix.format(prefix),1)
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

def make_corpus(file_name,name=None):
	if name in CORPUS_DIRECTORY:
		return CORPUS_DIRECTORY[name]
	root = Node(None)

	for token in tokenize(file_name): # this could be a generator
		root.insert(nodify(token))
	if name:
		print "Adding {} to the canon".format(name)
		CORPUS_DIRECTORY[name] = root
		print "You can now access the work by doing CORPUS_DIRECTORY[{}]".format(name)
	return root

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
			words[word]=entry+1 # increments the count for each word found
	return words



class Corpus(Node):	

	# directory = {}

	def __init__(self,source):
		self.value = None
		self.children = []
		self.source = source
		self.isEnd = False
		for token in tokenize(self.text):
			nodes = nodify(token)

			self.insert(nodes)
	@property
	def text(self):
		"""Return a generator that allows for 'for line in text'"""
		if os.path.exists(self.source): # checks if the file can be read as a file
			return open(self.source)
		return (line for line in self.source.splitlines())

	@property
	def wordcount(self):
		"""Return wordcount and non-empty line-count of the file"""
		wc = 0
		#pdb.set_trace()
		for line in self.text:
			#pdb.set_trace()
			wc+=len(line.split())
		return wc

	@property
	def lines(self):
		lc = 0
		for line in self.text:
			lc+=1
		return lc

	@property
	def frequencies(self,tokenfn=lambda st: st.strip(string.punctuation).lower()):
		words = {}
		for line in self.text:
			for word in [tokenfn(st) for st in line.split()]:
				entry = words.setdefault(word,0)
				words[word]=entry+1 # increments the count for each word found
		return words

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




