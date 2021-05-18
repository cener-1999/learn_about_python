#-*-coding:utf-8-*-
import pymysql
from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''初次调用create_engine的时候并不会真正连接数据库，这是为了节省资源，叫做Lazy Connecting'''
engine=create_engine("mysql+pymysql://root:nbuser@localhost:3306/LearnDB",echo=True)

'''
#配置ORM时，分为两部分，1.描述要处理的数据库表的信息；2.将python类映射到这些表上来
#在sqlAlchemy中一起完成，成为Declarative
#使用Declarative参与ORM映射的类需要被定义为一个指定基类的子类
#这个基类应当含有ORM映射关系中的类和表的信息；这样的基类成为declarative base class
#在应用中，一般只需要一个这样的基类，这样的基类可以通过declarative_base来创建
'''

#映射声明，基类
Base = declarative_base()
#创建Session类，基类
Session = sessionmaker(bind=engine)

#构建新的Session
session=Session()

#定义对象
class Course(Base):
    #表名
    __tablename__='course'
    id=Column(Integer,primary_key=True)
    course_name=Column(String(20),default=None,nullable=False,comment='课程名称')
    teacher_name=Column(String(20),default=None,nullable=False,comment='任课老师')
    class_times=Column(Integer,default=0,nullable=False,comment='课时')

'''类的声明完成后，Declarative会将所有的Column成员替换为特殊的Python访问器，从而映射成能够读写数据库的表和列'''

#在DB中建表
Base.metadata.create_all(engine)

'''要应用类对象操作表，还需要一个Session对象，ORM对DB的入口即Session
当构建应用是，在create_engine的同一级别下定义一个Session类，作为生成新的Session类的工厂（Factory）类。
构建方式如下 Session = sessionmaker(bind=engine)  session=Session()
'''

'''为了将Course对象存入DB,需要调用Session的add()函数'''
#创建Course类实例
course_obj=Course(course_name='Python',teacher_name='ZHANG SAN',class_times='32')
#添加对象
session.add(course_obj)
'''add()之后，添加的实例状态为pending，就是目前实际上还没有执行sql操作，在DB中还没有产生对应的行，此时数据是存在内存中的
若要写入DB，还需要调用Session的commit()方法提交'''
session.commit()



