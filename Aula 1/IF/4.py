valor = eval(input("Digite um valor: "))

match valor:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case str() if valor.isdigit():
        print("String numérica")
    case str():
        print("String textual")
    case list():
        print("Lista")
    case _:
        print("Tipo desconhecido")