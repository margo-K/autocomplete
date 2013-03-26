def build_trie(word):
	"""Return the list of nodes with their parent"""
	letters = [letter for letter in word]
	root = letters[0]
	trie = Graph(root)

	for i in range(1,len(letters)):
		letter = letters[i]
		parent = letters[i-1]

		vertex = Node(letter,parent)
		trie.add(vertex)
	return trie



class Graph(object):

	def __init__(self,root_node):
		self.root = root_node
		self.nodes = []

	def add(self,node):
		self.nodes.append(node)

	def __repr__(self):
		return "Graph:\n Root:%s \n Nodes: %s" %(self.root,self.nodes)
class Node(object):

	def __init__(self,letter,parent):
		self.letter = letter
		self.parent = parent # parent is another Node

	def add_child(self,child):
		self.children.append(child)

	def __repr__(self):
		return "Node: {} Parent: {}".format(self.letter,self.parent)

if __name__ == '__main__':
	word = raw_input('Please enter a word:')
	trie = build_trie(word)
	print trie


