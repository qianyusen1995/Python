import sqlite3
# 连接到SQLite数据库
conn = sqlite3.connect('student.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into Mstudent (id, name,age,xuehao,banji) values ("1", "zhangsan1","20","180901","1809")')
conn.commit()
# 数据列表
data = [("2", "zhangsan2", "20", "180902", "1809"),
        ("3", "zhangsan3", "20", "180903", "1809"),
        ("4", "zhangsan4", "20", "180904", "1809"),
        ]

try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into Mstudent(id, name, age, xuehao,banji) values (?,?,?,?,?)", data)
    # 提交数据
    conn.commit()
except:
    # 发生错误回滚
    conn.rollback()

# 关闭游标
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection
conn.close()