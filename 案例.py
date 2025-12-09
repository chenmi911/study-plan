from file_definite import TextReader, JsonFileReader
from data_definite import Record
from pymysql import Connection

text_file_reader = TextReader("D:/python练习文件/一月.txt")
json_file_reader = JsonFileReader("D:/python练习文件/二月.json")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
all_data = jan_data + feb_data

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="mysql820830",
    autocommit=True
)
cursor = conn.cursor()
conn.select_db("py_sql")

for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province)" \
          f"values('{record.date}','{record.order_id}','{record.money}','{record.province}')"

    cursor.execute(sql)
conn.close()



