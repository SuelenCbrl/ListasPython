mes = float(input("Digite o consumo mensal: "))
radiação_solar = float(input("Digite media de radiação solar: "))
potencia = float(input("Digite a potencia do painel solar: "))

diario = mes / 30

prod_dia_nesc = diario * 1000

quant = prod_dia_nesc / potencia

print("Quantidade de placas necessarias: ",quant)