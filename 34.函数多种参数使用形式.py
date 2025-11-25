# 位置参数
def user_info(name, age, gender):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")

user_info("Tom", 20, "男")

# 关键字参数
# 可以不按顺序
user_info(age = 20, gender = "男", name = "tom")
# 可以和位置参数混合使用
user_info("shaoyu", gender = "男", age = 20)
# 如果有位置参数，位置参数必须在关键字参数之前，但关键字参数不分先后
user_info("shaoyu", gender = "男", age = 20)

# 缺省参数(默认参数)    有传递参数则改为传递参数    设置默认参数必须在最后可以多个默认参数
def user_info(name, age, gender = "女"):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{gender}")

user_info(name = "nancy", age = 8)
user_info(name = "nancy", age = 8, gender = "男")

# 不定长参数(可变参数)
# 不定长的位置传递
def user_info(*args):      # 传入参数被args接受，且合并成元组
    print(f"args的内容是{args}，类型是{type(args)}")

user_info("Tom", 1, 2, "boy")

# 关键字传递   接受“键=值”形式  key-word
def user_info(**kwargs):
    print(f"kwargs的内容是{kwargs}， 类型是{type(kwargs)}")

user_info(name = "Tom", age = 8)