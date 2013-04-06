"""
Benchmarking to compare Trie-based search to linear search

INPUTS:
*text file (all one)

METRICS:
*time
*space

VARIABLES:
*WC = size of file (by word count)
*frequency of search term in corpus,
	i.e. how does it perform for a commonly searched word vs. for the least frequent word in the corpus
*number of unique words (measured by nodes in the prefix trie)

HYPOTHESIS:
*Linear search = BigO(1) (i.e. linear in word count)
*Trie search = 

"""
import os
import os.path
import sys
import pdb
import time

sys.path.insert(0,'/Users/margoK/Dropbox/autocomplete/')
sys.path.insert(1,'/Users/margoK/Dropbox/autocomplete/corpus/')
from autocomplete import wordcount, word_frequency, make_corpus,nodify,get_files

log = {}

def make_file(file_names,newfile):
	with open(newfile,'a') as t:
		for fn in file_names:
			with open(fn) as f:
				lines = f.readlines()
				for line in lines:
					t.write(line)

def logtime(fn):
	def wrapped(*args):
		start = time.time()
		output = fn(*args)
		end = time.time()
		total = end-start
		log[fn.__name__] = total
		print "{} has been logged".format(fn.__name__)
		return output
	return wrapped

	
def report(file_name,word,*args):
	for f in file_name:
		lc, wc = wordcount(f)
		frequency,unique = word_frequency(f)

		print "\n----------Report----------\nFile Searched: {}\nFrequency of term searched: {} \nTotal words: {}\nTotal lines: {}\nUnique Words: {}\n".format(file_name,frequency[word],wc,lc,unique)

	for arg in args:
		print "\n {}: {}".format(arg,log[arg])


@logtime
def linear_search(file_name,word):
	"""Traverse a file, performing fn on each line"""
	for fl in file_name:
		with open(fl,'r') as f:
			for line in f:
				if word in line:
					print "Found: {}".format(word)
					break

@logtime
def trie_build(file_names):
	return make_corpus(file_names)
			
@logtime
def trie_search(corpus,word):
	corpus.find(nodify(word))

def benchmark(file_name,word):
	corpus=trie_build(file_name)
	linear_search(file_name,word)
	trie_search(corpus,word)

	ttime = log['trie_build'] + log['trie_search']
	lstime = log['linear_search']

	report(file_name,word,'trie_build','trie_search','linear_search')
	winning_method, winning_time = min([('linear', lstime), ('trie', ttime)],key = lambda x: x[1])
	print "\nWinning Method: {}, Winning Time: {}".format(winning_method, winning_time)

if __name__ == '__main__':
	f1 = '/Users/margoK/Dropbox/autocomplete/corpus/whitmanpoem.txt'
	benchmark([f1],'dead')
	name, files = get_files(directory='/Users/margoK/Dropbox/autocomplete/corpus/shakespeare/')
	name, files = get_files(directory='corpus/shakespeare/')
	f2 = name+'.txt'
	make_file(files,f2)
	benchmark([f2],'dream')



