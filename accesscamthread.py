'''
Created on 03-Mar-2012

@author: abhisheklal
'''
#import threading
import pyglet
import cv
import Xlib.display
from mouseserver import mousethread
#import pygame
from abt import  Ui_AbtDialog 
#import ImageQt
#import opencv
from PyQt4 import QtCore,QtGui
class accesscamthread():
	'''
	classdocs
	'''
	h_motion_range=20;
	s_motion_range=20;
	v_motion_range=20;
		
	hmax_motion=0;
	hmin_motion=300;
	smax_motion=0;
	smin_motion=300;
	vmax_motion=0;
	vmin_motion=300;
	
	h_motion=0;
	s_motion=0;
	v_motion=0;


	h_click_range=20;
	s_click_range=20;
	v_click_range=20;
	
	hmax_click=0;
	hmin_click=300;
	smax_click=0;
	smin_click=300;
	vmax_click=0;
	vmin_click=300;
	
	h_click=0;
	s_click=0;
	v_click=0;
	
	
	trackersize=5;
	go=1;
	
	screensize_x=0;
	screensize_y=0;
	
	key=-1;
	
	mousesmoothness=2
	prev_mouse_x=-1;
	prev_mouse_y=-1;
	
	clicksensitivity=78
	
	ui=None
	clicksound=None
	aboutwindow=None
	def setmousesmoothness(self,t):
		self.mousesmoothness=t;
	
	def setclicksensitivity(self,t):
		self.clicksensitivity=t;		
	
	def setrange_h_motion_range(self,h):
		self.h_motion_range=h
		print "new h_motion_range "+repr(self.h_motion_range)
	def setrange_s_motion_range(self,s):
		self.s_motion_range=s
	def setrange_v_motion_range(self,v):
		self.v_motion_range=v
		
	def settrackersize(self,t):
		self.trackersize=t;
	
	def seth_motion(self,t):
		self.h_motion=t;
	def sets_motion(self,t):
		self.s_motion=t;
	def setv_motion(self,t):
		self.v_motion=t;
		
	def setrange_h_click_range(self,h):
		self.h_click_range=h
		print "new h_click_range "+repr(self.h_click_range)
	def setrange_s_click_range(self,s):
		self.s_click_range=s
	def setrange_v_click_range(self,v):
		self.v_click_range=v
		
	def seth_click(self,t):
		self.h_click=t;
	def sets_click(self,t):
		self.s_click=t;
	def setv_click(self,t):
		self.v_click=t;
		
	def setkeyc(self):
		self.key=1048675;
		self.ui.selectcolor.setEnabled(1)
		self.ui.setclicktrackerbtn.setEnabled(0)
		self.ui.setmotiontrackerbtn.setEnabled(0)
	def setkeyv(self):
		self.key=1048694;
		self.ui.selectcolor.setEnabled(1)
		self.ui.setclicktrackerbtn.setEnabled(0)
		self.ui.setmotiontrackerbtn.setEnabled(0)
	def setkeyspc(self):
		self.key=1048608
		self.ui.selectcolor.setEnabled(0)
		self.ui.setclicktrackerbtn.setEnabled(1)
		self.ui.setmotiontrackerbtn.setEnabled(1)
	### code to show the about dialog box
	
	def about(self):
		self.aboutwindow = Ui_AbtDialog()
		self.AbtDialog = QtGui.QDialog()
   		self.aboutwindow.setupUi(self.AbtDialog)
  		self.AbtDialog.show()
		#self.aboutwindow=abt.QtGui.QDialog()
		#self.aboutwindow.show()
		##print "About dialog evide poyi"
		
		
	
	def __init__(self,ui,h,s,v):
		'''
		Constructor
		'''
		self.h_motion_range=h
		self.s_motion_range=s
		self.v_motion_range=v
		
		self.h_click_range=h
		self.s_click_range=s
		self.v_click_range=v

		self.ui=ui
		
		ui.h_spinBox.setValue(self.h_motion_range)
		ui.s_spinBox.setValue(self.s_motion_range)
		ui.v_spinBox.setValue(self.v_motion_range)
		
		ui.h_spinBox1.setValue(self.h_click_range)
		ui.s_spinBox1.setValue(self.s_click_range)
		ui.v_spinBox1.setValue(self.v_click_range)
		
		ui.smooth_slide.setValue(self.mousesmoothness)
		
		ui.clickstvt_slide.setValue(self.clicksensitivity)
		
		display = Xlib.display.Display(':0')
		#print display.screen_count()		# output: 1
		root = display.screen().root
		
		#print root.get_geometry().width	 # output: 2960 -> no way to get width of single display?
		#print root.get_geometry().height
		
		#get screen size
		
		self.screensize_x=root.get_geometry().width
		self.screensize_y=root.get_geometry().height
		
		### Click Sound initialising
		
		#pygame.mixer.init()
		#self.click_sound = pygame.mixer.Sound("click.wav")
		self.ui.log_txt.insertHtml("Set motion color and click color to start.<br>")
		
		pass
	
	def capture(self):
		
		print "Starting Camera"
		click=pyglet.resource.media('click1.wav')
		click.play()
		self.setkeyc();
		framenumber=1
		#frameskip=5
		image=None
		frame=None
		
		capture=cv.CreateCameraCapture (-1)
		
		overlay_motion = cv.CreateImage((self.screensize_x+200,self.screensize_y+200), 8, 3)
		overlay_click = cv.CreateImage((self.screensize_x+200,self.screensize_y+200), 8, 3)
		
		#cv.Rectangle(overlay_motion,(0,0),(400,400),cv.Scalar(0,0,225))
		#highgui.cvNamedWindow ('Aspire',CV_WINDOW_AUTOSIZE)
		#highgui.cvNamedWindow ('Aspire~orginal',highgui.CV_WINDOW_AUTOSIZE)
		
		f=0
		x=0
		y=0
		
		mc=mousethread()
		
		print "Position the object above the square and Press any key to set the colour."
		self.ui.log_txt.insertHtml("<b>Position the object above the square and Press any key to set the colour</b>.<br>")
		clicks=0
		while 1:
			if clicks==4 :
				clicks=0
			if self.go==0:
				
				return
			frame=cv.QueryFrame(capture)	
			image=cv.CreateImage((self.screensize_x+200,self.screensize_y+200),8,3)
			framenumber+=1
			#if framenumber%2==0:
			#	continue
			
			#redu=cv.CreateImage((100,100),8,1)
			
			cv.Resize(frame,image)
			cv.Flip(image,image,1)

			#grey=cv.CreateImage(cv.GetSize(image),8,1)#size,depth,channels
			#eig=cv.CreateImage(cv.GetSize(image),32,1)
			#tmp=cv.CreateImage(cv.GetSize(image),32,1)	
			#imghsv=cv.CreateImage(cv.GetSize(image),8,3)
			
			imghsv1_motion=cv.CreateImage(cv.GetSize(image),8,3)
			imgtresh_motion=cv.CreateImage(cv.GetSize(image),8,1)
			imgtreshc_motion=cv.CreateImage(cv.GetSize(image),8,3)
			
			imghsv1_click=cv.CreateImage(cv.GetSize(image),8,3)
			imgtresh_click=cv.CreateImage(cv.GetSize(image),8,1)
			imgtreshc_click=cv.CreateImage(cv.GetSize(image),8,3)
			
			#some stupid function editi the orginal input image so i create duplicat of all
			
			imghsv1_motion_d=cv.CreateImage(cv.GetSize(image),8,3)
			imgtresh_motion_d=cv.CreateImage(cv.GetSize(image),8,1)
			imgtreshc_motion_d=cv.CreateImage(cv.GetSize(image),8,3)
			
			imghsv1_click_d=cv.CreateImage(cv.GetSize(image),8,3)
			imgtresh_click_d=cv.CreateImage(cv.GetSize(image),8,1)
			imgtreshc_click_d=cv.CreateImage(cv.GetSize(image),8,3)
			
			
			
			#imaget=cv2.CreateImage((400,400),8,1)
			
			
			#cv.CvtColor (image, imghsv,cv.CV_BGR2HSV)
			cv.CvtColor (image, imghsv1_motion,cv.CV_RGB2HSV)
			cv.InRangeS(imghsv1_motion, cv.Scalar(self.h_motion-self.h_motion_range, self.s_motion-self.s_motion_range,self.v_motion-self.v_motion_range), cv.Scalar(self.h_motion+self.h_motion_range, self.s_motion+self.s_motion_range,self.v_motion+self.v_motion_range), imgtresh_motion);
			cv.CvtColor(imgtresh_motion,imgtreshc_motion,cv.CV_GRAY2BGR)
			cv.Copy(imgtreshc_motion,imgtreshc_motion_d)
			
			
		
			cv.CvtColor (image, imghsv1_click,cv.CV_RGB2HSV)
			cv.InRangeS(imghsv1_click, cv.Scalar(self.h_click-self.h_click_range, self.s_click-self.s_click_range,self.v_click-self.v_click_range), cv.Scalar(self.h_click+self.h_click_range, self.s_click+self.s_click_range,self.v_click+self.v_click_range), imgtresh_click);
			cv.CvtColor(imgtresh_click,imgtreshc_click,cv.CV_GRAY2BGR)
			cv.Copy(imgtreshc_click,imgtreshc_click_d)
			#pixel_value = cv.Get2D(imghsv1_motion, 0, 0)
			# Since OpenCV loads color images in BGR, not RGB
			#print repr(h_motion - pixel_value[0]) + " " +  repr(s_motion - pixel_value[1]) + " " + repr(v_motion - pixel_value[2])
				
			#h_motion = pixel_value[0]
			#s_motion = pixel_value[1]
			#v_motion = pixel_value[2]
			#print repr(h_motion) + " " + repr(s_motion)  + " " + repr(v_motion) + " " + repr(s_motion+h_motion)
			
			#cv.Copy (frame, image)
			#cv.CvtColor (image, grey, cv._RGB2GRAY)
			#cv.CvtColor (grey,image, cv._GRAY2RGB)
			
			
			
			if f==0 :	# accept motion color
				c=0
				self.h_motion=0
				self.s_motion=0
				self.v_motion=0
				self.hmax_motion=0
				self.hmin_motion= 300
				
				self.smax_motion=0
				self.smin_motion= 300
				
				self.vmax_motion= 0
				self.vmin_motion= 300
				
				#for i in xrange(self.screensize_y-self.trackersize,self.screensize_y) :
					#for j in xrange(self.screensize_x-self.trackersize,self.screensize_x) :
				
				x1=(((self.screensize_x-self.trackersize)+self.screensize_x)/2)#-30
				x2=(((self.screensize_x-self.trackersize)+self.screensize_x)/2)#+30
				y1=(((self.screensize_y-self.trackersize)+self.screensize_y)/2)#-30
				y2=(((self.screensize_y-self.trackersize)+self.screensize_y)/2)#+30
				cv.Circle(image, (int(x1), int(y1)),self.trackersize+10 , (0, 0, 250),3)
				cv.Circle(image, (int(x1), int(y1)),self.trackersize+15 , (0, 0, 240),3)
				
				#cv.Rectangle(image,(x1,y1),(x2,y2),cv.Scalar(50,50,225))
				for i in xrange(self.screensize_x-self.trackersize,self.screensize_x) :
					for j in xrange(self.screensize_y-self.trackersize,self.screensize_y) :
						c+=1
						#print repr(i)+" "+repr(j)
						pixel_value = cv.Get2D(imghsv1_motion, j, i)
						self.h_motion += pixel_value[0]
						self.s_motion += pixel_value[1]
						self.v_motion += pixel_value[2]
						cv.Rectangle(image,(i,j),(i,j),cv.Scalar(0,0,225))
						
						self.hmax_motion= [self.hmax_motion , pixel_value[0]][self.hmax_motion<pixel_value[0]]
						self.hmin_motion= [self.hmin_motion , pixel_value[0]][self.hmin_motion>pixel_value[0]]
						
						self.smax_motion= [self.smax_motion , pixel_value[1]][self.smax_motion<pixel_value[1]]
						self.smin_motion= [self.smin_motion , pixel_value[1]][self.smin_motion>pixel_value[1]]
						
						self.vmax_motion= [self.vmax_motion , pixel_value[2]][self.vmax_motion<pixel_value[2]]
						self.vmin_motion= [self.vmin_motion , pixel_value[2]][self.vmin_motion>pixel_value[2]]
						
						
						#print repr(pixel_value[0]) + ","+repr(pixel_value[1]) + ","+repr(pixel_value[2]) + ",\t",
						
					#print	""
				self.h_motion/=c
				self.s_motion/=c
				self.v_motion/=c	
				#print "\n "+repr(c)+"\t"+repr(h_motion) + "\t" + repr(s_motion)  + "\t" + repr(v_motion)
			
			
			if f==2 : # Accepting click color
				c=0
				self.h_click=0
				self.s_click=0
				self.v_click=0
				self.hmax_click=0
				self.hmin_click= 300
				
				self.smax_click=0
				self.smin_click= 300
				
				self.vmax_click= 0
				self.vmin_click= 300
				
				for i in xrange(self.screensize_x-self.trackersize,self.screensize_x) :
					for j in xrange(self.screensize_y-self.trackersize,self.screensize_y) :
						c+=1
						#print repr(i)+" "+repr(j)
						pixel_value = cv.Get2D(imghsv1_click, j, i)
						self.h_click += pixel_value[0]
						self.s_click += pixel_value[1]
						self.v_click += pixel_value[2]
						cv.Rectangle(image,(i,j),(i,j),cv.Scalar(0,0,225))
						
						self.hmax_click= [self.hmax_click , pixel_value[0]][self.hmax_click<pixel_value[0]]
						self.hmin_click= [self.hmin_click , pixel_value[0]][self.hmin_click>pixel_value[0]]
						
						self.smax_click= [self.smax_click , pixel_value[1]][self.smax_click<pixel_value[1]]
						self.smin_click= [self.smin_click , pixel_value[1]][self.smin_click>pixel_value[1]]
						
						self.vmax_click= [self.vmax_click , pixel_value[2]][self.vmax_click<pixel_value[2]]
						self.vmin_click= [self.vmin_click , pixel_value[2]][self.vmin_click>pixel_value[2]]
						
						
						#print repr(pixel_value[0]) + ","+repr(pixel_value[1]) + ","+repr(pixel_value[2]) + ",\t",
						
					#print	""
				self.h_click/=c
				self.s_click/=c
				self.v_click/=c	
				#print "\n "+repr(c)+"\t"+repr(h_motion) + "\t" + repr(s_motion)  + "\t" + repr(v_motion)
				
			pointerx=-1000
			pointery=-1000
			
			if f==1 : #motion image creation and path finding
				
				
				moments_motion = cv.Moments(imgtresh_motion, 0) 
				area_motion = cv.GetCentralMoment(moments_motion, 0, 0)
				#print repr(area_motion)
				#there can be noise in the video so ignore objects with small areas 
				if(area_motion > 10000): 
					#determine the x and y coordinates of the center of the object 
					#we are tracking by dividing the 1, 0 and 0, 1 moments by the area 
					#print "area " + repr(area)
					x = cv.GetSpatialMoment(moments_motion, 1, 0)/area_motion 
					y = cv.GetSpatialMoment(moments_motion, 0, 1)/area_motion 
					
					x-=100
					y-=100
					pointerx=x
					pointery=y
					#cv.Circle(overlay_motion, (int(x), int(y)),3 , (self.h_motion, self.s_motion, self.v_motion),)
					#cv.Circle(imgtreshc_motion_d, (int(x), int(y)), 3, (self.v_motion, self.s_motion,self.h_motion), 1)
					
					#seq = cv.FindContours(imgtresh_motion, cv.CreateMemStorage(), cv.CV_RETR_TREE, cv.CV_CHAIN_APPROX_SIMPLE)
					#cv.DrawContours(overlay_motion,seq , (100,100,100), (200,200,200),1)
					#cv.DrawContours(imgtreshc_motion_d ,seq,(100,100,100), (0,0,255),1)
					#cv.Add(imgtreshc_motion, overlay_motion, imgtreshc_motion_d)
					#cv.Add(image, overlay_motion, image) 
					
					if self.ui.mousectrlchkbox.isChecked():
						if not((x<=self.prev_mouse_x + self.mousesmoothness)and(x>=self.prev_mouse_x - self.mousesmoothness)):
							if not((y<=self.prev_mouse_y + self.mousesmoothness)and(y>=self.prev_mouse_y - self.mousesmoothness)):
								mc.mouseaction(int(x), int(y), 1)
								self.prev_mouse_x=x
								self.prev_mouse_y=y 
								
						
							
					
					
				else :
					overlay_motion = cv.CreateImage((self.screensize_x+200,self.screensize_y+200), 8, 3)
					pass
					
				imgtresh_click_d=imgtresh_click
				moments_click = cv.Moments(imgtresh_click, 0) 
				area_click = cv.GetCentralMoment(moments_click, 0, 0)
				
				#there can be noise in the video so ignore objects with small areas 
				if(area_click > 10000): 
					#determine the x and y coordinates of the center of the object 
					#we are tracking by dividing the 1, 0 and 0, 1 moments by the area 
					#print "area " + repr(area)
					x = cv.GetSpatialMoment(moments_click, 1, 0)/area_click 
					y = cv.GetSpatialMoment(moments_click, 0, 1)/area_click 
					x-=100
					y-=100
					#cv.Circle(overlay_click, (int(x), int(y)),3 , (self.h_click, self.s_click, self.v_click),)
					#cv.Circle(imgtreshc_click_d, (int(x), int(y)), 3, (self.v_click, self.s_click,self.h_click), 1)
					#cv.Add(imgtreshc_click_d, overlay_click, imgtreshc_click)
					#cv.Add(image, overlay_click, image)
					
					
					#print repr(pointerx) +" "+ repr(x)
					#print repr(x) + " " +repr(pointerx) + " " +repr(y) + " " +repr(pointery)
					#if 1:
					if self.ui.mousectrlchkbox.isChecked():
						
						if (x>=(pointerx-self.clicksensitivity)) and (x<=(pointerx+self.clicksensitivity)) :
							if (y>=(pointery-self.clicksensitivity)) and (y<=(pointery+self.clicksensitivity)) :
								print "click initiatiing";
								if clicks<>3:
									mc.mouseaction(int(pointerx), int(pointery), 2)
									clicks+=1
								else :
									mc.mouseaction(int(pointerx), int(pointery), 4)
								
								if self.ui.clicksound_chkbox.isChecked():
									#self.click_sound.play()#
									click=pyglet.resource.media('click1.wav')
									click.play()
									pass
								#return
						else:
							clicks=0
				else :
					overlay_click = cv.CreateImage((self.screensize_x+200,self.screensize_y+200), 8, 3)
					
					
					#add the thresholded image back to the img so we can see what was  
					#left after it was applied 
					#cv.Merge(imgtresh_motion, None, None, None, image)
			
					#for p in points[1]:
						#print p.x,"asdsd";
						#cv.Circle(imgtreshc_motion,(int(p.x),int(p.y)),3,cv.Scalar(v_motion,s_motion,h_motion,0),-1,8,0)
						#cv.ShowImage ('Aspire~Treshold', imgtreshc_motion)
					
					# cv.ShowImage ('hsv1', overlay_motion)
					#cv.Resize(imgtresh_motion,redu);
			
			
			#imagepil = ImageQt.ImageQt(opencv.adaptors.Ipl2PIL(image).transpose(Image.FLIP_LEFT_RIGHT))
			#pixmap = QtGui.QPixmap.fromImage(imagepil)
			#self.ui.label_3.setPixmap(pixmap)
			
			
			
			##Resize and display
			disp_scale=25
			imgtreshc_motion_disp=cv.CreateImage((304,171),8,3)### changed value from 16-12 & 9-8
			imgtreshc_click_disp=cv.CreateImage((304,171),8,3)### changed value from 16-12 & 9-8
			image_disp=cv.CreateImage((608,342),8,3)### changed value from 16 - 24
			
			cv.Resize(imgtreshc_motion_d,imgtreshc_motion_disp)
			cv.Resize(imgtreshc_click_d,imgtreshc_click_disp)
			cv.Resize(image,image_disp)
			
			#cv.ShowImage ('Aspire-Treshold', imgtreshc_motion_disp)
			#cv.ShowImage ('Aspire-Treshold click', imgtreshc_click_disp)
			#cv.ShowImage ('Aspire-Cam', image_disp)
			
			### Display the 3 images in the GUI
			
			qimage = QtGui.QImage(image_disp.tostring(), image_disp.width, image_disp.height, QtGui.QImage.Format_RGB888).rgbSwapped()
			pixmap = QtGui.QPixmap.fromImage(qimage)
			self.ui.labimage.setPixmap(pixmap)
			qimage = QtGui.QImage(imgtreshc_motion_disp.tostring(), imgtreshc_motion_disp.width, imgtreshc_motion_disp.height, QtGui.QImage.Format_RGB888).rgbSwapped()
			pixmap = QtGui.QPixmap.fromImage(qimage)
			self.ui.labtresh1.setPixmap(pixmap)
			qimage = QtGui.QImage(imgtreshc_click_disp.tostring(), imgtreshc_click_disp.width, imgtreshc_click_disp.height, QtGui.QImage.Format_RGB888).rgbSwapped()
			pixmap = QtGui.QPixmap.fromImage(qimage)
			self.ui.labtresh2.setPixmap(pixmap)


			#cv.ShowImage ('Aspire-Cam frame', frame)
			#self.ui.graphicsView.updateSceneRect(image)
			s=cv.WaitKey(10)
			
			
			
			if self.key<>-1 :
				#print self.key;
				if self.key==1048675:
					f=0;
					print "Selecting motion color."
					self.ui.log_txt.insertHtml("Selecting motion color.<br>")
				else :
					if self.key==1048694:
						print "Selecting click color."
						self.ui.log_txt.insertHtml("Selecting click color.<br>")
						f=2;
					else :
						if self.key==1048603:
							print("Exiting....");
							self.ui.log_txt.insertHtml("<b>Camera Stopped.</b><br>")
							self.ui.start_camera_btn.setText("Start Camera")
							return
						else :
							if self.key==1048608:   #space key to fix color
								self.ui.h_slide.setValue(self.h_motion);
								self.ui.s_slide.setValue(self.s_motion);
								self.ui.v_slide.setValue(self.v_motion);
								
								self.ui.h_slide1.setValue(self.h_click);
								self.ui.s_slide1.setValue(self.s_click);
								self.ui.v_slide1.setValue(self.v_click);
								
								
								#self.ui.h_slide.setEnabled(1)
								#self.ui.s_slide.setEnabled(1)
								#self.ui.v_slide.setEnabled(1)
								
								#print "("+repr(self.hmax_motion)+" , "+repr(self.smax_motion)+" , "+repr(self.vmax_motion)+")";
								#print "("+repr(self.hmin_motion)+" , "+repr(self.smin_motion)+" , "+repr(self.vmin_motion)+")";
								
								print "Press c to set motion color, v to set click color"
								f=1
								
			self.key=-1
								
