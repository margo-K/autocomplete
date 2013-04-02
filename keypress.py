import termios, fcntl, sys, os,time
import pdb
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd,termios.TCSANOW,newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd,fcntl.F_SETFL,oldflags | os.O_NONBLOCK)

def use_letter(fn,**kwargs):
	print "{} is now on".format(fn.__name__)
	time.sleep(1)
	c = ''
	while True:
		try:
			key = sys.stdin.read(1)
		except IOError:
			pass
		else:
			if key == '\n':
				c = ''
			else:
				c+= key
				print '\033[35m{}\033[0m---'.format(c)
				fn(c,**kwargs)

def clean_up():
	termios.tcsetattr(fd,termios.TCSAFLUSH,oldterm)
	fcntl.fcntl(fd,fcntl.F_SETFL,oldflags)
