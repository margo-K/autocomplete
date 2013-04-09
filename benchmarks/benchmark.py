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
*Linear search = BigO(n) (i.e. linear in word count)
*Trie search = 

"""
import os
import os.path
import sys
import pdb
import time
import string

sys.path.insert(0,'/Users/margoK/Dropbox/autocomplete/')
sys.path.insert(1,'/Users/margoK/Dropbox/autocomplete/corpus/')
from autocomplete import Corpus,nodify,get_files,wordcount,linecount,frequencies

def make_file(file_names,newfile):
	with open(newfile,'a') as t:
		for fn in file_names:
			with open(fn) as f:
				lines = f.readlines()
				for line in lines:
					t.write(line)
def timed(fn,*args):
	start_real = time.time()
	fn(*args)
	end_real = time.time()
	return end_real - start_real

def report(testfns,log,trial=-1):#defaults to most recent trial
	inputs = log[trial][0]
	t =log[trial][1]
	winner = min(t)

	file_name = inputs[0]
	search_term = inputs[1]
	lc, wc = linecount(open(file_name)),wordcount(open(file_name))
	freq= frequencies(open(file_name))
	unique=len(freq)

	report = string.Template("""\
	
				Report
	----------------------------------
	File Searched: $filename
	Frequency of term searched: $frequency
	Total words: $wordcount
	Total lines: $linecount
	Unique words: $unique

	Winning method: $winner
	Winning time: $wintime


	""")

	print report.substitute({'filename':file_name,
							'frequency': freq[search_term],
							'wordcount': wc,
							'linecount': lc,
							'unique': unique,
							'winner': testfns[t.index(winner)].__name__,
							'wintime': winner})

	for i in xrange(len(testfns)):
		print "\t{fn_name}: {time}".format(fn_name = testfns[i].__name__,time=t[i])
	

def stats(log,trials=1):
	pass
	# return max_time,min_time,avg_time



def linear_search(file_name,word):
	"""Traverse a file, performing fn on each line"""
	with open(file_name,'r') as f:
		for line in f:
			if word in line:
				print "Found: {}".format(word)
				break

def trie_build(file_name):
	return Corpus(file_name)
			
def trie_search(corpus,word):
	corpus.find(nodify(word))

def try_trie(file_name,word):
	corpus = trie_build(file_name)
	trie_search(corpus,word)

def benchmark(inputs,fns):
	log = []
	t = [timed(fns[i],*inputs) for i in xrange(len(fns))]

	log.append([inputs,t])
	report(fns,log)

if __name__ == '__main__':
	f1 = '/Users/margoK/Dropbox/autocomplete/corpus/whitmanpoem.txt'
	test_funcs = (linear_search,try_trie)
	benchmark((f1,'dead'),test_funcs)
	f2 = '/Users/margoK/Dropbox/autocomplete/shakespeare.txt'
	benchmark((f2,'dream'),test_funcs)



