#Bug 5: When autocompleting a full word, the word doesn't appear as a solution
###Status: Unsolved
###Understood: Maybe

##Commit being Referenced
[And beyond until this is fixed]

```
[real_trie *%]\ $ git log
commit a5de0a84d4dc2d1635cdfa5519520d5d26abc1a4
Author: Margo Kulkarni <margo.r.kulkarni@gmail.com>
Date:   Mon Apr 1 15:33:43 2013 -0400
```


##Code Snippet (if different from commit): Believed
```
  def autocomplete(self,pre,pretty=True):
		node = self.find(nodify(pre))
		if node:
			found_words =  [str(leaf) for leaf in node.endnodes()]
			if pretty:
				for word in found_words:
					print '\t'+word
			return found_words
		return node
```

```
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
```

##Run Context
```
	if __name__ == '__main__':
	try:
		root = Node(None)
		for word in split_file():
			root.insert(nodify(word))
		use_letter(root.autocomplete)
	except KeyboardInterrupt:
		print "Thanks for playing!"
		sys.exit(1)
	finally:
		clean_up()
```

##Desired Output
```
----alon----
	alone
	along
----alone----
  **alone**
```
##Returns
Note: code with ---''--- is input
```
----alo---- 
	alone
	along
----alon----
	alone
	along
----alone----
```
##Error Message
None

##Hypothes(is/es)
1. autocomplete() : find is not finding a node, so autocomplete is returning none
2. the word is not getting returned as one of its own endnodes
3. ~~the word is actually not a word in the corpus~~ [not true because it returns as a node in shorter versions]

##Fix

##Alterations

##Conclusions

##Diagrams & References
###Diagram [#]
###Code Run