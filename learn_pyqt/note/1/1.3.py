import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Ico(QWidget):

    def __init__(self):
       super().__init__()

       self.initUI()    


    def initUI(self):

       self.setGeometry(300, 300, 300, 220)
       self.setWindowTitle('学点编程吧出品')
       self.setWindowIcon(QIcon('xdbcb8.ico'))

       #构造函数的第一个参数是函数的标签，第二个是父窗口小部件
       qbtn = QPushButton('退出', self)
       #PyQt5中的事件处理系统采用信号和槽机制构建。 
       #如果我们点击按钮，点击的信号被发出。 槽可以是Qt槽函数或任何Python可调用的函数。 
       #QCoreApplication包含主事件循环; 它处理和调度所有事件。
       #instance（）方法给我们当前的实例。
       #请注意，QCoreApplication是通过QApplication创建的。 
       #点击的信号连接到终止应用程序的quit（）方法。
       #通信在两个对象之间完成：发送方和接收方。 发送方是按钮，接收者是应用对象。
       qbtn.clicked.connect(QCoreApplication.instance().quit)
       qbtn.resize(70,30)
       qbtn.move(50, 50)

       self.show()

if __name__ == '__main__':

   app = QApplication(sys.argv)
   ex = Ico()
   sys.exit(app.exec_())