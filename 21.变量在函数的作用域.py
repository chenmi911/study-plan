num = 100

def test_a():
    print(f"test_a{num}")

def test_b():
    global num
    num = 200
    print(f"test_b{num}")

test_a()
test_b()
print(num)