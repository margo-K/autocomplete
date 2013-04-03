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
		"""Insert item into a tree

		*nodes = return value from nodify(word),
		i.e. an increasing series of prefix nodes

		EX: root = Node(None)
			To insert "hi":

				root.insert([Node('h'),Node('hi')])
				=> root.children = [Node('h')]
				=> Node('h').children = [Node('hi')]
			"""
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
		"""Return node in self with the value equal to that in the prefix_nodes

		prefix_nodes = list of prefix nodes for a given term

		EX: To find 'hel' in a corpus
			corpus.find([Node('h'),Node('he'),Node('hel')])
			=> node = Node('hel'), 
				where node is in the corpus
		"""
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
		"""Returns a child of self, if a child exists 
			with node.value == child.value"""
		for child in self.children:
			if child == node:
				return child
		return None

	def pprint(self):
		"""Returns a string representation of a current graph"""
		printed = '\n|{}'.format(self)
		if self.isEnd:
			printed += '||'
		if self.children:
			for child in self.children:
				printed+=child.pprint().replace('\n','\n-')
		return printed