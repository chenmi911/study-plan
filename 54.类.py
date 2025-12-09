# class student:
#     name = None
#     age = None
#     gender = None
#
# s1 = student()
# s1.name = ""

# 类内部的函数叫方法

class student:
    name = None
    def say_hi(self):
        print(f"Hello, my name is {self.name}")

    def say_hello(self, msg):
        print(f"Hello, my name is {self.name}，{msg}")


s1 = student()
s1.name = "周杰伦"
s1.say_hello("哎呦，不错哦") # 括号内的传入msg

s2 = student()
s2.name = "林俊杰"
s2.say_hello("小伙子我看好你")


class clock:
    id = None
    price = None


    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock1 = clock()
clock1.id = "6660"
clock1.price = 100
clock1.ring()

