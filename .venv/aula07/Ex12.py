# Gerenciar Aluno
# 1 - Cadastrar
# 2 - Consultar
# 3 - Atualizar
# 4 - Remover
# 5 - Listar Alunos
# 6 - Sair do progama


while True:
    print("GERENCIAR ALUNO")
    print("1 - Cadastrar ")
    print("2 - Consultar ")
    print("3 -  Atualizar ")
    print("4 - Remover ")
    print("5 - Listar ")
    print("6 - Sair ")
    opcao = input("Digite uma opção: ")

    #Função isdigit(): utilizada para verificar se contém apenas números
    if opcao.isdigit():
        opcao = int(opcao)
        match opcao:
            case 1:
                print("Cadastrar Aluno")]
                #nome = input("Digite o nome: ")

            case 2:
                print("Consultar o Aluno")
            case 3:
                print("Atualizar o Aluno")
            case 4:
                print("Remover o Aluno")
            case 5:
                print("Lista os Alunos")
            case 6:
                print("Saindo do Programa")
                break
            case _:
                print("Você digitou uma opção invalida! Tente Novamente")

    else:
        print("Digite apenas numeros. De 0 até 6")