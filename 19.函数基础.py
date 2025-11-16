def check():
    print(f"欢迎来到黑马\n请出示健康码")

check()

def add(a, b):
    result = a + b
    print(f"a + b = {result}")

add(1, 2)


import random
num = random.randint(0, 40)

def check():
    print(f"欢迎来到黑马")
    if num > 37.3:
        print(f"您的体温为{num}，需要隔离")
    else:
        print(f"您的体温为{num}，请进")


check()