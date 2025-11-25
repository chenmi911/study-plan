def test_func(compute):
    result = compute(1, 2)
    print(result)

def compute(x, y):
    return x + y

test_func(compute)

# lambda匿名函数   只可临时使用一次
def test_func(computer):
    result = computer(1, 2)
    print(f"结果是{result}")

test_func(lambda x, y: x + y)    # 只能写一行
