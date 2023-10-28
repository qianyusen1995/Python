import sqlite3
# 连接到SQLite数据库
conn = sqlite3.connect('student.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('select * from  Mstudent')
#fetchone方法
result1=cursor.fetchone()
print("result1=",result1)
#fetchmany
cursor.execute('select * from  Mstudent')
result2=cursor.fetchmany(3)
print("result2=",result2)
#fetchall
cursor.execute('select * from  Mstudent')
result3=cursor.fetchall()
print("result3",result3)
# 关闭游标
cursor.close()
# 关闭Connection
conn.close()