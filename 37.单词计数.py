f = open("D:/word.txt", "r", encoding = "utf-8")
# content = f.read()
# count = content.count("itheima")
# print(f"itheima在文件出现次数:{count}")

count = 0
for line in f:
    line = line.strip()
    words = line.split(" ")
    print(words)
    for word in words:
        if word == "itheima":
            count += 1

print(f"itheiam有{count}个")





f.close()