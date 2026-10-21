senha = input("Digite a senha: ")
usuario = input("Digite o nome do usuario: ")

if senha != "fiap" or usuario !="admin":
    print("Senha OU Usuario incorretos")
else:
    print("Acesso permitido")
#OU

if senha == "fiap" and usuario =="admin":
    print("Acesso permitido")
else:
    print("Senha incorreta")