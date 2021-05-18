#用QTime类实现定时触发槽函数的功能
'''
QTimer类提供重复和单次定时器。
QTimer类为定时器提供高级编程接口。要使用它，请创建一个QTimer，
将其timeout()信号连接到相应的插槽，
然后调用start()。从那时起，它将以恒定的间隔发出timeout()信号。
'''

"""示例1：每隔一秒调用update()这个槽函数"""

#建一个timer对象
timer = QTimer()
#将timer和槽函数连接在一起
timer.timeout.connect(self.update)
#设置间隔
timer.start(1000)

"""示例2：您可以通过调用setSingleShot(True)将计时器设置为仅超时一次。
您还可以使用静态QTimer.singleShot()函数在指定的时间间隔后调用槽函数："""

QTimer.singleShot(2000, self.function)
    
def function(self):
    print('start')