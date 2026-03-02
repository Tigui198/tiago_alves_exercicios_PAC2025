metodo = input("Método (GET/POST): ").upper()
conteudo = input("Conteúdo: ")

requisicao = {"metodo": metodo, "conteudo": conteudo}

match requisicao:
    case {"metodo": "GET"}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("Requisição POST com dados válidos")
    case {"metodo": "POST"}:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")