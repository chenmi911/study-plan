# f = open("D:/test.txt", "w", encoding="utf-8")
# f.write("hello world")   # 此时内容还在内存中
# f.flush()    # 刷新将内存中积攒的内容写入硬盘
# f.close()    # close()内置了flush功能
f = open("D:/text.txt", "w", encoding="utf-8")
f.write("shaoyu")
f.close()
# w模式文件存在会将内容清空再写，不存在会创建新文件