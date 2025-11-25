# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码

# 以r模式打开文件，如果文件不存在则以w模式打开
try: # 此方法也可捕获所有异常
    f = open("D:/windows.txt", "r", encoding="utf-8")
except:
    f = open("D:/windows.txt", "w", encoding="utf-8")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现变量未定义的异常")
    print(f"e表示异常信息{e}")

# 捕获多个异常
try:
    1 / 0
    # print(name)
except (ZeroDivisionError, NameError) as e:
    print("出现了变量未定义或除以0的异常")

# 捕获所有异常
# try:
#
# except Exception as e:

try:
    print("hello")

except Exception as e:
    print("异常")
else:
    print("没有异常") # 没有异常时执行的代码
finally:
    print("finally表示无论有无异常均会运行")
