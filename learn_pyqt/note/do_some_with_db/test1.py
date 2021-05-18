import pymysql
from sqlalchemy import create_engine

#engine=create_engine('mysql+pymysql://root:nbuser@localhost::3306')

#print(f'the version of SQLAlchemy:{sqlalchemy.__version__}')

db=pymysql.connect(host='localhost',user='root',password='nbuser',database='LearnDB')
# 使用数据库连接对象的 cursor() 方法创建一个游标对象 cursor
cursor=db.cursor()
# 使用游标对象的 execute() 方法执行 SQL 查询
cursor.execute('SELECT VERSION()')
# 使用游标对象的 fetchone() 方法获取单条数据.
data=cursor.fetchone()
print(f'Database Version:{data}')
# 关闭数据库连接
db.close()