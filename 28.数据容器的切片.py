# 切片：从一个序列中，取出一个子序列
# 语法：序列[起始下标：结束下标(不含)：步长]
# 起始和步长不写表示从头到尾，步长为1可以省略


# 对list进行切片
# 对str切片
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r1 = my_list[1:4:1]
print(r1)

# 对tuple切片
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
r2 = my_tuple[::1]
print(r2)

# 对str切片
my_str = "0123456789"
r3 = my_str[::2]
print(r3)


# 对list进行切片
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r4 = my_list[3:1:-1]
print(r4)

# 对tuple切片
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
r5 = my_tuple[::-2]
print(r5)

# 对str切片
my_str = "01234567"
r6 = my_str[::-1]
print(r6)

str = "万过薪月，员序程马黑来，nohtyp学"
# 方法1
r7 = str[-10:-15:-1]
print(r7)

# 方法2
r8 = str[::-1][9:14]
print(r8)

# 方法3
r9 = str[5:10][::-1]
print(r9)

# 方法4
r10 = str.split("，")[1].replace("来", "")[::-1]
print(r10)
