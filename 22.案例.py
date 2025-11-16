money = 5000000
name = input("请输入您的姓名")

def query(show_header):
    if show_header:
        print("----------查询余额----------")
    print(f"{name}您好，您的余额剩余：{money}元")

def saving(num):
    global money
    money += num
    print("----------存钱----------")
    print(f"您存了{num}元， 余额为{money}元")

    query(False)

def get_money(num):
    global money
    money -= num
    print("----------取钱----------")
    print(f"您取了{num}元， 余额为{money}元")

    query(False)

def main():
    print("----------主菜单----------")
    print(f"请输入您的操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    if keyboard_input == "2":
        num = int(input("您想要存多少"))
        saving(num)
        query(False)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少"))
        get_money(num)
        query(False)
        continue
    else:
        break



