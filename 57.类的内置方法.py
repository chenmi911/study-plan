class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象 name: {self.name}, age: {self.age}"

    # __lt__魔术方法   比较大小，没有等于
    def __lt__(self, other):
        return self.age < other.age

    # __le__   有等于比较大小
    def __le__(self, other):
        return self.age <= other.age

    # __eq__ 比较相等
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("陈祯", 19)
stu2 = Student("周杰伦", 19)
print(stu1 <= stu2)
print(stu1 >= stu2)
print(stu1 == stu2)

print(stu1)



