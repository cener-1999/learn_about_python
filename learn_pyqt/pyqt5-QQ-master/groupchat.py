# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupchat.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(662, 577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/qq.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 81, 201, 491))
        self.listWidget.setStyleSheet("background-image: url(image/qqchatbk.jpg);")
        self.listWidget.setIconSize(QtCore.QSize(45, 45))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/qqlogin.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/partjob.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/loginbk.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/chatbk.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.listWidget.addItem(item)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 201, 81))
        self.frame.setStyleSheet("background-image: url(:/img/image/qqchatbk.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 40, 201, 41))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(190, -10, 471, 581))
        self.frame_2.setMinimumSize(QtCore.QSize(471, 581))
        self.frame_2.setMaximumSize(QtCore.QSize(471, 581))
        self.frame_2.setStyleSheet(";\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 410, 431, 101))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 81, 431, 311))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(30, 530, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 530, 101, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 471, 61))
        self.frame_3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 61, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Agency FB\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "群聊"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "perl"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "hacker"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "2097557613"))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "小明"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Dialog", "2097557613"))
        self.label.setText(_translate("Dialog", "群聊人员："))
        self.pushButton.setText(_translate("Dialog", "关闭"))
        self.pushButton_2.setText(_translate("Dialog", "发送"))
        self.label_3.setText(_translate("Dialog", "TCP群"))


