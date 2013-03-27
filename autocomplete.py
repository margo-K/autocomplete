import unittest
import string
import pdb

TEST_FILE = 'whitmanpoem.txt'

def triefy_file(file_name=TEST_FILE):
	with open(file_name,'r') as f:
		words = []
		for line in f:
			words.extend([word.strip(string.punctuation) for word in line.split()])
	return words

def prefix(li):
	return [li[:i] for i in range(1,len(li)+1)]


class Node(object):
	def __init__(self, value, children=None, isend=False):
		self.value = value
		self.children = children or []
		self.isEnd =isend

	def insert(self, nodes):
		if nodes == []:
			return self
		node,nodes = nodes[0],nodes[1:]
		child = self.get(node)
		if not child:
			self.children.append(node)
			child = node
		child.insert(nodes)
		return self

	def get(self,node):
		for child in self.children:
			if child == node:
				return child

		return None

	def __eq__(self,other_node):
		return self.value == other_node.value

	def __repr__(self):
		return "Node({})".format(self.value)

if __name__ == '__main__':
	root = Node(None)
	l1 = [Node('c'),Node('ca'),Node('cap')]
	l2 = [Node('c'),Node('ca'),Node('cat')]
	pdb.set_trace()

