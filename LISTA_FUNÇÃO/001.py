def pot (base,exp):
    cont = 1
    while exp >= cont:
        res = base ** exp
        base +=1
        cont +=1
        print(res)
    

pot(2,3)
    
