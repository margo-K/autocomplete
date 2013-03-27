import unittest
import string
import pdb

TEST_FILE = 'whitmanpoem.txt'

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
		if node.isEnd:
			child.isEnd = True
		child.insert(nodes)
		return self

	def get(self,node):
		for child in self.children:
			if child == node:
				return child

		return None

	def endnodes(self):
		if self.children == []:
			return []
		end_children = [node for node in self.children if node.isEnd]
		cs_ends = []
		for child in self.children:
			cs_ends.extend(child.endnodes())
		return end_children + cs_ends

	def __eq__(self,other_node):
		return self.value == other_node.value

	def __repr__(self):
		return "Node({})".format(self.value)


def triefy_file(file_name=TEST_FILE):
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


if __name__ == '__main__':
	root = Node(None)
	for word in triefy_file():
		root.insert(to_nodes(prefix(word)))
	pdb.set_trace()

