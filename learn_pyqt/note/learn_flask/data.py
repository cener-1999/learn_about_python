# -*-coding:utf-8-*-
from Session import get_session
from CREATE import User,Student,RoleEnum
session = get_session()
user_obj = User(ID=102, pwsd=154, Role=RoleEnum.student)
session.add(user_obj)
session.commit()
student_obj = Student(ID=102, name="zhangsan", roomID=101)
session.add(student_obj)
session.commit()