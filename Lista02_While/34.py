#Faça um Programa que leia 20 números inteiros e armazene-os
#em uma LISTA. Armazene os números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores
num = int(input("Digite um numero: "))
cont = 1
while cont <=20:
    if num % 2 == 0:
        print("Par",num)
    cont =-1
    if cont % 2 == 1:
        print("Impar",num)
    cont = cont -1
