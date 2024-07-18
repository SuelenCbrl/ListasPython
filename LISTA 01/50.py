import math

x1 = float(input("Digite a coordenada de x do primeiro ponto: "))
x2 = float(input("Digite a coordenada de x do segundo ponto: "))
y1 = float(input("Digite a coordenada de Y do primeiro ponto: "))
y2 = float(input("Digite a coordenada de y do segundo ponto: "))

distancia = math.sqrt((x2 - x1)** 2 + (y2 - y1) ** 2)

if distancia >=10:
    print("Longe")
else: 
    print("Perto")

