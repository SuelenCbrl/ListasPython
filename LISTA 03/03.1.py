nomes = []

for i in range(10):
    nome = input("nome{}: ".format(i +1))
    nomes.append(nome)

print("Nome da Cidades")
for nome in nomes:
    print(nome)