# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ergo2\OneDrive - Faculty of Information Technologies\Documents\GitHub\SEP--text-comparator\tekst.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1785, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textA = QtWidgets.QTextEdit(self.centralwidget)
        self.textA.setGeometry(QtCore.QRect(10, 50, 551, 621))
        self.textA.setReadOnly(True)
        self.textA.setObjectName("textA")
        self.textB = QtWidgets.QTextEdit(self.centralwidget)
        self.textB.setGeometry(QtCore.QRect(580, 50, 551, 621))
        self.textB.setReadOnly(True)
        self.textB.setObjectName("textB")
        self.labelA = QtWidgets.QLabel(self.centralwidget)
        self.labelA.setGeometry(QtCore.QRect(10, 15, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelA.setFont(font)
        self.labelA.setObjectName("labelA")
        self.labelB = QtWidgets.QLabel(self.centralwidget)
        self.labelB.setGeometry(QtCore.QRect(580, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelB.setFont(font)
        self.labelB.setObjectName("labelB")
        self.pb_A = QtWidgets.QPushButton(self.centralwidget)
        self.pb_A.setGeometry(QtCore.QRect(430, 20, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pb_A.setFont(font)
        self.pb_A.setObjectName("pb_A")
        self.pb_B = QtWidgets.QPushButton(self.centralwidget)
        self.pb_B.setGeometry(QtCore.QRect(1000, 20, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pb_B.setFont(font)
        self.pb_B.setObjectName("pb_B")
        self.pb_Compare = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Compare.setGeometry(QtCore.QRect(10, 680, 1121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_Compare.setFont(font)
        self.pb_Compare.setObjectName("pb_Compare")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1785, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textA.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textB.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.labelA.setText(_translate("MainWindow", "Preview of text A"))
        self.labelB.setText(_translate("MainWindow", "Preview of text B"))
        self.pb_A.setText(_translate("MainWindow", "Browse"))
        self.pb_B.setText(_translate("MainWindow", "Browse"))
        self.pb_Compare.setText(_translate("MainWindow", "Compare"))