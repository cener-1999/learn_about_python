# -*-coding:utf-8-*-
import sys

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QAbstractItemView
from ui import Ui_Dialog

class Test(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)
        self.setupUi(self)

        #table model hang lie
        self.model=QStandardItemModel(3,4)
        self.model.setHorizontalHeaderLabels(["class_id","class_num","teacher_id","sum"])

        arr = ['jak', 'tom',"an","bad"]
        for row in range(4):
            for column in range(4):
                item = QStandardItem(str(arr[column]))
                self.model.setItem(row, column, item)
                self.tableView.setModel(self.model)

        self.tableView.setModel(self.model)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        r = self.tableView.selectionModel().selectedRows()
        print(r)
        #self.tableView.columnCountChanged().connect(print(self.tableView.currentIndex().row()))


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = Test()
    myWin.show()
    sys.exit(app.exec_())


