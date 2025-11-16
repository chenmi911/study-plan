def add(a, b):
    result = a + b
    return result

# 函数的返回值通过变量接收， result后不执行
r = add(9, 6)
print(r)

# 无return语句的返回值
def say_hello():
    print("hello")

result = say_hello()
print(f"无返回值时内容为{result}")
print(f"无返回值时类型为{type(result)}")

def check_age(age):
    if age > 18:
        return "success"
    else:
        return None

result = check_age(14)
if not result:
    print("你是未成年")