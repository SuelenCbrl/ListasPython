print("Cardápio:")
print("1. Bife acebolado - R$15,00")
print("2. Lasanha - R$25,00")
print("3. Salada - R$15,00")
print("4. Sopa de Legumes - R$22,00")
print("5. Strogonoff - R$18,00")
print("6. Pizza  - R$30,00")
print("7. Caldo Verde - R$17,00")
print("8. Marmita P - R$22,00")
print("9. Marmita M - R$24,00")
print("10.Marmita G - R$26,00")

escolha = int(input("Escolha o número do prato desejado: "))
if escolha == 1:
    preco = 15.00
elif escolha == 2:
    preco = 25.00
elif escolha == 3:
    preco = 15.00
elif escolha == 4:
    preco = 22.00
elif escolha == 5:
    preco = 18.00
elif escolha == 6:
    preco = 30.00
elif escolha == 7:
    preco = 17.00
elif escolha == 8:
    preco = 22.00
elif escolha == 9:
    preco = 24.00
elif escolha == 10:
    preco = 26.00

gorjeta = int(input("Aceita pagar a gorjeta de 10% ? sim = 1 \\ não = 2 "))

if gorjeta == 1:
    valor_fim = preco * 1.10
else:
    valor_fim = preco
print("Valor FInal: R$",valor_fim)



