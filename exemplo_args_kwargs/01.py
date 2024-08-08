##OBBRIGATORIO PASSA 4 ARGS

def soma(x,y,z,t=0):
    soma = x +y+z +t
    return soma
#ARGUMENTO COM VALOR DEFAULT
res = soma(41,42,43)
print(res)

# ARGUMENTOS NAO ESPECIFICADOS #
def soma_args(*args):
   return sum(args)

x = soma_args(12,12,4,33,54,64)
print(x)