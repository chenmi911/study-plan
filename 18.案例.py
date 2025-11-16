import random

money = 10000
for i in range(1, 61):
    num = random.randint(1, 10)
    if num > 5:
        money -= 1000
        print(f"员工{i}的绩效分是{num}， 发放1000元， 账户余额还有{money}")
    if num < 5:
        print(f"员工{i}的绩效分不够，无法领取工资")
        continue
    if money == 0:
        break

