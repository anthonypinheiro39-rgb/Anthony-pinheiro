cadeia = input("Digite uma cadeia binária: ")

estado_atual = "q0"

valida = True

for simbolo in cadeia:
    if simbolo not in ["0", "1"]:
        valida = False
        break

    if estado_atual == "q0":
        if simbolo == "0":
            estado_atual = "q0"
        elif simbolo == "1":
            estado_atual = "q1"

    elif estado_atual == "q1":
        if simbolo == "0":
            estado_atual = "q0"
        elif simbolo == "1":
            estado_atual = "q1"

if not valida:
    print("Cadeia inválida. Use apenas 0 e 1.")
else:
    print("Estado final:", estado_atual)

    if estado_atual == "q1":
        print("Cadeia aceita!")
    else:
        print("Cadeia rejeitada!")

