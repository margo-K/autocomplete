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