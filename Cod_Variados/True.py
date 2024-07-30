idade =float(input("Digite sua idade: "))
teste_psicotecnico =(input("Digite se foi aprovado: "))
prova_teorica = float(input("Digite nota da prova: "))

if (idade >= 18):
    print("Tem idade oara tirar CNH")
    if teste_psicotecnico == "APROVADO" and prova_teorica >= 7:
        print("Esta apto para fazer as aulas práticas!")
    elif teste_psicotecnico == "REPROVADO" or prova_teorica < 7.0:
        print("Não está apto para fazer as aulas práticas!")
else:
    print("Não tem idade para tirar CNH!")        
