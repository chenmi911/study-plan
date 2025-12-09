# __函数只能在内部使用，无法在类对象使用

class Phone:

    __current_voltage = 1

    def __keep_single_core(self):
        print("让CPU以单核运转")

    def call_by_5G(self):
        if self.__current_voltage <= 1:
            print("5G通话开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话，已设置单核进行省电")

phone = Phone()
phone.call_by_5G()
