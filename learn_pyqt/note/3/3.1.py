import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QDial, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        #lcd是什么玩意，lcd数字显示槽
        lcd = QLCDNumber(self)
        #用了对话框了
        dial = QDial(self)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')

        lcd.setGeometry(100,50,150,60)
        dial.setGeometry(120,120,100,100)
        
        #出现了！事件
        #将QDial这个小部件的一个valueChanged信号连接到lcd数字的显示槽
        #dial对象发送信号，lcd接受信号，槽是对信号做出的反应
        dial.valueChanged.connect(lcd.display)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())