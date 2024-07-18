##Escreva um programa que peça ao usuário para 
##digitar 10 valores e some-os. 
cont = 0
soma = 0
while cont < 10:
    try: 
        num = int(input("Digite um numero: "))
        soma = soma + num
        cont = cont + 1
    except: 
        print("Entrada invalida!")
print("Soma = ",soma)