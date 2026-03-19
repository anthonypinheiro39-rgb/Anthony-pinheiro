alunos = []

modo = input("\nCadastrar outro aluno?\n1- Cadastrar Aluno\n2- Lista de Alunos\n")

while True:
    
    if modo == "1":
        print("-------------------\n Cadastro de Aluno\n-------------------")

        nome = input("Digite seu Nome: ")
        idade = int(input("Digite sua Idade: "))
        notas = []
        for i in range(3):
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)

        aluno = {
            "nome": nome,
            "idade": idade,
            "notas": notas
        }

        alunos.append(aluno)

    
    elif modo == "2":
        print("--------------------\n Alunos Cadastrados\n--------------------")
        for aluno in alunos:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            print(f"Aluno: {aluno['nome']} | Média: {media:.2f}")

    else:
        print("Opção Inválida!")

    modo = input("\nCadastrar outro aluno?\n1- Cadastrar Aluno\n2- Lista de Alunos\n")
