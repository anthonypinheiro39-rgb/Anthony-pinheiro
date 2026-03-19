senha = "123"
acesso = False

while acesso == False:
    login = input("\nColoque sua Senha:\n")

    if login != senha:
        print("\nAcesso Negado")

    elif login == senha:
        print("\nAcesso Permitido")
        acesso = True
