# 内容不重复，内容无序，不支持下标索引但可以修改

my_set = {"少羽", "浮木", "双亡", "少羽", "浮木", "双亡", "少羽", "浮木", "双亡"}
my_set.add("nb")
print(f"添加元素后结果是：{my_set}")

# 移除元素
my_set.remove("少羽")
print(f"经过remove移除元素后结果是：{my_set}  ")

# 取出元素  随机取出
element = my_set.pop()
print(f"pop随机抽取元素: {element}")

# 清空集合
my_set.clear()
print(my_set)

# 差集    集合1.difference(集合2)表示取出集合1有而集合2没有的
set1 = {1, 2, 3} # 原集合1和集合2不改变
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set3)

# 消除差集   集合1.difference_update(集合2)表示在集合1内，删除和集合2相同的元素，结果集合1改变，集合2不变
t1 ={1, 2, 3}
t2 = {1, 4, 6}
t1.difference_update(t2)
print(f"t1消除差集之后结果是：{t1}")

# 集合的合并    集合1.union(集合2)
t3 = {1, 2, 3}
t4 = {1, 4, 6}
t5 = t3.union(t4)
print(f"经过集合的合并后，结果是：{t5}")

# 统计
set1 = {1, 2, 3}
set2 = len(set1)
print(f"set1元素个数：{set2}")

# 集合的遍历 不可用while循环，不支持下标索引
set1 = {1, 2, 3, 5, 6}
for element in set1:
    print(f"集合set1有元素：{element}")


# practice
list = ["少羽", "浮木", "少羽", "浮木", "nb", "牛逼", "nb", "牛逼", 666]
my_set = set()
for element in list:
    my_set.add(element)
print(f"list1为：{my_set}")