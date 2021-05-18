#发送自定义信号
'''
信号与槽连接
事件处理重写
事件发送者
发出自定义信号
'''
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtCore import (pyqtSignal, QObject)

#我们创建一个名为showmouse的新信号。
#pyqtSignal（）作为外部Signal类的类属性创建一个信号

class Signal(QObject):#(1)
    showmouse = pyqtSignal()

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')
        #创建对象
        self.s = Signal()#(2)
        #自定义showmouse信号连接到QMainWindow的about（）的槽。
        #所以这个connect是把信号连接在槽事件的意思吗
        self.s.showmouse.connect(self.about)#(4)

        self.show()
    def about(self):
        QMessageBox.about(self,'鼠标','你点鼠标了吧！')

    #当我们用鼠标指针点击窗口时，会发出showmouse信号,调用相应的槽函数。
    #爷悟了
    def mousePressEvent(self, e):#(3)
        self.s.showmouse.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())