def verifica_idade(idade):
    if idade<= 0:
        return "TA MALUCO!!! NAO FAZEMOS CALCULOS COM BEBES OU PESSSOAS QUE NÃO NASCERAM"
    elif idade > 0 and idade < 99:
        return True
    else:
        return "TÁ MALUCO!!! O CARA É UMA LENDA"
    
print( verifica_idade(108))