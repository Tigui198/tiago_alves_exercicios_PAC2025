alunos = {}
while True:
    opcao = input("Digite '1' para inserir aluno, '2' para listar, ou '0' para sair: ")
    if opcao == '1':
        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")
        alunos[nome] = {'nome': nome, 'idade': idade, 'curso': curso}
    elif opcao == '2':
        for aluno in alunos.values():
            print(f"nome: {aluno['nome']}")
            print(f"idade: {aluno['idade']}")
            print(f"curso: {aluno['curso']}")
            print()
    elif opcao == '0':
        break