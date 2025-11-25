# 文件的读取
f = open("D:/for practice.txt", "r", encoding="utf-8")
print(type(f))

# # 读取文件    文件对象.read(字节)
# print(f"读取10字节的结果是：{f.read(10)}")
# # print(f"读取全部字节的结果是：{f.read()}")
# # 会从前面读取的结果继续读取
# print("------------------------------------------")
# # 文件对象.readlines()     数据类型为列表
# # lines = f.readlines()
# # print(f"lines的数据类型是：{type(lines)}")
# # print(f"lines的内容是：{lines}")   # readlines和read不同但来自同一个文件
# # 文件对象.readline()表示读取一行
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")
# print("------------------------------------------")
#
# for b in f:
#     print(b)

# 文件关闭
# time.sleep(50000)
# 文件对象.close()


# with open() as f
with open("D:/for practice.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"每一行的数据是{line}")