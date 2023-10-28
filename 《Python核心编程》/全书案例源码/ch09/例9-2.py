import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "student")
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 执行sql语句，插入多条数据
cursor.execute('insert into Mstudent(name, banji, age, xuehao) values ("zhangsan","J1802","18","2018030438")')
cursor.execute('insert into Mstudent(name, banji, age, xuehao) values ("zhangsi","J1802","18","2018030439")')
cursor.execute('insert into Mstudent(name, banji, age, xuehao) values ("zhangwu","J1802","18","2018030436")')
# 执行sql语句，删除一条条数据
cursor.execute('delete from  Mstudent where name="zhangsi"')
# 执行sql语句，修改一条条数据
cursor.execute('update Mstudent set age=19 where name="zhangwu"')
# 执行sql语句，查询数据
cursor.execute('select * from  Mstudent')
result1=cursor.fetchone()
print(result1)

# 关闭数据库连接
db.close()