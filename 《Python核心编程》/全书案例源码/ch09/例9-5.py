import sqlite3
# 连接到SQLite数据库
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('student.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 创建Mstudent表:
cursor.execute('create table Mstudent (id int(10)  primary key, name varchar(50),age varchar(50),xuehao varchar(50),banji varchar(50))')
# 关闭游标
cursor.close()
# 关闭Connection
conn.close()