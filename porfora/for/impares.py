numeros = []
for i in range(5):
    numeros.append(int(input("Digite um número: ")))

for numero in numeros:
    if numero % 2 != 0:
        print(numero)