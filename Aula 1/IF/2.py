nota = int(input("Digite uma nota (0-100): "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Bom")
    case n if n >= 50:
        print("Suficiente")
    case _:
        print("Insuficiente")