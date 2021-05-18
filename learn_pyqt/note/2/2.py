"""
按钮小提示
QLineEdit小部件使用
QMessageBox的使用
关闭窗口事件触发
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint

class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1,100)    

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70 ,30)
        #鼠标移上去时会弹出来提示
        #要创建一个工具提示，我们调用setTooltip()方法。 我们可以使用富文本格式。
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        #绑定事件
        self.bt1.clicked.connect(self.showMessage)  
        
        #显示数字
        self.text = QLineEdit('在这里输入数字', self)
        #选中所有
        self.text.selectAll()
        #变成被选择状态，和上一条一起组成
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150 ,30)

        self.show()    

    def showMessage(self):

        guessnumber = int(self.text.text())
        print(self.num)    
    
        if guessnumber > self.num:
            QMessageBox.about(self, '看结果','猜大了!')
            #setFocus()就是让焦点置于文本栏中，方便用户输入
            self.text.setFocus()        
        elif guessnumber < self.num:
            #QMessageBox.about就是弹出一个对话框
            QMessageBox.about(self, '看结果','猜小了!')
            self.text.setFocus()       
        else:
            QMessageBox.about(self, '看结果','答对了!进入下一轮!')
            self.num = randint(1,100)
            self.text.clear()
            self.text.setFocus()    
        
    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
        #accept就行了吗，为什么
            event.accept()        
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())