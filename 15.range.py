count = 0
for x in range(100):
    print(x)
    if x % 2 == 0:
        count += 1
print(f"总共有{count}个偶数")

for x in range(5, 0, -1):
    print(x)
print("fire")