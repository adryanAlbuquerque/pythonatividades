num = []
cont = 0
for i in range(5):
    num.append(int(input("Digite um numero: ")))

for x in num:
    if x % 2 == 0:
        cont+=1
        print(x,end=" ")

print()
print(cont,end=" numeros são pares")
