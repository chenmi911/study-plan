from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='mysql820830',
    autocommit=True
)
cursor = conn.cursor()
conn.select_db("py_sql")
cursor.execute("select * from orders")
data_list = cursor.fetchall()
print(data_list)
conn.close()

