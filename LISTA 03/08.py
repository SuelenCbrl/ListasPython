vetor_int = [0] *10
segn_vetor = []

print("Digite 10 números inteiros: ")
for i in range(10):
    numero = int(input("Numero{}: ".format(i+1)))
    vetor_int[i] = numero
    segn_vetor.append(numero * 5)

    print("Vetor de Inteiros: ",vetor_int)
    print("Segundo Vetor (multiplicando por 5): ",segn_vetor)