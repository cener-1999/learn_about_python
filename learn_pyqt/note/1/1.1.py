import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    #每个PyQt5应用程序必须创建一个应用程序对象。 sys.argv参数是来自命令行的参数列表。
    app = QApplication(sys.argv)

    #QWidget小部件是PyQt5中所有用户界面对象的基类。 我们提供了QWidget的默认构造函数。
    #默认构造函数没有父类。 没有父类口小部件称为窗口。
    w = QWidget()
    #调整窗口大小
    w.resize(250, 150)
    #从屏幕的哪里打开
    w.move(300, 300)
    w.setWindowTitle('学点编程吧出品')
    #在屏幕上显示窗口，先在内存中创建，再在屏幕上显示
    w.show()
    #开始应用程序的主循环
    sys.exit(app.exec_())