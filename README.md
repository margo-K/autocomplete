#Flexible Corpus Autocomplete

This project builds out autocomplete using a prefix-tree (trie) data structure that I also implemented. It allows you to autocomplete a string easily using different corpuses.
For example - included in the sampletexts are works by different authors. You could choose to autocomplete for the complete works of Shakespeare or autocomplete from Walt Whitman poems.

##Uses

I originally intended to the project as a UI feature for a search engine that relied on common search terms (similar to google's autocomplete). However, the trie-based data structure could also be used to store the entire search index itself. An expansion on this project would be to build a crawler using a prefix-tree as its index and analyze its space/time performance.

Though a user could simply use the autocomplete function, the package includes several other useful modules, which can be used independently (see 'Contents')

##Getting Started
####Requirements: None
####Open python REPL
```python
>>> from autocomplete import autocomplete
>>> from prefixcorpus import Corpus
>>> shakespeare = Corpus('sampletexts/allshakespeare.txt'
... )
>>> autocomplete(corpus=shakespeare,prefix='ham')
['hams', 'hames', 'hams', 'hamstring', 'hamper', 'hampton', 'hamlet', 'hamlets', 'hamlet', "hamlet's", 'hammer', 'hammers', 'hammer', "hammer'd", 'hammering']
```
Pretty-printing results (includes color highlighting of prefix in the terminal)
```python
>>> from autocomplete import autocomplete,autocompleteprint
>>> words = autocomplete(corpus=shakespeare,prefix='ham')
>>> autocompleteprint(prefix='ham',word_list=words)
	hams
	hames
	hams
	hamstring
	hamper
	hampton
	hamlet
	hamlets
	hamlet
	hamlet's
	hammer
	hammers
	hammer
	hammer'd
	hammering
```
####Run from Command line
```bash
$ python autocomplete.py
Setting autocomplete

Please enter some letters:

wint
	winter
	winters
	winter
	winter-time
	winter-cricket
	winter-ground
	winter's
	winterly

```
Note: corpus defaults to the Shakespeare corpus

####Exiting
Keyboard interrupt unsets autocomplete

##Contents
* __autocomplete.py__ : autocomplete function to complete from a prefix-tree corpus
* prefixcorpus.py : prefix-tree corpus class definition + helper functions; 
can be used to build a prefix tree from a file and easily access corpus attributes (wordcount, linecount, word frequencies, etc.)
* trie.py : base prefix-tree data structure
* keypress.py : terminal-altering for reading keypresses (temporarily disabled)
* sampletexts/: text files that can be used as a basis for corpus construction
* benchmarks/ : benchmarking module + sample benchmarks (see below)

##Benchmarks
benchmarks/
	- benchmark.py : generic module for time-benchmarking of functions 
	  & pprinting results of benchmark
	- searchbm.py : benchmarking of time for 
	  naive linear search vs. trie-based search on the Complete Works of Shakespeare
	- README.md : explanation of benchmark module, includes examples

##Status
###Features to Build
* tool which allows you to build a corpus from a book or collection of books on project gutenberg
	- instead of just checking the local cache for the work, it would look for a corresponding work on project gutenberg (and build a corpus from it, giving the user status-updates)
	- a chrome plugin that allows you to autocomplete from different corpuses

###To-Do
* tests! - include doctests for individual functions; also integration tests (esp. b/c of imports, etc.)
* change Node.insert & Node.find to accept a string or iterable (instead of nodes ); deprecate prefix_corpus.nodify
* rewrite corpus.pprint() that prints a series of strings instead of 
 one long string
* implement caching for corpuses from given files
* explore replacing make_file with a function that returns a generator (that can be written to a file, if desired)
* add support for different split parameters in Corpus construction (i.e. split on [' ', '--'], based on base text)
* refactor keypress.use_letter and turn non-echoing, individual keystroke feature back on
* have __main__ function take a parameter == the corpus


