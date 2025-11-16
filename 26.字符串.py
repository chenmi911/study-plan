list = "itheima and itcast"
value = list[2]
value1 = list[-8]
print(value)
print(value1)

# 字符串不可修改

# index方法
value2 = list.index("and")
print(f"在字符串{list}中查找and，其起始下标是{value2}")

# 字符串的替换   列表.replace(, )
new_list = list.replace("it", "程序")
print(new_list)

# 列表.split(" ")
list = "itheima and itcast"
new_list = list.split(" ")
print(f"将字符串{list}进行split切分后得到：{new_list}，类型是{type(new_list)})")

# strip方法
my_str = "  itcast and itheima  "
new_my_str = my_str.strip()  #不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后结果是：{new_my_str}")

my_str = "12itcast and itheima21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip后结果是：{new_my_str}")

# 统计字符串中某字符串出现的次数
count = my_str.count("it")
print(f"it出现次数{count}")

# 长度
num = len(my_str)
print(num)


# 字符串的遍历
index = 0
my_str = "12itcast and itheima21"
while index < len(my_str):
    print(my_str[index])
    index += 1

for element in my_str:
    print(element)


