import random
import json
# 变量：类型
var_1: int = 10
var_2: str = "hello"
var_3: bool = True

# 类对象注解
class Phone:
    pass

ph: Phone = Phone()

# 容器注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "itheima", True)
my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}

# 返回值注解
def func(data: list) -> list:
    return data

# type：类型
var_1 = random.randint(1,10)  # type:int
var_2 = json.loads('{"name": "zs"}') # type:dict[str, str]
def func():
    return 10
var_3 = func() # type: int