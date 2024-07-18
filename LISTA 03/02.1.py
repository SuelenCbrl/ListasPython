                    #outro jeito de fazer a lista##

cidades = ["Petra", "Ilha Santorini", "Marrocos","Singapura","Seoul"]
num_letras = {}
#contando cada letra da cidade
for cidades in cidades:
    num_letras[cidades] = len(cidades)

cidades_ordem = sorted(num_letras, key=num_letras.get, reverse = True)

for cidade in cidades_ordem:
        print(cidade)