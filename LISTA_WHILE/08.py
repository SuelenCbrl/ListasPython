#Escreva um programa que leia 10 inteiros positivos, 
#ignorando não positivos, e imprima sua média.
cont = 0 #AUXILIAR -> OBJETIVO
soma = 0

while cont < 10:
    num = int(input("Digite um numero:"))
    if num >0:
        print("caiu no IF")
        soma = soma + num 
        cont = cont + 1
    else:
        print("valor do cont: ",cont)
        print("valor da soma: ",soma)
        continue

media = soma / cont
print("MEDIA: ",media)