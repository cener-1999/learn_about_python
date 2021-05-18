import sys
from random import randint

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from myui import Ui_MainWindow

class run(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(run, self).__init__(parent)
        self.setupUi(self)
        self.num=randint(1,100)
        self.show()

    def on_pushButton_clicked(self):
        guessnumber = int(self.lineEdit.text())

        print(self.num)

        if guessnumber > self.num:

            QMessageBox.about(self, '看结果', '猜大了!')

            self.lineEdit.setFocus()

        elif guessnumber < self.num:

            QMessageBox.about(self, '看结果', '猜小了!')

            self.lineEdit.setFocus()

        else:

            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')

            self.num = randint(1, 100)

            self.lineEdit.clear()

            self.lineEdit.setFocus()
    def closeEvent(self, event):
        reply = QMessageBox.question(self,'go','never give up!')
        if reply ==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    action=run()
    sys.exit(app.exec_())