import unittest
import string
import pdb
from keypress import use_letter,clean_up
import os
import sys
import time
from trie import Node


CORPUS_DIRECTORY = {}

def make_corpus(files,name=None,):
	root = Node(None)
	for fl in files:
		tokens = tokenize(fl)
		for token in tokens:
			root.insert(nodify(word))
	if name:
		print "Adding {} to the canon".format(name)
		CORPUS_DIRECTORY[name] = root
		print "You can now access the work by doing CORPUS_DIRECTORY[{}]".format(name)
		return name
	return root

def get_files(directory='./corpus/shakespeare/',subfolders=['comedies/','histories/','tragedies/','poetry/']):
	files = []
	for folder in subfolders:
			# pdb.set_trace()
			contents = [directory.lstrip(".")+folder+text for text in os.listdir(directory+folder)]
			# pdb.set_trace()
			files.extend(contents)
	return files

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

def tokenize(file_names):
	words = []
	for fn in file_names:
		# pdb.set_trace()
		with open(fn,'r') as f:
			for line in f:
				words.extend([word.strip(string.punctuation).lower() for word in line.split()])
		return words

def prefix(li):
	return [li[:i] for i in range(1,len(li)+1)]

def nodify(word):
	return map(Node,prefix(word))

	
class TrieTests(unittest.TestCase):
	pass

class IntegrationTests():
	def test_autocomplete(self):
		try:
			entry = make_corpus(get_files(),name='Shakespeare')
			print "Using corpus {}".format(entry)
			corpus = CORPUS_DIRECTORY[entry]
			print corpus.pprint()
			use_letter(autocomplete,corpus=corpus)
		except KeyboardInterrupt:
			print "Unsetting autocomplete"
			time.sleep(1)
			sys.exit()
		finally:
			clean_up()

if __name__ == '__main__':
		entry = make_corpus(get_files(),name='Shakespeare')
		print "Using corpus: {}".format(entry)
		corpus = CORPUS_DIRECTORY[entry]
		print corpus.pprint()




