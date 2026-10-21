total_economizado = 0
mes = 1

while mes <= 12:
    valor = float(input(f"Digite o valor a ser economizado no mês {mes} R$: "))
    total_economizado += valor
    mes += 1

print("Parabéns! Você economizou R$", total_economizado)

#Contador normalmente é utilizado na condição do loop
# Contador incrementa valores por padrão +1, ou +2

#Acumulador pode ser utilizado na condição do loop
# Não soma valores padronizados