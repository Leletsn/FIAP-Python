#utilizando uma função para alterar o valor da variavel global

x = 0
def alterar(n1):
    # x = n1 #redeclarabdo -> não susbtitui o valor da variavel global
    global = x
    x = n1 # substituindo o valor de x
    print(x)

alterar(10)
print(x)