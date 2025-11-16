# 将元素依次取出进行处理的行为
def list_func():
    index = 0
    list = ["少羽", "浮木", "父母", "nb", "666"]

    while index < len(list):
        print(list[index])
        index += 1

list_func()

def list_func():
    list = ["少羽", "浮木", "父母", "nb", "666"]
    for element in list:
        print(element)

list_func()