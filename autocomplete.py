import unittest
import string
import pdb
from keypress import use_letter,clean_up
import os
import sys
import time

TEST_FILE = '/Users/margoK/Dropbox/autocomplete/whitmanpoem.txt'
SHAKESPEARE = []
base = '/Users/margoK/Dropbox/autocomplete/shakespeare'
sub_folders = ['/comedies/','/histories/','/tragedies/','/poetry/']
for folder in sub_folders:
	contents = [base+folder+work for work in os.listdir(base+folder)]
	SHAKESPEARE.extend(contents)

class Node(object):
	def __init__(self, value, children=None, isEnd=False):
		self.value = value
		self.children = children or []
		self.isEnd = isEnd

	def __eq__(self,other_node):
		return self.value == other_node.value

	def __repr__(self):
		return "Node({})".format(self.value)

	def __str__(self):
		if not self.value:
			return 'ROOT'
		return self.value 

	def insert(self, nodes):
		if nodes == []:
			return self
		node = nodes[0]
		child = self.get_child(node)
		if not child:
			self.children.append(node) # wouldn't be in find, replaced by return None
			child = node
		if not nodes[1:]:
			child.isEnd = True
		child.insert(nodes[1:])
		return self

	def find(self,prefix_nodes):
		node = prefix_nodes[0]
		child = self.get_child(node) ## return the node in tree
		
		if not child: # no matching child 
			return None
		if not prefix_nodes[1:]:
			return child
		else:
			return child.find(prefix_nodes[1:])

	def endnodes(self):
		cs_ends = []
		if self.isEnd:
			cs_ends.append(self)
		if self.children == []:
			return []
		end_children = [node for node in self.children if node.isEnd]
		for child in self.children:
			cs_ends.extend(child.endnodes())
		return end_children + cs_ends

	def contains(self,node):
		return node in root.endnodes()

	def get_child(self,node):
		"""Return the node in the tree that has the same value of the input node"""
		for child in self.children:
			if child == node:
				return child
		return None

	def pprint(self):
		printed = '\n|{}'.format(self)
		if self.isEnd:
			printed += '||'
		if self.children:
			for child in self.children:
				printed+=child.pprint().replace('\n','\n-')
		return printed

	def autocomplete(self,pre,pretty=True):
		node = self.find(nodify(pre))
		if node:
			found_words =  [str(leaf) for leaf in node.endnodes()]
			if pretty:
				for word in found_words:
					pretty_prefix = '\t\033[35m{}\033[0m'.format(pre)
					print word.replace(pre,pretty_prefix,1)
			return found_words
		return node


def split_file(file_names=SHAKESPEARE):
	words = []
	for fn in file_names:
		with open(fn,'r') as f:
			for line in f:
				words.extend([word.strip(string.punctuation).lower() for word in line.split()])
		return words

def prefix(li):
	return [li[:i] for i in range(1,len(li)+1)]

def nodify(word):
	return map(Node,prefix(word))


if __name__ == '__main__':
	try:
		root = Node(None)
		for word in split_file():
			root.insert(nodify(word))
		use_letter(root.autocomplete)
	except KeyboardInterrupt:
		print "Unsetting autocomplete"
		time.sleep(1)
		sys.exit()
	finally:
		clean_up()


class TrieTests(unittest.TestCase):
	pass

# class IntegrationTests():
# 	def basic_function(self):
# 		try:
# 			root = Node(None)
# 			for word in split_file():
# 				root.insert(nodify(word))
# 			root.autocomplete()
# 		except KeyboardInterrupt:
# 			print "Autocomplete exiting!"
# 			time.sleep(1)
# 			sys.exit(1)
# 		finally:
# 			clean_up()





