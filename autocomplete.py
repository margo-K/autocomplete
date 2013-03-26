def build_trie(word,trie={}):
	letters = [letter for letter in word]
	old_dict = trie
	while letters:
		current_letter, children = letters.pop(0),letters
		"I'm now working on this:"
		print current_letter, children
		current_dict = old_dict.setdefault(current_letter,{})
		old_dict = current_dict

	current_dict['END'] = True
	print "This is the final product"
	print trie
	return trie

if __name__ == '__main__':
	while True:
		word = raw_input('Please enter a word:')
		trie = build_trie(word)


