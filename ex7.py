idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH? (sim ou nao): ")

if idade>=18 and cnh=="sim":
    print("Você é permitido dirigir")
elif idade>=18 and cnh=="não" :
    print("Você tem o direito em solicitar a CNH, mas não pode dirigir")
else:
    print("Você não tem idade para dirigir ")


if idade>=18:
    if cnh=="sim":
        print("Você é permitido dirigir")
    else:
        print("Você em o direito em solicitar a CNH, mas não pode dirigir")
else:
    print("Você não em idade para dirigir")
