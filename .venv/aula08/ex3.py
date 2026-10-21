# Função com variavel global, sendo redeclarada dentro da função
def alterar(n1):
    n1 = n1 +1
    print("Dentro da função: "), n1

# n1 é a variavel global
n1 = 10

altera(n1)

print("Fora da função: "), n1)