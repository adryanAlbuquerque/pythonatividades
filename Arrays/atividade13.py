vetor =[]
soma = 0
contador = 0


for x in range (5):
    vetor.append(int(input("Digite um valor: ")))
    soma = soma+vetor[x]

for y in range(5):
    if vetor[y]%2 == 0:
        print(vetor[y],"é numero par")

media = soma/5

for j in range(5):
    if vetor[j] > media:
        contador=contador+1

print("A quantidade de numeros acima da media são",contador)


maior = vetor[0]
menor = vetor[0]

for h in range(5):
    if vetor[h]<menor:
        menor == vetor[h]

    if vetor[h]>maior:
        maior=vetor[h]

print("O maior numero é",h)