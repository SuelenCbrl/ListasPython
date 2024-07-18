produto = float(input("Digite o valor: R$"))
desconto = produto * 0.10
Total_Desconto = produto - desconto
Parcela = produto / 3
Comissao1 = Total_Desconto * 0.05
Comissao2 = produto * 0.05

print(f"\n Total a Pagar com desconto:R$",Total_Desconto,"\n Valor da Parcela em 3 vezes:R$",Parcela,"\n Valor Da Comissao venda a vista:R$",Comissao1,"\n Valor da Comissao venda parcelado: R$",Comissao2)