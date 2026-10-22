
pokemons = ['Pikachu', 'Mew', 'Abra', 'Charmander', 'Rayquaza', 'Dragonite', 'Lucario']

#append(valor): adicionar itens da lista
pokemons.append("Mewtwo")
pokemons.append("Articuno")
pokemons.append("Zapdos")
pokemons.append("Moltres")
pokemons.append("Ho-oh")

print(pokemons, len(pokemons))

#insert(indice, valor): adicionar um item através de uma posição
pokemons.insert(1, 'Gengar')
print(pokemons, len(pokemons))

#extend([valor, valor, valor]): adicionar multiplos itens
pokemons.extend(['Eevee', 'Igglypuff', 'Dratini'])

#pop(index): remover item da lista
pokemons.pop(3)
print(pokemons)

#reverse: inverte a ordem original
pokemons.reverse()
print(pokemons)

#sort: Ordenar valores de uma lista no modo crescente(A-Z, 0-n, etc)
pokemons.sort()
print(pokemons)

#remove(valor): remover um  item da lista por base do valor
pokemons.remove("Zapdos")
print(pokemons)

#del(index): remover item da lista por base do index
del pokemons[1]
print(pokemons)

#del(index): remover item da lista por base do intervalo de index
del pokemons[1:3] #1 até o 3
print(pokemons)

#clear(): limpar a lista toda
pokemons.clear()
print(pokemons)
