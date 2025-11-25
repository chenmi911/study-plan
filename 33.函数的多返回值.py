def return_num():
    return 1
    return 2

result = return_num()
print(result)

# 多返回值
def test_return():
    return 1, "hello", True

x, y, z = test_return()
print(x)
print(y)
print(z)