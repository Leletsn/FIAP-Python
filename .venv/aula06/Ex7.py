idade = int(input("Digite sua idade: "))
cnh = input("Possui CNH? (sim ou não)? ").lower()

if idade < 0:
    print("Idade inválida")
elif idade >= 18 and cnh == "sim":
    print("Pode dirigir")
elif idade >= 18 and cnh == "não":
    print("É maior de idade, mas não possui CNH")
elif idade < 18 and cnh == "sim":
    print("Você não tem idade suficiente para dirigir")
elif idade < 18 and cnh == "não":
    print("Menor de idade, não pode dirigir")
else:
    print("Valor inválido!")
    