# int(x) 将x转换成整数
# float(x) 将x转换成浮点数
# str(x) 将x转换成字符串
# 将数字转换成字符串
int_str=str(11)
print(type(int_str),int_str)
float_str=str(3.14)
print(type(float_str),float_str)
# 将字符串转换成数字
a=int(666)
print(type(a),a)
b=float(6.66)
print(type(b),b)
# 想要将字符串转换成数字，字符串内容必须是数字
# 整数转浮点数
c=float(66)
print(type(c),c)
# 浮点数转整数
d=int(66.6)
print(type(d),d)