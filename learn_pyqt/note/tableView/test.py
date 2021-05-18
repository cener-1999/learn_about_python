# -*-coding:utf-8-*-
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QBrush
from ui import Ui_Dialog
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyMainForm(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # n=5
        # self.tableWidget.setRowCount(n)
        # 设置标题与初始大小
        # self.setWindowTitle('QTableView表格视图的例子')
        # self.resize(500, 300)
        n=0

        self.model = QStandardItemModel(4, 2)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['old', 'new'])

        # #Todo 优化2 添加数据
        # self.model.appendRow([
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        # ])

        for row in range(4):
            for column in range(2):
                item = QStandardItem(str(1))
                # 设置每个位置的文本值
                self.model.setItem(row, column, item)
                # print(item.text())

        # 实例化表格视图，设置模型为自定义的模型
        self.tableView.setModel(self.model)

        # 设置数据层次结构，4行4列
        self.pushButton.clicked.connect(lambda: self.adddata(n))
        self.pushButton_2.clicked.connect(lambda: self.getnum())

    def adddata(self,n):
        mydata=self.getnum()
        print(mydata)
        self.model = QStandardItemModel(4, 2)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['old', 'new'])

        # #Todo 优化2 添加数据
        # self.model.appendRow([
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        #     QStandardItem('row %s,column %s' % (11,11)),
        # ])
        for row in range(4):
            for column in range(2):
                item = QStandardItem(str(2))
                # 设置每个位置的文本值
                self.model.setItem(row, column, item)
                # print(item.text())

        # 实例化表格视图，设置模型为自定义的模型
        self.tableView.setModel(self.model)
        # print(self.tableView.model().rowCount())
        # test = [[0] * 2 for _ in range(4)]
        # test[0][1]=1
        # test[1][0]=1
        # print(test)

        # #todo 优化1 表格填满窗口
        # #水平方向标签拓展剩下的窗口部分，填满表格
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # #水平方向，表格大小拓展到适当的尺寸
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #
        # #TODO 优化3 删除当前选中的数据
        # indexs=self.tableView.selectionModel().selection().indexes()
        # print(indexs)
        # if len(indexs)>0:
        #     index=indexs[0]
        #     self.model.removeRows(index.row(),1)

        # 设置布局
    def getnum(self):
        myrow=self.tableView.model().rowCount()
        test = [[0] * 2 for _ in range(myrow)]

        for row in range(myrow):
            for colnum in range(2):
                test[row][colnum]=self.tableView.model().item(row, colnum).text()
        # print(test)
        return test

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
