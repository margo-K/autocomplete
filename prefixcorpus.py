from trie import Node
import os
import string

def get_files(directory='sampletexts/shakespeare/',subfolders=['comedies/','histories/','tragedies/','poetry/']):
	files = (directory+folder+text for folder in subfolders for text in os.listdir(directory+folder))
	return files

def make_file(file_names,newfile):
	with open(newfile,'a') as t:
		for fn in file_names:
			with open(fn) as f:
				lines = f.readlines()
				for line in lines:
					t.write(line)

def token(st):
	"""Returns tokenized form of the input st"""
	return st.strip(string.punctuation).lower()

def prefix(li):
	return [li[:i] for i in range(1,len(li)+1)]

def nodify(word):
	return map(Node,prefix(word))

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
	return words

def cachedproperty(fn):
	cache = []
	def cached(self):
		try:
			return cache[0]
		except IndexError:
			val = fn(self)
			cache.append(val)
			return val
	return cached

class Corpus(Node):	

	def __init__(self,source,tokenfn=token):
		self.value = None
		self.children = []
		self.isEnd = False
		self.source = source
		words = set(word for line in self.text for word in line.split())
		self.words = set(tokenfn(word) for word in words)
		if '' in self.words:
			self.words.remove('')
		for word in self.words:
			self.insert(nodify(word))

	@property
	def text(self):
		"""Return a generator that allows for 'for line in text'"""
		if os.path.exists(self.source): # checks if the file can be read as a file
			return open(self.source)
		return (line for line in self.source.splitlines())

	@property
	@cachedproperty
	def source_wordcount(self):
		"""Return wordcount of the file"""
		return wordcount(self.text)

	@property
	@cachedproperty
	def lines(self):
		return linecount(self.text)

	@property
	@cachedproperty
	def frequencies(self,tokenfn=lambda st: st.strip(string.punctuation).lower()):
		return frequencies(self.text, tokenfn)

	@property
	def unique(self):
		return len(self.frequencies)
