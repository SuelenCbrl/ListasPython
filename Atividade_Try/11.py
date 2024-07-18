try:
    num = int(input("Digite um Numero: "))
    ant = num - 1
    suc = num + 1
    ts = suc * 3
    da = ant * 2 
    soma = ts + da

    print("A soma é; ",soma)
except:
    print("Entrada inválida!")