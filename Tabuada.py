valor = int(input("Escolha um numero multiplicador para a Tabuada:\n"))

print(f"---------------\n TABUADA DO {valor}!\n---------------")

for i in range(1, 11):
    print(f"- {valor} x {i} = {valor*i}")