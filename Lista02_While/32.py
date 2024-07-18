cont =0
num = int(input("Digite um numero: "))
maior = num 
menor = num 
while cont <4:
    if num > maior:
        maior = num
    if num < menor:
        menor = num 
    cont =+ 1
    num = int(input("Digite um numero: "))
print("Maior", maior)
print("Menor",menor)