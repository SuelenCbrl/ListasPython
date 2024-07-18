nome = (input("Digite o Produto: "))
codigo = int(input("Digite o cod do produto: "))
q = int(input("Digite a quantidade de produto: "))
ent = int(input("Digite a quantidade de entrada do produto: "))
estoque = q + ent
print("Produto e quantidade do estoque: ",nome,"Código: ",codigo,"quantidade atualizada: ",estoque)

prod1 = (input("Digite o Produto vendido: "))
ProdC= int(input("Digite o cod do produto vendido: "))
v = int(input("Digite a quantidade de produto vendido: "))
Qp = estoque
estoque = Qp - v

if estoque<=7:
    print("Quantidade no estoque atualizado: ",estoque,"Por favor compre mais produtos.")
else:
    print("Quantidade do estoque atualizado: ",estoque)
