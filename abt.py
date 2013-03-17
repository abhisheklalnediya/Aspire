# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abt.ui'
#
# Created: Wed Feb  8 21:10:30 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AbtDialog(object):
    def setupUi(self, AbtDialog):
        AbtDialog.setObjectName("AbtDialog")
        AbtDialog.setWindowModality(QtCore.Qt.NonModal)
        AbtDialog.resize(554, 342)
        AbtDialog.setSizeGripEnabled(True)
        self.button2 = QtGui.QPushButton(AbtDialog)
        self.button2.setGeometry(QtCore.QRect(240, 310, 96, 31))
        self.button2.setObjectName("button2")
        self.label = QtGui.QLabel(AbtDialog)
        self.label.setGeometry(QtCore.QRect(20, 220, 521, 71))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(AbtDialog)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 221, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("acm3.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AbtDialog)
        QtCore.QObject.connect(self.button2, QtCore.SIGNAL("clicked()"), AbtDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AbtDialog)

    def retranslateUi(self, AbtDialog):
        AbtDialog.setWindowTitle(QtGui.QApplication.translate("AbtDialog", "ABOUT", None, QtGui.QApplication.UnicodeUTF8))
        self.button2.setText(QtGui.QApplication.translate("AbtDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AbtDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ASPIRE CAM-MICE</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A new and innovative mouse pointer control technology .</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Abhishek Lal,Adhiraj George Shaji,Rajesh Vijayakumar,Prasandh Ravindran</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AbtDialog = QtGui.QDialog()
    ui = Ui_AbtDialog()
    ui.setupUi(AbtDialog)
    AbtDialog.show()
    sys.exit(app.exec_())

