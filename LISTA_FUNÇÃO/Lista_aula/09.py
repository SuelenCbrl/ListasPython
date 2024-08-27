# Considere o valor mínimo de R$9,00
# por hora e R$ 1,50 por hora adicional. O principal argumento da
# função é o tempo utilizado em minutos, a função deve retornar o
# valor total. Caso o usuário fique no estacionamento por menos de
# 15 minutos, o tempo utilizado não será cobrado.
# Adicione na função calcularTempo() do sistema para
# estacionamento o valor dos impostos pago pelo cliente. Considere
# o PIS: 0,33% , COFINS: 0,20% e ICMS: 17% no valor e imprima o
# recibo do cliente 

def estaionamento(hora):
    minutos = hora /60
    if minutos >= 15:
        print("Valor do estacionamento R$9,00")
    if hora ==1:
        pis = 9 *0.033
        cofins = 9*0.020
        icms = 9*.017
        print("Valor do estacionamento R$9,00")
        print("PIS:",pis)
        print("Cofins:",cofins)
        print("ICMS: ",icms)

    if hora >1:
        adicional = hora *1.5
        total_adicional= adicional + 9.0
        pis = total_adicional *0.033
        cofins = total_adicional *0.020
        icms = total_adicional * 0.17
        print("Valor do estacionamento R$",total_adicional)
        print("PIS:",pis)
        print("Cofins:",cofins)
        print("ICMS: ",icms)
    else:
        print("Não será cobrado o estacionamento")
    

quant = float(input("Tempo no estacionamento:"))

print(estaionamento(quant))