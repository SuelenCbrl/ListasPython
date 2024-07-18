#Elabore um programa que faça leitura de vários números inteiros,
#até que se digite um número negativo. O programa tem que 
#retornar o maior e o menor número lido.


num = int(input("Digite um numero: "))
cont =num
maior =0
menor = 9999999999999999999
while cont >=1:
    f = int(input("Digite um  numero: "))
    if f > maior:
        maior = f
    if f < menor:
        menor = f
    cont -=1
