#Do-while
while True:
    n = int(input("Digite 0 para sair"))

    if n == 0:
        print("Você digitou 0. Saindo do laço")
        break

    print("Você digitou" , n)

print("Fora do laço!")