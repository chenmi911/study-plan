# 元组不可修改
from itertools import count

t1 = (1, "少羽", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}, 内容是:{t1}")
print(f"t2的类型是：{type(t2)}, 内容是:{t2}")
print(f"t3的类型是：{type(t3)}, 内容是:{t3}")

t4 = ("hello")
print(f"t4的类型是：{type(t4)}, 内容是:{t4}")
# 定义单个元素元组要加逗号

# index()查找
t5 = ("少羽", "浮木", "父母", "nb", "666")
index = t5.index('少羽')
print(f"浮木的下标索引值是：{index}")
# count()
# len()

index = 0
while index < len(t5):
    print(t5[index])
    index += 1

for element in t5:
    print(element)


# 元组里嵌套一个list则可以修改list里的元素
t6 = (1, 2, ["chen", "zhen"])
print(t6)
t6[2][1] = "祯"
print(t6)

