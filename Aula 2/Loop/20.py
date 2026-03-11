def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def conta_divisores(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def eh_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n

num = int(input("Número entre 1 e 30000: "))
if 1 <= num <= 30000:
    for i in range(num, 0, -1):
        print(f"\nNúmero: {i}")
        print(f"Primo: {'Sim' if eh_primo(i) else 'Não'}")
        print(f"Divisores: {conta_divisores(i)}")
        print(f"Perfeito: {'Sim' if eh_perfeito(i) else 'Não'}")
        if (num - i + 1) % 10 == 0 and i != 1:
            input("Prima Enter para continuar...")
else:
    print("Número fora do intervalo.")