import unittest


def dict_depth(dictionary, depth=0):
	"""Gotten from stackoverflow"""
	if not isinstance(dictionary,dict) or not dictionary:
		return depth
	return max(dict_depth(v,depth+1) for k,v in dictionary.iteritems())

def build_trie(word,trie):
	letters = [letter for letter in word]
	old_dict = trie
	while letters:
		current_letter, children = letters.pop(0),letters
		current_dict = old_dict.setdefault(current_letter,{})
		old_dict = current_dict

	current_dict['END'] = True
	return trie

def list_words(trie):
	pass

class TrieTests(unittest.TestCase):

	def test_word_check(self):
		word = "hello"
		triefied_word = {'h':{'e':{'l':{'l':{'o':{'END':True}}}}}}

		self.assertEqual(build_trie(word,{}),triefied_word)

	def test_depth(self):
		word = 'oxford'
		trie = build_trie(word,{})

		self.assertEqual(dict_depth(trie),len(word)+1)

	def test_recover_words(self):
		pass

if __name__ == '__main__':
	unittest.main()
	# while True:
	# 	word = raw_input('Please enter a word:')
	# 	trie = build_trie(word)



