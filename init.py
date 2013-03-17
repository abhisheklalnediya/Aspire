#!/usr/bin/env python
#python
'''
Created on 03-Mar-2012

@author: abhisheklal
'''
from mainui import Ui_MainWindow
from PyQt4 import QtGui,QtCore
#import threading
import sys
import accesscamthread

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s
class mainclass(object):
	mousectrl=None
	ac=None
	ui=None
	app=None
	MainWindow=None
	cam_runing=0
	
	def startcamera(self):
		
		if self.ui.start_camera_btn.text()=="Start Camera":
			self.ui.start_camera_btn.setText("Stop Camera")
			self.cam_runing=1
			self.ac.go=1
			self.ui.log_txt.insertHtml("Starting Camera.<br>")
			self.ac.capture()
			
			
		else:
			self.ui.log_txt.insertHtml("<b>Camera Stopped.</b><br>")
			self.ui.start_camera_btn.setText("Start Camera")
			self.ac.go=0
			self.cam_runing=0
			
	def stopcamera(self):
			self.ui.start_camera_btn.setText("Start Camera")
			self.ac.go=0
			self.cam_runing=0	
			
	def togglem(self):
		self.ui.mousectrlchkbox.toggle()


if __name__ == '__main__':
	
	mc=mainclass()
	mc.app = QtGui.QApplication(sys.argv)
	mc.MainWindow = QtGui.QMainWindow()
	mc.ui = Ui_MainWindow()
	mc.ui.setupUi(mc.MainWindow)
	
	
	
	
	mc.ac=accesscamthread.accesscamthread(mc.ui,5,45,45)
	
	
	mc.ui.h_slide.setValue(mc.ac.h_motion_range)
	mc.ui.s_slide.setValue(mc.ac.s_motion_range)
	mc.ui.v_slide.setValue(mc.ac.v_motion_range)
	
	mc.ui.h_slide1.setValue(mc.ac.h_click_range)
	mc.ui.s_slide1.setValue(mc.ac.s_click_range)
	mc.ui.v_slide1.setValue(mc.ac.v_click_range)
	
	mc.ui.t_slide.setValue(mc.ac.trackersize)
	#mc.ui.h_slide.setDisabled(1);
	#mc.ui.s_slide.setDisabled(1);
	#mc.ui.v_slide.setDisabled(1);
	
	
	try:
		
		
		
		QtCore.QObject.connect(mc.ui.setclicktrackerbtn , QtCore.SIGNAL(_fromUtf8("clicked()")),mc.ac.setkeyv)
		QtCore.QObject.connect(mc.ui.setmotiontrackerbtn , QtCore.SIGNAL(_fromUtf8("clicked()")),mc.ac.setkeyc)
		QtCore.QObject.connect(mc.ui.selectcolor , QtCore.SIGNAL(_fromUtf8("clicked()")),mc.ac.setkeyspc)
		
		QtCore.QObject.connect(mc.ui.actionAbout , QtCore.SIGNAL(_fromUtf8("activated()")),mc.ac.about)
		QtCore.QObject.connect(mc.ui.actionExit , QtCore.SIGNAL(_fromUtf8("activated()")),mc.stopcamera)
		QtCore.QObject.connect(mc.ui.actionSet_Color , QtCore.SIGNAL(_fromUtf8("activated()")),mc.ac.setkeyspc)
		QtCore.QObject.connect(mc.ui.actionSet_Motion_Tracker , QtCore.SIGNAL(_fromUtf8("activated()")),mc.ac.setkeyc)
		QtCore.QObject.connect(mc.ui.actionSet_Click_Tracker , QtCore.SIGNAL(_fromUtf8("activated()")),mc.ac.setkeyv)
		QtCore.QObject.connect(mc.ui.actionSet_Mouse_Control , QtCore.SIGNAL(_fromUtf8("activated()")),mc.togglem)
		#QtCore.QObject.connect(mc.ui, QtCore.SIGNAL(_fromUtf8("destroyed()")),mc.stopcamera)
		#QtCore.QObject.connect(mc.ui, QtCore.SIGNAL(_fromUtf8("closed()")),mc.stopcamera)
		
		QtCore.QObject.connect(mc.ui.h_spinBox,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setrange_h_motion_range)
		QtCore.QObject.connect(mc.ui.s_spinBox,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setrange_s_motion_range)
		QtCore.QObject.connect(mc.ui.v_spinBox,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setrange_v_motion_range)
		
		QtCore.QObject.connect(mc.ui.t_slide,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.settrackersize)
		
		QtCore.QObject.connect(mc.ui.h_slide,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.seth_motion)
		QtCore.QObject.connect(mc.ui.s_slide,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.sets_motion)
		QtCore.QObject.connect(mc.ui.v_slide,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setv_motion)
		
		QtCore.QObject.connect(mc.ui.h_spinBox1,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setrange_h_click_range)
		QtCore.QObject.connect(mc.ui.s_spinBox1,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setrange_s_click_range)
		QtCore.QObject.connect(mc.ui.v_spinBox1,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setrange_v_click_range)
		
		QtCore.QObject.connect(mc.ui.h_slide1,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.seth_click)
		QtCore.QObject.connect(mc.ui.s_slide1,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.sets_click)
		QtCore.QObject.connect(mc.ui.v_slide1,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setv_click)
		
		QtCore.QObject.connect(mc.ui.smooth_slide,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setmousesmoothness)
		QtCore.QObject.connect(mc.ui.clickstvt_slide ,QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),mc.ac.setclicksensitivity)
		
		QtCore.QObject.connect(mc.ui.start_camera_btn, QtCore.SIGNAL(_fromUtf8("clicked()")),mc.startcamera)
		
	except Exception:
		print "Thread already started" 
	
	mc.MainWindow.show()
	
	
	sys.exit(mc.app.exec_())
