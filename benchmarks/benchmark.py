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
from __future__ import print_function
import os
import os.path
import sys
import pdb
import time
import string
import unittest

sys.path.insert(0,'/Users/margoK/Dropbox/autocomplete/')

from autocomplete import get_files

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


def simplereport(log,inputs):
	"""Report when only one function and one trial is in the log"""
	print("\n---REPORT---\nInput(s):{inputs}".format(inputs=inputs))
	report = "Function: {function}   Time:{time}"
	for fn in log.keys():
		print(report.format(function=fn.__name__,time=log[fn]))

def stats(log,trials=1):
	pass
	# return max_time,min_time,avg_time


def benchmark(inputs,fns,reportfn,*reportargs):
	if type(fns)!=list:
		fns = [fns]
	log = {fn:[] for fn in fns}
	
	for fn in fns:
		log[fn].append(timed(fn,*inputs))
	reportfn(log,inputs)

class BenchmarkTests(unittest.TestCase):

	def test_timed(self):
		t = 10
		fn = lambda _: time.sleep(t)
		arg = 'a'
		self.assertEqual(t,timed(fn,arg))

	def test_benchmarkfn(self):
		pass

if __name__ == '__main__':
	# unittest.main()
	def add(a,b):
		return a+b

	def mult(a,b):
		return a*b

	benchmark((1,2),[add,mult],simplereport)


