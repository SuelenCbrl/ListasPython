# Elaborar uma função para retornar o maior de três números recebidos 
# por parâmetro.
def maior(num1,num2,num3):
        num =[num1,num2,num3]
        print("O maior numero entre os digitados: ",max(num))
        return num

n1 =int(input("Digite um numero:"))
n2 =int(input("Digite um numero:"))
n3 =int(input("Digite um numero:"))

x = maior(n1,n2,n3)
print(x)