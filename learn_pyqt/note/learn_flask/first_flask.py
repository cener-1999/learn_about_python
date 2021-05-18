# -*-coding:utf-8-*-
from flask import Flask
from CREATE import Student
from Session import get_session
app = Flask(__name__)

@app.route('/first_test')
def table_query():
    print("why not?")
    session = get_session()
    # 数据查询
    query_result = session.query(Student).filter(Student.ID==102)
    print(query_result)#这种写法不是很熟
    print("why not print?")
    return str(query_result)