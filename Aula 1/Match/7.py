nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print(f"Média: {media:.1f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")