pao =  int(input("Digite quantidade de pães vendidos: "))
broa = int(input("Digite a quantidade de Broa vendidos: "))
dia_pao = pao * 0.12
dia_broa = broa * 1.50
total_dia = pao + broa
poupanca = total_dia * 0.10
print(f"\n Total de vendas Broas e Paes:R${total_dia}\n Valor da poupança:R${poupanca}")