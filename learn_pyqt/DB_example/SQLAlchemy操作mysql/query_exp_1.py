# 从session_create.py文件中导入get_session函数
from chapter5.common.session_create import get_session
# 从course.py文件中导入Course类
from chapter5.common.course import Course


def table_query():
    """
    表数据查询
    :return:
    """
    # 取得session对象
    session = get_session()
    # 数据查询
    query_result = session.query(Course).all()
    for item in query_result:
        print(f'查询结果为==>{item}')#这种写法不是很熟
    #在Course类中添加__repr__()方法对于打印指定形式的结果的便捷性


if __name__ == "__main__":
    table_query()
