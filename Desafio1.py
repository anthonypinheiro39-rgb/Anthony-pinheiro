print("Seja bem vindo, insira seu cartão para passar pela catraca, empurre a catraca ou desista")

estado_catraca = "fechada"

while True:
    acao = input("Digite 'inserir', 'empurrar' ou 'desistir': ").lower()

    if acao == "inserir":
        if estado_catraca == "fechada":
            print("Cartão inserido, a catraca está agora aberta.")
            estado_catraca = "aberta"
        else:
            print("A catraca está aberta, você pode passar.")

    elif acao == "empurrar":
        if estado_catraca == "aberta":
            print("Você passou pela catraca, a catraca fechou")
            estado_catraca = "fechada"
        else:
            print("A catraca está fechada, insira o cartão para abrir")

    elif acao == "desistir":
        print("Você desistiu de passar pela catraca.")
        break

    else:
        print("Ação inválida. Por favor, tente novamente.")
