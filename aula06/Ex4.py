dia = input("Digite o dia da semana: ").lower()

#função lower: transformar texto em minúsculo
# OR no Match-Case é o operador | (pipe)
# Não é possível utilizar o operador | (pipe) com if-elif-else, nesse caso é necessário utilizar o operador lógico or

match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sábado" | "domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido!")


if (dia == "segunda" 
    or dia == "terça" 
    or dia == "quarta" 
    or dia == "quinta" 
    or dia == "sexta"):
    print("Dia útil")
elif dia == "sábado" or dia == "domingo":
    print("Fim de semana")
else:
    print("Dia inválido!")