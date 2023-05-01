numeros = []
contador = 0

for i in range(5):
    numeros.append(int(input("Digite um número: ")))

for numero in numeros:
    if numero % 2 != 0:
        contador += 1
print("Temos",contador,"numeros ímpares")