limite = int(input("Digite um número: "))
for num in range(2, limite + 1):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores == num:
        print(f"{num} é perfeito")