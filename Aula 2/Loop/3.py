soma = 0
for i in range(10):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    soma += nota

media = soma / 10
print(f"A média das notas é: {media}")