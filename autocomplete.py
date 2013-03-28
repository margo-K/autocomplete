import unittest
import string
import pdb
import curses

TEST_FILE = 'whitmanpoem.txt'

class Node(object):
	def __init__(self, value, children=None, isend=False):
		self.value = value
		self.children = children or []
		self.isEnd = isend

	def insert(self, nodes):
		if nodes == []:
			return self
		node,nodes = nodes[0],nodes[1:]
		child = self.get(node)
		if not child:
			self.children.append(node) # wouldn't be in find, replaced by return None
			child = node
		if node.isEnd:
			child.isEnd = True # wouldn't be in find
		child.insert(nodes)
		return self

	def get(self,node):
		"""Return the node in the tree that has the same value of the input node"""
		for child in self.children:
			if child == node:
				return child
		return None

	def contains(self,node):
		return node in root.endnodes()

	def endnodes(self):
		if self.children == []:
			return []
		end_children = [node for node in self.children if node.isEnd]
		cs_ends = []
		for child in self.children:
			cs_ends.extend(child.endnodes())
		return end_children + cs_ends

	def find(self,prefix_nodes):
		node,nodes = prefix_nodes[0],prefix_nodes[1:]
		child = self.get(node)
		if node.isEnd or (child is None):
			return child
		return child.find(nodes)

	def __eq__(self,other_node):
		return self.value == other_node.value

	def __repr__(self):
		return "Node({})".format(self.value)
	def __str__(self):
		if not self.value:
			return 'ROOT'
		return self.value 

	def pprint(self):
		printed = '\n|{}'.format(self)
		if self.isEnd:
			printed += '||'
		if self.children:
			for child in self.children:
				printed+=child.pprint().replace('\n','\n-')
		return printed

def split_file(file_name=TEST_FILE):
	with open(file_name,'r') as f:
		words = []
		for line in f:
			words.extend([word.strip(string.punctuation).lower() for word in line.split()])
	return words

def prefix(li):
	return [li[:i] for i in range(1,len(li)+1)]

def to_nodes(prefix_list):
	nodes = map(Node,prefix_list)
	nodes[-1].isEnd = True
	return nodes

def autocomplete(corpus_node,pre):
	node_from_corp = corpus_node.find(to_nodes(prefix(pre)))
	if node_from_corp:
		return [str(node) for node in node_from_corp.endnodes()]
	return node_from_corp

if __name__ == '__main__':
	root = Node(None)
	for word in split_file():
		root.insert(to_nodes(prefix(word)))
	print root.pprint()


