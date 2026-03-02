tipo = input("Digite o tipo (compra/venda): ")
valor = float(input("Digite o valor: "))

pedido = {"tipo": tipo, "valor": valor}

match pedido["tipo"]:
    case "compra":
        print(f"Compra de {pedido['valor']}€")
    case "venda":
        print(f"Venda de {pedido['valor']}€")
    case _:
        print("Pedido desconhecido")