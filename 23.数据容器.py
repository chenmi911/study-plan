# 列表元素类型无限制
name_list = ["少羽", "浮木", "父母", "nb", "666"]
list = [[1, 2, 3], [4, 5, 6]]
print(name_list)
print(type(name_list))
print(list)
print(type(list))


#列表的下标索引       列表[下标索引]

# 从左往右是0开始，从右往左是-1开始
name_list = ["少羽", "浮木", "父母", "nb", "666"]
print(name_list[0])
print(name_list[-1])

list = [[1, 2, 3], [4, 5, 6]]
print(list[0][1])

# 列表查询     列表.index
name_list = ["少羽", "浮木", "父母", "nb", "666"]
list1 = name_list.index("nb")
print(f"nb在列表中的下标索引值是{list1}")

# 修改下标索引值    列表[] = 值
name_list[3] = "牛逼"
print(name_list)

# 元素插入    列表.insert(下标, 元素)
name_list = ["少羽", "浮木", "父母", "nb", "666"]
name_list.insert(1, "家人")
print(name_list)

# 插入元素   列表.append()
name_list = ["少羽", "浮木", "父母", "nb", "666"]
name_list.append(6)
name_list.append(["向", "日", "葵"])
print(name_list)

# 追加元素   列表.extend
name_list = ["少羽", "浮木", "父母", "nb", "666"]
name_list.extend(["向", "日", "葵"])
print(name_list)

# 元素删除
    # 方法1 del 列表[]
name_list = ["少羽", "浮木", "父母", "nb", "666"]
del name_list[2]
print(name_list)
    # 方法2 列表.pop(下标)
name_list = ["少羽", "浮木", "父母", "nb", "666"]
name_list.pop(1)
print(name_list)

# 删除某元素在列表中的第一个匹配项   列表.remove(元素)
name_list = ["少羽", "浮木", "少羽", "父母", "浮木" , "nb", "666"]
name_list.remove("少羽")
print(name_list)

# 清空列表    列表.clear()
# 统计列表某元素的数量  列表.count(元素)
name_list = ["少羽", "浮木", "少羽", "父母", "浮木" , "nb", "666"]
count = name_list.count("666")
print(count)

# 统计列表全部元素数量   len(列表)
num = len(name_list)
print(num)