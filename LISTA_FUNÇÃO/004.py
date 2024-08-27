# Faça uma função que receba 3 números inteiros como parâmetro, 
# representando horas, minutos e segundos, e os converta em segundos.

def hora(hora,min,seg):
    conver1 = hora * 3600
    conver2 = min * 60
    seg = seg
    print("Horas em segundos: ",conver1)
    print("Minutos em segundos: ",conver2)
    print("Segundos: ",seg)


print("Converter horas!")
x= int(input("Digite a hora: "))
y= int(input("Digite os minutos: "))
z= int(input("Digite os segudos: "))


convert = hora(x,y,z)
print(hora)
