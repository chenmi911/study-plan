from typing import Union
my_list: list[Union[str, int]] = [1, 2, "heima"]

def func(data: Union[int, str] ) -> Union[int, str]:
    pass


# 多态
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing_l_r(self):
        print("美的左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing_l_r(self):
        print("格力左右摆风")

def make(ac: AC):
    ac.cool_wind()
    ac.hot_wind()
    ac.swing_l_r()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make(midea_ac)
make(gree_ac)

