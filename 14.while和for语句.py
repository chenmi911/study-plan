# 打印数字1到5
"""
count = 1
while count <= 5:
    print(count)
    count += 1  # 重要：更新计数器，否则会无限循环
"""
"""
import random
num = random.randint(1, 2)
count = 0

flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字"))
    if guess_num == num:
        print("猜对了")
        flag = False
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")
    count += 1

print(f"猜了{count}次")
"""
# print("hello,", end='')
# print("world", end='')
print("hello\tworld")
print("chen\tzhen")
# \t代表对齐
"""
变量 = "whatever"
for x in 变量:
    print(x)

# (num1, num2, step)
# 不包括
for x in range(10):
    print("我是帅哥")


count = 0
for x in range(100):
    print(x)
    if x % 2 == 0:
        count += 1
print(f"总共有{count}个偶数")

for x in range(5, 0, -1):
    print(x)
print("fire")
"""
# count = 5
# while count >= 1:
#     print(count)
#     count -= 1
# print("fire")
i = 5
j =1
while j<= 10:
    print(f"{i} * {j} = {i * j}")
    j += 1
