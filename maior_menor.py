lista = []

print("Defina três números a seguir:\n")

for i in range(3):
    valor = int(input())

    lista.append(valor)

print(f"\nDos valores citados '{max(lista)}' é o Maior, e o '{min(lista)}' é o Menor.\n")