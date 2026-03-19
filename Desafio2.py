janela = "aberta"
luz = "desligada"
arcondicionado = "desligado"
while True:
    resposta = input(f"Segue estados de sua casa: \n Janela: {janela} \n Luz: {luz} \n ar-condicionado: {arcondicionado} \n _______________________ \n Ações disponíveis: \n ligar luz \n desligar luz \n ligar arcondicionado \n desligar arcondicionado \n abrir a janela \n fechar a janela \n sair \n Resposta: ")

    if resposta == "ligar luz":
        luz = "ligada"
    elif resposta == "desligar luz":
        luz = "desligada"

    if resposta == "abrir a janela":
        janela = "aberta"
    elif resposta == "fechar a janela":
        janela = "fechada"

    if resposta == "ligar arcondicionado" and janela == "aberta":
        print("Não é possível ligar ar-condicionado com a janela aberta")
    elif resposta == "ligar arcondicionado" and janela == "fechada":
        arcondicionado = "ligado"
    if resposta == "desligar arcondicionado":
        arcondicionado = "desligado"
    if janela == "aberta":
        print("Ar condicionado não pode ficar ligado com a janela aberta")
        arcondicionado = "desligado"



    if resposta == "sair":
        print("Tudo se desliga")
        break