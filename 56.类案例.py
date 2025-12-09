class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

for stu_num in range(1, 11):
    print(f"当前录入第{stu_num}位学生信息，总共需要录入10位学生信息")
    name = input("请输入学生名字")
    age = input("请输入学生年龄")
    adress = input("请输入学生地址")
    stu = Student(name, age, adress)
    print(f"学生{stu_num}信息录入完成，信息为【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.adress}】 ")

