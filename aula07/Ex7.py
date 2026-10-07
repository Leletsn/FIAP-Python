contador =0

while contador <=10:

    contador += 1
    # contador += 1 Antes do break não exibe o 5
    if contador == 5:
        print("Pulei o número 5!")
        continue # força o laço a realizar a verificação da condição (ou pular um loop)
    print(contador)
    #contador = contador + 1

print("Fora do laço!")