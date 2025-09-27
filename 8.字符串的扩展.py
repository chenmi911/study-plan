# 字符串内包含单引号
name = "'chenzhen'"
print(name)
# 使用转义字符\解除引号效用
name = "\"chenzhen\""
print(name)

print("我是", "chenzhen")
# 字符串字面量和字符串变量得到拼接
name = "chenzhen"
adress = "library"
print("我叫：" + name + ", 现在在：" + adress)
tel = 10086
change = str(tel) # 整数和浮点数要转类型
print("我叫：" + name + ", 现在在：" + adress + ",我的电话是：" + change)

# 字符串格式化
name = 122
message = "我是 %s" % name # %表示占位，s表示将变量变成字符串放入占位地方
print(message)

class_num = 57
avg_slaray = 15555
message = "python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_slaray)
print(message)

print(f"我是{class_num}, j{avg_slaray} ")
# %d 将内容转化成整数    %f将内容转化成浮点数
name = "chenzhen"
set_up = 1996.88
stock_price = 1500.5
message = "my name is %s, born in %d, and %f " % (name, set_up, stock_price)
print(message)

num1 = 11
num2 = 11.345
print("数字11限制宽度9， 小数精确到2， 结果是：%9.2f" % num1)
print("数字11.345限制宽度9， 小数精确到2， 结果是：%9.2f" % num2)
# %关心精度，要注意类型。f{}不关心精度，不理会类型

