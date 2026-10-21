opcao =  int(input("Digite uma opção (0 até 3):"))

# A estrutura match-case por padrão compara valores por igualdade
# Em outras linguagens é conhecido como SWITCH-CASE
# No Match informamos a variavél que será verificada, nesse caso é "opção"
# No Match não há limitações para cases, podemos ter N
# Porém, de maneira minima há 1 CASE e 1 CASE DEFAULT (case _:)
match opcao:
    case 0: #opcao == 0
        print("Opção 0")
    case 1: #opcao == 1
        print("Opção 1")
    case 2: #opcao == 2
        print("Opção 2")
    case 3: #opcao == 3
        print("Opção 3")
    case _: #else
        print("Valor incorreto, Digite de 0 até 3")


# OU

if opcao == 0:
    print("Opção 0")
elif opcao == 1:
    print("Opção 1")
elif opcao == 2:
    print("Opção 2")
elif opcao == 3:
    print("Opção 3")
else:
    print("Valor incorreto, Digite de 0 até 3")

