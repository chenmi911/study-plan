# 在子类重新定义同名属性或方法
class Phone:
    producer = "ITCAST"

    def call_by_4g(self):
        print("4g通话")

class Myphone(Phone):
    producer = "HM"

    def call_by_4g(self):
        # 方法1
        # print(f"父类厂商是：{Phone.producer}")
        # Phone.call_by_4g(self)
        # 方法2
        print(f"父类厂商是：{super().producer}")
        super().call_by_4g()
        print("换代升级")

i = Myphone()
i.call_by_4g()
print(i.producer)
