#Escreva um algoritmo que leia um vetor com 10 posições 
#de números inteiros. Em seguida receba um novo valor 
#do usuário e verifique se este valor se encontra no vetor.

numeros =[1,11,111,1111,11111,2,22,222,2222,22222]
digitado = int(input("Digite um numero: "))
cont = 0
while cont < len(numeros):
    if numeros[cont] == digitado:
        print("Esta na lista")
    cont +=1
    