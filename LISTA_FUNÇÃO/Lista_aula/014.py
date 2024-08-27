# Crie uma função que receba como argumento a potência elétrica de determinado
# aparelho e o tempo ligado e retorne o consumo em KWh em seguida chame
# outra função para calcular a conta de energia, levando em consideração o 
# consumo e o valor do KWh como argumentos.

def pt(pot,temp):
    con = pot * temp /1000
    return con

def conta(con):
    pt(con)
    conta = con * 0.53
    return conta

p = int(input("Digite potencia: "))
t = int(input("Digite potencia: "))

print(conta(p,t))