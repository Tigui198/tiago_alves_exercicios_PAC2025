saldo = float(input("Digite o saldo inicial: "))
cheque = float(input("Digite o valor do cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print(f"Cheque descontado, saldo: {saldo:.2f}")
else:
    print("Cheque não pode ser descontado, saldo insuficiente!")