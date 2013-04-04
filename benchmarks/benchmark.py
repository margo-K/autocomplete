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
from trie import Node


# CORPUS_DIRECTORY = "shakespeare/"
# SHAKESPEARE = []
# sub_folders = ['comedies/','histories/','tragedies/','poetry/']
# for folder in sub_folders:
# 	contents = [CORPUS_DIRECTORY+folder+work for work in os.listdir(CORPUS_DIRECTORY+folder)]
# 	SHAKESPEARE.extend(contents)

def make_file(file_names):
	with open('test_file.txt','a') as t:
		for fn in file_names:
			# pdb.set_trace()
			with open(fn) as f:
				# pdb.set_trace()
				lines = f.readlines()
				# pdb.set_trace()
				for line in lines:
					t.write(line)
	return t.name


def linear_search(file_name,word):
	"""Traverse a file, performing fn on each line"""
	start = time.time()
	with open(file_name,'r') as f:
		for line in f:
			if word in line:
				print "Found: {}".format(word)
				break
	end = time.time()
	totaltime = end-start
	print "\n{} took {} time to search".format('linear search',totaltime)
	return totaltime
			

def trie_search(file_name,word):
	start = time.time()
	corpus = make_corpus([file_name])
	post_build = time.time()
	build_time = post_build - start
	corpus.find(nodify(word))
	end = time.time()
	totaltime = end-start
	print "\n{} took {} time to build the tree".format('Prefix-tree', build_time)
	print "\n{} took {} time to search".format('Prefix tree',totaltime-build_time)
	print "\n{} took {} time total".format('Prefix tree',totaltime)


	return totaltime

def benchmark(file_name,word):
	lc, wc = wordcount(file_name)
	frequency,unique = word_frequency(file_name)

	print "\n----------Report----------\nFile Searched: {}\nFrequency of term searched: {} \nTotal words: {}\nTotal lines: {}\nUnique Words: {}\n".format(file_name,frequency[word],wc,lc,unique)

	lstime = linear_search(file_name,word)
	ttime = trie_search(file_name,word)

	winning_time = min(lstime,ttime)
	print "\nWinning Total Time: {}".format(winning_time)

if __name__ == '__main__':
	f1 = '/Users/margoK/Dropbox/autocomplete/corpus/whitmanpoem.txt'
	benchmark(f1,'dead')
	f2 = make_file(get_files(directory='/Users/margoK/Dropbox/autocomplete/corpus/shakespeare/'))
	benchmark(f2,'dream')

	# print "Linear results: {}".format(linear_search(f,"although"))
	# print "Trie results: {}".format(trie_search(f,"although"))




# class Benchmark:
# 	def __init__(file_name):
# 		self.file = file_name
# 		self.lc, self.wc = wordcount(file_name)
# 		self.frequency,self.unique = get_frequency(file_name)

# 	def 