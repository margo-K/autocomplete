import pdb
from keypress import use_letter,clean_up
import os
import sys
import time
import string
import unittest
from trie import Node
import pprint


CORPUS_DIRECTORY = {}

def make_corpus(files,name=None):
	root = Node(None)
	for fl in files:
		tokens = tokenize(fl)
		for token in tokens:
			root.insert(nodify(token))
	if name:
		print "Adding {} to the canon".format(name)
		CORPUS_DIRECTORY[name] = root
		print "You can now access the work by doing CORPUS_DIRECTORY[{}]".format(name)
	return root

def get_files(directory='corpus/shakespeare/',subfolders=['comedies/','histories/','tragedies/','poetry/']):
	files = []
	for folder in subfolders:
			contents = [directory+folder+text for text in os.listdir(directory+folder)]
			files.extend(contents)
	name = directory[len('corpus/'):]
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
	words = []
	# pdb.set_trace()
	with open(file_name,'r') as f:
		# pdb.set_trace()
		for line in f:
			if line:
				words.extend([token(st) for st in line.split()])
	return words

def token(st):
	"""Returns tokenized form of the input st"""
	return st.strip(string.punctuation).lower()

def prefix(li):
	return [li[:i] for i in range(1,len(li)+1)]

def nodify(word):
	return map(Node,prefix(word))

def wordcount(file_name):
	"""Return wordcount and non-empty line-count of the file

		*Words are any strings delimited by spaces"""
	wc = 0
	lc = 0
	with open(file_name,'r') as f:
		for line in f:
			if line:
				lc+=1
				wc+=len(line.split())
	return lc,wc

def word_frequency(file_name,tokenfn=token):
	words = {}
	with open(file_name,'r') as f:
		for line in f:
			if line:
				c_words = [tokenfn(st) for st in line.split()]
				for word in c_words:
					entry = words.setdefault(word,0)
					words[word]=entry+1 # increments the count for each word found

	uniquecount= len(words.keys())
	return words, uniquecount


def test_autocomplete():
		try:
			corpus = make_corpus(get_files(),name='Shakespeare')
			print "Using Shakespeare corpus"
			use_letter(autocomplete,corpus=corpus)
		except KeyboardInterrupt:
			print "Unsetting autocomplete"
			time.sleep(1)
			sys.exit()
		finally:
			clean_up()

def test_corpusconstruction():
	name, files = get_files()
	corpus = make_corpus(files,name=name)
	print corpus
	print "Using {} as corpus".format(name)
	print corpus.pprint()

def test_wordcount(f):
	print wordcount(f)


class Corpus(Node):
	pass

class CorpusTests(unittest.TestCase):

	def test_wordcount(self):
		"""Checks wordcount and linecount against bash versions"""
		file_name = 'corpus/whitmanpoem.txt'
		pass

	def test_word_frequency(self):
		"""Verifies that wordcount and wordfrequency are consistent"""
		file_name = 'corpus/whitmanpoem.txt'
		tokenfn = token

		lc, wc = wordcount(file_name)
		words, unique = word_frequency(file_name,tokenfn)

		self.assertEqual(wc, reduce(lambda x, y: x+y, words.itervalues()))

	def test_uniquevalues(self):
		"""Verify that the nodes in the corpus and unique words are the same"""
		file_name = 'corpus/whitmanpoem.txt'
		pass
		# make_corpus(file_name)






# class IntegrationTests():
# 	def __init__(self):
# 		test_corpusconstruction()
# 		test_autocomplete()



if __name__ == '__main__':
	unittest.main()

		



