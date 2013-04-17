import os
import sys
import time
from prefixcorpus import Corpus,nodify

def get_files(directory='corpus/shakespeare/',subfolders=['comedies/','histories/','tragedies/','poetry/']):
	files = (directory+folder+text for folder in subfolders for text in os.listdir(directory+folder))
	return files

def autocomplete(prefix,corpus=None,pretty=True):
	colorprefix = '\t\033[35m{prefix}\033[0m'
	node = corpus.find(nodify(prefix))
	if node:
		found_words =  [str(leaf) for leaf in node.endnodes()]
		if pretty:
			for word in found_words:
				print word.replace(prefix, colorprefix.format(prefix=prefix),1)
		return found_words
	else:
		return None


if __name__ == '__main__':
	try:
		alt_corpus = Corpus('shakespeare.txt')
		while True:
			letters = raw_input("Please enter some letters")
			autocomplete(prefix=letters,corpus=alt_corpus)
			time.sleep(.5)
	except KeyboardInterrupt:
		print "Unsetting autocomplete"
		time.sleep(.1)
	sys.exit()





