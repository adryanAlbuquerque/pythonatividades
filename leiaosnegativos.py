total=0

for x in range(10):
    num1 = int(input("Digite 10 numeros: "))
    if num1 < 0:
        total=total+1

print("Você digitou", total, "numeros negativos")