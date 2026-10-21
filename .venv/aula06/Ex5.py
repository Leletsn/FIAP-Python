idade = int(input("Digite a idade: "))
cnh = input("Possui CNH? (sim/não): ").lower()

# X é o valor que vamos verificar, nesse caso é a idade
# Foi definido uma variavél genérica para informar um valor possível

match idade:
    case x if x >= 18:
        print("Maior de idade")
    case x if x < 18:
        print("Menor de idade")
    case _:
        print("Valor inválido!")