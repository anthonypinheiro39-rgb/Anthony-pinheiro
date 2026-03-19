lista = []

print("\nDefina 5 valores a seguir:")

for i in range(5):
    valor = int(input())

    lista.append(valor)

print(f"-----------------------\n Estatísticas da Lista\n-----------------------")
print(f" - O Maior Valor: {max(lista)}\n - O Menor Valor: {min(lista)}\n - Soma Total: {sum(lista)}")
