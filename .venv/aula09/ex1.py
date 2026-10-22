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
