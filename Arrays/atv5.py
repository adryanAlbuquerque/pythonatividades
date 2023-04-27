vetorA = []
vetorM = []


for x in range(10):
    vetorA.append(int(input("Digite um numero do vetor: ")))

x = int(input("Digite um numero: "))

for y in range(10):
    vetorM.append(vetorA[y]*x)

print(vetorA)
print(x)
print(vetorM)

