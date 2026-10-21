idade = int(input("Digite sua idade: "))
cnh = input("Possui CNH? (sim ou não)? ").lower()

# i é a idade
# c é a cnh
match idade, cnh:
    case i, c if i >= 18 and c == "sim":
        print("Pode dirigir")
    case i, c if i < 18 and c == "não":
        print("Não pode dirigir")
    case i, c if i >= 18 and c == "não":
        print("É maior de idade, mas não possui CNH")
    case _:
        print("Valor inválido!")


#OU

match idade, cnh:
    case i, _ if i < 0:
        print("Idade inválida")
    case i, "sim" if i >= 18:
        print("Pode dirigir")
    case i, "não" if i >= 18:
        print("É maior de idade, mas não possui CNH")
    case i, _ if i < 18:
        print("Menor de idade, não pode dirigir")
    case i, "sim" if i < 18:
        print("Você não tem idade suficiente para dirigir")
    case _:
        print("Valor inválido!")