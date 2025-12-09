class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = True

    def call_by_5g(self):
        print("5g通话")

phone = Phone2022()
print(Phone.producer)
phone.call_by_5g()

class NFCReader:
    nfc_type = "5代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class Remote_contral:
    rc_type = "红外遥控"
    def contral(self):
        print("红外遥控开启")


class MYphone(Phone, NFCReader, Remote_contral):
    pass  # 表示占位


print(MYphone.producer)  # 当类里成员属性同名，按谁先继承谁优先