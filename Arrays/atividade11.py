a = []
contador = 0

for x in range(10):
    a.append(int(input("Digite um numero")))

num=int(input("Digite um numero que quer procurar: "))


for y in range(10):
    if num==a[y]:
        contador+=1

print("o numero",num,"aparece",contador, "vezes")