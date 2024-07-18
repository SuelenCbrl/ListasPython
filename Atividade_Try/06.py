terminou = False
p = i = 0
while (not terminou):
    try:
        n = int(input("Digite um número, ou zero para terminar: "))
        if n == 0:
            terminou = True
        else: 
            if n % 2 == 0:
                p = p + 1
            else:
                i = i +1
    except:
        print('INVALIDO!')
print("P = ",p)
print("I = ", i)