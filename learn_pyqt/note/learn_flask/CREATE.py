# -*-coding:utf-8-*-
# -*-coding:utf-8-*-
import enum

import pymysql
from sqlalchemy import Column, Integer, String, Enum, create_engine, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Session import get_session
from sqlalchemy.sql import func

engine = create_engine('mysql+pymysql://root:nbuser@localhost:3306/testdb?charset=utf8', echo=True)
# 声明映射
Base = declarative_base()
#映射声明，基类
Base = declarative_base()

session=get_session()

class RoleEnum(enum.Enum):
    teacher=1
    student=2

class User(Base):
    __tablename__='USER'
    ID=Column(Integer,primary_key=True)
    pwsd=Column(Integer)
    Role=Column(Enum(RoleEnum))

    def __repr__(self):
        ID = self.ID
        passward = self.pwsd
        Role = self.Role
        return f"Course:(ID={ID},ROLE={Role})"

class Teacher(Base):
    __tablename__="Teacher"
    ID=Column(Integer,ForeignKey(User.ID),primary_key=True)
    name=Column(String(100))

class Student(Base):
    __tablename__="Student"
    ID=Column(Integer,ForeignKey(User.ID),primary_key=True)
    name=Column(String(100))
    roomID=Column(Integer)

class Class(Base):
    __tablename__='Class'
    ClassID=Column(Integer,primary_key=True)
    Class_name=Column(String(30))
    teacherID=Column(Integer,ForeignKey(Teacher.ID))

class Reports(Base):
    __tablename__="Reports"
    reportID=Column(Integer,autoincrement=True,primary_key=True)
    classID=Column(Integer,ForeignKey(Class.ClassID))
    create_time = Column(DateTime,default=func.now())

class Report(Base):
    __tablename__ = "Report"
    reportID = Column(Integer, ForeignKey(Reports.reportID), primary_key=True)
    student_ID = Column(Integer, ForeignKey(Student.ID))
    #name = Column(String(100),ForeignKey(Student.name))  name用语句查就行
    grade=Column(Integer)

Base.metadata.create_all(engine)


