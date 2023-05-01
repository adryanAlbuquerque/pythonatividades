numeros = []
pares = 0

for i in range (5):
    numeros.append(int(input("Digite um numero: ")))

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
print("Temos",pares,"numeros pares")