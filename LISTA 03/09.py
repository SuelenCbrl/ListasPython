num_ant = float('inf')

print("Digite o numero em ordem decrescente: ")
while True:
    numero = float(input("Digite um numero: "))
    if numero > num_ant:
        break
    num_ant = numero
print("FIM DO PROGRAMA")