# Um pescador, comprou um PC para controlar o rendimento diário
# de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do MS (50 Kg) deve pagar
# uma multa de R$ 4,00 por quilo excedente. O pescador precisa que
# você crie uma função para ler a quantidade de peixes e calcular o
# excesso. Gravar na variável excesso a quantidade de quilos além do
# limite e na variável multa o valor da multa que o pescador deverá
# pagar. Imprima os dados do programa com as mensagens adequadas.

def peixe():
    multa = excesso + 4
    excesso = quant -50
    if quant > 50:
        print("Excesso, Multa de R$",multa)
    else:
        print("Dentro do regulamento")


quant = float(input("Digite peso total pescado: "))

print(peixe)