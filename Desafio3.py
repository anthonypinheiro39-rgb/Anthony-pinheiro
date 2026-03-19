
palavra = input("Escreva uma palavra:\n")
reverso = ""

for letra in palavra:
    reverso = letra + reverso

print(f"palavra Original:", palavra)
print(f"palavra Reversa:", reverso)

