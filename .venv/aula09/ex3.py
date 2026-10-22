
# Criando uma lista
veiculos = ['Gol', 'Kwid', 'HB20', 'UP', 'Mobi']

# Acessar os elementos da lista
# Acesso Rápido: lista[indice]
# Toda lista o seu indice inicia com 0

#Recuperar e Alterar valores
print(veiculos[0])

print(veiculos[3])

# Alterando um elemento da lista
veiculos[1] = 'BYD'
print(veiculos[1])

# Exibindo todos os elementos da klista
print(veiculos)

# Trocando valores
veiculos1 = veiculos[1]
veiculos2 = veiculos[2]

veiculos[1] = veiculos2
veiculos[2] = veiculos1

print(veiculos)


#Acesso posicional
#For-each
#for item in nome_lista:
print("Percorrendo uma lista com for-each: ")
i=0 #index

#item é uma variavel local, criada para receber 1 valor da lista a cada loop
for item in veiculos:
    print(f"{i} : {item}")
    i+=1

print("Tamanho da lista é:", len(veiculos))

# OU
#For
#for i in range(len(lista))
print("Percorrendo uma lista com for ")
# for necessita da variavel i para percorrer na lista
for i in range(len(veiculos)):
    print(f"{i} : {veiculos[i]}")
    #i: index

#While i < len(lista)
print("Percorrendo uma lista com while ")
i = 0
while i < len(veiculos):
    print(f"{i} : {veiculos[i]}")
    i += 1
