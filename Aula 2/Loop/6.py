def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

count = 0
num = 2
while count < 10:
    if eh_primo(num):
        print(num, end=" ")
        count += 1
    num += 1