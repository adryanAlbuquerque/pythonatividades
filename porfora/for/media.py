numeros = []

soma = 0

for i in range(5):
    numeros.append(int(input("Digite um numero: ")))

for x in numeros:
    soma += x

media = soma / (len(numeros))
print(media)