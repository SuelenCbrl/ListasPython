num1 = float(input("Digite um numero: "))
oper = input("Digite a operação: ")
num2 = float(input("Digite outro numero:"))

if oper == '+':
    resultado = num1 + num2
elif oper == '-':
    resultado = num1 - num2
elif oper == '*':
    resultado = num1 * num2
elif oper == '/':
    resultado = num1 / num2

print("Resultado: ",resultado)
