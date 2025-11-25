my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
print(f"列表元素个数有：{len(my_list)}")
print(f"元组元素个数有：{len(my_tuple)}")
print(f"字符串元素个数有：{len(my_str)}")
print(f"集合个数有：{len(my_set)}")
print(f"字典元素个数有：{len(my_dict)}")

# max最大元素
print(f"列表 最大的元素是：{max(my_list)}")
print(f"元组 最大的元素是：{max(my_tuple)}")
print(f"字符串最大的元素是：{max(my_str)}")
print(f"集合 最大的元素是：{max(my_set)}")
print(f"字典 最大的元素是：{max(my_dict)}")

# min最小元素
print(f"列表 最小的元素是：{min(my_list)}")
print(f"元组 最小的元素是：{min(my_tuple)}")
print(f"字符串最小的元素是：{min(my_str)}")
print(f"集合 最小的元素是：{min(my_set)}")
print(f"字典 最小的元素是：{min(my_dict)}")

# 容器的通用转换功能
# list()  str()  tuple()  set()

# 容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")
# 容器转元组
print(f"列表 转元组的结果是：{tuple(my_list)}")
print(f"元组 转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合 转元组的结果是：{tuple(my_set)}")
print(f"字典 转元组的结果是：{tuple(my_dict)}")
# 容器转字符串    字典中value可以保留
print(f"列表 转字符串的结果是：{str(my_list)}")
print(f"元组 转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合 转字符串的结果是：{str(my_set)}")
print(f"字典 转字符串的结果是：{str(my_dict)}")
# 容器转集合
print(f"列表 转集合的结果是：{set(my_list)}")
print(f"元组 转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")
print(f"集合 转集合的结果是：{set(my_set)}")
print(f"字典 转集合的结果是：{set(my_dict)}")
# 容器排序
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "abujskg"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 3, "key1": 1, "key2": 2, "key5": 5, "key4": 4}
print(f"列表 对象的排序是；{sorted(my_list)}")
print(f"元组 对象的排序是；{sorted(my_tuple)}")
print(f"字符串对象的排序是；{sorted(my_str)}")
print(f"集合 对象的排序是；{sorted(my_set)}")
print(f"字典 对象的排序是；{sorted(my_dict)}")

print(f"列表 对象反向的排序是；{sorted(my_list, reverse = True)}")
print(f"元组对象反向的排序是；{sorted(my_tuple, reverse = True)}")
print(f"字符串对象反向的排序是；{sorted(my_str, reverse = True)}")
print(f"集合  对象反向的排序是；{sorted(my_set, reverse = True)}")
print(f"字典 对象反向的排序是；{sorted(my_dict, reverse = True)}")



















