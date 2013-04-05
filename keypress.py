import termios, fcntl, sys, os,time
import pdb



def setup():
	fd = sys.stdin.fileno()
	oldterm = termios.tcgetattr(fd)

	newattr = termios.tcgetattr(fd)
	newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
	termios.tcsetattr(fd,termios.TCSANOW,newattr)

	oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
	fcntl.fcntl(fd,fcntl.F_SETFL,oldflags | os.O_NONBLOCK)

	return fd,oldterm,oldflags

def clean_up(fd,oldterm,oldflags):
	termios.tcsetattr(fd,termios.TCSAFLUSH,oldterm)
	fcntl.fcntl(fd,fcntl.F_SETFL,oldflags)

def use_letter(fn,**kwargs):
	# _setup()
	print "{} is now on".format(fn.__name__)
	time.sleep(1)
	c = ''
	while True:
		try:
			key = sys.stdin.read(1)
		except IOError:
			time.sleep(0.1)
		else:
			if key == '\n':
				c = ''
			else:
				c+= key
				print '\033[35m{}\033[0m---'.format(c)
				fn(c,**kwargs)
	clean_up(file_no,oldterm)