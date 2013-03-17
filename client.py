
from socket import *

while 1:
	s = socket(AF_INET,SOCK_STREAM)
	s.connect(('',1235))
	tm = s.recv(1024)
	print 'time is :' ,tm

	t1 = int(raw_input('Enter the value :'))
	t2 = int(raw_input('Enter the value :'))
	t3 = int(raw_input('Enter the value :'))
	mode = str(t1) +" "+ str(t2) +" "+ str(t3)
	s.send(str(mode))
	if t1 == -1 :
		break
s.close()

