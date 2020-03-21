# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'leadgram.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(593, 518)
        self.textEdit1 = QtWidgets.QTextEdit(Form)
        self.textEdit1.setGeometry(QtCore.QRect(20, 220, 251, 31))
        self.textEdit1.setObjectName("textEdit1")
        self.textEdit2 = QtWidgets.QTextEdit(Form)
        self.textEdit2.setGeometry(QtCore.QRect(310, 220, 251, 31))
        self.textEdit2.setObjectName("textEdit2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(470, 20, 101, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 451, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 151, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 160, 591, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 180, 151, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 181, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 151, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(310, 200, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(310, 290, 221, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(310, 270, 151, 17))
        self.label_9.setObjectName("label_9")
        self.textEdit2_2 = QtWidgets.QTextEdit(Form)
        self.textEdit2_2.setGeometry(QtCore.QRect(310, 310, 251, 31))
        self.textEdit2_2.setObjectName("textEdit2_2")
        self.textEdit1_2 = QtWidgets.QTextEdit(Form)
        self.textEdit1_2.setGeometry(QtCore.QRect(20, 310, 251, 31))
        self.textEdit1_2.setObjectName("textEdit1_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 290, 221, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(20, 270, 181, 17))
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 460, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 460, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 430, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 160, 591, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LeadGram"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">LeadGram</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Application will scrape Instagram username ,phone and email.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter your Instagram username and password,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Desired username (not Full Name),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and report file name (csv).</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Required Details</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Password:</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">UserName:</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "Instagram Username."))
        self.label_7.setText(_translate("Form", "Instagram Password."))
        self.label_8.setText(_translate("Form", "Output File to save report (csv)."))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Report File:</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p>Followers to scrape from.</p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">UserName To Scrape:</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

