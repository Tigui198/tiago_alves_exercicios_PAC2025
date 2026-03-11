soma = 0
count = 0
while count < 30:
    num = int(input("Digite um número par entre 1 e 50: "))
    if 1 <= num <= 50 and num % 2 == 0:
        soma += num
        count += 1
    else:
        print("Número inválido. Tente novamente.")

media = soma / 30
print(f"Média: {media}")