"""
if int(input("你的身高：")) > 120:
    print("身高超过限制，需要购票")
    print("如果你的vip等级大于3，则可以免费")

    if int(input("请告诉我你的VIP等级")) > 3:
        print("恭喜你，VIP达标，可以免费")
    else:
        print("都不达标，请购票")
else:
    print("欢迎小朋友来游玩")
"""
"""
age = int(input("请输入你的年龄"))
years = int(input("请输入你的工作年龄"))
level = int(input("请输入你的等级"))

if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if years > 2:
            print("你的入职时间达标了,可以领取礼物了")
        elif level > 3:
            print("你的等级达标了，也可以领取礼物")
        else:
            print("未达到两个标准")
    else:
        print("年龄太大了")
else:
    print("你tm还是未成年？")
"""

age = int(input("请输入你的年龄"))
years = int(input("请输入你的工作年龄"))
level = int(input("请输入你的等级"))

if age >= 18 and age < 30:
    if years > 2 or level > 3:
        print("你可以领取奖励")
    else:
        print("你不能领取奖励")
        print("原因：你的工龄和等级都不达标")
else:
    print("抱歉，你不能领取奖励")
    print("原因：你的年龄不在18——30")
