# 新增元素    语法：字典[key] = value
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
my_dict1["陈祯"] = 100   # 如果key重复，则会更新value值
print(f"新增元素后结果是：{my_dict1}")

# 元素删除   字典.pop(key)
score = my_dict1.pop("王力宏")   # 可以删除元素，也可以得到删除的元素
print(f"删除后结果为{my_dict1}, 王力宏的分数是：{score}")

# 清空元素  clear
my_dict1.clear()
print(f"清空后结果是：{my_dict1}")

# 获取全部key方法
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
keys = my_dict1.keys()
print(f"字典所有keys为：{keys}")

# 遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict1[key]}")

# 统计字典元素数量
num = len(my_dict1)
print(f"元素数量是：{num}")



# practice
info_dict = {"王力宏": {"部门": "科技部", "工资": 3000, "级别": 1},
             "周杰伦": {"部门": "市场部", "工资": 5000, "级别": 2},
             "林俊杰": {"部门": "市场部", "工资": 7000, "级别": 3},
             "张学友": {"部门": "科技部", "工资": 4000, "级别": 1},
             "刘德华": {"部门": "市场部", "工资": 6000, "级别": 2}}

for name in info_dict:
    if info_dict[name]["级别"] == 1:
        employee_info_dict = info_dict[name]
        employee_info_dict["级别"] = 2
        employee_info_dict["工资"] += 1000
        info_dict[name] = employee_info_dict

print(f"对员工升职加薪后结果是：{info_dict}")


