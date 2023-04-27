nota = []
soma = 0
i = 0

for x in range(5):
    nota.append(float(input("Digite uma nota: ")))

for y in range(5):
    soma += nota[y]

media=soma/5

for j in range(5):
    if nota[j]>=media:
        i+=1

print(i,"Alunos")