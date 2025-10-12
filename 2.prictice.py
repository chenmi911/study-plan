"""
num = 6

if int(input("请猜一次")) == num:
    print("恭喜猜对了")
elif int(input("猜错了请再来一次")) == num:
    print("恭喜这次猜对了")
elif int(input("最后一次机会了")) == num:
    print("答对了")
else:
    print("dacuol, 其实我想的是 %f" % num)
"""
"""
import random
num = random.randint(1,10)

guess_num = int(input("输入你猜测的数字"))

if num == guess_num:
    print("恭喜你，猜对了")
else:
    if num > guess_num:
        print("你猜的数字小了")
    else:
        print("你猜的数字大了")

    guess_num = int(input("第二次输入你猜测的数字"))

    if num == guess_num:
        print("恭喜第二次成了")
    else:
        if num > guess_num:
            print("你猜的数字小了")
        else:
            print("你猜的数字大了")

        guess_num = int(input("第三次输入你猜测的数字"))

        if num == guess_num:
            print("恭喜第三次成了")
        else:
            print("三次机会用完了")
"""
"""
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(f"从1累加到100的和：{sum}" )
"""
"""
import random
num = random.randint(1,100)
count = 0

flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字"))
    if guess_num == num:
        print("猜对了")
        flag = False
    else:
        if guess_num >num:
            print("大了")
        else:
            print("小了")
    count += 1
            
print(f"猜了{count}次")
"""
i = 1
while i < 100:
    print(f"今天是第{i}天表白")
    i += 1
    j = 1
    while j <= 10:
        print(f"送给她的第{j}只花")
        j += 1
    print("喜欢")

print(f"坚持了{i}天")
