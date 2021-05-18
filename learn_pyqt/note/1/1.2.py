import sys
from PyQt5.QtWidgets import QApplication, QWidget
#引入图标类
from PyQt5.QtGui import QIcon

class Ico(QWidget):
    
   #初始化
   def __init__(self):
       super().__init__()
       self.initUI()    
    
    #程序的GUI界面用initUI()函数创建
   def initUI(self):

       self.setGeometry(300, 300, 300, 220)
       self.setWindowTitle('学点编程吧出品')
       self.setWindowIcon(QIcon('xdbcb8.ico'))

       self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())