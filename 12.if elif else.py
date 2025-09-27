print("欢迎来到儿童游乐园，儿童免费，成人收费")

if int(input("请输入您的年龄")) >= 18:
    print("您已成年，游玩需买票10元。")
elif int(input("level")) >= 2:
    print("it is ok")
elif int(input("day")) >= 3:
    print("未成年")

# if条件满足，则elif条件不输出
