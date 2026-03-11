num = int(input("Digite um número: "))
operacoes = 0

for i in range(1, num):
    print(f"{num} + {i} = {num + i}")
    operacoes += 1
    print(f"{num} - {i} = {num - i}")
    operacoes += 1
    print(f"{num} * {i} = {num * i}")
    operacoes += 1
    if i != 0:
        print(f"{num} / {i} = {num / i}")
        operacoes += 1

print(f"Total de operações: {operacoes}")