# Escreva um programa, com uma função que necessite de um argumento. A 
# função retornar o valor de caractere ‘P’, se seu argumento for positivo, 
# e ‘N’, se seu argumento for zero ou negativo.
def idade(idade):
    if idade<= 0:
        return "N"
    elif idade > 0 and idade < 99:
        return "P"

print(idade(18))