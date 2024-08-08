def calculate_tax(value, **kwargs):
    total = 0
    print(kwargs)
    if 'iss' in kwargs:
        total += value * kwargs['iss']
    if 'pis' in kwargs:
        total += value * kwargs['pis']
    return total

print(calculate_tax)