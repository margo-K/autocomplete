import sys
import time
from prefixcorpus import Corpus,nodify


def autocomplete(prefix,corpus=None,pretty=True):
	node = corpus.find(nodify(prefix))
	if node:
		found_words =  [str(end) for end in node.endnodes()]
		return found_words
	else:
		return []

def autocompleteprint(prefix,word_list):
	colorprefix = '\t\033[35m{prefix}\033[0m'
	for word in word_list:
		print word.replace(prefix, colorprefix.format(prefix=prefix),1)



if __name__ == '__main__':
	try:
		alt_corpus = Corpus('sampletexts/allshakespeare.txt')
		print "Setting autocomplete. \n Please enter some letters:"
		while True:
			letters = raw_input()
			words = autocomplete(prefix=letters,corpus=alt_corpus)
			autocompleteprint(prefix=letters,word_list=words)
			time.sleep(.5)
	except KeyboardInterrupt:
		print "\nUnsetting autocomplete"
		time.sleep(.1)
	sys.exit()





