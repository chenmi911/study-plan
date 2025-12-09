class Student:
    name = None   # 可省略
    age = None   # 可省略
    tel = None   # 可省略

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

stu = Student("周杰伦", 31, "18296650954")
print(stu.name)
print(type(stu))