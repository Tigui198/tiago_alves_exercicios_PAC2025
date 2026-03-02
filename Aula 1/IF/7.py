categoria = input("Categoria (eletrônico/alimento): ").lower()
preco = float(input("Preço: "))

produto = {"categoria": categoria, "preco": preco}

match produto:
    case {"categoria": "eletrônico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrônico"}:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")