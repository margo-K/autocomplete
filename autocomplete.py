import pdb
from keypress import setup, use_letter,clean_up
import os
import sys
import time
import string
import unittest
from trie import Node
import pprint


CORPUS_DIRECTORY = {}

def get_files(directory='corpus/shakespeare/',subfolders=['comedies/','histories/','tragedies/','poetry/']):
	files = []
	for folder in subfolders:
			contents = [directory+folder+text for text in os.listdir(directory+folder)]
			files.extend(contents)
	name = directory[len('corpus/'):].strip('/')
	return name,files

def autocomplete(pre,corpus=None,pretty=True):
	node = corpus.find(nodify(pre))
	if node:
		found_words =  [str(leaf) for leaf in node.endnodes()]
		if pretty:
			for word in found_words:
				pretty_prefix = '\t\033[35m{}\033[0m'.format(pre)
				print word.replace(pre,pretty_prefix,1)
		return found_words
	else:
		return None

def tokenize(file_name):
	f = open(file_name)
	words = (word for line in f for word in line.split())
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

	tokens = tokenize(file_name)
	for token in tokens:
		root.insert(nodify(token))
	if name:
		print "Adding {} to the canon".format(name)
		CORPUS_DIRECTORY[name] = root
		print "You can now access the work by doing CORPUS_DIRECTORY[{}]".format(name)
	return root

class Corpus(Node):
	def __init__(self,source):
		self.value = None
		self.source = source
		# self.corpus = make_corpus(source) # not currently implemented

	@property
	def wordcount(self):
		"""Return wordcount and non-empty line-count of the file"""
		wc = 0
		for line in self.source:
			wc+=len(line.split())
		return wc

	@property
	def lines(self):
		lc = 0
		for line in self.source:
			lc+=1
		return lc

	@property
	def frequencies(self,tokenfn=lambda st: st.strip(string.punctuation).lower()):
		words = {}
		for line in self.source:
			for word in [tokenfn(st) for st in line.split()]:
				entry = words.setdefault(word,0)
				words[word]=entry+1 # increments the count for each word found
		return words

	@property
	def unique(self):
		return len(self.frequencies)

if __name__ == '__main__':

	fd, oldterm, oldflags = setup()
	try:
		name, files = get_files()
		corpus = make_corpus(files,name=name)
		print "Using Shakespeare corpus"
		use_letter(autocomplete,corpus=corpus)
	except KeyboardInterrupt:
		print "Unsetting autocomplete"
		time.sleep(1)
	finally:
		clean_up(fd,oldterm,oldflags)
		sys.exit()
		



