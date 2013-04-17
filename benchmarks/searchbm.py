"""
Benchmarking suite

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
from __future__ import print_function
from benchmark import simplereport, benchmark
import sys
import string
import pdb

sys.path.insert(0,'/Users/margoK/Dropbox/autocomplete/')
sys.path.insert(1,'/Users/margoK/Dropbox/autocomplete/corpus/')

from autocomplete import Corpus, nodify,wordcount,linecount,frequencies

def linear_search(file_name,word):
	"""Traverse a file, performing fn on each line"""
	with open(file_name,'r') as f:
		for line in f:
			if word in line:
				print("Found: {}".format(word))
				break

def trie_build(file_name):
	return Corpus(file_name)
			
def trie_search(corpus,word):
	corpus.find(nodify(word))

def try_trie(file_name,word):
	corpus = trie_build(file_name)
	trie_search(corpus,word)

def corpusreport(log,inputs,corpus=None):#defaults to most recent trial

	file_name = inputs[0]
	search_term = inputs[1]

	corpus_info = string.Template("""\
	
	Corps Stats
	----------------------------------
	File Searched: $filename
	Frequency of term searched: $frequency
	Total words: $wordcount
	Total lines: $linecount
	Unique words: $unique
	""")

	print(corpus_info.substitute({'filename':file_name,
							'frequency': corpus.frequencies[search_term],
							'wordcount': corpus.source_wordcount,
							'linecount': corpus.lines,
							'unique': corpus.unique}))
	# pdb.set_trace()
	simplereport(log,inputs)

if __name__ == '__main__':
	f1 = '/Users/margoK/Dropbox/autocomplete/corpus/whitmanpoem.txt'
	f2 = '/Users/margoK/Dropbox/autocomplete/shakespeare.txt'

	corpus = []
	
	def trie_build_test(f, _):
		corpus.append(trie_build(f))

	benchmark((f2,'foo'),trie_build_test,simplereport)
	corpus = corpus[0]

	def test_trie_search(_,word):
		trie_search(corpus,word)

	test_funcs = [linear_search, test_trie_search]#lambda _, word: trie_search(corpus, word)]
	benchmark((f2, 'dead'),test_funcs,reportfn=corpusreport,trials=1,corpus=corpus)


	 # test_funcs = (linear_search,try_trie)
	 # benchmark((f1,'dead'),test_funcs)
	# f2 = '/Users/margoK/Dropbox/autocomplete/shakespeare.txt'
	# benchmark((f2,'dream'),test_funcs)
