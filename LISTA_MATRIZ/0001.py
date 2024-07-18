mt = []

linhas = 0
colu = 3

i = 0 
a = 1 #
while i< linhas:
    linha =[]
    j = 0
    while j< colu:
        linha.append(a)
        a+= 1
        j+=1
    mt.append(linha)
    i+=1

x = 0
while x < len(mt):
    print(mt[x])
    x+=1