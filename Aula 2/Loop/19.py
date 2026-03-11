a, b = 1, 1
count = 0
while count < 60:
    print(a, end=" ")
    a, b = b, a + b
    count += 1