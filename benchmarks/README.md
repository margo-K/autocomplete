#Benchmark
A simple benchmarking utility for timing functions, comparing run time
of functions with the same input and producing reports comparing them

###Contents
- __benchmark.py__: main module, contains all helper functions for benchmarking
- searchbm.py: example of benchmarking search using a trie and linear search

###Requirements
None

###Getting Started
Benchmark is designed to be imported into a the python REPL
or into a script for benchmarking a particular application

####Primary Function (must always be imported):
- __benchmark(inputs,fns,reportfn,trials,*reportargs)__: does all 
the work of benchmarking (times the fns, prints a report)

####Current Report Functions (passed to benchmark fn)
- simplereport: prints all times in the log for all functions in the log
- statsreport: prints the avgtime, maxtime and mintime for all functions in the log

Note: User-defined report functions can also be passed using the reportfn keyword (see example in searchbm.py)

###Examples


Using the following functions for benchmarking:

```
def add(a,b):
	return a+b

def mult(a,b):
	return a*b
```


####Benchmark Two Functions with the Same Input:

```
from benchmark import simplereport,benchmark

benchmark((1,2),[add,mult],simplereport)

>>>---REPORT---
>>Input(s):(1, 2)
>>Function: mult   Time:0.0
>>Function: add   Time:2.14576721191e-06

```

####Benchmark a Single Function:

```
from benchmark import simplereport,benchmark

benchmark((1,2),add,simplereport)

>>---REPORT---
>>Input(s):(1, 2)
>>Function: add   Time:1.90734863281e-06
```

####Benchmark Using Multiple Trials:

```
from benchmark import statsreport,benchmark

benchmark((1,2),[add,mult],statsreport,trials=10)


	Report: mult
	----------------------------------

	AvgTime:5.24520874023e-07
	MaxTime:1.19209289551e-06
	MinTime:0.0
	
	
	Report: add
	----------------------------------

	AvgTime:4.76837158203e-07
	MaxTime:9.53674316406e-07
	MinTime:0.0

```




###Tests
- benchmark.py includes BenchmarkTests, a series of unittests

###Status & Notes
####Features to Add
* Add reporting function for comparing multiple inputs
* Add graph support:

	Ex: Prefix-Tree vs. Linear-Search 
		x-axis: size of input (measured by word-count)
		y-axis: time to build corpus

	or 
		x-axis: number of unique words in corpus
		y-axis: time to search in linear search vs. prefix-tree-search

* Add benchmarking for memory usage
* Add ability incorporate cProfile breakdown for function into report

####TO-DO List:
- add more unittests

####Design Decisions
- determine whether another interface should be implemented (similar to cProfile's multiple interfaces: could possibly 'benchmark' the __main__ 
functions of two files)






