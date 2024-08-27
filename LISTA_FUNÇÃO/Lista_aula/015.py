# Crie uma função que receba múltiplos argumentos não nomeados, considere
# que a função receba números inteiros como argumentos e retorne a soma 
# dos argumentos.


def soma_args(*args):
   return sum(args)

x = soma_args(12,12,4,33,54,64)
print(x)