frase = input("Introduza uma frase: ")
palavras = frase.split()
contagem_palavras = {}
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)