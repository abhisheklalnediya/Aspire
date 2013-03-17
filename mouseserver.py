from socket import *
#import time
from Xlib import display
import Xlib.ext.xtest
#import threading



class mousecontrol:	#class definition
	def __init__(self):
		self.display = display.Display()
		self.screen = self.display.screen()
		self.root = self.screen.root


	def mousepos(self):
		data = self.root.query_pointer()._data
		x = data["root_x"]
		y = data["root_y"]
		return x , y
	def mousemov(self,x,y):
		self.root.warp_pointer(x,y)
		self.display.sync()
	
	def leftclick(self,x,y):
		Xlib.ext.xtest.fake_input(self.display,Xlib.X.ButtonPress, 1)
		self.display.sync()
		Xlib.ext.xtest.fake_input(self.display,Xlib.X.ButtonRelease, 1)
		self.display.sync()
	
	def midclick(self,x,y):
		Xlib.ext.xtest.fake_input(self.display,Xlib.X.ButtonPress, 2)
		self.display.sync()
		Xlib.ext.xtest.fake_input(self.display,Xlib.X.ButtonRelease, 2)
		self.display.sync()
	
	def rightclick(self, x, y):
		Xlib.ext.xtest.fake_input(self.display,Xlib.X.ButtonPress, 3)
		self.display.sync()
		Xlib.ext.xtest.fake_input(self.display,Xlib.X.ButtonRelease, 3)
		self.display.sync()



class mousethread():
	port=None
	def setport(self,p):
		self.port=p
		
		
	def mouseaction(self,x,y,action):

				#tm = client.recv(1024)
				dat=[x,y,action]
								
				if int(dat[2]) == 1:
					m = mousecontrol()	#object creation
					m.mousemov(int(dat[0]),int(dat[1]))	#method calling
					##print ("Mouse move evoked")
					#print("The mouse position on the screen is {0}".format(m.mousepos()))	
				if int(dat[0]) == -1 :
					#break
					pass
				if int(dat[2]) == 2:
					m = mousecontrol()	#object creation
					m.leftclick(int(dat[0]),int(dat[1]))	#method calling
					#print ("Left Click evoked")
					#print("The mouse position on the screen is {0}".format(m.mousepos()))
				if int(dat[2]) == 3:
					m = mousecontrol()	#object creation
					m.midclick(int(dat[0]),int(dat[1]))	#method calling
					#print ("Middle Click evoked")
					#print("The mouse position on the screen is {0}".format(m.mousepos()))		
				if int(dat[2]) == 4:
					m = mousecontrol()	#object creation
					m.rightclick(int(dat[0]),int(dat[1]))	#method calling
					#print ("Mouse Right Click evoked")
					#print("The mouse position on the screen is {0}".format(m.mousepos()))
				if int(dat[2]) == 5:
					m = mousecontrol()	#object creation
					m.leftclick(int(dat[0]),int(dat[1]))	#method calling
					m.leftclick(int(dat[0]),int(dat[1]))
					#print ("Double Click evoked")
					#print("The mouse position on the screen is {0}".format(m.mousepos()))
