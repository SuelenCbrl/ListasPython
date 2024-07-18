ult_dig = int(input("Digite o ultimo digito da placa:"))
if ult_dig == 0 or ult_dig == 1:
    mensagem = "Não circular segunda-feira!"
elif ult_dig == 2 or ult_dig == 3:
    mensagem = "Não circular terça-feira!"
elif ult_dig == 4 or ult_dig ==5:
    mensagem = "Não circular quarta-feira!"
elif ult_dig == 6 or ult_dig == 7:
    mensagem = "Não circular quinta-feira!"
elif ult_dig == 8 or ult_dig == 9:
    mensagem = "Não circular sexta-feira!"
else:
    mensagem = "Erro"
print(mensagem)


