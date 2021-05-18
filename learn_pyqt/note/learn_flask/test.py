# -*-coding:utf-8-*-
from Session import get_session
from CREATE import Student
def table_query():
    print("why not?")
    session = get_session()
    # 数据查询
    query_result = session.query(Student).all()
    print(query_result)
    for item in query_result:
        print(f'查询结果为==>{item}')#这种写法不是很熟
    print("why not print?")


table_query()