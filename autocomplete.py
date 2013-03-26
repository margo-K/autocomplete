import unittest
import string

TEST_FILE = 'whitmanpoem.txt'

def triefy_file(file_name=TEST_FILE):
	with open(file_name,'r') as f:
		trial_trie = {}
		for line in f:
			words = line.split()
			for word in words:
				build_trie(word,trial_trie)
	return trial_trie

def dict_depth(dictionary, depth=0):
	"""Gotten from stackoverflow"""
	if not isinstance(dictionary,dict) or not dictionary:
		return depth
	return max(dict_depth(v,depth+1) for k,v in dictionary.iteritems())

def build_trie(word,trie):
	letters = [letter.lower() for letter in word if letter in string.letters]
	old_dict = trie
	while letters:
		current_letter, children = letters.pop(0),letters
		current_dict = old_dict.setdefault(current_letter,{})
		old_dict = current_dict

	current_dict['END'] = {}
	return trie
def pop_letter(word):
	return word[0], word[1:] # returns letter and the remainder of word

def in_trie(word,trie):
	built_word = ''
	pointer = 0
	start_trie = trie
	current_word = word
	while current_word:
		letter, rest_of_word = pop_letter(current_word)
		new_trie = start_trie.get(letter) # the dictionary in which we will in the next round (for the first letter in 'rest of word')
		if not new_trie:
			print "No entries for '{}'\n Only entries for: '{}' \n {}".format(word,built_word,start_trie)
			return False
		start_trie = new_trie
		current_word = rest_of_word
		built_word+=letter
		print "Current word portion found: {}".format(built_word)

	if 'END' in new_trie.keys():
		print "The word {} was found in the corpus".format(built_word)
		return True
	else:
		print "Only supersets of the word exist in the corpus: \n{}".format(new_trie)
		return False

class TrieTests(unittest.TestCase):

	def test_word_check(self):
		word = "hello"
		triefied_word = {'h':{'e':{'l':{'l':{'o':{'END':True}}}}}}

		self.assertEqual(build_trie(word,{}),triefied_word)

	def test_depth(self):
		word = 'oxford'
		trie = build_trie(word,{})

		self.assertEqual(dict_depth(trie),len(word)+1)

	def test_with_space(self):
		"""True if spaces are treated as characters"""
		words = 'hold up'
		trie = build_trie(words,{})
		triefied_words = {'h':{'o':{'l':{'d':{' ':{'u':{'p':{'END':True}}}}}}}}

		self.assertEqual(trie,triefied_words)

	def test_recover_words(self):
		pass

if __name__ == '__main__':
	trie = triefy_file()
	while True:
		term = raw_input("Please enter a search term: ")
		in_trie(term,trie)


