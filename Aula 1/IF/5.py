msg = input("Digite uma mensagem: ").lower()

match msg:
    case "olá" | "bom dia":
        print("Saudação")
    case _ if msg.endswith("?"):
        print("Pergunta")
    case _ if "tchau" in msg or "adeus" in msg:
        print("Despedida")
    case _:
        print("Mensagem genérica")