op = input("Operação (soma/subtrai/multiplica/divide): ").lower()
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

match op:
    case "soma":
        print(f"Resultado: {n1 + n2}")
    case "subtrai":
        print(f"Resultado: {n1 - n2}")
    case "multiplica":
        print(f"Resultado: {n1 * n2}")
    case "divide":
        if n2 != 0:
            print(f"Resultado: {n1 / n2}")
        else:
            print("Erro: divisão por zero")
    case _:
        print("Operação inválida")