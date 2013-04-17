#Autocomplete

###Contents
* __autocomplete.py__ : autocompleting from a prefix-tree corpus

* prefixcorpus.py: prefix-tree corpus class definition + helper functions
* trie.py : Base prefix-tree data structure
* keypress.py : terminal-altering for reading keypresses (temporarily disabled)

* sampletexts/: text files that can be used as a basis for corpus construction
* benchmarks/ : benchmarking module + sample benchmarks (see below)


###Getting Started
####Requirements: None (outside of Standard Library)
####Open REPL
```
```
###Examples

```
from autocomplete import autocomplete,Corpus,nodify

shakespeare = Corpus('sampletexts/allshakespeare.txt') # Construct corpus

autocomplete(corpus=shakespeare,prefix='ham')
>>	hams
>>	hames
>>	hams
>>	hamstring
>>	hamper
>>	hampton
>>	hamlet
>>	hamlets
>>	hamlet
>>	hamlet's
>>	hammer
>>	hammers
>>	hammer
>>	hammer'd
>>	hammering
>>['hams', 'hames', 'hams', 'hamstring', 'hamper', 'hampton', 'hamlet', 'hamlets', 'hamlet', "hamlet's", 'hammer', 'hammers', 
>> 'hammer', "hammer'd", 'hammering']

```
###Tests

###Benchmarks: 
benchmarks/:
	- benchmark.py : generic module for time-benchmarking of functions 
	  & pprinting results of benchmark
	- searchbm.py : benchmarking of time for 
	  naive linear search vs. trie-based search on the Complete Works of
	  Shakespeare
	- README.md : explanation of benchmark module, includes examples

###Status
###Notes

###To-Do
* tests! - include doctests for individual functions; also integration tests (esp. b/c of imports, etc.)
* change Node.insert & Node.find to accept a string or iterable (instead of nodes ); deprecate prefix_corpus.nodify
* implement an autocomplete printer (takes in the same paramters as autocomplete)
 so that autocomplete only returns a list (doesn't auto-print)
* rewrite corpus.pprint() that prints a series of strings instead of 
 one long string
* implement caching for corpuses from given files (perhaps by appending a pickled version to the table)
* explore replacing make_file with a function that returns a generator (that can be written to a file, if desired)
* add support for different split parameters in Corpus construction (i.e. split on [' ', '--'], based on 
 base text)
* refactor use_letter from keypress module as a decorator
* look at recent commits of keypress and one in which i found a segfault
