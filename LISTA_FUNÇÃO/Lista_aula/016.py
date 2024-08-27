# Crie uma função que receba múltiplos argumentos não nomeados, considere que
# a função receba números flutuantes como argumentos e retorne a média dos
# argumentos.
def media(*args):
    media = sum(args) /len(args)
    return media


x = media(12,12,13,14,9)
print(x)