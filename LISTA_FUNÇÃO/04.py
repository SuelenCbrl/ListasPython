def idade(idade):
    if idade<= 0:
        return "N"
    elif idade > 0 and idade < 99:
        return "P"

print(idade(18))