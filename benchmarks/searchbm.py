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

from benchmark import simplereport, benchmark
from autocomplete import Corpus, nodify,wordcount,linecount,frequencies
import sys
import string

sys.path.insert(0,'/Users/margoK/Dropbox/autocomplete/')
sys.path.insert(1,'/Users/margoK/Dropbox/autocomplete/corpus/')

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

def report(log,inputs,trial=-1):#defaults to most recent trial
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

	print(report.substitute({'filename':file_name,
							'frequency': freq[search_term],
							'wordcount': wc,
							'linecount': lc,
							'unique': unique,
							'winner': testfns[t.index(winner)].__name__,
							'wintime': winner}))

	for i in xrange(len(testfns)):
		print("\t{fn_name}: {time}".format(fn_name = testfns[i].__name__,time=t[i]))



if __name__ == '__main__':
	f1 = '/Users/margoK/Dropbox/autocomplete/corpus/whitmanpoem.txt'
	f2 = '/Users/margoK/Dropbox/autocomplete/shakespeare.txt'

	corpus = []
	
	def trie_build_test(f, _):
		corpus.append(trie_build(f))

	benchmark((f2,'foo'), [trie_build_test],simplereport)
	corpus = corpus[0]

	def test_trie_search(_,word):
		trie_search(corpus,word)

	test_funcs = [linear_search, test_trie_search]#lambda _, word: trie_search(corpus, word)]
	benchmark((f2, 'dead'), test_funcs, report)


	 # test_funcs = (linear_search,try_trie)
	 # benchmark((f1,'dead'),test_funcs)
	# f2 = '/Users/margoK/Dropbox/autocomplete/shakespeare.txt'
	# benchmark((f2,'dream'),test_funcs)
