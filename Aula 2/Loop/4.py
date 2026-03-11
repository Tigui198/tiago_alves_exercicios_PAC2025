num = int(input("Digite um número inteiro: "))

if num < 2:
    print("Não é primo")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")