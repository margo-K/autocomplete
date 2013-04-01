import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd,termios.TCSANOW,newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd,fcntl.F_SETFL,oldflags | os.O_NONBLOCK)

def use_letter(fn,*args):
	try:
		c = ''
		while True:
			try:
				let = sys.stdin.read(1)
				if let == '\n':
					c = ''
				else:
					c+= let
					print '----'+c+'----'
					fn(c,*args)
			except IOError: pass 
	finally:
		termios.tcsetattr(fd,termios.TCSAFLUSH,oldterm)
		fcntl.fcntl(fd,fcntl.F_SETFL,oldflags)