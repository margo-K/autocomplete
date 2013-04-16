from __future__ import print_function
import time
import string
import unittest
import pdb

def _timed(fn,*args):
	start_real = time.time()
	fn(*args)
	end_real = time.time()
	return end_real - start_real

def _simple_min(log,trial=-1):
	winners = []
	min_val = min([time[trial] for time in log.values()])
	for fn in log.keys():
		if log[fn][trial]==min_val:
			winners.append(fn)
	return min_val,winners

def simplereport(log,inputs):
	"""Prints functions and trial times in the log
	Winner is based only on the last value"""

	print("\nReport\n______________\nInput(s):{inputs}".format(inputs=inputs))
	fn_report = "Function: {function}   Time:{time}"
	for fn in log.keys():
		print(fn_report.format(function=fn.__name__,time=log[fn]))

	wintime, winfn = _simple_min(log)
	if len(winfn)==1:
		winfn=winfn[0]
	print("Winning method: {}\nWinning time: {}".format(winfn.__name__,wintime))

def statsreport(log,inputs):
	report = string.Template("""\
	
	Report: $function
	----------------------------------

	AvgTime:$avgtime
	MaxTime:$maxtime
	MinTime:$mintime
	""")

	for fn in log.keys():
		times = log[fn]
		print(report.substitute({'function': fn.__name__,
								'avgtime':sum(times)/len(times),
								'maxtime':max(times),
								'mintime':min(times)
								}))

def benchmark(inputs,fns,reportfn,trials=1,**reportargs):
	if type(fns)!=list:
		fns = [fns]
	log = {fn:[] for fn in fns}

	for fn in fns:
		for trial in range(trials):
			log[fn].append(_timed(fn,*inputs))
	reportfn(log,inputs,**reportargs)

class BenchmarkTests(unittest.TestCase):

	def test_timed(self):
		t = .5
		fn = lambda _: time.sleep(t)
		arg = 'a'
		self.assertEqual(t,_timed(fn,arg))

	def test_benchmarkfn(self):
		pass

if __name__ == '__main__':
	unittest.main()



